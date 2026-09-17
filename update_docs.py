#!/usr/bin/env python3
"""
GHL Documentation Update Scraper
Re-scrapes all documentation from help.gohighlevel.com, detects changes
(new, updated, removed articles), and commits only the differences to Git.
Designed to be run on a weekly schedule.

Usage: python update_docs.py [--no-push] [--force]
  --no-push  commit locally but do not push, so the result can be reviewed first
  --force    commit even when the scrape came back much shorter than the last run
"""

import os
import re
import sys
import time
import json
import html
import hashlib
import subprocess
import requests
from bs4 import BeautifulSoup
import html2text

# ── Configuration ──────────────────────────────────────────────────────────
BASE_URL = "https://help.gohighlevel.com"
# The repository this script lives in, so it runs from any checkout.
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(REPO_DIR, "docs")
MANIFEST_PATH = os.path.join(REPO_DIR, "article_manifest.json")
DELAY = 0.5  # seconds between requests
# A scrape that returns fewer articles than this share of the last run is treated
# as a failed scrape (network trouble, a blocked request, a changed page layout),
# not as the help center deleting that many articles.
MIN_SCRAPED_RATIO = 0.9
NO_PUSH = '--no-push' in sys.argv
FORCE = '--force' in sys.argv

# ── HTTP Session ───────────────────────────────────────────────────────────
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

# ── Markdown converter ────────────────────────────────────────────────────
h2t = html2text.HTML2Text()
h2t.ignore_links = False
h2t.ignore_images = False
h2t.body_width = 0
h2t.protect_links = True
h2t.wrap_links = False
h2t.unicode_snob = True


# ── Utility helpers ────────────────────────────────────────────────────────
def safe_filename(name):
    name = html.unescape(name)
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', ' ', name).strip().strip('.')
    return name[:100].strip() if len(name) > 100 else name


def safe_dirname(name):
    name = html.unescape(name)
    name = re.sub(r'[<>:"/\\|?*]', '-', name)
    name = re.sub(r'\s+', '-', name).strip('-')
    name = re.sub(r'-+', '-', name).strip('.')
    return name[:80].strip('-') if len(name) > 80 else name


def content_hash(text):
    """Return a short SHA-256 hex digest for change detection."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]


def repo_path(path):
    """Repo-relative path with forward slashes, the form the manifest stores.

    os.path.relpath uses backslashes on Windows, which never match a manifest
    written on Linux: every article then looks new, every old entry looks
    removed, and the removal step deletes the files that were just written.
    """
    return os.path.relpath(path, REPO_DIR).replace(os.sep, '/')


def fetch_page(url, retries=3):
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
            time.sleep(DELAY)
            return resp.text
        except Exception as e:
            print(f"  [WARN] {url}: {e} (attempt {attempt+1}/{retries})")
            time.sleep(2 * (attempt + 1))
    return None


def run_git(*args):
    result = subprocess.run(
        ['git'] + list(args),
        cwd=REPO_DIR, capture_output=True, text=True
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


# ── Scraping functions (unchanged logic) ──────────────────────────────────
def get_categories():
    print("[1/5] Fetching categories...")
    page_html = fetch_page(f"{BASE_URL}/support/solutions")
    if not page_html:
        return []
    soup = BeautifulSoup(page_html, 'html.parser')
    categories, seen = [], set()
    for link in soup.find_all('a', href=re.compile(r'/support/solutions/\d+')):
        href = link.get('href', '')
        text = link.get_text(strip=True)
        if href and text and href not in seen and '/folders/' not in href and '/articles/' not in href:
            seen.add(href)
            full_url = BASE_URL + href if href.startswith('/') else href
            categories.append({
                'name': html.unescape(text),
                'url': full_url,
                'id': href.split('/')[-1]
            })
    print(f"  Found {len(categories)} categories")
    return categories


def get_folders_from_category(category_url):
    page_html = fetch_page(category_url)
    if not page_html:
        return []
    soup = BeautifulSoup(page_html, 'html.parser')
    folders, seen = [], set()
    for link in soup.find_all('a', href=re.compile(r'/support/solutions/folders/\d+')):
        href = link.get('href', '')
        if href and href not in seen:
            seen.add(href)
            full_url = BASE_URL + href if href.startswith('/') else href
            folders.append(full_url)
    return folders


def folder_id(url):
    match = re.search(r'/support/solutions/folders/(\d+)', url or '')
    return match.group(1) if match else None


def get_folder_info(folder_url):
    """Every article in a folder plus its subfolders, following the portal's own page links.

    The portal pages folders at /folders/<id>/page/N, 20 items a page, and
    ignores ?page=N (which just returns page 1 again). Requesting ?page=N capped
    every folder at its first 20 articles, so this walks the page links the
    pager itself renders instead.

    Folders can hold subfolders, and some subfolders are linked only from their
    parent folder's page, never from the category page (52 folders and 320
    articles on 09/16/2026). They are returned so the caller can scrape them too.
    The "(N)" count in a folder's title counts its subfolders as well as its
    articles.
    """
    all_articles, seen = [], set()
    subfolders = []
    own_id = folder_id(folder_url)
    folder_name = "Unknown"
    listed_count = None
    url, visited, page_queue = folder_url, set(), []
    while url and len(visited) < 100:
        if url in visited or (url.endswith('/page/1') and folder_url in visited):
            url = page_queue.pop(0) if page_queue else None
            continue
        visited.add(url)
        page_html = fetch_page(url)
        if not page_html:
            break
        soup = BeautifulSoup(page_html, 'html.parser')
        if len(visited) == 1:
            title_el = soup.find(class_='fw-page-title')
            if title_el:
                title_text = title_el.get_text(strip=True)
                count_match = re.search(r'\((\d+)\)\s*$', title_text)
                listed_count = int(count_match.group(1)) if count_match else None
                folder_name = re.sub(r'\s*\(\d+\)\s*$', '', title_text)
        for link in soup.find_all('a', href=re.compile(r'/support/solutions/articles/')):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            if href and href not in seen:
                seen.add(href)
                full_url = BASE_URL + href if href.startswith('/') else href
                all_articles.append({'title': html.unescape(text) if text else '', 'url': full_url})
        for link in soup.find_all('a', href=re.compile(r'/support/solutions/folders/\d+')):
            # Breadcrumbs link back up to parent folders; only children count.
            if link.find_parent(class_=re.compile('breadcrumb', re.I)) or '/page/' in link['href']:
                continue
            sub_id = folder_id(link['href'])
            sub_url = f"{BASE_URL}/support/solutions/folders/{sub_id}"
            if sub_id and sub_id != own_id and sub_url not in subfolders:
                subfolders.append(sub_url)
        # Queue every numbered page this pager links to, not just "Next": the portal
        # sometimes renders a middle page with no pager at all (page 2 of Funnels and
        # Websites on 09/17/2026), which silently ended the walk there.
        for link in soup.find_all('a', href=re.compile(r'/support/solutions/folders/\d+/page/\d+$')):
            if folder_id(link['href']) != own_id:
                continue
            href = link['href']
            page_url = BASE_URL + href if href.startswith('/') else href
            if page_url not in visited and page_url not in page_queue:
                page_queue.append(page_url)
        url = page_queue.pop(0) if page_queue else None
    if listed_count is not None and len(all_articles) + len(subfolders) < listed_count:
        print(f"  [WARN] {folder_name}: portal lists {listed_count} items, found "
              f"{len(all_articles)} articles and {len(subfolders)} subfolders")
    return folder_name, all_articles, subfolders


def scrape_article(article_url):
    page_html = fetch_page(article_url)
    if not page_html:
        return None, None
    soup = BeautifulSoup(page_html, 'html.parser')
    title = ""
    h1 = soup.find('h1')
    if h1:
        title = h1.get_text(strip=True)
    content_div = (soup.find(class_='fw-content')
                   or soup.find(class_='article-body')
                   or soup.find(class_='fr-view'))
    if not content_div:
        return title, None
    # Capture video iframes before cleanup (for video-only articles)
    video_iframes = []
    for iframe in content_div.find_all('iframe'):
        src = iframe.get('src', '')
        if any(d in src for d in ['youtube.com', 'loom.com', 'vimeo.com', 'wistia.com']):
            video_iframes.append(src)
    for el in content_div.find_all(class_=re.compile(
            r'feedback|breadcrumb|sidebar|navigation|popular-articles|pagination|fw-article-meta')):
        el.decompose()
    for tag in content_div.find_all(['script', 'style', 'noscript']):
        tag.decompose()
    markdown = h2t.handle(str(content_div))
    markdown = re.sub(r'\n{4,}', '\n\n\n', markdown).strip()
    # If no text content but video iframes exist, create video-only stub
    if not markdown and video_iframes:
        lines = ["This article consists of video content:\n"]
        for i, src in enumerate(video_iframes, 1):
            if 'youtube.com/embed/' in src:
                vid = src.split('youtube.com/embed/')[-1].split('?')[0]
                watch = f"https://www.youtube.com/watch?v={vid}"
                lines.append(f"**Video {i}:** [Watch on YouTube]({watch})")
                lines.append(f"")
                lines.append(f"Embed: `{src}`")
            elif 'loom.com/embed/' in src:
                vid = src.split('loom.com/embed/')[-1].split('?')[0]
                watch = f"https://www.loom.com/share/{vid}"
                lines.append(f"**Video {i}:** [Watch on Loom]({watch})")
                lines.append(f"")
                lines.append(f"Embed: `{src}`")
            else:
                lines.append(f"**Video {i}:** [{src}]({src})")
            lines.append("")
        markdown = "\n".join(lines)
    return title, markdown


# ── Main update logic ─────────────────────────────────────────────────────
def main():
    start_time = time.time()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Pull latest from remote first
    print("[0/5] Pulling latest from remote...")
    run_git('pull', '--rebase', 'origin', 'main')

    # Load previous manifest for change detection
    old_manifest = {}
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
            old_manifest = json.load(f)

    new_manifest = {}
    stats = {
        'categories': 0, 'folders': 0,
        'articles_found': 0, 'articles_scraped': 0, 'articles_failed': 0,
        'articles_new': 0, 'articles_updated': 0, 'articles_unchanged': 0,
        'articles_removed': 0, 'stale_files_removed': 0
    }

    # Track every file path we write so we can detect removals
    written_files = set()

    # ── Scrape ─────────────────────────────────────────────────────────
    categories = get_categories()
    stats['categories'] = len(categories)

    index_content = "# GoHighLevel Documentation\n\n"
    index_content += ("This repository contains the complete documentation from the "
                      "[GoHighLevel Support Portal](https://help.gohighlevel.com/support/solutions).\n\n")
    index_content += "## Categories\n\n"

    # Every folder a category page lists, gathered up front, so a subfolder found
    # later is only scraped once and stays under the category that lists it.
    category_folders = {c['url']: get_folders_from_category(c['url']) for c in categories}
    seen_folders = {folder_id(u) for urls in category_folders.values() for u in urls}

    for cat_idx, category in enumerate(categories):
        cat_name = category['name']
        cat_dir_name = safe_dirname(cat_name)
        cat_dir = os.path.join(OUTPUT_DIR, cat_dir_name)
        os.makedirs(cat_dir, exist_ok=True)

        print(f"\n[2/5] [{cat_idx+1}/{len(categories)}] Category: {cat_name}")

        folders = list(category_folders[category['url']])
        cat_index = f"# {cat_name}\n\n**Source:** [{category['url']}]({category['url']})\n\n## Folders\n\n"

        if not folders:
            folder_name, articles, _ = get_folder_info(category['url'])
            if articles:
                folders = [category['url']]

        queue = list(folders)
        while queue:
            folder_url = queue.pop(0)
            folder_name, articles, subfolders = get_folder_info(folder_url)
            for sub_url in subfolders:
                if folder_id(sub_url) not in seen_folders:
                    seen_folders.add(folder_id(sub_url))
                    queue.append(sub_url)
            if not articles:
                continue

            stats['folders'] += 1
            folder_dir_name = safe_dirname(folder_name)
            folder_dir = os.path.join(cat_dir, folder_dir_name)
            os.makedirs(folder_dir, exist_ok=True)

            print(f"  Folder: {folder_name} ({len(articles)} articles)")
            stats['articles_found'] += len(articles)
            cat_index += f"### [{folder_name}]({folder_dir_name}/)\n\n"

            folder_index = f"# {folder_name}\n\n**Category:** {cat_name}\n\n## Articles\n\n"

            for art_idx, article in enumerate(articles):
                art_title = article['title']
                art_url = article['url']
                print(f"    [{art_idx+1}/{len(articles)}] {art_title[:60]}...")

                title, md_content = scrape_article(art_url)
                if not title:
                    title = art_title
                if not md_content:
                    stats['articles_failed'] += 1
                    continue

                stats['articles_scraped'] += 1
                art_filename = safe_filename(title or art_title) + ".md"
                art_path = os.path.join(folder_dir, art_filename)
                rel_path = repo_path(art_path)

                article_md = (f"# {title}\n\n"
                              f"**Source URL:** [{art_url}]({art_url})  \n"
                              f"**Category:** {cat_name}  \n"
                              f"**Folder:** {folder_name}\n\n---\n\n"
                              + md_content + "\n")

                new_hash = content_hash(article_md)
                new_manifest[rel_path] = {'url': art_url, 'hash': new_hash, 'title': title}
                written_files.add(rel_path)

                # Compare with old manifest
                old_entry = old_manifest.get(rel_path)
                # An unchanged hash only means "skip the write" if the file is really there.
                if old_entry and old_entry.get('hash') == new_hash and os.path.exists(art_path):
                    stats['articles_unchanged'] += 1
                elif old_entry:
                    stats['articles_updated'] += 1
                    with open(art_path, 'w', encoding='utf-8') as f:
                        f.write(article_md)
                else:
                    stats['articles_new'] += 1
                    with open(art_path, 'w', encoding='utf-8') as f:
                        f.write(article_md)

                folder_index += f"- [{title}]({art_filename})\n"

            folder_readme = os.path.join(folder_dir, "README.md")
            with open(folder_readme, 'w', encoding='utf-8') as f:
                f.write(folder_index)
            written_files.add(repo_path(folder_readme))

        cat_readme = os.path.join(cat_dir, "README.md")
        with open(cat_readme, 'w', encoding='utf-8') as f:
            f.write(cat_index)
        written_files.add(repo_path(cat_readme))

        index_content += f"- [{cat_name}](docs/{cat_dir_name}/)\n"

        if (cat_idx + 1) % 10 == 0:
            print(f"\n--- Progress: {stats['articles_scraped']} scraped, "
                  f"{stats['articles_new']} new, {stats['articles_updated']} updated ---\n")

    # ── Refuse to act on a short scrape ────────────────────────────────
    # Every article missing from this run gets deleted below, so a scrape that
    # broke halfway would wipe real documentation. Stop before any removal,
    # manifest write, or commit when the run came back clearly short.
    previous = len(old_manifest)
    if previous and stats['articles_scraped'] < previous * MIN_SCRAPED_RATIO and not FORCE:
        print(f"\n[ABORT] Scraped {stats['articles_scraped']} articles, but the last run "
              f"had {previous}. Nothing was removed, committed, or pushed. "
              f"Re-run with --force if the help center really shrank.")
        sys.exit(1)

    # ── Detect removed articles ────────────────────────────────────────
    print("\n[3/5] Detecting removed articles...")
    to_remove = [old_path for old_path in old_manifest if old_path not in new_manifest]
    # The help center retires a handful of articles a week, not hundreds. A
    # removal list this long means the paths stopped matching (a renamed
    # category, a platform path bug), and acting on it would delete live docs.
    if previous and len(to_remove) > max(50, previous * 0.1) and not FORCE:
        print(f"\n[ABORT] This run would remove {len(to_remove)} of {previous} articles. "
              f"Nothing was removed, committed, or pushed. Check the manifest paths, "
              f"or re-run with --force if the help center really removed them.")
        sys.exit(1)
    for old_path in to_remove:
        stats['articles_removed'] += 1
        full_path = os.path.join(REPO_DIR, *old_path.split('/'))
        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"  Removed: {old_path}")

    # Files this run did not write and the manifest never tracked: copies left under an
    # article's old title or folder, and indexes for folders the help center dropped.
    stale = []
    for dirpath, _, filenames in os.walk(OUTPUT_DIR):
        for name in filenames:
            path = repo_path(os.path.join(dirpath, name))
            if name.endswith('.md') and path not in written_files:
                stale.append(path)
    if previous and len(stale) > max(50, previous * 0.1) and not FORCE:
        print(f"\n[ABORT] {len(stale)} files under docs/ were not written by this run. "
              f"Nothing else was removed, committed, or pushed. Check the paths, "
              f"or re-run with --force if they really are stale.")
        sys.exit(1)
    for path in sorted(stale):
        os.remove(os.path.join(REPO_DIR, *path.split('/')))
        stats['stale_files_removed'] += 1
        print(f"  Removed stale file: {path}")

    # Clean up empty directories
    for dirpath, dirnames, filenames in os.walk(OUTPUT_DIR, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)

    # ── Write indexes & manifest ───────────────────────────────────────
    print("[4/5] Writing indexes and manifest...")
    elapsed = time.time() - start_time
    index_content += (f"\n\n---\n\n"
                      f"*Last updated: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())} "
                      f"from the [GoHighLevel Support Portal]"
                      f"(https://help.gohighlevel.com/support/solutions).*\n\n"
                      f"**Statistics:**\n"
                      f"- Categories: {stats['categories']}\n"
                      f"- Folders: {stats['folders']}\n"
                      f"- Articles: {stats['articles_scraped']}\n")

    with open(os.path.join(REPO_DIR, "README.md"), 'w', encoding='utf-8') as f:
        f.write(index_content)

    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(new_manifest, f, indent=2)

    with open(os.path.join(REPO_DIR, "scrape_stats.json"), 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)

    # ── Git commit & push ──────────────────────────────────────────────
    print("[5/5] Committing and pushing changes...")
    run_git('add', '-A')

    # Check if there are actual changes
    rc, diff_out, _ = run_git('diff', '--cached', '--stat')
    if not diff_out:
        print("No changes detected — nothing to commit.")
        return

    changes_summary = (
        f"Weekly docs update {time.strftime('%Y-%m-%d')}\n\n"
        f"- New articles: {stats['articles_new']}\n"
        f"- Updated articles: {stats['articles_updated']}\n"
        f"- Removed articles: {stats['articles_removed']}\n"
        f"- Stale files removed: {stats['stale_files_removed']}\n"
        f"- Unchanged articles: {stats['articles_unchanged']}\n"
        f"- Failed to scrape: {stats['articles_failed']}\n"
        f"- Total articles: {stats['articles_scraped']}\n"
        f"- Scrape duration: {elapsed/60:.1f} minutes"
    )

    run_git('commit', '-m', changes_summary)
    if NO_PUSH:
        print("  Committed locally; --no-push given, so nothing was pushed.")
    else:
        rc, out, err = run_git('push', 'origin', 'main')
        if rc != 0:
            print(f"  [ERROR] Push failed: {err}")
        else:
            print(f"  Push successful.")

    # ── Summary ────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"UPDATE COMPLETE  ({elapsed/60:.1f} minutes)")
    print(f"  Categories : {stats['categories']}")
    print(f"  Folders    : {stats['folders']}")
    print(f"  Found      : {stats['articles_found']}")
    print(f"  Scraped    : {stats['articles_scraped']}")
    print(f"  New        : {stats['articles_new']}")
    print(f"  Updated    : {stats['articles_updated']}")
    print(f"  Unchanged  : {stats['articles_unchanged']}")
    print(f"  Removed    : {stats['articles_removed']}")
    print(f"  Stale      : {stats['stale_files_removed']}")
    print(f"  Failed     : {stats['articles_failed']}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

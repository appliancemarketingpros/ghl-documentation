#!/usr/bin/env python3
"""
Recovery script for failed GHL documentation articles.
1. Re-scrapes all 1808 articles to find the ~48 that are missing from the manifest
2. For video-only articles: creates markdown stubs with embedded video links
3. For transient failures: retries with longer timeouts and more attempts
4. Commits and pushes recovered articles
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
REPO_DIR = "/home/ubuntu/ghl-documentation"
OUTPUT_DIR = os.path.join(REPO_DIR, "docs")
MANIFEST_PATH = os.path.join(REPO_DIR, "article_manifest.json")
DELAY = 0.5

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
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]

def fetch_page(url, retries=4):
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=45)
            resp.raise_for_status()
            time.sleep(DELAY)
            return resp.text
        except Exception as e:
            print(f"    [WARN] {url}: {e} (attempt {attempt+1}/{retries})")
            time.sleep(3 * (attempt + 1))
    return None

def run_git(*args):
    result = subprocess.run(
        ['git'] + list(args),
        cwd=REPO_DIR, capture_output=True, text=True
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def get_categories():
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
            categories.append({'name': html.unescape(text), 'url': full_url})
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

def get_folder_info(folder_url):
    all_articles, seen = [], set()
    folder_name = "Unknown"
    page = 1
    while True:
        url = folder_url if page == 1 else f"{folder_url}?page={page}"
        page_html = fetch_page(url)
        if not page_html:
            break
        soup = BeautifulSoup(page_html, 'html.parser')
        if page == 1:
            title_el = soup.find(class_='fw-page-title')
            if title_el:
                folder_name = re.sub(r'\s*\(\d+\)\s*$', '', title_el.get_text(strip=True))
        new_articles = []
        for link in soup.find_all('a', href=re.compile(r'/support/solutions/articles/')):
            href = link.get('href', '')
            text = link.get_text(strip=True)
            if href and href not in seen:
                seen.add(href)
                full_url = BASE_URL + href if href.startswith('/') else href
                new_articles.append({'title': html.unescape(text) if text else '', 'url': full_url})
        if not new_articles:
            break
        all_articles.extend(new_articles)
        if len(new_articles) < 20:
            break
        page += 1
    return folder_name, all_articles

def scrape_article_enhanced(article_url):
    """Enhanced scraper that handles video-only articles."""
    page_html = fetch_page(article_url)
    if not page_html:
        return None, None, "fetch_failed"
    
    soup = BeautifulSoup(page_html, 'html.parser')
    
    title = ""
    h1 = soup.find('h1')
    if h1:
        title = h1.get_text(strip=True)
    
    content_div = (soup.find(class_='fw-content')
                   or soup.find(class_='article-body')
                   or soup.find(class_='fr-view'))
    
    if not content_div:
        return title, None, "no_content_div"
    
    # Check for iframes BEFORE removing elements
    iframes = content_div.find_all('iframe')
    video_iframes = []
    for iframe in iframes:
        src = iframe.get('src', '')
        if any(domain in src for domain in ['youtube.com', 'loom.com', 'vimeo.com', 'wistia.com']):
            video_iframes.append(src)
    
    # Clean up non-content elements
    for el in content_div.find_all(class_=re.compile(
            r'feedback|breadcrumb|sidebar|navigation|popular-articles|pagination|fw-article-meta')):
        el.decompose()
    for tag in content_div.find_all(['script', 'style', 'noscript']):
        tag.decompose()
    
    markdown = h2t.handle(str(content_div))
    markdown = re.sub(r'\n{4,}', '\n\n\n', markdown).strip()
    
    # If markdown is empty but we have video iframes, create video-only content
    if not markdown and video_iframes:
        video_lines = ["This article consists of video content:\n"]
        for i, src in enumerate(video_iframes, 1):
            # Convert embed URLs to watch URLs for better UX
            watch_url = src
            if 'youtube.com/embed/' in src:
                video_id = src.split('youtube.com/embed/')[-1].split('?')[0]
                watch_url = f"https://www.youtube.com/watch?v={video_id}"
                video_lines.append(f"**Video {i}:** [Watch on YouTube]({watch_url})")
                video_lines.append(f"")
                video_lines.append(f"Embed: `{src}`")
            elif 'loom.com/embed/' in src:
                video_id = src.split('loom.com/embed/')[-1].split('?')[0]
                watch_url = f"https://www.loom.com/share/{video_id}"
                video_lines.append(f"**Video {i}:** [Watch on Loom]({watch_url})")
                video_lines.append(f"")
                video_lines.append(f"Embed: `{src}`")
            else:
                video_lines.append(f"**Video {i}:** [{src}]({src})")
            video_lines.append("")
        
        markdown = "\n".join(video_lines)
        return title, markdown, "video_only"
    
    if not markdown:
        return title, None, "empty_content"
    
    return title, markdown, "success"


def main():
    start_time = time.time()
    
    # Load current manifest
    with open(MANIFEST_PATH, 'r') as f:
        manifest = json.load(f)
    
    manifest_urls = {v['url'] for v in manifest.values()}
    
    print("=" * 70)
    print("RECOVERY: Finding and fixing failed articles")
    print("=" * 70)
    
    # Phase 1: Discover all articles
    print("\n[1/4] Discovering all articles from portal...")
    categories = get_categories()
    print(f"  Found {len(categories)} categories")
    
    all_articles = []  # (category_name, folder_name, title, url)
    
    for cat_idx, cat in enumerate(categories):
        cat_name = cat['name']
        folders = get_folders_from_category(cat['url'])
        if not folders:
            folder_name, articles = get_folder_info(cat['url'])
            if articles:
                folders = [cat['url']]
        
        for folder_url in folders:
            folder_name, articles = get_folder_info(folder_url)
            for art in articles:
                all_articles.append({
                    'category': cat_name,
                    'folder': folder_name,
                    'title': art['title'],
                    'url': art['url']
                })
        
        if (cat_idx + 1) % 10 == 0:
            print(f"  Progress: {cat_idx+1}/{len(categories)} categories, {len(all_articles)} articles")
    
    print(f"  Total articles found: {len(all_articles)}")
    
    # Phase 2: Identify missing articles
    print("\n[2/4] Identifying articles missing from manifest...")
    missing = [a for a in all_articles if a['url'] not in manifest_urls]
    print(f"  Missing articles: {len(missing)}")
    
    if not missing:
        print("  No missing articles found! All articles are in the manifest.")
        return
    
    # Phase 3: Scrape missing articles with enhanced handler
    print(f"\n[3/4] Scraping {len(missing)} missing articles with enhanced handler...")
    
    recovered = {'video_only': [], 'text_content': [], 'still_failed': []}
    
    for i, art in enumerate(missing):
        print(f"\n  [{i+1}/{len(missing)}] {art['title'][:60]}")
        print(f"    Category: {art['category']} > {art['folder']}")
        
        title, md_content, status = scrape_article_enhanced(art['url'])
        if not title:
            title = art['title']
        
        print(f"    Status: {status}")
        
        if md_content:
            # Write the file
            cat_dir_name = safe_dirname(art['category'])
            folder_dir_name = safe_dirname(art['folder'])
            cat_dir = os.path.join(OUTPUT_DIR, cat_dir_name)
            folder_dir = os.path.join(cat_dir, folder_dir_name)
            os.makedirs(folder_dir, exist_ok=True)
            
            art_filename = safe_filename(title or art['title']) + ".md"
            art_path = os.path.join(folder_dir, art_filename)
            rel_path = os.path.relpath(art_path, REPO_DIR)
            
            article_md = (f"# {title}\n\n"
                          f"**Source URL:** [{art['url']}]({art['url']})  \n"
                          f"**Category:** {art['category']}  \n"
                          f"**Folder:** {art['folder']}\n\n---\n\n"
                          + md_content + "\n")
            
            with open(art_path, 'w', encoding='utf-8') as f:
                f.write(article_md)
            
            # Update manifest
            new_hash = content_hash(article_md)
            manifest[rel_path] = {'url': art['url'], 'hash': new_hash, 'title': title}
            
            if status == 'video_only':
                recovered['video_only'].append({'title': title, 'url': art['url'], 'path': rel_path})
                print(f"    RECOVERED (video-only): {rel_path}")
            else:
                recovered['text_content'].append({'title': title, 'url': art['url'], 'path': rel_path})
                print(f"    RECOVERED (text): {rel_path}")
        else:
            recovered['still_failed'].append({
                'title': title or art['title'], 
                'url': art['url'], 
                'reason': status,
                'category': art['category'],
                'folder': art['folder']
            })
            print(f"    STILL FAILED: {status}")
    
    # Save updated manifest
    with open(MANIFEST_PATH, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    # Phase 4: Commit and push
    total_recovered = len(recovered['video_only']) + len(recovered['text_content'])
    still_failed = len(recovered['still_failed'])
    
    print(f"\n[4/4] Committing and pushing recovered articles...")
    run_git('add', '-A')
    
    rc, diff_out, _ = run_git('diff', '--cached', '--stat')
    if not diff_out:
        print("  No changes to commit.")
    else:
        elapsed = time.time() - start_time
        commit_msg = (
            f"Recover {total_recovered} previously failed articles\n\n"
            f"- Video-only articles recovered: {len(recovered['video_only'])}\n"
            f"- Text articles recovered (transient errors): {len(recovered['text_content'])}\n"
            f"- Still failed: {still_failed}\n"
            f"- Recovery duration: {elapsed/60:.1f} minutes"
        )
        run_git('commit', '-m', commit_msg)
        rc, out, err = run_git('push', 'origin', 'main')
        if rc != 0:
            print(f"  [ERROR] Push failed: {err}")
        else:
            print(f"  Push successful.")
    
    # Summary
    elapsed = time.time() - start_time
    print(f"\n{'='*70}")
    print(f"RECOVERY COMPLETE ({elapsed/60:.1f} minutes)")
    print(f"{'='*70}")
    print(f"  Video-only articles recovered: {len(recovered['video_only'])}")
    for a in recovered['video_only']:
        print(f"    + {a['title'][:60]}")
    print(f"  Text articles recovered:       {len(recovered['text_content'])}")
    for a in recovered['text_content']:
        print(f"    + {a['title'][:60]}")
    print(f"  Still failed:                  {still_failed}")
    for a in recovered['still_failed']:
        print(f"    x {a['title'][:60]} ({a['reason']})")
    print(f"{'='*70}")
    
    # Save recovery report
    report = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()),
        'duration_minutes': round(elapsed / 60, 1),
        'recovered': recovered,
        'total_recovered': total_recovered,
        'still_failed': still_failed
    }
    with open(os.path.join(REPO_DIR, 'recovery_report.json'), 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nDetailed report saved to recovery_report.json")


if __name__ == '__main__':
    main()

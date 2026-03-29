#!/usr/bin/env python3
"""
Diagnose which articles failed during the scrape and why.
Re-scrapes all article URLs, identifies the 48 that have no content,
and categorizes the failure reasons.
"""

import os
import re
import sys
import time
import json
import html
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://help.gohighlevel.com"
REPO_DIR = "/home/ubuntu/ghl-documentation"
MANIFEST_PATH = os.path.join(REPO_DIR, "article_manifest.json")
DELAY = 0.5

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

# Load manifest to know what was successfully scraped
with open(MANIFEST_PATH) as f:
    manifest = json.load(f)

scraped_urls = {v['url'] for v in manifest.values()}

def fetch_page(url, retries=2):
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=30)
            return resp.status_code, resp.text
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                return None, str(e)
    return None, "max retries"

def get_categories():
    status, page_html = fetch_page(f"{BASE_URL}/support/solutions")
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
    status, page_html = fetch_page(category_url)
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

def get_folder_articles(folder_url):
    all_articles, seen = [], set()
    folder_name = "Unknown"
    page = 1
    while True:
        url = folder_url if page == 1 else f"{folder_url}?page={page}"
        status, page_html = fetch_page(url)
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

# Phase 1: Collect all article URLs from the portal
print("=" * 70)
print("PHASE 1: Collecting all article URLs from the portal...")
print("=" * 70)

all_articles = []
categories = get_categories()
print(f"Found {len(categories)} categories\n")

for cat_idx, cat in enumerate(categories):
    folders = get_folders_from_category(cat['url'])
    if not folders:
        folder_name, articles = get_folder_articles(cat['url'])
        if articles:
            folders = [cat['url']]
    
    for folder_url in folders:
        folder_name, articles = get_folder_articles(folder_url)
        for art in articles:
            all_articles.append({
                'category': cat['name'],
                'folder': folder_name,
                'title': art['title'],
                'url': art['url']
            })
    
    if (cat_idx + 1) % 10 == 0:
        print(f"  Progress: {cat_idx+1}/{len(categories)} categories, {len(all_articles)} articles found")

print(f"\nTotal articles found in portal: {len(all_articles)}")
print(f"Total articles in manifest (successfully scraped): {len(manifest)}")

# Phase 2: Identify which articles are missing from the manifest
print("\n" + "=" * 70)
print("PHASE 2: Identifying failed articles...")
print("=" * 70)

failed_articles = []
for art in all_articles:
    if art['url'] not in scraped_urls:
        failed_articles.append(art)

print(f"\nFound {len(failed_articles)} articles NOT in the manifest\n")

# Phase 3: Diagnose each failed article
print("=" * 70)
print("PHASE 3: Diagnosing each failed article...")
print("=" * 70)

failure_reasons = {
    'http_error': [],
    'no_content_div': [],
    'empty_content': [],
    'redirect': [],
    'timeout': [],
    'other': []
}

for i, art in enumerate(failed_articles):
    url = art['url']
    print(f"\n[{i+1}/{len(failed_articles)}] {art['title'][:60]}")
    print(f"  URL: {url}")
    print(f"  Category: {art['category']} > {art['folder']}")
    
    time.sleep(DELAY)
    
    try:
        resp = session.get(url, timeout=30, allow_redirects=True)
        status_code = resp.status_code
        final_url = resp.url
        
        print(f"  HTTP Status: {status_code}")
        if final_url != url:
            print(f"  Redirected to: {final_url}")
        
        if status_code != 200:
            art['reason'] = f"HTTP {status_code}"
            failure_reasons['http_error'].append(art)
            continue
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # Check for the content div
        content_div = (soup.find(class_='fw-content')
                      or soup.find(class_='article-body')
                      or soup.find(class_='fr-view'))
        
        if not content_div:
            # Investigate what IS on the page
            page_title = soup.find('title')
            h1 = soup.find('h1')
            body_classes = []
            body = soup.find('body')
            if body:
                body_classes = body.get('class', [])
            
            # Check for common page structures
            all_divs = soup.find_all('div', class_=True)
            div_classes = set()
            for d in all_divs:
                for c in d.get('class', []):
                    div_classes.add(c)
            
            # Look for any content-like divs
            content_candidates = [c for c in div_classes if any(
                kw in c.lower() for kw in ['content', 'article', 'body', 'main', 'text']
            )]
            
            art['reason'] = "No fw-content/article-body/fr-view div found"
            art['page_title'] = page_title.get_text(strip=True) if page_title else "N/A"
            art['h1'] = h1.get_text(strip=True) if h1 else "N/A"
            art['content_candidates'] = content_candidates[:10]
            art['page_size'] = len(resp.text)
            
            print(f"  FAILURE: No content div found")
            print(f"  Page title: {art['page_title']}")
            print(f"  H1: {art['h1']}")
            print(f"  Page size: {art['page_size']} bytes")
            print(f"  Content-like classes: {content_candidates[:5]}")
            
            failure_reasons['no_content_div'].append(art)
        else:
            # Content div exists but might be empty
            text = content_div.get_text(strip=True)
            if not text:
                art['reason'] = "Content div exists but is empty"
                print(f"  FAILURE: Content div found but empty")
                failure_reasons['empty_content'].append(art)
            else:
                art['reason'] = "Content exists - may have been a transient error"
                art['content_length'] = len(text)
                print(f"  RECOVERABLE: Content found ({len(text)} chars) - was likely a transient error")
                failure_reasons['other'].append(art)
                
    except requests.exceptions.Timeout:
        art['reason'] = "Request timed out"
        print(f"  FAILURE: Timeout")
        failure_reasons['timeout'].append(art)
    except Exception as e:
        art['reason'] = str(e)
        print(f"  FAILURE: {e}")
        failure_reasons['other'].append(art)

# Phase 4: Summary report
print("\n\n" + "=" * 70)
print("DIAGNOSIS SUMMARY")
print("=" * 70)
print(f"\nTotal failed articles: {len(failed_articles)}")
print(f"\nBreakdown by failure reason:")
for reason, articles in failure_reasons.items():
    if articles:
        print(f"\n  {reason}: {len(articles)}")
        for a in articles[:5]:
            print(f"    - {a['title'][:70]}")
            print(f"      URL: {a['url']}")
            print(f"      Reason: {a.get('reason', 'unknown')}")
        if len(articles) > 5:
            print(f"    ... and {len(articles) - 5} more")

# Save detailed report
report = {
    'total_portal_articles': len(all_articles),
    'total_manifest_articles': len(manifest),
    'total_failed': len(failed_articles),
    'failure_breakdown': {k: len(v) for k, v in failure_reasons.items()},
    'failed_articles': failed_articles,
    'failure_details': {k: v for k, v in failure_reasons.items() if v}
}

with open('/home/ubuntu/ghl-documentation/failure_report.json', 'w') as f:
    json.dump(report, f, indent=2, default=str)

print(f"\nDetailed report saved to failure_report.json")

# Identify recoverable articles
recoverable = failure_reasons.get('other', [])
print(f"\nRecoverable articles (content available on retry): {len(recoverable)}")

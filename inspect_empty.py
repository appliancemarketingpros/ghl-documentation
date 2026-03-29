#!/usr/bin/env python3
"""
Deep inspection of the 10 articles with empty content divs.
Saves raw HTML and analyzes the page structure to find where content actually lives.
"""

import os
import re
import time
import json
import requests
from bs4 import BeautifulSoup

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

# The 10 empty-content articles
empty_articles = [
    {"title": "Mailgun - Unsubscribe Settings", "url": "https://help.gohighlevel.com/support/solutions/articles/48000981683-mailgun-unsubscribe-settings"},
    {"title": "Understanding The Create New Opportunity Toggle", "url": "https://help.gohighlevel.com/support/solutions/articles/48001077359-understanding-the-create-new-opportunity-toggle"},
    {"title": "Sticky Contact - Two-Step Order Form", "url": "https://help.gohighlevel.com/support/solutions/articles/48000980319-sticky-contact-two-step-order-form"},
    {"title": "Add Custom Values To Buttons In Funnel Builder", "url": "https://help.gohighlevel.com/support/solutions/articles/48001146374-add-custom-values-to-buttons-in-funnel-builder"},
    {"title": "Exporting Form answers to Google Sheets", "url": "https://help.gohighlevel.com/support/solutions/articles/48000979918-exporting-form-answers-to-google-sheets"},
    {"title": "No Slide Button in Survey", "url": "https://help.gohighlevel.com/support/solutions/articles/48001175185-no-slide-button-in-survey"},
    {"title": "Exporting Survey Answers to Google Sheets", "url": "https://help.gohighlevel.com/support/solutions/articles/48000979917-exporting-survey-answers-to-google-sheets"},
    {"title": "Instant Redirect Page - Funnel Troubleshooting", "url": "https://help.gohighlevel.com/support/solutions/articles/48000980323-instant-redirect-page-funnel-troubleshooting"},
    {"title": "When rescheduling link is blank", "url": "https://help.gohighlevel.com/support/solutions/articles/48001208024-when-rescheduling-link-is-blank-when-sending-email-sms-in-conversation"},
    {"title": "How To Set Up A PayPal Integration", "url": "https://help.gohighlevel.com/support/solutions/articles/48001204158-how-to-set-up-a-paypal-integration"},
]

os.makedirs('/home/ubuntu/ghl-documentation/debug_html', exist_ok=True)

for i, art in enumerate(empty_articles):
    print(f"\n{'='*70}")
    print(f"[{i+1}/10] {art['title']}")
    print(f"URL: {art['url']}")
    print(f"{'='*70}")
    
    resp = session.get(art['url'], timeout=30)
    html_text = resp.text
    
    # Save raw HTML
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', art['title'])[:50]
    with open(f'/home/ubuntu/ghl-documentation/debug_html/{safe_name}.html', 'w') as f:
        f.write(html_text)
    
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # Check page title
    title_tag = soup.find('title')
    print(f"  Page title: {title_tag.get_text(strip=True) if title_tag else 'N/A'}")
    
    # Check H1
    h1 = soup.find('h1')
    print(f"  H1: {h1.get_text(strip=True) if h1 else 'N/A'}")
    
    # Check for fw-content
    fw_content = soup.find(class_='fw-content')
    if fw_content:
        inner_html = str(fw_content)
        text_content = fw_content.get_text(strip=True)
        print(f"  fw-content found: {len(inner_html)} bytes HTML, {len(text_content)} chars text")
        if len(inner_html) < 500:
            print(f"  fw-content HTML:\n    {inner_html[:500]}")
    else:
        print(f"  fw-content: NOT FOUND")
    
    # Check for article-body
    article_body = soup.find(class_='article-body')
    if article_body:
        print(f"  article-body found: {len(article_body.get_text(strip=True))} chars")
    
    # Check for fr-view
    fr_view = soup.find(class_='fr-view')
    if fr_view:
        print(f"  fr-view found: {len(fr_view.get_text(strip=True))} chars")
    
    # Check for any iframes (content might be in an iframe)
    iframes = soup.find_all('iframe')
    if iframes:
        print(f"  iframes found: {len(iframes)}")
        for iframe in iframes:
            print(f"    src: {iframe.get('src', 'N/A')[:100]}")
    
    # Check for JavaScript-rendered content indicators
    scripts = soup.find_all('script')
    js_content_hints = []
    for script in scripts:
        text = script.string or ''
        if 'article' in text.lower() or 'content' in text.lower():
            # Look for JSON data or content loading patterns
            if 'articleBody' in text or 'article_body' in text or '"body"' in text:
                js_content_hints.append(text[:200])
    if js_content_hints:
        print(f"  JS content hints found: {len(js_content_hints)}")
        for hint in js_content_hints[:2]:
            print(f"    {hint[:150]}...")
    
    # Check for meta tags that might indicate article status
    meta_robots = soup.find('meta', attrs={'name': 'robots'})
    if meta_robots:
        print(f"  meta robots: {meta_robots.get('content', 'N/A')}")
    
    # Check for "article not found" or "deprecated" messages
    body_text = soup.get_text()
    for keyword in ['not found', 'deprecated', 'removed', 'archived', 'deleted', 'moved', 'redirect', 'no longer']:
        if keyword.lower() in body_text.lower():
            # Find the context
            idx = body_text.lower().find(keyword.lower())
            context = body_text[max(0,idx-50):idx+100].strip()
            print(f"  Found keyword '{keyword}': ...{context}...")
            break
    
    # Check for any visible text content on the page
    # Remove script/style content
    for tag in soup.find_all(['script', 'style', 'noscript']):
        tag.decompose()
    visible_text = soup.get_text(separator=' ', strip=True)
    print(f"  Total visible text: {len(visible_text)} chars")
    
    # Look at the article container structure
    article_container = soup.find(class_='fw-article')
    if article_container:
        children = article_container.find_all(recursive=False)
        print(f"  fw-article children: {[c.get('class', c.name) for c in children[:10]]}")
    
    # Check for data attributes that might contain content
    data_elements = soup.find_all(attrs={"data-article-body": True})
    if data_elements:
        print(f"  data-article-body elements: {len(data_elements)}")
    
    print(f"  Page size: {len(html_text)} bytes")
    
    time.sleep(0.5)

print("\n\nDone. Raw HTML files saved to debug_html/")

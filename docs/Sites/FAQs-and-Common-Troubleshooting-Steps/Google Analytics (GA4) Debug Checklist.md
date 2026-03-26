# Google Analytics (GA4) Debug Checklist

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007449-google-analytics-ga4-debug-checklist](https://help.gohighlevel.com/support/solutions/articles/155000007449-google-analytics-ga4-debug-checklist)  
**Category:** Sites  
**Folder:** FAQs and Common Troubleshooting Steps

---

## Purpose

This checklist helps you verify that your Google Analytics (GA4) tag and events are properly installed and sending data from your funnel pages before contacting support.

* * *

## 1\. Check if the Google Tag Is Installed

**Step 1:** Open your funnel page in Google Chrome.  
**Step 2:** Right-click on the page and click **Inspect**.  
**Step 3:** Go to the **Network** tab.  
**Step 4:** Refresh the page.  
**Step 5:** In the search/filter bar, type:

  * `gtag/js`

  * `collect`


Look for requests such as:

  * `google-analytics.com/collect`

  * `google.com/ccm/collect`


**If you see these requests:**  
Your Google tag is installed and sending data.

**If you do not see them:**  
The tag may not be added correctly, or it may be blocked.

* * *

## 2\. Use Google Tag Assistant (Recommended)

**Step 1:** Go to Google Tag Assistant.  
**Step 2:** Enter your funnel domain.  
**Step 3:** Start a debug session.  
**Step 4:** Reload your funnel page.

Check for:

  * A `page_view` event

  * Any custom events you expect (e.g., form submission, button click)


**If events appear:**  
Your tag is firing correctly on the page.

**If no events appear:**  
Your tag may not be configured properly.

* * *

## 3\. Confirm Data in GA4 Realtime

**Step 1:** Log in to your Google Analytics account.  
**Step 2:** Select the correct GA4 property.  
**Step 3:** Go to **Reports → Realtime**.  
**Step 4:** Visit your funnel page or trigger the event.

**If you see your visit or event in Realtime:**  
Data is successfully reaching GA4.

**If you do not see it:**  
Possible reasons include:

  * Incorrect Measurement ID

  * Tag installed on a different domain

  * Property mismatch

  * Data filters blocking traffic


* * *

## 4\. Check for Browser Errors

Open **Inspect → Console** and look for errors such as:

  * `gtag is not defined`

  * Script blocked errors

  * Content Security Policy (CSP) errors


If you see errors, they may prevent tracking from working correctly.

* * *

## When to Contact Support

Please contact support if:

  * The tag appears installed but events are not firing

  * Events fire in Tag Assistant but do not appear in GA4

  * You see script or blocking errors you cannot resolve

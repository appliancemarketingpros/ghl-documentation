# Why Tracking Code doesn't get copied on copying a page?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008756-why-tracking-code-doesn-t-get-copied-on-copying-a-page-](https://help.gohighlevel.com/support/solutions/articles/155000008756-why-tracking-code-doesn-t-get-copied-on-copying-a-page-)  
**Category:** Sites  
**Folder:** Funnels and Websites

---

Funnels & Websites • Tracking Code • Page Cloning

Why Tracking Code Is Not Copied When You Clone a Page

When you copy a funnel step or website page, page-level tracking code is intentionally excluded from the copied page. This prevents old pixels, analytics scripts, or page-specific events from being carried into the wrong page. This guide explains why that happens, how page-level and site-wide tracking differ, and how to add the correct tracking code after cloning.

What You'll Learn

Learn what happens to tracking code when a page is copied, why the code is excluded, when to use page-level versus site-wide tracking, and how to safely restore and test tracking on the copied page.

Important

Before manually adding tracking code to a copied page, check whether the same script is already configured at the funnel or website level. Adding the same tracking script at both levels can cause duplicate pageviews, events, or conversions.

Table of Contents

1\. What Happens to Tracking Code When You Copy a Page?  
2\. Key Benefits of Excluding Page-Level Tracking Code  
3\. Why Tracking Code Is Not Copied  
4\. Page-Level vs. Site-Wide Tracking Code  
5\. How To Add Tracking Code After Copying a Page  
6\. How To Verify Tracking Is Working  
7\. Troubleshooting Missing or Duplicate Tracking  
8\. Frequently Asked Questions  
9\. Related Articles

1

# What Happens to Tracking Code When You Copy a Page?

When a funnel step or website page contains tracking code added directly to that page, copying the page does not copy that page-level tracking code. The page design and supported page content can be duplicated, but the copied page starts without the original page's tracking script.

For example, the original page below contains a page-specific analytics script in its Tracking Code area.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081029222/original/i_eR3Iwq2i35nxE180ABqYp4s-VcRT_lhw.png?1789535427)

After that page is copied, the duplicated page appears alongside the original page.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081029230/original/M_KcSDGugj1VSLh5ym_qCdW9V-7hDrCIOQ.png?1789535441)

When the copied page's page-level Tracking Code area is opened, the original page-specific code is not carried over.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081029239/original/38afvBA0NIFnvGFwzn-fKqJ1HafWpkzDYQ.png?1789535451)

2

## Key Benefits of Excluding Page-Level Tracking Code

Keeping page-level tracking code out of copied pages gives you a chance to verify that the destination page should use the same tracking configuration before any analytics or advertising events begin firing.

  * **Prevents Duplicate Events:** Helps avoid accidentally firing the same pageview or conversion script more than once.
  * **Protects Page-Specific Tracking:** Prevents scripts intended for one page from automatically running on another.
  * **Reduces Incorrect Attribution:** Helps keep analytics and advertising events tied to the intended page or funnel step.
  * **Safer Sharing:** Reduces the chance of account-specific pixels or tracking IDs being unintentionally carried when pages are copied or shared.
  * **Encourages Intentional Setup:** Gives you an opportunity to choose whether tracking belongs at the page level or across the entire funnel or website.


3

## Why Tracking Code Is Not Copied

Page-level tracking scripts are often tied to a specific page, campaign, conversion event, analytics property, advertising account, or business. Automatically carrying those scripts into a copied page can cause inaccurate reporting or expose tracking configuration where it was not intended to be used.

This is especially important when a page is reused in another funnel, website, location, or agency. The copied page should be reviewed and assigned the correct tracking configuration for its new purpose.

4

## Page-Level vs. Site-Wide Tracking Code

Choosing the correct tracking level helps prevent unnecessary duplication. Use page-level tracking when the script should run only on one page, and site-wide tracking when the same script should run across the entire funnel or website.

Tracking Type| Best For| Where It Is Added  
---|---|---  
**Page-Level Tracking**|  Scripts or events that should run only on a specific funnel step or website page.| Open the page in the builder and use the Tracking Code/code icon to access Header Tracking or Footer Tracking.  
**Site-Wide Tracking**|  Scripts that should run across all pages or steps in the selected funnel or website.| Open the funnel or website Settings and use the Head tracking code or Body tracking code fields.  
  
**Example:** A general Google Analytics or Meta Pixel base script may be appropriate at the funnel or website level when it should run on every page. A conversion event that should fire only on a thank-you page may be better suited to that individual page.

5

## How To Add Tracking Code After Copying a Page

Re-add tracking only after confirming what the copied page should measure. This prevents the new page from inheriting a tracking ID, conversion event, or script that belongs to the original page.

### Add Tracking to One Page

  1. Go to **Sites**.
  2. Open **Funnels** or **Websites** , depending on where the copied page is located.
  3. Open the funnel or website containing the copied page.
  4. Open the copied page in the builder.
  5. Click the **Tracking Code** or code icon in the builder.
  6. Paste the appropriate page-specific script into **Header Tracking** or **Footer Tracking** , depending on the script provider's instructions.
  7. Click **Save**.
  8. Preview and test the page before sending live traffic to it.


### Add Tracking Across the Entire Funnel or Website

  1. Open the applicable funnel or website.
  2. Open its **Settings**.
  3. Locate **Head tracking code** or **Body tracking code**.
  4. Paste the tracking script into the location required by the provider.
  5. Save the changes.
  6. Verify the script on the published pages that should use it.


**Avoid duplicate placement:** If the same base tracking script already exists in the funnel or website settings, do not automatically add another copy of it at the page level. Add only the page-specific event code required for that page, if applicable.

6

## How To Verify Tracking Is Working

Testing after copying a page confirms that the correct script is running on the correct destination and that events are not being recorded more than once.

  1. Save and publish the copied page when it is ready for testing.
  2. Open the published page in a new browser session.
  3. Complete the action you expect to track, such as viewing the page, submitting a form, or reaching a confirmation page.
  4. Use the analytics or advertising provider's testing tool, when available, to confirm that the expected event was received.
  5. Check that the event is associated with the correct page or URL.
  6. Confirm that the event fires only the intended number of times.
  7. Use browser developer tools and network activity if additional troubleshooting is required.


**Tracking code may not appear in static page source.** Head and body tracking code can be injected dynamically in the browser. When validating a script, use the provider's testing tools or browser network activity instead of relying only on View Page Source.

7

## Troubleshooting Missing or Duplicate Tracking

Missing data and duplicate events usually come from where the script is installed, whether the copied page has been configured, or whether the same code exists at multiple tracking levels.

Issue| What To Check  
---|---  
Tracking disappeared after copying a page| This is expected for page-level tracking. Open the copied page and add the correct page-specific script if it is still required.  
The copied page records no analytics events| Check both the copied page's Tracking Code area and the funnel or website Settings to confirm where the script is installed.  
Events fire twice| Check whether the same script is installed at both the page level and the funnel or website level.  
The wrong conversion fires on the cloned page| Confirm that the copied page uses the correct event code, tracking ID, analytics property, pixel, and destination URL.  
Code does not appear in View Page Source| Tracking code can be injected dynamically. Test with browser network tools or the tracking provider's diagnostic tools instead.  
Custom code affects page rendering| Temporarily remove custom code, page-level tracking code, and custom CSS to isolate the script causing the issue.  
  
8

## Frequently Asked Questions

Q: Does page-level tracking code copy when I duplicate a funnel step or website page?

No. Page-level tracking code is intentionally excluded from the copied page.

Q: Do I always need to add the tracking script again?

No. First check whether the script is already configured at the funnel or website level. If it is site-wide, the copied page may already receive the required base tracking without another page-level copy.

Q: Can I use page-level tracking for a conversion or thank-you page?

Yes. Page-level tracking is useful when an event or script should run only on a specific page rather than across the entire funnel or website.

Q: Can I configure Google Analytics or Meta Pixel site-wide instead?

Yes. If the base script should run on every page, use the funnel or website tracking settings. Add page-specific events separately only where they are required.

Q: Why am I seeing duplicate events after adding the code back?

Check whether the same tracking script is installed both site-wide and on the individual page. Duplicate installations can cause the same event to fire more than once.

Q: Why can't I find my tracking script in the page source?

Tracking code can be injected dynamically by the browser. Use your analytics provider's testing tools or browser developer tools to confirm whether the script and events are running.

Q: Does copying a page also copy its analytics history?

No. A copied page is a separate page or step. Historical statistics from the source page are not transferred to the new page.

### Related Articles

  * [ Websites Overview: Build and Publish Sites in HighLevel ](<https://help.gohighlevel.com/support/solutions/articles/155000001633-websites-overview>)
  * [ Importing and Cloning Funnels & Websites ](<https://help.gohighlevel.com/support/solutions/articles/48001076117-import-and-or-cloning-funnels-websites>)
  * [ Record Pageviews in Google Analytics for Funnels and Websites ](<https://help.gohighlevel.com/support/solutions/articles/48001219725-how-to-record-pageviews-into-google-analytics-for-funnels-websites-ga4->)
  * [ Set Up a Funnel Event Pixel for Meta Conversions API ](<https://help.gohighlevel.com/support/solutions/articles/48001236281>)
  * [ How to Set Up Call Tracking ](<https://help.gohighlevel.com/support/solutions/articles/48000981393>)
  * [ Funnels, Websites & Webinars: Basic Troubleshooting ](<https://help.gohighlevel.com/support/solutions/articles/155000004983-faqs-basic-troubleshooting-funnels-websites-webinars>)

# Ad Manager - Custom Values in Ad Copy

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008389-ad-manager-custom-values-in-ad-copy](https://help.gohighlevel.com/support/solutions/articles/155000008389-ad-manager-custom-values-in-ad-copy)  
**Category:** Marketing  
**Folder:** Ad Campaign Creation and Management

---

Ad Manager

# Ad Manager - Custom Values in Ad Copy

Build faster, more consistent Meta, Google, and LinkedIn campaigns by reusing business details across ad copy

What You'll Learn

Custom Values in ad copy let you insert reusable, account-level placeholders like business name, city, phone number, and offer name, directly into supported text fields for Meta, Google, and LinkedIn campaigns. These placeholders resolve to their actual values in campaign previews so you can verify final ad copy before publishing.

This guide walks through what this feature does, where it works, how to insert and map Custom Values, and how to set it up confidently in your HighLevel account.

Table of Contents

1

What is Ad Manager - Custom Values in Ad Copy?

2

Key Benefits of Custom Values in Ad Copy

3

Custom Values in Ad Copy

4

Supported Ad Copy Fields and Limitations

5

How to Set Up Custom Values in Ad Copy

6

Frequently Asked Questions

7

Related Articles

1

## What is Custom Values in Ad Copy?

Custom Values in Ad Manager ad copy let you insert reusable, account-level "key:value" placeholders directly into supported text fields—such as primary text, headlines, descriptions, and introduction text—for Meta, Google, and LinkedIn campaigns. These placeholders are replaced ("resolved") with the actual stored values in your campaign preview and review screens so you can see the final ad copy before publishing.

HighLevel Custom Values are created in Settings → Custom Values as key:value pairs (for example, a key like `custom_values.business_name` and a value like "Summit Dental Studio"). Once created, the same key can be reused anywhere the Custom Values picker is supported—including Ad Manager—so you don't have to manually type the same information over and over.

Typical information you might store as Custom Values includes:

  * Business name
  * City or service area
  * Support email
  * Phone number
  * Offer or promotion name
  * Standard guarantee or CTA phrases


2

## Key Benefits of Custom Values in Ad Copy

**Create campaigns faster** — Insert pre-saved details (business name, city, phone, URL fragments, offer names) instead of retyping them in every ad.

**Reduce repetitive copy entry** — Reuse the same Custom Value across campaign types and platforms; update once at the value level instead of editing every ad.

**Keep ad copy consistent** — Ensure phone numbers, emails, and branding lines appear exactly the same across all ads and channels.

**Reuse templates across sub-accounts** — Save campaigns as templates that keep Custom Value keys, so you can map client-specific values per sub-account rather than rebuilding copy.

**Preview final resolved copy before publishing** — See actual text (not just placeholders) on the preview and review screens, reducing the risk of typos or placeholder tokens slipping into live ads.

**Avoid publishing issues** — Built-in validation warns when Custom Values are missing, blank, invalid, or push copy over platform character limits so you can fix issues before launch.

3

## Custom Values in Ad Copy

This feature centers around using your existing HighLevel Custom Values directly in the ad copy fields of Ad Manager campaigns. Instead of writing "Summit Dental Studio" manually, you can pick values from an Insert Custom Values picker and have them resolve to the stored text when the ad is previewed and published.

Key points to understand:

**Backed by global Custom Values** — Ad Manager uses the same Custom Values you configure under Settings → Custom Values, where each value is defined as a key and a value (e.g., `custom_values.city` → "Austin").

**Works across multiple platforms** — You can use Custom Values in ad copy for Meta (Facebook/Instagram), Google, and LinkedIn campaigns created within HighLevel Ad Manager.

**Resolves into real text at preview** — In the campaign builder and on review screens, Custom Values display as the final text so you can confirm exactly what your audience will see.

**Non-supported areas stay manual** — Custom Values are intentionally limited to eligible text fields (copy), so you still set URLs, CTAs, media, and budgets explicitly.

Related Resources

For a foundational understanding of how Custom Values work across the platform (outside of Ad Manager), review [](<https://help.gohighlevel.com>)[How to use Custom Values](<https://help.gohighlevel.com/en/support/solutions/articles/48001161575>) and [](<https://help.gohighlevel.com>)[Custom Values Settings](<https://help.gohighlevel.com/en/support/solutions/articles/155000004705>).

4

## Supported Ad Copy Fields and Limitations

Knowing exactly where Custom Values are supported prevents confusion when certain fields do not show the Insert Custom Values picker or don't accept merge fields. This section summarizes where you can and cannot use Custom Values in Ad Manager.

Supported Fields

Across Meta, Google, and LinkedIn campaigns, Custom Values can be used in eligible text-based ad copy fields such as:

Platform| Supported Fields  
---|---  
Meta| Primary Text, Headline, Description  
Google Ads| Headlines, Descriptions  
LinkedIn| Intro/Primary Text, Headline (where supported)  
  
Not Supported

Custom Values are not supported in:

  * URL fields (final URLs, display URLs, tracking templates)
  * CTA dropdowns (e.g., "Learn More", "Book Now")
  * Lead form selectors
  * Media upload fields (images, videos, carousels)
  * Targeting settings (location, interests, demographics)
  * Budget or bid strategy fields


Tip

If a field doesn't expose the Insert Custom Values icon or merge-field picker, assume Custom Values are not supported in that area and enter information manually.

5

## How to Use Custom Values in Ad Copy

Setting up this feature is mainly about preparing the right Custom Values and then using the Insert Custom Values picker inside your existing Ad Manager workflow. Investing a few minutes up front to define clean, well-named values pays off every time you launch or duplicate a campaign.

Step 1

Plan which details should be Custom Values

Before building a campaign, decide which pieces of information you reuse across ads and accounts. Common candidates:

  * Business Name (e.g., "Summit Dental Studio")
  * Primary City or Service Area
  * Support Email (e.g., "support@yourdomain.com")
  * Main Phone Number
  * Offer Name (e.g., "$47 New Patient Special")
  * Guarantee/USP (e.g., "Results in 30 days or we work for free")


Using Custom Values for these items means you can update them centrally later if needed (for future campaigns) and keep templates cleaner.

Step 2

Create or verify Custom Values in Settings

  1. In the sub-account, go to **Settings** → **Custom** **Values**.
  2. Click **\+ Add Custom Value**.
  3. Enter a descriptive **Name** (this becomes the key, such as `custom_values.business_name`).
  4. Enter the **Value** exactly as you want it to appear in your ads (e.g., "Summit Dental Studio – Downtown").
  5. Optionally assign the Custom Value to a **folder** like "Ad Manager – Client Basics" to keep things organized.
  6. Click on **Create**.


Repeat this for each business detail you'll reference in ad copy.  
  


![](https://jumpshare.com/share/P1KhIvHvSzxyOH3u3Btg+/GIF+Recording+2026-08-07+at+18.54.24.gif)

Step 3

Create or edit an Ad Manager campaign

  1. Navigate to **Marketing** → **Ad Manager**.
  2. **Create** a **new** **campaign** or **edit** an **existing** campaign for **Meta** , **Google** , or **LinkedIn**.
  3. Proceed through the campaign steps until you reach the Ad level Text & Media / ad copy step (names vary slightly by platform, but this is where you set Primary Text, Headline, Description, and media).  
  


![](https://jumpshare.com/share/NZLwqq8cSyEQddDJYXEh+/GIF+Recording+2026-08-07+at+19.02.47.gif)

Step 4

Insert Custom Values into ad copy

  1. Click into a supported copy field (e.g., Primary Text).
  2. Click the **Insert Custom Values** icon next to the field.
  3. Search or browse to find the value you created (e.g., "Business Name", "City", "Main Offer").
  4. Click to insert; the merge token is added to the field.
  5. Add context around it, such as: "`{{custom_values.business_name}}` is now accepting new patients in `{{custom_values.city}}`!" or "Call `{{custom_values.phone}}` to claim our `{{custom_values.offer_name}}`."
  6. Repeat for any headlines, descriptions, or intro text where you want dynamic values.  
  


![](https://jumpshare.com/share/Xj947k7ZMzmSwgcM7Wd8+/GIF+Recording+2026-08-07+at+19.14.15.gif)

Step 5

Map custom values and fix any issues

  1. After finishing the copy, click **Map custom values** (typically available near the Review step).
  2. Review the detected Custom Value keys and their current values.
  3. Fill in or correct any missing, blank, or placeholder values.
  4. **Save** and return to the campaign builder.  
  


![](https://jumpshare.com/share/AKeHXZBC8bcIJkX2NMUo+/GIF+Recording+2026-08-07+at+19.17.16.gif)

Step 6

Preview resolved ad copy

  1. Click on the **Review** button.
  2. Verify that all Custom Values have resolved to their actual text (e.g., you see "Austin" instead of `{{custom_values.city}}`).
  3. Check that copy reads naturally and stays within character limits.
  4. Make any final adjustments to copy or values as needed.  
  


![](https://jumpshare.com/share/ga961hZsa15yo619IDtA+/GIF+Recording+2026-08-07+at+19.19.50.gif)

Step 7

Publish your campaign

  1. Once preview looks correct and all validation checks pass, click **Publish Campaign Now**.
  2. HighLevel sends the fully resolved ad copy (with Custom Values replaced) to the ad platform.
  3. Your ads go live with the correct business details automatically inserted.


  
![](https://jumpshare.com/share/xze4RnueLnw5Xb7T0ifw+/Screenshot+2026-08-07+at+19.21.33.png)

6

## Frequently Asked Questions

Q: Can I use Custom Values in URL fields or CTAs?

No. Custom Values are only supported in text-based ad copy fields like Primary Text, Headlines, and Descriptions. You cannot use them in URL fields, CTA dropdowns, lead form selectors, media uploads, targeting settings, or budget fields.

Q: What happens if I forget to map a Custom Value before publishing?

Built-in validation warns you when Custom Values are missing, blank, or invalid. The campaign builder prevents you from publishing until all Custom Values are properly mapped and resolved, reducing the risk of placeholder text appearing in live ads.

Q: Can I update a Custom Value after my campaign is live?

Updating a Custom Value in Settings only affects future campaigns. Live campaigns use the value that was resolved at the time of publishing. To change the ad copy in an active campaign, you need to edit the campaign directly and republish it.

Q: Do Custom Values work across Meta, Google, and LinkedIn?

Yes. You can use the same Custom Values in ad copy for all three platforms. The supported fields vary slightly by platform (Primary Text and Headline for Meta, Headlines and Descriptions for Google, Intro Text for LinkedIn), but the underlying Custom Values system works the same way.

Q: Will Custom Values in ad copy push me over character limits?

The platform validates character limits after resolving Custom Values to their actual text. If the resolved copy exceeds platform limits (e.g., Meta's 125-character headline limit), you'll see a validation warning and need to shorten your copy or Custom Value before publishing.

Q: Can I reuse campaigns with Custom Values as templates across sub-accounts?

Yes. When you save a campaign as a template, the Custom Value keys are preserved. You can then map client-specific values per sub-account without rebuilding the entire ad copy structure.

Q: Where do I see the final resolved ad copy before publishing?

The Review and Preview screens show the fully resolved ad copy with Custom Values replaced by their actual text. This lets you verify exactly what your audience will see before the campaign goes live.

7

## Related Articles

  * [How to use Custom Values](<https://help.gohighlevel.com/en/support/solutions/articles/48001161575>)

  * [Custom Values Setting ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004705>)

  * [Overview of Ad Manager](<https://help.gohighlevel.com/en/support/solutions/articles/155000002433>)

  * [How to Get Started with Meta Campaigns in Ad Manager](<https://help.gohighlevel.com/en/support/solutions/articles/155000003044>)

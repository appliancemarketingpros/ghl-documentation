# Email Services Configuration - Reply & Forward Settings

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001155000-email-services-configuration-reply-forward-settings](https://help.gohighlevel.com/support/solutions/articles/48001155000-email-services-configuration-reply-forward-settings)  
**Category:** Email  
**Folder:** General

---

Email Services

# Reply & Forwarding Addresses

Configure forwarding, reply-to, BCC, and reply tracking settings for your GoHighLevel email service.

Table of Contents

  1. 1\. Forwarding Address
  2. 2\. Reply Address
  3. 3\. BCC Emails
  4. 4\. Forward to Assigned User
  5. 5\. Billing for Forwarded Emails
  6. 6\. Enable Reply Tracking – Other SMTP Providers
     * ·Example With Reply Tracking
     * ·Example Without Reply Tracking
  7. 7\. Frequently Asked Questions


## Where to Find Reply & Forward Settings

These settings let you receive copies of emails, configure reply-to addresses, and control how replies are tracked. To get started, navigate to:

Settings → Email Services → Reply & Forward Settings

![Email Services settings navigation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031378307/original/sTiyHi3hqgNimmaOnIK2tUuzV8jltXg4GQ.jpg?1724182488)

## Forwarding Address

When a lead responds to an email, that response always appears in the **Conversations** tab. If you also want a copy of the lead's reply delivered to someone's inbox, enter that email address here.

You can enter multiple forwarding addresses separated by commas, for example:  
email1@test.com, email2@test.com, email3@test.com

⚠️

**Important** Forwarding address and BCC Emails **only work with Mailgun and LC Email**. Other SMTP providers are not supported. All incoming and outgoing emails (To, CC, and BCC) will be charged.

![Forwarding address configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031378336/original/c3rgbqnGtH4wUFzgVQHWw-xOjviN0LTHvQ.jpg?1724182531)

## Reply Address

Adding a reply-to address routes all incoming email replies to that address _instead of_ the Conversation tab.

When you reply to a lead's email from your external inbox (outside the CRM), that reply will **not sync back to the CRM**.

You can add up to **5 email addresses**.

Navigate to Settings → Email Services → Reply & Forward Settings → Reply Address and click **Save** after adding your addresses.

![Reply address configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031547525/original/19Bs496zgaiTVo1bO9nwhTXXoA-anf5jsw.png?1724400925)

![Reply address settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031378366/original/qADgEHJ_7tnNV3n3amaaOlUmjr9frQvMeQ.jpg?1724182590)

## BCC Emails

Receive a Blind Carbon Copy of every 1-on-1 email, workflow email, and billing email sent from this location. Configure this from Settings → Email Services → Reply & Forward Settings → BCC Emails.

ℹ️

**BCC Scope** BCC is supported only for **1-on-1 emails, workflow emails, and billing emails**. It does **not** apply to bulk or campaign emails.

![BCC email configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031378457/original/e6UutfFjMKYAJTconTpaZbdXT1s829mt9Q.jpg?1724182752)

## Forward to Assigned User

The lead's assigned user receives email replies directly in their email inbox. The email is sent to the address configured under Settings → My Staff → Edit User → User Info.

![Forward to assigned user](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031378472/original/8FqD-K9rmcAe_-g7s3oyRrYwr-6kvqjWYQ.jpg?1724182778)

## Billing for Forwarded Emails

Forwarded messages are billed the same way as normal outgoing emails when **rebilling** is enabled, improving usage accuracy and transparency.

Service| Applies To  
---|---  
**LC Email**|  Agency and sub-account (when rebilling is enabled)  
**Mailgun (Location-owned)**|  Sub-account only  
  
Each **forwarded email** incurs a per-email charge aligned to regular email sending rates.

?

**How to verify charges** Check billing entries for **Billing Source Type** (the service that generated the charge) and **Billing Trigger ID** (unique identifier for the forwarded-email event).

## Enable Reply Tracking – Other SMTP Providers

There is no option to enable reply tracking for Mailgun since it is directly integrated with the Receiving Route set up in Mailgun. [Learn how to set up replies in Mailgun →](<https://help.gohighlevel.com/en/support/solutions/articles/48000987293>)

If you mask the sender email (e.g. testing@gmail.com), the reply-to address will show as **testing@replies.subdomain.com** — the Mailgun subdomain configured for the location in Agency Settings → Mailgun.

Replies will still appear correctly in the sub-account's Conversation tab.

![Reply tracking SMTP screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48286916898/original/w-1dICJ2Bsh_RZAP7ac2r7jnJsfEuOMb8Q.png?1678723680)

![Reply tracking settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031378496/original/gePZQCEUWIstIyH1C68WKaiSaOcgjonr8Q.jpg?1724182805)

### ✅ Example With Reply Tracking

The reply-to address shown in the email header is the Mailgun subdomain address. This allows the system to capture replies and route them back into the **Conversation tab** , where you can read, respond, or trigger automated workflows using tags.

?

**Important** Copying the reply-to address and sending a brand-new email to it will _not_ route back to the Conversation tab. You must reply to the original email sent from the system.

![Example with reply tracking enabled](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48260597029/original/MM1xCqK_FV3P9RIVLiwReIssTd-Qb4hbIQ.png?1667330277)

### ❌ Example Without Reply Tracking

Without reply tracking, the reply-to address points to the configured sender email. Responses go directly to that inbox and are **not captured** in the Conversation tab.

![Example without reply tracking](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48260597698/original/IFF1KAgY2Qq0-jX_xY_cHqEWOSsOv33SJg.png?1667330551)

## Frequently Asked Questions

Q Why are attached files not forwarded along with email replies?

The forwarding settings in the Email Services tab do not support forwarding attachments. If a contact replies with an attachment, you must log in to the HighLevel conversation view to access it.

Q Why do the forwarding emails I've added disappear after saving?

If email addresses are invalid, or they conflict with a dedicated domain added to your sub-account, they cannot be used as a forwarding address and will not be saved.

Q Are forwarded emails free?

No. When **rebilling** is enabled, each forwarded email is billed like a normal outgoing email.

Q Which services does forwarding billing apply to?

**LC Email** (Agency and sub-account when rebilling is enabled) and **Mailgun (Location-owned)** at the sub-account level.

Q Do forwarded emails use the same per-email rate as regular sends?

Yes — charges are aligned with standard email send rates. _(Confirm with your account manager for any plan-specific markup or fees.)_

Q Where can I verify which forwarded emails were billed?

Check your billing views for **Billing Source Type** (the service that generated the charge) and **Billing Trigger ID** (the unique event ID) to trace each charge. _(Confirm the exact page and CSV columns with your account team.)_

Q Do these charges apply if rebilling is turned off?

No. Forwarded-email charges require **rebilling** to be enabled for the sub-account.

Q Is this change retroactive?

Charges typically apply from the effective date forward. _(Confirm the exact effective date and retroactivity details with your account manager.)_

Q Does agency-level Mailgun forwarding get billed?

This update references **Mailgun (Location-owned) at the sub-account level only**. Agency-level Mailgun forwarding is not covered under this billing update.

![FAQ supporting screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029443187/original/_qck3ZATobcGzaVOA4RzV5XfjyYYBRnrLA.jpg?1721248883)

Related Articles

[ ? Email Re-Billing on Unlimited & Pro Plans ](<https://help.gohighlevel.com/en/support/solutions/articles/48001188579>) [ ? What is LC Email? ](<https://help.gohighlevel.com/en/support/solutions/articles/48001220605>) [ ? Rebilling, Reselling & Wallets Explained ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002095>) [ ? Analyze Agency Spending on LC Communications ](<https://help.gohighlevel.com/en/support/solutions/articles/48001225291>) [ ? Account Billing Dashboard (Sub-Account) ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004182>) [ ⚙️ Email Services – Reply & Forward Settings ](<https://help.gohighlevel.com/en/support/solutions/articles/48001155000>)

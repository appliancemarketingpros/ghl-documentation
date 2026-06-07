# How to Enable and Rebill LC Email Verification

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001235221-how-to-enable-and-rebill-lc-email-verification](https://help.gohighlevel.com/support/solutions/articles/48001235221-how-to-enable-and-rebill-lc-email-verification)  
**Category:** Email  
**Folder:** LC Email

---

Email Deliverability

Email Verification

Automatically validate email addresses before sending to protect your sender reputation and improve deliverability. Available for LC Email and Mailgun.

What You'll Learn

Email Verification is a bulk tool that checks whether an email address is legitimate and active before any email is sent. When enabled, it runs automatically in the background — no manual action required.

This article covers how to enable verification at the agency and subaccount levels, how to set up 90-day re-verification, pricing and rebilling, and how to check verification status on individual contacts.

Table of Contents

1

What is Email Verification

2

How to Enable Email Verification (Agency Level)

3

How to Enable Email Verification (Subaccount Level)

4

Enable Email Re-verification Every 90 Days

5

Email Verification Pricing and Rebilling

6

How Email Verification Works

7

What Email Verification Actually Checks

8

What Email Verification Does NOT Guarantee

9

Common Reasons a Verified Email Still Bounces

10

Frequently Asked Questions

1

## What is Email Verification

Email Verification is a background process that checks whether an email address has the qualities of a legitimate, active account. It runs automatically when enabled — you don't need to trigger it manually.

By filtering out fake or inactive addresses before sending, Email Verification keeps your sending score high and significantly improves email delivery rates. It can also be configured to re-verify addresses every 90 days, since email quality can change over time.

Note

Email Verification is a paid service. It is available exclusively for **LC Email** and **Mailgun** email providers.

2

## How to Enable Email Verification (Agency Level)

Agency admins can enable or disable Email Verification for individual subaccounts — or all subaccounts at once — from the Agency Settings panel.

Step 1

Navigate to Agency → Settings

Open your Agency dashboard and go to **Settings**.

![Agency Settings navigation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226444/original/BmdtAPhC_AVF0oeJONK0GfYUKuI58wSjdg.png?1737504795)

Step 2

Navigate to Email Services → Location Settings → Email Verification

Within Settings, go to **Email Services → Location Settings** and locate the **Email Verification** column.

![Email Services Location Settings panel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226468/original/3Pa434oDNqywtAwKMJwsUo5gzpxviq3RAQ.png?1737504887)

Step 3

Enable or disable Email Verification per subaccount

Toggle Email Verification on or off for each individual subaccount, or use the bulk toggle to apply the setting across all subaccounts at once.

![Toggle Email Verification per subaccount](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226484/original/1r_FrAbbQAaa9K1H1Bg9wxpKgJ0YsWs1RA.png?1737504968)

Step 4 — Optional

Configure automatic verification for new subaccounts

Navigate to **Advanced Settings** and check or uncheck **"Automatically enable email verification for new Subaccounts"** to control default behavior for newly created subaccounts.

![Advanced Settings for auto-enabling email verification on new subaccounts](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226767/original/tjBsZtiTzP9nxA3pj7WwVtRUolE4Fq86cA.png?1737506094)

3

## How to Enable Email Verification (Subaccount Level)

Subaccount users can also enable Email Verification directly from their own account settings.

Step 1

Navigate to Subaccount → Settings

Open the subaccount and go to **Settings**.

![Subaccount Settings navigation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226719/original/dUw4mXRhuaZ5TCLgsajdcEGO_TEzAC3vEw.png?1737505836)

Step 2

Navigate to Business Profile → General

Go to **Business Profile → General** within Settings.

![Business Profile General settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226733/original/GPwxyWWVxdylX5rmqrrSMUQMO1OdYYK6Xg.png?1737505901)

Step 3

Check or uncheck the Verify Email setting

Toggle the **Verify Email** checkbox to enable or disable email verification for this subaccount.

![Verify Email checkbox in subaccount settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226749/original/4EFxdTjfNaZ6brzMO_wFU_8Ad5-Rnj2BXg.png?1737505937)

Heads Up

When a subaccount user enables Email Verification, a notification is automatically sent to all active agency admins and the company's registered email address (LC Email only). Subject line: **ATTN: Email Verification Enabled in Sub-Account**.

![Email notification sent to agency admins when subaccount enables verification](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029902371/original/GIN4_Fw_IN3QaYv5k9TPQIeWSt1F-OgPow.jpg?1721926642)

4

## Enable Email Re-verification Every 90 Days

Email address quality can change over time — an address that was valid six months ago may now be inactive or abandoned. Enabling 90-day re-verification ensures you catch these changes before they hurt your sender score, rather than after.

Step 1

Navigate to Agency → Subaccounts → Manage Client

Go to **Agency → Subaccounts** , click the **three-dot menu** in the lower right corner of the subaccount card, and select **Manage Client**.

![Subaccount card three-dot menu showing Manage Client option](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226787/original/GYYxPDEUZlzGxEZLaEG2L9vd-8x2k7V53g.png?1737506220)

Step 2

Enable Re-verification in Advanced Email Settings

Navigate to **Advanced Settings → Advanced Email Settings** and check or uncheck **"Enable Re-verification for 90 days"**.

![Enable Re-verification for 90 days setting in Advanced Email Settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226804/original/3NDtG-FaLhZrJuPdH4PjCCRFJ9CVlIpwmg.png?1737506342)

5

## Email Verification Pricing and Rebilling

Pricing

**$2.50 per 1,000 Email Verifications** — available on all plans. This is significantly lower than most providers (e.g., Mailgun charges $12/1,000).

Rebilling settings for LC Email Verification are found in **SaaS Configurator → Plan Details → Rebilling**. Rebilling capabilities vary by plan:

Plan| Rebilling Capability  
---|---  
Starter| No rebilling  
Unlimited| Fixed markup only (1.05x)  
Pro| Variable markup (1.05x – 10x)  
  
![SaaS Configurator rebilling settings for Email Verification](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040226905/original/3n_R-VvMrLnzpi0n3JKwX6g1gbCSa_bOhg.png?1737506674)

To review individual Email Verification charges, navigate to the **Agency Billing Wallet**. Every execution is itemized so you can audit usage with full transparency.

Step 1

Navigate to Agency → Settings

Open your Agency dashboard and go to **Settings**.

![Agency Settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300128/original/arhHUQsbo9aVrGwGQI9r0YcvjJYUapTB8Q.png?1737596728)

Step 2

Navigate to Billing → Wallet & Transactions → Detailed Transactions

Go to **Billing → Wallet & Transactions** and open **Detailed Transactions**.

![Billing Wallet and Transactions view](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300100/original/Cht9DFF36yQaJKnY1JVRE_IIo9xuQZ5f8g.png?1737596561)

Step 3

Filter to Email Verification and review each transaction

Use the filter to show only **Email Verification** items, then click into individual transactions for a full breakdown.

![Filtering transactions to show only Email Verification charges](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300126/original/wXYCGB6MXvRNpdodySbMi0DXIwTizc-46A.png?1737596703)

6

## How Email Verification Works

When Email Verification is active, all email addresses are verified before the first email is sent — if they haven't been verified already. If 90-day re-verification is also enabled, any verification older than 90 days will expire and the address will be re-checked before the next send.

You can also manually check or trigger verification for any contact from the Contact Details page.

Step 1

Navigate to Subaccount → Contacts

Go to the **Contacts** section of the subaccount.

![Contacts section in the subaccount](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300160/original/SKALqJ_LL8rxLaZEnTLKDl0ezY0AIPcnaQ.png?1737596920)

Step 2

Click into a contact's details

Select a contact from the list to open their detail view.

![Opening a contact's detail view](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300210/original/1Q8oQog4BgRGb0F-0x-Fqo21WRN7R5J4FQ.png?1737597032)

Step 3

Expand the Contact section

Click to expand the **Contact** section within the detail panel.

![Expanding the Contact section in contact details](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300233/original/kEive6W3un5YtnbZ2ZUXMd_LJsU5m0Ikqw.png?1737597112)

Step 4

Scroll down to the Email field

The Email field displays the current verification status for this contact's email address.

![Email field showing verification status on contact details page](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040440257/original/FJYzNO-k72vrGzNDGyN2Ij9YXP1dlTEt6g.png?1737770899)

Verification status meanings:

Status| Meaning  
---|---  
Not Verified| The email has not yet been tested by the Email Verification service.  
Invalid| The email was tested and failed Email Verification. Emails will not be sent to this address.  
Verified| The email was tested and passed Email Verification. Safe to send.  
  
![Not Verified status indicator](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300289/original/kvN55koy3sDHrGJXgDXIkSvAk13u-WgfNw.png?1737597234)

Not Verified status

![Invalid status indicator](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300292/original/xqVPIQfH1Set388He-QkYoEOsNzwMSkrTA.png?1737597259)

Invalid status

![Verified status indicator](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040300294/original/A1DriVwG5LvV65BmqXhRbf4RwIltTTViuA.png?1737597283)

Verified status

7

## What Email Verification Actually Checks

Email verification tools run a series of technical checks to assess whether an address is likely to exist and accept mail. Here is what each check does:

Check 1

Syntax Validation

Confirms the address is properly formatted — e.g., name@domain.com. Catches obvious typos like missing @ symbols or invalid characters.

Check 2

Domain / MX Record Lookup

Verifies that the domain (e.g., gmail.com) has active MX records, meaning the domain is configured to receive email at all.

Check 3

SMTP Ping (Mailbox Existence)

Initiates a connection to the mail server and asks if the specific mailbox exists — without actually sending a message. If the server responds positively, the address is marked "valid."

What This Means

Passing all three checks means the address **appears to exist at the time of verification**. It does not mean your email will reach the inbox.

8

## What Email Verification Does NOT Guarantee

Verification is a pre-send check — it cannot control what happens during and after delivery. The following are outside its scope:

  * The email will not bounce — a "valid" address can still be rejected post-delivery
  * The email will land in the inbox rather than spam or be silently discarded
  * The address is still active — mailboxes can be deactivated after verification passes
  * Your sending domain or IP is not on a blocklist
  * The recipient's inbox is not full or subject to temporary server issues


Note

Think of verification like confirming a mailing address exists on a map — it doesn't guarantee the package will be accepted at the door, or that no one moved out since you last checked.

9

## Common Reasons a Verified Email Still Bounces

Even after passing verification, emails can still fail to deliver. Here are the most common causes and why verification can't catch them:

Cause| Why Verification Misses It  
---|---  
Catch-all domain| Server accepts all addresses during SMTP check, then rejects unknown mailboxes after delivery  
Mailbox deactivated after verification| Address was valid at check time; account was deleted or suspended since then  
Sender reputation / IP blocklist| Verification checks the recipient — not whether your sending domain or IP is trusted  
Spam / content filtering| Recipient's mail server rejects the message based on content or DMARC/SPF/DKIM failure  
Role-based address filtering| Addresses like info@, admin@, noreply@ may verify as valid but reject marketing email by policy  
Temporary soft bounce| Server was down, over quota, or greylisting at delivery time — unrelated to address validity  
  
Important

Catch-all domains are the most common culprit. There is no reliable way for a verification tool to distinguish a real mailbox from a catch-all, because the server intentionally accepts everything during the SMTP handshake.

10

## Frequently Asked Questions

Q: What does Email Verification check for?

Email Verification checks whether an email address is on a known "bad" list at Mailgun, and additionally verifies that: the syntax is correct; the domain is set up to receive email; the address exists; the address is not high-risk; and the address is not role-based (such as info@domain.com or admin@domain.com).

Q: Why is Email Verification important?

Email Verification boosts your delivery rate by removing invalid addresses, maintains list hygiene, improves marketing metrics like open rate and CTR, and protects your sender reputation — all of which directly impact whether your emails reach inboxes.

Q: How does Email Verification impact my email deliverability?

Bounced emails damage your IP address and domain reputation. When your email service provider can't deliver a message, it signals to email clients that your domain may not be trustworthy — leading to future emails landing in spam or being blocked entirely. Verifying addresses before sending reduces bounce rates and keeps your sender reputation intact.

Q: Why does my subaccount have automatic email verification enabled?

Automatic email verification is enabled for subaccounts created within the last 30 days where the deliverability rate of the imported email list fell below 90%. This safeguard protects your sending reputation while the account's list quality is being established.

Q: When should I verify my email list?

Verify your list if you've purchased a mailing list (which is not recommended), inherited an unfamiliar list, or if your list has grown significantly or hasn't been cleaned in a while. When in doubt, run a health check — catching stale addresses proactively is always better than discovering them through bounces.

Q: Where can I see my client's email verification usage?

Navigate to **Agency Settings → Billing → See Details** (under Credits) to view per-client usage. For a full itemized breakdown, use the **Billing → Wallet & Transactions → Detailed Transactions** view and filter by Email Verification.

Q: How can I bill my clients for Email Verification usage?

If you are on the Unlimited or Pro plan, you can enable rebilling through **SaaS Configurator → Plan Details → Rebilling**. This lets you automatically pass costs on to clients at a markup, saving you from having to invoice them manually.

Q: Does Email Verification affect contacts who have already been sent emails?

No. Verification only runs before the _next_ email send for a given contact. Previously sent emails are not affected. If 90-day re-verification is enabled, a contact's verification status will expire after 90 days and they will be re-checked before any subsequent send.

# Where Can I Find My Dedicated Domain SMTP Credentials?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002132-where-can-i-find-my-dedicated-domain-smtp-credentials-](https://help.gohighlevel.com/support/solutions/articles/155000002132-where-can-i-find-my-dedicated-domain-smtp-credentials-)  
**Category:** Email  
**Folder:** LC Email

---

Email Infrastructure

SMTP Credentials for Email Domains

Create, manage, reset, and delete SMTP credentials for your dedicated email domain — plus ports, limits, pricing, and IMAP notes.

What You'll Learn

To use the SMTP server, you need credentials tied specifically to your dedicated sending domain. Each domain has its own set of SMTP credentials — they are not shared across domains or at the agency level.

This article covers how to create, reset, and delete SMTP credentials; which ports are supported; email and credential limits; pricing; and where to find IMAP settings for receiving email.

Table of Contents

1

How to Create SMTP Credentials

2

What Ports Does Mailgun Support?

3

How to Reset SMTP Password

4

How to Delete SMTP Credential

5

Limits for SMTP and Emails

6

LC Email Pricing

7

Where to Find IMAP Settings

8

Troubleshooting

9

Frequently Asked Questions

Video Walkthrough

1

## How to Create SMTP Credentials

SMTP credentials are created at the **sub-account level** under a dedicated domain — not at the agency level, and not for agency-assigned domains.

Step 1

Navigate to Sub-account Settings

Go to **Email Service → SMTP Service → Dedicated Domain and IP → SMTP Settings** under your dedicated domain.

![SMTP Settings location under Dedicated Domain and IP in Email Services](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155023337421/original/nMyZojgr2ZYUAZSkyYnJ6GXwk_Eyr_1HGw.png?1711087651)

Step 2

Create New SMTP User

Click **Create New SMTP User** and enter a username and password for the credential.

Note — Approval Required

The platform uses an automated approval system for SMTP access. Eligible sub-accounts can create credentials immediately. If your account is not approved, the **Create New SMTP User** button may be disabled or you may see a warning message.

![Create New SMTP User button and form](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155023337477/original/3gfn3HeigPBnj1KhpAJrkIlpaoOzAJ0ONw.png?1711087786)

![SMTP user created successfully](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155023337530/original/utUNsl_XodI8FsMRFgE8TrwwQdmfgvu_uA.png?1711087862)

Your SMTP Settings

SMTP Server Address| smtp.mailgun.org  
---|---  
Secure Connection| TLS/SSL (based on your mail client or SMTP plugin)  
SMTP Username| YourGivenName@DomainName.com  
SMTP Password| YourGivenPassword  
SMTP Ports| 25, 465 (SSL/TLS), 587 (STARTTLS), 2525  
  
2

## What Ports Does Mailgun Support?

The SMTP server (smtp.mailgun.org) listens on the following ports:

Port| Protocol| Use When  
---|---|---  
25| Standard SMTP| Server-to-server relaying (often blocked by ISPs for client use)  
465| SSL/TLS| Clients requiring implicit TLS from the start of the connection  
587| STARTTLS| Recommended for most email clients and SMTP plugins  
2525| Alternative SMTP| Fallback when ports 25, 465, and 587 are blocked  
  
3

## How to Reset SMTP Password

To reset the password for an existing SMTP credential, locate the credential in your domain's SMTP Settings and click the reset option. In the confirmation modal, click **Reset Password** to finalize the change.

![Reset Password button in SMTP credential modal](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155023337656/original/22ZqznlGSww3OYVk2ULdCYph_uhwvbBG9A.png?1711088188)

Initiate the password reset from the SMTP credential row

![Confirm Reset Password in the confirmation modal](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155023337668/original/NsTvuvM2YMJRI2xkQypolDdneD_Yn8-tJw.png?1711088202)

Confirm the reset in the pop-up modal

4

## How to Delete SMTP Credential

To remove an SMTP credential, locate it in your domain's SMTP Settings and click **Delete**. Confirm the deletion in the pop-up modal.

![Delete SMTP credential button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155023337727/original/f7oeVWxByu7aA60MK7YoTBAA7c-citPWbg.png?1711088371)

Click Delete on the SMTP credential row

![Confirm deletion of SMTP credential](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155023337732/original/-c2VpTSwanpwk3Nc_sLI3fi87590WKS2TA.png?1711088383)

Confirm deletion in the modal

5

## Limits for SMTP and Emails

SMTP Credential Limit

5 credentials per dedicated domain

A maximum of **five SMTP credentials** can be created for each dedicated domain.

Daily Email Limit

1,500 emails per day per account

Each account is limited to **1,500 emails per day**.

Important

If the daily email limit is exceeded, **all SMTP credentials will be automatically deleted** from all dedicated domains on the account.

6

## LC Email Pricing

LeadConnector email is priced at **$0.675 per 1,000 emails** — lower than most major SMTP providers (Mailgun charges $0.80/1,000). All plans use the same per-email rate.

Email charges are deducted from your account credits and can be reviewed at **Agency View → Billing → Credits**.

Note

[All incoming and outgoing emails — including To, CC, and BCC recipients — are each charged separately.](<https://help.gohighlevel.com/support/solutions/articles/48001220605-what-is-lc-email-i-want-to-know-more#LC---Email-Pricing>)

7

## Where to Find IMAP Settings

Not Supported

Since mailboxes are not hosted here, POP and IMAP protocols are not supported. **SMTP credentials cannot be used in IMAP settings.**

IMAP is used to _retrieve_ messages from your mailbox, while SMTP is for _sending_. If you need IMAP to read email in a client, you must get those settings from your email hosting provider — not from this platform.

**Example — Google Workspace:** Generate an app password in Google, then use:

Google IMAP Settings

Username| Your full email address  
---|---  
Password| Your Google app password  
IMAP Host| imap.gmail.com  
IMAP Port| 993  
  
For other providers, find IMAP settings in their own support documentation. Quick links:

[Amazon AWS WorkMail](<https://docs.aws.amazon.com/workmail/latest/userguide/using_IMAP.html>)

[Hostgator](<https://www.hostgator.com/help/article/email-connection-settings>)

[Ionos](<https://www.ionos.com/help/email/general-topics/settings-for-your-email-programs-imap-pop3/>)

[Kinghost](<https://king.host/wiki/artigo/como-configurar-seu-e-mail-no-pipedrive/>)

[Rackspace](<https://docs.rackspace.com/support/how-to/rackspace-email-and-hosted-exchange-settings/>)

[TransIP](<https://www.transip.eu/knowledgebase/entry/309-the-email-settings-at-transip/>)

[Bluehost](<https://www.bluehost.com/help/article/email-application-setup>)

[Titan](<https://support.titan.email/hc/en-us/articles/900000215446-Configure-Titan-on-other-apps-using-IMAP-POP>)

[Dreamhost](<https://help.dreamhost.com/hc/en-us/articles/215612887-Email-client-protocols-and-port-numbers>)

[InMotion](<https://www.inmotionhosting.com/support/email/getting-started-guide-email/>)

If your provider isn't listed, contact them directly for IMAP hostname and port information.

Common IMAP Reference

Provider| IMAP Host| IMAP Port  
---|---|---  
Google / Gmail| imap.gmail.com| 993  
Verizon| imap.verizon.net| 995  
AOL| imap.aol.com| 993  
  
8

## Troubleshooting

Issue

"Unable to Create SMTP User" — button is disabled or a warning banner appears

This means SMTP credentials cannot be created for that domain at this time. This is controlled by an automated approval system. Eligible accounts get access immediately; others require manual review.

**What to do:**

  * Contact Support to request SMTP access for your sub-account.
  * Include your sub-account ID, the sending domain or subdomain, and a screenshot of the warning message.


9

## Frequently Asked Questions

Q: Why am I seeing "SMTP Credential creation is blocked. Please contact support"?

This appears when your account has hit usage thresholds or has been flagged by internal controls to prevent abuse — commonly triggered by exceeding the 1,500 emails/day limit. Contact support with your sub-account ID to have the block reviewed and resolved.

Q: Can I create SMTP credentials at the agency level?

No. SMTP credentials are created at the sub-account level only, and only under a dedicated domain — not agency-assigned domains.

Q: What happens to my SMTP credentials if I exceed the daily email limit?

All SMTP credentials will be automatically deleted from all dedicated domains on the account. You will need to re-create them once your account is back within limits.

Q: Which port should I use for my email client or WordPress SMTP plugin?

Port **587 with STARTTLS** is the recommended choice for most email clients and SMTP plugins. Use port **465** if your client requires implicit TLS. Port **2525** is a reliable fallback if the others are blocked by your host or ISP.

Q: Can I use SMTP credentials to receive email (IMAP/POP)?

No. SMTP credentials are for _sending_ only. Mailboxes are not hosted here, so POP and IMAP are not supported. For receiving email, use the IMAP settings provided by your email hosting provider (e.g., Google Workspace, Outlook, etc.).

Q: How many SMTP credentials can I create per domain?

Up to **five SMTP credentials** can be created per dedicated domain.

Q: Are BCC recipients counted toward the daily email limit?

Yes. All recipients — To, CC, and BCC — are each counted and charged individually. A single email sent to 3 recipients (1 To, 1 CC, 1 BCC) counts as 3 emails toward both the daily limit and billing.

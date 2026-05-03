# Dedicated Email Sending Domains Overview & Setup

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001226115-dedicated-email-sending-domains-overview-setup](https://help.gohighlevel.com/support/solutions/articles/48001226115-dedicated-email-sending-domains-overview-setup)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Services

# Dedicated Sending Domain

A dedicated sending domain gives your business full control over what email servers deliver on your behalf — helping you avoid spam filters, protect your brand reputation, and improve deliverability.

⚠️

LC Email Users Only

Dedicated sending domains apply **only** to accounts on the [LC Email system](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>). Warm up any brand-new domain before emailing large lists to avoid poor deliverability.

ℹ️

Using a Third-Party SMTP?

If you want to connect an external provider instead, see [Setting Up SMTP Providers](<https://help.gohighlevel.com/support/solutions/articles/48001059689-setting-up-smtp-providers>).

Table of Contents

  1. 1 What is a Dedicated Sending Domain?
  2. 2 Configuring Dedicated Sending Domains
  3. 3 Shared Domain Email Refactoring
  4. 4 Troubleshooting Dedicated Sending Domains
  5. 5 Frequently Asked Questions


?

## What is a Dedicated Sending Domain?

A dedicated sending domain lets you send emails that appear to come directly from your brand — not from HighLevel's shared infrastructure. This protects your sender reputation and gives recipients a trustworthy, consistent experience. Any sub-account or agency can set one up quickly.

By default, all emails sent through the platform show HighLevel's sending servers in the **"sent on behalf of"** or **"sent via"** headers, as shown below:

![Default sent-on-behalf-of header](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48265938968/original/spw7PyvCIf6DlxRXiukwE1KRAbxsW5nK9w.png?1669638686)

⚙️

## Configuring Dedicated Sending Domains

You can create multiple sending domains and assign different ones for 1-to-1 emails, workflow emails, marketing campaigns, and payment/invoice emails.

1

### Navigate to Email Services

  * Go to **Settings → Email Services**
  * Click the **"Dedicated Domain and IP"** tab.


![Settings Email Services](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155039358860/original/SDAmMz_uAVt2ybizJ-_9H4TdvCGO9uG8bw.png?1736193889)

![Dedicated Domain and IP button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155039359007/original/fPkMuNjtNulufDsHraKqi_RhiT7kVj6i7g.png?1736194222)

* * *

2

### Add Domain Information

  * Click **"Add Domain"** to begin configuring.
  * Enter the sub-domain you want to use for sending.


![Add Domain flow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155039359484/original/eF1kHVNdn9F8E4LQc47YnPLKxFqETCQFag.gif?1736195532)

?

What is a Sub-Domain?

Sub-domains are variants of your root domain. For example, if your root domain is **agency123.com** , you can create sub-domains like emails.agency123.com or no-reply.agency123.com.

You can create as many sub-domains as you like and use different ones for different campaigns or communication types.

* * *

3

### Verify DNS Records

After adding your sub-domain, you'll need to verify DNS records. HighLevel can auto-configure them, or you can add them manually if auto-configuration isn't available.

?

**Propagation can take up to 24 hours.** If it's been longer, double-check your DNS settings. Note: **Multiple DKIM records for the same domain are not supported.**

![Verify DNS flow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155039360349/original/P-zGHtE40RWBS1c78K9-QxTVmAZcGYspOA.gif?1736198292)

#### Manually Adding DNS Records

To add DNS records manually, create them in your hosting provider's dashboard using the values HighLevel provides (as shown below). Then verify them from the HighLevel settings panel.

![DNS Records example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155039360663/original/HzBGtABLJsce2UkbD9t9VMG5rxqjnhBPfg.png?1736199195)

Instructions for common DNS providers:

  * ▸ [GoDaddy](<https://www.godaddy.com/help/manage-dns-zone-files-680>)
  * ▸ [Google Domains](<https://support.google.com/a/answer/48090?hl=en>)
  * ▸ [Hostgator](<https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom>)
  * ▸ [Hover](<https://help.hover.com/hc/en-us/articles/217282457>)
  * ▸ [Namecheap](<https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/cpanel-email-deliverability-tool--spf-and-dkim-records/>)


  * ▸ [AWS Route 53](<https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html>)
  * ▸ [Cloudflare](<https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/>)
  * ▸ [Bluehost](<https://www.bluehost.com/help/article/dns-management-add-edit-or-delete-dns-entries>)
  * ▸ [Hostinger](<https://www.hostinger.com/tutorials/how-to-use-hostinger-dns-zone-editor>)
  * ▸ [InMotion](<https://www.inmotionhosting.com/support/domain-names/create-cname-record/>)


* * *

4

### Dedicated Sending Domains for Calendar Emails

You can assign dedicated sending domains specifically for Calendar emails (confirmations, reminders, reschedules) to protect deliverability for time-sensitive appointment communications.

① Go to Settings → Email Service → SMTP Service

![SMTP Service settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064125555/original/Dy-QEZM3XvMs3u8XmtdQ29qdiEk6YH7vMw.png?1770150834)

② Select Dedicated Domain and IP

![Dedicated Domain and IP](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064125509/original/617xc1HLrTXNE-33RpoYWkoBCPkU6T-nZw.png?1770150765)

③ Under Domain Configuration → Calendar, add up to 5 domains

![Calendar domain dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064125759/original/T6e4IJkNkOpE5WWg4LVsxbIJt0zqHwPX-w.png?1770151371)

④ Set percentage-based distribution across multiple Calendar domains

![Distribution settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064125862/original/PJo--R5OwIcyYgi5iiKypuhjotEyGck1PA.png?1770151576)

Only sub-account–created domains are available for selection. This feature is available for **LC Email users only**.

?

## Set Up Google Postmaster Tools

For your dedicated sending domain

Google Postmaster Tools (GPT) helps you monitor Gmail-specific deliverability for your HighLevel dedicated sending domain. Track domain/IP reputation, spam rate, authentication alignment, and delivery errors to diagnose inboxing issues and improve performance.

1

Sign in to Google Postmaster Tools

Visit [gmail.com/postmaster](<https://gmail.com/postmaster/>) with a Google account.

2

Add your domain (e.g., `yourbrand.com` or `mail.yourbrand.com`)

![GPT add domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064881962/original/qmIt0mt7eOEjspzPldDL1WuWoDHfmqav5Q.jpeg?1770994245)

3

Choose Verify and copy the TXT record

![GPT TXT record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064882021/original/0t5JorwG7N5BNjfTtJP0EcRwEQaQvrCT8g.png?1770994314)

4

Add TXT record to your DNS host exactly as shown, then save

![Add TXT to DNS](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064888368/original/zt-XcQXZF4ZbVfVswWouRQGDDnWwyqCQZQ.png?1770996887)

5

Return to GPT and complete verification. Google may take some time to detect the record.

6

Send email from HighLevel using your verified dedicated domain.

7

After Google collects sufficient volume, review **Domain Reputation** , **IP Reputation** , **Spam Rate** , **Authentication** , and **Delivery Errors** dashboards.

?

## Shared Domain Email Refactoring

When using a shared sending domain (HighLevel-owned or an Agency Shared Domain), HighLevel automatically refactors the actual sent address to match the shared-domain infrastructure.

### How It Works

HighLevel keeps the From address you configured, but rewrites the sending address behind the scenes using a "plus" format:

# From address (as configured)

test@gohighlevel.com

# Shared domain (account-level)

mg.msgsndr.com

# Actual sent address

test+gohighlevel.com@mg.msgsndr.com

Applies To:

  * All agency sub-accounts created after August 26th
  * All locations under these agencies using shared domains
  * Refactoring will be automatically applied to all existing agencies within the next 2 weeks


Existing agencies are **not impacted yet**. The same functionality is planned to be available in **Labs** for existing agencies for testing and gradual rollout.

✅

To avoid email refactoring and maintain your brand identity:

Set up a dedicated sending domain following the steps in this article. With a dedicated domain, your emails send exactly as configured — no modifications.

?

## Troubleshooting Dedicated Sending Domains

Below are common issues you may encounter when setting up your dedicated sending domains, along with how to resolve them without contacting support.

?

Error: "Domain already pointing to email server!"

This means your domain already has DNS records connected to a different service. You'll need to remove any existing **MX** or **SPF records** (even HighLevel ones) before connecting it here.

Use a free lookup tool to check your current records: [mxtoolbox.com/SuperTool.aspx →](<https://mxtoolbox.com/SuperTool.aspx>)

❓

## Frequently Asked Questions

  


  


  


  


  


  


  


  


Q: How do I choose a sending domain name for my account?

Use a unique subdomain not used for any other purpose. For example, if your root domain is **yourbrand.com** , create a subdomain like `mg.yourbrand.com` where **"mg"** is the subdomain portion.

Q: How do I set up a dedicated IP address?

Setting up a dedicated IP address is a separate process. [Click here to learn more about dedicated IP addresses →](<https://help.gohighlevel.com/en/support/solutions/articles/155000001152>)

Q: What do I do if some DNS records are not verified yet?

Force the verification process manually. If records still aren't verified after that, contact your hosting provider — there may be an issue they can help resolve on their end.

Q: How do I generate an SSL certificate for dedicated sending domains?

The SSL certificate is automatically generated when your domain is verified. If it's showing as verified but no SSL exists, re-verify by going through the full verification process again. If that doesn't work, contact your hosting provider.

Q: What if my domain has a wildcard DNS record?

Wildcard records (e.g., `*.yourdomain.com`) act as catch-alls, so any subdomain already "exists" by default — this causes a "pre-existing record" error.

**Fix:** Temporarily remove the wildcard record, verify the dedicated domain, then add the wildcard back. Alternatively, manually add DNS records for each subdomain to override the wildcard.

Q: Will my recipients see the refactored email address?

Yes — recipients will see the refactored sending address (e.g., `support+yourbusiness.com@mg.msgsndr.com`) in their email client.

Q: How can I prevent my email addresses from being refactored?

Set up a dedicated sending domain. With a dedicated domain, your emails will send with your exact From address — no modifications applied.

Q: Does refactoring affect my reply-to address?

No — refactoring only affects the sending address. Your reply-to address remains exactly as configured.

  


**Q: What is the differenc e between the sending email address and the reply-to email address? Can I use my root domain instead of a subdomain?**

  


The sending email address (From address) is used to send emails and must be authenticated using a dedicated sending domain, typically set up as a subdomain. The reply-to email address is where recipient replies are delivered and can be configured independently without requiring domain authentication.

  


While your From address can appear as a root domain email, using a subdomain for sending is recommended to protect domain reputation and improve deliverability. You can still set the reply-to address to your root domain email to receive replies in your main inbox.

Related Articles

[ ? Email Sending Guide: Email Best Practices & Email Warm Up ](<https://help.gohighlevel.com/en/support/solutions/articles/155000001021>)

# How to Add a Domain and Verify DNS Record

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002220-how-to-add-a-domain-and-verify-dns-record](https://help.gohighlevel.com/support/solutions/articles/155000002220-how-to-add-a-domain-and-verify-dns-record)  
**Category:** Email  
**Folder:** LC Email

---

Email Infrastructure

Adding & Verifying Your Domain

Protect your brand, prevent spoofing, and improve inbox placement by authenticating your sending domain.

What You'll Learn

Adding and verifying your domain is an essential step to ensure secure and reliable email delivery. This process protects your brand reputation, prevents spoofing, and increases the chances of your emails landing in the inbox instead of spam.

This article will guide you through adding your domain, verifying DNS records, and troubleshooting common issues.

Table of Contents

1

What You'll Need Before You Start

2

Step 1: Add Your Domain

3

Step 2: Verify Your Domain

4

After Verification

5

Troubleshooting Common Issues

6

Frequently Asked Questions

1

## What You'll Need Before You Start

Before setting up your domain, make sure you have the following in place:

  * Access to your DNS provider's control panel (Cloudflare, GoDaddy, AWS Route 53, Namecheap, Google Domains, etc.) — log in to wherever your domain is currently hosted and add the required records there.
  * The domain or subdomain you want to use for sending emails.
  * Credentials or permissions to add/edit DNS records.
  * A basic understanding of DNS record types (SPF, DKIM, DMARC, CNAME, TXT, MX).


2

## Step 1: Add Your Domain

Adding your domain is the first step toward email authentication. Follow the three steps below.

Step 1

Access Dedicated Domains

Navigate to **Settings → Email Services → Dedicated Domain & IP**.

![Settings > Email Services > Dedicated Domain & IP navigation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053797876/original/QX6-2-QGltHkBgYk-vToXdQZ3T9ECRHWoA.png?1757947789)

Step 2

Add Domain

Inside the **Dedicated Domains** menu, click **\+ Add Domain** at the top right corner.

![Add Domain button in the Dedicated Domains menu](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053797941/original/WXqTJ3QH216r_zijFc0qvVi1OVoxJolaeA.png?1757947835)

Step 3

Add Domain Details

Enter the domain or subdomain you want to use. We recommend using a subdomain (e.g., **mail.yourdomain.com**) for better deliverability. Then click **Add & Verify**.

![Add domain details form with subdomain entry and Add & Verify button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053798546/original/rK-bp-KmrNeVDP10evTY13GeeuO5z0gdnw.png?1757948031)

3

## Step 2: Verify Your Domain

Verification ensures your emails are authenticated and trusted by inbox providers. This involves setting up DNS records for your domain.

What DNS Record Types Are Needed & Why

Record| Purpose  
---|---  
SPF| **Sender Policy Framework** — Authorizes which servers can send emails on behalf of your domain.  
DKIM| **DomainKeys Identified Mail** — Adds a digital signature to your emails proving they haven't been altered in transit.  
DMARC| **Domain-based Message Authentication, Reporting & Conformance** — Enforces authentication policies and provides reporting on email delivery.  
  
![DNS record types required for domain verification: SPF, DKIM, and DMARC](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053798663/original/XPwCzaCP9KTSX6rsPHTQj5cGnCYT_-PaoA.png?1757948102)

Verifying Your Domain from the Menu

Once your domain is added, open the **three-dot menu** next to it and click **Verify domain**. This tells the system to check whether your DNS records are correctly configured.

![Three-dot menu with Verify domain option highlighted](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053799931/original/nKdX5oSwO0xNf_65ogodozDF6X7vMVHnEw.png?1757948731)

Checking Your DNS Records

After clicking **Verify domain** , you'll see a list of all DNS records your domain requires (SPF, DKIM, CNAME, MX, and DMARC). Each record shows its current verification status, and you can use the **Copy** buttons to paste values directly into your DNS provider. Once all records check out, your domain will be marked as verified.

![DNS records verification list showing status for each required record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053867806/original/pRQ-Oa9_dyPPKdZ6l7IEC4rZYNnrihAhJA.png?1758026774)

DNS Configuration

Choose Your Setup Method

Configure DNS records automatically if your provider is supported, or enter them manually.

Option 1

Auto-Configure via DNS Provider Integration

This is the simplest method if your DNS provider is supported.

  1. After adding your domain, click **Continue**.
  2. The platform will detect your DNS provider (e.g., Cloudflare, GoDaddy, Namecheap).
  3. Log in and authorize Lead Connector to configure your DNS records automatically.
  4. Once completed, your domain will be marked as **Verified**.


Note

If your DNS provider isn't supported for auto-configuration, you'll be prompted to set up records manually instead.

![Auto-configure DNS provider integration authorization screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053797760/original/1B4vPtUrNt_fg8-Q06IDWSn4UYSWCAXQgw.png?1757947702)

Option 2

Manual DNS Setup

If auto-configure isn't available, add DNS records manually. The platform will provide the exact records you need. Follow these general guidelines:

  * **Type:** Add records as TXT, CNAME, or MX as instructed.
  * **Name / Host:** For root domains use "@". For subdomains (e.g., mail.yourdomain.com), enter only the subdomain part (e.g., "mail").
  * **Value:** Copy and paste the values exactly as shown — do not alter them.
  * **TTL:** Set to 5 minutes (300 seconds) where possible.


![Manual DNS record entry fields showing Type, Name, Value, and TTL](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053797699/original/O1xyu5hnbNCZBVZ1ca3aJEQcYMRYLOJJbw.png?1757947671)

Examples by DNS Provider

Cloudflare

  1. Log into Cloudflare.
  2. Go to your domain's **DNS** settings.
  3. Add the records provided (TXT, CNAME, MX). Make sure records are set to **DNS only** (gray cloud) — not Proxied.


GoDaddy

  1. Log into GoDaddy.
  2. Open **Domains → Manage DNS**.
  3. Click **Add** and enter each record.


AWS Route 53

  1. Open the AWS console.
  2. Go to **Route 53 → Hosted Zones**.
  3. Create the necessary record sets.


Namecheap

  1. Log into Namecheap.
  2. Go to **Domain List → Manage → Advanced DNS**.
  3. Add the DNS records provided.


Google Domains

  1. Log into Google Domains.
  2. Select your domain and go to **DNS settings**.
  3. Add the DNS records accordingly.


4

## After Verification

Once your records are verified, here's what to expect and what to do next:

  * **SSL Certificate Issued:** An SSL certificate is automatically issued — this typically takes 1–10 minutes after verification completes.
  * **Domain Status:** Your domain will show as **Verified / Active** in the platform.
  * **Test Sending:** Send test emails to confirm SPF and DKIM pass in the email headers.
  * **Monitor Deliverability:** Use DMARC reports and inbox placement testing tools to track ongoing performance.


You're All Set

Your domain is now authenticated and ready for sending. Continue monitoring your DMARC reports regularly to catch any deliverability issues early.

5

## Troubleshooting Common Issues

If verification fails, work through the following checklist:

  * Double-check that each record matches exactly as provided — even a single character difference can cause failure.
  * Ensure you selected the correct **record type** (TXT, CNAME, or MX).
  * Verify the **Host / Name** field is correct — avoid adding extra "@" symbols or omitting the subdomain portion.
  * Check if **TTL** is set too high — lower it to 300 seconds (5 minutes) if possible to speed up propagation.
  * Be patient: DNS propagation can take up to 24–48 hours depending on your provider.
  * For DMARC: Ensure only **one DMARC record** exists per domain — multiple records will cause authentication to fail.
  * For SPF: Ensure there are no **duplicate SPF records** — only one SPF TXT record should exist per domain.


Tip

After updating DNS records, wait a few minutes then click **Verify domain** again from the three-dot menu to re-trigger the verification check.

6

## Frequently Asked Questions

Q: Should I use a root domain or a subdomain?

We recommend using a subdomain (e.g., mail.yourdomain.com) to protect your root domain's reputation. If deliverability issues arise, isolating email on a subdomain prevents them from affecting your main domain.

Q: How long does domain verification take?

Typically within 1–10 minutes, but in rare cases DNS propagation can take up to 24–48 hours depending on your provider's TTL settings.

Q: What if my DNS provider isn't supported for auto-configuration?

Use the manual setup option instead. The platform provides all exact values you need to copy and paste directly into your DNS provider's control panel.

Q: Do I need a DMARC record for both my root domain and subdomain?

No. If a DMARC record is already set on your root domain, you don't need to add it again for the subdomain — the root domain policy applies to subdomains by default.

Q: What happens if I misconfigure SPF or DKIM?

Emails may land in spam or fail authentication checks entirely, significantly reducing deliverability. Always double-check your records against the provided values before triggering verification.

Q: Can I add multiple domains?

Yes. You can add and verify multiple dedicated domains or subdomains from **Settings → Email Services → Dedicated Domain & IP**. Each domain goes through the same verification process.

Q: Why is Cloudflare proxying causing verification to fail?

In Cloudflare, ensure your DNS records are set to **DNS only** (gray cloud icon), not **Proxied** (orange cloud). Proxying CNAME records used for email authentication is not supported and will cause verification failure.

Q: What does "SSL Certificate Issued" mean after verification?

After your domain verifies, an SSL certificate is automatically issued to secure connections associated with your sending domain. This completes within 1–10 minutes and is required before the domain becomes fully active.

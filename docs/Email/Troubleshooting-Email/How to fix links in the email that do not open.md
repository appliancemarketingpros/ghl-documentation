# How to fix links in the email that do not open?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001151622-how-to-fix-links-in-the-email-that-do-not-open-](https://help.gohighlevel.com/support/solutions/articles/48001151622-how-to-fix-links-in-the-email-that-do-not-open-)  
**Category:** Email  
**Folder:** Troubleshooting Email

---

Email Deliverability

Fixing Links That Don't Open in Emails

Diagnose and resolve tracking-domain and DNS issues that stop links in your emails from opening.

Overview

If links in your emails aren't opening, it's usually caused by an issue with your tracking domain or DNS configuration. This article walks through why this happens and provides steps to troubleshoot and fix the issue.

Table of Contents

1

What Causes Email Links to Not Open?

2

How to Fix Links in Emails That Do Not Open

3

Troubleshooting Common Issues

4

FAQ

5

Related Articles

Video Walkthrough

Note

This video example uses Mailgun, but the same principles apply to all providers.

1

## What Causes Email Links to Not Open?

Email links usually don't open because the **tracking domain isn't set up correctly** or isn't resolving in DNS.

When an email is sent, the link is rewritten so it passes through a tracking domain before sending the recipient to the final page. If that tracking domain has a DNS or SSL issue, the redirect breaks and the link won't open.

To fix this, make sure your tracking domain is configured properly: the correct CNAME record is in place, the domain resolves in DNS, and HTTPS/SSL is active. Once these are set correctly, the redirect works again and your links will open normally.

Note

Link tracking (redirecting links through a tracking domain) is used by most email providers to enable click tracking and ensure proper link routing. However, [Email Tracking](<https://help.gohighlevel.com/en/support/solutions/articles/155000003213>) (such as open and click reporting on the platform) is only available when using LC Email.

![Email link tracking overview](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070162151/original/K15npCUzv1qi8NIKobiSJza24O7kCZaQaA.png?1777399256)

### How Email Link Redirects Work

Understanding how links behave behind the scenes makes it easier to diagnose why they fail.

1

Your original link is replaced with a tracking link.

2

The tracking link routes through a subdomain (e.g., `email.yourdomain.com`).

3

This subdomain relies on a **CNAME record** in your DNS.

4

If the DNS or SSL is misconfigured, the redirect fails and the link may not open.

2

## How to Fix Links in Emails That Do Not Open

Step 1

Identify your tracking domain

From your Agency Dashboard, go to **Settings → Email Services → Location Settings**.

Find the domain used for email tracking (e.g., `email.yourdomain.com`) for the location you're troubleshooting.

![Location Settings tracking domain field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070163225/original/dBsHWHN98kdOUSD_rBfWPAvHnlo6zpbIGg.png?1777400124)

Step 2

Look up your CNAME record

Go to [MX Toolbox](<https://mxtoolbox.com/CnameLookup.aspx>) or [Whatsmydns](<https://www.whatsmydns.net/>) to look up the CNAME record for your tracking lookup domain.

1\. Copy your tracking domain from Step 1 (e.g., `mg.yourdomain.com`)  
2\. Add `email.` in front → `email.mg.yourdomain.com`

**For example:**

  * If you set up `mg.companyname.com`, look up the CNAME record for `email.mg.companyname.com`
  * If you set up `replies.companyname.com`, look up the CNAME record for `email.replies.companyname.com`
  * If you set up `support.companyname.com`, look up the CNAME record for `email.support.companyname.com`


The result should return a valid CNAME record. If you see **"DNS record not found,"** your CNAME is missing or incorrect.

![CNAME lookup result example 1](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070243288/original/lvHcfFvJJgGbWq7VDpBDC_OV4l3Os5cNcA.png?1777480548)

![CNAME lookup result example 2](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070244734/original/CRtpx0qOclPZf4bzq6WDfJRHbxBkXP4PTg.png?1777481515)

Step 3

Verify the CNAME record with your DNS provider

Log in to your DNS provider and locate the CNAME record for your tracking domain. Ensure:

  * The host is only the subdomain (e.g., `email.mg`, not the full domain)
  * The value points to your provider's tracking domain


![CNAME record in DNS provider](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070247826/original/VPNK5vb32wmqp5BoP-7oNByINEQrRKImNQ.png?1777484783)

Step 4

Ensure HTTPS is enabled

Tracking domains must support HTTPS. Go to your provider settings and ensure the tracking protocol is set to HTTPS. Wait for SSL provisioning if it was recently updated.

[More information on how to enable HTTPS tracking links](<https://help.mailgun.com/hc/en-us/articles/360011566033-How-to-Enable-HTTPS-Tracking-Links>)

![HTTPS tracking setting](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070244057/original/9J_4NYHimCj5o882fj48_Kwu5hTXhTeERA.png?1777481018)

Step 5

Test your links

Send a test email from the platform. Click the link and confirm it redirects properly to the final URL.

Step 6

Contact support if the issue persists

If your links still don't open, contact your **domain/DNS provider** (e.g., GoDaddy, Cloudflare, Google Domains) and:

  * Ask them to verify that your **CNAME record for the tracking domain is correctly set up and resolving**
  * Share screenshots of your DNS records for faster troubleshooting


If your DNS provider confirms everything is correct and the issue continues, [contact Support](<https://help.gohighlevel.com/en/support/solutions/articles/155000000969>).

![Example DNS record screenshot to share with support](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070244555/original/SFX68oZGxh9oG7a6deTu8uvYoUBRbkC0lA.png?1777481329)

3

## Troubleshooting Common Issues

Even after following the setup steps, some configurations can still cause links to fail. Reviewing these common issues can help you quickly identify what might still be wrong.

  * **CNAME record not found:** if MX Toolbox shows "DNS record not found," the tracking domain CNAME is missing. Re-add the record with your DNS provider.
  * **Wrong CNAME value:** the CNAME must point to your email provider's tracking host. If it points elsewhere, links won't redirect properly.
  * **Using the full domain in the Host field:** in most DNS providers (like GoDaddy or Namecheap), you should only enter the subdomain (e.g., `email` or `email.mg`), not the full domain like `email.yourdomain.com`.

Correct host name format (common setups):

    * If your subdomain is `mg.companyname.com` → host should be `email.mg`
    * If your subdomain is `replies.companyname.com` → host should be `email.replies`
    * If your subdomain is `support.companyname.com` → host should be `email.support`
  * **Cloudflare proxy enabled:** if you're using Cloudflare, the record must be set to DNS Only (no proxy).
  * **HTTPS not enabled:** some providers require HTTPS tracking to be enabled in their settings. If HTTP is used or SSL isn't active, links may fail to open.
  * **DNS not fully propagated:** after making changes, it can take up to 24–48 hours for DNS updates to apply globally.


4

## FAQ

Q: Why do links work in some email clients but not others?

Some clients cache DNS or SSL certificates differently, or apply their own link-safety scanning. If the tracking domain's CNAME or SSL is only partially propagated, you can see inconsistent behavior across clients until propagation finishes.

Q: How long does it take for DNS changes to fully propagate?

Typically up to 24–48 hours, though it's often much faster. Use MX Toolbox or Whatsmydns to check propagation status before assuming the fix didn't work.

Q: Should I use my root domain or a subdomain for tracking?

Use a subdomain (e.g., `email.yourdomain.com`). It isolates tracking traffic from your main domain and avoids conflicts with existing DNS records on the root domain.

Q: My DNS looks correct in Cloudflare but links still fail — why?

Check whether the record is proxied (orange cloud) in Cloudflare. Tracking CNAME records must be set to DNS Only (gray cloud) — a proxied record breaks the redirect.

Q: Does this issue only affect LC Email, or all providers?

Tracking-domain and DNS misconfiguration can break link redirects on any email provider, not just LC Email. The open/click reporting feature itself, however, is only available when sending through LC Email.

Q: How can I confirm HTTPS tracking is actually active?

Send yourself a test email, hover over (or click) a link, and check that the resolved URL starts with `https://` rather than `http://`. You can also check your certificate status directly in your provider's tracking domain settings.

Related Articles

[Email Tracking for LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/155000003213>) [Google Dedicated Sending Domain Setup (LC Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001240481>) [How to Add a Domain and Verify DNS Records](<https://help.gohighlevel.com/en/support/solutions/articles/155000002220>) [Connecting Your Domain - A Guide](<https://help.gohighlevel.com/en/support/solutions/articles/155000005132>)

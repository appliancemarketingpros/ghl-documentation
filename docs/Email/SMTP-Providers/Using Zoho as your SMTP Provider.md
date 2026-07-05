# Using Zoho as your SMTP Provider

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001173743-using-zoho-as-your-smtp-provider](https://help.gohighlevel.com/support/solutions/articles/48001173743-using-zoho-as-your-smtp-provider)  
**Category:** Email  
**Folder:** SMTP Providers

---

Email Infrastructure

Configuring Zoho as Your SMTP Provider

The exact outgoing server settings for connecting Zoho Mail as your SMTP provider, for both personal and domain-based accounts.

Overview

SMTP (Simple Mail Transfer Protocol) is what reliably delivers email sent from the platform. Using Zoho Mail's SMTP server can help ensure smooth, consistent delivery for your outbound messages.

This guide covers the outgoing server settings for both personal Zoho accounts and domain-based organization accounts, plus a few common configuration gotchas.

Table of Contents

1

Outgoing server settings for personal email users

2

Outgoing server settings for domain-based organizations

3

Frequently Asked Questions

Video Walkthrough

Reference

If you also need incoming mail settings, see Zoho's [Zoho Mail IMAP Server Details](<https://www.zoho.com/mail/help/imap-access.html>).

1

## Outgoing server settings for personal email users

For personal accounts with an address like **username@zoho.com** , use these settings:

Setting| Value  
---|---  
Outgoing Server Name| smtp.zoho.com  
Port| **465** with SSL — or — **587** with TLS  
Require Authentication| Yes  
  
Tip

Learn more about [Why Can't I Use My Free Email Address As The SMTP?](<https://help.gohighlevel.com/en/support/solutions/articles/48001063376>)

2

## Outgoing server settings for domain-based organizations

For organization accounts with a domain-based address like **you@yourdomain.com** , use these settings:

Setting| Value  
---|---  
Outgoing Server Name| smtppro.zoho.com  
Port| **465** with SSL — or — **587** with TLS  
Require Authentication| Yes  
Username| Your Zoho username or full Zoho Mail address (you@yourdomain.com)  
Email Address| Your Zoho Mail address (you@yourdomain.com)  
Password| Your Zoho account password (an app-specific password is required if two-factor authentication is enabled)  
  
Note

If two-factor authentication is enabled on your Zoho account, you'll need to generate an [application-specific password](<https://www.zoho.com/mail/help/adminconsole/two-factor-authentication.html#alink5>) and use that in the password field instead of your regular Zoho password.

3

## Frequently Asked Questions

Q: Should I use smtp.zoho.com or smtppro.zoho.com?

Use **smtp.zoho.com** for a personal @zoho.com address. Use **smtppro.zoho.com** if your domain is hosted with Zoho and your email address is on a custom domain (you@yourdomain.com).

Q: Should I use port 465 or port 587?

Both work. Port 465 uses SSL and port 587 uses TLS. If one doesn't connect, try the other — it's usually a firewall or network restriction rather than a Zoho-side issue.

Q: Do I need an app-specific password?

Only if two-factor authentication is enabled on your Zoho account. In that case, your regular password won't work for SMTP — generate an application-specific password instead.

Q: Can I use a free personal Zoho address as my SMTP sender?

You can connect it, but sending high volumes of automated or bulk mail from a free personal address is more likely to hit provider sending limits or deliverability issues than a domain-based account.

Q: Is there a sending limit with Zoho SMTP?

Yes, Zoho enforces daily sending limits that vary by plan. Check your Zoho Mail plan details if you're sending in volume.

Q: Can I use a Zoho Mail alias as my sender address?

Generally yes, as long as the alias is verified in your Zoho account. Authenticate with your primary Zoho credentials and set the alias as the visible sender address.

Related Articles

[How to Setup Other SMTP Providers](<https://help.gohighlevel.com/support/solutions/articles/48001059689-setting-up-smtp-providers>) [Why Can't I Use My Free Email Address As The SMTP?](<https://help.gohighlevel.com/en/support/solutions/articles/48001063376>)

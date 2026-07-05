# When email replies are not showing up in Conversation

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001185819-when-email-replies-are-not-showing-up-in-conversation](https://help.gohighlevel.com/support/solutions/articles/48001185819-when-email-replies-are-not-showing-up-in-conversation)  
**Category:** Email  
**Folder:** Troubleshooting Email

---

Email Infrastructure

Email Replies Not Coming Back to the Conversation

Diagnose and fix missing reply threads caused by Mailgun setup, MX records, or domain/DNS provider issues.

Overview

This guide troubleshoots issues with email replies not appearing in conversations. This can be caused by several factors, like an incorrect Mailgun setup, faulty MX records, or issues with domain providers like WIX. Follow these steps to diagnose and resolve the issue efficiently.

Table of Contents

1

Troubleshooting steps

→ 1. Check if the Mailgun receiving route is set up → 2. How to check MX records → 3. Check if you're using the root domain with Google Workspace and Mailgun → 4. Double-check DNS records → 5. If you're using an SMTP provider instead of Mailgun/LC Email → 6. If you're using WIX as your domain/DNS provider

2

Frequently Asked Questions

3

Related Articles

1

## Troubleshooting: Email Replies Not Coming Back to the Conversation

Step 1

Check if the Mailgun receiving route is set up

If you're on LC Email, you can skip this step and move on to Step 2.

[How to set up replies in Mailgun](<https://help.gohighlevel.com/en/support/solutions/articles/48000987293>)

Step 2

How to check MX records

The MX record is essential for Mailgun to track replies.

1\. Switch to **agency view → Settings → Email Services → Location Settings** and copy the domain/subdomain set up for the sub-account.

![Location Settings domain field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033710730/original/336fiUo3ihzu_yI4uP56rIgrHdF3mahwKA.jpg?1727465017)

2\. Go to [MX Toolbox](<https://mxtoolbox.com/>) to look up the MX record for the subdomain/domain you copied.

Depending on the subdomain you set up with Mailgun, for example:

  * If you set up `companyname.com`, you'll look up the MX record for `companyname.com`
  * If you set up `replies.companyname.com`, you'll look up the MX record for `replies.companyname.com`


  * Check whether two records point to `mxa.mailgun.org` and `mxb.mailgun.org`
  * If they're missing, add **mxa.mailgun.org** and **mxb.mailgun.org** and set priority 10 for both MX records


![MX record lookup result](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033710796/original/FM2Sxy9BQzzbC3CnquDFbcq0gzPPlYBQZw.jpg?1727465126)

Tip

If other records point to other email servers (e.g., Google Workspace), you can only choose one. You'll need to either set up a subdomain for Mailgun, or not use the domain for other email servers. See [Can I use the same domain name for Mailgun and Google Apps (or another email server)?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

Still Not Working?

Share a screenshot of all the DNS records in your domain provider (GoDaddy, Namecheap, etc.) and [reach out to support here](<https://help.gohighlevel.com/en/support/solutions/articles/48001204857>). You can also check with your domain provider's support to see what's missing.

Step 3

Check if you're using the root domain with Google Workspace and Mailgun

If you're setting up a root domain to use with Mailgun, make sure it isn't pointing elsewhere too (like Google Workspace), as this can conflict when the same domain is used for work email through Google Workspace or Outlook. See [Can I use the same domain name for Mailgun and Google Apps (or another email server)?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

If you use MX Toolbox to look up the MX record for the root domain and it's pointing to both Mailgun **and** another email server (e.g., Google Workspace), you can only choose one. You'll need to either set up a subdomain for Mailgun, or not use that domain for other email servers.

![MX record pointing to Mailgun and another server](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033710845/original/rGC1BTGGbHk5MNi82nlWRVyA9Di8s7ocRA.jpg?1727465286)

Step 4

Double-check DNS records

Log in to [Mailgun](<https://login.mailgun.com/login/>):

1\. Expand the **Sending** tab  
2\. Click the last menu item, **Domain Settings**  
3\. Make sure the correct domain/subdomain for the location is selected at the top  
4\. Click **DNS records** in the top middle  
5\. Click **Verify DNS settings** and check whether all 5 DNS records — especially the MX record — show a green checkmark

Tip

Sometimes the checkmarks show green even when a record isn't actually correct. Click **Verify DNS Settings** again to refresh and re-check the records.

![Mailgun DNS records verification screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033710882/original/n5TrO-ghOMdCcUoKy1eLVCyu09YJz5OnAA.jpg?1727465373)

Step 5

If you're using an SMTP provider instead of Mailgun/LC Email

![SMTP provider reference screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48283738240/original/iuhABh85E9KeBQj_tREvrShtALdHnMmXAA.png?1677272715)

Step 6

If you're using WIX as your domain/DNS provider

Check out [Mailgun replies not working when using WIX as the domain provider](<https://help.gohighlevel.com/support/solutions/articles/48001188738-mailgun-replies-not-working-when-using-wix-as-the-domain-provider>).

2

## Frequently Asked Questions

Q: Can I customize the email address that replies are sent to?

Yes, you can usually customize the "reply-to" email address in your settings. This lets you route replies to a specific address, which can help manage communications more effectively.

Q: How can I integrate other email providers to improve reply visibility?

Integrating other email providers can often enhance functionality. Check the platform's integration options to connect services like Gmail or Outlook, which may provide better tracking and visibility for email replies.

Q: What should I do if the issue persists despite troubleshooting?

If troubleshooting doesn't resolve the issue, reach out to support for further assistance. They can provide insights specific to your account and help identify any underlying issues.

Q: Do I need to repeat this setup for every sub-account or location?

Yes. MX records and receiving routes are configured per domain/subdomain, so each sub-account using its own sending domain needs its MX and DNS records verified separately.

Q: How do I know if my MX record changes have propagated yet?

Use MX Toolbox to re-run the lookup for your domain/subdomain. If it still doesn't show `mxa.mailgun.org` and `mxb.mailgun.org`, give it a bit more time — DNS propagation can take up to 24–48 hours.

Related Articles

[How to send a test email in conversations](<https://help.gohighlevel.com/support/solutions/articles/48001208887-how-to-send-a-test-email-in-the-conversation>) [Troubleshooting when conversations are glitching](<https://help.gohighlevel.com/support/solutions/articles/48001184861-troubleshooting-when-conversations-are-glitching>)

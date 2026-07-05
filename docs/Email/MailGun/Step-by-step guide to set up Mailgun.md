# Step-by-step guide to set up Mailgun

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001219824-step-by-step-guide-to-set-up-mailgun](https://help.gohighlevel.com/support/solutions/articles/48001219824-step-by-step-guide-to-set-up-mailgun)  
**Category:** Email  
**Folder:** MailGun

---

EMAIL INFRASTRUCTURE

Mailgun Step-by-Step Setup Guide

Sign up for Mailgun, add your sending domain, configure your DNS records, and send your first test email.

What You'll Learn

This guide walks you through creating a Mailgun account, adding a sending domain, choosing between a main domain and a subdomain, publishing the required DNS records, and confirming everything works with a test email.

Table of Contents

1

Sign Up for Mailgun

2

Verify Your Email Address

3

Add a New Sending Domain

4

Choose a Main Domain or Subdomain

5

Add Your DNS Records

6

Get Your API Key & Send a Test Email

7

Frequently Asked Questions

8

Related Articles

1

## Sign Up for Mailgun

Create your Mailgun account by visiting [signup.mailgun.com/new/signup](<https://signup.mailgun.com/new/signup>).

2

## Verify Your Email Address

Check your email inbox for a message from Mailgun and click the verification link to confirm your account.

![Mailgun signup confirmation screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243535009/original/7tQRdPUgguqaYEpnIV2uS3kIQpMd7jZBZw.png?1659724083)

![Email verification confirmation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243535045/original/kRGmwZtbq3-zkULjp6-Pg0J-7sTNMNHymQ.png?1659724108)

3

## Add a New Sending Domain

From your Mailgun dashboard, click **Sending → Add New Domain**.

![Sending menu with Add New Domain option](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243535197/original/doBfy9jAqoxcOqD5LiuyQO9rnyVWfkkAeg.png?1659724186)

4

## Choose a Main Domain or Subdomain

If your domain is **companyname.com** , you can set up either the main domain or a subdomain with Mailgun.

Option A

Main Domain

If you add the main domain, it should not already be in use with Google Workspace or any other email provider.

Option B

Subdomain

To set up a subdomain with Mailgun, you can type **anything_here.companyname.com**. Examples:

  * mg.companyname.com
  * replies.companyname.com
  * support.companyname.com


Note

Set up the domain or subdomain under the **US** region, not EU. Once you've made your selection, click **Add domain**.

![Add domain form with US region selected](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243536037/original/B5DZocdO2h64MlEDtfuFjER-U_0AO_NOEg.png?1659724559)

Setup Guide

Now let's publish the DNS records

This is the step most setups get stuck on — follow it carefully.

5

## Add Your DNS Records

Log in to your DNS host based on where you registered the domain, and add the 5 DNS records Mailgun provides.

Not Sure Where to Add the Records?

Step 1: Look up your domain in MXToolbox

Search your domain in [MXToolbox](<https://mxtoolbox.com/SuperTool.aspx>). Only enter the domain itself — do not add "http://" in front of it.

![MXToolbox domain lookup search bar](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243537503/original/VQuAatUlq58RsSVIlLqFfKJQsi1EtB2pjg.png?1659725181)

Once you look up the domain, the results will show your DNS hosting provider.

![MXToolbox results showing DNS hosting provider](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243537328/original/O4VqrFqJo6APt8Z_bhPobo_S50QD230bQg.png?1659725095)

Step 2

Check the "reported by" note

MXToolbox will show a note at the bottom naming your host, e.g. "reported by wordpress.com." Once you know your provider, you can add the DNS records in that provider's dashboard. If you're not sure where to find the DNS records area, search "**[provider name] DNS records**."

Based on your domain provider, use one of these step-by-step guides to add the records. If your provider isn't listed, one of these should still be a close match:

[**GoDaddy** — Mailgun domain setup](<https://help.gohighlevel.com/en/support/solutions/articles/48000981678>) [**Namecheap** — Mailgun domain setup](<https://help.gohighlevel.com/en/support/solutions/articles/48000981680>) [**Siteground** — Mailgun domain setup](<https://help.gohighlevel.com/en/support/solutions/articles/48000981685>) [**HostGator** — Mailgun domain setup](<https://help.gohighlevel.com/en/support/solutions/articles/48000981679>) [**Google Domains** — Mailgun domain setup](<https://help.gohighlevel.com/en/support/solutions/articles/48001155148>) [**CloudFlare** — Mailgun domain setup](<https://help.gohighlevel.com/en/support/solutions/articles/48001064413>)

6

## Get Your API Key & Send a Test Email

Once all of your DNS records are added and verified, grab your key from [Mailgun API Key: Where to Find It in Mailgun and Add It to the Platform](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>).

You're Almost Done

Send a test email to confirm everything works. See [How to Send a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>) for the steps.

7

## Frequently Asked Questions

Q: Should I use my main domain or a subdomain?

A subdomain (like mg.companyname.com) is usually the safer choice, since your main domain shouldn't be added if it's already in use with Google Workspace or another email provider.

Q: Why does it matter whether I choose US or EU when adding the domain?

The region determines which Mailgun infrastructure sends your mail. Always select US when setting up your domain or subdomain for this workflow.

Q: I don't know who my DNS provider is — how do I find out?

Look up your domain in MXToolbox. The results page will show a "reported by" note naming your DNS host.

Q: My domain provider isn't in the list of guides — what should I do?

Use one of the listed provider guides as a reference — the process of adding TXT, CNAME, and MX records is similar across most DNS hosts.

Q: How long does it take for DNS records to verify?

DNS propagation can take anywhere from a few minutes to 48 hours, though most records verify within an hour.

Q: My test email didn't go through — what should I check first?

Confirm all 5 DNS records show as verified in Mailgun, and double-check that your API key was entered correctly before sending another test.

Related Articles

[Mailgun API Key: Where to Find It in Mailgun and Add It to the Platform](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>) [How to Send a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>)

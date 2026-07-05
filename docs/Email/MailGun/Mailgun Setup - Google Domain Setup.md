# Mailgun Setup - Google Domain Setup

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001155148-mailgun-setup-google-domain-setup](https://help.gohighlevel.com/support/solutions/articles/48001155148-mailgun-setup-google-domain-setup)  
**Category:** Email  
**Folder:** MailGun

---

Email Infrastructure

Mailgun + Google Domains Setup

Step-by-step DNS configuration for connecting Mailgun to a domain registered with Google Domains.

What You'll Learn

This guide walks through signing up for Mailgun, adding your domain, and configuring the five DNS records Mailgun requires — two TXT records, both MX values, and one CNAME — inside Google Domains.

It also covers how to avoid breaking your existing Google Workspace/Gmail mail delivery while adding Mailgun's records.

Table of Contents

1

Sign up for Mailgun & add your domain

2

Access DNS records in Google Domains

3

Add the 1st TXT record (SPF)

4

Add the 2nd TXT record (DKIM)

5

Add the MX records

6

Add the CNAME record

7

Verify DNS & finish setup

8

Frequently Asked Questions

Video Recap

1

## Sign up for Mailgun & add your domain

Step 1

Sign up at [Mailgun.com](<https://signup.mailgun.com/new/signup>), then check your inbox to verify your email address.

![Mailgun signup confirmation screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382834/original/93q62at2bi41NnpFtGv2FEPRQFFSRfxR7w.png?1677635327)

![Mailgun email verification confirmation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382837/original/cRlyZ3AGCLES6EuDfYfGZsvx1meXvGsPdg.png?1677635328)

Step 2

Log in to Mailgun, then click **Sending → Add New Domain**.

![Sending menu with Add New Domain option in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382836/original/dX85fHXCrcdjQS7AUBN05K-nzvcunlx1CQ.png?1677635327)

Step 3

If your domain is **companyname.com** , decide whether to set up the main domain or a subdomain with Mailgun.

  * **Main domain:** if you use the main domain, it should not also be used with Google Workspace or any other email provider — see [Mailgun's guidance](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->) on sharing a domain with another email server.
  * **Subdomain:** type **ANYTHING_HERE**.companyname.com — for example mg.companyname.com, replies.companyname.com, or support.companyname.com.


Important

Set up the domain or subdomain under the **US** region — not EU.

Click **Add domain**.

![Adding a domain in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382833/original/orhf_0AVhwlQvuxlv2cPV72PZBV30Ec4gw.png?1677635326)

2

## Access DNS records in Google Domains

Now log in to your DNS records and add the 5 DNS records Mailgun requires.

  * Log in to [domains.google.com](<https://domains.google.com>).
  * Click into the domain you're trying to set up.
  * Click **DNS** on the left panel — this is where you'll add all 5 records.


![DNS management screen in Google Domains](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243542584/original/jduaWZZKo0s-PYGnVfTYxkAaGSceLswDuQ.png?1659727406)

3

## Add the 1st TXT record (SPF)

Fields

**Host name:**

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain (companyname.com) → host name is **@**


**Type:** select **TXT** from the dropdown.

**Data:** paste the first copied TXT record — v=spf1 include:mailgun.org ~all.

![TXT record form filled with the SPF value in Google Domains](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243542124/original/92-SiILtsZ5kfbsAEFFhKKjKEM8sGjIWEQ.png?1659727285)

Note

Don't click Save yet — there are 4 more records to add. Once you've finished this record, click **Create new record** and move to the next section.

4

## Add the 2nd TXT record (DKIM)

Fields

**Host name:** this part is a little tricky. Copy everything from the beginning of the value up until the subdomain part — **do not copy the main domain**.

![Example of the host name value to copy for the DKIM record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243542908/original/5vSFtNLEoaRQt2aK8L4rniJCWjLDJy6Vmg.png?1659727560)

Example| Highlighted part to copy  
---|---  
Using a subdomain| ![Example of the host value to copy when using a subdomain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243543383/original/LybPtPP4joO7bl9IEDJ1fwxnIvEiXCedvA.png?1659727679)  
Using the main domain| ![Example of the host value to copy when using the main domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284378839/original/6xJR3U2ek0CgVESacXXEwkHcgsLaOXbjhQ.png?1677631543)  
  
**Type:** select **TXT** from the dropdown.

**Data:** paste the second, longer TXT record here.

![Second TXT record form filled with the DKIM value in Google Domains](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243543480/original/SA3H2iuimeXJJUdD5n5KAwd7ZwCI3qt5gA.png?1659727710)

5

## Add the MX records

Click **Create new record**.

Fields

**Host name:**

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**Type:** select **MX** from the dropdown.

**Data:** Google Domains lets you add both MX values to the same record.

  * Copy and paste 10 mxa.mailgun.org
  * Click **+Add more to this record**
  * Copy and paste 10 mxb.mailgun.org


![Completed MX record with both mailgun values in Google Domains](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243544215/original/laPv0qzJMIw-tvzuWSaNoZUh1BosRw4EOg.png?1659728081)

6

## Add the CNAME record

Click **Create new record**.

Fields

**Host name:**

  * mg.companyname.com → host name is **email.mg**
  * replies.companyname.com → host name is **email.replies**
  * Main domain (companyname.com) → host name is **email**


**Type:** select **CNAME** from the dropdown.

**Data:** copy and paste mailgun.org.

![Completed CNAME record in Google Domains](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243543931/original/4TQk2kmsk4suUaSdEwDrhVPLhdT8fYRTiw.png?1659727913)

7

## Verify DNS & finish setup

Now that you've added all 5 DNS records, click **Save**.

Go back to Mailgun and click **Verify DNS Settings**. If some records still aren't showing a green checkmark, click the same button again — DNS propagation can take a little time.

![Verify DNS Settings button in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48243544863/original/fZ4MWAp_hBYkuUM9L9YEuCRqwG5FLmD8Yw.png?1659728463)

Next Steps

Once all records are verified, grab your [Mailgun API key and add it to your email service settings](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>).

Then send a test email to confirm everything works — see [how to send a test email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>).

8

## Frequently Asked Questions

Q: Why does Google Domains only need one MX record instead of two?

Google Domains lets you add multiple values to a single MX record using "+Add more to this record," so both mxa.mailgun.org and mxb.mailgun.org live under one record instead of two separate ones.

Q: Why shouldn't I click Save after adding just the first record?

You can save at any point, but it's easier to add all 5 records first and save once at the end, rather than saving and reopening the DNS page repeatedly.

Q: Will this affect my existing Google Workspace or Gmail email?

Not if you use a subdomain for Mailgun rather than your main domain, and leave your existing Google Workspace MX records on the main domain untouched.

Q: How long does DNS propagation take in Google Domains?

Usually fast, but it can occasionally take a few hours. If a record isn't showing green yet in Mailgun, wait a bit and click Verify DNS Settings again.

Q: What priority value do I use for the MX record?

Use 10 for both mxa.mailgun.org and mxb.mailgun.org — this is entered right before the value, for example "10 mxa.mailgun.org".

Q: What do I do after all 5 records show a green checkmark?

Grab your Mailgun API key, add it to your email service settings, and send a test email in a conversation to confirm delivery is working.

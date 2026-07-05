# Mailgun Setup - CloudFlare Domain Setup

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001064413-mailgun-setup-cloudflare-domain-setup](https://help.gohighlevel.com/support/solutions/articles/48001064413-mailgun-setup-cloudflare-domain-setup)  
**Category:** Email  
**Folder:** MailGun

---

Email Infrastructure

Mailgun + Cloudflare Domain Setup

Step-by-step DNS configuration for connecting Mailgun to a domain managed through Cloudflare.

What You'll Learn

This guide walks through signing up for Mailgun, adding your domain, and configuring the five DNS records Mailgun requires — two TXT records, two MX records, and one CNAME — inside Cloudflare's DNS Records panel.

It also covers a Cloudflare-specific step that trips people up: switching the CNAME record from Proxied to DNS only.

Table of Contents

1

Sign up for Mailgun & add your domain

2

Access DNS records in Cloudflare

3

Add the 1st TXT record (SPF)

4

Add the 2nd TXT record (DKIM)

5

Add the 1st MX record

6

Add the 2nd MX record

7

Add the CNAME record

8

Verify DNS & finish setup

9

Frequently Asked Questions

Video Recap

1

## Sign up for Mailgun & add your domain

Step 1

Sign up at [Mailgun.com](<https://signup.mailgun.com/new/signup>), then check your inbox to verify your email address.

![Mailgun signup confirmation screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284378416/original/VewuZVN3oFOFIvBdf4XqMAOX4vtVGv_jNg.png?1677630998)

![Mailgun email verification confirmation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284378421/original/GU6IL6Y3N81qm6KMH9aTz7l5FV5IEv7ySA.png?1677630999)

Step 2

Log in to Mailgun, then click **Sending → Add New Domain**.

![Sending menu with Add New Domain option in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284378418/original/kxsnymCeuFAsBWkXaOes6QaaWED2_bfASA.png?1677630999)

Step 3

If your domain is **companyname.com** , decide whether to set up the main domain or a subdomain with Mailgun.

  * **Main domain:** if you use the main domain, it should not also be used with Google Workspace or any other email provider — see [Mailgun's guidance](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->) on sharing a domain with another email server.
  * **Subdomain:** type **ANYTHING_HERE**.companyname.com — for example mg.companyname.com, replies.companyname.com, or support.companyname.com.


Important

Set up the domain or subdomain under the **US** region — not EU.

Click **Add domain**.

![Adding a domain in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382652/original/woVjMqNw3YY_Zjs20LoBHUb4KrThVvj_Rw.png?1677635102)

Tip

The next screen asks you to add DNS records to your domain. Leave this screen open — you'll need it for the next step.

![Mailgun DNS records screen to keep open for the next step](https://help.mailgun.com/hc/article_attachments/8759612958491/Screen_Shot_2022-09-11_at_6.39.22_PM.png)

2

## Access DNS records in Cloudflare

Now log in to your DNS records and add the 5 DNS records Mailgun requires.

Step 1

Log in to the [Cloudflare dashboard](<https://dash.cloudflare.com/login>) and select your account and domain. See Cloudflare's own guide on [creating DNS records](<https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/>) if you'd like more detail.

Step 2

Click on **DNS → Records**.

![DNS Records section in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284386950/original/7Br2BkIKLhDBiHeqj6uRhzUTM68HZihKIQ.png?1677639074)

Step 3

Click **\+ Add Record**. You'll repeat this for each of the 5 records below.

![Add Record button in Cloudflare DNS](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387199/original/vr_JbieNqi07EUV9m4GhTYCExqDcTOc-zw.png?1677639281)

3

## Add the 1st TXT record (SPF)

![Add record form in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387183/original/Y8NTiChTf60Ju-PPIBkxMoPvepF9sUSQqQ.png?1677639258)

Fields

**A. Type:** select **TXT** from the Type menu.

**B. Name:** different for everyone — **do not include the root domain.**

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain (companyname.com) → host name is **@**


**C. Content:** the same for everyone — paste v=spf1 include:mailgun.org ~all.

**D.** Click **Save**.

![Completed first TXT record in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284384681/original/QCbqi3BnzhNKNCspyADXNWBZfk3F55e2dg.png?1677636916)

4

## Add the 2nd TXT record (DKIM)

Click **\+ Add Record** again.

![Adding the second TXT record in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387388/original/pGwHEEJ73iotP2Px-sz8EMcZlT852MZg1g.png?1677639444)

Fields

**A. Type:** select **TXT** from the Type menu.

**B. Name:** this part is a little tricky. Copy everything from the beginning of the value up until the subdomain part — **do not include the root domain.** Everyone's 2nd TXT record name and value are different.

Example| Name to copy| Highlighted part  
---|---|---  
Using a subdomain| mx._domainkey.helpdesk| ![Example of the name value to copy when using a subdomain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380215/original/t6MGY8Bw9AK1Vv01kUxtJAkNwp_4UfYjHw.png?1677632945)  
Using the main domain| mailo._domainkey| ![Example of the name value to copy when using the main domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380223/original/JSERXQQhYNvzVp7YoXhIji_yeomZNLXUKA.png?1677632951)  
  
**C. Content:** head back to Mailgun and copy the 2nd, much longer TXT record — highlighted in the screenshot below — and paste it here.

![Mailgun screen highlighting the long DKIM TXT record to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385043/original/UvAhE3LGN5sYkTb4kyEsXNM0GE0Uc8Eq1Q.png?1677637220)

**D.** Click **Save**.

5

## Add the 1st MX record

![MX records overview in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385538/original/qHcrrZPnp3g0LC4c75qM1hg_opwYUXgE0w.png?1677637720)

Click **\+ Add Record** again.

![Add MX record form in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387485/original/P9K8ytrObBrwMJdpaEBYJYuK3S7Z-iq5yg.png?1677639588)

Heads Up

If you have a Google Workspace account capturing incoming email for your main domain, make sure you're using a subdomain for Mailgun instead. See [Can I Use the Same Domain Name for Mailgun and for Google Apps (Or Another Email Server)?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

Fields

**A. Type:** select **MX** from the Type menu.

**B. Name:** different for everyone —

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**C. Mail Server:** the same for everyone — paste mxa.mailgun.org.

**D. Priority:** 10 — the same for everyone, no matter what domain you're setting up.

**E.** Click **Save**.

6

## Add the 2nd MX record

Click **\+ Add Record** again.

![Add second MX record form in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387662/original/7FOCRV3g2jhAT9ogHOZI9nNtWZiNGsDqlQ.png?1677639703)

Fields

**A. Type:** select **MX** from the Type menu.

**B. Name:** different for everyone —

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**C. Mail Server:** the same for everyone — paste mxb.mailgun.org.

**D. Priority:** 10 — the same for everyone.

**E.** Click **Save**.

7

## Add the CNAME record

![CNAME records overview in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385721/original/3LyKoigujZ-vEjMFQDflCfmRRfAJra3rYA.png?1677637907)

In Cloudflare, click **\+ Add Record** again.

![Add CNAME record form in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387826/original/6ADDI371NG-0XbruZ2zs5EF4QgaagbkXqQ.png?1677639817)

Fields

**A. Type:** select **CNAME** from the Type menu.

**B. Name:** different for everyone. Head back to Mailgun to copy the host name — copy everything from the beginning up until the subdomain part, **do not copy the main domain**.

![Mailgun CNAME host name to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385985/original/OtLw_A4zY8FbLbBKqMB9kUKRaQJO3xpp8A.png?1677638165)

  * mg.companyname.com → host name is **email.mg**
  * replies.companyname.com → host name is **email.replies**
  * Main domain (companyname.com) → host name is **email**


**C. Target:** the same for everyone — paste mailgun.org.

Important — Cloudflare-Specific

**D.** Click the orange cloud icon to switch it from **Proxied** to **DNS only**. If this record stays proxied, Mailgun won't be able to verify it and mail delivery will fail.

**E.** Click **Save**.

![Completed CNAME record set to DNS only in Cloudflare](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387917/original/KyyhGEhxb0QZRZCV2f8MAaNP6jb9n37nvA.png?1677639894)

8

## Verify DNS & finish setup

Now that you've added all 5 records, go back to Mailgun and click **Verify DNS Settings**. If some records still aren't showing a green checkmark, click the same button again — DNS propagation can take a little time.

![Verify DNS Settings button in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387965/original/I7T5QQCSjAnBvT1zqQlVgXSuNdgfuNiM3w.png?1677639928)

Next Steps

Once all records are verified, grab your [Mailgun API key and add it to your email service settings](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>).

Then send a test email to confirm everything works — see [how to send a test email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>).

9

## Frequently Asked Questions

Q: Why does the CNAME record need to be "DNS only" instead of "Proxied"?

Cloudflare's proxy sits in front of the record and changes how it resolves, which breaks Mailgun's ability to verify it. Setting it to DNS only (gray cloud) lets Mailgun see the record directly.

Q: Where do I find the +Add Record button in Cloudflare?

After selecting your domain, go to DNS → Records. The +Add Record button sits at the top of the records table.

Q: Do the TXT and MX records also need to be set to DNS only?

TXT and MX records aren't proxyable in Cloudflare — only records that resolve to a web-facing address (like CNAME and A records) show the proxy toggle. Only the CNAME record needs the DNS-only setting checked.

Q: Will this affect my existing Google Workspace or Gmail email?

Not if you use a subdomain for Mailgun rather than your main domain, and leave your existing MX records for Google Workspace untouched on the main domain.

Q: How long does DNS propagation take with Cloudflare?

Cloudflare's own DNS updates are typically fast, but it can occasionally take a few hours for changes to fully propagate. If a record isn't showing green yet in Mailgun, wait a bit and click Verify DNS Settings again.

Q: What do I do after all 5 records show a green checkmark?

Grab your Mailgun API key, add it to your email service settings, and send a test email in a conversation to confirm delivery is working.

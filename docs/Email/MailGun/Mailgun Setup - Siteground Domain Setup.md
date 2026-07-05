# Mailgun Setup - Siteground Domain Setup

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981685-mailgun-setup-siteground-domain-setup](https://help.gohighlevel.com/support/solutions/articles/48000981685-mailgun-setup-siteground-domain-setup)  
**Category:** Email  
**Folder:** MailGun

---

Email Infrastructure

Mailgun + SiteGround Domain Setup

Step-by-step DNS configuration for connecting Mailgun to a domain hosted with SiteGround.

What You'll Learn

This guide walks through signing up for Mailgun, adding your domain, and configuring the five DNS records Mailgun requires — two TXT records, two MX records, and one CNAME — inside SiteGround's DNS Zone Editor.

It also covers how to avoid breaking your existing Google Workspace/Gmail mail delivery while adding Mailgun's records.

Table of Contents

1

Sign up for Mailgun & add your domain

2

Access DNS records in SiteGround

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

## Access DNS records in SiteGround

Now log in to your DNS records and add the 5 DNS records Mailgun requires.

Step 1

Log in to [SiteGround](<https://login.siteground.com/login?lang=en>). See SiteGround's own guide on [managing DNS records](<https://world.siteground.com/kb/manage-dns-records/#TXT_record_settings>) if you'd like more detail.

Step 2

Go to **Site Tools → Domain → DNS Zone Editor**.

![DNS Zone Editor in SiteGround Site Tools](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284391901/original/ZwLX5zPm5t6xvyGMrcxkIhoPH6U7XtbQsw.png?1677643178)

Step 3

In the **Create New Record** section, you'll repeat the process below for each of the 5 records.

![Create New Record section in SiteGround DNS Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284392257/original/BnfApclXdbWZ_ONRoVqVaZZLCw-m9GTxFw.png?1677643477)

3

## Add the 1st TXT record (SPF)

Fields

**A.** Click on the **TXT** tab.

**B. Name:** different for everyone — **do not include the root domain.**

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain (companyname.com) → host name is **@, or leave it empty**


**C. Value:** the same for everyone — paste v=spf1 include:mailgun.org ~all.

**D.** Click **Create**.

![Completed first TXT record in SiteGround](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284384681/original/QCbqi3BnzhNKNCspyADXNWBZfk3F55e2dg.png?1677636916)

4

## Add the 2nd TXT record (DKIM)

Click **\+ Add Record** again.

![Adding a second record in SiteGround DNS Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284392423/original/WFBDHip6_j3WmEo4nRgIeENzQN-OEFhqqA.png?1677643605)

Fields

**A.** Click on the **TXT** tab.

**B. Name:** this part is a little tricky. Copy everything from the beginning of the value up until the subdomain part — **do not include the root domain.** Everyone's 2nd TXT record name and value are different.

Example| Name to copy| Highlighted part  
---|---|---  
Using a subdomain| mx._domainkey.helpdesk| ![Example of the name value to copy when using a subdomain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380215/original/t6MGY8Bw9AK1Vv01kUxtJAkNwp_4UfYjHw.png?1677632945)  
Using the main domain| mailo._domainkey| ![Example of the name value to copy when using the main domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380223/original/JSERXQQhYNvzVp7YoXhIji_yeomZNLXUKA.png?1677632951)  
  
**C. Value:** head back to Mailgun and copy the 2nd, much longer TXT record — highlighted in the screenshot below — and paste it here.

![Mailgun screen highlighting the long DKIM TXT record to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385043/original/UvAhE3LGN5sYkTb4kyEsXNM0GE0Uc8Eq1Q.png?1677637220)

**D.** Click **Create**.

5

## Add the 1st MX record

![MX records overview in SiteGround](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385538/original/qHcrrZPnp3g0LC4c75qM1hg_opwYUXgE0w.png?1677637720)

Click on the **MX** tab, then select **Add your own MX records**.

![Add your own MX records option in SiteGround](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284392929/original/H-xERjs6rnHBgx2KfGgEYZBZ7Mmkxa_00A.png?1677644034)

Heads Up

If you have a Google Workspace account capturing incoming email for your main domain, make sure you're using a subdomain for Mailgun instead. See [Can I Use the Same Domain Name for Mailgun and for Google Apps (Or Another Email Server)?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

![MX record fields in SiteGround](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284393043/original/KK8SevO7iTJJWSHB-9l9vRPfuZtGzkKxmw.png?1677644111)

Fields

**A. Name:** different for everyone —

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**B. Priority:** 10 — the same for everyone, no matter what domain you're setting up.

**C. Destination:** the same for everyone — paste mxa.mailgun.org.

**D.** Click **Create**.

6

## Add the 2nd MX record

Add another MX record. This time the destination will be mxb.mailgun.org.

![Add second MX record form in SiteGround](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284393336/original/Rwlp0thYONnclsrwYeGKRE6xBW0jl1A2KQ.png?1677644328)

Fields

**A. Name:** different for everyone —

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**B. Priority:** 10 — the same for everyone.

**C. Destination:** the same for everyone — paste mxb.mailgun.org.

**D.** Click **Create**.

7

## Add the CNAME record

![CNAME records overview in SiteGround](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385721/original/3LyKoigujZ-vEjMFQDflCfmRRfAJra3rYA.png?1677637907)

![Add CNAME record form in SiteGround](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284393711/original/khGHMR_qTn12M2FmkiCTjNf8k9lHWO-gDw.png?1677644645)

Fields

**A.** Click on the **CNAME** tab.

**B. Name:** different for everyone. Head back to Mailgun to copy the host name — copy everything from the beginning up until the subdomain part, **do not copy the main domain**.

![Mailgun CNAME host name to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385985/original/OtLw_A4zY8FbLbBKqMB9kUKRaQJO3xpp8A.png?1677638165)

  * mg.companyname.com → host name is **email.mg**
  * replies.companyname.com → host name is **email.replies**
  * Main domain (companyname.com) → host name is **email**


**C. Resolves to:** the same for everyone — paste mailgun.org.

**D.** Click **Create**.

![All 5 DNS records added in SiteGround](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284393881/original/3o8rKOzJY89uxP0iayB1w-9flRZKZ1EM8g.png?1677644794)

8

## Verify DNS & finish setup

Now that you've added all 5 records, go back to Mailgun and click **Verify DNS Settings**. If some records still aren't showing a green checkmark, click the same button again — DNS propagation can take a little time.

![Verify DNS Settings button in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387965/original/I7T5QQCSjAnBvT1zqQlVgXSuNdgfuNiM3w.png?1677639928)

Next Steps

Once all records are verified, grab your [Mailgun API key and add it to your email service settings](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>).

Then send a test email to confirm everything works — see [how to send a test email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>).

9

## Frequently Asked Questions

Q: Where do I find the DNS Zone Editor in SiteGround?

Log in to SiteGround, then go to Site Tools → Domain → DNS Zone Editor. From there you can add TXT, MX, and CNAME records for your domain.

Q: What if "Add your own MX records" isn't available?

This option appears under the MX tab in the DNS Zone Editor. If you don't see it, confirm you're on the correct domain and that email hosting isn't locked to a different provider in your SiteGround plan.

Q: Should I leave the Name field empty or use @ for the main domain?

Either works in SiteGround's DNS Zone Editor — both represent the root domain. Use whichever the field accepts without an error.

Q: Will this affect my existing Google Workspace or Gmail email?

Not if you use a subdomain for Mailgun rather than your main domain, and leave your existing MX records for Google Workspace untouched on the main domain.

Q: How long does DNS propagation take with SiteGround?

Usually fast, but it can occasionally take a few hours. If a record isn't showing green yet in Mailgun, wait a bit and click Verify DNS Settings again.

Q: What do I do after all 5 records show a green checkmark?

Grab your Mailgun API key, add it to your email service settings, and send a test email in a conversation to confirm delivery is working.

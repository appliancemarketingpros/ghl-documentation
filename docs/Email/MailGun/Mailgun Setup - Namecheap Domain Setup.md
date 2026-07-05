# Mailgun Setup - Namecheap Domain Setup

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981680-mailgun-setup-namecheap-domain-setup](https://help.gohighlevel.com/support/solutions/articles/48000981680-mailgun-setup-namecheap-domain-setup)  
**Category:** Email  
**Folder:** MailGun

---

EMAIL INFRASTRUCTURE

Step-by-Step Mailgun Setup: Namecheap Domain Setup

Sign up for Mailgun, add your domain, and publish the TXT, MX, and CNAME records in Namecheap so your emails verify and deliver.

What You'll Learn

This guide covers creating a Mailgun account, adding a sending domain, choosing between a main domain and a subdomain, and publishing the 5 required DNS records — 2 TXT, 2 MX, and 1 CNAME — inside Namecheap's Advanced DNS settings.

Table of Contents

1

Sign Up for Mailgun

2

Verify Your Email Address

3

Add a New Domain in Mailgun

4

Choose a Main Domain or Subdomain

5

Add Your DNS Records in Namecheap

→ To Add the 1st TXT Record

→ To Add the 2nd TXT Record

→ To Add the 1st MX Record

→ To Add the 2nd MX Record

→ To Add the CNAME Record

6

Get Your API Key & Send a Test Email

7

Video Recap

8

Frequently Asked Questions

9

Related Articles

1

## Sign Up for Mailgun

Create your account at [Mailgun.com](<https://signup.mailgun.com/new/signup>).

2

## Verify Your Email Address

Check your email inbox to verify the email address you signed up with.

![Mailgun signup confirmation screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284378416/original/VewuZVN3oFOFIvBdf4XqMAOX4vtVGv_jNg.png?1677630998)

![Email verification confirmation screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284378421/original/GU6IL6Y3N81qm6KMH9aTz7l5FV5IEv7ySA.png?1677630999)

3

## Add a New Domain in Mailgun

Log in to Mailgun and click **Sending → Add New Domain**.

![Sending menu with Add New Domain option in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284378418/original/kxsnymCeuFAsBWkXaOes6QaaWED2_bfASA.png?1677630999)

4

## Choose a Main Domain or Subdomain

If your domain is **companyname.com** , you can set up either the main domain or a subdomain with Mailgun.

Option A

Main Domain

If you add the main domain, [it should not be used with Google Workspace or any other email provider](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->).

Option B

Subdomain

To set up a subdomain with Mailgun, you can type **anything_here.companyname.com**. Examples:

  * mg.companyname.com
  * replies.companyname.com
  * support.companyname.com


Note

Set up the domain or subdomain under the **US** region, not EU. Then click **Add domain**.

![Add domain form in Mailgun with US region selected](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382652/original/woVjMqNw3YY_Zjs20LoBHUb4KrThVvj_Rw.png?1677635102)

Setup Guide

Now let's publish 5 DNS records in Namecheap

2 TXT records, 2 MX records, and 1 CNAME record — follow each sub-step carefully.

5

## Add Your DNS Records in Namecheap

Log in to [Namecheap.com](<https://www.namecheap.com/myaccount/login/>), then click **Domain List → Manage**.

![Namecheap Domain List with Manage button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284379162/original/ZFfDWZRqEj2vF1mZu2LLamthayVacfWNdQ.png?1677631852)

Click **Advanced DNS** — this is where we'll add all 5 DNS records.

![Namecheap Advanced DNS tab](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284379194/original/lbM_9qwxdQuZYJgoO8k_Bbs6207ECEULCA.png?1677631892)

DNS Record 1 of 5

To Add the 1st TXT Record

Click **Add New Record**.

![Add New Record button in Namecheap Advanced DNS](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284379255/original/z9t88DrLLsk_x-5McqcmUoQay6Rtpl-3JA.png?1677631962)

Select **TXT Record** from the dropdown.

![TXT Record selected in record type dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284379274/original/XZhGADHABEyG3gpE2kfSb4glLSsGZ7X29g.png?1677631986)

![TXT record row in Namecheap DNS table](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284379750/original/afOhZ_mYDjiPnMtdsXB_BaUvpK7-fBAbEg.png?1677632454)

**A. Host:** depending on the subdomain you're setting up:

  * mg.companyname.com → host name is mg
  * replies.companyname.com → host name is replies
  * Main domain (companyname.com) → host name is @


**B. Value:** head back to Mailgun and copy the first TXT record — it will look like v=spf1 include:mailgun.org ~all — and paste it here.

![TXT record value field with SPF record pasted](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284379641/original/OtndbakIxEwGec0uzyy6VhrQ9ahdwqWR4g.png?1677632355)

**C.** Click the green check to save.

DNS Record 2 of 5

To Add the 2nd TXT Record

Click **Add New Record** again, and select **TXT Record** from the dropdown.

![Add New Record button for the second TXT record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380045/original/p3EI2E6cXdPA44wNy1dlbvL9SeMlPsN_pg.png?1677632706)

![TXT Record type selected for the second record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380093/original/ymsCp1tf0vOpw8jh_ELv1eyAHoFR08klKA.png?1677632745)

![Second TXT record row in Namecheap DNS table](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380135/original/h15o-HQi5ZlCUWfi23NsIp_ULoUljPMbDw.png?1677632789)

**A. Host:** this one is a bit tricky — copy everything from the beginning until the subdomain part. **Do not copy the main domain.**

![Mailgun host value highlighted up to the subdomain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284379962/original/S6JIQJ-twEQMWBwUw7Do7908kLEMK8w9gg.png?1677632628)

Examples — copy the highlighted part:

Scenario| Screenshot  
---|---  
Using a subdomain| ![Example host value when using a subdomain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380215/original/t6MGY8Bw9AK1Vv01kUxtJAkNwp_4UfYjHw.png?1677632945)  
Using the main domain| ![Example host value when using the main domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380223/original/JSERXQQhYNvzVp7YoXhIji_yeomZNLXUKA.png?1677632951)  
  
**B. Value:** paste the second, longer TXT record from Mailgun here.

![Second TXT record value pasted into Namecheap](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380189/original/a5LTwyG6FV_Hp-L232_fAj2g1VUUDlSyPw.png?1677632888)

**C.** Click the green check to save.

DNS Record 3 of 5

To Add the 1st MX Record

Scroll down to **Mail Settings** and switch the dropdown to **Custom MX**.

![Mail Settings dropdown switched to Custom MX](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380651/original/s-vIse48Y60uv4ODRMU02N4qsPS5I5uYeg.png?1677633315)

Heads Up

Switching to Custom MX will affect your existing Google Workspace account for incoming mail on the main domain if Gmail was originally selected. Make sure you're using a subdomain for Mailgun. See [Can I Use the Same Domain Name for Mailgun and for Google Apps (Or Another Email Server)?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

You'll need to add back the **5** [MX records for Google Gmail](<https://support.google.com/a/answer/140034?hl=en>):

Host| TTL| Priority| Value  
---|---|---|---  
@| 3600| 1| ASPMX.L.GOOGLE.COM  
@| 3600| 5| ALT1.ASPMX.L.GOOGLE.COM  
@| 3600| 5| ALT2.ASPMX.L.GOOGLE.COM  
@| 3600| 10| ALT3.ASPMX.L.GOOGLE.COM  
@| 3600| 10| ALT4.ASPMX.L.GOOGLE.COM  
  
Once all **five** MX records above are added back, add the Mailgun MX record. Click **Add New Record**.

![Add New Record button for the first MX record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284381008/original/Hvcyh4kYnFgfuL6SKPnyDNBFReckD-0qqg.png?1677633693)

![MX record row being configured in Namecheap](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380997/original/nSuGvsypPVy3uastd0-zS4Dpu71FC2figA.png?1677633659)

**A. Host:** depending on the subdomain you're setting up:

  * mg.companyname.com → host name is mg
  * replies.companyname.com → host name is replies
  * Main domain (companyname.com) → host name is @


**B. Value:** mxa.mailgun.org

**C. Priority:** 10

**D.** Click the green check to save.

![First MX record saved in Namecheap](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284381240/original/2nrnlf9BwTPbv5cKXKZS8QStDqfFbqz-7w.png?1677633916)

DNS Record 4 of 5

To Add the 2nd MX Record

**A. Host:** depending on the subdomain you're setting up:

  * mg.companyname.com → host name is mg
  * replies.companyname.com → host name is replies
  * Main domain (companyname.com) → host name is @


**B. Value:** mxb.mailgun.org

**C. Priority:** 10

**D.** Click the green check to save.

![Second MX record saved in Namecheap](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284381184/original/wao3EJjnKT5qAO1wn_ZxZqBdEusgs_E8Qw.png?1677633856)

DNS Record 5 of 5

To Add the CNAME Record

Scroll back up to the **Host Records** section and click **Add New Record**.

![Add New Record button for the CNAME record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284381639/original/UJxPcf-rUHX7AwbK1pwp4kMH-N9VjEx62w.png?1677634175)

Select **CNAME Record** from the dropdown.

![CNAME Record selected in record type dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284381737/original/kaXoDz-tFmwEhnhJ-NOwZcvVlkk_b8I-bg.png?1677634268)

Head back to Mailgun to copy the host name — copy everything from the beginning until the subdomain part. **Do not copy the main domain.**

![Mailgun CNAME host value to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382024/original/SKui5c_vVTAOKtN714Bl9mx8OdjgxebDSA.png?1677634552)

Go back to Namecheap:

![Namecheap CNAME record row](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284381724/original/zDKUjwzlyWytyho6PuhbQEvKuqGiKzYypQ.png?1677634245)

**A. Host:** depending on the subdomain you're setting up:

  * mg.companyname.com → host name is email.mg
  * replies.companyname.com → host name is email.replies
  * Main domain (companyname.com) → host name is email


**B. Value:** mailgun.org

**C.** Click the green check to save.

Now that all 5 records have been added, go back to Mailgun and click **Verify DNS Settings**. Click the same button again if some records still aren't showing a green checkmark.

![Mailgun Verify DNS Settings results](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382101/original/PQecmA9d0ihGiF3VchOhZL1VKMrOZmUvDQ.png?1677634628)

6

## Get Your API Key & Send a Test Email

Once all the DNS records are added and verified, grab your key from [Mailgun API Key: Where to Find It in Mailgun and Add It to the Platform](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>).

You're Almost Done

Send a test email to confirm everything works. See [How to Send a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>) for the steps.

Video Recap

8

## Frequently Asked Questions

Q: Will switching to Custom MX break my existing Gmail or Google Workspace email?

It can, if you're adding the MX records to your main domain and it's already used with Google Workspace. Re-add all 5 Google MX records alongside the Mailgun ones, and consider using a subdomain instead to avoid the risk entirely.

Q: What's the difference between the "Host" value for the TXT/MX records and the CNAME record?

For TXT and MX records, the host is just your subdomain (e.g. "mg"). For the CNAME record, Namecheap expects "email.mg" — the tracking subdomain Mailgun uses for click and open tracking.

Q: My records aren't showing a green checkmark after verifying — what should I do?

DNS changes can take time to propagate. Double-check each host and value against what Mailgun shows, then click Verify DNS Settings again after a few minutes.

Q: Why do I need two separate TXT records?

The first TXT record is your SPF record, which authorizes Mailgun to send on your behalf. The second, longer TXT record is your DKIM key, which cryptographically signs your outgoing mail.

Q: Do I need to copy the exact values shown in this guide, or the ones from my own Mailgun account?

Always copy the exact host and value strings shown in your own Mailgun dashboard — the mxa.mailgun.org and mxb.mailgun.org values are standard, but your TXT record values are unique to your domain.

Q: Can I use this same process for a domain provider other than Namecheap?

The record types and values are the same everywhere, but the interface for adding them differs by provider. Check the related provider-specific setup guides below.

Related Articles

[Mailgun API Key: Where to Find It in Mailgun and Add It to the Platform](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>) [How to Send a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>)

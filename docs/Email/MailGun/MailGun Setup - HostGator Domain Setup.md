# MailGun Setup - HostGator Domain Setup

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981679-mailgun-setup-hostgator-domain-setup](https://help.gohighlevel.com/support/solutions/articles/48000981679-mailgun-setup-hostgator-domain-setup)  
**Category:** Email  
**Folder:** MailGun

---

Email Infrastructure

Mailgun + HostGator Domain Setup

Step-by-step DNS configuration for connecting Mailgun to a domain hosted with HostGator's cPanel.

What You'll Learn

This guide walks through signing up for Mailgun, adding your domain, and configuring the five DNS records Mailgun requires — two TXT records, two MX records, and one CNAME — inside HostGator's cPanel Zone Editor.

It also covers how to avoid breaking your existing Google Workspace/Gmail mail delivery while adding Mailgun's records.

Table of Contents

1

Sign up for Mailgun & add your domain

2

Access DNS records in cPanel

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

## Access DNS records in cPanel

Now log in to your DNS records and add the 5 DNS records Mailgun requires. This guide uses HostGator's cPanel as the example.

Step 1

Log in to [cPanel](<https://portal.hostgator.com/hosting/cPanel/sso-redirect?redirect=/frontend/paper_lantern/>).

Step 2

Look for the **Domains** section, then click **Zone Editor**.

![cPanel Zone Editor location](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284388376/original/0ObShEaAQ6GXG-G-sSlIwX_9uLXpFUjdCA.png?1677640303)

Step 3

Locate your domain in the Zone Editor section, then click its **Manage** button to view the domain's complete set of DNS records.

![Manage button next to a domain in cPanel Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284388585/original/ZsKY3OvmFHtUBZWXElGKPG31Nl51EuXcFA.png?1677640464)

Step 4

Click the **+Add Record** button and select **Add "TXT" Record**.

![Add TXT Record option in cPanel Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284388748/original/NLKDFwtDUhzgL1MKCSJEt-0sZ8a-ZR0JaA.png?1677640597)

3

## Add the 1st TXT record (SPF)

![TXT record entry form in cPanel Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284389218/original/uUNVP51P30hs2i_U9O701kVRlGP55HpdDw.png?1677641077)

Fields

**A. Name:** different for everyone — **do not include the root domain.**

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain (companyname.com) → host name is **@**


**B. Record:** the same for everyone — paste v=spf1 include:mailgun.org ~all.

![Mailgun screen showing the SPF TXT record to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284389338/original/L_D8amxfS4rLqz8NkwMDjBWCqAuPnFqSiw.png?1677641215)

**C.** Click **Add Record**.

4

## Add the 2nd TXT record (DKIM)

Click the **+Add Record** button and select **Add "TXT" Record** again.

![Add TXT Record option in cPanel Zone Editor for the second record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284388748/original/NLKDFwtDUhzgL1MKCSJEt-0sZ8a-ZR0JaA.png?1677640597)

![TXT record entry form for the DKIM record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284389413/original/bZ319PXDv8_TwakgxeWsjd6r5-6KFjcfAA.png?1677641278)

Fields

**A. Name:** this part is a little tricky. Copy everything from the beginning of the value up until the subdomain part — **do not include the root domain.** Everyone's 2nd TXT record name and record value are different.

Example| Host name to copy| Highlighted part  
---|---|---  
Using a subdomain| mx._domainkey.helpdesk| ![Example of the host value to copy when using a subdomain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380215/original/t6MGY8Bw9AK1Vv01kUxtJAkNwp_4UfYjHw.png?1677632945)  
Using the main domain| mailo._domainkey| ![Example of the host value to copy when using the main domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380223/original/JSERXQQhYNvzVp7YoXhIji_yeomZNLXUKA.png?1677632951)  
  
**B. Record:** different for everyone. Head back to Mailgun and copy the 2nd, much longer TXT record — highlighted in the screenshot below — and paste it here.

![Mailgun screen highlighting the long DKIM TXT record to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385043/original/UvAhE3LGN5sYkTb4kyEsXNM0GE0Uc8Eq1Q.png?1677637220)

**C.** Click **Add Record**.

5

## Add the 1st MX record

![MX records section in cPanel Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385538/original/qHcrrZPnp3g0LC4c75qM1hg_opwYUXgE0w.png?1677637720)

Click the **+Add Record** button and select **Add "MX" Record**.

![Add MX Record form in cPanel Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284389907/original/18xrjivpU7RYPDJqHY2wnce79K3AkwJe0A.png?1677641569)

Heads Up

If you have a Google Workspace account capturing incoming email for your main domain, make sure you're using a subdomain for Mailgun instead. See [Can I Use the Same Domain Name for Mailgun and for Google Apps (Or Another Email Server)?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

![MX record fields highlighted in cPanel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284390505/original/nO1ZhMzBXp4ZqlhfzX1QYLxgGT0_ET-_vg.png?1677642035)

Fields

**A. Name:** different for everyone —

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**B. Priority:** 10 — the same for everyone, no matter what domain you're setting up.

**C. Destination:** the same for everyone — paste mxa.mailgun.org.

Click **Save Record**.

6

## Add the 2nd MX record

Click the **+Add Record** button and select **Add "MX" Record** again. This time we'll add a second record pointing to mxb.mailgun.org.

![Add second MX Record form in cPanel Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284389907/original/18xrjivpU7RYPDJqHY2wnce79K3AkwJe0A.png?1677641569)

![Second MX record fields highlighted in cPanel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284390505/original/nO1ZhMzBXp4ZqlhfzX1QYLxgGT0_ET-_vg.png?1677642035)

Fields

**A. Name:** different for everyone —

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**B. Priority:** 10 — the same for everyone.

**C. Destination:** the same for everyone — paste mxb.mailgun.org.

Click **Save Record**.

7

## Add the CNAME record

![CNAME section in cPanel Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385721/original/3LyKoigujZ-vEjMFQDflCfmRRfAJra3rYA.png?1677637907)

Click the **+Add Record** button and select **Add "CNAME" Record**.

![Add CNAME Record option in cPanel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284390884/original/13yHoywGcgf3oSslLKzD03Sj9MAxoJQGfA.png?1677642360)

![CNAME record entry form in cPanel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284391213/original/QLb8ArxkgSrQsXJzo63PddCcQRhylQBGHw.png?1677642643)

Fields

**A. Name:** different for everyone. Head back to Mailgun to copy the host name — copy everything from the beginning up until the subdomain part, **do not copy the main domain**.

  * mg.companyname.com → host name is **email.mg**
  * replies.companyname.com → host name is **email.replies**
  * Main domain (companyname.com) → host name is **email**


![Mailgun CNAME host name to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385985/original/OtLw_A4zY8FbLbBKqMB9kUKRaQJO3xpp8A.png?1677638165)

**B. Record:** the same for everyone — paste mailgun.org.

**C.** Click **Save Record**.

8

## Verify DNS & finish setup

Now that you've added all 5 records, go back to Mailgun and click **Verify DNS Settings**. If some records still aren't showing a green checkmark, click the same button again — DNS propagation can take a little time.

![Verify DNS Settings button in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284387965/original/I7T5QQCSjAnBvT1zqQlVgXSuNdgfuNiM3w.png?1677639928)

Next Steps

Once all records are verified, grab your [Mailgun API key and add it to your email service settings](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>).

Then send a test email to confirm everything works — see [how to send a test email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>).

9

## Frequently Asked Questions

Q: Where do I find the Zone Editor in cPanel?

Log in to cPanel, look for the Domains section, and click Zone Editor. From there, find your domain and click Manage to view and add DNS records.

Q: Should I use my main domain or a subdomain with Mailgun?

If you already use your main domain with Google Workspace or another email provider, use a subdomain (like mg.companyname.com) for Mailgun instead to avoid mail routing conflicts.

Q: What does "do not include the root domain" mean for the Name field?

In cPanel's Zone Editor, the Name field only needs the subdomain portion — the root domain is added automatically. So for mg.companyname.com, you'd enter just "mg", not the full domain.

Q: Will this break my existing Gmail or Google Workspace email?

Not if you use a subdomain for Mailgun rather than your main domain, and leave your existing MX records for Google Workspace untouched on the main domain.

Q: How long does it take for DNS records to verify?

DNS propagation is usually fast, but it can occasionally take a few hours. If a record isn't showing green yet, wait a bit and click Verify DNS Settings again.

Q: What do I do after all 5 records show a green checkmark?

Grab your Mailgun API key, add it to your email service settings, and send a test email in a conversation to confirm delivery is working.

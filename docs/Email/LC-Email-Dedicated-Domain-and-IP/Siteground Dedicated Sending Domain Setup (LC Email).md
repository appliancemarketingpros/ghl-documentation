# Siteground Dedicated Sending Domain Setup (LC Email)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000000568-siteground-dedicated-sending-domain-setup-lc-email-](https://help.gohighlevel.com/support/solutions/articles/155000000568-siteground-dedicated-sending-domain-setup-lc-email-)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Deliverability

LC Email Dedicated Domain Setup — Siteground

A step-by-step guide to adding the 5 required DNS records in Siteground to authenticate your dedicated sending domain.

What You'll Learn

This guide walks you through configuring a dedicated sending domain for LeadConnector Email inside Siteground's DNS Zone Editor. You'll add two TXT records, two MX records, and one CNAME record — five records in total.

Before you start, decide whether you'll use your **main domain** (e.g. companyname.com) or a **subdomain** (e.g. replies.companyname.com). If your main domain is already used with Google Workspace or another mail provider, you must use a subdomain.

Table of Contents

1

Initial Setup — Add & Verify Your Domain

2

1st TXT Record (SPF)

3

2nd TXT Record (DKIM)

4

1st MX Record (mxa.mailgun.org)

5

2nd MX Record (mxb.mailgun.org)

6

CNAME Record

7

Frequently Asked Questions

Setup Guide

5 DNS Records — Complete All Steps in Order

Log in to Siteground and keep the DNS Zone Editor open alongside the platform's DNS records screen throughout this guide.

1

## Initial Setup — Add & Verify Your Domain

Step 1

Navigate to Dedicated Domain Settings

In your sub-account, go to **Settings → Email Services → Dedicated Domain → + Add Domain**.

![Navigating to Settings > Email Services > Dedicated Domain > Add Domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292765242/original/jQLugI8wtvQRfs38XJDujiQd2QnIgjQqSA.gif?1681496688)

Navigate to Settings → Email Services → Dedicated Domain → + Add Domain

Step 2

Choose Main Domain or Subdomain

If your domain is **companyname.com** , you can set up either the main domain or a subdomain.

**Main domain** — if you add the main domain, it must not be used with Google Workspace or any other email provider at the same time.

**Subdomain** — type anything before your root domain, e.g. **replies**.companyname.com or **support**.companyname.com. This is the recommended option if you already use your root domain for email.

Heads Up

If you use Google Workspace (Gmail) for your main domain's incoming email, you **must** use a subdomain here — otherwise your Google Workspace MX records will conflict with the Mailgun MX records you're about to add.

Step 3

Click Add & Verify

Enter your domain or subdomain name and click **Add & Verify**.

![Add & Verify button in the platform](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030769485/original/Q46amTmsqcDKAnWZRyL8QCC1l7hdpWCLCg.jpg?1723215212)

The next screen will display the 5 DNS records you need to add. **Keep this screen open** — you'll reference it throughout the following steps.

![DNS records screen showing the 5 records to add](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030769518/original/u0y6nwg71SG7K_cEFAXEO8VhBAzeldaGQA.jpg?1723215260)

Leave this DNS records screen open — you'll copy values from it in the steps below.

2

## 1st TXT Record (SPF)

Log in to [Siteground](<https://login.siteground.com/login?lang=en>) and go to **Site Tools → Domain → DNS Zone Editor**.

![Siteground Site Tools > Domain > DNS Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030769548/original/VsNojWfnrB6J31RPe6Kf-eYmW7DBngqqlQ.jpg?1723215298)

In the **Create New Record** section:

![Create New Record section in Siteground DNS Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030780106/original/bHbrF0bUz804hradJsT9OgCLJPXR8Qxiag.jpg?1723224477)

A

Click the TXT tab

B — Name

Different for everyone — do NOT include the root domain

Enter only the subdomain portion of your domain:

  * Setting up **lc**.companyname.com → Name: **lc**
  * Setting up **replies**.companyname.com → Name: **replies**
  * Setting up the **main domain** (companyname.com) → Name: **@ or leave empty**


![Name field for 1st TXT record in Siteground](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030780154/original/LirZym0_7wm9fj29hWQHDt2TXRZOmWAQUQ.jpg?1723224534)

C — Value

Same for everyone

Paste the following value exactly as shown:

v=spf1 include:mailgun.org ~all

![Value field for 1st TXT record — SPF value](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030780181/original/_hL8idOQ87Q9OiHkGuFyrBAmALbUCfdtAg.jpg?1723224576)

D

Click Create

3

## 2nd TXT Record (DKIM)

Click **\+ Add Record** again to open a new Create New Record form.

![Clicking + Add Record to add a second DNS record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030780286/original/-_m54mJDcyCoz2qwiphfIQjUELRRPGy2TQ.jpg?1723224707)

A

Click the TXT tab

B — Name

Different for everyone — do NOT include the root domain

Head back to the platform's DNS records screen and copy the hostname for the 2nd TXT record. Copy everything up to (but not including) your root domain. The key is to exclude **companyname.com** from whatever you paste.

![2nd TXT record hostname field in Siteground](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030780352/original/y-S6ROHWlFNZIPWbWP35TLikz7DU-x5SBg.jpg?1723224751)

Note

Everyone's 2nd TXT record hostname and value is unique to their account. Copy the exact values shown on your DNS records screen.

Examples — **copy only the highlighted portion** :

Scenario| Hostname to enter in Siteground| Example screenshot  
---|---|---  
Subdomain (e.g. helpdesk.companyname.com)| mx._domainkey.helpdesk| ![Subdomain DKIM example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768867/original/Oy2wnQ4XgDD5YzExKorYuiEBhl-wH7krkg.png?1681498513)  
Main domain (companyname.com)| mailo._domainkey| ![Main domain DKIM example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768954/original/rXlYB3cbDo6Ix-Oq_XBgdnsiwBHDHuTUig.png?1681498537)  
  
C — Value

Unique — copy from the platform's DNS records screen

Go back to the platform and copy the value shown for the 2nd TXT record (highlighted below). Paste it into the Value field in Siteground.

![2nd TXT record value highlighted on the platform DNS screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030780383/original/HdqP4IVZly9D-b8XMoSreStXhxpKOBhmvg.jpg?1723224827)

D

Click Create

4

## 1st MX Record (mxa.mailgun.org)

Click **\+ Add Record** to open a new form. This time, click the **MX** tab and select **Add your own MX records**.

![Clicking MX tab and selecting Add your own MX records](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030780422/original/rNjjKaWuMefXrQn3wNTgUYDpvKK7OsQibA.jpg?1723224862)

![MX record form with Add your own MX records selected](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030781114/original/Wr1IYksYWNCM4dmafAALzCOKd5u-UHIIRg.jpg?1723225787)

A — Name

Different for everyone

Use the same logic as the TXT records above:

  * **lc**.companyname.com → Name: **lc**
  * **replies**.companyname.com → Name: **replies**
  * Main domain (companyname.com) → Name: **@**


![Name field for 1st MX record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030782341/original/EoVTlF-5tjzN0euBbaIAnTPzyOadJO6xnw.jpg?1723228044)

B — Priority

Same for everyone: 10

![Priority field set to 10](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030782362/original/S3zPWDAvVfLvcHd18dzny8F2chlD-k-McA.jpg?1723228108)

C — Destination

Same for everyone

Paste the following destination:

mxa.mailgun.org

![Destination field set to mxa.mailgun.org](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030782390/original/dCrujp8-torR3KCkqHj9RCUxV9T4IpP4fw.jpg?1723228150)

D

Click Create

5

## 2nd MX Record (mxb.mailgun.org)

Click **\+ Add Record** again. The 2nd MX record is identical to the 1st except the destination changes to **mxb**.

![2nd MX record form](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030782407/original/STd7r76SSYxjjEueEZ71PlcaGBOkTHo5Jw.jpg?1723228189)

A — Name

Different for everyone — same logic as the 1st MX record

  * **lc**.companyname.com → Name: **lc**
  * **replies**.companyname.com → Name: **replies**
  * Main domain → Name: **@**


![Name field for 2nd MX record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030782413/original/HGLSaAWGMgGCvPBFzdZi2p5c6a2196-KMQ.jpg?1723228228)

B — Priority

Same for everyone: 10

![Priority set to 10 for 2nd MX record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030783105/original/TBBrnlPpoLpeqs517AvUL65F5TN5oV6qbQ.jpg?1723229730)

C — Destination

Same for everyone

mxb.mailgun.org

![Destination field set to mxb.mailgun.org](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030783114/original/gmZ3PYwnHX5SoqOoa1c3TPV-FvlUOwQM6A.jpg?1723229761)

D

Click Create

6

## CNAME Record

Click **\+ Add Record** one final time.

![CNAME record form in Siteground DNS Zone Editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030783142/original/PpLAFvnX8fpVSkGYfge-jqVsPe-05bhTMA.jpg?1723229788)

A

Click the CNAME tab

B — Name

Different for everyone — do NOT copy the root domain

Go back to the platform and copy the CNAME hostname. Exclude the root domain portion.

  * lc.companyname.com → Name: **email.lc**
  * replies.companyname.com → Name: **email.replies**
  * Main domain (companyname.com) → Name: **email**


![CNAME Name field in Siteground](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030783146/original/NzlqSBBFNxO15QArOp7-b2YQT2e5HoEqmg.jpg?1723229819)

C — Resolves To

Same for everyone

mailgun.org

![CNAME Resolves To field set to mailgun.org](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030783164/original/pajiIQ0wDsE7fPob2fz6xdduz_LfP-iKMg.jpg?1723229856)

D

Click Create

![All 5 DNS records added in Siteground](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030783184/original/F1CbuTsrXYX_Jc1kpb5rRqS82VtyueNFiQ.jpg?1723229890)

All 5 records have been added — now head back to the platform to verify.

Now that all 5 DNS records are in place, go back to the platform and click **Verify DNS Settings**.

![Verify DNS Settings button in the platform](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030783203/original/X-TDph4fv6CxTwGhAoTVFfFqut48mxYVKQ.jpg?1723229933)

Heads Up

If some records still show a red ✗ after verifying, click **Verify Domain** again. DNS changes can take up to 24–48 hours to propagate fully, though they often appear within minutes on Siteground.

Next Steps

Once all records show a green checkmark, verify your [SSL Certificate for Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) is set up correctly.

Then [send a test email from the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>) to confirm everything is working end-to-end.

7

## Frequently Asked Questions

Q: Do I need a dedicated sending domain, or can I use the shared domain?

You can use the shared LeadConnector domain to send emails without any DNS setup. However, a dedicated sending domain improves deliverability and brand trust because emails appear to come from your own domain rather than a shared one. It also gives you full control over your sending reputation.

Q: Can I use my main domain (e.g. companyname.com) if I also use Google Workspace for company email?

No — you cannot use the same domain for both Google Workspace (or any other mail provider) and the Mailgun MX records required for LC Email. If your main domain already has Google Workspace MX records, use a subdomain (e.g. **replies.companyname.com**) instead.

Q: How long does DNS propagation take after adding the records in Siteground?

Siteground DNS changes often propagate within a few minutes for records managed within their system. However, full global propagation can take up to 24–48 hours in some cases. If verification fails immediately after adding the records, wait 15–30 minutes and click **Verify Domain** again.

Q: Why do I need two MX records (mxa and mxb)?

The two MX records (**mxa.mailgun.org** and **mxb.mailgun.org**) provide redundancy for Mailgun's inbound email routing. If one server is unavailable, email is automatically routed through the other. Both records use the same priority of 10.

Q: Some of my DNS records show a red ✗ even after waiting. What should I do?

Double-check that you did not include the root domain in any of the Name/Hostname fields. For example, if your domain is **replies.companyname.com** , the name for the TXT and MX records should be **replies** only — not **replies.companyname.com**. Also confirm that the 2nd TXT value was copied exactly from the platform without any extra spaces.

Q: Can I use any subdomain name, or does it have to be something specific?

You can use any subdomain prefix you like — common choices are **replies** , **mail** , **lc** , **send** , or **support**. The subdomain name itself does not affect deliverability. Pick something that makes sense for your workflow.

Q: Will my contacts notice any difference after switching to a dedicated sending domain?

Contacts will see emails appearing to come from your own domain (e.g. noreply@replies.companyname.com) instead of a shared LeadConnector domain. This can improve open rates and trust. The sending experience from your side within the platform does not change.

Q: Do I need to repeat this process for each sub-account?

Yes — dedicated sending domains are configured per sub-account. If multiple sub-accounts need dedicated domains, you can use different subdomains for each (e.g. **team1.companyname.com** and **team2.companyname.com**), or the same subdomain on separate sub-accounts if needed.

Related Articles

[How to Migrate My Agency Over to LC - Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>) [How to Set Up a Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/support/solutions/articles/48001226115-how-to-set-up-a-dedicated-sending-domain-lc-email->) [SSL Certificate for Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) [How to Send a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>) [Siteground Domain Setup for Mailgun](<https://help.gohighlevel.com/a/solutions/articles/48000981685>)

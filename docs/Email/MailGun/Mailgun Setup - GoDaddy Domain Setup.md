# Mailgun Setup - GoDaddy Domain Setup

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981678-mailgun-setup-godaddy-domain-setup](https://help.gohighlevel.com/support/solutions/articles/48000981678-mailgun-setup-godaddy-domain-setup)  
**Category:** Email  
**Folder:** MailGun

---

Email Infrastructure

Mailgun + GoDaddy Domain Setup

Step-by-step DNS configuration for connecting Mailgun to a domain registered with GoDaddy.

What You'll Learn

This guide walks through signing up for Mailgun, adding your domain, and configuring the five DNS records Mailgun requires — two TXT records, two MX records, and one CNAME — inside GoDaddy's DNS editor.

It also covers how to avoid breaking your existing Google Workspace/Gmail mail delivery while adding Mailgun's records.

Table of Contents

1

Sign up for Mailgun & add your domain

2

Access DNS records in GoDaddy

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

![Mailgun DNS records screen to keep open for the next step](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033639864/original/enFXAfFTmzAed4_oLbMST-Xu1YBUby2MpQ.png?1727378325)

2

## Access DNS records in GoDaddy

Now log in to your DNS records and add the 5 DNS records Mailgun requires.

Step 1

Sign in to your [GoDaddy Domain Portfolio](<https://dcc.godaddy.com/control/portfolio>).

Step 2

Click the three dots for the Domain Edit Options next to your domain, then select **Edit DNS**. You may need to scroll down to see the Edit DNS option. See GoDaddy's own guide on [adding a TXT record](<https://ca.godaddy.com/help/add-a-txt-record-19232>) if you'd like more detail.

![Edit DNS option in GoDaddy Domain Portfolio](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284383735/original/cgJYei63pjBqxqUREcrgnMBHMYjimo-FBA.png?1677636137)

Step 3

Click **Add** to add a new record. You'll repeat this for each of the 5 records below.

![Add button for creating a new DNS record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284383808/original/H6np93jJkfJVHPLdTaLTLmRgo2mB_c6JRA.png?1677636223)

3

## Add the 1st TXT record (SPF)

![Add record form in GoDaddy DNS editor](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284384102/original/N9CKo-PVMexPIY_hCkU3qz4FgWu5LCmiKw.png?1677636518)

Fields

**A. Type:** select **TXT** from the Type menu.

**B. Host:** different for everyone — **do not include the root domain.**

![Example of the Host field in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292759996/original/0Cj6mdSJlEYwYG4Qt4KqNjenCcUdx500Tw.png?1681494292)

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain (companyname.com) → host name is **@**


**C. TXT Value:** the same for everyone — paste v=spf1 include:mailgun.org ~all.

![TXT Value field with the SPF record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292760093/original/5Gl9rXwkPu648V7b7A73EVcYsiwQjSX3fQ.png?1681494342)

**D.** Click **Save**.

![Completed first TXT record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292760158/original/whQOMoD2hGeHEbJgNmnIm1fdwCQhF1Mz9g.png?1681494360)

4

## Add the 2nd TXT record (DKIM)

Click **Add** to add another new record.

![Add record form for the second TXT record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284384815/original/FlVncn3L0vrYLOa9P1vI4X9Pt16_Q-FUOg.png?1677637017)

Fields

**A. Type:** select **TXT** from the Type menu.

**B. Host:** this part is a little tricky. Copy everything from the beginning of the value up until the subdomain part — **do not include the root domain.** Everyone's 2nd TXT record host name and value are different.

![Example of the Host field for the DKIM record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292760457/original/uKwd7XSYgsN0abFfq-uLghjMc4gYBKFShw.png?1681494446)

Example| Host name to copy| Highlighted part  
---|---|---  
Using a subdomain| mx._domainkey.helpdesk| ![Example of the host value to copy when using a subdomain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380215/original/t6MGY8Bw9AK1Vv01kUxtJAkNwp_4UfYjHw.png?1677632945)  
Using the main domain| mailo._domainkey| ![Example of the host value to copy when using the main domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284380223/original/JSERXQQhYNvzVp7YoXhIji_yeomZNLXUKA.png?1677632951)  
  
**C. TXT Value:** head back to Mailgun and copy the 2nd, much longer TXT record — highlighted in the screenshot below — and paste it here.

![Mailgun screen highlighting the long DKIM TXT record to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385043/original/UvAhE3LGN5sYkTb4kyEsXNM0GE0Uc8Eq1Q.png?1677637220)

**D.** Click **Save**.

![Completed second TXT record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292760542/original/dHr8OmpttMWN0VMOkXNfAi5G8Ou_hQUiVQ.png?1681494507)

5

## Add the 1st MX record

![MX records overview in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385538/original/qHcrrZPnp3g0LC4c75qM1hg_opwYUXgE0w.png?1677637720)

Click **Add** to add a new record.

![Add MX record form in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385352/original/nEr12soR47bfSHjwNBS075J4Dr_Fd3jqUQ.png?1677637478)

Heads Up

If you have a Google Workspace account capturing incoming email for your main domain, make sure you're using a subdomain for Mailgun instead. See [Can I Use the Same Domain Name for Mailgun and for Google Apps (Or Another Email Server)?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

Fields

**A. Type:** select **MX** from the Type menu.

**B. Host:** different for everyone —

![Example of the Host field for the MX record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292761281/original/ilff0N0hrTpB9rOZOLtKWFcpd_pFm1FAAg.png?1681494876)

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**C. Points to:** the same for everyone — paste mxa.mailgun.org.

**D. Priority:** 10 — the same for everyone, no matter what domain you're setting up.

**E.** Click **Save**.

![Completed first MX record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292761314/original/r1sCz03HEK4u2NnzjZxK6TRXfTixx9qJpg.png?1681494889)

6

## Add the 2nd MX record

Click **Add** to add another new record.

![Add second MX record form in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385634/original/wYOidp2P0QPZbDYtP60qHBim2dahkciEMw.png?1677637830)

Fields

**A. Type:** select **MX** from the Type menu.

**B. Host:** different for everyone —

![Example of the Host field for the second MX record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292761375/original/qVuzSSON9aWqKQCpGlKX89woV1txgzea3g.png?1681494908)

  * mg.companyname.com → host name is **mg**
  * replies.companyname.com → host name is **replies**
  * Main domain → host name is **@**


**C. Points to:** the same for everyone — paste mxb.mailgun.org.

**D. Priority:** 10 — the same for everyone.

**E.** Click **Save**.

7

## Add the CNAME record

![CNAME records overview in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385721/original/3LyKoigujZ-vEjMFQDflCfmRRfAJra3rYA.png?1677637907)

Click **Add** to add a new record.

![Add CNAME record form in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385821/original/Z_H7aEV9Fj-ulIPJTmhnmpgRUG-CWVntNA.png?1677638013)

Fields

**A. Type:** select **CNAME** from the Type menu.

**B. Host:** different for everyone. Head back to Mailgun to copy the host name — copy everything from the beginning up until the subdomain part, **do not copy the main domain**.

![Mailgun CNAME host name to copy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292761488/original/yTenM0KsBABRkiuopqOQIzy7E_TjKkeVDw.png?1681494956)

  * mg.companyname.com → host name is **email.mg**
  * replies.companyname.com → host name is **email.replies**
  * Main domain (companyname.com) → host name is **email**


**C. Points to:** the same for everyone — paste mailgun.org.

**D.** Click **Save**.

![Completed CNAME record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292761511/original/Q-pg6CdROQ4wXlfIoOIOkvDgY1yJdVN1Ug.png?1681494965)

8

## Verify DNS & finish setup

![All 5 DNS records added in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284386112/original/kW6t3s2sXMcjCylHMSgGSwJy8HDwA4momQ.png?1677638281)

Now that you've added all 5 records, go back to Mailgun and click **Verify DNS Settings**. If some records still aren't showing a green checkmark, click the same button again — DNS propagation can take a little time.

![Verify DNS Settings button in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284382101/original/PQecmA9d0ihGiF3VchOhZL1VKMrOZmUvDQ.png?1677634628)

Next Steps

Once all records are verified, grab your [Mailgun API key and add it to your email service settings](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>).

Then send a test email to confirm everything works — see [how to send a test email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>).

9

## Frequently Asked Questions

Q: What should I do if I run into errors during setup?

Double-check your API key and domain settings in Mailgun, confirm the DNS records are entered correctly in GoDaddy, and verify your domain is showing as verified in Mailgun's dashboard. Mailgun's support resources can help decode specific error messages.

Q: Can I use a subdomain with Mailgun, and how do I set it up?

Yes. Choose a subdomain when adding your domain in Mailgun (like mg.companyname.com), then follow the same 5 DNS records in this guide using that subdomain's host names.

Q: How do I monitor email deliverability after setup?

Use the Mailgun dashboard to track opens, clicks, bounces, and spam complaints. Reviewing these regularly helps you catch deliverability issues early.

Q: I don't see an "Edit DNS" option in my GoDaddy account — what should I check?

Make sure you're viewing the domain from the Domain Portfolio and clicking the three-dot menu next to the correct domain. If your DNS is managed elsewhere (like a separate hosting provider), you'll need to edit records there instead.

Q: Do the record values change depending on whether I use a subdomain or the main domain?

The Host field changes (mg, replies, or @ for the main domain), but the record values themselves — the SPF value, MX destinations, and CNAME target — stay the same either way.

Q: Is adding records in GoDaddy different from other registrars?

The same 5 records (2 TXT, 2 MX, 1 CNAME) are required no matter your registrar. Only the interface for adding them — like GoDaddy's Type/Host/Value/Priority fields — looks different.

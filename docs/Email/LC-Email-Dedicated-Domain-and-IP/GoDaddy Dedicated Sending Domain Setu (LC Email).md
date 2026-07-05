# GoDaddy Dedicated Sending Domain Setu (LC Email)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001237513-godaddy-dedicated-sending-domain-setu-lc-email-](https://help.gohighlevel.com/support/solutions/articles/48001237513-godaddy-dedicated-sending-domain-setu-lc-email-)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Infrastructure

LC Email Dedicated Domain Setup — GoDaddy

A step-by-step guide to adding and verifying your dedicated sending domain using GoDaddy DNS.

What You'll Learn

This article walks you through connecting a dedicated sending domain to LC Email using GoDaddy as your DNS provider. You will add 5 DNS records in total: 2 TXT records, 2 MX records, and 1 CNAME record.

Unlike some DNS providers, GoDaddy requires you to save each record individually. Follow the steps in order and click **Save** after each record before adding the next.

Table of Contents

1

Add Your Domain in Email Services

2

Access GoDaddy DNS

3

Add the 1st TXT Record (SPF)

4

Add the 2nd TXT Record (DKIM)

5

Add the 1st MX Record (mxa.mailgun.org)

6

Add the 2nd MX Record (mxb.mailgun.org)

7

Add the CNAME Record

8

Verify Your Domain

9

Frequently Asked Questions

1

## Add Your Domain in Email Services

Step 1

Navigate to Dedicated Domain settings

In your sub-account, go to **Settings → Email Services → Dedicated Domain** and click **\+ Add Domain**.

![Navigating to Settings > Email Services > Dedicated Domain > + Add Domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292765242/original/jQLugI8wtvQRfs38XJDujiQd2QnIgjQqSA.gif)

Navigating to Settings → Email Services → Dedicated Domain → + Add Domain

Step 2

Choose your domain type

If your domain is **companyname.com** , you can register either the root domain or a subdomain as your dedicated sending domain.

**Main domain** (companyname.com) — must not already be in use with Google Workspace or another email provider.

**Subdomain** — enter any prefix before your root domain, for example **replies.companyname.com** or **support.companyname.com**.

Note

If you use Google Workspace or another email provider on your root domain, adding the root domain here will conflict with your existing MX records. Use a subdomain instead. See [Can I use the same domain for Mailgun and Google Apps?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

Step 3

Click Add & Verify

After entering your domain name, click **Add & Verify**. The next screen will display the 5 DNS records you need to add. Keep this tab open — you will copy values from it in the steps below.

![Add & Verify button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292766472/original/5TxDqQG542C3YtKLt6stGIAfwcbDmmcesg.png)

![DNS records screen showing 5 records to add](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48293298198/original/xGMUZ9x0JoahqbofrVsYVWEjEF9LDDvsMQ.png)

Keep this DNS records screen open — you will copy values from it in the steps below.

Tip

Migrating from Mailgun? See [How to move a sending domain from Mailgun to LeadConnector](<https://help.gohighlevel.com/support/solutions/articles/48001226115-how-to-set-up-a-dedicated-sending-domain-lc-email-#How-to-move-sending-domain-from-Mailgun-to-LeadConnector?>).

2

## Access GoDaddy DNS

In a new browser tab, sign in to your [GoDaddy Domain Portfolio](<https://dcc.godaddy.com/control/portfolio>). Then follow these steps to open the DNS editor for your domain.

Step 1

Click the **three-dot menu** next to your domain to open the Edit Options.

Step 2

Select **Edit DNS**. You may need to scroll down to see this option.

![GoDaddy domain portfolio — click three dots then Edit DNS](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284383735/original/cgJYei63pjBqxqUREcrgnMBHMYjimo-FBA.png)

GoDaddy Save Behavior

GoDaddy requires you to click **Save** after each individual DNS record. You cannot batch all records and save once — complete each section below in full before moving to the next.

DNS Setup Guide

Adding Your 5 DNS Records

Sections 3–7 cover each record. Click Add, fill in the fields, then click Save before starting the next record.

3

## Add the 1st TXT Record (SPF)

In the GoDaddy DNS editor, click **Add** to create a new record.

![GoDaddy Add button for new DNS record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284383808/original/H6np93jJkfJVHPLdTaLTLmRgo2mB_c6JRA.png)

![New DNS record form in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284384102/original/N9CKo-PVMexPIY_hCkU3qz4FgWu5LCmiKw.png)

A. Type

Select **TXT** from the Type menu.

B. Host — do not include the root domain

Enter only the subdomain prefix. GoDaddy appends the root domain automatically:

  * Setting up **lc**.companyname.com → enter **lc**
  * Setting up **replies**.companyname.com → enter **replies**
  * Setting up root domain companyname.com → enter **@**


![GoDaddy Host field — enter subdomain prefix only](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292767095/original/U0Uh3wPJ901NXe3E0tAj8DzwIys4kzuXFA.png)

C. TXT Value — same for everyone

Paste the following SPF record value exactly as shown:

v=spf1 include:mailgun.org ~all

![SPF TXT record filled in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292767368/original/n_1Mu3Av0f2EYEvZG9iBeM-knKybDa2RPg.png)

D. Save

Click **Save** to confirm this record.

![Saving the 1st TXT record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292760158/original/whQOMoD2hGeHEbJgNmnIm1fdwCQhF1Mz9g.png)

4

## Add the 2nd TXT Record (DKIM)

Important

Everyone's 2nd TXT record hostname and value is **unique to their domain**. Copy both values directly from your platform's DNS records screen — do not use values from screenshots in this article.

Click **Add** in the GoDaddy DNS editor to create a new record.

![GoDaddy Add button for new DNS record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284383808/original/H6np93jJkfJVHPLdTaLTLmRgo2mB_c6JRA.png)

![New TXT record form for DKIM](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284384815/original/FlVncn3L0vrYLOa9P1vI4X9Pt16_Q-FUOg.png)

A. Type

Select **TXT** from the Type menu.

B. Host — copy everything before the root domain

Look at the 2nd TXT hostname in your DNS records screen. Copy only the portion **before** your root domain — do not include the root domain itself.

![DKIM hostname — copy highlighted portion only](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768165/original/xN_6s9kcDwkztqKLFUlRtJJJlE7M_GD54w.png)

Scenario| Copy this as hostname| Example  
---|---|---  
Using a subdomain| mx._domainkey.helpdesk| ![Subdomain DKIM hostname example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768867/original/Oy2wnQ4XgDD5YzExKorYuiEBhl-wH7krkg.png)  
Using the root domain| mailo._domainkey| ![Root domain DKIM hostname example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768954/original/rXlYB3cbDo6Ix-Oq_XBgdnsiwBHDHuTUig.png)  
  
C. TXT Value

Paste the full 2nd TXT record value from your platform's DNS records screen (the long highlighted value). This is unique to your domain.

![2nd TXT value — copy the highlighted long value](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768735/original/cUIeRsQGsIF81ZCW8a-cj-v7iGlndoLiKw.png)

D. Save

Click **Save** to confirm this record.

![Saving the 2nd TXT record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292760542/original/dHr8OmpttMWN0VMOkXNfAi5G8Ou_hQUiVQ.png)

5

## Add the 1st MX Record (mxa.mailgun.org)

Google Workspace Users

If you use Google Workspace to send and receive mail on your root domain, adding MX records to the root domain will break your existing email. Use a subdomain for LC Email instead. See [Can I use the same domain for Mailgun and Google Apps?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

Click **Add** in the GoDaddy DNS editor to create a new record.

![GoDaddy Add button for new DNS record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284383808/original/H6np93jJkfJVHPLdTaLTLmRgo2mB_c6JRA.png)

![MX record form in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385352/original/nEr12soR47bfSHjwNBS075J4Dr_Fd3jqUQ.png)

A. Type

Select **MX** from the Type menu.

B. Host

Same logic as the TXT records — enter only the subdomain prefix:

  * **lc**.companyname.com → enter **lc**
  * **replies**.companyname.com → enter **replies**
  * Root domain companyname.com → enter **@**


![MX record host field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292769400/original/UKCDaverUyyLQpklJb1Jxf15cmXUamb0VQ.png)

C. Points To — same for everyone

Paste the following value:

mxa.mailgun.org

![MX Points To field — mxa.mailgun.org](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292769476/original/xvdURibcJ1cBG-y1bc5ngzqpnSNCdRALmA.png)

D. Priority — same for everyone

Set Priority to **10**. This value is the same regardless of which domain you are setting up.

![MX Priority field set to 10](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292769807/original/1wmkWSsWNVmgj5fdec3hG0a9KbuWBxPhnA.png)

E. Save

Click **Save** to confirm this record.

![Saving the 1st MX record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292761314/original/r1sCz03HEK4u2NnzjZxK6TRXfTixx9qJpg.png)

6

## Add the 2nd MX Record (mxb.mailgun.org)

Click **Add** in the GoDaddy DNS editor to create a new record.

![GoDaddy Add button for new DNS record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284383808/original/H6np93jJkfJVHPLdTaLTLmRgo2mB_c6JRA.png)

![2nd MX record form in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385634/original/wYOidp2P0QPZbDYtP60qHBim2dahkciEMw.png)

A. Type

Select **MX** from the Type menu.

B. Host

Same as the 1st MX record — enter only the subdomain prefix:

  * **lc**.companyname.com → enter **lc**
  * **replies**.companyname.com → enter **replies**
  * Root domain companyname.com → enter **@**


![2nd MX record host field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292770778/original/1YS3yCM8yCVGkdwvDlET1DiZvGimSLDnCA.png)

C. Points To — same for everyone

Paste the following value:

mxb.mailgun.org

![2nd MX Points To field — mxb.mailgun.org](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292770829/original/lo34kUcHgQ_jNcW7DaT0x3DUPiEu1AubLw.png)

D. Priority — same for everyone

Set Priority to **10**.

![2nd MX Priority field set to 10](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292770920/original/Fw8uyagc8TOy9xxMDsHe3atzfkyEu3QnKw.png)

E. Save

Click **Save** to confirm this record.

![Saving the 2nd MX record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292770952/original/JOROtyvxFT7kuhgJS6UKxsSCMfE6_5IS8A.png)

7

## Add the CNAME Record

Click **Add** in the GoDaddy DNS editor to create a new record.

![GoDaddy Add button for new DNS record](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284383808/original/H6np93jJkfJVHPLdTaLTLmRgo2mB_c6JRA.png)

![CNAME record form in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284385821/original/Z_H7aEV9Fj-ulIPJTmhnmpgRUG-CWVntNA.png)

A. Type

Select **CNAME** from the Type menu.

B. Host — copy from the platform DNS records screen

The CNAME hostname is prefixed with **email.** followed by your subdomain prefix. Copy the portion before the root domain from the platform's DNS records screen:

  * lc.companyname.com → enter **email.lc**
  * replies.companyname.com → enter **email.replies**
  * Root domain companyname.com → enter **email**


![CNAME host field in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292771034/original/ey4vFuccg-PcVOVNEqKhNZR24VOtPxjuCA.png)

C. Points To — same for everyone

Paste the following value:

mailgun.org

![CNAME Points To field — mailgun.org](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292771083/original/z9S5z7FviH8eq6xc6sXjhiBRLNZCCKQ5LA.png)

D. Save

Click **Save** to confirm this record.

![Saving the CNAME record in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292761511/original/Q-pg6CdROQ4wXlfIoOIOkvDgY1yJdVN1Ug.png)

![All 5 DNS records saved in GoDaddy](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48284386112/original/kW6t3s2sXMcjCylHMSgGSwJy8HDwA4momQ.png)

All 5 Records Saved

All 5 DNS records have been added to GoDaddy. Proceed to Section 8 to verify your domain.

8

## Verify Your Domain

Switch back to the platform tab and click **Verify Domain** on the Email Services screen.

![Verify Domain button in Email Services](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292771391/original/DSHng9iQ27K8gMmkLYLkL7mpGKnMfyFSkA.png)

Some records still not green?

DNS propagation can take a few minutes. Click **Verify Domain** again after waiting a moment. If records remain unverified after 10+ minutes, go back to GoDaddy and confirm each record's Type, Host, and value are correct.

You're All Set

Once all records show a green checkmark, your dedicated sending domain is active. Next, confirm your [SSL Certificate for Dedicated Sending Domain (LC Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) is properly set up.

Then send a test email to confirm everything is working. [Learn how to send a test email in the Conversation.](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>)

9

## Frequently Asked Questions

Q: Why do I need to save after each record in GoDaddy?

GoDaddy's DNS editor saves records one at a time. Unlike some providers that let you queue multiple records and save at once, GoDaddy requires each record to be individually confirmed. Follow the steps in order and click Save after each one.

Q: Can I use my root domain if I already use it with Google Workspace?

No. Adding MX records to a root domain that is already in use with Google Workspace will conflict with your existing email setup. Use a subdomain (e.g. **replies.companyname.com**) for LC Email instead.

Q: Why do I add two separate MX records instead of one?

The two MX records (**mxa.mailgun.org** and **mxb.mailgun.org**) provide redundancy — if one mail server is temporarily unavailable, the other can receive messages. Both should be added with Priority 10. GoDaddy requires each MX record to be added and saved separately.

Q: Why is the 2nd TXT record hostname different from what I see in examples?

The 2nd TXT record is a DKIM key generated uniquely for your domain. Its hostname and long value are always different per account. Always copy both from your own DNS records screen — never use values shown in screenshots in this article.

Q: How long does DNS propagation take in GoDaddy?

GoDaddy DNS changes typically propagate within a few minutes to an hour. If records are still not verifying after 10 minutes, wait a bit longer before troubleshooting. Full propagation can take up to 48 hours in rare cases.

Q: What is the difference between a dedicated and a shared sending domain?

A **shared domain** is used by multiple accounts, meaning your sender reputation is pooled with others. A **dedicated domain** is exclusive to your account, giving you full control over your deliverability reputation as it builds over time.

Q: My domain shows as verified but emails are not delivering — what should I check?

First, send a test email from the Conversations area to confirm basic sending is working. Then check that the [SSL Certificate for your Dedicated Sending Domain](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) is active. If issues persist, review each of your 5 GoDaddy DNS records for typos in the Host or Points To fields.

Q: Can I set up multiple dedicated domains for different sub-accounts?

Yes. Each sub-account can have its own dedicated sending domain. Each domain requires its own complete set of 5 DNS records to be added and verified separately in GoDaddy.

Related Articles

[How to Migrate My Agency Over to LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>) [How to Set Up a Dedicated Sending Domain (LC Email)](<https://help.gohighlevel.com/support/solutions/articles/48001226115>) [SSL Certificate for Dedicated Sending Domain (LC Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) [How to Send a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>)

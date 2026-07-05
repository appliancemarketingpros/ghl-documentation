# Google Dedicated Sending Domain Setup (LC Email)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001240481-google-dedicated-sending-domain-setup-lc-email-](https://help.gohighlevel.com/support/solutions/articles/48001240481-google-dedicated-sending-domain-setup-lc-email-)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Infrastructure

LC Email Dedicated Domain Setup — Google Domains

A step-by-step guide to adding and verifying your dedicated sending domain using Google Domains DNS.

What You'll Learn

This article walks you through connecting a dedicated sending domain to LC Email using Google Domains as your DNS provider. You will add 5 DNS records in total: 2 TXT records, 2 MX records, and 1 CNAME record.

You can set up either your root domain (companyname.com) or a subdomain (e.g. replies.companyname.com). If you already use Google Workspace for email on your root domain, you must use a subdomain instead.

Table of Contents

1

Add Your Domain in Email Services

2

Open Google Domains DNS

3

Add the 1st TXT Record (SPF)

4

Add the 2nd TXT Record (DKIM)

5

Add MX Records

6

Add the CNAME Record

7

Save & Verify Your Domain

8

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

If you use Google Workspace to send and receive mail on your root domain (e.g. user@companyname.com), you **must** use a subdomain here. Adding the root domain will conflict with your existing Google Workspace MX records. See [Can I use the same domain for Mailgun and Google Apps?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

Step 3

Click Add & Verify

After entering your domain name, click **Add & Verify**. The next screen will display the 5 DNS records you need to add. Keep this tab open — you will copy values from it in the steps below.

![Add & Verify button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292766472/original/5TxDqQG542C3YtKLt6stGIAfwcbDmmcesg.png)

![DNS records screen showing 5 records to add](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48293298198/original/xGMUZ9x0JoahqbofrVsYVWEjEF9LDDvsMQ.png)

Keep this DNS records screen open — you will copy values from it in the steps below.

Tip

Migrating from Mailgun? See [How to move a sending domain from Mailgun to LeadConnector](<https://help.gohighlevel.com/support/solutions/articles/48001226115-how-to-set-up-a-dedicated-sending-domain-lc-email-#How-to-move-sending-domain-from-Mailgun-to-LeadConnector?>).

2

## Open Google Domains DNS

In a new browser tab, log in to [domains.google.com](<https://domains.google.com/>), click into the domain you are setting up, then click **DNS** in the left panel. You will add all 5 records here.

![Google Domains DNS panel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48299273463/original/nvtEdnUCOa_aEuQG29TmvxEc8zT-TEDQbw.png)

Reminder

Do **not** click Save after each individual record. Add all 5 records first, then save once at the end.

DNS Setup Guide

Adding Your 5 DNS Records

Follow sections 3–6 to add 2 TXT records, 2 MX records, and 1 CNAME. Don't save until all 5 are entered.

3

## Add the 1st TXT Record (SPF)

Click **Create new record** in Google Domains and fill in the fields below.

Host Name

Enter only the subdomain prefix — do not include the root domain

Google Domains appends your root domain automatically. Enter only the prefix part:

  * Setting up **lc**.companyname.com → enter **lc**
  * Setting up **replies**.companyname.com → enter **replies**
  * Setting up root domain companyname.com → enter **@**


![Host name field in Google Domains — enter subdomain prefix only](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48299273966/original/QyOvl4oeTZwm5vxk_Qr4E9axVI_3VmGQbQ.png)

Type

Select **TXT** from the Type dropdown.

Data — same for everyone

Paste the following SPF record value exactly as shown:

v=spf1 include:mailgun.org ~all

![SPF TXT record filled in Google Domains](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292767368/original/n_1Mu3Av0f2EYEvZG9iBeM-knKybDa2RPg.png)

Next Step

Do **not** click Save yet. Click **Create new record** to continue to the 2nd TXT record.

4

## Add the 2nd TXT Record (DKIM)

Important

Everyone's 2nd TXT record hostname and value is **unique to their domain**. Copy both values directly from your platform's DNS records screen — do not use values from screenshots in this article.

Type

Select **TXT** from the dropdown.

![Selecting TXT from the type dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48299274267/original/tgkjiuJTNQWqB0YufpMnGh7eGG8ju2BhYQ.png)

Host Name

Copy everything before your root domain — do not include the root domain itself

Look at the 2nd TXT hostname in your DNS records screen. Copy only the portion before your root domain name. The examples below show which part to copy.

![2nd TXT host name field — copy highlighted portion only](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48299274349/original/QZx8yVWaSu8EU88v7eBp1CPDH4P80GKGXg.png)

Scenario| Copy this as hostname| Example  
---|---|---  
Using a subdomain| mx._domainkey.helpdesk| ![Subdomain DKIM hostname example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768867/original/Oy2wnQ4XgDD5YzExKorYuiEBhl-wH7krkg.png)  
Using the root domain| mailo._domainkey| ![Root domain DKIM hostname example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768954/original/rXlYB3cbDo6Ix-Oq_XBgdnsiwBHDHuTUig.png)  
  
Data

Paste the full 2nd TXT record value from your platform's DNS records screen. This value is unique to your domain — copy it as-is from the highlighted field.

![2nd TXT record value — copy the highlighted value](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292768735/original/cUIeRsQGsIF81ZCW8a-cj-v7iGlndoLiKw.png)

Next Step

Do **not** click Save yet. Click **Create new record** to add the MX records.

5

## Add MX Records

Click **Create new record** in Google Domains and fill in the fields below.

Google Workspace Users

If you have a Google Workspace account that sends and receives mail on your root domain, adding MX records to the root domain will break existing email. Use a subdomain for LC Email. See [Can I use the same domain for Mailgun and Google Apps?](<https://help.mailgun.com/hc/en-us/articles/203357040-Can-I-Use-the-Same-Domain-Name-for-Mailgun-and-for-Google-Apps-Or-Another-Email-Server->)

Host Name

Same logic as the TXT records — enter only the subdomain prefix:

  * **lc**.companyname.com → enter **lc**
  * **replies**.companyname.com → enter **replies**
  * Root domain companyname.com → enter **@**


![MX record host name field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155000003027/original/5aF_dZ_ziXuTz59XlBASIHTyI7uQ7bOo_g.png)

Type

Select **MX** from the dropdown.

Data

Paste the first MX value, then click **\+ Add more to this record** and paste the second:

10 mxa.mailgun.org

10 mxb.mailgun.org

![MX records data entry](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155000003013/original/7ZgVLhVdhJ7tXtoJ_8k_TFkrR5RA2pUb4g.png)

![MX records completed](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155000003080/original/w3lgIZMfVu8zipEIyYvMh72IQgpl6HADcA.png)

Next Step

Do **not** click Save yet. Click **Create new record** to add the final CNAME record.

6

## Add the CNAME Record

Click **Create new record** in Google Domains and fill in the fields below.

Host Name

The CNAME hostname is prefixed with **email.** followed by your subdomain prefix:

  * lc.companyname.com → enter **email.lc**
  * replies.companyname.com → enter **email.replies**
  * Root domain companyname.com → enter **email**


Type

Select **CNAME** from the dropdown.

Data — same for everyone

mailgun.org

![CNAME record fields filled in](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155000003126/original/UjjcYWc_abbbgStIJ5Q7rOwoXfIFdaAT4g.png)

![CNAME record completed](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155000003129/original/4CjEilgb6jZy-PnRXT7Eyoxf94_AeHGPcw.png)

All 5 Records Added

You have now entered all 5 DNS records. Proceed to Section 7 to save and verify.

7

## Save & Verify Your Domain

Step 1

Save in Google Domains

Now that all 5 DNS records are entered, click **Save** in Google Domains.

Step 2

Verify in Email Services

Switch back to the platform tab and click **Verify Domain** on the Email Services screen.

![Verify Domain button in Email Services](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48292771391/original/DSHng9iQ27K8gMmkLYLkL7mpGKnMfyFSkA.png)

Some records still not green?

DNS propagation can take a few minutes. Click **Verify Domain** again after waiting a moment. If records remain unverified after 10+ minutes, double-check the values you entered in Google Domains against the platform's DNS records screen.

You're All Set

Once all records show a green checkmark, your dedicated sending domain is active. Next, confirm your [SSL Certificate for Dedicated Sending Domain (LC Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) is properly set up.

Then send a test email to confirm everything is working. [Learn how to send a test email in the Conversation.](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>)

8

## Frequently Asked Questions

Q: Can I use my root domain if I already use it with Google Workspace?

No. Adding MX records for a root domain that is already used with Google Workspace will conflict with your existing Google Workspace MX records and break email delivery. Use a subdomain (e.g. **replies.companyname.com**) for LC Email instead.

Q: How long does DNS propagation take in Google Domains?

Changes in Google Domains typically propagate within a few minutes, though it can occasionally take up to 24–48 hours. If records are not verifying after 10 minutes, wait a bit and try again before troubleshooting values.

Q: Why is the 2nd TXT record hostname different from examples I see online?

The 2nd TXT record is a DKIM key that is generated uniquely for your domain. Its hostname and value will always differ from other accounts. Always copy both from your own DNS records screen — never from this article or another account's setup.

Q: What is the difference between a dedicated domain and a shared domain?

A **shared domain** is a common sending domain shared across multiple accounts — quick to enable, but your sender reputation is pooled with others. A **dedicated domain** is exclusive to your account, giving you full control over your sender reputation and deliverability.

Q: Can I set up multiple dedicated domains for different sub-accounts?

Yes. Each sub-account can have its own dedicated sending domain. Each domain requires its own set of DNS records to be added and verified separately.

Q: Will my contacts notice a change after I switch to a dedicated domain?

Not directly — the sending domain appears in email headers but not in the visible "From" name. Over time, a dedicated domain improves deliverability as your sender reputation builds independently.

Q: My domain shows as verified but emails still aren't delivering — what should I check?

Send a test email from the Conversations area first to confirm basic sending works. Then check that the [SSL Certificate for your Dedicated Sending Domain](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) is active. If issues persist, review your SPF and DKIM values in Google Domains for any typos.

Q: Is there a cost to use a dedicated sending domain?

Setting up a dedicated sending domain through LC Email does not require a separate paid plan beyond your existing subscription. You do need to own and manage the domain through your DNS provider (in this case, Google Domains).

Related Articles

[How to Migrate My Agency Over to LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>) [How to Set Up a Dedicated Sending Domain (LC Email)](<https://help.gohighlevel.com/support/solutions/articles/48001226115>) [SSL Certificate for Dedicated Sending Domain (LC Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) [How to Send a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>)

# Setting Up SMTP Providers

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001059689-setting-up-smtp-providers](https://help.gohighlevel.com/support/solutions/articles/48001059689-setting-up-smtp-providers)  
**Category:** Email  
**Folder:** SMTP Providers

---

Email Services

# SMTP Setup Guide

Everything you need to configure, test, and troubleshoot your SMTP provider integration with GoHighLevel.

⚠️

**Before You Use SMTP — Read This** We have direct integrations with both **Google** and **Outlook**. If you're sending through these providers, please use those integrations instead of SMTP.

**Gmail Sync:** [Two-Way Email Sync for Gmail](<https://help.gohighlevel.com/support/solutions/articles/48001235216-how-to-set-up-two-way-email-sync-for-gmail>)

**Outlook Sync:** [Two-Way Email Sync for Outlook](<https://help.gohighlevel.com/support/solutions/articles/48001229663-two-way-email-sync-for-outlook>)

**LC Email:** [What is LC Email?](<https://help.gohighlevel.com/support/solutions/articles/48001220605-what-is-lc-email-i-want-to-know-more>)

If you choose to use SMTP, you do so at your own discretion. SMTP is an advanced use case and not how most users should send email through HighLevel. Support is provided on a best-effort basis.

## A List of SMTP and IMAP Servers

Use the reference below to look up the SMTP and IMAP server settings for your email provider:

[ ? SMTP & IMAP Server Reference List ](<https://www.arclab.com/en/kb/email/list-of-smtp-and-imap-servers-mailserver-list.html>)

## Sender Email Address Configuration Limitation

If you are using an SMTP provider, make sure the sender email you mask here **matches the email you integrated with**. [Learn more on how to configure the sender's email address here](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>).

?

If the sender's email does not match the SMTP integrated email, or if the sender's email is not verified with your SMTP provider, the email **will fail to deliver**.

## How to Test Your SMTP Integration

When sending an email, update the sender's email address so it matches the integrated SMTP email.

In manual conversation, the sender email defaults to your login email. You'll need to change it to match the SMTP integrated email. By default it will show your login email:

![SMTP sender email configuration screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029827288/original/gnPwP2x5q8zEvsCuFGHt1QHIQlamElUaEA.jpg?1721840067)

## Daily Sending Limits

Your SMTP provider may impose daily limits on email volume. [Gmail, for example, limits approximately 100–150 emails per day](<https://support.google.com/a/answer/166852?hl=en>) when connected via a remote email client.

[Why Can't I Use My Free Email Address As The SMTP? →](<https://help.gohighlevel.com/en/support/solutions/articles/48001063376>)

## Workflow / Email Statistics

Via SMTP, we currently receive only **sent** , **open** , **click** , and **bounce** events. A **delivered** event is not available from the SMTP provider.

ℹ️

Because of this limitation, the system marks an email as **delivered only after an open event is received**.

We highly recommend [setting up Mailgun or LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001219824>) to get full sending statistics. Learn more about [Troubleshooting Email Stats](<https://help.gohighlevel.com/en/support/solutions/articles/48001208601>).

## Why SMTP Emails Are Stuck in "Sent" Status

With SMTP, we only receive **sent** , **open** , **click** , and **bounce** events. A **delivered** event is not available from the SMTP provider.

Because of this limitation, the system marks an email as **delivered only after an open event is received**.

That's why the email initially shows as **sent**. Once the recipient opens the email, the status updates accordingly.

## Common Issues When Setting Up SMTP Providers

1 Make sure [Email Re-Billing](<https://help.gohighlevel.com/en/support/solutions/articles/48001188579>) is **disabled** while making changes to the default provider.

2 Try testing your SMTP credentials using the GMass SMTP Test tool: [gmass.co/smtp-test](<https://www.gmass.co/smtp-test>)

## Help Docs for SMTP Providers

[ ? Google / Gmail / GSuite – Using Google as Your SMTP Provider ](<https://help.gohighlevel.com/en/support/solutions/articles/48001148427>) [ ? Setting an Alias for Google SMTP ](<https://help.gohighlevel.com/en/support/solutions/articles/48001184605>)

? Yahoo – Temporarily disabled SMTP. No ETA on availability.

[ ? SendGrid – Using SendGrid as the SMTP Provider ](<https://help.gohighlevel.com/en/support/solutions/articles/48001166110>) [ ? Zoho – Using Zoho as Your SMTP Provider ](<https://help.gohighlevel.com/en/support/solutions/articles/48001173743>)

## Setting Up Amazon SES

Follow these steps when configuring Amazon SES as your SMTP provider:

1 Use the correct server name listed on the **SMTP Settings** page.

2 Use **port 465**.

3 Use the **IAM Username & Password** you created (save these — you cannot view them again).

4 Use the **Amazon AWS Root User Email Address**.

Amazon SES Resources

[ ? Amazon SES Quick Start Guide ](<https://docs.aws.amazon.com/ses/latest/DeveloperGuide/quick-start.html>) [ ? Managing Your Amazon SES Sending Quotas ](<https://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-sending-quotas.html>) [ ? Moving Out of the Amazon SES Sandbox ](<https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html>)

## Setting Up Outlook / Microsoft Office 365

It is common to see an **"Authentication unsuccessful"** error even with two-step verification disabled. Microsoft changed its security requirements — third-party apps now require **SMTP Authentication to be explicitly enabled**.

[ ? Microsoft Guide: Enable SMTP Authentication ](<https://docs.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365>)

If the above guide does not resolve your issue, please reach out to **Outlook support** to get the account authenticated.

## Frequently Asked Questions

Q The "Add Service" button is missing in the Email Services > SMTP services tab. How do I fix this?

Switch to **Agency View → Sub-accounts** , click the three dots next to the account, then select **Manage Client**.

![Manage Client screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030990778/original/1NAK5QK9IlXxPlsN-xmBJpq5lMvM1QTfyA.png?1723595394)

Click on **Advanced Settings** and make sure **"Disable the Add Email Service button in the sub-account Email Services Settings"** is turned **off**.

![Advanced Settings screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030990761/original/IQ70geRyZWV4bKSosx3qOb5Eni3qMnRH8g.png?1723595268)

Q How many SMTP service providers can we have on a sub-account?

A sub-account can have **multiple SMTP service providers**. However, the same SMTP credentials cannot be added more than once — using the same email ID with different integrations is not allowed. Additionally, the same provider (e.g., Gmail) cannot be added twice.

Related Articles

[ ? Hide The SMTP Setup Help Doc Link ](<https://help.gohighlevel.com/support/solutions/articles/48001065654-hide-the-smtp-setup-help-doc-link>) [ ? Setting Alias for Google SMTP ](<https://help.gohighlevel.com/support/solutions/articles/48001184605-setting-alias-for-google-smtp>)

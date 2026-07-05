# Limitation of using SMTP when emails are not sending

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001203144-limitation-of-using-smtp-when-emails-are-not-sending](https://help.gohighlevel.com/support/solutions/articles/48001203144-limitation-of-using-smtp-when-emails-are-not-sending)  
**Category:** Email  
**Folder:** SMTP Providers

---

Email Deliverability

Why Your SMTP Emails Aren't Delivering

The most common cause of SMTP delivery failures — a sender email mismatch — plus how to check errors and set up sender identities by provider.

Overview

If you're using an SMTP provider to send emails and they're not delivering most of the time, the reason is usually that the [sender email](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>) doesn't match the SMTP email you've configured. This article covers how to spot that mismatch, how to read the error the platform shows you, and how to verify a sender identity for the most common SMTP providers.

Table of Contents

1

The most common cause: a sender email mismatch

2

Checking the error in a conversation

3

Verifying your sender by provider

4

Frequently Asked Questions

Video Walkthrough

1

## The most common cause: a sender email mismatch

If your SMTP provider is connected but most emails still aren't delivering, check whether the **sender email** matches the SMTP email you've configured. This is the single most common reason SMTP-sent emails fail.

![SMTP configuration screen showing the sender email field to check for a mismatch](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48280761517/original/7EeQW-iMOrII91u4q9JADK0pynS16WBRlg.png?1675971805)

2

## Checking the error in a conversation

Once your SMTP provider is set up, if you get an error when you [send a test email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>), you can click the **⚠️ (red triangle) icon** to view more details about the error.

![Clicking the red triangle icon to view SMTP error details in a conversation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48280761065/original/ema0tGCjaqikKsDX4vwAd2Tkm7VsoO1DuQ.png?1675971606)

What Changed

The error shown in the conversation is fetched directly from your SMTP provider. If you're already sending from the SMTP-integrated email address and still seeing the error, open a support ticket with your SMTP provider so they can share the delivery status of the email.

3

## Verifying your sender by provider

Each SMTP provider handles sender verification a little differently. Use the guide below for the provider you're connected to.

Google Workspace (G Suite)

Setting an alias for Google SMTP

[help.gohighlevel.com/support/solutions/articles/48001184605-setting-alias-for-google-smtp](<https://help.gohighlevel.com/support/solutions/articles/48001184605-setting-alias-for-google-smtp>)

SendGrid

Sender identity setup

[docs.sendgrid.com/ui/sending-email/senders](<https://docs.sendgrid.com/ui/sending-email/senders>)

Zoho

Using Zoho as your SMTP provider

[help.gohighlevel.com/support/solutions/articles/48001173743-using-zoho-as-your-smtp-provider](<https://help.gohighlevel.com/support/solutions/articles/48001173743-using-zoho-as-your-smtp-provider>)

4

## Frequently Asked Questions

Q: What does it mean if the sender email doesn't match my SMTP email?

It means the address shown as the "from" is different from the address actually authenticated with your SMTP provider. Most providers reject or fail these mismatched sends.

Q: How do I fix a sender email mismatch?

Either update the sender email so it matches the address integrated with SMTP, or verify the sender address separately with your SMTP provider, depending on what that provider requires.

Q: What does clicking the red triangle icon show me?

It expands the error message returned directly by your SMTP provider for that specific send, which usually points to the exact cause — like an unverified sender.

Q: Can I mask my sender email and still avoid this error?

Yes, as long as the masked address either matches your SMTP-integrated email or is separately verified with your provider. See the sender masking article for details.

Q: Who do I contact if the error persists even after fixing the mismatch?

Open a support ticket directly with your SMTP provider. They can check the delivery status on their end and confirm whether the issue is with sending or with the recipient's inbox.

Q: Does sender verification work the same way across all providers?

No — each provider has its own process. Google Workspace uses email aliases, SendGrid uses sender identities, and Zoho verifies through account credentials. Use the provider-specific links above.

Related Articles

[Masking Sender Emails - From Name & Address](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>) [Why Can't I Use My Free Email Address As The SMTP?](<https://help.gohighlevel.com/en/support/solutions/articles/48001063376>) [Sending a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>)

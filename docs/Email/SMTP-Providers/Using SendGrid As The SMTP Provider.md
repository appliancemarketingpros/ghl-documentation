# Using SendGrid As The SMTP Provider

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001166110-using-sendgrid-as-the-smtp-provider](https://help.gohighlevel.com/support/solutions/articles/48001166110-using-sendgrid-as-the-smtp-provider)  
**Category:** Email  
**Folder:** SMTP Providers

---

Email Infrastructure

Integrating SendGrid as Your SMTP Provider

Step-by-step setup for connecting SendGrid so your outbound email sends reliably through a verified SMTP provider.

Overview

This guide walks through connecting SendGrid as your SMTP provider within the platform. It covers the exact configuration and settings needed for seamless, reliable email delivery through SendGrid.

Follow each step in order — from creating your SendGrid account through verifying a sender identity — to avoid the most common connection errors. For deeper troubleshooting, see the dedicated section near the end of this article.

Table of Contents

1

Sign up for SendGrid

2

Go to Location Settings in your sub-account

3

Get your SendGrid API key

4

Add your API key to the platform

5

Set up 2FA with SendGrid

6

Verify your SendGrid account as a single sender

7

Save again to complete the integration

8

Troubleshooting a sender identity error

9

Frequently Asked Questions

Video Walkthrough

1

## Sign up for SendGrid

If you don't already have a SendGrid account, create one at [signup.sendgrid.com](<https://signup.sendgrid.com/>).

2

## Go to Location Settings in your sub-account

Click on **Email Services → Add Service** , then select **SendGrid** from the dropdown.

If you want to integrate SendGrid for all locations at once, you can set this up from the agency view instead:

<https://app.gohighlevel.com/settings/email_services>

![Selecting SendGrid from the Email Services dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846783/original/VVFsJCextfR1_d_11XTHga9oeNKatWS0hQ.jpg?1724881299)

3

## Get your SendGrid API key

In SendGrid, click **Settings → API Keys → Create API Key**.

![Creating a new API key in SendGrid settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846792/original/eUL7EU_-EOzGchxYPWL0EMk5sjACZxHEPw.jpg?1724881326)

Sub-step A

Type an API Key Name

Make sure **API Key Permissions** is set to **Full Access** , then click **Create & View**.

![Naming the API key with Full Access permissions selected](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846796/original/a9MrgUej0WqHziz31i8UjSTQwtbDIFmj4A.jpg?1724881352)

Sub-step B

Copy the highlighted API key

SendGrid only shows the full key once — copy it now. You'll paste it into the platform in the next step.

![Copying the generated SendGrid API key](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846806/original/vmo403We5u7Gp8bKNAXeV7jlxNY_I1Ysag.jpg?1724881381)

4

## Add your API key to the platform

Username: **apikey**

Email: **your SendGrid login email**

Password: **paste the copied API key here**

Click **Save**.

![Entering the SendGrid API key into the platform's email service settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846811/original/kq58-V-iDLVwKZwNQXw_UXO2lwUUiMcY9Q.jpg?1724881409)

5

## Set up 2FA with SendGrid

SendGrid requires two-factor authentication on your account before it will allow full API access. Complete the 2FA setup from your SendGrid account settings if you haven't already.

![Setting up two-factor authentication in SendGrid](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846832/original/HYY2tHoxAB-4qW-jO_raEIIxKBf7lj2QWA.jpg?1724881430)

6

## Verify your SendGrid account as a single sender

![Verifying a SendGrid single sender](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846845/original/9ipTCXKk0sEKBCLdPOYf1kDUFCiCjpvzAw.jpg?1724881455)

Create a sender here using your **SendGrid login email**.

![Creating a sender identity with your SendGrid login email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846859/original/zBMxS2C0LUORdKKq5EvXd_eDtR6jhzybiQ.jpg?1724881476)

7

## Save again to complete the integration

Go back to the platform and click **Save** again to finalize the integration.

![Saving the SendGrid integration again in the platform](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846872/original/XR8nHLqvALSgWinGBq6BV3WYFk9rfKfzPA.jpg?1724881510)

You'll now see SendGrid listed as your active SMTP provider in the platform.

![SendGrid now displayed as the active SMTP provider](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846879/original/wL9FUvg9EHRVoljO3xNEpr5RS0vzxaYFdA.jpg?1724881532)

8

## Troubleshooting a sender identity error

If you get an error when you [send a test email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>), click the **⚠️ (red triangle) icon** to view more details about the error.

![Viewing the error details icon in the conversation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031846886/original/q9lMrW_IBu8lblpact0WJarWC8nimrXzTw.jpg?1724881564)

Common Error

550 The from address does not match a verified Sender Identity. Mail cannot be sent until this error is resolved.

Visit SendGrid's [Sender Identity requirements](<https://sendgrid.com/docs/for-developers/sending-email/sender-identity/>) to see what's needed.

Tip

If you're using [sender masking](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>), make sure the masked sender email matches the SMTP-integrated email, or that the sender email is separately verified with SendGrid at [docs.sendgrid.com/ui/sending-email/senders](<https://docs.sendgrid.com/ui/sending-email/senders>).

9

## Frequently Asked Questions

Q: Do I need a paid SendGrid plan to use this integration?

No — SendGrid's free tier includes API key access and sender verification, which is all this integration requires. Higher sending volumes may eventually require a paid plan.

Q: Why do I need to verify a sender identity in SendGrid?

SendGrid blocks outbound mail from any "from" address that hasn't been verified as a sender on your account. This prevents spoofing and protects deliverability for everyone using SendGrid.

Q: What should I enter in the password field when connecting SendGrid?

Paste your full SendGrid API key into the password field — not your actual SendGrid account password. The username should always be **apikey**.

Q: Can I still mask the sender email if I'm using SendGrid?

Yes, but the address you mask must either match the address integrated with SMTP or be separately verified as a sender in SendGrid — otherwise you'll hit the sender identity error.

Q: What does the "550 sender identity" error mean?

It means SendGrid rejected the message because the from address isn't a verified sender on your SendGrid account. Verify that address as a single sender to resolve it.

Q: Is two-factor authentication required for the API key to work?

Yes. SendGrid requires 2FA to be enabled on the account before full-access API keys can be created and used.

Q: What happens if I regenerate my API key later?

The old key stops working immediately. You'll need to update the password field in your email service settings with the new key to keep sending.

Related Articles

[Sending a Test Email in the Conversation](<https://help.gohighlevel.com/en/support/solutions/articles/48001208887>) [Masking Sender Emails - From Name & Address](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>)

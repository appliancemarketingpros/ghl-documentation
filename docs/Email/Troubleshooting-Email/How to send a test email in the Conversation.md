# How to send a test email in the Conversation

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001208887-how-to-send-a-test-email-in-the-conversation](https://help.gohighlevel.com/support/solutions/articles/48001208887-how-to-send-a-test-email-in-the-conversation)  
**Category:** Email  
**Folder:** Troubleshooting Email

---

Email Deliverability

How to Send a Test Email in a Conversation

Create a test contact, send a test email, configure your sender address, and troubleshoot delivery issues.

Overview

This guide walks through creating a test contact, sending a test email, configuring your sender address for Mailgun or SMTP, and troubleshooting delivery if the email doesn't arrive or replies don't come back.

Table of Contents

1

Creating a Test Contact

2

Sending the Test Email

3

Configuring the Sender's Email

→ If you're using Mailgun → If you're using SMTP integration

4

Troubleshooting Email Delivery

5

If Email Replies Are Not Coming Back

6

FAQ

1

## Creating a Test Contact

Step 1

From agency view, click **Click here to switch** in the top left.

Step 2

Click the sub-account you want to test in.

Step 3

Click **Contacts**.

![Switching to a sub-account and opening Contacts](https://i.ibb.co/zNV0S4V/2023-1-24-11-50-37.gif)

Step 4

Click **Add Contact**.

![Add Contact button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029821714/original/3CoAFhjjyHDlYZmB19SN0T_TqAK1e37VWA.jpg?1721834838)

Step 5

Fill out the **First name** and **email** , then click **Save**.

![Add Contact form with name and email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029821818/original/I96Iz9MiMb85t_HZYfAbvYtTFXY5aptZcw.jpg?1721834890)

2

## Sending the Test Email

Saving the contact should automatically redirect you to the conversation page. Click **Send Email** below.

![Send Email button in the conversation view](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029821920/original/mO1ZsfTekzCkLub_fVoTZq3HSilwgaU1Rg.jpg?1721834939)

3

## Configuring the Sender's Email

The highlighted field is where you configure the sender's email address. By default, it shows the logged-in user's email as the sender. [See how to configure the sender email address when sending bulk emails](<https://gohighlevelassist.freshdesk.com/support/solutions/articles/48000979925-masking-campaign-emails-from-name-address>).

![Sender email field in the conversation composer](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029822266/original/ooUl9-PlqUjmPxfLAtVJujfPR5tACZMRDg.jpg?1721835184)

If you're using Mailgun

If you mask the sender email as `testing@gmail.com`, the reply-to address will show as `testing@replies.subdomain.com` — the Mailgun subdomain set up for the sub-account under **Agency Settings → Email Services → Location Settings**. Replies will still appear correctly in the sub-account's Conversation tab.

For example, if your Mailgun subdomain is `subdomain.yourdomain.com`, the reply-to email address will show as `kate@subdomain.yourdomain.com`.

![Reply-to address matching the Mailgun subdomain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029822829/original/sIHHts5GEbn1g0b-ruhREN619Is0x-QMkA.jpg?1721835508)

You can set `testing@subdomain.com` as the sender's email address to improve deliverability, since the reply-to address domain will then match the sender's email domain.

You can also set up [cold inbound email](<https://help.gohighlevel.com/support/solutions/articles/48001185801-cold-email-inbound-setup>) to capture any emails sent to addresses ending in `@replies.subdomain.com`.

If you're using SMTP integration

Go to **Sub-account Settings → Email Services**.

Copy the highlighted email address integrated as your SMTP sender, and use that as the sender email in the conversation tab.

![SMTP sender email in Email Services settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029823782/original/2kuSUuG1Pr11ztYDcKVm960c_D1TdBV7PQ.jpg?1721836209)

Depending on your SMTP integration, you can set up an alias or verified sender to send from other addresses:

  * [Setting up an alias for Google SMTP](<https://help.gohighlevel.com/support/solutions/articles/48001184605-setting-alias-for-google-smtp>)
  * [Setting up an alias for Zoho SMTP](<https://help.gohighlevel.com/support/solutions/articles/48001173743-using-zoho-as-your-smtp-provider>)
  * [Verifying sender email with SendGrid](<https://docs.sendgrid.com/ui/sending-email/senders>)


4

## Troubleshooting Email Delivery

Once you send the email, if you don't receive it, be sure to check the spam folder.

For errors displayed in the Conversation view, we fetch the error from the Mailgun API or SMTP server and display it. Click the error icon to view the full message — it should explain why the email couldn't send.

If the error isn't helpful, open a support ticket with your SMTP provider so they can provide the delivery status for that email.

If you're using Mailgun, you can [check the Mailgun logs](<https://help.gohighlevel.com/support/solutions/articles/48001188059-how-to-check-logs-for-a-specific-email-in-mailgun>) and check out our [email not sending help doc](<https://gohighlevelassist.freshdesk.com/support/solutions/articles/48000981687-emails-not-sending>).

5

## If Email Replies Are Not Coming Back

Once you receive the test email, reply to it and check whether the reply shows up in the Conversation tab. If it doesn't, see [When email replies are not coming back to the Conversation](<https://help.gohighlevel.com/support/solutions/articles/48001185819-when-email-replies-are-not-coming-back-to-the-conversation>).

6

## FAQ

Q: Do I need to create a new test contact every time, or can I reuse one?

You can reuse the same test contact for future checks. Just make sure the email address on it is one you can actually access, so you can confirm delivery and test replies.

Q: Why does the reply-to address look different from the sender address on Mailgun?

When you mask the sender with a different address, replies are still routed through your Mailgun subdomain so they can be tracked back into the Conversation tab — that's why the reply-to domain can differ from the sender you typed.

Q: I don't see a Send Email button on the test contact's conversation — why?

Make sure the contact was saved with a valid email address and that you're viewing the Email tab (not SMS or another channel) within the conversation.

Q: Can I use my own personal email as the sender for testing?

Yes, for a quick test. For production sending, use a sender address on your verified/configured domain so deliverability and reply routing work as expected.

Q: How can I tell if a delivery failure is on our end vs. the recipient's mail server?

Click the error icon on the failed message in the Conversation view. If it references a specific rejection reason from the receiving mail server, the issue is likely on their end; if it references your domain setup, check your DNS/CNAME/MX records first.

Q: Do these steps differ if I'm on LC Email instead of Mailgun or SMTP?

The test contact and Send Email steps are the same. Sender configuration is simpler on LC Email since it's managed for you — you won't need to configure a Mailgun subdomain or SMTP alias separately.

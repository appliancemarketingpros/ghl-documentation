# Sending Priority - From Name & Address

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000979925-sending-priority-from-name-address](https://help.gohighlevel.com/support/solutions/articles/48000979925-sending-priority-from-name-address)  
**Category:** Email  
**Folder:** General

---

Email Configuration

Sender Email Priority & Configuration

Understand which sender email your contacts will see — and where to configure it for manual emails, automated emails, and workflows.

Heads up

Workflows are now live in all accounts. You can do everything Triggers and Campaigns do — and more — all in one builder.

What You'll Learn

Which sender email gets used when you send to a lead — manual vs automated, assigned vs unassigned — and the priority order each one follows.

Then a tour of every place you can configure the sender email: Conversations, Email Templates, Bulk Send, Workflow settings, and Workflow Send Email actions.

Table of Contents

1

Which Sender Email Should the Leads Be Receiving Emails From?

2

How to Check If Contacts Are Assigned or Unassigned

3

Manual Email — The Conversation Tab

4

Automated Email — Email Templates

5

Automated Email — Bulk Action: Send Email

6

Automated Email — Workflow Settings

7

Automated Email — Workflow Send Email Action

8

Frequently Asked Questions

1

## Which Sender Email Should the Leads Be Receiving Emails From?

The sender email a contact sees depends on (a) whether the email is manual or automated, and (b) whether the contact is assigned to a user. Use the priority table below as the canonical reference.

Email Type| Sender source| Unassigned Contact| Assigned Contact  
---|---|---|---  
Manual Emails| Logged-in user email| 1st priority| 1st priority  
Location email| N/A| N/A  
Assigned user email| N/A| N/A  
Agency email| N/A| N/A  
Automated Emails| Campaign / workflow settings| 1st priority| 1st priority  
Assigned user email| N/A| 2nd priority  
Location email| 2nd priority| 3rd priority  
Agency email| 3rd priority| 4th priority  
Review Request Emails| Always uses the **logged-in user email** as the sender.  
Appointment Confirmation Emails  
(Calendar Settings → 3. Confirmation)| Uses do-not-reply@replies.domain.com based on the Mailgun subdomain set up for the location, or the SMTP integrated email if one is connected.  
  
Not Sure About SMTP?

_Not sure how to connect your SMTP provider?_ [Follow these steps to set it up.](<https://help.gohighlevel.com/en/support/solutions/articles/48001059689>)

If you are using Mailgun or LC Email, the Business email is used as the sender if the lead is not assigned:

![Business email used as sender for unassigned leads when Mailgun or LC Email is active](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230234/original/LukUd53t-tjwMn_dHkUbmkoiyMFs0MVgSg.png?1758468487)

2

## How to Check If Contacts Are Assigned or Unassigned

Step 1

Search for the contact in the Smart Lists tab

Open **Contacts → Smart Lists** and locate the contact you want to check.

![Smart Lists search to locate a contact](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230430/original/xV9ahg5895S7bEOtO_x3vpeQJchyHcPkRw.png?1758468592)

Step 2

Open Conversations and view contact details

Open **Conversations** and click the icon on the right to view the contact's details panel.

![Open the contact details panel from Conversations](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230574/original/xeWmQjJoK1c1CDvcp3ouxStrSEb9_oFCPw.png?1758469037)

Step 3

Review the assigned user

In the details panel, check the **Assigned User** field. A populated value means the contact is assigned; a blank value means it's unassigned.

![Check the Assigned User field on the contact](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230590/original/WHLGxGLu_lgUbp8VMrPX7Qdu0N2sZvL4ng.png?1758469109)

Configuration Guide

Where to Configure the Sender Email

Five surfaces, one for each way your contacts receive email.

3

## Manual Email — The Conversation Tab

When you send a one-off email from the **Conversation** tab, the From address defaults to your logged-in user email:

![Conversation tab — From email defaults to the logged-in user email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230663/original/iOGx-LWFQvZQbd1jviS60WE9MGKlCVQPew.png?1758469162)

Two-Way Email Sync

If you have 2-way email sync configured, the From email will show your integrated email instead.

[Set up Two-Way Email Sync for Gmail](<https://help.gohighlevel.com/en/support/solutions/articles/48001235216>) · [Set up Two-Way Email Sync for Outlook](<https://help.gohighlevel.com/en/support/solutions/articles/48001229663>)

4

## Automated Email — Email Templates

Navigate to **Marketing → Emails → Templates → + New** to start a new template.

![Marketing > Emails > Templates > New template](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230722/original/mhcvjez4vv9dDOSLWqm1Mze-o6roXtuMnA.png?1758469252)

![Email template editor where the sender details are set](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230755/original/WfELc367egeqKtFKSioPk9xJheyU7_k2cw.png?1758469342)

5

## Automated Email — Bulk Action: Send Email

Step 1

Open Bulk Send Email

Go to **Contacts → Smart Lists** , select the contacts you want to email, then click **Send Email**.

![Smart Lists with contacts selected — click Send Email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230958/original/ChQW9qc8NCaqCoYr44PpauJrgatMH9al2Q.png?1758469438)

Step 2

Set the From Name and From Email

In the bulk-send dialog, fill in the **From Name** and **From Email**. These override the default sender for this send.

![From Name and From Email fields in the bulk send dialog](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054230965/original/xc9hiF8uAXelg45ZHErj1zHTKZwQtNzbZg.png?1758469471)

6

## Automated Email — Workflow Settings

Step 1

Open Workflows

Go to **Automation → Workflows** and click **Create Workflow**.

![Automation > Workflows > Create Workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054231022/original/nIi7qExg8bVqI6mUWWXejs12Dp5xBLFmGQ.png?1758469549)

Step 2

Start from scratch

Choose **Start from scratch** and click **Create new workflow**.

![Start from scratch and create a new workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054231079/original/yf8J13CKvWamnZ9W9o7HBUKnHzBk-fXmEA.png?1758469619)

Step 3

Configure the sender address

In the workflow builder, click **Settings → Configure Sender Address** to set the From details for every email this workflow sends.

![Workflow Settings — Configure Sender Address](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054231085/original/Et08a1v65mJKmkImQ3wZ9dD1byc63SKmcQ.png?1758469667)

7

## Automated Email — Workflow Send Email Action

Step 1

Add a Send Email action

Click the **+** button in your workflow and select **Send Email**.

![Add a Send Email action to the workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054231139/original/wV8WhjpkvQj_C9WDKCRPclPpO91043Halg.png?1758469707)

Step 2

Set From Name and From Email

Inside the action, fill in the **From Name** and **From Email**. These take precedence over the workflow-level sender address.

![From Name and From Email fields inside the Send Email action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054231144/original/PaXSJLcjoxA2QdrjoDIiKown142mVkbcYQ.png?1758469725)

8

## Frequently Asked Questions

Q: Why is the From email for Outlook always long and strange?

This is how Outlook displays sender information when the underlying envelope sender doesn't match the visible From address. If you send the same email to a Gmail address, the sender shows correctly. Learn how to [hide "sent by" information in Outlook](<https://stackoverflow.com/questions/35148098/hide-sent-by-information-in-outlook/35149628>).

![Outlook display showing 'sent by' on a sender](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48257301042/original/spc9PucOJ-wT0rT3Sf4IBvjR6JcaJn-1QQ.png?1666018222)

![Same email rendered in another mail client](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48257301207/original/D6asla-m-OdXThoGwKQTtT1P_GnYyRIpsg.png?1666018251)

Q: How do I remove the "via" information shown in Gmail?

Use a sender email domain that matches the Mailgun domain set up for the location. When the From domain doesn't match the SPF/DKIM-aligned sending domain, Gmail surfaces the "via" notice. Learn more about [extra info next to the sender's name](<https://support.google.com/mail/answer/1311182>).

Q: What happens if my workflow has both a Configure Sender Address and a Send Email action with its own From details?

The Send Email action's own From Name and From Email take precedence. The workflow-level Configure Sender Address acts as a fallback for any Send Email action that doesn't specify its own sender.

Q: My contact is unassigned and I'm running an automated campaign — which email gets used?

For unassigned contacts on an automated send, the priority is: Campaign / workflow settings → Location email → Agency email. The first non-empty value wins. If your workflow has a configured sender, that's what your contact sees.

Q: Can I use the assigned user's email as the From for manual emails?

Manual emails always use the logged-in user's email — that's the user actually typing the message. To make the assigned user the sender, ask them to log in and send the email themselves, or switch to an automated workflow where the assigned user email moves up the priority list.

Q: Why are Review Request emails always from the logged-in user, not the campaign sender?

Review Requests are deliberately sender-locked to the logged-in user so the recipient sees a personal, recognisable name from the team — review prompts perform measurably better with a known sender than with a brand alias.

Q: Where do appointment confirmation emails come from, and can I change the sender?

Appointment confirmation emails (configured under Calendar Settings → 3. Confirmation) use a system address based on the Mailgun subdomain set up for the location, or the SMTP integrated email if one is connected. If you need a different sender, connect an SMTP integration so it overrides the default.

Related Articles

[Setting Up SMTP Providers](<https://help.gohighlevel.com/en/support/solutions/articles/48001059689>) [Email Sending Guide: Best Practices & Email Warm Up](<https://help.gohighlevel.com/en/support/solutions/articles/155000001021>) [How to Set Up Two-Way Email Sync for Gmail](<https://help.gohighlevel.com/en/support/solutions/articles/48001235216>) [How to Set Up Two-Way Email Sync for Outlook](<https://help.gohighlevel.com/en/support/solutions/articles/48001229663>) [Using Custom Email Domains with Mailgun](<https://help.gohighlevel.com/en/support/solutions/articles/155000002561>) [SMTP Limitations When Emails Aren't Sending](<https://help.gohighlevel.com/en/support/solutions/articles/48001203144>)

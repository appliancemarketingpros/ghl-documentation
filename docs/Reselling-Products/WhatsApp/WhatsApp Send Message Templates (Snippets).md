# WhatsApp: Send Message Templates (Snippets)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003069-whatsapp-send-message-templates-snippets-](https://help.gohighlevel.com/support/solutions/articles/155000003069-whatsapp-send-message-templates-snippets-)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# Snippets & WhatsApp Template 

Send reusable Snippets, preview WhatsApp Templates before sending, and replace template media in one click

Table of Contents

  * • Overview
  * • Step 1 — Prepare the Snippet or Template
  * • Step 2 — Send a Snippet from Conversations
  * • Step 3 — Preview Templates at Send Time
  * • Step 4 — Replace Media in a Template
  * • Step 5 — Send via Workflows
  * • Step 6 — Bulk Actions
  * • Troubleshooting & Tips
  * • FAQs
  * • Related Articles


## Overview

Snippets are saved text or multimedia blocks you can insert into active WhatsApp conversations for faster, consistent replies. WhatsApp Templates (pre-approved messages) are separate and used to message contacts outside the 24-hour window.

**Recent updates:**

  * Templates can be **previewed at runtime** inside the conversation composer and Bulk Actions.
  * Template **category** and **language** are displayed during selection.
  * Template **media** can be **replaced in one click** from local files.
  * New UI experience may be available behind Labs.


    
    
    Note: To enable the updated features (if offered via Labs), go to Sub-account > Labs. This update for templates is expected to be available by default, but check Labs if you don't see the UI.

* * *

## Step-by-Step — Sending Snippets, Previewing Templates, and Replacing Media

### Step 1 — Prepare the Snippet or Template

1

Go to **Marketing > Templates (Snippets)**.

2

Click **Add Template (Snippet) > Add Text Template (Snippet)** to create a snippet, or edit an existing one.

3

Save the snippet with a clear name for quick selection.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064131720/original/ceZDjknikYyX69AvwtF8oT8kh_GvgRKZLQ.png?1770168661)

### Step 2 — Send a Snippet from Conversations

1

Go to **Conversations**.

2

Open an active WhatsApp conversation with the contact. There must be a message from the contact within the last 24 hours.

3

Ensure **WhatsApp** is selected as the channel.

4

Click **Insert Snippets** (or the snippets icon) in the composer.

5

Select the snippet you want; it will auto-populate the composer.

6

Edit the snippet text if necessary. You can use Custom Values or Trigger Links.

7

Click **Send**.

### Step 3 — Preview WhatsApp Templates at Send Time (Conversations & Bulk Actions)

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064131725/original/TGGfxxBq0qAMAsz_Q3DGMPnhGgzElrs-mw.png?1770168682)

1

In the message composer (Conversations) or Bulk Actions template selection, choose **WhatsApp Template** instead of free-form or snippet.

2

The UI displays an **instant preview** of the template content.

3

The preview shows **template category** (e.g., Marketing, Utility) and **language** next to the template name.

4

Confirm the template and proceed to send or schedule.
    
    
    Note: Previewing at runtime removes the need to open WhatsApp settings to confirm template content. Use the preview to verify category and language before sending.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064131758/original/hQHl5nPJRG8jv5tBJJKLT1OTxwe60nWe6w.png?1770168782)

### Step 4 — Replace Media in a WhatsApp Template (One-Click)

1

When a selected template includes media (image, document, or video), the composer shows the media placeholder and a **Replace media** option.

2

Click **Replace media**.

3

Choose a file from your local device; a file browser opens.

4

The selected media replaces the template media instantly in the composer preview.

5

Review the message and send.
    
    
    Note: This is available in Conversations and Bulk Actions where template selection occurs. Replacing media does not change the template itself in Meta/WhatsApp -- it swaps the media at send time for that message instance only.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064131831/original/okDZf39N8wkfQajbs28YJrIj0ME3JzoAdA.png?1770169177)

### Step 5 — Send Snippets or Templates via Workflows

1

Go to **Automation > Create Workflow** (or edit an existing workflow).

2

Add an initial trigger, then add the action **WhatsApp: Customer Service Window Check** to confirm the contact is within the 24-hour window.

3

Under the **Open** branch of the check, add a **WhatsApp** action.

4

Choose **WhatsApp Template** if you must use a template, or choose **None – Free form message** and insert snippet content programmatically.

5

If using a template, the workflow composer shows the template preview and allows media replacement similar to Conversations.

6

Save and publish the workflow.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064131873/original/PiyeF_OcVZKBV5AGBdT-UoddCqLnv2h4lw.png?1770169310)

### Step 6 — Bulk Actions: Send Templates and Replace Media

1

Go to **Contacts** (or wherever Bulk Actions are available) and select the contacts you want to message.

2

Choose **Bulk Action > Send WhatsApp** (or the platform's Bulk WhatsApp flow).

3

Select **WhatsApp Template** and use the runtime preview to verify category and language.

4

Use the **Replace media** control to swap local files if the template contains media.

5

Confirm and send the bulk operation.
    
    
    Note: Bulk Actions follow the same template preview and media-replacement experience as Conversations. Ensure recipients meet messaging rules such as opt-in and allowed content.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064131897/original/G6-Vtif6kGmeBjDIx5pViSPrpxF7Wu-ogQ.png?1770169397)

* * *

## Troubleshooting & Tips

  * If you do not see the template preview or replace-media options, try refreshing the conversation UI and confirm your account supports the updated experience.
  * If media replacement fails, verify the file type and size meet WhatsApp and platform limits.
  * Templates with strict placeholders may still require compliance with Meta's approved structure — replacing media does not bypass template formatting rules.


* * *

## FAQs

Q. What is a Snippet?

Snippets are pre-defined blocks of text or multimedia saved in the CRM that you can insert into active WhatsApp conversations for fast, consistent responses.

Q. What is the difference between Snippets and WhatsApp Templates?

WhatsApp Templates are pre-approved messages required to contact users outside the 24-hour window and must be approved by Meta/WhatsApp. Snippets are internal, editable canned responses used within the 24-hour window and do not require approval.

Q. Can I preview a WhatsApp template before sending?

Yes. Templates can now be previewed directly in the conversation composer and in Bulk Actions. The preview shows the message content along with the template's category and language.

Q. Can I replace the media inside a template at send time?

Yes. If a template includes media, you can click Replace media and upload a file from your local device. This is available in Conversations and Bulk Actions.

Q. Do Snippets work outside the 24-hour window?

No. Snippets can only be sent when the contact has an open 24-hour conversation window, meaning an inbound message within the last 24 hours. To message outside that window, use a pre-approved WhatsApp template.

Q. Does replacing media change the saved template?

No. Replacing media swaps the media for that send instance only. The stored template remains unchanged and still reflects the original approved content.

Q. Where do I enable the new UI features if I don't see them?

Check Sub-account > Labs for optional UI updates. If your account does not expose an option and you still don't see the behavior, contact Support for account-level verification.

* * *

## Related Articles

  * [WhatsApp Bulk Action](<https://help.gohighlevel.com/en/support/solutions/articles/155000001790>)
  * [WhatsApp FAQs](<https://help.gohighlevel.com/en/support/solutions/articles/155000002698>)

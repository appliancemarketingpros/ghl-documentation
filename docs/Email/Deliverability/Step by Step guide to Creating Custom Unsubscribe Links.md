# Step by Step guide to Creating Custom Unsubscribe Links

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001175857-step-by-step-guide-to-creating-custom-unsubscribe-links](https://help.gohighlevel.com/support/solutions/articles/48001175857-step-by-step-guide-to-creating-custom-unsubscribe-links)  
**Category:** Email  
**Folder:** Deliverability

---

Workflow Automation

Creating Custom Unsubscribe Links

Replace the default unsubscribe link with a branded landing page and a trigger-based DND workflow.

What You'll Learn

This guide walks you through replacing the platform's default unsubscribe link with a custom one that lands contacts on a branded page and automatically marks them DND for email.

You'll create a landing page, a Trigger Link, a workflow with the "Set Contact DND" action, and wire it all into your email footer — in five steps.

Table of Contents

1

Create a landing page for your unsubscribe message

2

Create a Trigger Link pointing to that landing page

3

Replace the default unsubscribe URL with the Trigger Link

4

Build a workflow: Trigger Link Clicked → Set Contact DND

5

Add the Trigger Link to your email footer

6

Frequently Asked Questions

Video Walkthrough

1

## Create a landing page with messaging you want contacts to see when they unsubscribe

Build a simple funnel or website page that confirms the unsubscribe, thanks the contact, or offers a preference-management option. This is the page contacts will land on after clicking your custom unsubscribe link.

Note

Copy the published URL of this page — you'll paste it into the Trigger Link in Step 2. Make sure the page is published and accessible before continuing.

![Example unsubscribe landing page in the funnel builder](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261125003/original/F6oF0Wn6O50_TnuFP9yd7RTkv0jjwCTIVw.png?1667490676)

2

## Use the landing page URL to create a Trigger Link

A Trigger Link is a trackable URL that fires platform events when clicked. You'll use it here so the system knows exactly when a contact clicks your unsubscribe link — and can act on it automatically via workflow.

![Trigger Link configuration screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261125458/original/sfQHzV3vpGXUkSnFDenKYz0p9O1LTYsncw.png?1667490774)

3

## Replace the default unsubscribe link URL with the Trigger Link

Navigate to **Marketing** → **Trigger Links** → **Add Link**.

![Marketing > Trigger Links > Add Link navigation path](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261126153/original/-VyZcKnG5SeCALDNpMx7NVP9lVRqyaegrw.png?1667490908)

Fill in the fields as follows, then click **Save** :

Field| Value  
---|---  
Name| Unsubscribe Link  
Link URL| Paste your funnel unsubscribe page URL here  
  
![Trigger Link save dialog with Name and URL fields filled in](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261126567/original/glGbKN7IqUol8z0F4hwbrCOQlohiSFRMlg.png?1667490990)

4

## Create a workflow: "Trigger Link Clicked" → "Set Contact DND"

This workflow listens for clicks on your unsubscribe Trigger Link and automatically marks the contact as DND for the Email channel.

Step 1

Create a new workflow from scratch

Go to **Automation** → **Create Workflow** , then choose **Start from Scratch** → **Create New Workflow**.

![Automation > Create Workflow button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261127134/original/Sv8p6-k-UA0_DO72blhz55stl_xIR6Yvqw.png?1667491133)

![Start from Scratch > Create New Workflow dialog](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261127183/original/87AS1sjlz186pBDk6WReW4644BjT4QHSqA.png?1667491149)

Step 2

Name the workflow and add the trigger

Set the workflow title to **Trigger Link Unsubscribe** , then click **Add New Workflow Trigger**.

Search for and select **Trigger Link Clicked**.

![Workflow builder with title set to Trigger Link Unsubscribe and Add New Workflow Trigger highlighted](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261128730/original/J3Pxd_nx2E5vpsS7YcoBNviqZEu_-CUHQw.png?1667491473)

![Trigger Link Clicked trigger selected in the search panel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261157897/original/yyB-KLZyTqKrqK3mOtkhHzmW22YQOsqLug.png?1667495978)

Step 3

Add a filter for your Unsubscribe Link

Click **Add Filters** and set **Trigger Link** to **Unsubscribe Link** (the Trigger Link you created in Step 3).

![Add Filters panel with Trigger Link set to Unsubscribe Link](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261156865/original/dS8hfoUWQxc3Hc4FMfZDulNz6f_wsSnqIQ.png?1667495917)

Step 4

Add the "Set Contact DND" action

Click the **+** to add your first workflow action. Search for and select **Set Contact DND**. In the dropdown, choose **Enable DND for Specific Channels** , select **Email** as the channel, then click **Save Actions**.

![Set Contact DND action panel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48189714739/original/ztd7nXaMuBE1r8Xs5jTPe061k_VTRRVLPQ.png?1644717318)

![Enable DND for Specific Channels dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261159180/original/Do6EgbFQRcl3V22HmpxAkY51JQP0nZ_Enw.png?1667496316)

![Email selected as the DND channel, Save Actions button visible](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261159739/original/P-JHrs4KKzM5tVSPfbNitaujaxEhrqtjaw.png?1667496364)

Step 5

Save and publish the workflow

Click **Save** and then toggle the workflow to **Published**. The workflow won't run until it is published.

![Workflow published toggle](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261160801/original/HDtrZZgv7Ow6sdHhHI0HFfu_F1wmPuHgsg.png?1667496408)

5

## Add the Trigger Link as the unsubscribe link in the email footer

Open your email template and locate the unsubscribe text in the footer. To wire up the Trigger Link:

Steps

1\. Highlight the word **here** (or whatever your unsubscribe anchor text is).

2\. Click the **Link** icon in the email editor toolbar.

![Email footer editor with 'here' highlighted and the link icon visible](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261161713/original/lmJVNd3TaGu8c2qv-0B1FvPDukoNajedmw.png?1667496519)

In the link dialog, select **Unsubscribe Link** from the **Link List** , then click **Save**.

![Link dialog with Unsubscribe Link selected from the Link List](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261161888/original/wkDOqjIjtErRzPhEirqGqo227Xl6DfvCjg.png?1667496574)

You're All Set

Anyone who clicks the unsubscribe link in your email will land on your branded page _and_ be automatically marked DND for the Email channel — no manual follow-up needed.

![Email footer showing the unsubscribe link wired to the Trigger Link](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261162112/original/ZafVcitYh6DrB5hC877AGDzZDGFBaIGlbA.png?1667496598)

6

## Frequently Asked Questions

Q: Do I still need the default unsubscribe link if I set up a custom one?

The Trigger Link replaces the role of the default unsubscribe URL in your email footer. However, some regulatory requirements (like CAN-SPAM) mandate a working unsubscribe mechanism in every commercial email, so always ensure your custom link is functional and that the workflow is published before sending.

Q: What happens if a contact clicks the link but the workflow isn't published?

The contact will still land on your unsubscribe landing page, but the "Set Contact DND" action won't fire. Their email DND status will not be updated. Always verify the workflow is in a **Published** state before sending campaigns.

Q: Can I mark contacts DND for channels other than Email?

Yes. In the **Set Contact DND** action, choose **Enable DND for Specific Channels** and select any combination of channels — SMS, calls, email, and more. You can add multiple DND actions in the same workflow if needed.

Q: Will contacts who already unsubscribed via the default link be affected?

No. The workflow only triggers for future clicks on the Trigger Link. Any contacts who previously unsubscribed through the default mechanism retain their existing DND status, which is separate.

Q: Can I use this same setup to add a tag or remove contacts from a list when they unsubscribe?

Absolutely. Within the same workflow, add extra actions after **Set Contact DND** — for example, **Add Tag** (e.g., "Unsubscribed") or **Remove from List**. This makes it easy to segment unsubscribed contacts for reporting or suppression lists.

Q: My landing page is on a custom domain — do I need any special setup?

Your funnel page must be published and accessible on the internet via a connected domain. If you haven't set up a domain yet, complete Domain Setup under **Settings → Domains** first, then publish the page and copy the URL before creating the Trigger Link.

Q: Can I use a different Trigger Link for different email campaigns?

Yes. Create multiple Trigger Links — one per campaign or list — each pointing to a different landing page if needed. In the workflow filter, specify the exact Trigger Link to scope the DND action to only contacts who clicked that specific link.

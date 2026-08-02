# Email Actions for Company & Custom Object Workflows

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008293-email-actions-for-company-custom-object-workflows](https://help.gohighlevel.com/support/solutions/articles/155000008293-email-actions-for-company-custom-object-workflows)  
**Category:** Marketing  
**Folder:** Others

---

Workflow Automation

# Send Email Action in Company & Custom Object Workflows

Send automated emails directly from Company and Custom Object workflows to associated contacts without creating additional Contact workflows.

What You'll Learn

This article explains how to use the Send Email action in Company and Custom Object workflows, allowing you to automate email communications to associated contacts based on company or custom object events.

You'll learn how to configure the Send Email action, select recipients using association labels, and manage email delivery for your automated communications.

Labs Feature

Send Email Action in Company & Custom Object Workflows is a Labs feature. Enable it in Settings > Labs before use. Labs features are in active development and may receive updates based on user feedback.

Table of Contents

1

What Is the Send Email Action?

2

Popular Use Cases

3

How to Set Up the Send Email Action

4

Frequently Asked Questions

1

## What Is the Send Email Action?

The Send Email action enables you to send automated emails directly from Company and Custom Object workflows in HighLevel. Previously, email actions were only available in Contact workflows, requiring you to create separate workflows or complex conversion steps to email contacts associated with companies or custom objects.

With this enhancement, you can automate email communication based on Company or Custom Object events without creating additional Contact workflows. When you add the Send Email action to a Company or Custom Object workflow, you select which associated contacts should receive the email using association labels and recipient selection options.

The system uses the relationships defined between your companies or custom objects and their associated contacts to deliver messages automatically when workflow triggers activate, streamlining your automation processes for non-contact record types.

2

## Popular Use Cases

Use the Send Email action to automate communications for various business scenarios:

**Customer onboarding** — Send welcome emails when a new Company or Custom Object record is created.

**Renewal reminders** — Automate reminders for contracts, subscriptions, or memberships approaching expiration.

**Project or deal updates** — Send status updates to associated stakeholders when project milestones are reached.

**Order or service notifications** — Trigger notifications based on Custom Object status changes, such as order fulfillment or service completion.

**Internal approvals** — Send approval requests to associated support representatives or team members.

**Follow-up emails** — Automate follow-ups when a Company or Custom Object reaches a specific stage in your business process.

3

## How to Set Up the Send Email Action

Follow these steps to configure the Send Email action in your Company or Custom Object workflows:

Step 1

Enable the Labs Feature

Navigate to Settings > Labs in your HighLevel account. Locate "Email Action in Company & Custom Object Workflows" and enable the feature.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077245088/original/zW0xIXt7qL2-7oGnzkEujxosvp6stktMlg.png?1785416058)

Step 2

Open Your Workflow

Create or open an existing Company or Custom Object workflow in the Automation section of your account.

Step 3

Add the Send Email Action

Click the + Add button in your workflow. In the Actions panel, locate the Communication section and select "Send email" from the available actions. You can also use the search bar to find it quickly by typing "Send email".

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077245335/original/aFQlf2w9cfxbghyNTCXvhsb_W2kudkpTow.png?1785416142)

Step 4

Configure Email Recipients

In the Email Recipients dropdown, select one of the following options under the Associations section:

  * **All associated contacts** — Sends to all contacts associated with the company or custom object
  * **Most recently associated contact** — Sends only to the most recently associated contact (Custom Object workflows only)
  * **Earliest associated contact** — Sends only to the earliest associated contact (Custom Object workflows only)


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077245534/original/sNetnWzLL6UejE84FaYgq7pum_otrDLa0Q.png?1785416185)

Step 5

Select Association Labels (Optional)

If you want to target specific types of associated contacts, use the Association Label field to select one or more association labels. This filters which contacts receive the email based on their relationship type. If you leave this field empty, the email sends based on your Email Recipients selection without filtering by association type.

Step 6

Configure Email Settings

Complete the email configuration fields:

  * **From Name** — Enter the sender name for the email
  * **From Email** — Enter the sender email address
  * **Subject** — Add your email subject line
  * **Cc/Bcc** — Add any Cc or Bcc recipients if needed


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077245636/original/qQ5R8EtbTeZa_Sv7iGfJwrLzOZOBH3a58A.png?1785416233)

Step 7

Create Your Email Content

Compose your email content using the email editor. You can include custom fields, personalization tokens, and formatting as needed. The editor supports the same features available in other workflow email actions.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077245680/original/I31f4om-cIJeBCTBxnMK5mRm0PjW3Ki6iw.png?1785416257)

Step 8

Save and Publish

Click "Save action" to save your email configuration, then publish your workflow to activate the automation. When the workflow is triggered, emails will automatically be sent to the selected associated contacts.

Important Notes

Emails are sent using the Bulk Email sending domain configured for your account.

This email will be delivered based on the account's timezone setting.

If the From Name and From Email fields are empty, the email will be sent using the default values configured in your account settings.

If a contact matches multiple selected association labels, they receive only one email. Recipient deduplication is handled automatically to prevent duplicate email sends.

4

## Frequently Asked Questions

Q: Do I need to enable this feature in Labs before using it?

Yes, this capability is currently a Labs feature. Navigate to Settings > Labs and enable "Email Action in Company & Custom Object Workflows" before the Send Email action appears in your Company and Custom Object workflows.

Q: Where do I find the Send Email action in the workflow builder?

After clicking the + Add button in your workflow, the Send Email action appears under the Communication section in the Actions panel. You can also search for "Send email" using the search bar to locate it quickly.

Q: What's the difference between "All associated contacts" and using Association Labels?

When you select "All associated contacts" in the Email Recipients dropdown without specifying an Association Label, the email sends to every contact associated with the company or custom object. If you specify labels in the Association Label field, the email only sends to contacts matching those specific relationship types, allowing you to target specific subsets of associated contacts.

Q: What happens if a contact matches multiple selected association labels?

If a contact matches multiple association labels you've selected, they receive only one email. The system automatically prevents duplicate emails to the same contact through recipient deduplication, even when they qualify through multiple association paths.

Q: Can I choose which associated contact receives the email in Custom Object workflows?

Yes, when configuring the Send Email action in Custom Object workflows, you can select whether to send to the earliest associated contact, most recently associated contact, or all associated contacts in the Email Recipients dropdown under the Associations section. This flexibility allows you to target the most relevant recipient based on your business process.

Q: Does the Send Email action work the same way in Company workflows as it does in Custom Object workflows?

The core functionality is similar—both use the Association Label field to identify recipient contacts. The main difference is that Custom Object workflows provide additional recipient selection options in the Email Recipients dropdown (earliest, most recent, or all associated contacts), while Company workflows default to sending to all associated contacts matching the selected labels.

Q: Can I use personalization tokens in these emails?

Yes, you can use custom fields and personalization tokens when composing your email content. The email editor supports the same personalization features available in other workflow email actions, including contact fields, custom object fields, and system tokens.

Q: What if there are no contacts associated with the selected labels when the workflow runs?

If no contacts match the selected Association Label when the Send Email action executes, no email is sent. The workflow continues to any subsequent actions without errors, allowing your automation to handle scenarios where associations may not yet exist.

Q: Which sending domain is used for these emails?

Emails sent from Company and Custom Object workflows use the Bulk Email sending domain configured for your account. Ensure your bulk email domain is properly configured and verified to ensure successful email delivery.

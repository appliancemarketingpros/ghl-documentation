# Email Verification Action in Workflow

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007749-email-verification-action-in-workflow](https://help.gohighlevel.com/support/solutions/articles/155000007749-email-verification-action-in-workflow)  
**Category:** Email  
**Folder:** General

---

Workflow Automation

# Email Verification in Workflows

Validate contact email addresses before sending — improve deliverability, reduce bounce rates, and protect your sender reputation.

What You'll Learn

The **Email Verification** action in Workflow ensures a contact's email address is valid before continuing with email-related actions. This guide walks through how it works, how to set it up, and how to branch your workflow based on the result.

Table of Contents

1

What Does Email Verification Do?

2

Prerequisites

3

Step-by-Step: Add the Email Verification Action

4

Using Email Verification Results in Conditions

5

Best Practice Recommendation

6

Summary

7

Frequently Asked Questions

Watch the Walkthrough

1

## What Does Email Verification Do?

When a contact reaches the **Email Verification** action in a workflow, the system checks whether the contact's email address is valid and safe to use for sending emails.

This helps prevent:

  * Sending emails to invalid addresses
  * High bounce rates
  * Poor sender reputation
  * Deliverability issues


2

## Prerequisites

Email Verification will run only if the following conditions are met:

Requirement 1

Email Verification is Enabled for the Sub-Account

The feature must be enabled for the specific sub-account before it can be used inside workflows.

Requirement 2

The Contact is Not Excluded from Verification

If the contact is excluded from verification, the Email Verification action will be skipped.

Setup Guide

Add the Email Verification Action

Follow these steps to add email verification to your workflow.

3

## Step-by-Step: Add the Email Verification Action

Email verification actions help you ensure that only valid email addresses progress through your workflow. This protects your sender reputation, reduces bounce rates, and makes your email campaigns more effective. Here's how to set up and use this feature.

Step 1

Open Your Workflow Builder

Click the **plus (+)** icon in your workflow builder to add a new action.

![Click the plus icon in workflow builder](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864158/original/g8JhUyM02XfHqR6Xua9zBKx9Ra7olH_q6A.png?1777020896)

Step 2

Search for Email Verification

Search for **Email Verification** in the action list and add it to your workflow.

![Search for Email Verification in the action list](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864161/original/KYIrOfw_xwHqWHt_FYPeRu2_DXYoCESitg.png?1777020896)

Step 3

Ensure Email Verification is Enabled

Make sure **Email Verification** is enabled for your sub-account. If it's not active, the action will be skipped.

![Enable Email Verification for your sub-account](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864156/original/JXOb6vBfscc1Gxq99R-46sgBB52-1_5qhg.png?1777020896)

Step 4

Confirm the Contact Isn't Excluded

Confirm that the contact you want to verify isn't excluded from email verification. Contacts can be excluded in their details, so make sure that's not the case for anyone you want checked.

![Confirm contact is not excluded from verification](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864173/original/QBjpHAHwDjzi1aVH6Tmy43UYMQgsKuB9PA.png?1777020896)

Step 5

Verification Runs When Contact Enters Workflow

When a contact is added to the workflow, the **Email Verification** action checks if the contact's email is valid. If so, the workflow continues to the next steps; if not, the process is skipped for that contact.

![Email Verification action running](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864176/original/2egazNT-JAbo_BTITG5iOBWO4eU7NNU5_Q.png?1777020896)

![Verification result displayed on workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864165/original/AMmxvfjUGtyTfyxbdBaCV5JiRdJ-VurcmA.png?1777020896)

Step 6

If Verification Fails, Next Steps Are Skipped

If email verification fails (for example, the email is invalid, excluded, or the feature is disabled), the workflow will skip over the next steps for that contact.

4

## Using Email Verification Results in Conditions

Branch your workflow based on whether an email is valid or not — this lets you send emails only to real contacts and take action for invalid ones.

Step 1

Add a Condition After Email Verification

Add a **Condition** action immediately after your Email Verification action.

![Add a Condition after email verification](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864167/original/vFa_cTF8fJviFDtqfzq3CvIpJS6I7RRlvQ.png?1777020896)

Step 2

Configure the "is verified" Condition

Use the **is verified** value from the email verification check as your condition. Set one branch for when it's **true** (valid) and another for when it's **false** (invalid).

![Select isEmailVerified condition field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864170/original/MVb5V3n5KWsZScum3J8z5t8_g613zHZftw.png?1777020896)

![Condition configuration true branch](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864177/original/z1gTDzLUR1SF-RycQbIg-qJo5b8OVIZ6mA.png?1777020896)

![Condition configuration false branch](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864164/original/HbWndr3i389hXav1PYBowy_QfLhVqbl0sw.png?1777020896)

Step 3

Set Up Actions on Each Branch

Set up actions on each branch. For example, send emails to valid contacts, and either mark or suppress contacts with invalid emails.

![Actions configured on true and false branches](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864172/original/q03YKuVhmw6zx2D82N_VdVuW5LJy7V5uvg.png?1777020896)

Step 4

Add Notes or Tracking Actions

Add notes or take other actions to track which contacts are valid or invalid during your testing.

![Add notes action to track valid contacts](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864169/original/Suw5LJvaIO7_sEn2gYptkhnanHnIaCnV0Q.png?1777020896)

![Tracking action for invalid contacts](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864171/original/4v6JoZ9qYvBeL_GroCLKTD6jvCru6dENnw.png?1777020896)

Step 5

Test with Valid and Invalid Contacts

Test your workflow with both valid and invalid contacts. Use the **Execution History** to confirm if emails were classified and processed correctly.

![Execution history of email verification](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864155/original/hLNnGdepCw8gVHnVSnBO5VfL1MYzs4bZXQ.png?1777020896)

![Execution history result - valid contact](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864174/original/ROwW9GIdnetCcyrgrrlzfVmaQZtdRzff2A.png?1777020896)

![Execution history result - invalid contact](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864179/original/x4XSfinfcGH6MHkhdzjGZ6UUNEeBH52Njg.png?1777020897)

![Execution history detail view](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069864178/original/v6ybFpN-qYTkbzVsXQvXhCsi5uoCQu6_Jg.png?1777020897)

Note

If a contact is on the excluded list for verification or if email verification is disabled at the sub-account level, those cases will also be handled automatically by the workflow logic.

5

## Best Practice Recommendation

A recommended workflow setup is:

Email Verification → Condition Check → Action Based on Result

Example:

**Verified (true)** → Send Email

**Not Verified (false)** → Mark as DND

Pro Tip

This creates a safer and more reliable email automation process that protects your sender reputation over time.

6

## Summary

The **Email Verification** action helps improve workflow efficiency by validating email addresses before sending emails.

By combining it with the **isEmailVerified** condition, you can create smarter workflows that:

  * Send emails only to valid contacts
  * Avoid unnecessary bounces
  * Protect sender reputation
  * Automatically handle invalid contacts


You're All Set

This ensures better deliverability and cleaner contact management across your sub-account.

7

## Frequently Asked Questions

Q: Does Email Verification cost extra?

Email Verification charges may apply depending on your plan and sub-account settings. Check with your agency admin or review your sub-account billing settings for exact charges per verification.

Q: What happens if Email Verification is disabled for my sub-account?

If the feature is disabled, the Email Verification action will be skipped in workflows and your contacts will proceed to the next action without being verified. Enable it in the sub-account settings to activate verification.

Q: Will already-verified contacts be re-verified every time?

Contacts that have been recently verified and are marked as excluded from verification will not be re-verified. This helps save verification credits and speeds up workflow execution.

Q: Can I use isEmailVerified inside an If/Else Condition branch?

Yes. Inside any Condition action, you can select the **isEmailVerified** field and branch your workflow based on whether the value is **true** or **false**.

Q: What does the verification actually check?

The verification checks syntax, domain validity, mailbox existence, and detects risky addresses like catch-alls, disposables, or known spam traps to determine if the email is safe to send to.

Q: Should I always add Mark as DND for invalid emails?

Marking invalid emails as DND is the recommended best practice because it prevents future email attempts and protects your sender reputation. You can also route invalid contacts to a cleanup list or tag them for review.

Q: Does Email Verification work on all workflow triggers?

Yes. The Email Verification action can be added to any workflow regardless of the trigger, as long as the contact has an email address on their record and the feature is enabled for the sub-account.

Q: Will this improve my email deliverability?

Yes. Removing invalid addresses from your send list lowers bounce rates, which is one of the biggest factors in sender reputation. Over time, this significantly improves inbox placement across major email providers.

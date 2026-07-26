# Auto-Enable Email DND When a Contact's Email Bounces

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008249-auto-enable-email-dnd-when-a-contact-s-email-bounces](https://help.gohighlevel.com/support/solutions/articles/155000008249-auto-enable-email-dnd-when-a-contact-s-email-bounces)  
**Category:** Email  
**Folder:** General

---

Workflow Automation

Auto-Enable Email DND When a Contact's Email Bounces

Use the Email Events trigger and the DND Contact action together to automatically stop sending to bounced addresses.

What You'll Learn

This article walks through a specific, ready-to-build workflow: whenever a contact's email **bounces** , the workflow automatically enables outbound Email DND (Do Not Disturb) for that contact, preventing further sends to a broken or invalid address.

You'll see how to configure the **Email Events** trigger with a "Bounced" filter, pair it with the **DND Contact** action scoped to Outbound + Email, and understand what this does (and doesn't) protect against.

Table of Contents

1

Why Enable DND on Bounce

2

Building the Workflow

3

Hard Bounces vs. Soft Bounces

4

Example Use Case

5

Frequently Asked Questions

1

## Why Enable DND on Bounce

Every time an email bounces, it signals that the address is unreachable, either permanently (invalid mailbox, closed domain) or temporarily (full inbox, server issue). Continuing to send to bounced addresses hurts your account in a few concrete ways:

  * **Sender reputation:** Repeated sends to invalid addresses raise your bounce rate, which email providers use as a spam signal.
  * **Deliverability:** A high bounce rate can get your sending domain throttled or blocklisted, affecting delivery to valid contacts too.
  * **Wasted sends:** Every automated email or campaign step sent to a dead address is a wasted send that never reaches anyone.
  * **Cleaner data:** Automatically flagging bounced contacts with DND keeps your list quality high without manual review.


2

## Building the Workflow

This workflow only needs two elements: an **Email Events** trigger filtered to "Bounced," and a **DND Contact** action scoped to Outbound Email. Here's how to set each one up.

Step 1

Create the workflow and add the Email Events trigger

From **Automation → Workflows** , create a new workflow (or open an existing one) and click **Add New Trigger**. Search for and select **Email Events** — this trigger fires on open, click, bounce, or reply events.

Step 2

Filter the trigger to "Bounced" events

Give the trigger a clear name (for example, **"Email Events"**), then under **Filters** , add a filter for **Event** and set it to **Bounced**. This restricts the workflow so it only runs when the email event type is a bounce — not an open, click, or reply.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076448577/original/-7gb22qUti-l_BSPNnBmzE5aKX-FYYFZQw.png?1784612252)

Step 3

Add the "Enable/disable DND" action

Click the **+** below the trigger and add the **DND Contact** action (labeled **Enable/disable DND** in the canvas). Name the action something descriptive, such as **"Enable/disable DND."**  
****

Step 4

Configure the direction, DND setting, and channel

Inside the action, configure the following fields:

  * **DND Direction:** Set to **Outbound** , since you're stopping messages sent to the contact, not messages coming from them.
  * **DND:** Set to **Enable DND for specific channels** , so only email is affected and other channels like SMS or calls remain unaffected.
  * **Channels:** Select **Email** from the channel picker.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076448622/original/ihn5L72ffSrN_GwAtg8H4Pb_VVW3sRH1iQ.png?1784612330)


Step 5

Save the trigger and action, then publish

Click **Save trigger** and **Save action** on each panel. Once the workflow reads Email Events (Bounced) → Enable/disable DND → End, toggle the workflow from **Draft** to **Publish** to activate it.

3

## Hard Bounces vs. Soft Bounces

Not every bounce means the address is permanently invalid, so it's worth understanding what happens to a contact once this workflow fires.

  * **Hard bounces** (invalid mailbox, non-existent domain) are automatically marked as **Invalid** and are the clearest case for enabling DND.
  * **Soft/generic bounces** (full inbox, temporary server error) are typically **temporary** conditions that may resolve on their own.


Note

Not all bounces mean an address is invalid. Hard bounces are automatically marked as Invalid, while soft/generic bounces are temporary. Adding this "Enable DND" action will block **all** bounced emails equally, and email validation won't automatically remove the DND flag later. If you want to distinguish hard from soft bounces, add an additional filter or a Condition step before the DND action, and plan for a manual or scheduled review process to lift DND from contacts whose addresses turn out to be reachable.

4

## Example Use Case

**Scenario:** A business sends a monthly email newsletter to its full contact list. A portion of addresses have gone stale over time — some mailboxes no longer exist. The business wants bounced addresses automatically suppressed from future sends without manually scrubbing the list every month.

Trigger Setup

**Trigger:** Email Events | **Filter:** Event Is Bounced

Workflow Action

DND Contact → Direction: Outbound → DND: Enable for specific channels → Channel: Email

Outcome

The moment an email bounces, that contact is automatically excluded from all future email sends while remaining reachable through SMS, calls, or other channels — keeping the newsletter list clean without manual maintenance.

5

## Frequently Asked Questions

Q: Will this workflow un-DND a contact if their email later becomes valid?

No. Enabling DND through this action does not get automatically reversed by email validation or a later successful send. If you want to re-enable email for a contact, you'll need a separate workflow or manual step using the "Disable DND" configuration of the same action.

Q: Does this affect SMS, calls, or other channels for the same contact?

No. Because the DND setting is scoped to "specific channels" with only Email selected, the contact remains reachable through SMS, phone calls, and any other channel. Only outbound email is blocked.

Q: What's the difference between Inbound and Outbound DND in this action?

Outbound DND controls whether you can send communications to a contact. Inbound DND controls whether incoming messages or calls from a contact are allowed. For bounce handling, you always want Outbound, since a bounce means your emails aren't reaching the contact, not the other way around.

Q: Can I distinguish between a single bounce and repeated bounces before enabling DND?

The Email Events trigger alone fires on every bounce event. To require multiple bounces before enabling DND, add a Condition step or a contact tag/counter that increments on each bounce, and only run the DND action once a threshold is met.

Q: Will contacts already mid-workflow in other campaigns still receive email after DND is enabled?

Once outbound Email DND is enabled, any email-sending step in any workflow will automatically skip that contact. Non-email steps in those workflows (SMS, tasks, tags) will continue to run normally.

Q: Should I add a tag in addition to enabling DND?

It's a good practice. Adding a tag like "Email Bounced" alongside the DND action makes it easy to filter, report on, and later review these contacts for manual re-verification or list cleanup.

Related Articles

[Workflow Trigger - Contact DND](<https://help.gohighlevel.com/support/solutions/articles/155000002673-workflow-trigger-contact-dnd>) [Workflow Action - DND Contact](<https://help.gohighlevel.com/support/solutions/articles/155000003270-workflow-action-dnd-contact>) [Workflow Trigger - Messaging Error Code - SMS](<https://help.gohighlevel.com/support/solutions/articles/155000003201-workflow-trigger-messaging-error-code-sms>) [How to Resubscribe After Unsubscribing from an Email List](<https://help.gohighlevel.com/support/solutions/articles/155000002948-how-to-resubscribe-after-unsubscribing-from-an-email-list>)

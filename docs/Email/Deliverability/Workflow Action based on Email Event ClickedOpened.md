# Workflow Action based on Email Event Clicked/Opened

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001208599-workflow-action-based-on-email-event-clicked-opened](https://help.gohighlevel.com/support/solutions/articles/48001208599-workflow-action-based-on-email-event-clicked-opened)  
**Category:** Email  
**Folder:** Deliverability

---

Workflows & Automation

# How To Add an Email Event Trigger (Clicked / Opened) to a Workflow

Trigger workflows the moment a contact opens or clicks an email. This guide walks through adding an Email Events trigger, filtering by event type, and using it to power smarter follow-ups.

Table of Contents

  1. 1 Video Walkthrough
  2. 2 Step-by-Step: Add the Email Event Trigger
  3. 3 Frequently Asked Questions


## Video Walkthrough

## Step-by-Step: Add the Email Event Trigger

Follow the five steps below to wire an **Email Events** trigger into any workflow so it fires on every **Open** or **Click**.

1

### Select the Initial Trigger and Search "Email"

Open your workflow, click **Add New Trigger** , and search **email** to surface the email-related trigger options.

![Search email in the workflow trigger picker](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029828492/original/bGpvJt4_kQ8_6QVOYFsGdEfwx6kXgkEOLQ.jpg?1721841822)

* * *

2

### Select Email Events from the Dropdown

Choose **Email Events** from the dropdown list — this is the trigger type that listens for opens, clicks, bounces, and other engagement signals.

![Select Email Events from the dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029828552/original/N-2L_Wb1zwfqKZdN2qGYmNwgvQkC3hN1Tg.jpg?1721841891)

* * *

3

### Click Add Filters

Click **Add Filters** to narrow down exactly which events you want the trigger to respond to.

![Click Add Filters](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029828580/original/EpAbf5v6gNamruGMSYT8aGfCODT3AslZeQ.jpg?1721841969)

* * *

4

### Pick Email Events → Event

From the filter options, select **Email Events** , then choose **Event** to expose the list of available event types.

![Select Email Events then Event](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029828646/original/t3i6XuxuPNGMGhJSuCpb_-Yuzwmrw0MLZg.jpg?1721842096)

* * *

5

### Choose Clicked or Opened

Pick the specific action you want the workflow to fire on:

Clicked Opened

![Choose Clicked or Opened](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029828702/original/66704TyO48ntssF31iLO2kcgyVrktX6CWg.jpg?1721842180)

Your new trigger is now live in your workflow!

Any contact who performs the selected email event will be enrolled into this workflow automatically.

Note on Tracking

For accurate tracking and a strong sender reputation, make sure **Open and Click events are enabled** for your sending domain. These events provide the engagement data that mailbox providers use to determine deliverability.

## Frequently Asked Questions

Q: What's the difference between the Clicked and Opened events?

**Opened** fires when a recipient loads the tracking pixel in your email. **Clicked** fires when a recipient clicks any tracked link. Clicks are a stronger engagement signal than opens since they require deliberate action.

Q: Can I target an Email Event trigger to a specific campaign or workflow?

Yes. After adding the Event filter, layer additional filters like **Campaign Name** or **Source** so the trigger only fires for opens/clicks on the sends you care about.

Q: Why isn't my Email Event trigger firing?

The most common cause is that **Open and Click tracking is disabled** on your sending domain. Check your email service settings and re-enable tracking. Also confirm the workflow is **published** and the filter matches the actual event type and source name.

Q: Will bot-generated opens or clicks trigger my workflow?

If **Bot Detection Prevention** is enabled in your Business Profile, bot-driven opens and clicks are filtered out and will not trigger the workflow — keeping your automations honest.

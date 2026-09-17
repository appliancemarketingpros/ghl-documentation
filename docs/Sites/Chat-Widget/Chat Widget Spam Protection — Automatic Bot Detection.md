# Chat Widget Spam Protection — Automatic Bot Detection

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008686-chat-widget-spam-protection-automatic-bot-detection](https://help.gohighlevel.com/support/solutions/articles/155000008686-chat-widget-spam-protection-automatic-bot-detection)  
**Category:** Sites  
**Folder:** Chat Widget

---

Chat Widget

# Chat Widget Spam Protection

Automatically detect and tag spam and bot submissions from your chat widget forms — without adding CAPTCHA or delaying genuine visitors.

What You'll Learn

Chat widget forms can receive high volumes of fake or bot-generated submissions that waste messaging spend and damage your sender reputation. Spam Protection automatically flags suspicious leads, pauses outbound messaging on those contacts, and tags them for review — all without disrupting the experience for legitimate visitors.

This guide explains how the feature works, how to enable it for your chat widgets, and how to review flagged leads so you retain control over which contacts are genuine.

Table of Contents

1

What is Chat Widget Spam Protection?

2

Key Benefits

3

Protection Options

4

How to Enable Spam Protection

5

Reviewing Flagged Leads

6

Managing Legitimate Surges

7

Frequently Asked Questions

1

## What is Chat Widget Spam Protection?

Chat Widget Spam Protection automatically detects and tags submissions that exhibit patterns consistent with bot or spam behavior. When a lead is flagged as suspicious, HighLevel pauses outbound messaging on the channels you choose — preventing wasted SMS credits and protecting your email sender reputation — while still creating the contact record and tagging it for your review.

The feature operates server-side without adding CAPTCHA, extra form fields, or visible delays. Legitimate visitors experience no change to the chat widget form.

Suspicious leads arrive in your contacts list tagged with **chat_widget_high_volume_flag**. You retain full control: review the flagged contacts, restore genuine leads with a single click, and delete confirmed spam.

2

## Key Benefits

Spam Protection delivers automatic bot detection without disrupting your conversion funnel or discarding leads you may need to review.

**Zero Visitor Friction** — No CAPTCHA, no extra form fields, and no added wait time. Genuine visitors see the same fast, simple chat widget experience as before.

**Suspicious Leads Are Kept** — Flagged contacts are created and tagged rather than deleted, so borderline judgments never cost you real business. You make the final call.

**Sender Reputation Protected** — No outbound messages are sent to flagged leads on paused channels. Your account stops accumulating bounces that degrade delivery of genuine campaigns.

**Per-Widget Control** — Configure protection independently on each chat widget. Choose from four options: Tag only, Pause SMS, Pause Email, or Pause Both.

**Precise and Reversible** — Only the channels you select are paused. Calls, inbound messages, and all other DND settings remain untouched. Restore a contact in one click.

**Clear Audit Trail** — The activity log shows "DnD enabled by chat widget spam protection" and names the paused channel, so you always know why a message was not sent.

3

## Protection Options

You can configure how Spam Protection handles flagged leads by choosing one of four options. Select the level of protection that matches your needs and risk tolerance.

Option 1

Tag Only

Flagged leads are tagged with **chat_widget_high_volume_flag** but messaging is not paused. Use this if you want visibility into suspicious submissions without blocking outbound communication.

Option 2

Pause SMS

Flagged leads are tagged and SMS messaging is paused. Email remains enabled. Ideal for protecting SMS spend while allowing email follow-ups.

Option 3

Pause Email

Flagged leads are tagged and email messaging is paused. SMS remains enabled. Use this to protect email sender reputation while allowing SMS outreach.

Option 4

Pause Both

Flagged leads are tagged and both SMS and email messaging are paused. This is the default setting for new chat widgets and provides the most comprehensive protection.

Note

Calls, inbound messaging, and other DND settings are never affected by Spam Protection. Only the outbound channels you select are paused on flagged contacts.

4

## How to Enable Spam Protection

Spam Protection is configured per chat widget. Follow these steps to enable it on an existing widget or verify the default setting on a new one.

Step 1

Navigate to Sites → Chat Widget

Open the chat widget builder by selecting the widget you want to configure.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080611354/original/kHVBwLAhBBGXgANtjrNy15cyAHoCYMBEPg.jpeg?1789047621)

Step 2

Open the Spam Protection Panel

In the builder sidebar, locate and expand the **Spam Protection** section.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080611691/original/OcuEUZJ3cJBr5zIQC3ZG9RKZI2UAkPv8rQ.png?1789047763)

  


Step 3

Toggle Protection On

Enable the Spam Protection toggle. Existing widgets default to OFF; new widgets default to ON.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080611793/original/9xn1sJioGlrjNVlBOs2Acw073pdroOUQmw.png?1789047800)

Step 4

Choose the Protection Level

Select one of the four options.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080611841/original/dJbtYj-SB3p4WVU9T-PIqe9QNEI1IIfB2A.png?1789047841)

Step 5

Save the Widget

Click **Save** to apply your changes. Protection is active immediately for submissions received after saving.

Default Behavior

New chat widgets created in the builder have Spam Protection enabled by default with **Pause Both** selected. Existing widgets remain OFF until you manually enable them.

5

## Reviewing Flagged Leads

Flagged contacts appear in your contacts list with the tag **chat_widget_high_volume_flag**. Review them periodically to identify genuine leads that were flagged by mistake and restore messaging permissions.

Step 1

Filter by Tag

Go to **Contacts** and filter on the tag **chat_widget_high_volume_flag** to view all flagged submissions.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080613182/original/Qw6YfBfVDBeUxfdRZbRYttb3nGVa5akbhw.png?1789048352)

Step 2

Review Contact Details

Open each contact to inspect the submission. Check the activity log for the entry **"DnD enabled by chat widget spam protection"** to confirm which channels were paused.

Step 3

Restore Genuine Leads

If a contact is legitimate, manually remove the DND setting for the paused channel(s) and remove the **chat_widget_high_volume_flag** tag. Outbound messaging resumes immediately.

Step 4

Delete Confirmed Spam

Bulk-select confirmed spam contacts and delete them. This clears your contact list and prevents accidental outreach to invalid addresses.

Tip

Schedule regular reviews of flagged contacts — weekly or after campaigns — to ensure you restore genuine leads before they become stale.

6

## Managing Legitimate Surges

Legitimate spikes in chat widget submissions — caused by product launches, paid ad campaigns, events, or press coverage — can resemble spam waves from an automated detection standpoint. During these periods, temporarily disable Spam Protection to avoid tagging genuine leads.

Follow these steps to pause and resume protection around high-volume events:

Step 1

Disable Protection Before the Event

Navigate to **Sites → Chat Widget** , open the widget, and toggle Spam Protection OFF before your campaign or event begins.

Step 2

Re-enable Protection After the Surge

Once the event concludes and submission volume normalizes, toggle Spam Protection back ON and restore your protection settings.

Note

If you forget to disable protection during a legitimate surge, review the flagged contacts after the event and restore any genuine leads that were paused.

7

## Frequently Asked Questions

Q: Does Spam Protection add CAPTCHA or extra fields to my chat widget?

No. Spam Protection operates server-side and does not modify the visitor-facing form. Legitimate users experience no change — no CAPTCHA, no extra steps, and no visible delay.

Q: Are flagged leads deleted automatically?

No. Flagged contacts are created in your account and tagged with **chat_widget_high_volume_flag**. Outbound messaging on the selected channels is paused, but the lead remains available for you to review and restore if legitimate.

Q: Can I restore a flagged contact if it's genuine?

Yes. Open the contact record, remove the DND setting for the paused channel(s), and delete the **chat_widget_high_volume_flag** tag. Outbound messaging resumes immediately.

Q: Does Spam Protection affect existing leads or workflows?

No. Spam Protection only applies to new submissions received after it is enabled. Existing contacts and active workflows are unaffected. The feature defaults to OFF on all existing chat widgets, so you must manually enable it.

Q: What happens to inbound calls and messages from flagged contacts?

Nothing. Spam Protection only pauses outbound messaging on the channels you select (SMS and/or email). Inbound calls, text replies, and all other contact interactions function normally.

Q: How do I know which channel was paused on a flagged contact?

Open the contact record and check the activity log. You will see an entry that reads **"DnD enabled by chat widget spam protection"** and specifies the paused channel (SMS, email, or both).

Q: Will Spam Protection affect my form conversion rate?

No. Because the feature operates server-side and adds no visible friction, it does not impact the visitor experience. Legitimate users complete the form exactly as they did before protection was enabled.

Q: Can I use Spam Protection on multiple chat widgets?

Yes. Protection is configured independently on each chat widget. You can enable it on some widgets and leave it off on others, or apply different protection levels (Tag only, Pause SMS, Pause Email, Pause Both) to each widget based on its purpose.

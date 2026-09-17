# Ringless Voicemail/Voicemail Drops Setup Guide

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981430-ringless-voicemail-voicemail-drops-setup-guide](https://help.gohighlevel.com/support/solutions/articles/48000981430-ringless-voicemail-voicemail-drops-setup-guide)  
**Category:** Phone System  
**Folder:** Calling

---

Workflow Automation

# Ringless Voicemail Setup Guide for Workflows

Deliver pre-recorded voicemail messages through automated workflows without requiring live conversations

What You'll Learn

Ringless Voicemail, also called Voicemail Drop, lets you deliver a pre-recorded voicemail to a contact through a workflow without requiring a live conversation. It can be used for follow-ups, appointment reminders, lead nurturing, and re-engagement when the contact has provided the required consent.

This guide explains the prerequisites, setup process, delivery behavior, testing steps, and common troubleshooting scenarios.

Table of Contents

1

What is Ringless Voicemail?

2

How Ringless Voicemail Works

3

Key Benefits

4

Prerequisites

5

How to Set Up Ringless Voicemail

6

Testing Your Voicemail Drop Workflow

7

Troubleshooting Ringless Voicemail

8

Understanding Voicemail Sending Limits

9

Related Articles

10

Frequently Asked Questions

1

## What is Ringless Voicemail?

Ringless Voicemail is a workflow action that delivers a pre-recorded audio message directly to a contact's voicemail without triggering a traditional phone call. The contact's phone does not ring, and no live conversation is required. This makes it useful for automated follow-ups, appointment reminders, lead nurturing campaigns, and re-engagement workflows where you have obtained the required consent.

The feature is also referred to as Voicemail Drop and is configured as an action within HighLevel workflows.

Ringless Voicemail vs. Standard Voicemail

Ringless Voicemail is an outbound workflow action that delivers a pre-recorded message to a contact. Company and User Voicemail are inbound call-routing features used when callers reach voicemail after dialing your HighLevel number.

2

## How Ringless Voicemail Works

Ringless Voicemail uses an automated calling sequence designed to route a pre-recorded message to the recipient's voicemail without requiring a live conversation. Understanding this behavior helps explain why delivery can vary by carrier, device, and voicemail configuration.

**Call Sequence** — The system initiates one call to the recipient's number, then places a second call shortly afterward. The second call is routed to voicemail, where the pre-recorded message is deposited.

**Carrier-Dependent Delivery** — Success depends on the recipient's carrier, network configuration, and voicemail system. Not all carriers or devices process the call sequence in the same way.

**No Guaranteed Delivery** — Because delivery relies on carrier and device behavior, Ringless Voicemail is not guaranteed to reach every recipient. Always test your workflow before deploying it to a larger audience.

For a detailed technical explanation, see [Voicemail Drop: How It Works and Why It Matters](<https://help.gohighlevel.com/support/solutions/articles/voicemail-drop-how-it-works>).

Important

Ringless Voicemail delivery is not guaranteed. Delivery can vary based on the recipient's carrier, device, voicemail configuration, network behavior, and other provider-level factors. Always test your workflow before using it with a larger audience.

3

## Key Benefits

Ringless Voicemail offers several advantages for automated communication workflows when used with appropriate consent and compliance measures.

**Non-Intrusive Delivery** — The contact's phone does not ring, reducing interruption while still delivering your message.

**Scalable Automation** — Voicemail Drops can be sent to multiple contacts through a single workflow without requiring manual dialing.

**Consistent Messaging** — Pre-recorded audio ensures every contact receives the same message with the same tone and information.

**Time-Saving Follow-Ups** — Ringless Voicemail is useful for appointment reminders, lead nurturing, and re-engagement campaigns where live conversations are not required.

Use Case| Example  
---|---  
Appointment Reminders| Send a pre-recorded reminder 24 hours before a scheduled appointment.  
Lead Nurturing| Deliver a follow-up message to leads who have requested information.  
Event Notifications| Notify registered attendees about upcoming webinars or events.  
Consented Lead Re-Engagement| Re-engage contacts who have the required consent for prerecorded or automated calling.  
  
4

## Prerequisites

Before setting up a Ringless Voicemail workflow, confirm that you have the following:

  * An active LC Phone or connected Twilio number in the sub-account.
  * A pre-recorded MP3 or WAV file prepared at 64 kbps.
  * Required consent for prerecorded or automated calls.
  * A workflow trigger that identifies when the voicemail should be sent.
  * A valid phone number on the contact record.
  * A test contact for validating the workflow before publishing.


For guidance on creating and formatting audio files, see [Create an Audio File for Voicemail and Voicemail Drops](<https://help.gohighlevel.com/support/solutions/articles/create-an-audio-file-for-voicemail>).

Important

Ringless Voicemail may be subject to federal, state, provincial, carrier, and industry-specific rules governing prerecorded or automated calls. Obtain the required consent before sending and confirm that your use case complies with applicable regulations.

5

## How to Set Up Ringless Voicemail

Follow these steps to add a Ringless Voicemail action to a workflow. This example assumes you have already created a workflow and are ready to add the Voicemail action.

Step 1

Navigate to the Workflow

Go to **Automation → Workflows** and open the workflow where you want to add the Voicemail action.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080039422/original/Oh2pHu51FqxrTVqwTu7Xn2edzjrAgOQ-NQ.jpeg?1788451372)

Step 2

Add the Voicemail Action

Click the **+** button where you want to insert the action, select **Voicemail** from the action list, and click **Done**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080039489/original/a4yL3r3gJTb9MPNKefJ-DWYPZ1Y4EGxF5w.png?1788451417)

Step 3

Configure the Action Name (Optional)

In the **Action Name** field, enter a descriptive label for internal reference. This name appears in the workflow builder and helps you identify the action's purpose.

Step 4

Upload or Select the Audio File

Click **Add Attachments** to upload a new file, or select an existing recording from the dropdown menu.

Confirm that the file is in MP3 or WAV format and exported at 64 kbps.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080041180/original/ADDz0X8hp0NQS8prgIfQOMaY_VvGslIexQ.png?1788452221)

[Screenshot: Voicemail action panel with Add New Recording button and dropdown menu]

Step 5

Assign the Contact to a User (Optional)

Assigning the contact to a user is optional and can help associate the contact with a specific team member before the voicemail is sent. Use this only when contact ownership is part of your workflow logic.

Leave this field blank if user assignment is not needed.

Step 6

Save the Action

Click **Save** to add the Voicemail action to your workflow.

6

## Testing Your Voicemail Drop Workflow

Before publishing the workflow for real contacts, run it with a test contact and confirm that the expected behavior occurs.

  * The correct voicemail file is used.
  * The audio plays clearly.
  * The workflow triggers at the expected time.
  * The message reaches voicemail as expected.


If the test does not succeed, see the [Troubleshooting Ringless Voicemail ](<https://help.gohighlevel.com/en/support/solutions/articles/48000981430>)section.

7

## Troubleshooting Ringless Voicemail

Delivery problems can come from the audio file, contact phone number, workflow configuration, carrier behavior, or voicemail availability. Check the basics before changing the workflow or contacting Support.

  * Confirm the contact has a valid phone number.
  * Confirm the workflow actually enrolled the contact.
  * Confirm the Voicemail action was reached.
  * Confirm the uploaded file is MP3 or WAV at 64 kbps.
  * Re-upload or re-export the audio if playback fails.
  * Test the workflow with another contact or phone number.
  * Confirm the destination has voicemail enabled.
  * Check whether the account has reached its voicemail-drop limit.


8

## Understanding Voicemail Sending Limits

Voicemail Drop sending limits may increase as the account establishes usage history. If you reach the current limit or need additional capacity, contact HighLevel Support.

These limits are subject to change and may vary based on account activity and carrier requirements.

9

## Related Articles

  * [Create an Audio File for Voicemail and Voicemail Drops](<https://help.gohighlevel.com/en/support/solutions/articles/48000981433>)
  * [Voicemail Drop: How It Works and Why It Matters](<https://help.gohighlevel.com/en/support/solutions/articles/155000006808>)
  * [Workflow Action - Voicemail](<https://help.gohighlevel.com/en/support/solutions/articles/155000003275>)
  * [Voicemail For Company And For Users](<https://help.gohighlevel.com/en/support/solutions/articles/48001146671>)
  * [Overview of Phone Number Configuration Options](<https://help.gohighlevel.com/en/support/solutions/articles/48001229976>)


10

## Frequently Asked Questions

Q: Do I need consent before sending Ringless Voicemail?

Yes. You should obtain the level of consent required for your use case and jurisdiction before sending prerecorded or automated voicemail messages. Requirements can vary based on message purpose and location.

Q: What audio file format should I use?

Use MP3 or WAV format. Export or convert the file at 64 kbps for best compatibility. If the file does not play correctly, re-export it at 64 kbps, upload it again, save the workflow action, and test it with a test contact. For detailed guidance, see [Create an Audio File for Voicemail and Voicemail Drops](<https://help.gohighlevel.com/support/solutions/articles/create-an-audio-file-for-voicemail>).

Q: Why is my voicemail not being delivered?

Delivery can fail due to carrier behavior, device configuration, or voicemail availability. Confirm that the contact has a valid phone number, the workflow enrolled the contact, the Voicemail action was reached, and the audio file is correctly formatted. Test with another contact or number to isolate the issue.

Q: Can I see when a voicemail was delivered?

You can view when the Voicemail action was triggered in the workflow history. However, because Ringless Voicemail relies on carrier-level behavior, delivery confirmation is not always available or guaranteed.

Q: Do I need additional registration or verification before sending Ringless Voicemail?

Ringless Voicemail does not use the same registration process as A2P SMS messaging. However, prerecorded-call and telemarketing requirements can vary by location and use case. Confirm that you have the required consent and meet any applicable legal or industry requirements before sending.

Q: How many Ringless Voicemails can I send per day?

Sending limits may increase as the account establishes usage history. If you reach the current limit or need additional capacity, contact HighLevel Support. Limits are subject to change and may vary based on account activity and carrier requirements.

Q: Can I use Ringless Voicemail for cold outreach?

Ringless Voicemail should only be used for contacts who have provided the required consent for prerecorded or automated calls. Confirm that your use case complies with applicable regulations before sending.

Q: What is the difference between Ringless Voicemail and standard voicemail?

Ringless Voicemail is an outbound workflow action that delivers a pre-recorded message to a contact. Company and User Voicemail are inbound call-routing features used when callers reach voicemail after dialing your HighLevel number. For more information, see [Voicemail For Company And For Users](<https://help.gohighlevel.com/support/solutions/articles/voicemail-for-company-and-users>).

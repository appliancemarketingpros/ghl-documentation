# Troubleshooting SMS Delivery

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981696-troubleshooting-sms-delivery](https://help.gohighlevel.com/support/solutions/articles/48000981696-troubleshooting-sms-delivery)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Troubleshooting

Why Are My SMS Messages Not Delivering?

A complete guide to diagnosing and fixing SMS delivery failures — from the platform layer all the way to the carrier network.

What You'll Learn

It's frustrating when a text never arrives — whether it's an appointment reminder, a promotion, or a two-way chat. This guide walks you through each step of our delivery pipeline, shows you where things can go wrong, and gives you clear, actionable fixes so you can get back on track fast.

Table of Contents

1

How Message Delivery Works

2

Where to Find Error Messages

3

Common Reasons Why Messages Fail (And How to Fix Them)

4

Super-Quick Checklist Before You Click "Send"

5

Frequently Asked Questions

6

Related Articles

1

## How Message Delivery Works

When you send a message from the platform, it travels through multiple layers. If the message fails at any layer, it may not be delivered to the end user.

![Diagram showing SMS delivery pipeline layers](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155047990043/original/rtRKVPSokDhZTTns4Bqu6AbZhQHdt-PEfA.jpeg?1749549338)

The three layers a message passes through before reaching the recipient.

Let's look at how to spot issues at each layer and fix them.

2

## Where to Find Error Messages

If your message didn't go through, check the **Conversations View**. In most cases, when a message fails to send or deliver, an error badge is displayed in the conversation view like this:

![Screenshot of error message displayed in Conversations View](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155052685143/original/yYUXlUZ2Nin4ZumnCdX6gbB9zHgw972n0g.jpeg?1756470598)

Error badge displayed inside the Conversations View.

The error message and error code will provide you with clues about what is going wrong and how to proceed from there.

3

## Common Reasons Why Messages Fail (And How to Fix Them)

Layer 1

At the Platform Layer

Issue| Cause| Fix (Help Docs)  
---|---|---  
Contact has DND (Do Not Disturb) enabled| When DND is enabled for a contact on the message channel or overall, the platform doesn't send the message and displays an error in the conversation screen.| Remove DND status from the contact to resume message sending.  
  
➡️ [DoNotDisturb DND](<https://help.gohighlevel.com/support/solutions/articles/48001214849>)  
The Number Is a Landline| When number validation is enabled, the system checks if a number is message-capable (i.e., not a landline). If not, it prevents the message from being sent.| Use a mobile number instead or disable number validation if necessary.  
  
➡️ [Number Intelligence](<https://help.gohighlevel.com/en/support/solutions/articles/48001153968>)  
Sub-Account is New and Undergoing Ramped Sending| The platform restricts message volume for new sub-accounts to prevent spam, gradually increasing limits over time.| Wait for limits to increase automatically, or have the agency request a lift.  
  
➡️ [LC Phone Messaging Policy (Ramp-Up Model section)](<https://help.gohighlevel.com/en/support/solutions/articles/48001213941>)  
Sub-Account Has Hit Its Daily Message Limit| Each sub-account has a daily message limit set by the agency. Bulk and automated messages stop sending once this limit is hit, but individual replies can still be sent. Agencies have control over these limits for each sub-account.| Adjust daily limits from the agency settings, or wait until the next day.  
  
➡️ [LC Phone Messaging Policy](<https://help.gohighlevel.com/en/support/solutions/articles/48001213941>)  
Sub-Account Sending Suspended Due to High Errors, Opt-Outs, or Complaints| Sub-accounts exceeding spam, opt-out, or carrier complaint thresholds have message sending suspended. Attempts to send messages during suspension will be skipped and display an error.| Follow deliverability best practices and contact support if needed.  
  
➡️ [Best Practices for Deliverability](<https://help.gohighlevel.com/support/solutions/articles/155000000079>)  
  
Layer 2

At the Twilio / LC Phone Layer

Error| Cause| Fix  
---|---|---  
Number is on Twilio's DND list| The number is on Twilio's DND list due to a previous opt-out or carrier complaint. Messages will fail unless the contact opts back in.| The contact must text **"START"** to the same Twilio number to re-enable messaging.  
30001: Queue Overflow| Messages are queued based on the sender's or account's rate. If they stay in the queue for over 4 hours, they fail.| Reduce the Validity Period in Messaging Service settings or API requests to shorten queue time.  
30002: Suspended Sub-Account| The message fails if the Twilio sub-account is suspended between queuing and sending.| Contact Twilio or platform Support to resolve the suspension.  
  
Layer 3

At the Sender Carrier Network Layer

Error| Cause| Fix  
---|---|---  
30003: Unreachable Destination Handset| The recipient's phone may be off, have no signal, be a landline, or there may be a mobile carrier issue.| Retry later or verify the number is a mobile line and properly reachable.  
30004: Message Blocked| Possible reasons include: the destination number is blocked, the device has insufficient signal or cannot receive messages (e.g., landline), the number is on India's Do Not Call registry, there's a mobile carrier issue, or a US/CA toll-free number was sent to a handset that previously opted out.| Ensure the number is valid and opted in. Avoid sending to DND or blocked numbers.  
Attachment File Too Large| The file size exceeds carrier limits for MMS.| ➡️ [File Size Limits for Attachments in SMS](<https://help.gohighlevel.com/support/solutions/articles/48001208913>)  
International Geo Permissions| Your account might not have permission to send international messages.| Contact support to enable international messaging permissions.  
Message Body Too Long| If you are using a trigger to send a message, check the body of the message — especially if it contains the custom value **{{message.body}}**. For example, if someone replies via email and their email exceeds the limit of 1,600 characters, the message will fail to send.  
  
![Screenshot showing message body too long error](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155047990631/original/PvnlWbqLsSDvP46SqUbwxdC7wgjSuYDhkQ.png?1749549640)| Trim the message manually or modify the trigger logic to exclude large custom values.  
  
Tip

To learn more about error codes and troubleshooting, refer to the [Twilio Error and Warning Dictionary](<https://www.twilio.com/docs/api/errors>).

4

## Super-Quick Checklist Before You Click "Send"

**1\. Check Conversations** — Note any red error badge displayed next to the message.

**2\. Match Error Code** — Use the tables in Section 3 above to find the cause for that specific error.

**3\. Apply Fix** — Follow the "Fix" column for that issue and take the recommended action.

**4\. Retry** — Resend the message after making the necessary adjustments.

**5\. Monitor** — Confirm delivery or note a new error code for the next round of troubleshooting.

5

## Frequently Asked Questions

Q: Why am I getting charged for failed messages?

Charges apply once a message is **attempted** — even if it fails later in the delivery process. The cost is incurred at the point of submission to the carrier, not at confirmed delivery.

Q: How do I know exactly why a message failed?

You can check the message logs in Twilio for a full breakdown of what happened at the carrier level.  
  
➡️ [How to check Twilio logs](<https://help.gohighlevel.com/en/support/solutions/articles/48001222601>)

Q: What's the difference between a "failed" and an "undelivered" message?

**Failed** means the message was never submitted to the carrier (it was blocked at the platform or Twilio layer before sending). **Undelivered** means the message was submitted to the carrier but could not be delivered to the recipient's handset — typically a Layer 3 issue such as the phone being off or the number being unreachable.

Q: How do I prevent my sub-account from being suspended?

Maintain low error rates, opt-out rates, and spam complaint rates. Follow messaging best practices — only send to opted-in contacts, keep message content relevant, and honor unsubscribe requests immediately.  
  
➡️ [Best Practices for SMS Deliverability](<https://help.gohighlevel.com/support/solutions/articles/155000000079>)

Q: The contact says they didn't receive my message, but no error shows in the conversation view — why?

If the conversation view shows the message as "sent" with no error, the message was successfully submitted to the carrier. At that point, delivery is outside the platform's control. The issue is likely on the carrier or device side — the phone may have been off, have no signal, or the carrier may have silently filtered the message. Check Twilio logs for the final delivery status.

Q: Does DND block two-way conversations too?

Yes. If DND is enabled at the channel level or globally for a contact, outbound messages from the platform — including replies in active conversations — will be blocked and display an error. You must remove the DND flag from the contact before any outbound message can be sent.

Q: How long does the ramp-up period last for new sub-accounts?

Ramp-up timelines vary based on account activity and sending behavior. Limits increase automatically as the system establishes a positive sending history. If you need limits increased faster, your agency can request a lift. See the LC Phone Messaging Policy for details on the ramp-up model.  
  
➡️ [LC Phone Messaging Policy](<https://help.gohighlevel.com/en/support/solutions/articles/48001213941>)

Q: Can I resend a failed message automatically via a workflow?

Not automatically — the platform does not retry failed messages on its own. However, you can build a workflow that checks for delivery errors and triggers a follow-up action (such as sending via a different channel or alerting your team) based on message status. Resolve the root cause first before resending to avoid repeated failures.

Related Articles

[Best Practices for SMS Deliverability and Avoiding SMS Restrictions](<https://help.gohighlevel.com/en/support/solutions/articles/155000000079>) [LC - Phone Messaging Policy](<https://help.gohighlevel.com/en/support/solutions/articles/48001213941>) [SMS / Phone Number Validation](<https://help.gohighlevel.com/en/support/solutions/articles/48001153968>)

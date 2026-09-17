# Why Calls or Messages May Appear Incorrectly in Conversations

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001184861-why-calls-or-messages-may-appear-incorrectly-in-conversations](https://help.gohighlevel.com/support/solutions/articles/48001184861-why-calls-or-messages-may-appear-incorrectly-in-conversations)  
**Category:** Phone System  
**Folder:** Messaging

---

Conversations Troubleshooting

# Why Calls or Messages May Appear Incorrectly in Conversations

Understanding why anonymous callers, group text replies, and integration-triggered messages sometimes display unexpectedly in HighLevel.

What You'll Learn

Conversations can sometimes appear incorrect when caller identity, group message support, or third-party integrations affect how calls and messages are routed. This article explains three common scenarios that may look like a Conversations issue but are caused by expected platform or carrier behavior.

Use the examples below to identify the source before escalating to Support.

Table of Contents

1

What Can Cause Conversations to Appear Incorrect?

2

Anonymous Callers Appearing Under the Same Number

3

International Group Text Replies Appearing as Separate Conversations

4

Check the Message Source Before Escalating

5

When to Contact Support

6

Related Articles

7

Frequently Asked Questions

1

## What Can Cause Conversations to Appear Incorrect?

Conversations relies on caller or sender identity and source information provided by carriers, messaging providers, and connected integrations. When that information is missing, limited, or routed differently, calls and messages can appear grouped, split, or unexpected even when the underlying activity is being processed as designed.

The three most common scenarios involve anonymous caller IDs grouping multiple unrelated callers together, international group text replies splitting into separate threads, and messages triggered by third-party integrations that appear without user action.

  


Watch it here, <https://www.loom.com/share/3d4bfc5cc51c4712b63acec9bc5c3d89>.

2

## Anonymous Callers Appearing Under the Same Number

When multiple people call with anonymous or blocked caller IDs, their calls may all appear under a single placeholder number in Conversations. This happens because the carrier does not provide distinct caller information, so HighLevel groups all anonymous calls under the same generic identifier.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079936172/original/VYnnP3fzGDuHBK3IOwNOiduCRNwbyZMwdg.png?1788363815)  


Note

The exact placeholder number can vary depending on the carrier or provider. Common examples include generic numbers like +266696687 or similar system-generated identifiers.

Why This Happens

When multiple anonymous calls arrive with the same placeholder caller ID, HighLevel may associate them with the same contact or conversation because the incoming calls do not contain distinct caller numbers. This is expected carrier behavior when caller ID is hidden or unavailable.

What You Can Do

Anonymous caller IDs cannot be "unmasked" by HighLevel or the carrier. If you need to differentiate between callers, ask them to disable anonymous calling on their device or carrier settings before calling again.

3

## International Group Text Replies Appearing as Separate Conversations

When you send a group text and recipients reply, their responses may appear in separate conversation threads instead of staying grouped together. This typically happens when using international numbers, toll-free numbers, or short codes that do not support group messaging.

Group Texting Support

Group Texting is supported for eligible +1 long code numbers in the US and Canada. Toll-free numbers, short codes, and international numbers are not supported for group texting through this workflow.

Why This Happens

When group texting is not supported for your number type, the messaging provider treats each reply as an individual one-to-one message rather than part of a group thread. This causes replies to appear in separate conversations in HighLevel.

What You Can Do

Use a US or Canada +1 long code number for group texting workflows. If you need to send messages to multiple recipients using a toll-free or international number, consider using broadcast messaging instead, where replies are expected to appear as individual conversations.

4

## Check the Message Source Before Escalating

Sometimes messages appear unexpectedly in Conversations not because of a platform issue, but because they were triggered by a connected integration, custom messaging provider, or Marketplace app. Before reporting a message as erroneous, check the Message Details to confirm the source.

Step 1

Open Message Details

Click on the message in Conversations and select **Message Details** from the context menu or information panel.

Step 2

Review the Source Field

Look for the source identifier, which may show a Marketplace app name, custom integration, workflow automation, or messaging provider. If the message was sent by an integration rather than a user or automation you recognize, this explains the unexpected activity.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079936335/original/HoHU7qL1WyH3X50OpCPS66Fr_TBeLltkcg.png?1788363861)

Troubleshooting Tip

If the message source shows an unexpected integration, review your connected apps and workflow automations to determine whether the message was triggered intentionally. This can help you distinguish between a platform issue and expected integration behavior.

5

## When to Contact Support

If you have confirmed that the issue is not caused by anonymous caller IDs, unsupported group texting, or integration-triggered messages, and the behavior persists, escalate to Support with the following information. Providing complete examples helps Support distinguish between a carrier limitation, integration source, or platform issue more quickly.

What to Include When Contacting Support

**Contact Name or Phone Number** — Identify the specific contact or conversation where the issue appears.

**Exact Timestamp** — Provide the date and time (including timezone) when the unexpected behavior occurred.

**Channel Involved** — Specify whether the issue affects calls, SMS, email, or another communication channel.

**Single or Multiple Contacts** — Indicate whether the issue affects one contact or multiple contacts to help identify patterns.

**Screenshots** — Include screenshots of the Conversations view and Message Details modal showing the unexpected behavior.

**Message Details Source** — Copy the source information from the Message Details modal if available.

**Reproducibility** — Note whether the issue happens consistently or intermittently, and whether it can be reproduced with specific steps.

6

## Related Articles

  * [Troubleshooting SMS Delivery Issues](<https://help.gohighlevel.com/en/support/solutions/articles/48001208912>)
  * [Understanding Caller ID and Inbound Calls](<https://help.gohighlevel.com/en/support/solutions/articles/155000005438>)
  * [Managing Connected Integrations and Marketplace Apps](<https://help.gohighlevel.com/en/support/solutions/articles/155000005791>)


7

## Frequently Asked Questions

Q: Why are incoming calls from different people all showing the same number?

When callers have anonymous or blocked caller IDs enabled, their calls may all appear under the same placeholder number because the carrier does not provide distinct caller information. This is expected behavior when caller ID is hidden or unavailable.

Q: Does the same placeholder number always mean the callers are the same person?

No. When caller ID is hidden or unavailable, multiple unrelated callers may appear under the same placeholder number because their actual numbers were not provided. Each call may be from a different person.

Q: Why are replies showing up in separate conversations instead of the group thread?

Group texting is only supported for US and Canada +1 long code numbers. If you send a group text from a toll-free, short code, or international number, replies will appear in separate conversations because the messaging provider treats each reply as an individual message.

Q: Does this issue affect SMS as well as calls?

The scenarios described in this article primarily affect calls (anonymous caller IDs) and group SMS (unsupported number types). Individual SMS messages are not typically affected by anonymous sender behavior, but integration-triggered messages can appear in any channel including SMS.

Q: How do I confirm a message came from an integration and not a genuine issue?

Click on the message in Conversations and select **Message Details**. The source field shows whether the message was triggered by a Marketplace app, custom integration, workflow automation, or messaging provider. If the source matches an integration you have connected, the message is expected behavior.

Q: What should I include when contacting Support about Conversations issues?

Provide the contact name or phone number, exact timestamp (with timezone), channel involved, whether the issue affects one or multiple contacts, screenshots of the Conversations view and Message Details, the message source if available, and whether the issue can be reproduced consistently.

Q: Does group texting work with toll-free or international numbers?

No. Group texting is only supported for +1 long code numbers in the US and Canada. Toll-free numbers, short codes, and international numbers cannot participate in group texting workflows. Replies from recipients will appear as separate one-to-one conversations when using unsupported number types.

Q: Can anonymous caller IDs be unmasked or identified?

No. When a caller blocks their caller ID or the carrier does not provide the number, HighLevel cannot retrieve the actual phone number. To identify callers, ask them to disable anonymous calling on their device or carrier settings before calling again.

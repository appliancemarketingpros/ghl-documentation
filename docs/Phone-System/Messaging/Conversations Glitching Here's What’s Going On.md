# Conversations Glitching? Here's What’s Going On?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001184861-conversations-glitching-here-s-what-s-going-on-](https://help.gohighlevel.com/support/solutions/articles/48001184861-conversations-glitching-here-s-what-s-going-on-)  
**Category:** Phone System  
**Folder:** Messaging

---

Conversations Troubleshooting

Conversations Are Glitching

Why different callers can share one number, and why group replies split into separate threads.

Overview

Are your calls and messages acting weird in the platform? Maybe you're seeing different people showing up under the same number — or replies scattered across separate conversations?

Don't worry — you're not alone, and this quick guide will help you pinpoint what's happening.

Table of Contents

1

Scenario 1: Same Number, Different Callers

2

Check the Message Source Before Escalating

3

Scenario 2: Replies Splitting into Separate Conversations

4

Wrap-Up

5

Frequently Asked Questions

Video Walkthrough

1

## Scenario 1: Same Number, Different Callers

What You'll See

Incoming calls from different people all showing the same number (e.g., +266696687).

### What's Happening

  1. Leads sometimes call anonymously, meaning their caller ID is hidden or not traceable.
  2. Instead of showing their actual phone number, the system logs these calls under a generic or placeholder number (e.g., +266696687).
  3. As a result, all anonymous calls using this placeholder number get grouped together.
  4. This causes multiple leads' calls to merge into a single contact or conversation in the system, making it difficult to distinguish between them.


![Multiple anonymous calls grouped under one placeholder number](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048047118/original/um1zeDCwO3GujkVLnoEOQMKoguUdqWlnvw.png?1749621896)

### Why This Matters

Because the platform identifies contacts based on phone number, all anonymous calls get grouped under the same contact. That's why conversations are merging or stacking incorrectly.

Can We Retrieve the Actual Caller ID?

You cannot "unmask" an anonymous call. If the caller's carrier/VoIP provider does not send a caller ID, the platform cannot retrieve or display it.

Support doc: [Why am I getting calls from these strange numbers?](<https://help.twilio.com/articles/223179988-Why-am-I-getting-calls-from-these-strange-numbers->)

2

## Check the Message Source Before Escalating

If a message appears to have been sent unexpectedly, review the message details in Conversations before escalating the issue. Messages sent through a Marketplace App or custom provider can include source information that helps identify which integration triggered the message.

This can help you confirm whether the message came from an installed app, a custom provider, or another connected source.

![Message Details modal showing the message source](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073370023/original/IK05ZMrlivZYXJawtgXIANgsUvC8zi6TVg.png?1781097425)

Message Details modal showing the source integration

3

## Scenario 2: Replies Splitting into Separate Conversations

What You'll See

Replies in separate conversations, instead of one shared group thread.

### What's Happening

"We now support Group Texting, but it's important to note that this feature is only available for +1 (US/Canada) long code numbers. Toll-free numbers and short codes can't participate in group texts through Twilio."

  1. This issue usually happens when your Twilio number is included in a group text or conversation involving contacts outside the US or Canada.
  2. Currently, the system does **not** support Group Texting or Group SMS for international numbers.
  3. Because of this limitation, replies from each participant in the group are routed into **separate, individual conversation threads** instead of staying within one group thread.
  4. Although it may look like a system error, this is actually **expected behavior** based on the current functionality restrictions for group messaging outside of the US and Canada.


4

## Wrap-Up

Conversation glitches — such as calls from multiple people showing under the same number, or replies splitting into separate threads — are usually caused by anonymized caller IDs, formatting inconsistencies, or multi-channel interactions.

Still Stuck?

If issues continue, don't hesitate to contact Support with detailed examples — our team is here to help resolve these edge cases quickly.

5

## Frequently Asked Questions

Q: Why are replies showing up in separate conversations?

The system doesn't yet support Group Texting or Group SMS for countries outside of the US/Canada. Because of this limitation, replies from each participant get routed into separate, individual conversation threads.

Q: Why are incoming calls from different people all showing the same number (e.g., +266696687)?

This issue occurs when leads call anonymously, meaning their carrier or VoIP provider doesn't send a traceable caller ID. Instead, all these anonymous calls get grouped under a placeholder number like +266696687. Multiple leads calling anonymously will merge into the same conversation.

Q: Does this issue affect SMS as well as calls?

The anonymous-caller-ID grouping is specific to voice calls. The separate-conversation issue is specific to group SMS/texting outside the US and Canada. They're two distinct behaviors, both tied to how caller/sender identity is passed through to the system.

Q: Will international group texting be supported in the future?

This is currently a platform-wide restriction tied to how group texting is supported through Twilio for +1 (US/Canada) long code numbers. If that changes, it will be announced separately — for now, treat individual threads as expected behavior for international group conversations.

Q: How do I confirm a message came from an integration and not a genuine glitch?

Open the message in Conversations and check its Message Details modal. Messages sent through a Marketplace App or custom provider include source information showing which integration triggered the send.

Q: What should I include when contacting Support about a conversation glitch?

Include the contact or number involved, timestamps of the affected calls or messages, and screenshots of the conversation thread. Detailed examples help the team diagnose edge cases much faster.

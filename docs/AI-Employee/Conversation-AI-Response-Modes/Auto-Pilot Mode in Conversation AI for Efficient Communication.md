# Auto-Pilot Mode in Conversation AI for Efficient Communication

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008094-auto-pilot-mode-in-conversation-ai-for-efficient-communication](https://help.gohighlevel.com/support/solutions/articles/155000008094-auto-pilot-mode-in-conversation-ai-for-efficient-communication)  
**Category:** AI Employee  
**Folder:** Conversation AI - Response Modes

---

Conversation AI

# Auto-Pilot Mode in Conversation AI

Let your AI bot handle conversations autonomously with extended 100-message capacity and smart sleep controls

What You'll Learn

Auto-Pilot Mode enables Conversation AI bots to manage customer conversations independently, now supporting up to 100 messages per thread—4x the previous limit.

This guide covers how Auto-Pilot works, when bots go to sleep, and how to optimize the new message limit for longer, more complex dialogues without manual intervention.

Table of Contents

1

What is Auto-Pilot Mode?

2

The New 100-Message Limit

3

How Auto-Pilot Handles Message Limits

4

Enabling and Configuring Auto-Pilot

5

When Bots Go to Sleep

6

Waking a Sleeping Bot

7

Best Practices for Message Limits

8

Frequently Asked Questions

1

## What is Auto-Pilot Mode?

Auto-Pilot Mode allows Conversation AI bots to operate independently without requiring human oversight for every interaction. When enabled, the bot handles incoming messages across all connected channels—SMS, Facebook Messenger, Instagram, WhatsApp, and more—until it reaches its configured message limit or encounters a condition that requires escalation.

This mode is ideal for high-volume use cases like lead qualification, appointment scheduling, FAQ handling, and basic troubleshooting where the bot can resolve most inquiries without intervention.

Key Benefit

With the new 100-message limit, Auto-Pilot bots can now support 4x longer conversations than before, reducing the need for manual intervention and enabling more complex multi-step workflows.

2

## The New 100-Message Limit

HighLevel recently increased the maximum number of messages a bot can send in a single conversation from 25 to **100 messages**. This enhancement allows Auto-Pilot bots to handle significantly longer dialogues without requiring manual reactivation.

Why This Matters

Previously, over 5,000 contacts hit the 25-message cap every day, causing conversations to stall mid-flow. The new 100-message ceiling eliminates this bottleneck for the vast majority of use cases.

### What Counts Toward the Limit

Only bot-generated messages increment the counter. The following do **not** count:

**Human Agent Messages** — Replies from team members in the Conversations inbox

**Workflow Messages** — Automated messages sent via workflows or campaigns

**Inbound Contact Messages** — Messages received from the contact

3

## How Auto-Pilot Handles Message Limits

When a bot operating in Auto-Pilot Mode reaches its configured message limit (anywhere from 1 to 100 messages), it automatically goes to sleep for that conversation. This prevents runaway loops and gives you control over when automation should pause.

### Sleep Behavior

Once the bot reaches its limit:

Step 1

Bot Sends Final Message

The bot delivers its last allowed reply (message #25, #50, #100, or whatever limit you set).

Step 2

Bot Goes Dormant

The bot stops responding to new messages in that conversation thread until manually or programmatically reactivated.

Step 3

Conversation Remains Open

The conversation stays in your inbox. Human agents can still reply, and workflows can still trigger—but the bot will not generate new messages.

Note

The bot does not automatically send a "goodbye" message when hitting the limit. If you want contacts to know the bot is pausing, include that instruction in your bot's prompt or use a workflow fallback.

4

## Enabling and Configuring Auto-Pilot

Auto-Pilot Mode is enabled by default for all Conversation AI bots. The key configuration is setting the appropriate message limit for your use case.

Step 1

Navigate to Bot Settings

Go to **Sub-Account** → **Conversation AI** → **Bots** , then select the bot you want to configure.

Step 2

Set Maximum Message Limit

In **Bot Settings** , locate **Maximum messages a Bot can send in a Conversation**. Enter a value between 1 and 100 (default is 100 for new bots).

Step 3

Save Changes

Click **Save**. The new limit applies immediately to all new conversations; existing conversations retain their current counter but will use the new limit going forward.

5

## When Bots Go to Sleep

A bot in Auto-Pilot Mode will go to sleep in two scenarios:

Scenario 1

Message Limit Reached

The bot has sent the maximum number of messages you configured (1–100) in the current conversation thread.

Scenario 2

Manual or Workflow Pause

A human agent or workflow action explicitly put the bot to sleep using the "Update Conversation AI Bot and Status" action.

Tip

Monitor conversations that consistently hit the 100-message limit. If you see this pattern, consider raising the limit further or reviewing your bot's prompt to make responses more concise.

6

## Waking a Sleeping Bot

When a bot goes to sleep after hitting its message limit, you have two options to reactivate it and reset the message counter to zero.

### Manual Reactivation

Open the conversation in the **Conversations** inbox and mark it as **Read**. This immediately wakes the bot and resets the counter, allowing it to send up to 100 more messages (or whatever your configured limit is).

### Workflow Reactivation

Use the **Update Conversation AI Bot and Status** workflow action to programmatically wake the bot. This is useful for automated scenarios like:

**Time-Based Resume** — Re-engage the bot after 24 hours if the contact sends a new message

**Keyword Trigger** — Wake the bot only when the contact says "I need help" or similar phrases

**Tag-Based Logic** — Reactivate if the contact is tagged with "VIP" or "High Priority"

Pro Tip

Create a workflow trigger on "Conversation Status = Bot Sleeping" to automatically route high-value conversations to a human agent instead of reactivating the bot.

7

## Best Practices for Message Limits

Choosing the right message limit balances automation with quality. Here are recommended ranges based on conversation complexity:

Use Case| Recommended Limit  
---|---  
Quick FAQs, Lead Capture| 10–25 messages  
Appointment Scheduling, Simple Troubleshooting| 26–60 messages  
In-Depth Product Guidance, Multi-Step Forms| 61–100 messages  
  
### Monitoring and Adjustment

Review conversation transcripts weekly. If most chats end well before the limit, consider lowering it to keep metrics tidy and reduce unnecessary AI usage costs. If many conversations hit the cap, raise it or refine your bot's prompt to be more concise.

Cost Consideration

Every AI-generated message counts toward your Conversation AI usage quota. Raising the limit from 25 to 100 can increase costs if conversations routinely use the full range. Monitor your billing dashboard after making changes.

8

## Frequently Asked Questions

Q: Does the 100-message limit apply to my existing bots?

Yes. All Prompt-based and Form-based bots automatically inherit the new 100-message ceiling. You can lower the limit in Bot Settings if your use case requires shorter conversations.

Q: Can I set different message limits for different channels?

No. The Maximum Message Limit is set at the bot level and applies uniformly across SMS, Facebook, Instagram, WhatsApp, and all other enabled channels.

Q: What happens if a contact keeps messaging after the bot sleeps?

The bot remains dormant and does not respond. The conversation stays open in your inbox, and you can either manually mark it as Read to reactivate the bot or have a human agent take over.

Q: Does resetting the counter start it from zero?

Yes. When you mark a conversation as Read or use the workflow action to reactivate the bot, the message counter resets to zero, giving the bot another full cycle (up to 100 messages or your configured limit).

Q: Can I use Auto-Pilot with hybrid human-bot conversations?

Yes. Human agents can jump into any Auto-Pilot conversation at any time. Their messages do not count toward the bot's limit. The bot will continue responding (up to its limit) unless you manually put it to sleep or it reaches the cap.

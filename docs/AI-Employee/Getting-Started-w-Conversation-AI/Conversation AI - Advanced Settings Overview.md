# Conversation AI - Advanced Settings Overview

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004415-conversation-ai-advanced-settings-overview](https://help.gohighlevel.com/support/solutions/articles/155000004415-conversation-ai-advanced-settings-overview)  
**Category:** AI Employee  
**Folder:** Getting Started w/ Conversation AI

---

Conversation AI

# Advanced Settings Overview – Conversation AI

Master every configuration option to fine-tune how your AI bots engage contacts across channels

What You'll Learn

This article covers the advanced settings that control Conversation AI bot behavior, including the new 100-message limit, response timing, channel preferences, and safety controls.

Configure these settings to balance automation with human oversight and deliver the right customer experience at scale.

Table of Contents

1

Accessing Advanced Settings

2

Maximum Message Limit (1–100)

3

Response Delay Settings

4

Channel-Specific Controls

5

Safety and Fallback Options

6

Resetting the Message Counter

7

Frequently Asked Questions

1

## Accessing Advanced Settings

Every Conversation AI bot—whether Prompt-based or Form-based—has a dedicated Settings panel where you control message limits, response timing, and channel behavior.

Step 1

Navigate to Your Bots

Go to **Sub-Account** → **Conversation AI** → **Bots**.

Step 2

Open Bot Settings

Click the bot you want to configure, then select **Bot Settings** from the navigation.

Step 3

Adjust and Save

Modify any field below, then click **Save** at the bottom of the panel.

2

## Maximum Message Limit (1–100)

The **Maximum messages a Bot can send in a Conversation** field caps how many replies your bot may send in a single thread before going to sleep. HighLevel recently raised this ceiling from 25 to **100 messages** , allowing bots to handle longer, more complex dialogues without manual intervention.

Why This Matters

Previously, over 5,000 contacts hit the 25-message cap every day, causing conversations to stall. The new 100-message limit reduces manual escalations and keeps customer journeys flowing smoothly.

### How It Works

Once the bot sends its maximum number of messages in a conversation, it automatically goes dormant. Only bot-generated messages count toward the limit—human agent replies, workflow messages, and inbound contact messages do not increment the counter.

Conversation Type| Recommended Limit  
---|---  
Quick FAQs, Lead Capture| 10–25 messages  
Appointment Scheduling, Simple Troubleshooting| 26–60 messages  
In-Depth Guidance, Multi-Step Forms| 61–100 messages  
  
Note

Raising the limit can increase Conversation AI usage costs. Every bot-generated message counts toward your plan's AI generation quota, so monitor usage after adjusting this setting.

### Setting the Limit

In the **Bot Settings** panel, locate the **Maximum messages a Bot can send in a Conversation** field. Enter any value from **1 to 100** (the default for new bots is 100). Click **Save** to apply the change immediately to all active conversations.

3

## Response Delay Settings

Control how quickly your bot replies to create a more natural conversation pace. Add artificial delays to simulate human typing behavior or keep responses instant for high-volume support queues.

Option

Minimum Response Delay

Set a floor (in seconds) before the bot can reply. Use 2–5 seconds to mimic human reading time.

Option

Maximum Response Delay

Cap the longest delay (in seconds). Prevents frustration if the bot takes too long to respond.

4

## Channel-Specific Controls

Enable or disable your bot on individual channels (SMS, Facebook Messenger, Instagram, WhatsApp, etc.). The Maximum Message Limit applies uniformly across all enabled channels—you cannot set different limits per channel.

Tip

If certain channels require shorter conversations, create a separate bot with a lower message limit and assign it only to those channels.

5

## Safety and Fallback Options

Configure guardrails to protect contacts from repetitive loops or off-brand responses. These settings work alongside the message limit to ensure quality interactions.

Setting

Fallback Message

Displayed when the bot cannot generate a confident reply or when it hits the message limit.

Setting

Content Filters

Block specific words or phrases to prevent the bot from discussing sensitive topics.

Setting

Auto-Escalation

Automatically assign conversations to a human agent after the bot hits its limit or detects frustration.

6

## Resetting the Message Counter

When a bot hits its maximum message limit, it goes to sleep. You can wake it manually or via workflow to resume the conversation.

### Manual Reset

In the **Conversations** inbox, open the sleeping bot conversation and mark it as **Read**. This resets the counter to zero and reactivates the bot immediately.

### Workflow-Based Reset

Use the **Update Conversation AI Bot and Status** workflow action to programmatically wake the bot. Pair this with conditions (e.g., "contact replied with keyword") to resume automation only when appropriate.

Pro Tip

Set a workflow trigger on "Conversation Status = Bot Sleeping" to automatically re-engage the bot after 24 hours if the contact sends a new message.

7

## Frequently Asked Questions

Q: Does the 100-message limit apply to my existing bots?

Yes. All Prompt-based and Form-based bots automatically inherit the new 100-message ceiling. You can lower the limit if your use case requires shorter conversations.

Q: Can I set different limits for different channels?

No. The Maximum Message Limit is set at the bot level and applies uniformly across SMS, Facebook, Instagram, WhatsApp, and all other enabled channels.

Q: Will raising the limit increase my costs?

Potentially. Every AI-generated message counts toward your Conversation AI usage quota. Monitor your billing dashboard after increasing the limit to track any changes in consumption.

Q: Do human agent messages count toward the limit?

No. Only bot-generated messages increment the counter. Messages from human agents, workflows, or inbound contact messages do not count.

Q: What happens when the bot hits the limit mid-conversation?

The bot goes to sleep immediately after sending its final allowed message. You can reactivate it manually (mark as Read) or via the "Update Conversation AI Bot and Status" workflow action.

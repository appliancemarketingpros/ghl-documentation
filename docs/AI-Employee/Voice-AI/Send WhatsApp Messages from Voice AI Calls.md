# Send WhatsApp Messages from Voice AI Calls

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008302-send-whatsapp-messages-from-voice-ai-calls](https://help.gohighlevel.com/support/solutions/articles/155000008302-send-whatsapp-messages-from-voice-ai-calls)  
**Category:** AI Employee  
**Folder:** Voice AI

---

Voice AI Automation

# Send WhatsApp Messages from Voice AI Calls

Enable your Voice AI agents to automatically deliver WhatsApp templates to callers during live conversations.

What You'll Learn

Voice AI agents can now send approved WhatsApp templates to contacts during live calls, enabling you to deliver booking links, payment details, or business information exactly when needed in the conversation.

This article covers how to configure the Send WhatsApp Message action, set trigger conditions, and ensure compliant message delivery during Voice AI calls.

Labs Feature

The Voice AI - Send WhatsApp Message Action (Location) must be enabled via Settings → Labs before it appears in your Voice AI agent configuration.

Table of Contents

1

What is the Send WhatsApp Message Action?

2

Key Benefits

3

Prerequisites

4

How to Set Up the Send WhatsApp Message Action

5

How the Action Works During a Call

6

Important Compliance and Delivery Notes

7

Frequently Asked Questions

1

## What is the Send WhatsApp Message Action?

The Send WhatsApp Message action enables Voice AI agents to automatically deliver pre-approved WhatsApp templates to contacts during live phone calls. When a caller requests information such as a booking link, payment details, or business contact information, your AI agent can instantly send the relevant WhatsApp message to the contact's WhatsApp number without interrupting the conversation.

This action uses your connected WhatsApp Business numbers and only sends templates that have been approved by WhatsApp, ensuring every message complies with WhatsApp's messaging policies. The AI agent cannot compose custom messages, modify templates, or change recipients during the call.

2

## Key Benefits

The Send WhatsApp Message action streamlines information delivery during Voice AI calls by providing instant access to critical details through WhatsApp.

**Instant Information Delivery** — Send booking links, payment URLs, or business details to callers the moment they need them, without requiring them to write down information or visit a website.

**Seamless Call Experience** — Message delivery is asynchronous and does not interrupt or pause the ongoing conversation between the AI agent and the caller.

**Automatic Recipient Detection** — The message is automatically sent to the contact's WhatsApp number associated with the call — no manual phone number entry required.

**Full WhatsApp Compliance** — Only pre-approved WhatsApp templates can be sent, ensuring every message adheres to WhatsApp Business API policies and template guidelines.

**Contextual Trigger Control** — Define specific conversation conditions that trigger the message send, such as when a caller asks for appointment details or payment options.

3

## Prerequisites

Before configuring the Send WhatsApp Message action, ensure the following requirements are met in your sub-account:

**WhatsApp Business API Setup** — WhatsApp must be configured in the sub-account with at least one WhatsApp-enabled phone number connected (Settings → WhatsApp).

**Approved WhatsApp Templates** — At least one WhatsApp message template must be created and approved by WhatsApp that complies with Meta's guidelines before it can be used with Voice AI agents.

**Labs Feature Enabled** — The Voice AI - Send WhatsApp Message Action (Location) must be enabled in Settings → Labs before the action appears in your Voice AI agent configuration.

4

## How to Set Up the Send WhatsApp Message Action

Follow these steps to configure a Voice AI agent to send WhatsApp messages during calls.

Step 1

Enable the Labs Feature

Navigate to Settings → Labs and enable the **Voice AI - Send WhatsApp Message Action (Location)** feature. This makes the action available in your Voice AI agent configuration.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077129474/original/tKluSeMjDa2NSEtMgkMlEEPk6TRSeD6ktA.png?1785324686)

Step 2

Access Your Voice AI Agent

Open the Voice AI agent you want to configure and navigate to the **Actions** section. Click the **\+ New Action** button to open the action selection menu.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077129551/original/RmTgQCwXp_I8VqBrz8WI4l19wFj7spEK_A.png?1785324736)

Step 3

Add the Send WhatsApp Message Action

From the action dropdown menu, select **Send WhatsApp message**. This opens the Send WhatsApp Message configuration modal where you will define how and when the action executes during calls.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077129630/original/xb-FgjFKdEc_ejRBVTY8bX326xbiNl276Q.png?1785324785)

Step 4

Name Your Action

In the **Action name** field, enter a descriptive name for the action (e.g., "send_whatsapp" or "send_booking_link"). This name helps you identify the action in your agent configuration.

Step 5

Define When the WhatsApp Delivery Should Take Place

In the **When should the WhatsApp delivery take place?** field, specify the trigger condition. For example, enter "When user wants to receive quotation over whatsapp" or "When the caller asks for the booking link." The AI agent monitors the conversation and triggers the action when this condition is met.

Step 6

Set What to Say Before Sending the WhatsApp Message

In the **What to say before sending WhatsApp message** field, enter what the AI agent should say immediately before sending the message. For example, "Sending you right away" or "I'll send that to your WhatsApp now." This provides context to the caller during the conversation.

Step 7

Select the WhatsApp Number

In the **From** dropdown, choose the WhatsApp Business number from which the message will be sent. This must be a WhatsApp number already connected to the sub-account via Settings → WhatsApp.

Step 8

Choose an Approved WhatsApp Template

In the **Template** dropdown, select one of your WhatsApp templates that has been approved by WhatsApp. The dropdown displays all approved templates available in the sub-account, showing the template name, category, language, and number of variables. Only approved templates can be sent via this action.

Step 9

Fill in Body Variables

If the selected template contains body variables (placeholders for dynamic content), fill in each variable in the **Body variables** section. Enter the values as free text. As you configure the variables, a live preview on the right displays the final message that will be sent to the contact, allowing you to verify the content before saving.

Step 10

Save the Action Configuration

Click **Update** to save the action settings. The action will now appear in the **DURING THE CALL** section of your Voice AI agent's Actions panel. The Voice AI agent is now configured to send the selected WhatsApp template when the trigger condition is met during a call.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077129739/original/F5H1wsdADNmIVv5OxVBzIdu-Pxs2znK3Rw.png?1785324863)

5

## How the Action Works During a Call

Once configured, the Send WhatsApp Message action operates automatically during live calls based on the trigger condition you defined.

When the AI agent detects that the trigger condition has been met — for example, when the caller requests a quotation over WhatsApp — the agent first says the pre-configured message you defined in the "What to say before sending WhatsApp message" field, such as "Sending you right away." The agent then automatically sends the configured WhatsApp template to the contact's WhatsApp number associated with the call.

The message delivery happens asynchronously, meaning the WhatsApp message is sent in the background without interrupting or pausing the phone call. The AI agent can continue the conversation while the WhatsApp message is delivered to the contact.

6

## Important Compliance and Delivery Notes

The Send WhatsApp Message action is designed to maintain full compliance with WhatsApp's messaging policies while providing a seamless user experience.

Template-Only Messaging

The AI agent can only send pre-approved WhatsApp templates. The agent cannot compose free-form WhatsApp messages, modify template content, or change the template structure. This ensures every message complies with WhatsApp Business API policies and template approval requirements.

Asynchronous Delivery

WhatsApp message delivery occurs in the background and does not interrupt the ongoing phone call. The AI agent continues the conversation while the message is sent, providing a seamless experience for the caller.

Fixed Recipient

The WhatsApp message is automatically sent to the contact associated with the call. The AI agent cannot alter the recipient or send the message to a different WhatsApp number during the call.

7

## Frequently Asked Questions

Q: Can the AI agent send custom WhatsApp messages during a call?

No. The AI agent can only send pre-approved WhatsApp templates. It cannot compose free-form messages, modify template content, or change the template structure. This ensures compliance with WhatsApp Business API policies and template approval requirements.

Q: Does the WhatsApp message interrupt the phone call?

No. Message delivery is asynchronous and does not interrupt or pause the ongoing conversation. The AI agent continues speaking with the caller while the WhatsApp message is sent in the background.

Q: How does the AI agent know which WhatsApp number to send the message to?

The message is automatically sent to the WhatsApp number associated with the contact on the call. No phone number entry is required — the system uses the contact record linked to the active call.

Q: What happens if the selected WhatsApp template is not approved?

Only approved WhatsApp templates appear in the template selection dropdown. If a template has not been approved by WhatsApp, it will not be available for use with the Send WhatsApp Message action. Ensure your templates are approved via Settings → WhatsApp before configuring the action.

Q: Can I send multiple WhatsApp messages during a single call?

Yes. You can configure multiple Send WhatsApp Message actions with different trigger conditions in the same Voice AI agent. Each action will execute independently when its specific trigger condition is met during the call.

Q: Where do I manage my WhatsApp templates?

WhatsApp templates are created and managed in Settings → WhatsApp. You must create a template and wait for WhatsApp to approve it before it can be used with the Send WhatsApp Message action.

Q: Can I preview the WhatsApp message before saving the action?

Yes. When you configure the template variables, a live preview displays on the right side of the configuration modal showing the final message that will be sent to contacts. This allows you to verify the message content before saving the action configuration.

Q: Is the Send WhatsApp Message action available for all HighLevel accounts?

The Send WhatsApp Message action is currently available as a Labs feature. To use it, you must enable the Voice AI - Send WhatsApp Message Action (Location) in Settings → Labs. Labs features may be in testing or early access and could be subject to changes or limitations.

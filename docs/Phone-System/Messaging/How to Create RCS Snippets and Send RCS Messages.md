# How to Create RCS Snippets and Send RCS Messages

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007783-how-to-create-rcs-snippets-and-send-rcs-messages](https://help.gohighlevel.com/support/solutions/articles/155000007783-how-to-create-rcs-snippets-and-send-rcs-messages)  
**Category:** Phone System  
**Folder:** Messaging

---

RCS Messaging

Creating and Sending RCS Snippets

Automate rich, interactive RCS conversations directly from HighLevel Workflows with RCS-specific actions.

What You'll Learn

This article explains how to use the new RCS Workflow actions to automate rich messaging experiences. You'll learn how to add RCS actions to your Workflows, create interactive customer journeys, and leverage rich cards and buttons to drive engagement.

Whether you're building onboarding sequences, promotional campaigns, or customer support automations, RCS Workflow actions help you deliver next-generation messaging experiences at scale.

  


  


Availability

This feature is currently available as part of the RCS Private Beta.

If you're interested in early access, please reach out to your Customer Success Manager or submit the RCS Private Beta interest form - <https://api.leadconnectorhq.com/widget/form/gBhAwqgT5SdbKSmCRszF>

Table of Contents

1

Before You Begin

2

Part 1: Creating an RCS Snippet

3

Part 2: Sending RCS Messages to Your Contacts

4

What the Message Looks Like After It's Sent

5

Sending RCS from Conversations (1:1 Messages)

6

RCS Through Workflows

7

You're Ready to Send

8

Frequently Asked Questions

Video Walkthrough

1

## Before You Begin

This guide assumes RCS is already enabled on your account and your Sender ID has been approved. If you haven't completed setup yet, start with the overview article — _[RCS in the Platform](<https://help.gohighlevel.com/support/solutions/articles/155000007782-rcs-in-highlevel>)_ — which walks through the full setup process.

Once you're live, there are two things you need to do: create an RCS Snippet (your message template), and then send it to your contacts via Bulk Actions. This guide covers both, in that order.

Why Snippets First?

RCS Snippets are the templates that power your campaigns. You build them once, then reuse them across as many sends as you need. You can't send a rich RCS campaign without one — so creating your Snippet is always the first step.

2

## Part 1: Creating an RCS Snippet

Snippets live inside Conversations. To get there, go to the Conversations page and select Snippets from the left panel. Then click **Add RCS Snippet** to open the template builder.

![Add RCS Snippet button inside Conversations](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070144531/original/RAN5qbb5uuvOau7f12C_30VrpHf4xn8pDg.png?1777388249)

You'll see three template formats. Each one is suited to a different type of message — choosing the right format before you start saves time and makes the rest of the process straightforward.

### The Three Snippet Formats

![The three RCS Snippet formats: Plain Text, Standalone Card, Carousel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070144545/original/xArws_745fxWj8cWtc2pxRMNfv4bpN5xJw.png?1777388268)

Format 1

Plain Text

Plain Text is exactly what it sounds like — a simple text message with no images, no media, and no action buttons. As you type, a live preview shows you exactly how the message will appear on the recipient's device.

Use this format when the words alone do the job — confirmations, reminders, short updates. It's the lightest format and the one closest to a standard SMS in feel, but it still benefits from RCS branding (your business name in the inbox instead of a number).

![Plain Text RCS Snippet preview](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070144552/original/BxIO4wfW9DhMvRUE7LuNxxxNSz-W-SgOGg.png?1777388285)

When to Choose Plain Text

If your message doesn't need a button or an image to be effective, Plain Text is the right call. Simpler templates also have a lower chance of triggering fallback issues on edge-case devices.

Format 2

Standalone Card

A Standalone Card is a single rich message — one card with a title, a description, an image or media file, and up to three action buttons. This is the format to reach for when you want the experience to feel premium: a promotional offer, a service announcement, an appointment reminder with a "Book Now" button.

Action buttons can be set to call a phone number, open a URL, or insert a suggested reply. You can add up to three buttons per card, and you can use emoji and custom tags inside the title and description fields.

A fallback SMS message is required for every Standalone Card. This is the plain text version of your message that gets delivered to contacts who can't receive RCS. The platform enforces this — you won't be able to save the template without it.

![Standalone Card RCS Snippet builder](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070144604/original/5yksqU5N7rFYFYdO5hukuKL7nVMd5v5lnw.png?1777388315)

Write the Fallback First

Before designing the card, write your fallback SMS. If the plain text version doesn't communicate the core message clearly on its own, the card isn't ready either. Strong fallback copy makes the whole template stronger.

Format 3

Carousel

A Carousel lets you build multiple rich cards that appear in a swipeable row inside the message — a minimum of 2 cards and a maximum of 10. Each card has its own title, description, media, and up to two action buttons.

Use a Carousel when you're presenting a set of options or items side by side — a product line, multiple service packages, a set of team members, different property listings. It gives the recipient context and comparison in a single message without requiring them to tap out to a website first.

Like the Standalone Card, a Carousel requires a fallback SMS message. Contacts who can't receive RCS will get the fallback text instead of the swipeable cards.

![Carousel RCS Snippet with multiple swipeable cards](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070144616/original/_RV55iiYoAdNE6wej7RMY6QmWei8tXTxgg.png?1777388330)

Carousel Limits

Minimum 2 cards, maximum 10. Each card supports up to 2 action buttons (one fewer than a Standalone Card). Keep card titles and descriptions concise — they need to read clearly on a phone screen.

### Building a Snippet — Step by Step

The walkthrough below uses a Standalone Card as the example, but the process follows the same structure for all three formats.

Step 1

Go to Conversations → Snippets → Add RCS Snippet

Select your template format from the three options. For a rich card with media and buttons, choose Standalone Card.

Step 2

Name Your Template

Give the template a clear, unique name — you'll be selecting it from a dropdown later when setting up your campaign. A descriptive name like "Spring Furniture Promo Card" is easier to find than something generic.

Step 3

Fill In the Card Details

Add your card title, description, and any promo codes or custom tags. You can use emoji in these fields. Keep the description focused — this is the copy the recipient reads first.

Step 4

Upload Media

Add an image or media file to the card. Use a high-quality image that represents the offer or message clearly — this is the visual anchor of the card.

Step 5

Add Action Buttons

Add up to three action buttons (two for Carousel cards). Set each button to call a number, open a URL, or insert a suggested reply. Save each action before moving to the next.

Step 6

Write the Fallback SMS

Type the plain text version of your message in the fallback field. This is what contacts receive if their device can't support RCS. It should communicate the same core information as the card — no buttons or images, just clear copy.

Step 7

Create the Template

Click _Create Template_ to save. Your Snippet is now in your library and ready to use in a campaign.

Your Snippet Is Ready

Once saved, your template appears in the Snippets library. You can reuse it across as many campaigns as you need — no rebuilding required.

3

## Part 2: Sending RCS Messages to Your Contacts

With your Snippet ready, the next step is sending it. RCS Snippets are sent via Bulk Actions — this is currently the only way to send rich RCS templates at scale. Here's the full process.

### Selecting Your Contacts

Go to **Contacts** and open **Smart Lists**. Select the contacts you want to reach — you can select individual contacts or an entire Smart List. Once selected, click **More → Send SMS & RCS** to open the campaign configuration screen.

![Selecting a Smart List and choosing Send SMS and RCS](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070143184/original/CC868lPmBedZkfXTov9WSPKMNKewkzZPog.png?1777387596)

### Configuring Your Campaign

The configuration screen has a few required fields — filling these correctly before you send saves having to troubleshoot later:

Field| What to Do  
---|---  
Action Name| Give your campaign a name you'll recognize on the Bulk Actions tracking page.  
From (Sender ID)| Select your approved RCS Sender ID from the dropdown. Only registered, approved IDs appear here — if yours isn't showing, check with Support.  
RCS Template| Select the Snippet you just created. Only saved Snippets appear in this list.  
Send Mode| Choose Send All at Once, Send at Scheduled Time, or Send in Drip Mode depending on your campaign needs.  
Consent Checkbox| Check this to confirm your contacts have opted in. This is required — the Send button won't activate without it.  
  
### Previewing and Sending

![RCS template preview before sending](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070143255/original/XDjU2MiTdRRXV8jwXqVtGNV2fjGEmjjejw.png?1777387635)

Before you send, review the template preview — this shows exactly how the message will appear to recipients who can receive RCS. Confirm the card title, description, buttons, and media all look correct.

When you're ready, click **Send RCS**. The campaign fires and you can track its progress on the Bulk Actions page by clicking **Check Progress**.

Tracking Your Send

Head to the Bulk Actions page after sending to monitor delivery progress. The page shows how many messages were sent, delivered, and whether any fell back to SMS.

![Bulk Actions tracking page showing delivery progress](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070144323/original/MalCL1Mh5rGxVGiG2Vz0OOO443ekIznu7A.png?1777388151)

Note

Bulk Actions is currently the only method for sending RCS Snippets.

4

## What the Message Looks Like After It's Sent

Once the campaign has gone out, you can view the conversation in the contact's thread under Conversations. The message appears with an **RCS** label and shows the Sender ID it was sent from so you can confirm it went out on the right profile.

Delivery status updates (Sent, Delivered, Opened) appear in the conversation view as the message moves through to the recipient. If the message fell back to SMS, the conversation will reflect the SMS delivery instead.

What "Opened" Means

An Opened status means the recipient viewed the message on a device that supports read receipts. Not all devices support this — and recipients can disable it. It's a positive signal when it appears, but not a metric to depend on across your full audience.

5

## Sending RCS from Conversations (1:1 Messages)

If you want to send a single RCS message to one contact directly — without a Snippet or a campaign — you can do that from the Conversations page.

Open the contact's thread, compose your message, select your approved RCS Sender ID from the sender selector, and send. The message goes out as RCS if the contact's device supports it, and falls back to SMS automatically if not.

![Sending a 1:1 RCS message from a contact's Conversations thread](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070143126/original/tsOq8vqK4hsg6EF6cvRAltP5MYYORo4VCg.png?1777387551)

  


## **Send RCS Snippets in Conversations (1:1)**

  


Select and send pre-built RCS snippets directly from a one-to-one conversation without leaving the Conversations page. This streamlines your messaging workflow by allowing you to choose an existing snippet, preview how it will appear to the recipient, and send it from the conversation composer.

  


> **Note:** Sending RCS snippets from the Conversations composer is currently available as part of the **RCS Private Beta** and may not be available in all accounts.

### **How to Send an RCS Snippet**

  1. Navigate to **Conversations** and open the conversation with the desired contact.  
  

  2. In the message composer, click the **RCS Snippet** option to open the **Choose RCS message** window. Also, the "**FROM** " number should be rcs sender id.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078361005/original/xhFHf4tjgTiKUncqf2Sgcpa5OQOL0658oA.png?1786632379)

  


  3. Select an existing RCS snippet from the **List of templates** dropdown.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078361098/original/zJ0cVbeJo8qVYuet8gr3GD-m2_OwduH3eQ.png?1786632409)
  4. Review the snippet details and preview to verify the content before sending.

     * Confirm the title, description, and action buttons.
     * If the snippet contains multiple cards, browse through each card to ensure the content is correct.
     * Review the fallback message that will be delivered to recipients who do not support RCS.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078361160/original/elDnlszKeYI9xygK1BOr9Aabc-be0CQOUw.png?1786632435)
  5. Click **Send** to deliver the RCS snippet to the contact.  
  


> **Important:** Only previously created RCS snippets are available for selection. If you need a new snippet, create it first before returning to the conversation.

6

## RCS Through Workflows

You can now create richer, more engaging customer journeys with **RCS messaging directly inside Workflows**. The new **Send RCS** and **RCS Interactive Message** workflow actions let you automate conversations using the next generation of business messaging.

### What You Can Do

With the new Workflow actions, you can:

  * Send standard RCS messages from Workflows.
  * Build interactive RCS experiences with rich cards and buttons.
  * Trigger different workflow paths based on customer interactions.
  * Automate reminders, promotions, follow-ups, and customer engagement using RCS.


### How to Use This Feature

  1. Navigate to **Automation → Workflows**.
  2. Create a new Workflow or edit an existing one.
  3. Add either the **Send RCS** or **RCS Interactive Message** action.
  4. Configure your message or interactive experience.
  5. Publish your Workflow.


### Why It Matters

Using RCS in Workflows allows you to:

  * Automate rich, conversational customer experiences.
  * Increase engagement with interactive RCS messages.
  * Route contacts based on button selections and responses.
  * Deliver a more modern messaging experience directly from your Workflow automations.


7

## You're Ready to Send

Creating an RCS Snippet takes a few minutes once you've got your content ready. Sending it to your contacts takes a few clicks. The experience your contacts receive — a branded, interactive card inside their native messaging app — is worth both.

Start with one Snippet. Send it to a small list. Check the conversation view to see how it lands. Then scale from there.

Good to Know

For questions about enabling RCS, setting up your Sender ID, or understanding pricing and compliance, see the companion article: _[RCS in the Platform](<https://help.gohighlevel.com/support/solutions/articles/155000007782-rcs-in-highlevel>)_.

8

## Frequently Asked Questions

### **Q: Do I need an RCS Snippet to send any RCS message?**

**A:** No. You only need an RCS Snippet for rich formats such as Standalone Cards or Carousels. You can also send a plain-text RCS message directly from a 1:1 conversation without creating a snippet.

* * *

### **Q: Can I send a Standalone Card or Carousel to just one contact?**

**A:** Yes. You can now send supported RCS snippets, including Standalone Cards and Carousels, directly from a 1:1 conversation by selecting an existing RCS snippet from the conversation composer. This feature is currently available to accounts enrolled in the RCS Private Beta.

* * *

### **Q: Can I preview an RCS snippet before sending it?**

**A:** Yes. After selecting an RCS snippet from the conversation composer, you can preview the content, media, buttons, and fallback message before sending it.

* * *

### **Q: Can I create a new RCS snippet directly from a conversation?**

**A:** No. You must create and save an RCS snippet first. Once it has been created, you can select it from the conversation composer when sending a message.

* * *

### **Q: Can I edit the selected RCS snippet before sending it?**

**A:** No. The conversation composer allows you to select and preview an existing RCS snippet before sending it. To modify the content, edit the snippet first, then return to the conversation to send the updated version.

* * *

### **Q: What happens if a contact's device doesn't support RCS?**

**A:** If the recipient's device or carrier does not support RCS, the configured fallback message is delivered instead, ensuring the contact still receives your communication.

* * *

### **Q: How many action buttons can I add to each format?**

**A:** Standalone Cards support up to **three** action buttons. Carousel cards support up to **two** action buttons per card. Plain Text snippets do not support action buttons.

* * *

### **Q: Can I trigger RCS messages automatically instead of sending them manually?**

**A:** Yes. You can use the **Send RCS** and **RCS Interactive Message** workflow actions to automate RCS messaging, create interactive experiences, and build automated customer journeys.

* * *

### **Q: What's the difference between Sent, Delivered, and Opened?**

**A:** **Sent** means the message has left the platform. **Delivered** means it reached the recipient's device. **Opened** indicates the recipient viewed the message on a device that supports read receipts. Not all devices support read receipts, so this status may not always be available.

* * *

### **Q: Can I reuse the same RCS snippet across multiple messages or campaigns?**

**A:** Yes. Once an RCS snippet is saved, it remains available in your snippet library and can be reused in Bulk Actions, Workflows (where supported), and 1:1 conversations if your account has access to the feature.

> * * *

### **Q: Why don't I see the option to send an RCS snippet in Conversations?**

**A:** Sending RCS snippets from the Conversations composer is currently available only to accounts participating in the **RCS Private Beta**. If you don't see the option, your account may not yet have access.

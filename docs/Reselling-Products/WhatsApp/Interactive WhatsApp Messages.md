# Interactive WhatsApp Messages

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006082-interactive-whatsapp-messages](https://help.gohighlevel.com/support/solutions/articles/155000006082-interactive-whatsapp-messages)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# Interactive WhatsApp Messages

Add buttons, lists, location, and contact cards to WhatsApp messages sent from CRM Workflows.

Interactive WhatsApp Messages let you **add buttons, lists, location, and contact cards to WhatsApp messages** sent from CRM Workflows. This article covers what interactive messages are, which interactive WhatsApp message types you can send, and how to configure them within Workflows.

TABLE OF CONTENTS

  * What are Interactive WhatsApp Messages?
  * Key Benefits
  * Prerequisites: Customer Service Window
  * How to Add the WhatsApp Interactive Messages Action
  * Interactive Reply Buttons
  * Location
  * Contact
  * List
  * CTA (Visit Website) URL Button
  * Branching & Workflow Behavior
  * Best Practices
  * Frequently Asked Questions
  * Related Articles


## What are Interactive WhatsApp Messages?

The CRM supports **Interactive WhatsApp Messages** directly inside the Automation module. The **WhatsApp Interactive Messages** action makes it easy to send rich, interactive experiences to your customers on WhatsApp. With this feature, you can send:

**Interactive Reply Buttons:** Up to 3 quick-reply buttons your users can tap.

**Location Messages:** Send a map location with latitude and longitude.

**Contact Messages:** Send rich contact cards with names, phone numbers, addresses, and emails.

**List Messages:** Present structured menus with multiple sections and rows.

## Key Benefits of Interactive WhatsApp Messages

The points below explain the practical advantages you'll gain by using interactive WhatsApp messages within your workflows.

**Higher Reply Rates:** Contacts answer faster because responding is a single tap, no need to type.

**Cleaner CRM Data:** Choices are standardized, cutting typos and mismatches so reporting stays accurate.

**Lower Messaging Costs:** Window-aware sending helps you avoid unnecessary spend.

**More Conversions:** Direct calls-to-action move contacts to booking, checkout, or payment with less friction.

**Fewer Mistakes and Misunderstandings:** Predefined options minimize typos and ambiguity, so conversations stay accurate and on track.

## Prerequisites: Customer Service Window

Before you send Interactive WhatsApp Messages, you must ensure the **WhatsApp 24-hour Customer Service Window** is open.

When a WhatsApp user sends your business a message, a 24-hour Customer Service Window begins. During this window:

  * You can send unlimited Interactive WhatsApp messages at no cost.
  * There are no restrictions on free-form messaging.


[Learn more about WhatsApp: Customer Service Window Check](<https://help.gohighlevel.com/support/solutions/articles/155000003235-whatsapp-customer-service-window-check>)

### How to Check or Trigger the Customer Service Window

You have two options in Automations:

Option 1: Use the Customer Replied Trigger (WhatsApp)

The Customer Replied via WhatsApp trigger ensures the workflow only starts when the customer sends a WhatsApp message, which automatically opens the 24-hour window. Use the information below to configure this trigger:

  * **Workflow Trigger:** Customer Replied
  * **Filters:** Set Reply Channel = WhatsApp


Option 2: Use the WhatsApp: Customer Service Window Check Action

![Customer Service Window Check action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155052286891/original/3p45ZiR6nSp7HO_6m0HuAiT8noU3aMYSXw.png?1756120926)

Use the _WhatsApp: Customer Service Window Check_ action to evaluate whether the 24-hour window is open before sending your interactive message. Use the information below to configure this action:

  * **Action Name:** WhatsApp: Customer Service Window Check
  * **Conversation Phone Number:** Choose the WhatsApp number you're sending from.
  * Configure Branches:
    * _**Branch Name:** Open – Condition: Customer Service Window is Open_
    *  _**Branch Name:** Closed – Condition: Customer Service Window is Closed_


    
    
    IMPORTANT: If the window is closed, you must send a Marketing or Utility Template message to reopen the conversation.

![Customer Service Window Check branches](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155052303654/original/FJ1UwAUkxDRrkuBv4yk2GcPknCNGmD3fiA.png?1756128686)

## How to Add the WhatsApp Interactive Messages Action

Once you've confirmed the Customer Service Window is open, you can add the new Interactive Messages action.

1

Open your **Workflow**.

2

Click **Add Action (+)**.

3

Select **WhatsApp Interactive Messages**.

4

(Optional) Rename **Action Name** for clarity (default is **WhatsApp Interactive Messages**).

5

In **Interactive Message Configuration** , select the **From Phone Number** then choose the **Interactive Message Type**.

![Interactive Message Configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053696925/original/ZNv9FFIduh2wqWMn4lQszCuhrux-KHQecg.png?1757707568)

## Interactive Reply Buttons (Interactive Message Type)

Interactive Reply Buttons let you present up to 3 predefined responses. Users tap a button, and their selection can trigger branches, tags, or follow-up actions in your workflow. Here is how you configure Interactive Reply Buttons:

1

Choose the Interactive Message Type: set **Interactive Message Type = Quick Reply Buttons**

![Quick Reply Buttons selection](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053696931/original/pGFXib0bZdiFXP1hYZhsHzOzvr-SF2q1sQ.png?1757707607)

2

Fill out the required fields for Quick Reply Button messages:

  * **Input for Button Message** – The main message text.
  * **Button Count** – Choose up to 3.
  * **Header Type** – Text, Image, Video, or Document.
  * **Header Text or Media URL** – Enter text or media link.
  * **Body** – Required; main message body.
  * **Footer** – Optional; short supporting text.
  * **Timeout Unit** – Minutes, Hours, or Days.
  * **Timeout Value** – Enter number of units.
  * **Button Titles** – Add label text for each button.


Once all information has been added, make sure to Save and Test your workflow!
    
    
    TIP: Keep body text concise so buttons are visible without scrolling.

![Quick Reply Button fields](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053697047/original/Ey4RWC5g-LFOdffnA4lZb_P04N7k3FdCKQ.png?1757707904)

## Location (Interactive Message Type)

With the Location Interactive Message Type, you can send customers a location card that includes a clickable map preview. Here is how you configure Interactive Location Messages:

1

Choose the Interactive Message Type: set **Interactive Message Type = Location**.

![Location message type](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053697233/original/H_yqPhMhzOVV9YOX7kfa3L3qds3MVZoz6w.png?1757708451)

2

Fill out the required fields in Location Details:

  * **Location Name** – Example: `Facebook HQ`
  * **Address** – Example: `1 Hacker Way, Menlo Park, CA 94025`
  * **Latitude** – Example: `37.758056`
  * **Longitude** – Example: `-122.425332`


Save and test to confirm the location renders correctly in WhatsApp.
    
    
    TIP: Always double-check coordinates match your business address to avoid confusion.

![Location details fields](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053697255/original/6TbqEiRjbLl2hhAx_xXD_Pe_BCQxdp_XVQ.png?1757708534)

## Contact (Interactive Message Type)

With the Contact Interactive Message Type, you can send customers a rich contact card that they can save to their device. Here is how you configure Interactive Contact Messages:

1

Choose the Interactive Message Type: set **Interactive Message Type = Contact**.

![Contact message type](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053697343/original/1wBRIHgioXCvGOSGKnQOs5evGBjFrpuXXQ.png?1757708813)

2

Fill out the required fields:

  * **Contact Name** – First Name (required, e.g., `John`) and Last Name (required, e.g., `Jones`).
  * **Phone Numbers** – Phone Number (required, e.g., `+16505551234`) and Phone Type (Work, Mobile, Home).
  * **Email** – Email Address (optional, e.g., `john.jones@company.com`) and Email Type (Work, Home).


Save and test the workflow to confirm the contact card appears properly in WhatsApp.

![Contact card fields](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053697351/original/A10hwB70kfbG-ICVzcy6TfsEByUBXXTPdQ.png?1757708885)

## List (Interactive Message Type)

List Messages allow you to send structured menus with multiple sections and rows, giving customers clear options to choose from. Each selection can trigger separate branches in your workflow. Here is how you configure Interactive List Messages:

1

Choose the Interactive Message Type: set **Interactive Message Type = List**.

![List message type](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053697461/original/jAhje1lcLkV524FVO-gkPHzgAL8CZdyphA.png?1757709100)

2

Fill out the required fields:

  * **Input for Button Message** – The main prompt text for the menu.
  * **Section Count** – Choose how many sections you want (e.g., 3).
  * **Header Text** – Optional; short header title.
  * **Body** – The main message body.
  * **Footer** – Optional; supporting text.
  * **List Button Text** – The button label that opens the list (e.g., "View Options").
  * **Timeout Unit & Value** – Choose the timeout (5 minutes to 2 days).


Configure each section:

  * **Section Title** – Example: "Plans" or "Services".
  * **Row Count** – Number of rows in the section.
  * **Row Title** – Option label (e.g., "Premium Plan").
  * **Row Description** – Optional description for the option.


Add branching for each row:

  * Example: _Section1 Row1_ , _Section2 Row1_ , etc.
  * Additional branches are available for **Not Delivered** and **Timeout**.


Save and test to confirm the menu appears and selections trigger the correct branches.
    
    
    TIP: Use section titles to group related options (e.g., "Plans", "Add-ons") for better clarity.

![List message configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053697482/original/AVIAAbGp3xNshGnnZ85VE7WQnp2U6H0GKw.png?1757709159)

## Interactive Call-to-Action (Visit Website) URL Button Messages

WhatsApp users may be hesitant to tap long or complex URLs in plain text messages. **Interactive CTA URL Button Messages** solve this by mapping any URL to a clean, tappable button — creating a smoother and more trustworthy experience. When tapped, the button opens the specified URL in the user's default browser. Here is how you configure it:

1

Choose the Interactive Message Type: set **Interactive Message Type = Visit Website Button**.

2

Complete the required fields:

  * **Header Type** – Choose from Text, Image, Video, or Document.
  * **Header Text or Media URL** – Provide the header text or media link.
  * **Body** – Enter the main message body (max 1024 characters).
  * **Footer** – Optional short supporting text (max 60 characters).
  * **URL** – Enter the destination URL.
  * **Button Text** – Enter the text that will appear on the button (max 20 characters).
  * **Timeout Unit & Value** – Choose Minutes, Hours, or Days (allowed range: 5 minutes – 2 days).


Save and test with a sample contact to confirm the button displays correctly and links open in the browser.

![CTA URL button example 1](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155057874072/original/6brNPbS8T0q-ZhBmH6H4YCpfCfxRY4Tqdw.png?1762550971) ![CTA URL button example 2](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155057874080/original/ueMfiC4y8-l88Wg7aTBVRU2rGIjATSDlEA.png?1762550994)

### Example URL with CRM Variables

You can dynamically personalize URLs by embedding **CRM fields** , including **contact fields** and **custom values**.

`https://www.google.com/?name={{contact.name}}&calendar={{custom_values.agent_calendar}}`

In this example:

  * `{{contact.name}}` will dynamically insert the contact's name.
  * `{{custom_values.agent_calendar}}` will insert the assigned agent's calendar link.


This lets you build personalized booking links, payment URLs, or campaign landing pages.

### Example Button Setup in Workflow

  * **Header (Text):** _Workshop Details_
  * **Body:** _Tap below to book your slot._
  * **Footer:** _Spots are limited._
  * **URL:** `https://mybusiness.com/booking?name={{contact.name}}`
  * **Button Text:** _Book Now_
  * **Timeout Value:** 30 Minutes


**Result:** Each customer sees a unique button linking to their personalized booking page.

## Branching & Workflow Behavior

You can branch workflows based on the button's delivery and interaction:

  * **Link Opened** – Trigger when the link is successfully opened.
  * **Not Delivered** – Trigger if the message fails to deliver.
  * **Timeout** – Trigger if the message expires without interaction.


This allows you to automate follow-up actions based on whether customers engage with the link.

![Workflow branching options](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155057873995/original/2mqJTecLKybuHkZCCqGIFC0vY3t1Q_LIfA.png?1762550749)

## Best Practices

  * Always use trusted or branded URLs for better click-through rates.
  * Use CRM variables to reduce friction (e.g., pre-fill forms or auto-assign calendars).
  * Combine with Customer Service Window Check to ensure the message is sent during an open session.


## Frequently Asked Questions

Q: Do Interactive WhatsApp Messages cost extra?

No. As long as the 24-hour Customer Service Window is open, Interactive WhatsApp Messages are free. Meta does not charge for service conversations.

Q: What happens if I try to send an Interactive Message outside the 24-hour window?

If the Customer Service Window is closed, you must send a Marketing or Utility Template message first to reopen the window.

Q: How many buttons can I add in a Quick Reply message?

You can add up to 3 reply buttons. Each must have unique text (20-character limit).

Q: Can I use both headers and footers in a Quick Reply Message?

Yes. Headers support Text, Image, Video, or Document. Footers support short text only (max 60 characters).

Q: What happens if I enter the wrong coordinates for a Location Message?

The location card may drop the pin in the wrong place. Always verify latitude and longitude before saving.

Q: Can I send multiple contacts in a single Contact Message?

No. Each Contact Message supports one contact card. To send multiple, create separate actions.

Q: How many sections and rows can I add in a List Message?

You can configure multiple sections, each with one or more rows. Each row requires a title (mandatory) and can include an optional description. Timeout must be set between 5 minutes and 2 days.

Q: Can I personalize URLs in Interactive Call-to-Action (Visit Website) Button Messages?

Yes. You can use CRM variables, including contact fields and custom values, inside URLs. Example:

`https://www.google.com/?name={{contact.name}}&calendar={{custom_values.agent_calendar}}`

This allows you to create personalized booking links, payment pages, or campaign landing pages.

Q: What happens if the customer taps a Visit Website button?

The link opens in their default browser. In workflows, you can branch based on outcomes:

  * Link Opened
  * Not Delivered
  * Timeout


Q: What are the timeout rules for Interactive Messages?

Timeouts define how long an interactive message (buttons, lists, or visit website buttons) stays active.

  * Minimum: 5 minutes
  * Maximum: 2 days


After timeout, the interactive element becomes inactive, and you can use the Timeout branch in workflows for follow-ups.

Q: Can I send multiple interactive types in one message (e.g., a List and a Visit Website Button)?

No. WhatsApp only allows one interactive message type per message. You can, however, send multiple actions sequentially in workflows.

## Related Articles

WhatsApp Full Setup Guide for Agency

WhatsApp Contact Management and Smartlist

WhatsApp Flows: In-App Appointment Booking

How to Set Up WhatsApp for a Sub-Account

WhatsApp: Send Message Templates (Snippets)

# WhatsApp Flows: In app Appointment Booking

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003720-whatsapp-flows-in-app-appointment-booking](https://help.gohighlevel.com/support/solutions/articles/155000003720-whatsapp-flows-in-app-appointment-booking)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

WhatsApp Automation

# WhatsApp Flows for Appointment Booking

Create guided, in-chat booking experiences that increase conversions and reduce drop-offs

What You'll Learn

This article explains how WhatsApp Flows enable interactive appointment booking directly inside WhatsApp, reducing friction and increasing booking completion rates.

You'll learn how to create appointment booking Flows, send them through templates or workflows, and use Ask AI to manage Flows conversationally.

Table of Contents

1

Why Flows Increase Booking Rates & Reduce Drop-offs

2

How to Create an Appointment Booking Flow

3

How to Send WhatsApp Flows Through Templates

4

How to Send WhatsApp Flows from Workflows

5

Managing Flows with Ask AI

6

Frequently Asked Questions

Video Walkthrough

1

## Why Flows Increase Booking Rates & Reduce Drop-offs

WhatsApp Flows is a feature that allows businesses to create interactive, guided conversations within WhatsApp. It enables the creation of structured, multi-step interactions that can collect information, provide choices, and guide users through specific processes—like booking an appointment.

**Reduced Friction** — Users can complete the entire booking process within WhatsApp, eliminating the need to switch to external websites or apps.

**Familiar Interface** — WhatsApp is a widely used platform, so users are already comfortable with the interface.

**Immediate Interaction** — Users can start the booking process instantly from a conversation, capitalizing on their initial interest.

**Personalization** — User details can be pre-filled, reducing effort and improving the booking experience.

**Reduced Load Times** — Unlike external websites, Flows operates within WhatsApp, typically resulting in faster load times and interactions.

2

## How to Create an Appointment Booking Flow

Step 1

Navigate to WhatsApp Flows Settings

Go to **Settings > WhatsApp > Flows**.

![WhatsApp Flows settings page](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034646684/original/NVp_HaDFK6wayVWYNpnobSJJdlt_XL0ltA.png?1728907137)

Step 2

Create a New Flow

Click **Create new Flow** , add a flow name, pick the calendar where appointments should be booked, then click **Next**.

![Create new Flow form](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034969111/original/JPfD77SO7WK3PD2OJA-qTqKNYjpyjlNGxg.png?1729254396)

Step 3

Arrange Form Fields

Arrange the default form fields for your appointment booking Flow.

![Form field arrangement](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035181602/original/_B5k1a8IdV7Ri5ExOnW6FH9_hoUDVMvQCA.png?1729599697)

Step 4

Configure Flow Content and Publish

Add the Header, Body, Footer, and Button text, then click **Publish**.

![Flow content configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035182484/original/FO0nEdCva9goQYT6lRIBHPE-jv4wVhIbAQ.png?1729600214)

Note

Calendars which have payments enabled will not be supported through WhatsApp Flows, since WhatsApp currently does not have payment capabilities.

3

## How to Send WhatsApp Flows Through Templates

Step 1

Navigate to WhatsApp Templates

Go to **WhatsApp > Templates > Create Template**.

![Create WhatsApp template](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035183476/original/MLEVHH87wrWLYCygp9xjE4rlF8iUeYe_RA.png?1729600770)

Step 2

Configure Template Content

Add the template name, category, language, header text, body, and footer.

![Template configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035184031/original/8GtcOZvkunN9KntkgRlzMdNfRcSysmnYMA.png?1729601046)

Step 3

Add a Flow Button

Add a button and select **Flow** to link it to your WhatsApp Flow.

![Add Flow button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035184085/original/LCkagOXfbXIFZ-3wcIbK1ZqEaqwucam1kw.png?1729601081)

4

## How to Send WhatsApp Flows from Workflows

Note

Recurring calendar events are currently not supported through WhatsApp Flows.

### Option 1: Send WhatsApp Flow via a WhatsApp Template

Step 1

Create a New Workflow

Go to **Automations > Create Workflow > Start from Scratch**.

![Create workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035062857/original/b4eyIMVE8ocE8xLR7vp4AfwkIovWWtBbeQ.png?1729493072)

Step 2

Add WhatsApp Action with Flow Template

Add the **WhatsApp Action** , select the template with the WhatsApp Flow, then click **Save Action**.

![WhatsApp action with Flow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035184319/original/bvxkgYVoIdIOtvCziiWAcuseq8bHnShx5g.png?1729601212)

### Option 2: Send WhatsApp Flow Inside an Open Conversation (Free of Cost)

Step 1

Create a New Workflow

Go to **Automations > Create Workflow > Start from Scratch**.

![Create workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035062857/original/b4eyIMVE8ocE8xLR7vp4AfwkIovWWtBbeQ.png?1729493072)

Step 2

Add Customer Service Window Check

Click the **+** button, add **WhatsApp: Customer Service Window Check** , then click **Save Action**.

![Customer service window check](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035062955/original/MkcpQ6kS0vmVceanLIkud9dp6cNbDsBDtQ.png?1729493170)

Step 3

Add Send Flows Action

Under the **Open** branch, add **WhatsApp: Send Flows** , then select the WhatsApp Flow to send.

![Send Flows action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035063231/original/NM7MrrswjF12yTOuFb65GeBUiQ46MhYybA.png?1729493428)

Step 4

Save the Action

Click **Save Action** to complete the workflow configuration.

![Save action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035063241/original/EUKYLlZmty06UbUsEW9TxeLqQ51bje-wLg.png?1729493465)

5

## Managing Flows with Ask AI

You can now create, update, publish, deprecate, and delete WhatsApp appointment-booking Flows using conversational prompts through Ask AI for WhatsApp. This eliminates manual Flow configuration and lets you deploy self-serve booking experiences at speed.

What Ask AI Can Do

Full Lifecycle Flow Management

  * Create new Appointment Booking Flows by saying which calendar or pipeline to use
  * Update existing Flows conversationally (for example, changing questions or availability rules)
  * Publish, deprecate, or delete Flows when they're no longer needed
  * Use a guided calendar-selection wizard to link Flows to the correct HighLevel calendar (for example, "Sales Calendar" or "Clinic Appointments")


Example Prompts

  * "Create a WhatsApp flow for appointment booking linked to my Sales Calendar, and publish it"
  * "Update my clinic booking Flow to ask for insurance information"
  * "Build a WhatsApp appointment booking Flow for my Therapy Calendar, publish it, and show me how to attach it to my reminder template"


For more details on using Ask AI to manage WhatsApp Flows, templates, campaigns, and analytics, see the Ask AI for WhatsApp article.

6

## Frequently Asked Questions

Q: How do I send a WhatsApp Flow for appointment booking?

There are two options:  
  
**Option 1 — Using a WhatsApp Template:** Go to Automations > Create Workflow > Start from Scratch. Select the WhatsApp Action, choose a template with the WhatsApp Flow for appointment booking, then save the action.  
  
**Option 2 — Using an Open Conversation:** Go to Automations > Create Workflow > Start from Scratch. Click the + button, add WhatsApp: Customer Service Window Check, then save the action. Under the Open branch, add WhatsApp: Send Flows and select the Flow to send, then save.

Q: How do I create an appointment booking flow?

Go to Settings > WhatsApp > Flows, create a new flow, add a name and select the calendar for appointments, arrange the default form fields, add header, body, footer, and button text, then publish.  
  
Note: Calendars with payment options are not supported, as WhatsApp currently does not process payments.

Q: How do I send WhatsApp Flows through templates?

Go to WhatsApp > Templates > Create Template. Add a template name, category, language, header text, body, and footer. Add a button and select Flow to link it to the WhatsApp Flow.

Q: Can I use Ask AI to create and manage WhatsApp Flows?

Yes. Ask AI for WhatsApp provides full lifecycle control of appointment-booking Flows through conversational prompts. You can create, update, publish, deprecate, and delete Flows without manual configuration. For example, you can say "Create a WhatsApp flow for appointment booking linked to my Sales Calendar, and publish it" and Ask AI will handle the entire Flow setup.

Q: Why does integrating flows for appointment booking increase booking rates and reduce drop-offs?

  * **Reduced Friction:** Users complete the booking process entirely within WhatsApp, avoiding external sites or apps.
  * **Familiar Interface:** Customers feel more comfortable since WhatsApp is a widely used platform.
  * **Immediate Interaction:** Customers can start booking directly from a conversation, capturing interest instantly.
  * **Personalization:** Key details like name and contact info are pre-filled, reducing effort.
  * **Faster Load Times:** Interactions happen quickly without the lag of external websites.


Q: What are the key benefits of using WhatsApp Flows for appointment booking?

  * **Reduced friction:** Everything happens inside WhatsApp, leading to a smoother booking experience.
  * **Pre-filled customer details:** Critical information such as name, email, phone number, and time zone is automatically filled in.
  * **Increased engagement:** Step-by-step guided conversations help reduce confusion and increase completion rates.
  * **Faster load times:** Flow interactions happen directly within WhatsApp, speeding up the process.
  * **Free conversations:** The first 1,000 service conversations for appointment booking are free each month.


Q: What limitations should I be aware of with WhatsApp Flows for appointment booking?

  * **No payment processing:** Appointments that require payments cannot be booked through the WhatsApp Flow, as WhatsApp currently does not support payments.
  * **Custom fields:** Only default form fields are supported. Custom fields must be handled manually.
  * **Recurring appointments:** Recurring calendar events are not supported.
  * **Guest support:** Guest booking functionality is not available within the WhatsApp Flow.


Q: How can I create a personalized appointment booking experience using WhatsApp Flows?

Use customer-specific data fields like name, email, and phone number, which are automatically pre-filled. Customize the messaging templates with variables that match customer preferences, offering a tailored and seamless booking experience.

Q: Are there any costs associated with sending WhatsApp Flows for appointment booking?

The first 1,000 service conversations for appointment booking using WhatsApp Flows are free each month. After that, charges may apply based on WhatsApp's pricing model.  
  
Note: If the sub-account's WhatsApp integration is Coex, Flows is not supported, because Meta does not support Flows for Coex integrations.

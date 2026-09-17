# RCS in HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007782-rcs-in-highlevel](https://help.gohighlevel.com/support/solutions/articles/155000007782-rcs-in-highlevel)  
**Category:** Phone System  
**Folder:** Messaging

---

# What is Covered

What it is, how it works, and what you need to know before you send your first message.

## What Is RCS?

SMS has been the backbone of business messaging for a long time. It works, it's reliable, and it reaches nearly every device. But it has a ceiling , a phone number as the sender, no images, no buttons, no way to know if your message was actually read.

Rich Communication Services (RCS) is what comes next. It's a modern messaging standard built into Android and ios devices that lets your business show up in a customer's inbox the way a real brand should , with your name, your logo, images, tappable action buttons, and interactive cards. All of it delivered inside the native messaging app, with no app download required from the recipient.

In HighLevel, RCS sits alongside your existing SMS setup. The only thing you require is a R sender id. When a contact's device supports it, they get the rich experience. When it doesn't falls back SMS is sent, so the message always gets through, regardless of the device.

**The core idea** RCS is SMS with a brand identity. Same reliability, dramatically better experience for contacts who can receive it.  
---  
  
### Join Our Private Beta List

RCS in HighLevel is rolling out in waves. Add your details below to join the private beta list and get early access as soon as we open the next cohort.Form not loading? [Open it in a new tab](<https://api.leadconnectorhq.com/widget/form/gBhAwqgT5SdbKSmCRszF>).  
---  
  
## What You Can Send with RCS

RCS gives you a set of tools that plain SMS simply doesn't offer. Depending on your plan and configuration, you can send:

  * Branded messages — your business name appears in the inbox instead of a phone number
  * Images and rich media layouts
  * Tappable action buttons — Call, Open URL, or Suggested Replies
  * Standalone rich cards with titles, descriptions, images, and buttons
  * Carousels — multiple swipeable cards in a single message
  * Read receipts and delivery signals where the recipient's device supports them


You can send RCS in two ways: as a 1:1 message directly from a contact's Conversations thread, or as a campaign via Bulk Actions using pre-built RCS Snippets. Both are covered in the companion article — _[How to Create RCS Snippets and Send RCS Messages](<https://help.gohighlevel.com/support/solutions/articles/155000007783-how-to-create-rcs-snippets-and-send-rcs-messages>)_.

## How RCS Compares to SMS and MMS

Before using RCS, it helps to understand exactly what it adds — and where its limits are. The biggest one: RCS reach is growing but not yet universal. That makes it important to design every message so the SMS fallback version is just as clear and useful as the rich version.

Feature| RCS| SMS| MMS  
---|---|---|---  
Branded Identity| Business name| Phone number| Phone number  
Rich Media| Native & fluid| None| Inconsistent  
Tap-to-Act Buttons| Yes| No| No  
Read Receipts| Often available| No| No  
Auto SMS Fallback| Built-in| —| —  
Universal Reach| Growing fast| Universal| Universal  
**⭐ Design for both** Before finalizing any RCS message, ask: if this arrives as plain text with no image and no buttons, does it still make sense? If yes, you're ready. If no, revise the copy first.  
---  
  
## Who Can Receive RCS?

RCS delivery depends on four things aligning on the recipient's end: their device, their messaging app, their carrier, and their app settings. In practice:

  * Most modern Android devices using Google Messages or a carrier-supported app are ready to receive RCS
  * iPhone support depends on iOS version and carrier — many iPhone users still receive SMS fallback today
  * Even within Android, some carrier configurations limit certain RCS features
  * Recipients can disable RCS features in their app settings, which also triggers fallback


HighLevel handles detection and routing automatically. You send one message — the platform determines whether to deliver it as RCS or fall back to SMS based on what the recipient can actually receive.

**What fallback means in practice** When a message falls back to SMS, the recipient gets your fallback text instead of the rich card. Billing reflects SMS pricing for that message. Opt-outs apply across both channels — a contact who opts out via SMS is suppressed on RCS too.  
---  
  
## Compliance and Consent

RCS is a branded, high-visibility channel — which means the same compliance principles that govern SMS apply here, just with higher stakes. Getting this right protects your deliverability, your sender reputation, and your customers.

### Opt-In

Only send RCS to contacts who have explicitly opted in. Your opt-in must tell them what type of messages they'll receive, how often, how to opt out, and how to reach support.

### Opt-Out

Honor these keywords immediately and without exception — they must suppress all future messages across both RCS and SMS:

STOP • UNSUBSCRIBE • CANCEL • END • QUIT

The opt-out notice is appended to the first 1:1 RCS message sent to a new contact — unlike SMS, it doesn't repeat periodically after that. Texas blocking rules apply the same as SMS and MMS.

### Content and Sending Frequency

Avoid deceptive, misleading, or spammy content. Keep sending frequency consistent with what you promised at opt-in. Reminders, confirmations, and genuinely useful updates perform best — they feel like service, not noise. For regulated industries, ensure your messaging aligns with your specific legal obligations.

**Sender identity** Use a sender name that matches your business or website exactly. Inconsistency in your sender identity erodes trust and increases opt-outs over time.  
---  
  
## Setting Up RCS

RCS needs to be enabled on your account before you can send anything. The process runs through HighLevel Support — here's the full sequence:

### What to Have Ready

  * Brand name and website URL
  * Support email and/or business phone number
  * Business address
  * Logo (if your configuration supports it)
  * A working opt-in process already in place for your contacts
  * A connected Twilio account


### Fees & Timelines (US Registrations)

A quick heads-up on fees & timelines: there are carrier fees involved for US registrations:

  * **Brand Verification:** $200 / year
  * **T-Mobile Submission:** $500 one-time fee

  
---  
  
Registrations are also available for several other countries. See the most up-to-date list of supported regions: [](<https://www.twilio.com/docs/rcs/regional>)[Programmable Messaging – RCS Regional Availability](<https://docs.google.com/document/d/1mURQxv7oQB67hElRxK_eyfZxYsNrLQG9PKkaU9Hvj6s/edit?tab=t.0>)

### The Setup Steps

01| **Contact HighLevel Support to Enable RCS** Request RCS activation on your account. Nothing else can happen until this is confirmed.  
---|---  
02| **Create Your RCS Sender Profile** Your sender profile is your brand's identity on the RCS network — name, logo, contact details. ISV locations work with HighLevel Support directly. Non-ISV locations share their brand details with Support for setup.  
---|---  
03| **Submit for Carrier Approval** HighLevel Support submits your sender profile for approval. This is required before any message can go out. Approval timelines vary — complete, accurate submissions move through faster.  
---|---  
04| **Enable SMS Fallback** Go to Settings → Messaging → RCS → Fallback and turn on Fallback to SMS. This ensures every message reaches every contact — RCS where supported, SMS where not.  
---|---  
05| **Send a Test Message** Open Conversations, pick a test contact (US Android device recommended), and send a plain text message first, then test rich content. Some contacts may receive SMS fallback — this is expected behavior, not an error.  
---|---  
  
## Message Statuses

After a message is sent, HighLevel shows delivery signals directly in the conversation view:

Status| What It Means  
---|---  
**Sent**|  Message left HighLevel and is in transit.  
**Delivered**|  Message arrived on the recipient's device.  
**Opened**|  Recipient viewed the message (where device supports read receipts).  
  
Read receipts are only available when the recipient's device and messaging app support them — and recipients can turn this off. Treat it as a useful signal when it appears, not a metric you can rely on universally.

## Pricing and Billing

RCS billing is based on message type and direction. Here's the full breakdown for US messages:

Message Type| Direction| Billing Unit| Price (USD)  
---|---|---|---  
Basic RCS Text| Outbound| Per segment| $0.0083  
Basic RCS Text| Inbound| Per message| $0.0083  
Rich RCS| Inbound| Per message| $0.0165  
Rich RCS| Outbound| Per message| $0.0220  
  
### Carrier Fees

  * Carrier fees are billed directly by Twilio
  * Agency Accounts: standard Twilio pricing
  * Location Accounts: Twilio pricing + 5% markup


### Failed Message Billing

**Scenario A — RCS fails → SMS fallback delivers** No RCS charge. You pay only for the SMS that successfully delivered.  
---  
**Scenario B — RCS fails → SMS fallback also fails** A static processing fee of $0.001 applies — unless the failure matches specific Twilio error codes (30036, 30002, 30450, 21408, and others), in which case no fee is charged.  
---  
**First-attempt rule** First-attempt RCS failures that trigger SMS fallback are not charged. A fee only applies if the final SMS fallback also fails.  
---  
  
## Frequently Asked Questions

### Will every message be delivered as RCS?

No , and this is by design. Contacts on unsupported devices or networks receive your message as SMS fallback. Always design your messages to work in both formats.

### Can I use my existing phone number for RCS?

RCS works differently from SMS. In supported inboxes, your brand name and logo appear instead of a phone number , which is one of the channel's biggest advantages over traditional SMS.

### How long does sender approval take?

Timelines vary depending on submission quality and carrier review volume. Submitting complete, accurate information the first time avoids delays.

### Can I send images and buttons to all my contacts?

Not universally. Contacts who receive SMS fallback won't see images or buttons — only the plain text fallback message. Your core call-to-action needs to work in words, not just a button.

### Do opt-outs carry over between RCS and SMS?

Yes. Opt-outs are contact-level, not channel-level. A STOP received via SMS suppresses RCS messages too , and vice versa.

## Ready to Get Started?

If RCS isn't enabled on your account yet, reach out to HighLevel Support to get the feature activated. Once you're approved and your Sender ID is live, the next step is creating your first RCS Snippet and sending it to your contacts.

For a step-by-step walkthrough of creating Snippets and sending your first RCS campaign, see the companion article: _[How to Create RCS Snippets and Send RCS Messages.](<https://help.gohighlevel.com/support/solutions/articles/155000007381-the-complete-guide-to-rcs-in-highlevel>)_

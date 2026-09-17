# WhatsApp: Unsupported Message Type

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007905-whatsapp-unsupported-message-type](https://help.gohighlevel.com/support/solutions/articles/155000007905-whatsapp-unsupported-message-type)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

Troubleshooting GuideWhatsApp: Unsupported Message TypeUnderstand why some messages appear as unsupported in HighLevel, what message types are supported, and how to resolve error code 131051.  
---  
  
* * *

**TABLE OF CONTENTS**

  * What is an Unsupported Message Type?
  * Error Code 131051 Explained
  * Supported Message Types in HighLevel
  * Unsupported Message Types
  * How Unsupported Messages Appear in HighLevel
  * How to Resolve This
  * Frequently Asked Questions


* * *

What is an Unsupported Message Type?Why some messages cannot be displayed or sent through the WhatsApp Business API  
---  
  
WhatsApp offers many message types in the consumer app — stickers, polls, voice notes, GIFs, contact cards, and more. However, the **WhatsApp Business Platform (Cloud API)** that powers HighLevel only supports a specific set of message types.

When a customer sends a message type that the Business API does not support — such as a poll or a deleted message — HighLevel **cannot display or process it**. Instead, you will see a notification indicating that the message is unsupported.

This is **not a bug in HighLevel** — it is a limitation set by Meta's WhatsApp Business Platform API. The same restriction applies to all CRM platforms built on the API.
    
    
    Unsupported message types are a **Meta API limitation** , not a HighLevel issue. These message types cannot be displayed or responded to from any Business API-based platform.

* * *

Error Code 131051 — Unsupported Message TypeWhat this error means and when it occurs  
---  
  
Meta assigns the error code **131051** when a message type is not supported by the WhatsApp Business API. This error appears in two situations:

|  Inbound (Customer sends to Business)A customer sends a message type the API cannot process — such as a poll, GIF, or deleted message. HighLevel receives a webhook notification with `type: "unsupported"` and error code `131051` instead of the message content.  
---  
|  Outbound (Business sends to Customer)A message fails to send because the message type or format used is not supported by the API. The message is not delivered and the error is returned.  
---  
      
    
    **Error Code:** 131051
    **Title:** Unsupported message type
    **Details:** Message type is not currently supported
    **Type returned:** unknown or unsupported

* * *

✓ Supported Message Types in HighLevelThese message types are fully supported by the WhatsApp Business Platform API  
---  
  
The following message types can be **sent and received** through HighLevel's WhatsApp integration:

Message Type| Direction| Details  
---|---|---  
Text| Both| Plain text messages, including emojis and links  
Image| Both| JPEG, PNG. Max 5MB  
Video| Both| MP4, 3GPP. Max 16MB  
Audio| Both| AAC, MP4, MPEG, AMR, OGG (audio). Max 16MB  
Document| Both| PDF, Word, Excel, PowerPoint, and more. Max 100MB  
Sticker| Both| Static WebP (outbound). Animated WebP (inbound only)  
Location| Both| Share or receive a map pin with coordinates  
Template Messages| Outbound| Pre-approved Marketing, Utility, and Authentication templates  
Interactive| Outbound| List messages, Reply buttons, CTA URL buttons  
Contacts| Both| Structured contact cards via the API only  
Reaction| Both| Emoji reactions to messages (API v2.45+)  
  
* * *

✘ Unsupported Message TypesThese types cannot be displayed or processed through the WhatsApp Business API  
---  
  
The following message types are **not supported** by the WhatsApp Business Platform API. If a customer sends any of these, they will appear as an unsupported message in HighLevel and you will not be able to see the content:

| PollsWhatsApp polls sent by customers cannot be received or displayed through the API.  
---  
|  Ephemeral MessagesDisappearing messages set to auto-delete are not supported by the Business API.  
---  
|  Deleted MessagesWhen a customer deletes a message, the API receives an unsupported notification and cannot recover its contents.  
---  
|  GIFsAnimated GIFs sent from the consumer app are treated as an unsupported type by the Business API.  
---  
|  Voice CallsRegular WhatsApp voice and video calls from the consumer app are not supported. WhatsApp Calling via the Business API is a separate feature.  
---  
|  Group MessagesMessages sent from WhatsApp groups are not supported by the Business Platform API.  
---  
|  Contact Cards (from Consumer App)Contact cards shared natively from a consumer's phonebook via WhatsApp are not supported inbound. Structured contact messages sent via the API are supported.  
---  
|  Business-to-Business (API to API)WhatsApp API accounts are not designed to message other WhatsApp API accounts. This is a Meta restriction and will trigger error 131051.  
---  
  
* * *

How Unsupported Messages Appear in HighLevelWhat you'll see in your conversation view when an unsupported message is received  
---  
  
When a customer sends an unsupported message type, HighLevel displays a placeholder in the conversation thread. Depending on the message type, you may see:

| ? A message bubble that reads **"Unsupported Message"** or **"This message type is not supported"**  
---  
| ? For unsupported **file types** that exceed limits, the file may be converted into a URL link  
---  
| ? For **custom payloads** , a "Show More" option may appear to view raw JSON data  
---  
  
The message will still appear as **received** in HighLevel — you will know the customer sent something, but the contents cannot be read. You can still reply to the contact normally.
    
    
    ? Best practice: If a customer seems to be sending unsupported content, reply asking them to resend their message as a **text, image, audio, or document** so it can be processed correctly.

* * *

How to Resolve ThisSteps to take when you encounter unsupported message type errors  
---  
| Step 1**Identify the message type** — check the conversation to understand what the customer was trying to send  
---  
| Step 2**Reply to the customer** asking them to resend using a supported format such as text, image, audio, or document  
---  
| Step 3If you are **sending** a message and getting this error — verify your message type and format matches the supported types listed above  
---  
| Step 4If the error persists for **outbound messages** , check that your API parameters are correct and no unsupported fields are included in the payload  
---  
      
    
    This error is **not fixable** for inbound unsupported messages — there is no way to read the content of a poll, deleted message, or GIF through the Business API. This is a Meta platform limitation.

* * *

Frequently Asked QuestionsCommon questions about unsupported message types  
---  
❓ A customer sent me a poll — why can't I see it in HighLevel?Polls are not supported by the WhatsApp Business Platform API. When a customer sends a poll, HighLevel receives a webhook with error code 131051 and the message appears as unsupported. There is no way to view the poll content — ask the customer to share their response as a text message instead.  
---  
❓ Is this a bug in HighLevel?No. This is a limitation of Meta's WhatsApp Business Platform API. Every CRM and messaging platform built on the API — including HighLevel — has the same restriction. It cannot be worked around.  
---  
❓ Can I still reply to a customer who sent an unsupported message?Yes. Even though you cannot see the content of the unsupported message, the conversation is still open. You can reply normally using any supported message type such as text, image, or audio.  
---  
❓ A customer deleted a message — can I recover what they sent?No. Deleted messages are not recoverable through the API. Once a message is deleted by the customer, neither HighLevel nor Meta's servers will have a record of its content.  
---  
❓ Will Meta add support for polls and GIFs in the future?Meta periodically expands the Business API's capabilities. Reactions, for example, were added in a later API version. Keep an eye on Meta's [WhatsApp Business Platform changelog](<https://developers.facebook.com/documentation/business-messaging/whatsapp/overview/>) for updates. HighLevel will incorporate new supported types as Meta makes them available.  
---  
❓ I'm getting error 131051 when sending a message — what should I check?Verify that the message type you are sending is in the supported list above. Common causes include sending an animated GIF, using an incorrect API parameter, or attempting to send a message to another WhatsApp Business API account (business-to-business messaging is not supported by Meta).  
---  
? Quick TipTo avoid confusion with customers, consider adding an **automated reply** in HighLevel that triggers when an unsupported message is received — letting the customer know their message couldn't be read and asking them to resend as text, image, audio, or document.  
---

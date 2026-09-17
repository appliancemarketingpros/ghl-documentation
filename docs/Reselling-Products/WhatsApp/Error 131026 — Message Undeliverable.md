# Error 131026 — Message Undeliverable

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007934-error-131026-message-undeliverable](https://help.gohighlevel.com/support/solutions/articles/155000007934-error-131026-message-undeliverable)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

Troubleshooting GuideError 131026 — Message UndeliverableUnderstand why WhatsApp messages fail to deliver with error code 131026, what causes it, and how to resolve it.  
---  
What you'll learn| + What error 131026 means| + All known causes| + How to diagnose it| + Steps to resolve it  
---|---|---|---  
  
* * *

**TABLE OF CONTENTS**

  * What is Error 131026?
  * Known Causes
  * How to Diagnose the Cause
  * How to Resolve It
  * How to Prevent It
  * Related Error Codes
  * Frequently Asked Questions


* * *

What is Error 131026?Message Undeliverable — the message was sent but could not be delivered to the recipient  
---  
  
Error **131026** is a WhatsApp Cloud API delivery-level failure. It means the message was successfully submitted to Meta's servers but **could not be delivered to the recipient's device**.

This is what the error looks like in the API response:
    
    
    "errors": [
      {
        "code": 131026,
        "title": "Message Undeliverable"
      }
    ]

According to Meta's official documentation, error 131026 is intentionally a **"bucket error"** — meaning multiple different underlying causes all return the same error code. Meta does not always disclose the specific reason to protect user privacy. This makes diagnosing the root cause require some investigation.
    
    
    **Important:** You are **not billed** for messages that return error 131026. The message was not delivered and no conversation was opened, so no charge is applied.

* * *

Known CausesAll officially documented and commonly observed reasons for this error  
---  
  
The following causes are listed in Meta's official documentation or have been confirmed by the WhatsApp developer community:

1\. Recipient phone number is not on WhatsAppThe phone number you are messaging has not registered a WhatsApp account, or the number no longer exists. This is the most common cause of error 131026.  
---  
2\. Recipient has blocked your business numberIf the recipient has blocked your WhatsApp Business number, messages cannot be delivered. Meta returns error 131026 without disclosing the block to protect user privacy.  
---  
3\. Recipient has not accepted Meta's Terms of Service or Privacy PolicyIf the recipient has not accepted WhatsApp's latest Terms of Service and Privacy Policy, some messages — particularly template messages — may fail to deliver.  
---  
4\. Recipient is using an outdated version of WhatsAppWhatsApp requires a minimum app version to receive Cloud API messages. If the recipient has not updated their app, messages with buttons, links, or media may fail. The minimum required versions are:  
  
**Android:** 2.21.15.15 or higher  
**iOS:** 2.21.170.4 or higher  
**KaiOS:** 2.2130.10 or higher  
---  
5\. Authentication template sent to an India (+91) numberAuthentication templates **cannot be sent to WhatsApp users with a +91 (India) country code**. This is a hard restriction from Meta — it is not a bug and cannot be bypassed. Use SMS, email, or another OTP channel for Indian numbers.  
---  
6\. Marketing message frequency limit reachedMeta enforces **Marketing Template Frequency Capping** to protect users from receiving too many marketing messages from multiple businesses. If a user has already received several marketing messages from different businesses in a short period, further marketing messages may be blocked — even from businesses they have opted into. The exact limits are dynamic and not disclosed by Meta.  
  
Note: This scenario may also return error **131049** in some cases.  
---  
7\. Recipient is located in a restricted or sanctioned countryMessages cannot be delivered to users in countries that are sanctioned or restricted under applicable laws and regulations. Meta does not disclose which specific countries are restricted in API responses.  
---  
8\. Business-to-Business (API to API) messagingThe WhatsApp Business API is designed for businesses to message consumers — not for one API account to message another API account. Attempting to send a template message from one WhatsApp Business API account to another will consistently return error 131026.  
---  
  
* * *

How to Diagnose the CauseUse this step-by-step method to narrow down the root cause  
---  
  
Because Meta groups multiple causes under the same error code, the best way to diagnose which specific reason is triggering 131026 is to use a process of elimination.

Step 1 **Send a plain-text utility message** to the same number — no buttons, no media, no links. Just a simple text-only message using a utility template

| **If it delivers successfully:** The issue is likely the recipient's WhatsApp version being too old to render advanced message formats. Ask them to update WhatsApp.  
---  
| **If it also fails:** The number is likely not on WhatsApp, has been disconnected, or the user has blocked your number. Remove from your active list.  
---  
  
Step 2 **Check if the error is isolated or widespread** — is it failing for one specific number, a segment of contacts, or all messages?

| **Isolated to one number:** That specific contact is likely not on WhatsApp, has blocked you, or hasn't accepted Terms of Service.  
---  
| **Widespread failures on marketing messages:** Likely triggered by Meta's marketing frequency capping — try sending utility messages instead.  
---  
  
Step 3 **Check the phone number format** — verify that all numbers include the correct international country code and have no extra characters or spaces

Step 4 **Check the template category** — if you are sending to an India (+91) number, confirm you are not using an Authentication template

Step 5 **Check Meta's platform status** — visit [metastatus.com/whatsapp-business-api](<https://metastatus.com/whatsapp-business-api>) to confirm there are no ongoing outages affecting message delivery

* * *

How to Resolve ItActions to take based on the identified cause  
---  
Cause| Resolution  
---|---  
Number not on WhatsApp| Remove the number from your contact list. Use a phone number validation service before sending.  
Number has blocked you| Stop messaging the contact. Continuing to attempt delivery to a blocked number will not succeed.  
Has not accepted Terms of Service| No action possible from your side. The recipient must accept the terms themselves by opening WhatsApp.  
Outdated WhatsApp version| Send a simple text-only message first. If it delivers, ask the recipient to update their WhatsApp app.  
Auth template to India (+91)| Use SMS, email, or another OTP channel for Indian numbers. This is a hard Meta restriction.  
Marketing frequency cap| Send a utility message instead. Wait before retrying marketing messages. Retry with increasing time intervals — do not send the same message immediately again.  
Restricted country| Remove contacts from restricted or sanctioned countries from your messaging lists.  
Business-to-Business messaging| This is not supported by Meta. Use the WhatsApp consumer app to open a conversation window first.  
      
    
    **Do not retry immediately.** If 131026 is caused by frequency capping, resending the same message right away will return the same error. Wait and retry with increasing time intervals.

* * *

How to Prevent ItBest practices to reduce error 131026 occurrences  
---  
| **Validate phone numbers before sending** — use a number validation service to confirm numbers exist and are registered on WhatsApp before adding them to your contact list  
---  
| **Collect proper opt-ins** — ensure every contact has explicitly opted in to receive WhatsApp messages from your business before you message them  
---  
| **Keep your contact list clean** — regularly remove contacts who have unsubscribed, blocked you, or whose messages have been consistently undeliverable  
---  
| **Use the correct template category** — misclassifying a template as Marketing instead of Utility increases the chance of hitting frequency limits  
---  
| **Monitor your template quality rating** — low quality ratings increase the risk of delivery failures. Keep templates relevant, clear, and valuable to recipients  
---  
| **Do not use Authentication templates for India (+91) numbers** — route Indian users to SMS or email OTP as an alternative  
---  
  
* * *

Related Error CodesOther delivery errors you may see alongside 131026  
---  
Error Code| Title| Description  
---|---|---  
131049| Healthy Ecosystem Engagement| Marketing message blocked to protect user from excessive messages. Do not retry immediately.  
131051| Unsupported Message Type| The message type used is not supported by the WhatsApp Business API.  
131021| Same Sender and Recipient| Sender and recipient phone number is the same. Send to a different number.  
130497| Restricted from Messaging Country| Your WhatsApp Business Account is not approved to message users in that country.  
  
* * *

Frequently Asked QuestionsCommon questions about error 131026  
---  
Q: Will I be charged for messages that return error 131026?No. Messages that fail with error 131026 are not delivered and no conversation is opened, so you will not be billed for them.  
---  
Q: Can I find out exactly why the message was not delivered?Not directly. Meta intentionally uses error 131026 as a broad code to protect recipient privacy. You can narrow it down using the diagnostic steps in this article, but the exact reason is not always disclosed.  
---  
Q: Should I retry sending the message immediately after getting this error?No. Retrying immediately will not help and may make things worse if the cause is frequency capping. If you need to retry, use increasing time intervals between attempts. If the number is not on WhatsApp or has blocked you, retrying will never succeed.  
---  
Q: My messages were delivering fine before but are now returning 131026 — what changed?A sudden increase in 131026 errors on marketing templates is most likely caused by Meta's marketing frequency capping. This enforcement has been expanding since 2024. Try sending utility messages to the same contacts and check if those deliver. If they do, the issue is specifically with marketing template delivery limits.  
---  
Q: What is the difference between error 131026 and error 131049?Both indicate undeliverable messages, but error **131049** is specifically tied to Meta's marketing message frequency cap ("Healthy Ecosystem Engagement"). Error **131026** is broader and can be caused by multiple reasons including invalid numbers, blocked contacts, outdated app versions, and more. In some cases, frequency capping may still surface as 131026.  
---  
Q: Can I send to India (+91) numbers at all?Yes — you can send **Marketing** and **Utility** templates to India (+91) numbers without issues. The only restriction is that **Authentication templates** cannot be sent to +91 numbers. This is a hard Meta rule and cannot be changed.  
---  
Quick SummaryError 131026 means the message was not delivered. The most common causes are an invalid number, a blocked contact, or a marketing frequency cap. Use the diagnostic steps above to identify the cause, clean your contact list regularly, and always collect proper opt-ins before messaging. If the issue persists, contact our support team.  
---

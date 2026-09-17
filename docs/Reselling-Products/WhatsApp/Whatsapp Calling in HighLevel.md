# Whatsapp Calling in HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007253-whatsapp-calling-in-highlevel](https://help.gohighlevel.com/support/solutions/articles/155000007253-whatsapp-calling-in-highlevel)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

WhatsApp Calling enables your team to make and receive voice calls directly within WhatsApp conversations in HighLevel, eliminating the need for an external dialer or sharing personal phone numbers. With support for inbound and outbound calling, configurable business hours, call permissions, and call dispositions, your team can resolve customer issues faster while keeping every interaction in one conversation thread. 

  


This guide explains how to configure WhatsApp Calling, manage permissions, and use the feature on both Web and Mobile.  
  
What you'll learn| ✓ What WhatsApp Calling is| ✓ How to enable & set up| ✓ Configure call permissions| ✓ Make and receive calls  
---|---|---|---  
  
* * *

**TABLE OF CONTENTS**

  * What Is WhatsApp Calling?
  * How to Enable WhatsApp Calling
  * Country Availability
  * WhatsApp Inbound Calls
  * Setting Up WhatsApp Calling
  * Setting Up WhatsApp Call Permissions
  * Making and Receiving WhatsApp Calls
  * Configure Staff User Calling Settings


* * *

What Is WhatsApp Calling?Voice and chat in one place — no app switching required  
---  
      
    
    **Accessing WhatsApp Calling (Beta)**
    
    WhatsApp Calling is currently in **beta** and is not yet available to all users. To request access, please complete the beta access form:
    
    [https://api.leadconnectorhq.com/widget/form/xpGWoA9VnKVWRqr4oibs](<https://api.leadconnectorhq.com/widget/form/xpGWoA9VnKVWRqr4oibs>)

  


WhatsApp Calling brings voice conversations directly into your existing WhatsApp conversations, allowing your team to seamlessly transition from messaging to voice whenever a call is the fastest way to help a customer. Keeping calls inside the same conversation preserves context, simplifies communication, and automatically logs call activity alongside messages.

  


WhatsApp Calling supports both inbound and business-initiated outbound voice calls (where supported by Meta), making it easier for sales and support teams to communicate without switching applications or using external phone systems.

  


**Key capabilities include:**

  * Make and receive WhatsApp voice calls directly within HighLevel  
  

  * Use WhatsApp Calling on both Web and the LeadConnector Mobile App  
  

  * Configure business availability and temporary unavailable periods  
  

  * Route incoming calls to multiple users  
  

  * Request customer permission before placing business-initiated calls  
  

  * Track every WhatsApp call alongside traditional phone calls  
  

  * Apply custom call dispositions after each call  
  

  * Trigger automations based on call outcomes


* * *

## **Key Benefits of WhatsApp Calling**

  


Voice conversations often resolve complex questions faster than extended messaging exchanges. WhatsApp Calling combines messaging and voice into a single customer experience while providing administrators with complete visibility into every interaction.

  


  * **Keep conversations together:** Calls and messages remain in the same WhatsApp conversation for complete customer context.  
  

  * **Faster issue resolution:** Escalate from chat to a voice call with a single click when messaging becomes inefficient.  
  

  * **Improved sales conversions:** Speak with high-intent leads immediately while they're engaged.  
  

  * **Business-controlled availability:** Configure when customers can call using business hours and temporary unavailable schedules.  
  

  * **Smart call routing:** Route incoming WhatsApp calls to specific team members or the contact's assigned user.  
  

  * **Automation-ready:** Trigger workflows based on custom call dispositions after every conversation.  
  

  * **Centralized reporting:** Review WhatsApp call performance alongside other voice activity in Call Reporting.  
  

  * **Available on Web and Mobile:** Agents can answer and place calls whether working from their desktop or mobile device.


* * *

# Prerequisites

**Meeting the required prerequisites ensures WhatsApp Calling functions correctly and complies with Meta's eligibility requirements. Verify each requirement before enabling the feature for your business.**

Before enabling WhatsApp Calling, ensure your sub-account meets all of the following requirements:

  * A WhatsApp phone number is connected and in a **Connected** status.
  * Your WhatsApp Business Account (WABA) messaging limit is **2,000 conversations or higher**.
  * The phone number is **not using WhatsApp Coexistence**.
  * Users have permission to access the connected WhatsApp number.
  * LeadConnector Mobile App version **4.18 or later** is installed for mobile calling.
    * White-label mobile apps must also be updated to a version that includes WhatsApp Calling support.

How to Enable WhatsApp CallingActivate calling for your sub-account  
---  
  
To activate WhatsApp Calling for your sub-account, click the provided activation link and complete the request form with the required details. Once submitted, WhatsApp Calling access will be enabled for your **sub-account within 24 hours**.

  

    
    
    **Requirements — Before using WhatsApp Calling, ensure the following:**
    
    ✓  The WhatsApp number must be supported by Meta's WhatsApp Business API.
    ✓  WhatsApp Calling is NOT supported for Coexistence (WhatsApp App + API on the same number).
    
    ✓  The business must have a messaging limit of at least [2,000 business-initiated conversations](<https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits>) in a rolling 24-hour period. More details on [scaling your account capabilities](<https://www.facebook.com/business/help/595597942906808>).

* * *

Country AvailabilityWhatsApp Calling is available in most countries  
---  
  
WhatsApp Calling is available in most locations. However, Business initiated calls (BIC) is currently **not supported** in the following countries:

| **United States**  
---  
**Canada**  
**Turkey**  
| | **Egypt**  
---  
**Vietnam**  
**Nigeria**  
      
    
    If your business or customer is located in one of these countries, Business initiated calls (BIC)  will not be available at this time.

* * *

WhatsApp Inbound Calls (Customer-Initiated)When a customer calls you directly via WhatsApp  
---  
  
Inbound calls occur when a **customer calls your business via WhatsApp**. These calls will appear inside your CRM like any other notification. You can answer, decline, or let the call go to voicemail if configured.

  


**How it works in CRM:**

| ? When a customer calls, you will see an alert inside your CRM message or call interface.  
---  
| ✅ You can **accept the call directly** within the CRM — no need to open WhatsApp separately.  
---  
| ? After the call ends, call details (time, duration, outcome) are stored and linked to the customer's conversation for future reference.  
---  
  
  


* * *

Setting Up WhatsApp CallingConfigure your phone number and assign users to handle calls  
---  
  
Step 1 Open **WhatsApp** and go to **Settings**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069597360/original/bLs9rRGI73eKFGnEbBlIdQLz1ZGzhC7UyQ.png?1776768958)

  


Step 2 Select **Calling** from the menu.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069597830/original/Uy52qjpXwlZx3meYlEa8ctfNLGNQt-yaDw.png?1776769266)

  


Step 3 You will see a list of phone numbers currently showing as **connected**. Identify the number you want to set up for calling.

  


Step 4 Find the number you want to configure and click **Manage**.

  


Step 5 Assign a **friendly name** (e.g., _Sales Team_) for easy identification across your workspace.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069594284/original/3KQ8jnEyfOd6YZU7mPo-_NK5FjcfgRpcvQ.png?1776767351)

  


Step 6 Under **Ring WhatsApp Calls To** , add the users who should receive inbound calls. Set a **primary user** to ring first, and add additional users as backup if needed.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069594793/original/dCUjG_mi_C1a9rPlaFcEylRgHT0yufXEGA.png?1776767564)

  


Step 7 Enable **Allow Voice Calls** to activate WhatsApp Calling for this number. Turn on **Allow People to Request Callback for Missed Calls** so customers can request a return call if their call goes unanswered.

  


Step 8 Toggle **Display Call Button** so customers see a call option directly on your WhatsApp business profile.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069597841/original/psv8jkMyktJMlIftbzOGpEcKVr5qTDSpfQ.png?1776769284)

  


Step 9 Set up **Available Callers** and **Temporarily Unavailable Callers** based on your team's schedule and availability.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069593579/original/gah6QaPHDW3Kxa4l3ND_VcpVDtFjW2r_vQ.png?1776767005)
    
    
    ? Tip: Keep your caller availability updated to ensure inbound calls are always routed to the right person and to reduce missed calls.

* * *

Setting Up WhatsApp Call PermissionsRequest and manage customer call permissions  
---  
      
    
    **Important:** WhatsApp requires explicit customer approval before calling can be enabled for a contact. Always confirm permission is active before initiating a call.

  


Step 1 Go to **Settings** > **WhatsApp Templates**.

  


Step 2 Create a new template requesting call permission from your customers.

  


Step 3 Under **Call-to-Action Buttons** , select **WhatsApp Call Permissions**. This adds a button to the template that customers can tap to grant you calling access.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069597849/original/76RQlsjsLAzwb5ORzWLmPRM0JMS8nO22Pw.png?1776769302)

  


Step 4 When customers receive this message, they tap the provided button to grant permission for a **temporary** or **unlimited** duration.

  


Step 5 You can also include a call button directly in templates and set the permission duration to **1, 7, 15, or 30 days** depending on your use case.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069593581/original/xbgjUIRB8nes2eipsg9DVpFbSttovJNkBw.png?1776767005)

Once customers grant permission, you are ready to handle calls.

* * *

Making and Receiving WhatsApp CallsInitiate and receive calls from the Conversations view  
---  
  
Step 1 Go to **Conversations** > open any contact > tap **WhatsApp** as the messaging channel.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069596270/original/0vqB4nOQXe5QNuBGSfNU5ZXnXahIi88hrw.png?1776768237)

  


Step 2 Select the messaging template that requests call permission and send it to the customer.

  


Step 3 Once the customer grants permission, their status will update to **"Call permissions active indefinitely"** — or display the specific duration they selected.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069597879/original/lKp8lQfL53xVS6OAK_pnVUFs8-v_SzL6wQ.png?1776769328)

  


Step 4 When making or receiving a call, you will see options to **end the call** and **add dispositions** to log the outcome.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069596524/original/MbloHKJEuLMX6vhcJo60Apetv944ciqscw.png?1776768349)

  


Step 5 For inbound calls, customers can call you directly by tapping the **call button** on your WhatsApp business profile. The call will ring through to the users assigned in your calling settings.
    
    
    ? Tip: Always add a call disposition after each call to keep your team's records accurate and make follow-ups easier.

* * *

Configure Staff User Calling SettingsSet the default call channel for each staff member  
---  
  
Step 1 Go to **Settings** > **My Staff**.

  


Step 2 Search for the assigned staff user and click **Edit**.

  


Step 3 Open the **Calling & Voicemail** tab.

  


Step 4 Set **Default Channel for WhatsApp Calls** to either **Mobile App** or **Web App**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062503358/original/zdRC0vWcpOawO9-QNwpr2x_6CcFMP-TtVA.png?1768283146)

? Mobile AppCalls ring on the staff member's mobile device| | ? Web AppCalls ring in the CRM browser interface  
---|---|---  
  
* * *

✅ You're all set!WhatsApp Calling brings fast, reliable voice communication into your existing messaging workflow. Keep your availability settings current, respond to permission requests promptly, and use call dispositions to stay organised — so your team stays reachable and your customers stay engaged.  
---  
  
  


Feature GuideWhatsApp User Call PermissionsBefore your business can place a WhatsApp voice call, the customer must grant permission. This guide explains how permissions work, how to request them, and what happens when they expire or are revoked.  
---  
What you'll learn| ✓ How permissions work| ✓ Temporary vs permanent| ✓ Permission limits & rules| ✓ Expiry & unanswered calls  
---|---|---|---  
OverviewThe user is always in control of call permissions  
---  
  
If you want to place a call to a WhatsApp user, your business must receive their permission first. The business has no control over this — permission can only be granted or revoked by the user, at any time.

  


**There are three ways a customer can grant call permission:**

| ? **Permission request message** — You send the customer a free-form or template message requesting permission to call.  
---  
| ? **Customer calls you first** — When a user calls your business, temporary permission is automatically granted (callback setting must be enabled).  
---  
| ? **Via Business Profile** — The user can grant or update call permissions directly through your WhatsApp Business Profile at any time.  
---  
  
* * *

Temporary vs Permanent PermissionsPermanent permissions available as of November 3, 2025  
---  
  
When a customer approves a call permission request, they choose between two options:

  


Temporary Permission

  * Lasts **7 calendar days (168 hours)** from the moment the user approves
  * Expires automatically — no notification sent on expiry
  * Subject to the connected calls limit
  * Can be requested again after expiry

| | Permanent Permission

  * **Does not expire**
  * Stored until the user explicitly revokes it
  * Subject to the same connected calls limit
  * User can revoke at any time via the Business Profile

  
---|---|---  
  
  


The screenshots below show how the permission options appear to the customer on their WhatsApp app:

  


Allow Calls (Permanent)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069763268/original/BRzAJvAQftu5LfSRGqP_cT7OYBViPV4b_g.png?1776931400)| | Temporarily Allow Calls![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069763297/original/YgFUhA3h1HJdgvEYXax6qlpxLGUAdpvYEQ.png?1776931412)  
---|---|---  
  
* * *

Permission LimitsEnforced automatically by WhatsApp to protect users  
---  
Limit| Value  
---|---  
Permission requests per contact per day| Maximum 1 every 24 hours  
Permission requests within a 7-day period| Maximum 2 requests  
Connected calls per business phone number| Maximum 100 every 24 hours  
Temporary permission duration| 7 calendar days (168 hours)  
When limits reset| When any connected call is made between the business and user  
  
* * *

How to Request Call PermissionProactively send a permission request message to the customer  
---  
  
You can request call permission from a customer by sending a permission request message. The customer can then choose to **approve (temporary or permanent)** , **decline** , or simply not respond.

  

    
    
    **Important:** Even if a customer approves permission, they can revoke it at any time. Conversely, if a customer declines, they can still choose to grant permission later — up until the request expires.

* * *

Free-Form vs Template MessagesChoose the right message type based on your conversation history  
---  
? Free-Form Message**When to use:** You have an open customer service window with the contact.

  * Text body is optional but recommended
  * Header and footer are **not supported**
  * No new conversation window needed

| | ? Template Message**When to use:** No recent conversation exists with the contact.

  * Text body is **required**
  * Supports header and footer
  * Must be pre-approved by WhatsApp

  
---|---|---  
  
  


— Criteria for Sending Call Permission Request Messages

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069761824/original/C7UtBrW4NDyeh2o7a7jxWu1SywP5M9rq1g.png?1776930401)

  


**How template messages look to the customer:**

  


Template with Header, Body & Footer![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069761953/original/vlJ_H7XFc9RuNO1_0_fvu0afC_em7b6Mog.png?1776930505)| |  Template with Body Only![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069762003/original/W5XTKdjwFZxBXeOSWCL7jmbwEtVcbAl8UQ.png?1776930549)  
---|---|---  
  
  


Free-Form Message with No Text Body

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069762107/original/5k2EQTqU7ilUHhCyldp2ScyzVXD7ojR5XQ.png?1776930626)
    
    
     Best practice: Always include a clear, specific reason for the call in your message body. For example: _"We'd like to call you to confirm delivery of your order #ON-12345."_ This context significantly improves customer approval rates.

* * *

Consecutive Unanswered CallsWhatsApp automatically protects users from repeated missed calls  
---  
  
If your business repeatedly calls a customer and the calls go unanswered, WhatsApp takes automatic protective action:

  


| 2 Consecutive Unanswered CallsWhatsApp sends the user a **system message** prompting them to reconsider whether they still want to allow this business to call them.  
---  
|  4 Consecutive Unanswered CallsCall permission is **automatically revoked** by WhatsApp. The user may choose to grant it again, but only through their own explicit action.  
---  
      
    
    **Note:** Only call customers when there is a clear, relevant reason. Repeated unanswered calls damage trust, trigger automatic warnings, and risk permanent permission revocation.

* * *

Permission Request Expiry ScenariosA permission request expires in one of three situations  
---  
Scenario| What Happens  
---|---  
User accepts or declines the request| Request expires 7 days after the user's response  
User does not respond| Request expires 7 days after delivery  
A new permission request is sent| The previous request expires **immediately**  
  
  


**Expiry scenario screenshots:**

  


Expires After 7 Days (User Responded)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069762194/original/ysWVw16Fn9cBhX6Gc7thH6pbJqGUFYa4Pw.png?1776930678)| |  Expires After 7 Days (No Response)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069762568/original/w_h26HnBHX0HkibJKux-t6ZRAIlNip8Dsw.png?1776930924)  
---|---|---  
  
  


Previous Expires, New Request Received![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069762580/original/eWFxfd96ZC7WjfBbu_ClVLUSW3lDiVQdcw.png?1776930959)| | Previous Expires, User Approves New Request![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069762599/original/SuaHRQ2Ky19b0CyRtL5UOpl4LOuRgJWzLQ.png?1776930982)  
---|---|---  
      
    
    No webhook notification is sent when a temporary permission expires. To check the current permission status of a contact at any time, query the **Get Current Call Permission State** endpoint in the WhatsApp Business API.

* * *

✅ Key TakeawaysCall permission is always controlled by the user — you can request it, but you cannot force it. Keep messages clear and relevant, respect the request limits, only call when there is genuine value, and handle unanswered calls carefully. This builds customer trust and keeps your permission status healthy.  
---  
  
##   


## WhatsApp Calling Pricing

WhatsApp Calling rates are charged **per minute** and vary by market. Rates listed below are in **USD** and apply to business-initiated calls. User-initiated (inbound) calls are **free of charge**.

User-Initiated Calls

Free

No charge when customer calls your business

Business-Initiated Calls

Per minute

Rate depends on destination market

### How Calls Are Billed

Businesses are charged for calls based on:

| **Duration of the call** — calculated in **six-second pulses**  
---  
| **Country code** of the phone number being called  
---  
      
    
    **Example:** A 56-second call = 9.33 pulses → rounded up to **10 pulses**.
    Fractional pulses are always counted as one full pulse.

### Call Rates by Market (USD per minute)

Market| Country Code| Currency| Rate per Minute  
---|---|---|---  
Argentina| +54| USD| $0.0106  
Brazil| +55| USD| $0.0113  
Chile| +56| USD| $0.0127  
Colombia| +57| USD| $0.0117  
France| +33| USD| $0.0104  
Germany| +49| USD| $0.0108  
India| +91| USD| $0.0056  
Indonesia| +62| USD| $0.0254  
Israel| +972| USD| $0.0133  
Italy| +39| USD| $0.0127  
Malaysia| +60| USD| $0.0113  
Mexico| +52| USD| $0.0099  
Netherlands| +31| USD| $0.0066  
Pakistan| +92| USD| $0.0125  
Peru| +51| USD| $0.0127  
Russia| +7| USD| $0.0102  
Saudi Arabia| +966| USD| $0.0133  
South Africa| +27| USD| $0.0113  
Spain| +34| USD| $0.0135  
United Arab Emirates| +971| USD| $0.0133  
United Kingdom| +44| USD| $0.0104  
Rest of Africa| Various| USD| $0.0108  
Rest of Asia Pacific| Various| USD| $0.0120  
Rest of Central & Eastern Europe| Various| USD| $0.0100  
Rest of Latin America| Various| USD| $0.0122  
Rest of Middle East| Various| USD| $0.0133  
Rest of Western Europe| Various| USD| $0.0108  
Other| Various| USD| $0.0139  
Egypt| +20| USD| N/A  
Nigeria| +234| USD| N/A  
Turkey| +90| USD| N/A  
North America (US & Canada)| +1| USD| N/A  
      
    
     User-Initiated Calling
    Available in **every location where Cloud API is available**. No country restrictions apply.
    
     Business-Initiated Calling
    
    Your business can call customers in most countries. However, calling is **not available** if your business phone number is registered in any of these countries:

|  United States  
---  
Canada  
Egypt  
| |  Vietnam  
---  
Nigeria  
  
  


  


**Note:** The country restriction applies to your **business phone number**. Your customers can be located in any country where WhatsApp is supported.

Frequently Asked QuestionsCommon questions about WhatsApp Calling  
---  
❓ Can I make WhatsApp calls from a desktop browser?Yes. When configuring staff user settings, you can set the **Default Channel for WhatsApp Calls** to **Web App** , which allows calls to be handled directly from the CRM browser interface.  
---  
❓ Do I need customer permission before making a call?Yes. WhatsApp requires **explicit customer approval** before your business can initiate an outbound call. Inbound calls from customers do not require prior permission.  
---  
❓ How long does call permission last?Temporary permission lasts **7 calendar days (168 hours)**. Permanent permission does not expire. If the customer does not respond to a request, it expires after **7 days**.  
---  
❓ How many permission requests can I send to the same customer?**1 request every 24 hours** , maximum **2 requests within a 7-day period**. These limits reset when any connected call is made between your business and the user.  
---  
❓ Is WhatsApp Calling available in my country?WhatsApp Calling is available in most countries. It is currently **not supported** in the United States, Canada, Turkey, Egypt, Vietnam, and Nigeria.  
---  
❓ What happens if I miss an inbound WhatsApp call?If a call goes unanswered, the customer can request a callback if you have enabled **Allow People to Request Callback for Missed Calls**. The missed call is also logged in the customer's conversation.  
---  
❓ Can multiple team members receive the same inbound call?Yes. In **Ring WhatsApp Calls To** , you can assign a **primary user** who rings first and add additional team members as backup. If the primary user does not answer, the call routes to the next assigned user.  
---  
❓ Can a customer revoke call permission?Yes. Customers can revoke permission at any time by opening the WhatsApp chat, tapping the **business profile name** , going to **Business Calling Permissions** , and disabling call access.  
---  
❓ What is a call disposition and why should I use it?A call disposition is an **outcome tag** you add after a call — for example, _Resolved_ , _Follow-up Required_ , or _No Answer_. It keeps records accurate and makes follow-ups easier to track.  
---  
❓ What happens after 4 consecutive unanswered calls?After **2 unanswered calls** , WhatsApp sends the user a system message prompting them to reconsider. After **4 unanswered calls** , call permission is **automatically revoked** by WhatsApp.  
---  
❓What happens if permission is auto-revoked?If a customer does not answer 4 consecutive outbound calls, WhatsApp automatically revokes calling permission. You will need to request permission again to place future calls.  
---

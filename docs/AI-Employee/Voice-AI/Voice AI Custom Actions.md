# Voice AI Custom Actions

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005461-voice-ai-custom-actions](https://help.gohighlevel.com/support/solutions/articles/155000005461-voice-ai-custom-actions)  
**Category:** AI Employee  
**Folder:** Voice AI

---

This article explains how to use Voice AI Custom Actions to send real-time POST webhook requests during live calls. Custom Actions allow Voice AI agents to interact with external systems mid-conversation, such as looking up data, sending information, or triggering external processes before the call ends.

* * *

**TABLE OF CONTENTS**

  * What are Voice AI Custom Actions?
  * Key Benefits of Voice AI Custom Actions
  * Voice AI Conversation Triggers
  * Webhook Custom Action
  * Dynamic Parameter Collection
  * How to Set Up Voice AI Custom Actions
    * Step 1: Navigate to your Voice AI Agent
    * Step 2: Create Custom Action
    * Step 3: Configure Custom Action
  * Voice AI - Real-time Testing
  * Frequently Asked Questions
  * Related Articles


* * *

# **What are Voice AI Custom Actions?**

  


Voice AI Custom Actions allow Voice AI agents to send custom POST webhook requests to external APIs during a live conversation. These actions can include webhook URLs, headers, authentication, and dynamic parameters collected from the caller in real time. This helps the agent retrieve or send information based on what the caller says during the call.

* * *

## **Key Benefits of Voice AI Custom Actions**

  


Voice AI Custom Actions help Voice AI agents connect with external systems during a live call. This allows the agent to personalize responses, retrieve information, and complete tasks faster.

  


  * Send real-time POST webhook requests based on caller intent or conversation cues.  
  

  * Look up or submit information during the call.  
(Example: If a caller asks, “What’s the status of my recent order?”, the AI can call your order management system and retrieve the order status without putting the caller on hold.)  
  

  * Configure webhook URLs, headers, and authentication.  
  

  * Pass dynamic call data, such as phone numbers, email addresses, dates, or order IDs.  
  

  * Test webhook requests and responses before saving the action  
  

  * Reduce manual follow-up by resolving more requests during the call.


* * *

## **Voice AI****Conversation Triggers**

  


Conversation triggers define when a Custom Action should run during a call. A trigger can be based on what the caller says, the information they provide, or the intent detected by the Voice AI agent.

  


**Example triggers:**

  


  * When a caller says, “I want to check my appointment.”  
  

  * When the caller provides an email address.  
  

  * When the caller provides a string of digits, such as an order number, booking ID, or account number.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755629/original/vgHTKbSkl3-K92KksuOOFk68vYIqwNYOkw.png?1760133377)

* * *

## **Webhook Custom Action**

  


Webhook integration is the core of Voice AI Custom Actions. It allows your Voice AI agent to interact with external systems that support API requests, such as CRMs, scheduling tools, databases, order management systems, and other business applications.

  


Each Custom Action is defined by a POST request, which may include:

  


  * A webhook endpoint URL  
  

  * Headers, such as API keys or tokens  
  

  * Authentication, such as Bearer token or Basic Auth  
  

  * A request body with dynamic parameters collected during the call


  


Example: If you are integrating with a CRM, your webhook URL might target an endpoint such as `/api/v1/lookupContact` and include parameters like the caller’s email address or phone number.

  


**Example:** If you’re integrating with a CRM like Salesforce, your webhook URL might target an endpoint like /api/v1/lookupContact and include parameters like the contact’s email or phone number.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755818/original/0AnIb0Kcut2JhaBPtg13Hc2HJYhgfZpu7A.png?1760134023)

* * *

## **Dynamic Parameter Collection**

  


Voice AI can extract and label relevant information during a live conversation. These values can be assigned to parameters in the webhook request body. This is useful when the AI needs to collect details like an order number, email address, phone number, or appointment date before sending the webhook request.

  


**Supported data types:**

  


  * Text / String
  * Number / Numeric
  * Email
  * Phone Number
  * Date


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755787/original/ce1pQwudBZ1h7MA3OKbJUXB1XQna-sm0fA.png?1760133816)

* * *

## **How to Set Up Voice AI Custom Actions**

  


Voice AI Custom Actions can be configured from the Voice AI Agent interface with just a few steps. Here’s how to get started:

  


  


### _**Step 1:** Navigate to your Voice AI Agent_

  


Navigate to **Voice AI > Agent Goals > Switch to Advanced Mode (_If not already enabled_) > Custom Actions**.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055756037/original/ZDxjDk2l3UtR29agJ99VMgLzn8fPCh3gSg.gif?1760134862)

  


  


### _**Step 2:** Add a Custom Action_

  


In the Setup your Actions section, click Custom Action to open the custom action configuration window.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755970/original/L86KAuL1cDyz8H2y8lY-p93YQNZgVNIgQw.jpeg?1760134618)  


  


### _**Step 3:** Configure the Custom Action_

  


Enter the required Custom Action details. Some fields may be optional depending on your webhook setup.

  


  1. Enter a name for the Custom Action.  
  

  2. Set the conversation trigger conditions.  
  
Example: If a caller asks to “check my account balance,” you can set a trigger for that request and define a phone number parameter to pass into your external API.  
  

  3. Add your webhook URL.  
  

  4. Confirm that the request method is POST.  
  

  5. Add any required headers.  
  

  6. Enter authentication details if required, such as a Bearer token or Basic Auth.  
  

  7. Define the dynamic parameters that should be collected from the conversation.  
  

  8. Use the Test Webhook feature to validate the setup before saving.  
  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055756544/original/nF_csn19zfxSMnNRhz8aoPEHn3sVJIkc_Q.jpeg?1760136422)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055756461/original/QakH6lkuv8dghp6PziRjzkrBE7VA8QnEpw.png?1760135971)

* * *

## **Voice AI -****Real-time Testing**

  


Before saving a Custom Action, use the built-in Test Webhook tool to validate the request and response. This allows you to pass test data, review the webhook request, and confirm that your external system returns the expected response.

  


**You’ll be able to:**

  


  * Review the full request, including headers and body.  
  

  * View the raw response from the webhook, such as 200 OK, 400 Bad Request, or 404 Not Found.  
  

  * Confirm that the returned data can be used by the Voice AI agent during the call.  
  

  * Identify and fix configuration issues before saving.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055756518/original/QnD2obzf89LBLKjkEbmtslKhe45Euau57g.png?1760136257)

* * *

## **Frequently Asked Questions**

  


**Q: Can I use GET or other request types?**

No, only POST requests are currently supported for Custom Actions.

  


**Q: Where do I access Voice AI Custom Actions?**

You can access Custom Actions by going to **AI Agents > Voice AI**, then creating or editing a Voice AI agent. In the agent setup area, go to Setup your Actions and select Custom Action.

  


**Q: Is authentication supported in webhooks?**

Yes, you can use Bearer tokens, Basic Auth, or pass keys in headers.

  


**Q: What if my webhook fails during the call?**

The system logs the failure. You can define fallback behavior for cases where no data is returned, the request fails, or the webhook times out.

  


**Q: Can I trigger multiple webhooks during a single call?**

Yes. Each Custom Action can be triggered independently based on its own conditions.

  


**Q: Do I need a developer to set up these actions?**

Not always. Basic webhook setups may be configured by users who have the external system’s API documentation. More advanced use cases, authentication requirements, or custom payloads may require help from a developer.

  


**Q: What request method is supported?**

Custom Actions currently support POST requests.

* * *

### **Related Articles**

  


  * [AI Voice Agents Overview](<https://help.gohighlevel.com/en/support/solutions/articles/155000003911>)  
  

  * [Creating Voice AI Agents](<https://help.gohighlevel.com/en/support/solutions/articles/155000004107>)  
  

  * [Working Hours for AI Employee](<https://help.gohighlevel.com/en/support/solutions/articles/155000004139>)  
  

  * [Inbound Call Flow for Voice AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000003431>)  
  

  * [Voice AI Custom Actions](<https://help.gohighlevel.com/en/support/solutions/articles/155000005461>)

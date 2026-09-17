# WhatsApp: Customer Service Window Check

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003235-whatsapp-customer-service-window-check](https://help.gohighlevel.com/support/solutions/articles/155000003235-whatsapp-customer-service-window-check)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# WhatsApp: Customer Service Window Check

Use this workflow condition to send free-form WhatsApp messages at no cost within the 24-hour service window

Table of Contents

  * • Prerequisite for Using WhatsApp Under Workflows
  * • What Are Conversations
  * • Marketing, Utility & Authentication Conversations
  * • Service Conversations
  * • What Is a Customer Service Window
  * • Free Tier Conversations
  * • How to Use WhatsApp: Customer Service Window Check
  * • FAQs


In this article, we discuss how the **WhatsApp: Customer Service Window Check** condition can be used to create automated workflows and send free-form messages. This powerful condition lets you determine whether an active Customer Service Window is open between your business and your customer. When the window is open, you can send unlimited free-form messages at no cost for the first 1,000 service conversations each month.

* * *

## Prerequisite for Using WhatsApp Under Workflows

WhatsApp needs to be subscribed and enabled on the location account. Refer to this article for setting up WhatsApp on your sub-account: [WhatsApp Sub-Account Setup](<https://help.gohighlevel.com/a/solutions/articles/155000001980?portalId=48000045315#Subaccount-Setup>).

Additionally, if you want to send business-initiated conversations, ensure you have an approved template in place: [How to Create a WhatsApp Template](<https://help.gohighlevel.com/support/solutions/articles/155000000861-how-to-create-a-whatsapp-template->).

## What Are Conversations

Conversations are 24-hour message threads between you and your customers and are the basis for pricing. Conversations can be opened by sending either free-form messages or template messages.

Conversations are opened when you send a message to a customer under the following conditions.

### 1\. Marketing, Utility, and Authentication Conversations

When you send an approved marketing, utility, or authentication template to a customer, we check if an open conversation matching the template's category already exists between you and the customer. If one exists, no new conversation is opened. If one does not exist, a new conversation of that category is opened, lasting 24 hours.

For example:

  * **Hour 0:** You send a targeted promotion (marketing template message) to a customer. No open marketing conversation exists, so a marketing conversation lasting 24 hours is opened.
  * **Hour 4:** The customer completes an order on your site, so you send an order confirmation (utility template message). No open utility conversation exists, so a utility conversation lasting 24 hours is opened.
  * **Hour 10:** You send a shipment confirmation (utility template message). An open utility conversation already exists, so a new one is not opened.


### 2\. Service Conversations

A service conversation is opened when any message other than a template message is delivered to your customer and no open conversation of any category exists between you and the customer.
    
    
    Note: A customer service window must exist between you and the customer before you can send them a non-template message.

For example:

  * **Hour 0:** You send a targeted promotion (marketing template) to a customer. No open marketing conversation exists, so a marketing conversation lasting 24 hours is opened.
  * **Hour 4:** The customer messages you. This opens a customer service window, allowing you to send them any type of message for the next 24 hours.
  * **Hour 5:** You send an interactive list message. An open conversation already exists (the marketing conversation), so a service conversation is not opened.
  * **Hour 24:** The marketing conversation expires.
  * **Hour 25:** The 24-hour customer service window is still open, so you send a second text message. No open conversation exists anymore, so a service conversation is opened, lasting 24 hours.
  * **Hour 26:** The 24-hour customer service window is still open, so you send a third text message. An open service conversation already exists, so a new one is not opened.


## What Is a Customer Service Window

When a WhatsApp user messages you, a 24-hour timer called a customer service window starts, or refreshes.

## Free Tier Conversations

Each WhatsApp Business Account gets 1,000 free service conversations each month across all of its business phone numbers. This number refreshes at the beginning of each month, based on the WhatsApp Business Account time zone.

Marketing, utility, and authentication conversations are not part of the free tier.

* * *

## How to Use WhatsApp: Customer Service Window Check

To send free-form messages to your customers, you first need to verify if the customer service window is open. If it is, you can proceed with sending the free-form message. Responding to a customer's inbound message automatically opens a service conversation. You can initiate up to 1,000 free service conversations each month, helping you reduce your messaging costs.

1

Go to **Automations > Workflows > Create Workflow > Start from Scratch**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032110933/original/dhgXLmbZK6BUiWao0efgrITVnawa0U_GYA.png?1725326485)

2

Click the plus button to add an action, then select **WhatsApp: Customer Service Window Check**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032064326/original/5Wu83WCEBufxxBUQgacV5vC9YJg-2iHmGg.png?1725273049)

3

Choose the conversation's phone number.
    
    
    Note: If the Customer Service Window is open, you can send unlimited free-form messages. If it is closed, you need to send a Marketing or Utility template to start a conversation with the customer.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042687784/original/VUBA4yUfCv94WiHMIdMfffm98Q4CejeT7w.png?1741171907)

4

Under the **Open** branch, select the **WhatsApp** action and set the template to **None – Free form message**.
    
    
    Note: If the customer service window is open, you can send unlimited free-form messages to the customer. Each WABA account gets 1,000 free service conversations every month, meaning you can send these messages for free until your 1,000 service conversations are used up.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032078204/original/D2yDApfBewDZk7TVW8zQWpw4YGPI0Npmmg.png?1725280992)

5

Under the **Closed** branch, select the **WhatsApp** action and choose a marketing or utility template to initiate the conversation with the customer.
    
    
    Note: If the customer service window is closed, meaning there is no customer reply in the last 24 hours, you can only send WhatsApp marketing or utility templates.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032078337/original/saR0wa8LHzRlSZusnI7D512Lz24k-tpjdQ.png?1725281089)

* * *

## FAQs

Q. What's the difference between "None – Free form message" and selecting a template when sending WhatsApp messages in workflows?

"None – Free form message" lets you write a free-form message within the 24-hour customer service window. Selecting a template is for sending pre-approved messages, useful for starting conversations outside the 24-hour window or for specific marketing or support purposes.

Q. Where can I check my free tier conversation count?

Go to [Facebook Business Manager](<https://business.facebook.com/wa/manage/insights/>), select your WhatsApp account, then go to Account Tools > Insights.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032110899/original/ZW0QUfhwK2gkSe_4GcLJutkU6GC4dCVO1Q.png?1725326249)

Q. Can I create workflows that combine WhatsApp with other channels like SMS or Email?

Yes. CRM workflows are flexible, allowing you to combine WhatsApp with other communication channels to create comprehensive automation sequences.

Q. Can I use WhatsApp workflow automation to send messages outside the 24-hour customer service window?

Yes, you can use approved WhatsApp templates after the 24-hour customer service window is closed, for outreach or follow-up messages. Keep in mind that these template-based messages will incur additional charges.

Q. What's a "Free Entry Point Conversation" and how is it different from a regular conversation?

  * Triggered when a customer clicks a "Click to WhatsApp" ad or a Facebook Call-to-Action button.
  * Lasts for 72 hours, compared to the standard 24-hour window.
  * During this extended window, you can send both free-form and template messages.

# Workflow Action - AI Email Parser

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008742-workflow-action-ai-email-parser](https://help.gohighlevel.com/support/solutions/articles/155000008742-workflow-action-ai-email-parser)  
**Category:** Workflows  
**Folder:** Workflow AI Workflow Actions

---

HighLevel's **Email Parser** workflow action uses AI to extract structured data from inbound emails for use in your automations. This article shows how to configure the action, define the data to extract, and use those values in downstream workflow steps.

  

    
    
    **Note:** AI Email Parser is a **premium** **workflow** **action** and **incurs** **additional** **charges** per execution.
    

* * *

**TABLE OF CONTENTS**

  * What is the AI Email Parser Action?
  * Key Benefits of the AI Email Parser Action
  * How To Use the AI Email Parser Action
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is the AI Email Parser Action?**

  


The AI Email Parser is a workflow action designed specifically to turn information contained in emails into structured workflow data. This makes it easier to automate processes that begin with emails from lead providers, inquiry forms, appointment systems, order notifications, or other external sources.

  


The action reads the email that triggered the workflow, identifies the information you specify, and makes the extracted values available to downstream workflow actions.

  


For example, a real estate lead notification could contain a prospect's name, email address, phone number, and inquiry. Email Parser can extract those values and then automatically create the contact and begin follow-up.

* * *

## **Key Benefits of the AI Email Parser Action**

  


  * **Purpose-built email parsing:** Extract structured information from inbound emails without configuring the broader AI Extract Data action for this specific use case.  
  

  * **Pre-built extraction templates:** Start with common use cases such as New Lead, Order Details, Inquiry, and Appointment.  
  

  * **Custom data extraction:** Define additional information you want AI to identify from the email.  
  

  * **Multiple data types:** Extract values as Text, Email, Phone Number, Date, Date and Time, URL, or Boolean fields.  
  

  * **Reusable workflow outputs:** Use parsed values in actions such as Create Contact, Send Email, Send SMS, opportunity actions, notifications, assignments, and other workflow steps.  
  

  * **Flexible email content selection:** Parse the latest email message, the full email thread, or a custom value depending on your workflow.


* * *

## **How To Use the AI Email Parser Action**

  


A properly configured workflow ensures that the correct incoming emails trigger the automation and that Email Parser receives enough context to extract reliable structured data. The following example uses an inbound real estate lead notification and creates a contact from the parsed information.

  


**Before you begin:**

  


  * Make sure you know which mailbox or email flow should trigger the workflow.  
  


  * Decide which values you want to extract from the email.  
  


  * Decide where those extracted values should be stored or used after extraction.


  

    
    
    **Note:** AI email parser action requires Inbound email trigger to be present. 

  


### ** _Step 1:_**_Create a new workflow_

  


  1. Go to **Automation** > **Workflows**.  
  


  2. Click **\+ Create Workflow**.  
  


  3. Choose **Start from Scratch**.  
  


  4. Select **Standard Builder or Advanced Builder** as per your preference.


  


![](https://jumpshare.com/share/d2BdXJDO3sLLJUZ0ip3P+/GIF+Recording+2026-07-03+at+18.01.03.gif)

  


  


### **_Step 2:_**_Add the email trigger_

  

    
    
    **Note:** For complete trigger behavior and email configuration requirements, see [Workflow Trigger - Inbound Email](<https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email>).

  


  1. Click **\+ Add New Trigger**.  
  


  2. Select **Inbound Email**.  
  


  3. Configure the trigger based on the mailbox or email pattern you want to monitor.  
  


  4. Use filters such as:  
  


     * **Email Sent To Mailbox**

     * **Email Sent From**

     * **Subject**

     * **Body Plain Text**

     * **Has Attachments**  
  


  5. In **Advanced Settings** , choose whether the workflow should run only for a new email conversation.  
  


  6. For example, if lead notification emails consistently contain a phrase such as "New Buyer Lead," you can configure **Body Plain Text > Contains** and enter that phrase. You can also filter by the sender's email address when notifications always come from the same source.

  


To prevent replies in an existing thread from triggering the workflow again, enable **Trigger Only for New Email Conversations**. When enabled, only the first email that begins a new conversation triggers the workflow.

  


  7. Click **Save Trigger**.


  


![](https://jumpshare.com/share/iNckpBfLhtAz9ZAIGauw+/GIF+Recording+2026-07-03+at+18.10.17.gif)

  


  


### _**Step 3:** Add the Email Parser Action_

  


  1. Click the **+** icon below the trigger.  
  

  2. Search for **Email Parser**.  
  

  3. Select **Email Parser** under **AI Actions**.


  


**![](https://jumpshare.com/share/RlbXuLXYtyz1f603vlRI+/GIF+Recording+2026-09-14+at+16.56.43.gif)**  


  


### _**Step 4:** Configure the Action_

  


  1. Enter or update the **Action Name** if needed.  
  

  2. Under **Email Content** , select the content the AI should parse:  
  
**The AI reads the email that triggered this workflow. With Body or Full body, the subject line is included by default. If you choose a "Custom Value', the AI reads that value instead, and it may not be an email.**  
  

     * **Body** for the latest email message.  
  

     * **Full Body** when the reply thread should also be analyzed.  
  

  3. Use the **About This Email** field to tell the AI what type of email it is analyzing.  
  
**For example:** `New buyer lead notification from a real estate lead provider.`  
  
Keep the description short and specific so the AI has useful context for the extraction.


  
![](https://jumpshare.com/share/ZeU98BFW0hS5Y7SNBjBG+/GIF+Recording+2026-09-14+at+17.00.40.gif)  
  


### _**Step 5:** Configure the Fields to Extract_

  


  1. Under **Fields to Extract** , select a pre-built template: New Lead, Order Details, Inquiry, Appointment.  
  

  2. Using **New Lead** for this example.  
  

  3. Configure the information that should be extracted, such as:  
  

     * Name
     * Email
     * Phone
     * Message  
  

  4. Select the correct data type for each field.  
  

  5. Add a short description explaining what information the field should contain.  
  

  6. Click **Add Data** if additional fields are required.  
  

  7. Click **Save Action** when finished.


  
When an email matching the Inbound Email trigger enters the workflow, Email Parser will analyze the selected content and return the configured values.

  


![](https://jumpshare.com/share/ZicqXlj8xhawE07iH22Q+/GIF+Recording+2026-09-14+at+17.06.22.gif)

  
  


### **_Step 6:_**_Add a Downstream Action to Store or Use the Extracted Values_

  

    
    
    **Important:** AI Email Parser **does not permanently store the extracted values by itself**. The extracted **values are only available inside the workflow through the custom value picker in later actions**. If you do not add another action after AI Extract Data, the extracted data will not be saved to a contact, opportunity, or any other record.
    

  


  1. Common next actions include:  
  

     * **Create Contact**
     * **Update Contact Field**
     * **Create Opportunity**
     * **Create/Update Opportunity**
     * **Internal Notification**
     * **Send Email/SMS**  
  

  2. In **Create Contact** or **Update Contact Field** , map each destination field to the corresponding value from **AI Extract Data** in the custom value picker.  
  

  3. If you want to create or update an opportunity, map relevant extracted values such as budget, service type, or job details into the correct opportunity fields.  
  


![](https://jumpshare.com/share/Ekk8smrN1hKfCgfGLoJm+/GIF+Recording+2026-09-14+at+17.10.06.gif)

  
  


### _**Step 7:** Add Follow-Up Actions_

  


Once the email has been parsed and the information is available in the workflow, you can continue the automation based on your business process.

  


Examples include:

  


  * Send an email
  * Send an SMS
  * Create or update an opportunity
  * Send an internal notification
  * Assign the lead to a user
  * Trigger another workflow
  * Start another automated follow-up process


  


For example, after creating the contact, you could immediately add a **Send Email** action to acknowledge the inquiry.

  


**![](https://jumpshare.com/share/bfzq1uIDOawkZ6JCvJuG+/Screen+Shot+2026-09-14+at+17.16.38.png)**

* * *

## **Frequently Asked Questions**

  


**Q: What is the difference between AI Email Parser and AI Extract Data?  
****AI Email Parser** is purpose-built for extracting structured information from emails, while **AI Extract Data** is a more general action that can extract data from emails, SMS content, we-bhook payloads, AI outputs, and other text-based inputs. Use Email Parser when your workflow is specifically focused on email parsing, and use AI Extract Data when you need more flexibility across different types of content.

  


**Q: Does Email Parser require an Inbound Email trigger?**  
For the standard email-parsing workflow described in this article, the Inbound Email trigger provides the email that Email Parser analyzes. Email Parser can also analyze a custom value when that option is selected.

  


**Q: Should I use Body or Full Body?**  
Use **Body** when the information you need is contained in the latest message. Use **Full Body** when information elsewhere in the email thread needs to be included in the analysis.

  


**Q: Can I extract fields that are not included in a pre-built template?**  
Yes. You can add additional data fields and define the data type and description for the information you want AI to extract.

  


**Q: Can I use the extracted values in later workflow actions?**  
Yes. The outputs from Email Parser are available through the custom value picker and can be mapped into downstream workflow actions.

  


**Q: How can I prevent replies in the same email thread from repeatedly starting the workflow?**  
Enable **Trigger Only for New Email Conversations** in the Inbound Email trigger. When enabled, replies to an existing email conversation are ignored by the trigger.

* * *

### **Related Articles**

  


  * [How to Parse Emails Using AI Extract Data Action](<https://help.gohighlevel.com/support/solutions/articles/155000008182-how-to-parse-emails-using-ai-extract-data-action>)  
  

  * [Workflow Trigger - Inbound Email](<https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email>)  
  

  * [Workflow Action - AI Extract Data](<https://help.gohighlevel.com/support/solutions/articles/155000007992>)  
  

  * [Workflow Action - Create Contact](<https://help.gohighlevel.com/support/solutions/articles/155000002685>)  
  

  * [Workflow Action - Send Email](<https://help.gohighlevel.com/support/solutions/articles/155000002472-action-send-email>)  
  

  * [Dedicated Email Sending Domains Overview & Setup](<https://help.gohighlevel.com/support/solutions/articles/48001226115-dedicated-email-sending-domains-overview-setup>)

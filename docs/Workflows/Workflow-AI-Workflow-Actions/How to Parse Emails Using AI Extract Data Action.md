# How to Parse Emails Using AI Extract Data Action

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008182-how-to-parse-emails-using-ai-extract-data-action](https://help.gohighlevel.com/support/solutions/articles/155000008182-how-to-parse-emails-using-ai-extract-data-action)  
**Category:** Workflows  
**Folder:** Workflow AI Workflow Actions

---

When inbound emails contain lead details, service requests, or other important information in unstructured text, teams often waste time manually copying that data into the CRM. AI Extract Data helps turn email content into structured values that workflows can use right away. This article shows how to parse email data in HighLevel workflows, store the extracted values using a follow-up action, and then use that data for automation.

  

    
    
    **Note:** AI Extract Data is a **premium** **workflow** **action** and **incurs** **additional** **charges** per execution.

* * *

**TABLE OF CONTENTS**

  * What is Email Parsing Using the AI Extract Data Action?
  * Key Benefits of Email Parsing with AI Extract Data Action
  * How To Parse Email Data Using AI Extract Data Action
  * Use Case
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Email Parsing Using the AI Extract Data Action?**

  


Email parsing with AI Extract Data allows HighLevel to read inbound email content and pull out specific details such as a lead's name, email address, phone number, budget, service request, or other structured information. This makes it easier to convert unstructured email text into workflow-ready values without manual copying. Once the values are extracted, you can use later workflow actions to create or update records, trigger follow-ups, and notify your team.

  


AI Extract Data is especially useful when emails come from lead sources, marketplaces, referrals, or external systems that do not send information in a clean CRM format.

* * *

## **Key Benefits of Email Parsing with AI Extract Data Action**

  


  * **Faster lead handling** : Capture important details from inbound emails automatically so your team can follow up sooner.  
  


  * **Less manual entry** : Reduce copy-and-paste work by extracting structured values directly from email content.  
  


  * **More consistent data capture** : Map extracted values into contact or opportunity fields for cleaner records.  
  


  * **Better workflow automation** : Use parsed values in later actions such as contact creation, opportunity creation, notifications, emails, calls, or SMS.  
  


  * **More flexible intake processes** : Support use cases where valuable information arrives by email instead of forms or direct CRM entry.


* * *

## **How To Parse Email Data Using AI Extract Data Action**

  


A complete email parsing workflow does more than extract values from an email. To make the extracted data useful, the workflow must also store or use those values in a later action such as Create Contact, Update Contact Field, or Create Opportunity.

  

    
    
    **Note:** To learn more about how the AI Extract Data action works and understand the action in more detail, see [Workflow Action - AI Extract Data](<https://help.gohighlevel.com/support/solutions/articles/155000007992-workflow-action-ai-extract-data>).

  


**Before you begin:**

  


  * Make sure you know which mailbox or email flow should trigger the workflow.  
  


  * Decide which values you want to extract from the email.  
  


  * Decide where those extracted values should be stored or used after extraction.  
  


  * Keep in mind that AI Extract Data is a premium workflow action and incurs additional charges per execution.


  


### **_Step 1:_**_Create a new workflow_

  


  1. Go to **Automation** > **Workflows**.  
  


  2. Click **\+ Create Workflow**.  
  


  3. Choose **Start from Scratch**.  
  


  4. Select **Standard Builder or Advanced Builder** as per your preference.


  


![](https://jumpshare.com/share/d2BdXJDO3sLLJUZ0ip3P+/GIF+Recording+2026-07-03+at+18.01.03.gif)

  


  


### **_Step 2:_**_Add the email trigger_

  

    
    
    **Note:** You can also use **Customer Replied** with the reply channel set to **Email** if your use case depends on replies instead of newly received inbound emails.
    

  


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


  


![](https://jumpshare.com/share/iNckpBfLhtAz9ZAIGauw+/GIF+Recording+2026-07-03+at+18.10.17.gif)

  


  


### **_Step 3:_**_Add the AI Extract Data action_

  


  1. Click the **+** icon under the trigger.  
  
![](https://jumpshare.com/share/8IlHbwUlIP0TTgFXCL8x+/Screen+Shot+2026-07-03+at+18.15.37.png)  
  


  2. Search for and select **AI Extract Data**.  
  
![](https://jumpshare.com/share/aB21vBl6HJ4oEiXeqKxy+/Screen+Shot+2026-07-03+at+18.18.19.png)  
  


  3. **Rename** the **action** if needed so the workflow is easy to understand.  
  
![](https://jumpshare.com/share/tO6ZKQBmL2EFF8klliig+/Screen+Shot+2026-07-03+at+19.40.27.png)  
  


### **_Step 4:_**_Choose the email content to extract from_

  


  1. In Extract From, open the **custom value picker**.  
  


  2. Go to **Inbound Email**.  
  


  3. Select the email content you want to parse. Common options include:  
  


     * **Body Plain Text**

     * **Full Body Includes Reply Thread**

     * **Subject**

     * **Message ID**

     * **From Email**

     * **From Name**

     * **CC**

     * **Date**


  


![](https://jumpshare.com/share/iACr6EbxL0HvDgiw1HCf+/GIF+Recording+2026-07-03+at+18.26.17.gif)

  


  


### ** _Step 5:_**_Add Additional Context to improve extraction accuracy_

  


  1. Use **Additional Context** to explain what kind of email the action should expect.  
  


  2. Add details that help the AI identify the correct values.  
  
**Example Additional Context:** "Inbound lead email from platforms like Zillow or Realtor.com. Extract the lead's name, email, phone number, budget, and property interest. Phone numbers may appear in plain text."  
  
This is especially useful when the email format varies or when certain values may be labeled differently from one sender to another.  
  


  3. You can also add **custom values**.


  


![](https://jumpshare.com/share/3xdy5hc8PdGqWpG3i4tY+/Screen+Shot+2026-07-03+at+18.28.53.png)

  


  


### **_Step 6:_**_Define the data you want to extract_

  


  1. Use a pre-built template if it helps you get started, such as:  
  


     * **Contact Info**

     * **Opportunity Info**

     * **Order Info**

     * **Appointment Info**  
  


  2. After applying a template, edit the fields so they match your use case.  
  


  3. Add, remove, or rename fields as needed.  
  


  4. **Example fields for a lead notification email:**  
  


     * Lead Name

     * Contact Email

     * Contact Phone

     * Budget  
  


  5. Choose field names that match the data you want to store later. This makes downstream mapping easier and more accurate.  
  


  6. Click **Save Action**.  


  


![](https://jumpshare.com/share/FNflsiEp7iFzsPc5dqlz+/GIF+Recording+2026-07-03+at+19.43.41.gif)

  


  


### **_Step 7:_**_Add a downstream action to store or use the extracted values_

  

    
    
    **Important:** AI Extract Data does not permanently store the extracted values by itself. The extracted values are only available inside the workflow through the custom value picker in later actions. If you do not add another action after AI Extract Data, the extracted data will not be saved to a contact, opportunity, or any other record.
    

  


  1. Common next actions include:  
  

     * **Create Contact**
     * **Update Contact Field**
     * **Create Opportunity**
     * **Create/Update Opportunity**
     * **Internal Notification**
     * **Send Email/SMS**  
  

  2. In **Create Contact** or **Update Contact Field** , map each destination field to the corresponding value from **AI Extract Data** in the custom value picker.  
  

  3. If you want to create or update an opportunity, map relevant extracted values such as budget, service type, or job details into the correct opportunity fields.  


  


![](https://jumpshare.com/share/7musNYUnP6MkBRxNXExA+/GIF+Recording+2026-07-03+at+19.47.11.gif)

  


  


### **_Step 8:_**_Add any follow-up actions you need_

  


  1. After the values are stored, you can continue the workflow with additional actions such as:  
  

     * Sending an internal notification to a teammate  
  

     * Sending an email or SMS follow-up  
  

     * Assigning the lead for follow-up  
  

     * Creating or updating an opportunity  
  

     * Triggering another workflow based on the updated contact or opportunity data


  


![](https://jumpshare.com/share/q6iyDxUZgLmo6UrO8Y8w+/Screen+Shot+2026-07-03+at+18.55.45.png)

* * *

## **Use Case**

  


### **Real Estate Lead Notifications**

  


Real estate teams often receive lead notifications from listing platforms and referral sources by email. Those emails usually contain valuable details such as the lead's name, phone number, email address, budget, and property interest, but the information may appear in unstructured text. Parsing those emails with AI Extract Data helps agents capture the details faster and start follow-up without waiting on manual entry.

  


**Example use case**

  


  1. A real estate team receives lead notification emails from external platforms.  
  


  2. The workflow triggers when the email reaches the assigned mailbox.  
  


  3. AI Extract Data parses the lead details from the email body.  
  


  4. A downstream action creates the contact or opportunity.  
  


  5. The workflow then sends an internal notification so a team member can follow up quickly.


  


![](https://jumpshare.com/share/52ozGEjWlmC1td2RIQ6D+/Screen+Shot+2026-07-03+at+19.00.33.png)

* * *

## **Frequently Asked Questions**

  


**Q: Does AI Extract Data store the extracted values automatically?**  
No. The extracted values are only available in later workflow actions through the custom value picker. To save them permanently, add another action such as Create Contact, Update Contact Field, or Create Opportunity.

  


**Q: Which trigger should I use for email parsing?**  
Use **Inbound Email** when the workflow should run when a new email reaches a mailbox. Use **Customer Replied** with the reply channel set to **Email** when the workflow should run from an email reply event.

  


**Q: What should I choose in the Extract From field?**  
For most email parsing workflows, use an inbound email value such as **Body Plain Text** or **Full Body Includes Reply Thread**. The best option depends on whether you want to parse only the current message or a larger email thread.

  


**Q: Why should I add Additional Context?**  
Additional Context helps the AI understand what kind of email it is parsing and which values matter most. This can improve extraction accuracy, especially when the email format varies.

  


**Q: Can I use parsed email data to create an opportunity?**  
Yes. After extracting the data, you can create or update an opportunity using the relevant values. In many workflows, the cleanest setup is to create or update the contact first and then create the opportunity.

  


**Q: Do I need to use a template in AI Extract Data?**  
No. Templates can help you start faster, but you can edit the template fields or build the extraction fields manually to fit your use case.

* * *

### **Related Articles**

  


  * [Workflow Action - AI Extract Data](<https://help.gohighlevel.com/support/solutions/articles/155000007992-workflow-action-ai-extract-data>)  
  


  * [Workflow Trigger - Inbound Email](<https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email>)  
  


  * [Workflow Trigger - Customer Replied](<https://help.gohighlevel.com/support/solutions/articles/155000002677-workflow-trigger-customer-replied>)  
  


  * [Workflow Action - Create Contact](<https://help.gohighlevel.com/support/solutions/articles/155000002685-workflow-action-create-contact>)  
  


  * [Workflow Action - Update Contact Field](<https://help.gohighlevel.com/support/solutions/articles/48001214441-workflow-action-update-contact-field>)  
  


  * [Workflow Action - Create Opportunity](<https://help.gohighlevel.com/support/solutions/articles/155000004752-workflow-action-create-opportunity>)

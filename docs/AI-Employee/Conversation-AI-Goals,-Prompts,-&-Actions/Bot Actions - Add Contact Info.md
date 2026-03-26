# Bot Actions - Add Contact Info

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004097-bot-actions-add-contact-info](https://help.gohighlevel.com/support/solutions/articles/155000004097-bot-actions-add-contact-info)  
**Category:** AI Employee  
**Folder:** Conversation AI - Goals, Prompts, & Actions

---

The **Add Contact Info** feature allows users to easily add contact information directly from the AI conversation. By capturing information like business details, addresses, and dates directly from the contact’s responses, you can reduce manual data entry and keep contact records update. 

* * *

**TABLE OF CONTENTS**

  * What is the Add Contact Info Bot Action?
  * Key Benefits of the Add Contact Info Action
  * How To Set up the Add Contact Info Action
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is the Add Contact Info Bot Action?**

  


The **Add Contact Info** bot action helps you collect important details during a Conversation AI chat and automatically save them to the contact record. This makes it more efficient to maintain accurate and up-to-date information about your customers and leads.

  

    
    
    **Important:** This feature only updates the empty fields in a contact information. Contact's email and phone are automatically updated so this action is not required for adding or updating email or phone.

  

    
    
    **Tip:** After saving contact info, explicitly ask the customer for their contact details in the bot’s prompt. If this instruction isn't included in the prompt, the bot will not ask for the required information, and the contact field won't be updated.

* * *

## **Key Benefits of the Add Contact Info Action**

  


  * **Faster Data Capture:** Collect details like address, business info, or date of birth as part of a natural conversation.  
  


  * **Cleaner CRM Records:** Save information directly to the contact profile so your team doesn’t need to re-type it.  
  


  * **Better Personalization:** Use captured details to tailor responses, follow-ups, and appointment flows.  
  


  * **Flexible Fields:** Update both standard fields and supported custom field types for your specific use case.


* * *

## **How To Set Up the Add Contact Info Action**

  


  


####  _**Step 1:** Open the Agent_

  


Navigate to**AI Agents** > **Conversation** **AI** > **Agents** **List**. Open the agent you would like to edit.  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066406893/original/C5Nk7Rgv033kTT-VlvkhtqyMilhZ_UclVA.png?1772833791)**

  


  


#### _**Step 2:** Open Bot Goals_

  


Once the agent is open, select the **Bot Goals** tab.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066406906/original/ME_6LQl4tJAW0tt4sXRMkHReNCI2pGZWkQ.png?1772833891)

  


  


#### _**Step 3:** Select Contact Info_

  


Scroll down to the **Setup your Actions** section. Choose **Contact Info**.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066406925/original/9GMyHVOHGIhx4eYOFj1HATk14u6WcxiCiQ.png?1772833923)  
  


#### _**Step 4:** Configure the Action_

  


Follow these steps to configure the update contact details action:

  


  * **Action Name:** Assign an action name of your choice. This will help you recognize the action later. For example, "Update Contact's Date of Birth".  
  

  * **Which contact field to be updated:** Choose the field you want to update from the dropdown menu (e.g., name, phone, email, business name, etc.).  
  

  * **What to update in the field:** In the third field, write a short description of what you’re updating. This information helps the AI generate more accurate and personalized responses. For example, if you choose Date of Birth, you could write: "This is the birth date of the contact". If you select Business Name, you might write: "This the business name of the contact."  
  

  * **Output Example (Custom Fields Only):** If applicable, provide at least 2 examples of the updated information. For example, if you're updating "What is your favorite food?", you could enter "Tacos" and "Hamburgers".


  


Once you're done, click **Save** to finalize the new contact information settings.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066406938/original/ZlCgvC0yucIJED6KAQNY9gUNva_NpN_PYA.png?1772834007)  
  


#### _**Step 5:** Update Prompt_

  


Update your bot’s **Additional Information** Prompt to explicitly ask the customer for that contact detail(s) you would like to update. If this instruction isn't included in the prompt, the bot will not ask for the required information, and the contact field won't be updated.

  


**Example:** Lets say you want to collect name, email, phone, business name, date of birth before booking an appointment. Add this in the Additional Information section of the prompt to make sure the bot asks these questions:  
  
__###mandatory instruction : before booking an appointment always start the conversation by asking these question one after another  
1\. Ask the customer his name   
2\. Ask the customer his email  
3\. Ask the customer his phone  
4\. Ask the customer his date of birthdate  
5\. Ask the customer his business name __

  

    
    
    **Important: **If this instruction isn't included in the prompt, the bot will not ask for the required information and the contact field won't be updated.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066406960/original/BiVl3YyyKBwJsT5YTOgrJ_8GMIsQSZ7x0Q.png?1772834065)

* * *

## **Frequently Asked Questions**

  


**Q: Is there a limit to how many contact fields I can add using the Add Contact Info action?**  
The Add Contact Info action allows you to map a limited number of fields at one time. If you need to capture additional information, you can trigger a workflow from Conversation AI and use Update Contact Field actions inside the workflow to populate as many contact fields as needed based on the conversation.

  


**Q: Can Add Contact Info action overwrite an existing value?**

No. This action updates empty fields only.

* * *

## **Related Articles**

[  
](<https://help.gohighlevel.com/en/support/solutions/articles/155000003353>)

  * [Trigger a Workflow within Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004098>)  
[  
](<https://help.gohighlevel.com/en/support/solutions/articles/155000003353>)
  * [Workflow Action - Update Custom Values](<https://help.gohighlevel.com/en/support/solutions/articles/155000003353>)  
  

  * [How to Use Custom Fields](<https://help.gohighlevel.com/en/support/solutions/articles/48001161579>)  
  

  * [How to Use Conversation AI to Book Appointments](<https://help.gohighlevel.com/en/support/solutions/articles/155000000210>)  
  

  * [Guided Form Based Setup for Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000005382>)  
  

  * [Conversation AI Bot - Explained](<https://help.gohighlevel.com/en/support/solutions/articles/155000001335>)

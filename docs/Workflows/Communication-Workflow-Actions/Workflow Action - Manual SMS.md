# Workflow Action - Manual SMS

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003289-workflow-action-manual-sms](https://help.gohighlevel.com/support/solutions/articles/155000003289-workflow-action-manual-sms)  
**Category:** Workflows  
**Folder:** Communication Workflow Actions

---

**TABLE OF CONTENTS**

  * Overview
  * Action Name
  * Action Description
  * Action Details
  * Example


##   


## Overview

The **Manual SMS** action allows you to create a task for a user to manually send an SMS to a contact. This is useful when you want a personalized message sent that requires human intervention. The task created will appear in the Conversations > Manual Actions tab.

  


## Action Name

**Manual SMS**

  


## Action Description

This action generates a manual task to send an SMS message to a specific contact. The task requires user intervention to finalise and send the message. Users can select a template, add custom values, include trigger links, and test the message before sending.You can also assign the task to a specific user instead of the default contact owner.

  


  


## Action Details

  


Field| Description| Mandatory  
---|---|---  
Action Name| Name of the action to identify it in the workflow.| Yes  
Templates| Select an SMS template from the pre-defined templates available.| No  
Message| The message body to be sent. This field supports custom values and trigger links.| Yes  
Custom Values| Custom values available for personalising the message. Examples include contact name, appointment details, etc.| No  
Add Attachment| Option to add attachments to the SMS message via URL.| No  
Test Phone Number| A phone number to send a test SMS. Include country code.| No  
Assign To| Select a specific user to assign the manual SMS task to. Found under Advanced Settings. If left empty, defaults to the contact owner. If the selected user does not have contact access, the task is assigned to the contact owner or Unassigned if| No  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032219728/original/HpUKp_V3W_snYFG_RxXyaNZTC1EIGGN-qg.png?1725442538)

  


### **How to Configure**

  1. **Select Template** : Choose a pre-defined SMS template if applicable. This populates the message field with the template content.
  2. **Enter Message** : Write the message you want to send. Use the custom values dropdown to insert placeholders for dynamic data (e.g., contact name, appointment details).
  3. **Add Attachment** : If needed, add files by entering the URL.
  4. **Test SMS** : Enter a phone number to test how the SMS will appear when received.
  5. **Assign To (Advanced Settings)** : Optionally select a specific user to assign the task to. This overrides the default contact owner assignment.

  


  


### **Custom Values and Trigger Links**

The Manual SMS action supports custom values as well as Trigger links in the body of the message. 

Such as joining a calendar community or filling out a custom form. These links are clickable and can direct the contact to specific actions.

  


### **Assign To Behavior**

The Assign To field in Advanced Settings allows you to assign the manual SMS task to a specific user instead of the default contact owner. This is useful when you want a particular team member to handle certain tasks regardless of who owns the contact.  
  


**Assignment logic:**  
  


  * If a user is selected and has contact access, the task is assigned to that user.
  * If a user is selected but does not have contact access, the task falls back to the contact owner.
  * If no user is selected, the task defaults to the contact owner.
  * If neither the selected user nor contact owner is available, the task is marked as Unassigned.


  


  


## Example

  * **Trigger** : When a lead fills out a form on the website.
  * **Action** : Create a Manual SMS task for the assigned user to send a follow-up SMS.
  * **Message** : "Hi {{Contact Name}}, thank you for filling out our form. Click here to schedule an appointment: [Calendar Link]."
  * **Test Phone Number** : +11234567890 (for testing the SMS)


  


In this example, when a lead submits a form, a manual task is created to send a personalised SMS with a link to book an appointment. The message uses custom values to personalise the text and a trigger link for scheduling.

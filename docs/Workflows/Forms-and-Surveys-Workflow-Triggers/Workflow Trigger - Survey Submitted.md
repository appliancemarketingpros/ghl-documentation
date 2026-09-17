# Workflow Trigger - Survey Submitted

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003259-workflow-trigger-survey-submitted](https://help.gohighlevel.com/support/solutions/articles/155000003259-workflow-trigger-survey-submitted)  
**Category:** Workflows  
**Folder:** Forms and Surveys Workflow Triggers

---

This article will show you how to use the "Survey Submitted" workflow trigger! This trigger allows you to automate actions when a contact submits a specific survey. From follow-up emails to tagging and lead qualification, this trigger helps streamline post-survey workflows.

* * *

**TABLE OF CONTENTS**

  * What is the Survey Submitted Workflow Trigger?
  * Key Benefits of the Survey Submitted Trigger
  * How to Configure the Survey Submitted Trigger
  * Example
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is the Survey Submitted Workflow Trigger?**

  


This trigger is activated when a contact submits a survey. You can configure it with specific filters to target particular surveys or survey responses, allowing for tailored automation based on the contact's feedback. The Survey Submitted trigger allows you to initiate a workflow whenever a contact submits a survey. This can be useful for automating follow-up actions based on survey responses, such as sending a thank-you email, updating contact information, or adding tags based on the survey results.

* * *

## **Key Benefits of the Survey Submitted Trigger**

  


This trigger allows you to automate responses to survey submissions, reducing manual work and increasing the efficiency of lead processing and customer engagement.

  


  * Filters qualified and disqualified leads automatically  
  


  * Enables workflow branching based on survey type or conditions  
  


  * Saves time and ensures consistent communication  
  


  * Personalizes the post-survey experience


* * *

## **How to Configure the Survey Submitted Trigger**

  


  1. **Choose a Workflow Trigger** : Select **Survey Submitted** from the list of available triggers.  
  


  2. **Workflow Trigger Name** : Enter a descriptive name for your trigger, such as "Survey Submitted."  
  


  3. **Filters** : Use filters to refine when the trigger should activate. This allows you to specify which survey submissions should start the workflow.


  


Value| Description| Mandatory  
---|---|---  
Disqualified| Indicates if the survey response disqualifies the contact. Options are is true or is false.| No  
Survey is| Selects specific surveys to trigger the workflow. You can choose one or multiple surveys from the list.| No  
  
  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032022350/original/kqFxG4OUFG8-l2VypGm6BDl-PuIKNZW9uA.png?1725188871)

* * *

## **Example**

  


You want to create a workflow that triggers when a contact submits a feedback survey and is not disqualified. The workflow will then send a follow-up email thanking the contact for their participation.

  


  * **Workflow Trigger Name** : "Feedback Survey Submitted"  
  

  * **Filters** :  
  

    * **Disqualified** : `is false` (Only trigger if the contact is not disqualified)  
  

    * **Survey is** : "Customer Satisfaction Survey"


  


**Workflow Steps** :  
  


  1. **Trigger** : Survey Submitted (as configured above)  
  

  2. **Action** : Send Email - "Thank you for your feedback!"  
  

  3. **Action** : Update Contact Field - Mark the survey as "Completed."


* * *

## **Frequently Asked Questions**

  


**Q: Can I trigger a workflow from any survey?**  
Yes. Leave the “Survey is” filter blank to trigger from any survey, or choose a specific one.

  


**Q: Can I use logic based on survey answers?**  
While this trigger doesn’t directly evaluate answers, you can use custom fields or tags applied via survey to build logic.

  


**Q: Will this work if the survey is in a funnel?**  
Yes. The trigger works for surveys embedded in funnels, websites, or externally shared links.

* * *

## **Related Articles**

  


  * [Workflow Builder Walkthrough](<https://help.gohighlevel.com/en/support/solutions/articles/155000001254>)  
  

  * [Getting Started with Workflows](<https://help.gohighlevel.com/en/support/solutions/articles/155000002288>)  
  

  * [A List of Workflow Triggers](<https://help.gohighlevel.com/en/support/solutions/articles/155000002292>)

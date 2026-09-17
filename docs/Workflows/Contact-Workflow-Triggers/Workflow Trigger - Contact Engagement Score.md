# Workflow Trigger - Contact Engagement Score

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003496-workflow-trigger-contact-engagement-score](https://help.gohighlevel.com/support/solutions/articles/155000003496-workflow-trigger-contact-engagement-score)  
**Category:** Workflows  
**Folder:** Contact Workflow Triggers

---

**TABLE OF CONTENTS**

  * Overview
  * Trigger Name
  * Trigger Description
  * How to Configure
  * Example


## Overview

The **Contact Engagement Score** trigger is used to add contacts to a workflow based on their engagement score and other criteria, helping you to automate actions based on their interactions and overall engagement level.

  


## Trigger Name

**Contact Engagement Score**

  


## Trigger Description

This trigger allows you to filter contacts into a workflow based on their **Engagement Score** and other contact attributes. The trigger helps automate tasks like follow-ups, segmenting highly engaged contacts, or adjusting marketing efforts based on specific criteria.

  


## Trigger Details

  


Field Name| Description| Mandatory  
---|---|---  
Score| The engagement score of the contact. Filters are applied based on engagement criteria.| Yes  
Business Niche| The business category associated with the contact, such as Education, Healthcare, etc.| No  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033065696/original/RevefXKprkOBwX7qFdxChkT3dIs5xV6SFg.png?1726648831)

  


Operator| Description  
---|---  
Equals to| Triggers if the score or field value equals the input value.  
Greater than| Triggers if the score or field value is greater than the input value.  
Greater than or Equal to| Triggers if the score or field value is greater than or equal to the input value.  
Less than| Triggers if the score or field value is less than the input value.  
Less than or Equal to| Triggers if the score or field value is less than or equal to the input value.  
Is empty| Triggers if the field value is empty.  
Is not empty| Triggers if the field value is not empty.  
Contains Phrase| Triggers if the field contains the phrase entered.  
Does not contain Phrase| Triggers if the field does not contain the entered phrase.  
  
  


## How to Configure

  * **Step 1:** Select the trigger “Contact Engagement Score” from the workflow builder’s trigger options.
  * **Step 2:** Give the trigger a name, such as “High Engagement Contacts.”
  * **Step 3:** Set the filters to define the engagement score or other criteria.
    * For example, select **Score** from the filter dropdown and choose **Greater than**. Enter a value like **195**.
    * You can add additional filters like **Business Niche** and choose **Contains Phrase** , then enter the niche (e.g., **Education**).
  * **Step 4:** Save the trigger configuration and add further actions or steps to your workflow as needed.


  


## Example

In this scenario, the **Contact Engagement Score** trigger is set to capture contacts with a score **Greater than 195** and in the **Education** niche. When the contact meets both criteria, they will be added to the workflow for a follow-up email campaign.

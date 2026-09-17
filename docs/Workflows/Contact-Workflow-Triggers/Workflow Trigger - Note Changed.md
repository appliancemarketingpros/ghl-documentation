# Workflow Trigger - Note Changed

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003249-workflow-trigger-note-changed](https://help.gohighlevel.com/support/solutions/articles/155000003249-workflow-trigger-note-changed)  
**Category:** Workflows  
**Folder:** Contact Workflow Triggers

---

**TABLE OF CONTENTS**

  * Overview
  * Trigger Name
  * Trigger Description
  * How to Configure
  * Example


##   


## Overview

The **Note Changed** trigger is designed to initiate specific actions within a workflow whenever an existing note on a contact's record is modified. This is useful for keeping track of updates to important notes, ensuring team members are informed of changes, and maintaining up-to-date communication records.

  


## Trigger Name

**Note Changed**

  


## Trigger Description

The **Note Changed** trigger activates a workflow when an existing note is modified on a contact's profile. This allows for actions to be taken in response to changes in note content, such as notifying relevant team members, updating contact details, or tagging contacts based on the updated information.

  


## How to Configure

  


To configure the **Note Changed** trigger, set the workflow trigger name and choose from available filters to refine the conditions under which this workflow is activated.

  


  


Field| Description| Mandatory  
---|---|---  
Workflow Trigger Name| Name given to the trigger for easy identification.| Yes  
Doesn't Have Tag| Workflow will only trigger if the contact does not have a specified tag.| No  
Has Tag| Workflow will trigger only if the contact has a specified tag.| No  
  
####   


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032021312/original/jI7RBYV5rETUUFsCCL2m1jbsksISQ9DAzA.png?1725185292)

  


## Example

  


In this example, the workflow is set up to trigger when an existing note is changed for a contact who has a specific tag:

  1. **Workflow Trigger Name:** `Note Changed`
  2. **Filters:**
     * **Has Tag:** `Important Client`


####   


#### **Example Workflow**

  


When a note is changed on a contact record, the following actions could be triggered:

  * **Notify Account Manager:** Send an internal notification to the assigned account manager to review the changes made to the note on an important client's profile.
  * **Update Task:** Automatically update or create a task for the team member to take appropriate follow-up action based on the modified note content.
  * **Log Change:** Record the note change in a specific log or update the CRM to ensure there is a history of the modification.


This configuration ensures that the workflow is activated whenever a note is changed, allowing for immediate action and communication based on the updates to the note.

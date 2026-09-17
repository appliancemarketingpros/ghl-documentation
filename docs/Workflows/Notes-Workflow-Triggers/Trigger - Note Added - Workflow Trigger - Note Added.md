# Trigger - Note Added -> Workflow Trigger - Note Added

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003205-trigger-note-added-workflow-trigger-note-added](https://help.gohighlevel.com/support/solutions/articles/155000003205-trigger-note-added-workflow-trigger-note-added)  
**Category:** Workflows  
**Folder:** Notes Workflow Triggers

---

**TABLE OF CONTENTS**

  * Overview
  * Trigger Name
  * Trigger Description
  * How to Configure
  * Example


##   


## Overview

  


The "Note Added" trigger is used to initiate specific actions within a workflow whenever a note is added to a contact’s record. 

  


## Trigger Name

Note Added

  


## Trigger Description

This trigger can be used to automate a variety of tasks, such as sending internal notifications, updating contact information, or triggering subsequent actions in your automation processes.

  


## How to Configure

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031735352/original/3DZrIODcvvb3FnjC51E91xPf76V7HM_h0w.png?1724759304)

  


  


Value| Description| Mandatory  
---|---|---  
Choose a Workflow Trigger| Select "Note Added" from the dropdown.| Yes  
Workflow Trigger Name| Enter a name for your trigger, e.g., "Note Added"| Yes  
  
Filters| Specify conditions to narrow down the trigger, such as Has Tag/ Doesn't Have tag| No  
  
  


**Step-by-Step Guide**

  * Navigate to Workflow Triggers
  * Choose a Workflow Trigger: Select "Note Added" from the list of available triggers.
  * Name Your Trigger: Enter a descriptive name for the trigger, such as "Note Added."
  * Set Up Filters (Optional): Add filters to specify which filters it should trigger the workflow. For example, you can filter by standard fields such as Has tag/ Doesn't have tag or custom fields if present. 


##   


  


## Example : Haircut Note Notification

  


**Scenario:** A Saloon wants to ensure that any note labeled "Haircut" triggers an immediate internal notification to the saloon manager.

#### **Trigger Setup:**

  * **Trigger:** Note Added
  * **Name:** Haircut Note Alert
  * **Filter:** Note contains the tag "Haircut"


#### **Workflow Actions:**

  1. **Notification:** Send an internal notification to the saloon manager with the content of the note.
  2. **Task Creation:** Automatically create a task for the saloon manager to review the note.


**Outcome:** This automation ensures that any note mark![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031736934/original/bKUxyiduXUe2DVglxJlbSFVAoBDXO8blGA.png?1724760287)ed as "Haircut" is immediately flagged for the saloon manager’s attention, enabling prompt action and improving response times for critical issues.

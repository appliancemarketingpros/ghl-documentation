# Workflow Action - Task Notification

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003375-workflow-action-task-notification](https://help.gohighlevel.com/support/solutions/articles/155000003375-workflow-action-task-notification)  
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

The **Task Notification** action allows you to create a new task with a defined due date that will be assigned to a specific user. This is particularly useful for ensuring team members are aware of tasks that need their attention.

  


## Action Name

**Task Notification**

  


## Action Description

This action creates a task within the system, assigns it to a user, and defines a due date by which the task must be completed. You can specify task titles, assign users, set descriptions, and establish deadlines, ensuring task management is easy to organize.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032490951/original/clJ29r5zGEHylhicr_7iIfahd-PbJO_-mw.png?1725872615)

  


### **How to configure:**

  1. **Action Name:** Give the task an appropriate name such as "Add Task" to reflect its purpose.
  2. **Title:** Enter the task title that will be visible to the user.
  3. **Description:** Provide detailed information about the task. This is what the user will see to understand their assignment.
  4. **Assign To:** Select the user or team member to whom the task will be assigned.
  5. **Due In:** Define the deadline for the task using predefined durations (e.g., 1 day, 2 days, or immediate).


##   


Field Name| Description| Mandatory  
---|---|---  
Title| Title of the task to help users identify it.| Yes  
Description| Detailed description of the task, providing context and guidance to the assigned user.| No  
Assign To| Select the user to whom the task will be assigned from the available list of users.| Yes  
Due In| Set the deadline for the task (e.g., in 1 day, 2 days, 5 days, or "Now" for immediate tasks).| Yes  
  
##   


## Example

Let’s say you want to assign a task to a team member, John, to follow up with a lead. You can configure the action as follows:

  * **Action Name:** Add Task
  * **Title:** Follow-up with Lead XYZ
  * **Description:** Call Lead XYZ and check on the progress of their onboarding process.
  * **Assign To:** John Doe
  * **Due In:** 2 Days


  


In this case, John will receive the task in the system, and it will be due within 2 days.

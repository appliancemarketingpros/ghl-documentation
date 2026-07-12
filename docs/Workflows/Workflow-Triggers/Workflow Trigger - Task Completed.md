# Workflow Trigger - Task Completed

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003495-workflow-trigger-task-completed](https://help.gohighlevel.com/support/solutions/articles/155000003495-workflow-trigger-task-completed)  
**Category:** Workflows  
**Folder:** Workflow Triggers

---

**TABLE OF CONTENTS**

  * Overview
  * Trigger Name
  * Trigger Description
  * How to Configure
  * Example


##   


## Overview

The **Task Completed** workflow trigger allows you to automate follow-up actions based on the completion of tasks. By setting this trigger, you can initiate workflows when a task assigned to a user is marked as completed, creating an efficient way to handle task-related workflows and subsequent actions.

  


## Trigger Name

**Task Completed**

  


## Trigger Description

This trigger fires when a task assigned to a user is completed. It is useful for automatically moving a workflow forward based on task completion, whether to notify the team, follow up with a contact, or update a system status. You can filter this trigger to only fire for specific users or custom fields associated with tasks.

  


  


## Trigger Details

  


Field Name| Description| Mandatory  
---|---|---  
Assigned User| The user to whom the task was assigned. You can specify a particular user or leave it blank to apply to any user completing a task.| No  
Business Niche| A custom field used to filter task completions based on the business niche associated with the contact or task.| No  
Description| A custom field that can be used to filter task completions based on specific content in the task description.| No  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033063213/original/vdlEGQZz1ZJqELlAFNpuMfidSB3yC15KMg.png?1726647122)

  


## How to Configure

  * **Choose a Workflow Trigger:**

    * From the list of available triggers, select "Task Completed."
  * **Set the Workflow Trigger Name:**

    * Enter a descriptive name, such as "Task Completed Follow-up."
  * **Apply Filters (Optional):**

    * You can add filters to limit when the trigger fires. For example, you can specify that only tasks completed by a specific user should activate the trigger or tasks that contain specific values in custom fields.
  * **Save the Trigger:**

    * After configuring the trigger and filters, save your settings.


  


## Example

Let’s say you want to set up a workflow where a follow-up email is automatically sent to a contact after a sales task is marked as complete by a specific user.

  * **Trigger Name:** Sales Task Completed
  * **Assigned User:** John Doe
  * **Filter:** Business Niche = Real Estate


Once John Doe completes a task assigned to a contact in the Real Estate niche, this trigger will fire and automatically move the workflow to the next step, such as sending an email to the contact or updating the CRM status.

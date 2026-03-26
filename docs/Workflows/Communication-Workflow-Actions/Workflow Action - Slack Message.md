# Workflow Action - Slack Message

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003273-workflow-action-slack-message](https://help.gohighlevel.com/support/solutions/articles/155000003273-workflow-action-slack-message)  
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

The "**Slack Message** " action enables you to send notifications directly to Slack, whether it's to a specific user, a private channel, or a public channel. This action allows for seamless communication and notification management, ensuring that team members are promptly informed about relevant activities or updates. As a premium action, it will incur additional charges for each execution.

  


## Action Name

**Slack Message**

  


## Action Description

The "Slack Message" action sends a customized message to a designated Slack account. You can choose whether to send a direct message to a specific user, post in a private channel, or broadcast in a public channel. This integration helps streamline communication by automating notifications for various events, such as task completions, contact updates, or new lead assignments.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032062796/original/Vjk7HtsO6kWQ_NA8iL2v4xpUlr6s6wuCmw.png?1725272305)

  


Field| Description| Mandatory  
---|---|---  
Choose an Account| Select the Slack account you want to send notifications to.| Yes  
Event| Choose the type of message to send: direct message to a user, private channel, or public channel.| Yes  
  
##   


**How to Configure:**

  1. **Choose an Account:** Select the Slack account from the dropdown list where you want the message to be sent. This is required to ensure the message is delivered to the correct workspace.
  2. **Event:** Select the type of event you want to trigger the message. Options include:
     * **Send Direct Message to a User:** Choose this option to send a private message to a specific Slack user.
     * **Send Private Channel Message:** Select this option to send a notification to a designated private channel.
     * **Send Public Channel Message:** Use this option to send a notification to a public channel where everyone in the workspace can see it.


  


**Suggested Triggers to Combine with This Action:**

  * **Task Added:** Notify a Slack channel when a new task is assigned to a user.
  * **Opportunity Status Changed:** Send a message to a sales channel when the status of an opportunity changes.
  * **Form Submitted:** Send a notification to a specific channel when a customer submits a form.


## Example

Suppose you want to send a Slack notification to the "Marketing Team" channel whenever a new lead is added to the system and tagged with "High Priority."

  


**Workflow Configuration Example:**

  1. **Trigger:** `Contact Added`
     * **Filters:** Tag = `High Priority`
  2. **Action:** `Send notification to Slack`
     * **Choose an Account:** `Your account`
     * **Event:** `Send Private Channel message`
     * **Channel:** `#Marketing Team`
     * **Message:** `A new high-priority lead has been added. Please check the details.`

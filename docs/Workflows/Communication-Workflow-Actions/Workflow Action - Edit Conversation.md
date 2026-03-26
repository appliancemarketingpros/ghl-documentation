# Workflow Action - Edit Conversation

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003269-workflow-action-edit-conversation](https://help.gohighlevel.com/support/solutions/articles/155000003269-workflow-action-edit-conversation)  
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

The "**Edit Conversation** " action allows you to modify the state of a conversation by marking it as read or unread, as well as by archiving or unarchiving it. This can be useful for managing conversations effectively and keeping track of which messages have been addressed.

  


## Action Name

**Edit Conversation**

  


## Action Description

The "Edit Conversation" action lets you:

  1. Mark a conversation as read or unread.
  2. Archive a conversation, moving it out of the active conversation list.
  3. Unarchive a conversation, moving it back into the recents tab.


This action helps streamline conversation management by enabling quick status updates and organization.

  


## Action Details

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032056538/original/lmhpQmBv5nAr2vTAa551pSfX8rizwVFRpQ.png?1725268913)

  


Field Name| Description| Mandatory  
---|---|---  
Mark as Read or Unread| Choose to mark the conversation as either read or unread. Options include: <ul><li>None</li><li>Mark as Read</li><li>Mark as Unread</li></ul>| No  
Archive or Unarchive| Choose to archive or unarchive the conversation. Options include: <ul><li>None</li><li>Archive</li><li>Unarchive -> Move to Recents tab</li></ul>| No  
  
##   


#### **How to Configure**

  1. **Action Name:** Enter a descriptive name for the action, such as "Mark as Read and Archive."
  2. **Mark as Read or Unread:** Select an option to change the read status of the conversation.
  3. **Archive or Unarchive:** Choose whether to archive the conversation or move it back to the recents tab.


####   


#### **Suggested Triggers**

  1. **Contact Replied:** Use this action to automatically mark a conversation as read when a contact replies.
  2. **Appointment Status Changed:** Use this action to archive a conversation after an appointment is marked as completed.


#### 

##   


## Example

**Scenario:** You want to ensure that conversations are archived and marked as read once a customer service issue is resolved.

  1. Set up a workflow trigger for when a contact replies.
  2. Add the "Edit Conversation" action.
  3. Configure it to mark the conversation as read and archive it.
  4. This way, all resolved conversations are automatically moved out of the active conversation list, helping your team stay organised and focused on unresolved issues.


  


This setup helps maintain a clean and organised communication channel, ensuring that only active and unresolved conversations are immediately visible to the support team.

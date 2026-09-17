# How to Send Inbound SMS Notifications via a Workflow

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001156789-how-to-send-inbound-sms-notifications-via-a-workflow](https://help.gohighlevel.com/support/solutions/articles/48001156789-how-to-send-inbound-sms-notifications-via-a-workflow)  
**Category:** Phone System  
**Folder:** Messaging

---

Workflow Automation

How to Send Inbound SMS Notifications via a Workflow

Use the Customer Replied workflow trigger to notify your team by SMS when a contact sends an inbound text message.

Overview

Inbound SMS messages are received and stored in the Conversations tab in HighLevel. A phone number's call-forwarding settings do not automatically forward those inbound SMS messages to another phone number.

If your team also needs an SMS alert when a contact replies, you can create a Customer Replied workflow that sends a separate internal SMS notification containing the inbound message. This article explains how to configure the trigger, add the message content, manage repeat replies, and troubleshoot common issues.

Table of Contents

What is Inbound SMS Notification Forwarding? Key Benefits of Inbound SMS Notifications How the Workflow Works How to Set Up Inbound SMS Notifications Configure Re-entry for Repeated SMS Replies Troubleshooting Frequently Asked Questions Related Articles

Video Walkthrough

# What is Inbound SMS Notification Forwarding?  
  


Inbound SMS notification forwarding uses a workflow to alert internal users when a contact sends an SMS. The original message remains in Conversations, while the workflow creates a separate internal notification containing information from that message.

This is different from call forwarding. Configuring a forwarding phone number for calls does not automatically forward inbound text messages to that same destination.

## Key Benefits of Inbound SMS Notifications  
  


Internal SMS notifications help team members stay aware of inbound replies even when they are not actively monitoring Conversations. Dynamic values can include the contact and message information needed to understand who replied and what they said.

  * **Faster Response Awareness:** Alert team members when a contact sends an inbound SMS.
  * **Message Context:** Include dynamic values such as the contact's name and inbound message body.
  * **Flexible Recipients:** Send internal notifications to the applicable users, roles, or teams supported by the Internal Notification action.
  * **Channel Control:** Use Reply Channel = SMS so replies from other channels do not trigger the same SMS notification workflow.


## How the Workflow Works  
  


The workflow listens specifically for inbound SMS replies and then sends a new internal notification to your selected recipient. The contact's original SMS remains available in Conversations and is not moved or replaced.

  1. A contact sends an inbound SMS.
  2. The message appears in Conversations.
  3. The **Customer Replied** trigger detects the reply.
  4. The **Reply Channel = SMS** filter confirms the message came from SMS.
  5. The workflow sends an **Internal Notification** containing the message details.


Important

The workflow sends a **new internal notification**. It does not natively forward the original SMS thread through the phone number's call-forwarding setting.

## How to Set Up Inbound SMS Notifications  
  


Proper trigger filters ensure the workflow reacts only to inbound SMS replies, while the Internal Notification action determines who receives the alert and what information is included. Test the workflow before relying on it for live conversations.

Step 1

Create a New Workflow

Go to **Automation → Workflows → Create Workflow**.

![Automation menu showing Workflows and Create Workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054130737/original/95tUaOX4SPgqFWq8o42zKkLBOrb3tjWtdA.png?1758279172)

Select **Start from Scratch** , then choose **Create New Workflow**.

![Start from Scratch option selected with Create New Workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054130880/original/H-26rH1GF0MkZOOQL1iKd1V_1tzRhIcl5g.png?1758279262)

Step 2

Add the Customer Replied Trigger  
  


Click **Add New Workflow Trigger**.

![Add New Workflow Trigger button in the workflow builder](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131077/original/HOq864JsX-wWx1cruXGdObKDsvKSPJ05FA.png?1758279349)

Select **Customer Replied**.

![Customer Replied selected as the workflow trigger](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131310/original/51XMxxiWX-u4o-Kl0w4oApwzqZDavHBnqw.png?1758279423)

Step 3

Filter the Trigger to SMS Replies

Click **Add Filters**.

![Add Filters option in Customer Replied trigger settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131335/original/0fpNZPq7R2UlUM6JFbgvlu_PAdMnq6j2fQ.png?1758279461)

Choose **Reply Channel**.

![Reply Channel filter selected](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131523/original/6qbjI1i223rfhQpNppjcwA_F6uARI6fPHw.png?1758279519)

Select **SMS** as the Reply Channel.

![SMS selected from the Reply Channel dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131571/original/g_oLzHXTS11l9bLBtjbxWzvvLXFKS_yKLw.png?1758279548)

Click **Save Trigger**.

![Save Trigger button and workflow action prompt](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131595/original/o3pLYwY_EgdHXo0ZNMn7dVP5B-N8olGW_Q.png?1758279574)

Step 4

Add the Internal Notification Action  
  


Click the action below the trigger and select **Send Internal Notification**.

Messaging Charges

SMS internal notifications generate outbound SMS usage and applicable messaging charges.

![Send Internal Notification selected as the workflow action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131685/original/AUl9fAcdFRTqir3wrdvPRqlqpK14SQ55gg.png?1758279623)

Choose **SMS** as the notification type and select the appropriate internal recipient supported by your configuration.

![Internal SMS notification configuration panel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131784/original/mK9gRU0NiByWvt9VPG3n_e-oUo4dLNKwFQ.png?1758279666)

Step 5

Add the Inbound Message Body  
  


In the notification message, open the Custom Values picker and select **Message → Message Body**. This inserts **{{message.body}}** , which provides the content of the reply that triggered the workflow.

![Custom Values picker showing Message Body](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054131877/original/fUx-zzkaWf67vLqw4LGymFTCmAxkow8q8Q.png?1758279735)

Step 6

Add Contact Details

Add useful contact values such as **Contact → First Name** so the notification identifies who sent the message.

![Custom Values picker showing Contact First Name](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054132059/original/CfQHim1rFFEmNoNrFnjOC4B78pxkyUJtrg.png?1758279821)

**Example notification:**  
New SMS from {{contact.first_name}}:  
{{message.body}}

Step 7

Publish and Test the Workflow

Save the action, publish the workflow, and send a test SMS reply from a contact. Confirm that the inbound message appears in Conversations and that the intended internal recipient receives the separate SMS notification.

## Configure Re-entry for Repeated SMS Replies

Allow Re-entry controls whether the same contact can enter the workflow again after completing it. This setting matters for an inbound SMS notification workflow because contacts may reply more than once over time.

  * **Allow Re-entry enabled:** A contact can enter the workflow again after they have completed it or have been manually removed.
  * **Allow Re-entry disabled:** A contact can enter and complete the workflow only once.


    
    
    **Important:** A contact cannot re-enter while they are still active in the workflow. For a simple notification workflow, keep the workflow short so it can complete before the contact's next qualifying reply.

## Troubleshooting Inbound SMS Notifications

Most notification issues are caused by trigger filters, workflow status, recipient configuration, re-entry settings, or SMS delivery limits. Checking each layer in order can quickly identify why an expected alert was not received.

The workflow does not trigger

  * Confirm the trigger is **Customer Replied**.
  * Confirm the filter is **Reply Channel = SMS**.
  * Confirm the workflow is published and active.
  * If the contact has already completed the workflow, check whether **Allow Re-entry** is enabled.


The notification action executes but the user does not receive the SMS

  * Confirm the intended internal user has a valid phone number configured.
  * Review the workflow execution history for errors.
  * Check the failed SMS in Conversations or messaging logs for an error code when available.


The notification is too long

If the resulting SMS body exceeds approximately 1,600 characters, the message can fail to send. This can happen when a large dynamic value such as **{{message.body}}** is inserted into the notification. Keep SMS notification content concise or use another internal notification channel when long content is expected.

## Frequently Asked Questions

Q: Will I be charged for each SMS internal notification?

Yes. SMS internal notifications use outbound messaging and can generate applicable SMS charges. For high-volume alerts, consider an in-app or email internal notification instead.

Q: Is the original inbound SMS actually forwarded?

No. The original inbound message remains in Conversations. The workflow creates a separate internal notification that can include the original message content through **{{message.body}}**.

Q: Will the workflow notify me every time the same contact sends another SMS?

Only when the contact is eligible to enter the workflow again. Enable **Allow Re-entry** if the same contact should be able to re-enter after completing the workflow.

Q: What does {{message.body}} contain?

It inserts the message content associated with the reply that triggered the workflow. If the resulting SMS notification becomes too long, delivery can fail, so keep the notification template concise.

Q: Can I notify more than one team member?

Yes. Internal Notifications can target supported users, roles, or teams depending on the notification configuration. Each SMS recipient can contribute to messaging usage.

Q: Can the Customer Replied trigger also monitor email or chat replies?

Yes. Customer Replied supports multiple reply-channel filters. If you need notifications for other channels, configure the appropriate Reply Channel filters or separate workflows so each channel can be managed intentionally.

Q: Does the contact receive a confirmation when the internal notification is sent?

No. The Internal Notification action alerts your internal recipient and does not automatically reply to the contact. If you want the contact to receive an automated response, add a separate **Send SMS** action.

### Related Articles

[ Workflow Trigger - Customer Replied ](<https://help.gohighlevel.com/support/solutions/articles/155000002677>) [ Workflow Action - Internal Notification ](<https://help.gohighlevel.com/support/solutions/articles/155000003202>) [ Workflow Settings - Overview ](<https://help.gohighlevel.com/support/solutions/articles/48001239875-workflow-settings-overview>) [ Workflow Action - Send SMS ](<https://help.gohighlevel.com/support/solutions/articles/155000002474-workflow-action-send-sms>) [ Troubleshooting SMS Delivery Issues ](<https://help.gohighlevel.com/support/solutions/articles/48000981696-troubleshooting-sms-delivery-issues>)

# Workflow Trigger - User Replied

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008196-workflow-trigger-user-replied](https://help.gohighlevel.com/support/solutions/articles/155000008196-workflow-trigger-user-replied)  
**Category:** Workflows  
**Folder:** Events Workflow Triggers

---

The User Replied trigger fires whenever a user (member of your team), sends a message to a contact. Use it to measure how quickly your team responds, stop automations once a person steps in, log outbound activity, and route conversations based on who replied and where. This article shows how to setup and use the User Replied trigger in Workflows.

* * *

**TABLE OF CONTENTS**

  * What is the User Replied Trigger?
  * Key Benefits of Using the User Replied Trigger
  * How to Use the User Replied Trigger in Workflows
  * Trigger Filters
  * Replied By: The Grouped User Picker
  * Channel Behavior
  * Custom Values
  * Use Cases
  * Setting Up SLA Tracking and Escalation
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is the User Replied Trigger?**

  


The User Replied trigger starts a workflow when someone on your team sends a message to a contact from the conversation view. It is built around reply and response activity, and it fires on two kinds of messages a user sends:

  


  * **A new outbound message.** A user sends the first message to a contact, for example when a contact comes in through a form and a rep reaches out.  
  

  * **A reply in an existing thread.** A contact has messaged in, and a user answers within that conversation


  

    
    
    **Important:** This trigger fires only on messages a user sends from the conversation view, and only once that message is delivered, not the moment it is sent. Messages sent by workflow actions (Send SMS, Send Email, and so on) or by Conversation AI do not fire it. For automation based on Conversation AI, use the separate Conversation AI Trigger, which fires on a condition you define rather than on a specific message.

* * *

## **Key Benefits of Using the User Replied Trigger**

  


  * **Track response times:** Capture the moment a rep responds to a contact so you can measure how fast your team replies.  
  

  * **Stop automations when a person takes over:** End a drip or nurture sequence as soon as a team member replies personally, so a contact never receives an automated message and a human message at the same time.  
  

  * **Build "wait and check" flows:** Pair the trigger with the User Replied wait condition to cover the classic pattern where a contact messages in, you wait a few minutes, and if nobody has replied you alert the owner.  
  

  * **Route by who replied and where:** Branch a workflow based on the sending user, the contact's assigned user, or the channel the message went out on.  
  

  * **Act on what was said:** React when a rep's message contains a phrase like "refund approved" by moving the opportunity, sending a confirmation, or applying a tag.  
  

  * **Log activity:** Record every outbound reply, or keep fields like "Last Contacted By" and "Last Contact Date" up to date.


* * *

## **How to Use the User Replied Trigger in Workflows**

  


  1. Log in to your account.  
  

  2. Go to **Automations > Workflows**.  
  

  3. **Create** a new **workflow** or **edit** an **existing** one.  
  

  4. Click **\+ Add New Trigger** , then select **User Replied** from the list (under **Events**).  
  
![](https://jumpshare.com/share/1fHp8adcptdb0ypSPekL+/GIF+Recording+2026-07-10+at+20.29.33.gif)  
  

  5. Enter a clear **Trigger Name** so it is easy to find later, for example "Rep Replied (SLA Timer)".  
  

  6. Click **\+ Add Filters** to narrow when the workflow should run. If you add no filters, the trigger fires on every user reply, to any contact, on any channel.  
  

  7. Click **Save Trigger**.  
  

  8. Add your workflow actions, such as Add Tag, Send Email/SmS, Assign to User, Send Internal Notification, or Update Opportunity, etc, then **Publish** the workflow.  
  
![](https://jumpshare.com/share/eLWFJFDk9rjFbG13oaXN+/GIF+Recording+2026-07-10+at+21.38.48.gif)


* * *

## **Trigger Filters**

  


Filters let you control which user replies should start the workflow. You can combine several of them to get as specific as you need.

  


Filter| Operator| Values| Notes  
---|---|---|---  
Sent By| Is any of| Grouped user picker (see below)| Multi-select. Pick the contact's assigned user and/or specific users.  
Message Channel| Is any of| SMS, Email, WhatsApp, Facebook Messenger, Instagram DM, Live Chat| Select one or more channels to match. Some channels offer additional channel-specific options.  
Contains Phrase| Contains| Free text (case-insensitive)| Runs only when the message includes the words or phrases you specify. Supports several comma-separated phrases.  
Exact Match Phrase| Equals| Free text (case-insensitive)| Runs only when the message matches exactly. Whitespace is trimmed before comparing.  
Has Tag| Has any of| Tag picker| Runs only if the contact has the selected tag.  
Doesn't Have Tag| Has none of| Tag picker| Runs only if the contact does not have the selected tag.  
  
####   


#### **Replied By: The Grouped User Picker**

  


The **Replied By** filter is a single, searchable, multi-select dropdown with two kinds of options:

  


  * **User assigned to the Contact.** This dynamic option always sits at the top. Use it when you only want the trigger to fire if the contact's own assigned user replies.
  * **Users.** Every available user, listed by name.


  

    
    
    **Note:** If you do not add a **Replied By** filter, the trigger fires when any user replies.

  


![](https://jumpshare.com/share/9No5ot74hueMwhSbLob9+/Screen+Shot+2026-07-10+at+21.45.31.png)

* * *

## **Channel Behavior**

  


The trigger works across all the main conversation channels. Because each channel threads its conversations a little differently, what counts as a brand new outbound message versus a reply can vary. The table below shows how that works on each channel.

  


Channel| New Outbound| Reply to Existing  
---|---|---  
Email| User writes a new email, where a new subject line starts a new thread| User replies inside an existing email thread  
SMS| First SMS to a contact who has no prior messages| Any later SMS in the ongoing thread  
WhatsApp| User starts with a template message, outside the 24-hour window| User replies inside the 24-hour service window  
Facebook Messenger| First message to a contact with no prior conversation| Any later message in the ongoing thread  
Instagram DM| First DM to a contact with no prior conversation| Any later DM in the ongoing thread  
Live Chat| Not applicable, since the visitor always starts the session| User replies inside an active session  
  
  


Email is the only channel where a user can keep several separate threads going with the same contact. On single-thread channels like SMS, Messenger, and Instagram DM, every message simply adds to one continuous conversation.

* * *

## **Custom Values**

  


The trigger makes the following values available inside your workflow actions and If/Else conditions. Use them to personalize notifications, log activity, and route conversations.

  


Name| Custom Value| Description  
---|---|---  
User Name| `{{user_replied.senderName}}`| Name of the user who sent the message  
User ID| `{{user_replied.userId}}`| Internal user ID of the sender, which is more reliable than the name for external integrations  
Message Body| `{{user_replied.messageBody}}`| The content of the message  
Channel| `{{user_replied.channel}}`| The channel the message was sent on, such as SMS, Email, or WhatsApp  
Timestamp| `{{user_replied.timeStamp}}`| When the message was sent  
Conversation ID| `{{user_replied.conversationId}}`| The conversation or thread ID  
User Email| `{{user_replied.senderEmail}}`| Email address of the user who sent the message  
  
* * *

## **Use Cases**

  


**Keyword-Based Routing**

  


  * Trigger: User Replied
  * Filter: Contains Phrase set to "refund approved"
  * Actions: Move the opportunity to a new pipeline stage and send a confirmation.


  


**Log Outbound Activity**

  


  * Trigger: User Replied
  * Actions: Update "Last Contacted By" with `{{user_replied.senderName}}` and "Last Contact Date" with `{{user_replied.timeStamp}}`, or record the reply somewhere outside the platform.


* * *

## **Setting Up SLA Tracking and Escalation**

  


Response-time SLAs are the most common reason to reach for this event. If you want to make sure a rep replies within a target time and escalate when they do not, you build that with the User Replied event as a **Wait** condition and a **Goal** , rather than with the trigger on its own.

  


The pattern looks like this:

  


  1. Start the workflow with the event that begins the clock, such as Customer Replied, so it runs when a contact messages in.  
  

  2. Add a **Wait** step set to the **User Replied** condition, with a timeout such as five minutes.  
  

  3. On the timeout branch, where no user replied in time, add your escalation actions, such as notifying the owner or manager, creating a task, or sending an internal alert.  
  

  4. To stop a reminder or nurture sequence as soon as a rep replies, add a **User Replied** goal so the contact jumps out of the remaining steps.


  

    
    
    **Note:** The Wait condition and the Goal are set up in their own steps. For the full walkthrough, see the [Workflow Action - Wait](<https://help.gohighlevel.com/support/solutions/articles/155000002470-workflow-action-wait>) and [Workflow Action - Goal Event](<https://help.gohighlevel.com/support/solutions/articles/155000003328-workflow-action-goal-event>) articles.

* * *

## **Frequently Asked Questions**

  


**Q: Do messages sent by a workflow fire this trigger?**

No. Automated messages from workflow actions such as Send SMS or Send Email do not fire it. Only a message a user sends from the conversation view counts.

  


**Q: Will it fire on cold or mass outbound outreach?**

Not reliably. The trigger is built around replies and responses, not cold first-touch outreach.

  


**Q: Can I fire only when the contact's assigned user replies?**

Yes. Add a **Sent By** filter and choose "User assigned to the Contact".

  


**Q: What happens if a user sends several messages quickly?**

Each message fires the trigger on its own, unless re-enrollment is restricted on the workflow.

  


**Q: What if a contact is enrolled in more than one workflow?**

The trigger fires independently in each workflow.

* * *

### **Related Articles**

  


  * [Workflow Trigger - Customer Replied](<https://help.gohighlevel.com/support/solutions/articles/155000002677-workflow-trigger-customer-replied>)  
  

  * [Workflow Trigger - Inbound Email](<https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email>)  
  

  * [Workflow Action - Wait](<https://help.gohighlevel.com/support/solutions/articles/155000002470-workflow-action-wait>)  
  

  * [Workflow Action - Goal Event](<https://help.gohighlevel.com/support/solutions/articles/155000003328-workflow-action-goal-event>)

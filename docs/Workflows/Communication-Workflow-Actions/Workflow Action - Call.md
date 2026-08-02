# Workflow Action - Call

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003274-workflow-action-call](https://help.gohighlevel.com/support/solutions/articles/155000003274-workflow-action-call)  
**Category:** Workflows  
**Folder:** Communication Workflow Actions

---

The Call workflow action helps your team respond quickly by automatically calling the person responsible for a contact and then connecting that person with the contact. HighLevel can play a personalized whisper message before placing the contact call, giving the recipient useful context before the conversation begins. Use this action for time-sensitive follow-up, appointment outreach, new-customer onboarding, and other situations where a live conversation is valuable.

* * *

**TABLE OF CONTENTS**

  * What is the Call Workflow Action?
    * Key Benefits of the Call Workflow Action
    * How Call Routing Works
    * Action Details
    * How to Configure this Workflow Action
    * Disable Voicemail Detect
    * Example Workflow


* * *

# **What is the Call Workflow Action?**

  


The **Call** workflow action creates an automated call connection between an internal recipient and a workflow contact. Understanding the order of the calls helps you configure the correct recipient, write a useful whisper message, and avoid contacting a lead before a team member is ready.

  


When a contact reaches the Call action, HighLevel first calls one of the following recipients:  
  


  1. The user assigned to the contact.  
  

  2. If the contact is unassigned, this event will call the number listed in Settings > Company tab > Company Phone field  
  


After the recipient answers, HighLevel plays the configured whisper message. Depending on the action’s keypress setting, the recipient may need to press a number key before HighLevel calls the contact. If the contact answers, HighLevel bridges the two parties.

  


The company phone number used for an unassigned contact is configured in the sub-account’s Business Profile.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077377071/original/p69RQfBs7YHRV4lrgvj5rpbXYARE1Yv1BQ.png?1785526566)

* * *

## **Key Benefits of the Call Workflow Action**

  


  * **Faster lead response:** Automatically alert and connect a team member when a contact completes an important action.  
  

  * **Assignment-based routing:** Call the user responsible for the contact without manually selecting a recipient for every workflow execution.  
  

  * **Context before connection:** Play a whisper message containing the contact’s name, the triggering event, or other relevant information.  
  

  * **Flexible automation:** Use the action after triggers such as an appointment being confirmed or a tag being added.


* * *

## **How Call Routing Works**

  


The Call action uses a flow that adapts based on whether the contact is assigned or unassigned.

  


  1. The contact reaches the Call action in the workflow.
  2. HighLevel calls the correct internal recipient:
     * **Assigned user** (if the contact is assigned), or
     * **Company phone** (if the contact is unassigned)
  3. The internal recipient answers the call.
  4. HighLevel plays the whisper message to give context.
  5. If keypress is enabled, the recipient must press a number key to continue.
  6. HighLevel calls the contact.
  7. If the contact answers, both parties are connected.


  

    
    
    **Note:** The number called if the contact is not assigned to a user is the number listed in Settings > Company tab > Company Phone field

  


* * *

## **Action Details**

  


Field| Description| Mandatory  
---|---|---  
Action Name| The name for this specific call action.| Yes  
Call Whisper| A short message that will be played to the receiver before the call is connected. Custom values can be used to personalize the message. This message will play up to three times.| No  
Call Timeout (s)| The maximum number of seconds to wait before terminating the call attempt if not connected.| Yes  
Disable Voicemail Detect| If enabled, the system will not attempt to detect voicemail. This setting is useful to reduce the delay caused by voicemail detection, but it might lead to voicemail connections being treated as normal calls. Recommended for shorter call timeouts.| No  
Connect Call After Keypress| If enabled, the call will only connect after the receiver presses a key. This is useful to confirm that a live person has answered the call.| No  
  
  

    
    
    **Important:** Note: The Call Whisper message uses Text-to-Speech (TTS). TTS is billed at $0.00084 per 100 characters.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077377766/original/9ZEyLgjKwF6pAGSfCQS0B_cRKasQgAShRg.jpeg?1785528036)

* * *

## **How to Configure this Workflow Action**

  


  1. **Add the Call Action** : In your workflow, select the Call action from the list of available actions.  
  

  2. **Set Action Name** : Provide a name for this action, such as "Customer Support Call."  
  

  3. **Enter Whisper Message** : Type the message you want the receiver to hear before connecting. Use custom values if necessary.  
  

  4. **Set Call Timeout** : Define the time in seconds for the call to attempt connection before ending.  
  

  5. **Configure Advanced Settings** : Decide whether to enable voicemail detection or require a keypress to connect the call.  
  

  6. **Save the Configuration** : Once all settings are configured, save the action.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032063905/original/QIzRg25DV6YQaZNN_mntHs3KTkhDBMOyxg.png?1725272857)

* * *

## **Disable Voicemail Detect**

  


See this article [Stop On Response and Disable Voicemail Detect](<https://help.gohighlevel.com/en/support/solutions/articles/155000006910>) for details on the interaction between the workflow setting Stop on Response and the Call action setting Disable Voicemail Detect.

  

    
    
    Note that what the Business does in the Call action is irrelevant to Stop on Response and Disable Voicemail Detect. The Business will be called first; if the Business doesn't answer, the workflow will continue, if the Business does answer, and the Contact then doesn't answer, the workflow will continue. Only the Contact (or the Contact's voicemail) is relevant to Stop on Response/Disable Voicemail Detect.

  


When a call connects, we, by default, try to understand if a person answered or if it’s voicemail. This creates a slight delay in the call connection but if you have “Stop On Reply” turned on and it is determined that a voicemail answered, the contact will continue in the workflow. Toggling this on will disable the voicemail detection, eliminating the delay - but if “Stop On Reply” is on and voicemail detection is off, the workflow will be stopped when either a person or a voicemail answers.

  

    
    
    If you have the Workflow Setting Stop On Reply ON (and Disable Voicemail Detect OFF), and the Call action calls the business who answers but the lead does not, the workflow will carry on.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155057573408/original/5WxfA4EOT9nym7W94JUOajYnuAfJhtG-Xg.png?1762282547)

* * *

## **Example Workflow**

  


**Workflow Configuration Example:**

  * **Trigger** : "Appointment Confirmed" - When an appointment status changes to confirmed.
  * **Action** : "Call" - A call is initiated to the assigned user to remind them of the upcoming appointment.
    * **Action Name** : "Appointment Call Reminder"
    * **Call Whisper** : "You have a new appointment scheduled with [Contact Name] at [Appointment Time]. Press any key to confirm."
    * **Call Timeout** : 30 seconds
    * **Disable Voicemail Detect** : Enabled (for quicker connection)
    * **Connect Call After Keypress** : Enabled (to ensure the call connects to a person)


  


**Some Triggers to Use with This Action (But not limited to)**

  1. **Appointment Confirmed** : Automatically call the assigned user when an appointment is confirmed.
  2. **Lead Form Submitted** : Initiate a call when a lead's submits a form, such as "First Contact Form"


  


This configuration will ensure that users are proactively contacted when critical events, such as confirmed appointments or lead status changes, occur, allowing for better customer engagement and timely responses.

# Bot Status for Individual Contacts

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004096-bot-status-for-individual-contacts](https://help.gohighlevel.com/support/solutions/articles/155000004096-bot-status-for-individual-contacts)  
**Category:** AI Employee  
**Folder:** Conversation AI

---

Bot Status for Individual Contacts gives your team more control over when Conversation AI should respond, pause, or stay inactive for a specific contact. This article explains how to manage bot status from the Conversations tab, how each status works, and when Conversation AI may automatically become inactive or ent

* * *

**TABLE OF CONTENTS**

  * What is Bot Status for Individual Contacts
    * Key Benefits of Bot Status for Individual Contacts
    * Bot Status Options
    * When Conversation AI May Automatically Become Inactive
    * How to Update Bot Status for an Individual Contact
    * Frequently Asked Questions
    * Related Articles


* * *

# **What is Bot Status for Individual Contacts**

  


Bot Status for Individual Contacts helps teams manage Conversation AI based on the needs of each contact conversation.

  


Instead of turning Conversation AI on or off for every contact, users can update the bot status for one conversation while other contacts keep their current AI behavior. This contact-level control is available from the message composer in the Conversations tab, and status changes apply only to the selected contact conversation.

  


This feature is **only available Suggestive or Auto-Pilot mode.** If the bot status icon is not visible in the message composer, confirm that Conversation AI is enabled for the sub-account and that the bot is using one of these supported modes

* * *

## **Key Benefits of Bot Status for Individual Contacts**

  


  * **Contact-Level Control:** Update Conversation AI status for one contact without changing bot behavior for every other contact.  
  


  * **Temporary Pausing:** Snooze Conversation AI for a selected amount of time so it can automatically reactivate later.  
  


  * **Permanent Inactive Option:** Keep Conversation AI inactive for a contact until someone manually turns it back on.  
  


  * **Improved Conversation Accuracy:** Prevent AI from responding in conversations where manual review, opt-out handling, or special attention is needed.  
  


  * **Flexible AI Management:** Use Conversation AI differently across contacts based on each conversation’s context.


* * *

## **Bot Status Options**

  


Each bot status determines how Conversation AI behaves for the selected contact. Understanding these options helps you choose whether AI should continue responding, pause temporarily, or stop engaging with that contact.  
  


  * **Active:** The bot will respond to all incoming messages.  
  

  * **Inactive:** The bot remains off until manually reactivated.  
  

  * **Sleep/Snooze:** The bot is temporarily paused, either manually or due to certain actions (e.g., when a manual or workflow message is sent, or message limits are reached). Users can set a specific time for the bot to automatically wake up and start responding again.


* * *

## **When Conversation AI May Automatically Become Inactive**

  


Conversation AI status can change automatically depending on contact behavior, bot settings, and account configuration. Conversation AI may become inactive for a contact when:  
  


  * A contact replies with an opt-out keyword such as “STOP.”  
  


  * The bot reaches the maximum configured AI message limit.  
  


  * A user sends a manual message and bot sleep settings are configured to pause AI after manual replies.  
  


  * A workflow sends a message or updates the Conversation AI bot status.  
  


  * Advanced Conversation AI settings are configured to send the bot to sleep during human handoff scenarios.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072346773/original/CjlHMnN2fQHDMNwiBe6_vWJ3RoEva8YaKw.png?1779915045)

* * *

## **How to Update Bot Status for an Individual Contact**

  


  1. Go to **Conversations** and open the conversation for the contact you want to update.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072346573/original/047wNX6NoR0C1u1Ovp4dlf5jHE5ac_4NDw.png?1779914424)  
  


  2. Locate the Conversation AI status icon in the message composer area. The icon may show that Conversation AI is currently active, inactive, or sleeping.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072346589/original/n-pROkwIhfBXX09pu6bZmwZ_kO75FQzmHw.png?1779914463)  
  

  3. Click the Conversation AI status icon and choose the desired status:  
  
**Active** to allow Conversation AI to respond or suggest replies based on the configured mode.  
  
**Inactive** to turn Conversation AI off for the contact. (Select **Inactive** if you want to use **Sleep/Snooze** to temporarily pause Conversation AI for the contact.)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072346598/original/fU2g_VLmJHgxFy31CdoCioucVXvdoycl0Q.png?1779914500)  
  


  4. If setting the status to Sleep/Snooze, select **Inactive**. Then choose when Conversation AI should reactivate by checking **Reactive bot after** and selecting a duration in minutes, hours, or days.  
  
Leave automatic reactivation unchecked if the bot should remain inactive until manually reactivated.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072346622/original/yXNv2Ca3lsq3sSHW-__BtMY-TiBEdxywzA.png?1779914608)  
  

  5. Apply the change by clicking out of the module. Confirm that the status icon updates in the message composer for that contact.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072346643/original/TFVaimDFBHUz18HoZbXI0kf2aEhn1JcwlQ.png?1779914668)


* * *

## **Frequently Asked Questions**

  


**Q: Does contact-level Inactive override global Conversation AI settings?**  
Yes. When set to **Inactive** , Conversation AI will not reply for that contact until you change the status to **Active**.  
  


**Q: What happens to incoming messages while the bot is Sleeping?**  
Messages are received as normal. Conversation AI remains paused until the wake time, after which it resumes based on your configuration.

  


**Q: Does sending a manual agent message pause the bot automatically?**  
Depending on your global settings, human messages can trigger auto-sleep or delay AI replies to prevent overlap.

  


**Q: Can I bulk-update bot status for many contacts at once?**  
Contact-level status is designed for one-to-one control. Use workflows for conditional or larger-scale changes.

  


**Q: What if the status control isn’t visible?**  
Verify that Conversation AI is enabled, a bot is assigned to the channel, and your response mode supports AI replies.

* * *

## **Related Articles**

  


  * [Setting Up Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004401>)  
  

  * [Auto-Pilot Mode](<https://help.gohighlevel.com/en/support/solutions/articles/155000001337>)  
  

  * [Conversations AI - Suggestive Mode](<https://help.gohighlevel.com/en/support/solutions/articles/155000007994>)  
  

  * [Advanced Settings Overview - Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004415>)  
  

  * [Update Conversation AI Bot and Status - Workflow Action](<https://help.gohighlevel.com/en/support/solutions/articles/155000003821>)

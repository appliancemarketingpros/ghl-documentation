# Workflow Action - Drip

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003360-workflow-action-drip](https://help.gohighlevel.com/support/solutions/articles/155000003360-workflow-action-drip)  
**Category:** Workflows  
**Folder:** Communication Workflow Actions

---

The **Drip Action** in workflows helps regulate the flow of contacts by processing them in batches at set intervals. This prevents overwhelming your system, ensures smooth automation execution, and maintains resource efficiency. In this guide, we’ll walk you through how to configure and optimize the Drip Action for better workflow control.

* * *

**TABLE OF CONTENTS**

  * What is the Drip Workflow Action?
    * Key Benefits of the Drip Workflow Action
    * Configuring Drip Workflow Action
      * Step 1: Access the Workflow Builder
      * Step 2: Add the Drip Action
      * Step 3: Naming the Action
      * Step 4: Setting the Batch Size
      * Step 5: Configuring the Drip Interval
      * Step 6: Save and Publish the Workflow
      * Drip Preview
    * Action Statistics, Batch Schedule & Insights
    * Draft & Publish Behavior
    * Good to Know
    * Frequently Asked Questions


* * *

# **What is the Drip Workflow Action?**

  


The Drip Workflow Action is designed to control the rate at which contacts progress through a workflow by processing them in batches at predefined intervals. Instead of executing actions on all contacts simultaneously, this feature allows you to stagger executions, ensuring smooth automation and preventing system overload. It is especially useful for managing high-volume workflows, such as bulk email or SMS campaigns, where controlled delivery is crucial for maintaining engagement and avoiding resource bottlenecks.

* * *

## **Key Benefits of the Drip Workflow Action**

  


  * **Controlled Execution:** Prevents system overload by processing contacts in manageable batches rather than all at once.


  


  * **Optimized Resource Management:** Helps maintain API limits, email/SMS sending capacity, and server performance.


  


  * **Improved Deliverability & Engagement:** Spreads out communications over time to avoid spam filters and enhance response rates.


  


  * **Flexible Scheduling:** Allows customization of batch size and intervals (minutes, hours, days) for precise automation control.  
  

  * **Schedule Transparency** : A live preview shows exactly when each batch is projected to run, so you can verify timing before publishing.  
  

  * **Pacing Protection** : The drip automatically pauses when a workflow moves to Draft and resumes its original pacing when published again, preventing contacts from bursting out all at once


* * *

## **Configuring Drip Workflow Action**

  


  


### **Step 1: Access the Workflow Builder**

  


Log in to your HighLevel account, go to Automation > Workflows, and either create a new workflow or choose an existing one to edit.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041803410/original/QlJnd7snzQ_lSrH1OVpWthrur0fxylvbjA.png?1739882387)

  


  


### **Step 2: Add the Drip Action**

  


Click the + icon to add a new action in your workflow, then search for Drip in the action list and select it.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041803595/original/F1Jy7GRiPtrofk-I6GyKVI5uxHCPKK51yw.png?1739882507)

  


  


### **Step 3: Naming the Action**

  


Give your Drip action a clear and descriptive name to make it easily identifiable in the workflow builder.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069571922/original/U8nxjdXRm7pC3OvyBaM9Syd1XJFUCJaVOg.png?1776757222)

  


  


### **Step 4: Setting the Batch Size**

  


Set the batch size to control how many contacts will move to the next step at a time. You can choose any number between 1 and 10,000, depending on your workflow needs. For example, if you set the batch size to 100, then 100 contacts will proceed at each interval, ensuring a steady and manageable workflow execution.

###   


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041806001/original/-DyEvE0byzhzTJHtG2SjeW7_lKKHvFPUUA.png?1739884042)

  


**Note** : If you update the batch size on a previously published workflow that already has contacts queued in the Drip action, an informational note will appear: “Contacts already queued in this drip will use the previous batch size. New contacts will use the updated batch size.” This ensures you’re aware that changes only apply to newly entering contacts.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069572115/original/_Ex3L0zrtg4ASGLMOUmwzD-sxPqbMN8x1Q.png?1776757324)

  


  


**  
**

### **Step 5: Configuring the Drip Interval**

  


Set the drip interval to determine how often each batch of contacts will move to the next step. You can choose from minutes (1–60), hours (1–24), or days (1–7) based on your workflow timing needs. For example, if you set the interval to 30 minutes, a new batch of contacts will progress every 30 minutes, ensuring a controlled and consistent workflow execution.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041806047/original/xO_eubmcJ3gzBVumg9Pg4U1GHxzRTTNwfA.png?1739884065)

  


  


### **Step 6: Save and Publish the Workflow**

  1. Click Save to apply the Drip action settings.
  2. Ensure the workflow is properly configured, then click Publish to activate automation.
  3. Run a test by adding test contacts and verifying batch processing in workflow history.


  


  


  


### **Drip Preview**

  


A live schedule preview is now available directly inside the Drip action while configuring it. You can see exactly when each batch is projected to run before publishing the workflow, removing the guesswork from drip scheduling.

**What the preview shows:**

  * A batch table with the batch number and scheduled send time, for up to 10 batches. If fewer batches exist, all are shown.
  * If a Workflow Time Window is active, an inline warning is displayed: “Workflow time window (e.g., 8 AM – 7 PM, Mon–Fri) is shifting some batches to the next available slot.” The time window text is a clickable link that opens the relevant setting directly.
  * The preview is shown during first-time setup. When editing a Drip action that already has contacts in it, the preview is hidden to keep the editing view clean.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069572841/original/TyEfvY-qJpAvc3Q1VUJEE-LUTXGfk-mG-g.gif?1776757563)  


##   


##   


## **Action****Statistics, Batch Schedule & Insights**

  


Clicking the statistics icon on the Drip action (the one showing how many contacts are waiting) opens a detailed view of what’s happening inside the drip. The entry point has been redesigned to be more discoverable.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069573505/original/PyFGz-WFnLHd7BNZFfW6AaVwaHU2vEABmw.png?1776757873)  


  


**This view includes:**

  * Quick summary cards showing contacts currently in the drip, next batch details, and ETAs.
  * A full batch schedule table with every batch, its scheduled send time, and any active constraints (e.g., time window) affecting timing.
  * The Workflow Time Window setting is surfaced directly inside this view, with a link to jump to the setting and review or change it.
  * Status column, pagination, and existing capabilities (move to next step, delete contact, contact hyperlink) are all available in one place.
  * If you return to action statistics after changing drip settings, a warning is shown along with a view of how many contacts are using the older settings vs. the newer settings.


## ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069573563/original/vF5H3eyQ_dWNLoK8K4MvEBBS1zQSgHQUWQ.gif?1776757899)

  


##   


##   


## **Draft & Publish Behavior**

When a workflow moves from Published to Draft while contacts are sitting in a Drip action, those contacts are now automatically paused for the full duration the workflow stays in Draft.

  * Once the workflow is published again, the drip resumes from where it left off – instead of bursting all queued contacts out at once.
  * This preserves the pacing the drip was designed for and protects sender reputation.


  


##   


## **Good to Know**

  * The schedule preview shows a maximum of 10 batches. If fewer exist, all are shown.
  * The preview is hidden while editing a Drip action that already has contacts in it.
  * The batch size change warning only appears on workflows that have been published at least once and currently hold contacts in the drip.
  * The “settings apply to new contacts only” note is shown only when you edit drip settings on a workflow with contacts already queued.


## **Frequently Asked Questions**

  


**Q: How is the Drip action different from a normal delay or wait step?**

A standard wait step holds all contacts at a specific point in the workflow until the set time passes. In contrast, the Drip action releases contacts in batches, allowing a controlled flow instead of moving everyone forward at once.

  


  


**Q: What happens if my batch size is too large?**

If your batch size is too large, all contacts will move at once, which may overload communication channels (e.g., sending thousands of emails or SMS at once). It’s best to choose a manageable batch size based on your business needs and provider limits.

  


  


**Q: Can I use the Drip action with emails, SMS, and other workflow actions?**

Yes! The Drip action can be used with any workflow step, including emails, SMS, task assignments, and other automation actions, making it a flexible tool for pacing workflow execution.

  


  


**Q: What happens if new contacts enter the workflow while the Drip action is running?**

New contacts will start from the beginning of the workflow and follow the same batch processing rules set in the Drip action. They won’t join an already running batch but will follow their own drip schedule based on the configured settings.

  


  


**Q: Can I change the batch size or drip interval after the workflow is published?**

Yes, you can update the batch size and drip interval at any time. However, changes will only apply to contacts that enter the Drip action after the update. Contacts already in progress will continue following the previous settings.An informational note will appear when you make changes on a workflow with contacts already queued, confirming this behavior.'''

  


  


**Q: How can I see when each batch is scheduled to run?**

When configuring a Drip action for the first time, a live schedule preview is shown directly in the action panel. It displays a table with the batch number and projected send time for up to 10 batches. For a published workflow with contacts already in the drip, click the statistics icon on top of Drip action(Blue Icon with people and the number of contacts waiting ) to see the full batch schedule along with summary cards and ETAs.

  


**Q: What happens if a Workflow Time Window is active?**

If a Workflow Time Window is set (e.g., 8 AM – 7 PM, Mon–Fri), it may shift some drip batches to the next available slot. This is surfaced as an inline warning in both the Drip Preview and the Action Statistics view, so you can catch schedule conflicts before they cause unexpected behavior. The warning includes a clickable link to open the Time Window setting directly.

  


  


Attachments (1)

[ ![thumbnail](/images/helpdesk/attachments/155069572819/thumb) ScreenRecording2026-04-09at5.17.27PM-ezgif.com-video-to-gif-converter (1).gif  
2.3 MB ](</helpdesk/attachments/155069572819>)

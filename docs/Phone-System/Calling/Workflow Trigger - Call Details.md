# Workflow Trigger - Call Details

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001212511-workflow-trigger-call-details](https://help.gohighlevel.com/support/solutions/articles/48001212511-workflow-trigger-call-details)  
**Category:** Phone System  
**Folder:** Calling

---

Workflow Automation

Workflow Trigger - Call Details

Automate follow-up actions based on call direction, call outcomes, phone numbers, number pools, and custom call dispositions.

What You'll Learn

The Call Details workflow trigger lets HighLevel respond automatically when a call matches specific outcomes or call information. You can target incoming or outgoing calls, specific statuses, phone numbers, number pools, and custom dispositions. This makes it easier to automate missed-call follow-up, voicemail handling, sales callbacks, internal notifications, and other call-based processes.

Table of Contents

  1. What is the Call Details Workflow Trigger?
  2. Key Benefits of the Call Details Workflow Trigger
  3. How the Call Details Trigger Works
  4. Available Call Details Filters
  5. How to Set Up the Call Details Workflow Trigger
  6. Common Use Cases
  7. Testing and Troubleshooting
  8. Frequently Asked Questions


# **What is the Call Details Workflow Trigger?**

Call Details is an event-based workflow trigger that enrolls a contact when a call log matches the conditions you configure. Instead of manually reviewing calls and deciding what should happen next, HighLevel can evaluate the call information and automatically start the appropriate workflow.

The trigger can evaluate information such as call direction, call status, the phone number involved, an associated Number Pool, and a Custom Disposition. Combining these filters makes it possible to create targeted automations for specific calling scenarios.

Example

A workflow could enroll a contact only when an **incoming** call has a status of **busy, voicemail, or no-answer**. The workflow could then send an internal notification, create a callback task, apply a tag, or begin another follow-up sequence.

## **Key Benefits of the Call Details Workflow Trigger**

Call-based automation helps teams respond consistently without requiring someone to monitor call logs throughout the day. Precise filters also make it possible to separate different calling scenarios and apply the right follow-up automatically.

  * **Automated follow-up:** Start callbacks, notifications, tasks, tagging, or messaging when a qualifying call occurs.
  * **Precise call targeting:** Narrow enrollment using call direction, status, phone numbers, Number Pools, and custom dispositions.
  * **Consistent handling:** Apply the same response every time a missed call, voicemail, or other configured call outcome occurs.
  * **Reduced manual monitoring:** Let workflows react to qualifying call events instead of requiring users to review call records manually.
  * **Flexible sales and support automation:** Build different workflows for incoming leads, outbound sales calls, missed calls, callback requests, and other call outcomes.


## **How the Call Details Trigger Works**

Each qualifying call is evaluated against the filters configured on the trigger. Adding more filter types narrows the conditions the call must satisfy before the contact can enter the workflow.

**1\. A call occurs** — HighLevel records the call and its available call details.

**2\. Trigger filters are evaluated** — The call is compared with the Call Direction, Call Status, Number Pool, Custom Disposition, phone number, and any other configured conditions.

**3\. The contact qualifies** — If the trigger conditions are satisfied and the workflow's enrollment rules permit entry, the contact enters the workflow.

**4\. Workflow actions run** — The workflow can send messages, create tasks, notify users, update records, apply tags, or perform other configured actions.

### **Call Status vs. Custom Disposition**

These filters represent different types of call information. Choosing the correct one prevents workflows from relying on the wrong outcome data.

Filter| What It Represents| Examples  
---|---|---  
**Call Status**|  A system-recorded call outcome.| Busy, voicemail, no-answer, completed  
**Custom Disposition**|  A defined post-call classification selected for the call.| Follow Up, Qualified, No Answer, Voicemail, Requested Callback  
  
Important

Custom Dispositions are separate from system Call Status values. If your automation is intended to react to an agent-selected call outcome, use the **Custom Disposition** filter rather than relying on the legacy manual call-status behavior.

## **Available Call Details Filters**

Filters determine which calls qualify for the workflow. Use only the conditions necessary for the automation so that valid calls are not unintentionally excluded.

Filter| Purpose| Example  
---|---|---  
**Call Direction**|  Separates incoming and outgoing call scenarios.| Incoming  
**Call Status**|  Matches selected system call outcomes.| Busy, voicemail, no-answer  
**In Number Pool**|  Limits the trigger to calls associated with a selected Number Pool.| Paid Search Tracking Pool  
**Custom Disposition**|  Matches a call classification recorded after the call.| No Answer, Voicemail  
**In Phone Number**|  Restricts the trigger to one or more selected phone numbers.| Main Sales Number  
  
Filter Example

If **Call Direction = Incoming** and Call Status includes **busy, voicemail, and no-answer** , the call must be incoming and match one of the selected call-status outcomes before the trigger qualifies.

## **How to Set Up the Call Details Workflow Trigger**

Proper trigger configuration ensures contacts enter the workflow only for the call scenarios you intend to automate. Build the trigger from the Workflow Builder, configure the required call filters, then test the workflow before publishing it.

### **Step 1: Open or Create a Workflow**

Navigate to **Automation → Workflows**. Open an existing workflow or click **Create Workflow** and choose **Start from Scratch** to build a new automation.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080157480/original/hZk_OT9HooyMYEF2E4juLiYTlg1JRARYTQ.png?1788561508)

### **Step 2: Add the Call Details Trigger**

In the Workflow Builder, click **Add New Trigger**. Under the Events trigger category, select **Call Details**.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080157484/original/fu4JTHxJv3347mT-F-ErBw34qOLo_wc6sA.png?1788561528)**

### **Step 3: Name the Trigger**

Enter a descriptive **Workflow Trigger Name**. The name does not change how the trigger executes, but clear names make workflows easier to understand and maintain.

For example, use a name such as **Incoming Missed Call** , **Voicemail Follow-Up** , or **Call Status Changed**.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080157487/original/YdRmOoa1UB30C3NsD-BX4gz-QlphziS9-Q.jpeg?1788561538)**

### **Step 4: Configure Call Direction**

Add the **Call Direction** filter when the workflow should apply only to incoming or outgoing calls. This is especially useful when inbound follow-up and outbound sales processes require different automations.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080157488/original/Focb0LsQfpxO3tc14w2cbYVkwzOTxOacrw.png?1788561550)**  


### **Step 5: Configure Call Status**

Use **Call Status** to select the system-recorded call outcomes that should qualify. You can select applicable outcomes such as **busy** , **voicemail** , or **no-answer**.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080157495/original/gjZzcW4OR_J9nDFeOqdJznCNHDQUgM-NIQ.png?1788561561)**

### **Step 6: Add a Number Pool Filter When Needed**

Use **In Number Pool** when the automation should apply only to calls attributed to a specific call-tracking Number Pool. This helps separate automations by campaign, traffic source, or tracking configuration.

For information about creating and managing Number Pools, see [How to Set Up Call Tracking (Number Pool)](<https://help.gohighlevel.com/support/solutions/articles/48000981393>).

### **Step 7: Add a Custom Disposition Filter When Needed**

Select **Custom Disposition** when the workflow should respond to a post-call classification such as No Answer, Voicemail, Follow Up, or another disposition configured for your account.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080157501/original/xUIFiFbgHZx9V5RgfhO8F5r5osgB10WmqA.png?1788561574)**

To learn how dispositions are created and used, see[Custom Dispositions for Voice Calls](<https://help.gohighlevel.com/support/solutions/articles/155000007191-custom-dispositions-for-voice-calls>).

### **Step 8: Restrict the Trigger to a Phone Number When Needed**

Use **In Phone Number** when the workflow should apply only to calls associated with a specific selected phone number. This is useful when different business lines require different call automations.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080157506/original/lqqrxafBaTe6L5-QZpS2eLj5IHkc4BOMqA.png?1788561588)**

### **Step 9: Save, Test, and Publish**

Save the trigger after the required filters are configured. Add the workflow actions that should run after enrollment, then use the workflow testing tools and a representative call scenario to confirm the automation behaves as expected.

Once testing is complete, switch the workflow from **Draft** to **Publish** so qualifying live calls can enroll contacts.

## **Common Use Cases**

The best trigger configuration depends on what should happen after the call. These examples show how call information can be turned into targeted follow-up automation.

Scenario| Example Trigger Setup| Possible Actions  
---|---|---  
**Missed inbound call**|  Direction = Incoming; Status = busy or no-answer| Notify team, create callback task, send follow-up  
**Voicemail follow-up**|  Status = voicemail| Notify assigned user or create follow-up task  
**Disposition-based sales follow-up**|  Custom Disposition = Follow Up or Requested Callback| Create task, move opportunity, send follow-up message  
**Campaign-specific calls**|  In Number Pool = selected tracking pool| Apply campaign-specific tags or internal routing  
**Dedicated business line**|  In Phone Number = selected line| Run a workflow designed only for that department or line  
  
## **Testing and Troubleshooting**

When a qualifying call does not produce the expected automation, check both the trigger conditions and the workflow's enrollment settings. Most issues can be isolated by comparing the actual call record with every filter configured on the trigger.

  1. **Confirm the workflow is published.** Draft workflows do not process live trigger events as published automations.
  2. **Compare the call with every trigger filter.** Verify direction, status, Number Pool, phone number, and disposition values as applicable.
  3. **Review Custom Disposition usage.** A disposition-based trigger requires the expected disposition to actually be recorded for the call.
  4. **Check Allow Re-entry.** A new qualifying call does not automatically mean a contact can enroll again. Workflow Settings determine whether completed or manually removed contacts may re-enter.
  5. **Check whether the contact is already active.** A contact cannot re-enter the same workflow while still active in it under normal re-entry behavior.
  6. **Review Enrollment History and Execution Logs.** Use these tabs to confirm whether the contact entered the workflow and whether any subsequent action was skipped or failed.
  7. **Test with a simplified trigger if needed.** Temporarily remove unnecessary filters to identify which condition is preventing qualification, then rebuild the required filter set.


Using Completed Call Status?

If your automation depends on a **Completed** status representing a true human connection, review [Using Call Connect to Ensure Accurate Call Status Tracking](<https://help.gohighlevel.com/support/solutions/articles/48001181825-call-status-marking-calls-as-completed-when-the-client-didn-t-answer-the-call>). Call Connect can improve the accuracy of call outcomes used for reporting and automation.

Re-entry

To review repeat-enrollment behavior, open the workflow's **Settings** tab and check **Allow Re-entry**. See [Workflow Settings - Overview](<https://help.gohighlevel.com/support/solutions/articles/48001239875-workflow-settings-overview>) for the current re-entry rules.

## **Frequently Asked Questions**

Q: Does Call Details trigger for every phone call?

No. The call must match the conditions configured on the trigger. Adding filters such as Call Direction, Call Status, phone number, Number Pool, or Custom Disposition narrows which calls qualify.

Q: Can the same contact enter a Call Details workflow more than once?

A later qualifying call can create another trigger event, but repeat enrollment depends on the workflow's **Allow Re-entry** setting. When re-entry is enabled, a contact can re-enter after completing the workflow or being manually removed. A contact cannot normally re-enter while still active in the same workflow.

Q: What is the difference between Call Status and Custom Disposition?

Call Status represents a system-recorded outcome such as busy, voicemail, no-answer, or completed. Custom Disposition represents a post-call classification configured for your team, such as Follow Up, Qualified, or Requested Callback.

Q: Can I select more than one call status?

Yes. You can select multiple applicable values within the Call Status filter, such as busy, voicemail, and no-answer. Other filter rows still narrow the overall trigger configuration.

Q: Why is my Custom Disposition workflow not triggering?

Confirm that the expected disposition was actually recorded for the call and still exists in the account. If a disposition used by a workflow is deleted, update the workflow filter to a valid disposition before testing again.

Q: Can one call qualify for multiple workflows?

Yes. Separate workflows evaluate their own trigger configurations independently. A call can qualify for more than one workflow when it satisfies each workflow's conditions and its contact-enrollment rules permit entry.

Q: What is the difference between In Number Pool and In Phone Number?

In Number Pool targets calls associated with a selected call-tracking Number Pool. In Phone Number targets one or more specific phone numbers. Choose the filter that matches how the call source is organized in your account.

Q: Where should I look if the trigger appears correct but the workflow still does not run?

Confirm the workflow is published, review the contact's Enrollment History, check Execution Logs, verify Allow Re-entry when applicable, and compare the actual call data with every configured trigger filter.

### **Related Articles**

  * [Getting Started with Workflows in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000002288>)
  * [A List of Workflow Triggers](<https://help.gohighlevel.com/support/solutions/articles/155000002292-a-list-of-workflow-triggers>)
  * [Workflow Settings - Overview](<https://help.gohighlevel.com/support/solutions/articles/48001239875-workflow-settings-overview>)
  * [Custom Dispositions for Voice Calls](<https://help.gohighlevel.com/support/solutions/articles/155000007191-custom-dispositions-for-voice-calls>)
  * [How to Set Up Call Tracking (Number Pool)](<https://help.gohighlevel.com/support/solutions/articles/48000981393>)
  * [Using Call Connect to Ensure Accurate Call Status Tracking](<https://help.gohighlevel.com/support/solutions/articles/48001181825-call-status-marking-calls-as-completed-when-the-client-didn-t-answer-the-call>)

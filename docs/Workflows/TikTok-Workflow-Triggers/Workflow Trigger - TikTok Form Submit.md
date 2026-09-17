# Workflow Trigger - TikTok Form Submit

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003262-workflow-trigger-tiktok-form-submit](https://help.gohighlevel.com/support/solutions/articles/155000003262-workflow-trigger-tiktok-form-submit)  
**Category:** Workflows  
**Folder:** TikTok Workflow Triggers

---

**TABLE OF CONTENTS**

  * Overview
  * Trigger Name
  * Trigger Description
  * How to Configure
  * Example


##   


## Overview

The **TikTok Form Submitted** trigger is designed to start a workflow whenever a form is submitted via TikTok. This can be particularly useful for capturing leads, collecting feedback, or gathering information from TikTok users, and then automating subsequent actions.

  


## Trigger Name

**TikTok Form Submit**

  


## Trigger Description

This trigger activates a workflow when a specific form on TikTok is submitted. You can specify which form submissions should trigger the workflow using filters, ensuring that only relevant submissions start the workflow.

  


## How to Configure

  * **Choose a Workflow Trigger** : Select **TikTok Form Submitted** from the list of available triggers.

  * **Workflow Trigger Name** : Enter a descriptive name for your trigger, such as "TikTok Lead Capture" or "TikTok Feedback Form."

  * **Filters** : Use filters to specify which form submissions will activate the workflow. You can filter based on the form name to narrow down the trigger to specific forms.


  


Value| Description| Mandatory  
---|---|---  
In Form| Selects the specific TikTok form that will trigger the workflow when submitted.| Yes  
  
  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032022492/original/A426hQAmcPS1t1wwCkwPOXY0vI_wRDYPqw.png?1725189426)

  


## Example

You want to create a workflow that sends a thank-you email to users after they submit a feedback form on TikTok.

  * **Workflow Trigger Name** : "TikTok Feedback Thank You"
  * **Filters** :
    * **In Form** : "TikTok Feedback Form" (Only submissions from this form will trigger the workflow)


  


**Workflow Steps** :

  1. **Trigger** : TikTok Form Submitted (as configured above)
  2. **Action** : Send Email - Thank the user for their feedback.
  3. **Action** : Update Contact - Tag the contact as "Feedback Provided" to keep track of users who have submitted feedback.

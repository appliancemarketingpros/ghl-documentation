# Workflow Action - Create/Update Opportunity

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002476-workflow-action-create-update-opportunity](https://help.gohighlevel.com/support/solutions/articles/155000002476-workflow-action-create-update-opportunity)  
**Category:** Workflows  
**Folder:** Opportunity Workflow Actions

---

**TABLE OF CONTENTS**

  


  * Overview
  * Action Name
  * Action Description
  * Action Details
  * Example


##   


## Overview

The "Create or Update Opportunity" action in your automation workflow is designed to manage opportunities within your sales pipeline. This feature allows you to automatically create or update opportunities based on predefined criteria, ensuring that your sales process is organised and efficient.

  


## Action Name

Create Opportunity

  


## Action Description

The "Create or Update Opportunity" action creates a new opportunity or updates an existing one within the selected pipeline and pipeline stage. This action helps in tracking leads and managing potential sales through different stages of your sales process.

However, **this action does not leverage** :

  * **Opportunities that trigger the workflow** (i.e., it does not automatically update the opportunity that caused the workflow to start).
  * **Any “Find Opportunity” step** (i.e., it does not use the opportunity found by a prior “Find Opportunity” action).


  


## Action Details

The details for configuring the "Create or Update Opportunity" action are as follows:

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155038428191/original/FL0knisuSnMYjK8PkXZ3pLdWt054jH15jQ.png?1734370334)

  


  


Value Name| Description| Mandatory  
---|---|---  
Action Name| The name you assign to this action for easy identification in your workflow.| Yes  
In Pipeline| The specific sales pipeline where the opportunity will be created or updated.| Yes  
In Pipeline Stage| The stage within the selected pipeline where the opportunity will be placed.| Yes  
Opportunity Name| The name assigned to the opportunity for easy identification.| Yes  
Opportunity Source| The source of the opportunity, indicating where the lead came from.| Yes  
Lead Value| The estimated value of the lead (optional).| No  
Status| The current status of the opportunity (e.g., open, closed).| Yes  
Allow Opportunity to Move to Any Previous Stage in Pipeline| Allows the opportunity to be moved to any previous stage in the pipeline if needed.| No  
Allow Duplicate Opportunities| Allows the creation of duplicate opportunities if a similar opportunity already exists.| No  
  
  


### Important Note

  * **Deprecation** : The **"Create or Update Opportunity"** action is being phased out. It is recommended to use **Create Opportunity** or **Update Opportunity** actions instead, which offer more granular control and support additional features (e.g., leveraging a “Find Opportunity” step or updating the triggering opportunity). 
        
        We’re gradually deprecating the combined action—but only for new workflows. Existing workflows using the combined action will continue to work as is.

  * **No “Find Opportunity” or Triggered Opportunity Support** : This action does not update the opportunity that triggered the workflow nor does it use any opportunity found via a **Find Opportunity** action. It operates solely on its own logic to either locate an existing opportunity or create a new one.


## Example: Managing New Leads from a Calendar Appointment Funnel

  


**Scenario:** Your business wants to create an opportunity in the sales pipeline whenever a new lead comes in from the calendar appointment funnel. This ensures that every lead is tracked and managed properly through your sales process.

  


**Solution using the "Create or Update Opportunity" action:**

  


**Trigger:** The workflow starts when a new lead is generated from the calendar appointment funnel.

**Action 1:** Create Opportunity action to create a new opportunity in the pipeline.

  


**Steps to Implement:**

  * Add the Create Opportunity action to your workflow to be triggered when a new lead is generated.
  * Set the Action Name to "Create Opportunity".
  * Select the appropriate sales pipeline from the In Pipeline dropdown (e.g., "YOUR PROMOTION Pipeline").
  * Choose the initial stage for the opportunity from the In Pipeline Stage dropdown (e.g., "New Leads").
  * Set the Opportunity Name to something descriptive, such as "Deal 251 Opportunity".
  * Define the Opportunity Source to indicate where the lead came from, e.g., "Lead from Calendar Appointment Funnel".
  * Optionally, you can fill in the Lead Value if you have an estimated value for the lead.
  * Set the Status to "open".
  * Configure additional settings as needed:
  * Enable Allow Opportunity to Move to Any Previous Stage in Pipeline if you want the flexibility to move opportunities backward in the pipeline.
  * Enable Allow Duplicate Opportunities if your process allows for creating duplicate opportunities for similar leads.


  


**Outcome:** This automation ensures that every new lead from the calendar appointment funnel is automatically tracked as an opportunity in your sales pipeline. This helps in organising and managing your sales process effectively, ensuring no lead is overlooked.

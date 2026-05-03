# Workflow Action - AI Decision Maker

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005649-workflow-action-ai-decision-maker](https://help.gohighlevel.com/support/solutions/articles/155000005649-workflow-action-ai-decision-maker)  
**Category:** Workflows  
**Folder:** Workflow AI Workflow Actions

---

The AI Decision Maker allows you to automatically route contacts through different workflow paths based on engagement, company size, behavior, and other data points. Instead of building complex logic trees with multiple conditions, you can provide plain-English instructions and let AI determine the most appropriate branch.

  


This action simplifies workflow routing while maintaining accuracy and flexibility across large volumes of contacts.

  


> **Note:** This is a premium action. Each execution will incur additional charges.

* * *

**TABLE OF CONTENTS**

  * What is AI Decision Maker?
  * Key Benefits of AI Decision Maker
  * How To Set Up AI Decision Maker
  * Popular Use-case
  * Frequently Asked Questions
  * Related Articles


* * *

# **What Is AI Decision Maker?**

  


AI Decision Maker acts as an intelligent routing engine inside workflows. Rather than relying on traditional if/then rules or manually configured filters, you describe routing conditions in plain English.

  


The AI evaluates contact data and determines the correct branch automatically. This allows workflows to adapt dynamically without requiring ongoing logic updates.

* * *

## **Key Benefits of AI Decision Maker**  
  


**Reduces Workflow Maintenance**  
  


Once configured, AI dynamically adapts to changes in contact data, reducing the need to update multiple filters and conditional rules.

  


**Scales Easily with Growth**  
  


Whether routing hundreds or thousands of contacts, the AI handles complexity without slowing workflow performance.

  


**Eliminates Human Error**  
  


AI-based decision logic removes inconsistencies caused by missed or overlapping conditional rules.

  


**Plain-English Instructions**  
  


No coding or rule stacking is required.

* * *

## **How To Set Up AI Decision Maker**

  


Follow these steps to insert and configure the action in your workflow.

###   
**_Step 1:_**_Choose or Create a Workflow_  
  


  1. Log into your sub-account.  
  


  2. Click **Automation** in the left menu.  
  


  3. Edit an existing workflow or click **\+ Create Workflow** to build a new one from scratch, template, or recipe.  
  


### ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155065903827/original/gu0xgnR3EMYGgjjQuk5nMi8q8z4lN-cU9w.png?1772231158)

  


**_Step 2:_**_Add the AI Decision Maker Action_

  


  1. Ensure a trigger is set (e.g., _Contact Changed_ or _Form Submitted_).  
  


  2. Click the **+** icon inside the workflow builder.  
  


  3. In the right-side panel, scroll to **AI Actions**.  
  


  4. Select **AI Decision Maker**.


  


Use a clear **Action Name** to keep branching-heavy workflows organized.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155065903852/original/G8V4nN8wSV8mKMONH_lyGqGiTZgOsISdHg.png?1772231259)

###   
**_Step 3:_**_Write Clear AI Instructions_

  


Use the **Instructions** field to describe how contacts should be routed.

  


Be specific about what the AI should evaluate, such as engagement score, industry type, or company size.

  


Use the variable picker (tag icon) to insert dynamic fields like:  
  


  


  * {{contact.engagement_score}}  
  


  * {{contact.company_size}}  
  


  * {{contact.tags}}


  


This ensures the AI evaluates real contact data.

  


### **Example Instruction**

  


Look at the contact’s engagement score and company size.

  


If the engagement score is over 60 OR they work at a large company, send them to sales.

  


If the engagement score is between 30–60 and it’s a small or medium company, send them to email nurturing.

  


If the engagement score is under 30, send them to a re-engagement campaign.

  


### **Important**  
  


The AI requires context to make informed decisions. Always include relevant contact fields, custom fields, tags, or data from previous workflow steps.

  


Examples of useful variables:  
  


  


  * Contact details: {{contact.email}}, {{contact.phone}}  
  


  * Custom fields: {{contact.lead_score}}, {{contact.company_size}}  
  


  * Tags: {{contact.tags}}  
  


  * Data from prior steps (forms, surveys, etc.)  
  


![](https://jumpshare.com/share/bAacCuRQFPrlmvWOC1v0+/Screen+Shot+2026-01-06+at+9.21.41+PM.png)

###   
**_Step 4:_**_Add Additional Context_

  


  


Use the **Additional Context** field to provide supporting information that improves AI accuracy.

  


Include business rules, segmentation definitions, or operational constraints.

  


### **Example**

  


We sell software to companies with 10–500 employees.

  


Small companies have 1–50 employees.  
  


Medium companies have 51–200 employees.  
  


Large companies have 200+ employees.

  


Engagement scores range from 0–100.  
  


Our sales team can handle about 20 new leads per week.

  


Providing structured context improves routing accuracy.

  


  


![](https://jumpshare.com/share/JZs9kpsBQQ4BhjVciDx2+/Screen+Shot+2026-01-06+at+9.22.46+PM.png)  
  


### **_Step 5:_**_Default Branch_

  


The **Default Branch** is automatically included and acts as a fallback for contacts who do not meet other conditions.  
  


  


  * The branch name is locked as “Default Branch.”  
  


  * It ensures uninterrupted workflow execution.  
  


  * It cannot be deleted or renamed.


  


This branch prevents contacts from getting stuck.

  


![](https://jumpshare.com/share/7bDj1sXBqUnP6CxMI21r+/Screen+Shot+2025-09-12+at+1.36.27+PM.png)

  
  


### **Step 6:**_Add Custom Branches_

  


Create additional branches to route contacts based on specific criteria.  
  
  


Each branch should include:  
  


  


  * A clear **Branch Name** (e.g., “High Priority – Sales”)  
  


  * A short description explaining when contacts should enter that path


  


Example:  
  


Route to Sales if {{contact.engagement_score}} > 60 OR company size is Large.  
  


![](https://jumpshare.com/share/ZRdpyhh0a1xMIkhDmzRk+/Screen+Shot+2025-09-12+at+1.41.47+PM.png)

  


  


### **_Step 7:_**_Add More Branches_

  


Click **\+ New Branch** to define additional routing paths.

  


Use clear naming and concise descriptions for each branch. This allows you to tailor follow-ups such as:  
  


  


  * Discount offers  
  


  * Product education  
  


  * Case studies  
  


  * Re-engagement campaigns  
  


![](https://jumpshare.com/share/8aZdrSywTzpks0v6zWU2+/Screen+Shot+2025-09-12+at+1.43.52+PM.png)

  


### ** _Step 8:_**_Save the Action_

  


Once all instructions and branches are configured, click **Save Action**.

  


The workflow will now automatically evaluate contacts and route them based on AI-driven decision logic.  
  
![](https://jumpshare.com/share/8wbPvJBdqIUuxcoNJKXl+/Screen+Shot+2025-09-12+at+1.46.30+PM.png)

* * *

## **Popular Use Case**

  


### **Spam Submission Detection**

  


Use AI Decision Maker to evaluate website form submissions.  
  


  


  1. Route form details into the AI Decision Maker.  
  


  2. Instruct the AI to classify submissions as spam or authentic.  
  


  3. Provide examples of spam to improve classification accuracy.  
  


  4. Create opportunities only for legitimate submissions.


  


This reduces manual review and protects pipeline quality.

* * *

## **Frequently Asked Questions**

  


**Q: How does the AI decide where to send someone?**

The AI reads your instructions and evaluates the included contact data to determine the most appropriate branch.

  


**Q: What if someone doesn’t match any rules?**

They are automatically routed to the Default Branch.

  


**Q: Can I delete or edit the Default Branch?**

No. The Default Branch is permanent and ensures fallback routing.

  


**Q: How do I check where a contact went?**

Use the **Execution Logs** tab within your workflow to review routing paths.

  


**Q: Can I use data from forms or surveys?**

Yes. Include variables from previous workflow steps using the variable picker.

* * *

## **Related Articles**

  


  * [Workflow Action - GPT Powered by OpenAI ](<https://help.gohighlevel.com/en/support/solutions/articles/155000000209>)  
  

  * [Workflow Action - Remove Opportunity](<https://help.gohighlevel.com/en/support/solutions/articles/155000003365>)  
[  
](<https://help.gohighlevel.com/en/support/solutions/articles/155000005885>)
  * [Workflow Action - AI Intent Detection](<https://help.gohighlevel.com/en/support/solutions/articles/155000005885>)  
  

  * [Workflow Action - AI Summarize](<https://help.gohighlevel.com/en/support/solutions/articles/155000005886>)  
  

  * [Workflow Action - AI Translate](<https://help.gohighlevel.com/en/support/solutions/articles/155000005892>)  
  

  * [Conversation AI: Multiple Messages in One Workflow Action](<https://help.gohighlevel.com/en/support/solutions/articles/155000003207>)

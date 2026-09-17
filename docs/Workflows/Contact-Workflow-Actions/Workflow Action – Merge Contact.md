# Workflow Action – Merge Contact

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007464-workflow-action-merge-contact](https://help.gohighlevel.com/support/solutions/articles/155000007464-workflow-action-merge-contact)  
**Category:** Workflows  
**Folder:** Contact Workflow Actions

---

Workflow Action – Merge Contact gives you an automated way to deduplicate contacts directly inside HighLevel workflows. It helps reduce CRM clutter, protect contact history, and keep follow-up actions running on the correct surviving record. This article explains what the feature does, when to use it, how to configure it, and how to verify merge activity in Execution Logs.

* * *

**TABLE OF CONTENTS**

  * What is Merge Contact Workflow Action?
  * Key Benefits of Merge Contact Workflow Action
  * Action Details
  * How to Use Merge Contact Workflow Action
  * Merge Behavior
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Merge Contact Workflow Action?**

  


Workflow Action – Merge Contact helps you automatically merge duplicate contacts while a workflow is running in HighLevel. Instead of manually cleaning up duplicate records from the Contacts area, this action checks the enrolled contact against existing records using your selected match criteria and merges the newer record into the older one when a duplicate is found. This keeps your CRM cleaner, reduces duplicate communication, and supports more accurate automation and reporting.

* * *

## **Key Benefits of Merge Contact Workflow Action**

  


  * **Automated deduplication** : Detects and merges duplicate contacts as they move through a workflow, reducing manual cleanup from the Contacts page.  
  


  * **Flexible matching options** : Lets you identify duplicates by Email, Phone Number, or Email and Phone Number, depending on how strict you want the match to be.  
  


  * **Cleaner CRM data** : Helps reduce duplicate records that can affect reporting, communication history, and workflow accuracy.  
  


  * **Protected workflow continuity** : Allows the workflow to continue on the surviving contact record after a merge.  
  


  * **Better operational visibility** : Makes it easier to review merge behavior using Workflow Execution Logs.


* * *

## **Action Details**

  


**Field**  
| **Description**  
  
---|---  
**Action Name**  
|  A custom name for the action. Defaults to “Merge Contact.”  
  
**Match By ***  
|  Select how duplicate contacts should be identified. Options:  


  * **Email** – Matches contacts that share the same email address.
  * **Phone Number** – Matches contacts that share the same phone number.
  * **Email and Phone Number** – Matches only if both email and phone number are identical.

  
  
* * *

## **How to Use Merge Contact Workflow Action**

  


Follow these steps to add the action to a workflow and configure it for consistent, predictable outcomes.

  


  1. Log in to your sub-account.  
  


  2. Go to **Automations > Workflows**.  
  
![](https://jumpshare.com/share/Cnveqtr2TxPJeI2Wif1E+/Screen+Shot+2026-01-05+at+6.02.58+PM.png)  


  3. Create a **new** **workflow** or **open** an **existing** one.  
  
![](https://jumpshare.com/share/vy9UlWTok3ZfxkZZpVLC+/Screen+Shot+2026-01-05+at+6.04.41+PM.png)  
  


  4. Click on the **\+ Add New Trigger** button to add a trigger that correlates to the **Merge Contact Action** (e.g., Contact Created, Form Submitted, Contact Changed.)  
  
![](https://jumpshare.com/share/50nKiylhvNfLjEt46hdJ+/GIF+Recording+2026-03-12+at+20.12.41.gif)  
  

  5. Add the **Contact Merged** Action.  
  


  6. In **Match Criteria** , choose one of the available options:  
  

     * **Email**

     * **Phone Number**

     * **Email and Phone Number**  
  


  7. **Save** the action.  
  
![](https://jumpshare.com/share/cFpLuIbxCZwZQKdSSq7H+/GIF+Recording+2026-03-12+at+20.16.41.gif)  
  


  8. **Publish** and **Save** the workflow.  
  
![](https://jumpshare.com/share/oPF0aXY55KEw5SOOONly+/Screen+Shot+2026-03-12+at+20.19.14.png)


* * *

## **Merge Behavior**

  


When the action executes, it follows this logic:

  


  1. The system searches for an existing contact that matches the enrolled contact based on the selected Match By criteria.  
  

  2. If a duplicate is found, the newer contact is always merged into the older contact. The older record is preserved as the primary, ensuring no historical data is lost.  
  

  3. If the enrolled contact is the older record, the duplicate is merged into it. If the enrolled contact is the newer record, it is merged into the older duplicate.  
  

  4. If no duplicate is found, the action completes with no changes – the contact moves to the next step in the workflow as-is.


  


## **Contact Merge Limitations**

  1. Goals may not work as expected if they were tied to the old contact ID before the merge.  
  

  2. Wait for reply steps can be affected if the email/SMS was sent before the merge, since the workflow may still be waiting on the original contact/message context.  
  

  3. Wait for email events may not resume as expected: the awaited event may still be associated with the old contact/message context.  
  

  4. Trigger link waits may fail as tracking links are generated with the original contact ID and message ID before the message is sent.  
  

  5. If the surviving contact is already in the same workflow, the execution being merged will end.  
  

  6. If the surviving contact was previously in the workflow and Allow Re-entry is turned off, the execution being merged will end.


* * *

## **Frequently Asked Questions**

  


**Q: Does Workflow Action – Merge Contact replace Contact Deduplication Preferences?**  
No. Deduplication preferences help reduce duplicate creation at the source, while Merge Contact handles duplicates automatically during workflow execution.  
  


**Q: When should I use this action instead of the Duplicate Management & Merge Tool?**  
Use Merge Contact when you want automation to handle duplicates during a workflow. Use the Duplicate Management & Merge Tool when you want to manually review and merge records from the Contacts area.

  


**Q: What happens if no duplicate is found?**  
The action is skipped and the workflow continues normally.

  


**Q: Which contact record is kept after a merge?**  
The older contact record is preserved as the surviving record.

  


**Q: Can the workflow continue after a contact is merged?**

Yes. The workflow continues on the surviving contact record after the merge is completed.

  


**Q: What is the safest match option to use?**  
Email and Phone Number is typically the strictest option and may be safer when you want to reduce unintended merges, but the best option depends on the quality and consistency of your contact data.

  


**Q: Should I test this before using it in a live workflow?**  
Yes. Testing with sample contacts helps confirm your selected match criteria behave as expected before you apply the action to larger workflows.

  


**Q: Can I still use the Contacts duplicate-management tools after enabling this action?**  
Yes. Workflow-based merging and manual duplicate management can be used together as part of a broader contact-cleanup strategy.

* * *

## **Related Articles**

  


  * [Contacts - Manage and Merge Duplicates ](<https://help.gohighlevel.com/en/support/solutions/articles/155000006647>)  
  


  * [Getting Started - Import Existing Contacts ](<https://help.gohighlevel.com/en/support/solutions/articles/155000005056>)  
  


  * [Workflow Action - Copy Contact To Sub Account](<https://help.gohighlevel.com/en/support/solutions/articles/155000003272>)  
  


  * [How To Delete Contacts and Their Data](<https://help.gohighlevel.com/en/support/solutions/articles/155000000583>)

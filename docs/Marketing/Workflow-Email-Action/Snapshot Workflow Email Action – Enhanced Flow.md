# Snapshot Workflow Email Action – Enhanced Flow

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005856-snapshot-workflow-email-action-enhanced-flow](https://help.gohighlevel.com/support/solutions/articles/155000005856-snapshot-workflow-email-action-enhanced-flow)  
**Category:** Marketing  
**Folder:** Workflow Email Action

---

Template management is now simpler. Only original templates and workflows appear in the target location, while linked email action templates are handled in the background.

Ask ChatGPT

####   
** _Overview_**  
The target location’s template list now only displays original templates and workflows, eliminating the clutter caused by email action templates. These email action templates are still imported and mapped in the background, but they remain hidden from users. This enhancement streamlines the template management process and improves the syncing of workflows and templates.

####   


  


**TABLE OF CONTENTS**

  * Overview
  * Benefits
  * What’s New
  * How to Use
  * Note
  * Limitations
  * FAQs


  


#### ** _Benefits_**

  * #### **Clean Interface:** The target location now shows only original templates and workflows.

  * **Reduced Clutter:** Only core templates and workflows are visible, improving navigation.

  * **Reliable Syncing:** Email action templates are automatically mapped and synced with workflows.


####   


#### **_✅What’s New_**

  * **Clean Target List View:** Only original templates are displayed in the target location’s template list, while email action templates are hidden but still imported in the background.

  * **Streamlined Snapshot Listing:** The snapshot modal now only shows original templates and workflows. Email action templates remain hidden but are imported and mapped in the background.

  * **Improved Sync Logic:** Syncing works as expected when both the workflow and template are pushed together, or if the template is pushed before the workflow.


####   
**_⚒️How to Use_**

  1. **Take a Snapshot:** From the source location, select the workflows and templates to snapshot.

  2. **View in Target Location:** In the target location, only original templates and workflows will appear in the template list.

  3. **Automatic Background Management:** Email action templates are automatically imported and mapped in the background. For email actions to work correctly, push the workflow and its linked template together, or push the template before the workflow.**  
**


#### _  
_

#### **_NOTE :_**

####  To apply the latest changes, delete the older workflows and linked email actions in the target location, then re-push them using the updated snapshot.

  


  


#### **_⏳Limitations_**

  * **Email Action Availability:** Email actions are not available if you push only the workflow without its linked template. Mapping and sync also fail if the template is pushed after the workflow.

  * **Sync Failures****:** Push the linked template before the workflow, or push both together. If the template is pushed after the workflow, mapping and sync fail.

  * **Bulk Deletion Not Supported:** Email actions do not currently support bulk deletion.


####   
**_❓FAQs_**

####   
**Q: Will email action templates still be imported?**  
Yes, email action templates will still be imported in the background and mapped to the relevant workflows, but they will not appear in the template list.

####   
**Q: What happens if I push only a workflow without its template?**  
If you push only a workflow without its associated template, email actions will not be available, and syncing will fail.

####   
**Q: Can I bulk delete email action templates?**  
********Bulk deletion of email action templates is not currently supported.********

####   
**Q: How do I apply the latest changes?**  
********To apply the latest changes, delete old workflows and email actions, and then re-push them using the updated snapshot.********

  


**Q: Are Conditional Sending rules preserved when I push email templates through snapshots?**

Conditional Sending rules in email templates are retained when you push templates from one location to another through snapshots, so visibility logic remains intact in the target location.

####   
****Q: Is the syncing process affected if the template is pushed after the workflow?****  
******Yes, syncing will fail if the template is pushed after the workflow. For proper syncing, ensure the template is pushed before the workflow or both are pushed together.******

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155050910394/original/FzGnQNGqbCsZG0jxRFErxNMkYETon4ZHkw.png?1754332069)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155050910424/original/HGMyr4Pb2sXIB0c4a2GGVS9u0_PBQG5U9w.jpeg?1754332109)

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155050910434/original/hm-1E7frTuGBaKnIzLPfd3bvFw0NR2QiWw.png?1754332141)

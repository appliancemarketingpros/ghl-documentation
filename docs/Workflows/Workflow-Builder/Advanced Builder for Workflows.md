# Advanced Builder for Workflows

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006635-advanced-builder-for-workflows](https://help.gohighlevel.com/support/solutions/articles/155000006635-advanced-builder-for-workflows)  
**Category:** Workflows  
**Folder:** Workflow Builder

---

Building and optimizing workflows just became faster and more collaborative. The Advanced Builder UI/UX Upgrades introduce a cleaner Stats Mode, image-ready Sticky Notes, inline Workflow Comments, and a right-click Quick Actions menu—everything you need to plan, document, and iterate without leaving the canvas.

* * *

  


* * *

**TABLE OF CONTENTS**

  * What is the Advanced Builder in Workflows?
  * Access & Requirements
  * The Canvas
  * Go-To connections for Triggers & Delinked Nodes (Parallel branches)
  * Delinked nodes (independent/parallel branches)
  * Enable / Disable Nodes
  * Sticky Notes & Color Coding
  * Keyboard Shortcuts & Power Navigation
  * Tidy Up (Auto-layout)
  * Workflow Switcher
  * Notes, Limits & Best Practices


* * *

## **What is the Advanced Builder in Workflows?**

  


The Advanced Builder is a fully visual, freeform canvas for building automations. Drag, drop, and connect multiple trigger paths, parallel branches, and complex logic in one view—without changing how workflows execute. It’s designed for flexibility, performance, and collaboration.

  


Bulk Selection Tools add context-aware actions—Enable/Disable, Format Selection, and Add Sticky Note. By acting on many nodes at once you can refactor branches, declutter spacing, and annotate logic in seconds—ideal for very large workflows.

  


This upgrade comprises four enhancements within the HighLevel Workflow Builder: Stats Mode, Sticky Notes 2.0, Workflow Comments, and Right-Click Quick Actions. Together, they streamline performance reviews, team collaboration, and day-to-day editing, all while keeping your workspace visually organized.

* * *

## **Access & Requirements**

  


  * **Where:** Open any workflow → toggle to **Advanced Builder** (top-left).  
  


  * **Switching views:** You can toggle between **Standard** and **Advanced** on the same workflow. (See **Additional Notes** below for Advanced-only features.)


  

    
    
    **Workflow name display:** Long workflow names in the builder header truncate with an ellipsis (…). Hover the name to view the full workflow title.

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155059091928/original/g9xV1gW00pqV9v6MUOC1DpzdE4PU5_0o3w.gif?1763993150)

  


  


  


* * *

## **Stats View**

  


Stats View helps you review trigger enrollment activity and communication-action performance without leaving the Workflow Builder. 

  


To use Stats View: 

  
1\. Open a workflow in the Advanced Builder. 

  


2\. Open Stats Mode. 

  


3\. Select a trigger or one of its displayed statistics. 

  


4\. Review the attempted, matched, and unmatched enrollment results.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076677185/original/JVfuhVn41VeAXURlhr6vgP0p69mNKwWgug.png?1784803303)

  
  


For workflow triggers, Stats View displays:  
  
**Attempted** : Contacts evaluated by the trigger.  
  
**Matched** : Contacts that met the trigger conditions.  
**Unmatched** : Contacts that did not meet the trigger conditions.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076676939/original/iryJCqCZTBHz64Ymx6MCANVvlcKWbWCtvw.gif?1784803137)

  
  


Click a trigger statistic to open its detailed view. You can review contact-level results, search for a specific contact, and investigate why contacts did not match.

  


For communication actions, Stats View displays the available delivery and engagement statistics for that action. Click a statistic to open its detailed report.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076675829/original/IuY1sQN1fo6nTS01f_BMvAEK4WpB0Mx7Ew.png?1784802571)

  
  


For tips on analyzing workflow performance, explore [How to Analyze Workflow Campaigns](<https://help.gohighlevel.com/support/solutions/articles/155000003902>). Stats are also available at the workflow level in the Workflow List Click the expand arrow under Stats.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155039915452/original/9rcKt_uTXnQ_WVrfXVHUnUyXksG_8oR64w.png?1737003186)

  
  

    
    
    Note that if a communication action was in the workflow, and used, and then deleted, the stats will still be saved in the workflow.
    
    You cannot edit a workflow while Stats View is active. Trigger Stats includes data from the last 30 days.
    
    For complete Trigger Stats instructions, see [Workflow Trigger Narration and Statistics](<https://help.gohighlevel.com/support/solutions/articles/155000006636-workflow-trigger-narration-and-statistics>).

* * *

## **The Canvas**

  


**Add & connect steps**

  


  * Open the **Triggers & Actions** panel.  
  


  * Configure from the panel **or** drag items directly onto the canvas.  
  


  * Connect nodes by dragging from the connector handle (or the **+** icon).

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055989412/original/neH1lwsEiNitnKprmoJTFVi9jfqESgVFFw.gif?1760459760)


  


  


### **Auto-connect steps (drag and drop)**

  


When you drag a trigger or action from the Triggers & Actions panel (sidebar) onto the canvas, it can auto-connect based on where you drop it:

  


  * Extend a branch: Drop the step on the last node in a branch to add it to the end.  
  

  * Insert between steps: Drop the step between two connected nodes to insert it in the middle.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067225359/original/7dBST391yMsPbyKqWGs2l9_I7Go3Rr146A.gif?1773842268)  
  


**Important**

  


  * Multi-select (marquee/Shift-drag) to move blocks of nodes.  
  


  * Copy/paste branches **across workflows** to reuse patterns  
  


  * Configure and save the new step after dropping it onto the canvas.  
  


  * Unconfigured actions will not run. Workflows do not execute incomplete (unconfigured) actions.


* * *

## **Go-To connections for Triggers & Delinked Nodes (Parallel branches)**

  


Trigger Go-To (set each trigger’s starting action)

  


  


  


Route a trigger to the **exact action** where it should start.

  


  * **Connect it:** Drag the trigger’s **Go-To** connector onto a target action.  
  


  * **How it looks:** Trigger Go-To connections are shown as a **dashed line with an arrowhead** (normal sequential links remain **solid**).  
  


  * **Execution Behavior:** When the trigger fires, the workflow **jumps directly** to the target action and continues from there.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069380101/original/nIFVEOUuPvWiIu47LrwtYX55qvbXqcSBbQ.jpeg?1776429175)

  


  

    
    
    **Note** : For more information do visit, [Go-To Connections for Triggers: Advanced Builder Workflow](<https://help.gohighlevel.com/support/solutions/articles/155000006690-go-to-connections-for-triggers-advanced-builder-workflow>)

* * *

## **Delinked nodes (independent/parallel branches)**

  


Create branches that don’t need to connect linearly—great for handling multiple triggers or outcomes in one canvas.

  


  * Build an **independent cluster** of actions anywhere.  
  


  * Attach a trigger via **Go-To connection** to start on that branch.  
  


  * Each branch runs **independently** within the same workflow context.  
  


![Delinked branch example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755867/original/x7qC1lGEGE-dcEXb3gKSm1t-XB6tFBK3Lg.jpeg?1760134183)

  


  


**Visual cues (at a glance)**

  


  * **Solid connector** → normal sequential path  
  


  * **Dashed connector with arrow** → **Trigger Go-To** (jump to target action)  
  


  * **Isolated cluster** → **Delinked** branch


  


  


## **Default Path for Parallel Branches (Advanced Builder)**

  


In Advanced Builder workflows with multiple parallel branches, you can choose the Default Path. The Default Path controls which branch contacts enter when:

  


\- you run a workflow test, or

\- a contact enters this workflow from another workflow.

  


**How it works**

\- The root node is labeled Default Path.

\- On the first node/action in each branch, click the branch icon to set that branch as the Default Path.

\- After you set a Default Path, workflow tests and contacts entering from another workflow follow that branch.

  


**Visual indicators**

\- A solid trigger connector means the branch is the Default Path.

\- A dashed trigger connector means the branch is reached through a Go To connector and is not the default path.

  


**How to set the Default Path**

  


1\. Open a workflow with multiple parallel branches in Advanced Builder.

2\. On the first action of the branch you want to use, click the branch icon.

3\. Set that branch as the Default Path.

4\. Run a workflow test or enroll a contact from another workflow to validate the path.

  


**Example**

If your workflow has multiple reminder branches, set one branch as the Default Path so your test contact enters that reminder branch first.

  


* * *

## **Enable / Disable Nodes**

  


  


  


Turn any action/condition **off** for testing—without deleting or rewiring.

  


  * **Disable:** Hover a node → click **pause**.  
  


  * **Enable:** Hover again → click **play**.  
  


  * **Execution:** Disabled nodes are **skipped** ; connections remain intact.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069380308/original/pIAzyiTju06bN5sLZiyBuWJjv48rI_8vQQ.gif?1776429288)

* * *

## **Sticky Notes & Color Coding**

  


Use notes to explain logic for teammates and future you.

  


  * Add a note from the **left sidebar**.  
  


  * Choose color/style, then enter text.  
  


  * Notes support **images and links**.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055990171/original/lWesgzRmMXSAmj5Roh_xnlzy2AwJRdhL0w.png?1760460252)

* * *

## **Keyboard Shortcuts & Power Navigation**

  


  


  


  


Open the keyboard icon (top-left) for the full list—Navigation, Tools, View, and Edit.

  


![Keyboard shortcuts](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755866/original/jS5kgFi-XYcAbSG8fqWuNvljI1kIzG0Nmg.jpeg?1760134183)

  


  


**Examples**

  


  * Arrow keys to move selection  
  


  * Cmd/Ctrl + C / V for copy/paste  
  


  * Next/Previous action buttons for fast traversa


  

    
    
    **Note** : For more do visit, [Keyboard Shortcuts in Workflow Builder](<https://help.gohighlevel.com/support/solutions/articles/155000006694-keyboard-shortcuts-in-workflow-builder>)

* * *

## **Tidy Up (Auto-layout)**

  


One click to clean up cluttered canvases—great after heavy edits or imports.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755927/original/2O9bzUQHsnEsu9mogf3zDITWB85uRtVdaA.gif?1760134584)

* * *

## **Workflow Switcher**

  


Navigate between workflows **without leaving the builder**.

  


  * Open the **Workflow Switcher** (left sidebar).  
  


  * See recent workflows or **search** by name/tag.  
  


  * Clicking a result opens it in a **new tab** —your current canvas stays open.


  


  


![Switcher entry point](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755871/original/Dho5NNvnSv5K45y8vi4bKnclX5f8umMTFg.jpeg?1760134184)

  


  


![Switcher panel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055755872/original/hA5bo8dIsuJMnwdxwSCqHYcre8I8CE4pAA.jpeg?1760134184)

> [](<https://help.gohighlevel.com/support/solutions/articles/155000001254-workflow-builder-walkthrough>)

* * *

## **Notes, Limits & Best Practices**

  


  * **Single enrollment per contact.** Even with parallel branches, the same contact won’t run **concurrently** through multiple branches of the same workflow.  
  


  * **Switching to Standard Builder:** Remove Advanced-only features (**Trigger Go-To** , **Delinked nodes** , **Disabled nodes**) before switching back.  
  


  * **Organize early:** Use color-coded notes and **Tidy Up** to keep complex maps readable.  
  


  * **Name clearly:** Give triggers/actions descriptive names (this helps in both canvas and Version History). [](<https://help.gohighlevel.com/support/solutions/articles/155000001254-workflow-builder-walkthrough>)

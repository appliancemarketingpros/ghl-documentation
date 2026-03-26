# How to Clone and Share Agent Studio Agents Using Snapshots

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007504-how-to-clone-and-share-agent-studio-agents-using-snapshots](https://help.gohighlevel.com/support/solutions/articles/155000007504-how-to-clone-and-share-agent-studio-agents-using-snapshots)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

Clone, distribute, and deploy your best-performing AI agents across sub-accounts using Account Snapshots. This guide explains how to package Agent Studio agents, include their dependencies, load them into other accounts, and share or sell them through Snapshot links or the Marketplace.

* * *

**TABLE OF CONTENTS**

  * What Are Agent Studio Snapshots?
  * Key Benefits of Using Snapshots with Agent Studio
  * How to Create an Agent Snapshot
  * How to Load Agent Snapshots into Sub-Accounts
    * Option 1: Load Into a Single Sub-Account
    * Option 2: Push Snapshot to Multiple Sub-Accounts
  * Conflict Resolution During Import
  * Snapshot Versioning and Refresh
  * Sharing or Selling Agent Snapshots
  * What Is Not Included in Snapshots
  * Permissions Required
  * Frequently Asked Questions
  * Related Articles


* * *

# **What Are Agent Studio Snapshots?**

  


Agent Studio Snapshots allow you to package one or more AI agents inside an Account Snapshot so they can be loaded into other sub-accounts.

  


When included in a snapshot, the following are preserved:

  


  * Agent flow structure

  * Node configurations

  * Connected knowledge bases

  * Version state (Draft, Staging, Production)

  * Associated supporting assets (if selected)


  


This removes the need to manually rebuild agents in every new account.

* * *

## **Key Benefits of Using Snapshots with Agent Studio**

  


Using snapshots to distribute agents helps agencies scale faster and maintain consistency.

  


  * **Clone agents instantly:** Copy complex AI agents to other accounts in minutes.


  


  * **Preserve configurations:** Agents retain their version states and logic.


  


  * **Include dependencies:** Knowledge bases and selected assets move with the agent.


  


  * **Standardize onboarding:** New clients can start with fully configured AI automations.


  


  * **Enable distribution and monetization:** Share or sell snapshots externally.


* * *

## **How to Create an Agent Snapshot**

  


Follow these steps to package your Agent Studio agent.

##   


### **Step 1: Go to Account Snapshots**

  


  1. Switch to **Agency View**

  2. Navigate to **Account Snapshots**

  3. Click **Create New Snapshot**


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066819121/original/HleAevJiPdYqrKr6yERei_HgxdWf0ItOwA.png?1773334189)

**  
**

  


### **Step 2: Name and Select Source Account**

  


  1. Enter a Snapshot Name

  2. Select the Sub-Account that contains your agent

  3. Click **Next**


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066819528/original/-3Nvfr6v8TfkHQUk8mvZX-TdVC2J8AiqVQ.png?1773334423)

  


  


### **Step 3: Select Agent Studio Assets**

  


  1. Expand the **Agent Studio** category

  2. Select the agent(s) you want to include

  3. Select any supporting assets (e.g., Knowledge Bases, Workflows, Custom Values)

  4. Click **Create** tab at the bottom right.


  


The system will package the selected agents and assets into the snapshot.

##   


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066819942/original/SlEEvHp3IJoXKKHX2SHt6bdpcEMP-LjuDw.png?1773334679)

  


  


  

    
    
    If your agent uses a Knowledge Base, you must select that Knowledge Base when creating the snapshot.
    
    Snapshots package only the assets you choose.
    
    If a connected knowledge base is not selected, the agent may load without its reference material.
    
    Always review the asset selection screen before proceeding.
    
    ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066838299/original/awGX4bvcPjZjTuR9X__U2w4lnVrFoZQHVg.png?1773368022)

  


  


### **Step 4: Review Snapshot Details**

  


After creation, you can view the snapshot details screen.

  


This screen confirms:

  


  * Included agents

  * Included knowledge bases

  * Total asset count


* * *

## **How to Load Agent Snapshots into Sub-Accounts**

  


You can load a snapshot into one or multiple sub-accounts.

##   


### **Option 1: Load Into a Single Sub-Account**

  


  * Go to **Agency View → Sub-Accounts**


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066838348/original/b3ysmTJbUNGOoaztWYjLZTm_vmWP-0x0dw.png?1773368390)

  


  


  * **Click the three-dot menu beside the account.******Select**Manage Client option.******


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066838382/original/TY9XBjHiWjLqh5z1i1EhWozAjazwGEWjTA.png?1773368520)

  


  


  * **********Choose**Actions → Load Snapshot************


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066838434/original/1nJUggswqmXRs19WqKdwhOfQBO62tkAL0g.png?1773368685)

  


  


  * ************Select your snapshot.************


  


  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066838458/original/TDnGVjFheDThnS-zlInvlNm74t6egphrHA.png?1773368798)

  


  


  * ************Select the Agent Studio category (or Select All).******************Confirm import******


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066838579/original/0RPunN1c3JMGsagchAbL1iJPIyxUvG1xFg.png?1773369214)

  


After loading, the agent will appear in Agent Studio inside the target sub-account.

##   


### **Option 2: Push Snapshot to Multiple Sub-Accounts**

  


  1. Go to **Account Snapshots**

  2. Open the snapshot

  3. Click **Push Snapshot**

  4. Select the sub-accounts

  5. Select assets

  6. Proceed through conflict check


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066838680/original/5HmXCmjbP5dgBLNWv7Loo3FNE4t4psGl_Q.png?1773369590)

  


  


This method allows bulk deployment.

* * *

## **Conflict Resolution During Import**

  


If an asset with the same name already exists in the target account, HighLevel will prompt you to resolve conflicts.

  


You may choose to:

  


  * Keep both copies

  * Overwrite existing

  * Proceed with conflict check


  


Always review conflicts before finalizing.

* * *

## **Snapshot Versioning and Refresh**

  


Each snapshot maintains versions.

  


When you update an agent in the source account:

  


  1. Return to **Account Snapshots**

  2. Select the snapshot

  3. Click **Refresh**


  


This updates the snapshot to reflect the latest agent configuration and creates a new version.

  


You can then push the updated version to sub-accounts.

* * *

## **Sharing or Selling Agent Snapshots**

  


Snapshots can be shared outside your agency.

  


To share:

  


  1. Go to **Account Snapshots**

  2. Click the three-dot menu

  3. Choose **Share Snapshot**

  4. Generate a share link or Marketplace listing


  


Recipients can load the snapshot into their own HighLevel accounts.

  


Note: SaaS plan requirements apply for Marketplace monetization.

* * *

## **What Is Not Included in Snapshots**

  


Snapshots do NOT include:

  


  * Contacts

  * Conversation history

  * Messages

  * Live data


  


Only configuration and selected assets are transferred.

* * *

## **Permissions Required**

  


Users must have:

  


  * “Create Snapshots” permission to create


  


  * “Share/Import Snapshots” permission to load or share


  


Permissions are managed by an admin.

* * *

## **Frequently Asked Questions**

  


**Q: Does loading a snapshot overwrite existing agents?**

Only if an agent with the same ID exists. You will be prompted to resolve conflicts.

  


**Q: Are knowledge bases included automatically?**

Only if selected during snapshot creation.

  


**Q: Can I load snapshots outside my agency?**

Yes, using share links or Marketplace distribution.

  


**Q: Are version states preserved?**

Yes. Draft, Staging, and Production states remain intact.

  


**Q: Does importing affect API endpoints?**

API endpoints remain available, but account-specific tokens may need updating.

* * *

## **Related Articles**

  


  * [Snapshots Overview](<https://help.gohighlevel.com/a/solutions/articles/48000982511?portalId=48000045315>)
  * [Creating New Snapshots in HighLevel](<https://help.gohighlevel.com/a/solutions/articles/48000982512?portalId=48000045315>)
  * [How to Share Snapshots](<https://help.gohighlevel.com/a/solutions/articles/48000982513?portalId=48000045315>)
  * [How to Load Snapshots into Existing Accounts](<https://help.gohighlevel.com/a/solutions/articles/48000982582?portalId=48000045315>)
  * [How to Use the AI Agent Studio in HighLevel](<https://help.gohighlevel.com/a/solutions/articles/155000006058?portalId=48000045315>)

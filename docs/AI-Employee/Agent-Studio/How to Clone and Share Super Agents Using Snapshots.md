# How to Clone and Share Super Agents Using Snapshots

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008247-how-to-clone-and-share-super-agents-using-snapshots](https://help.gohighlevel.com/support/solutions/articles/155000008247-how-to-clone-and-share-super-agents-using-snapshots)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

Super Agents can be packaged inside HighLevel Account Snapshots and deployed across multiple subaccounts. This helps agencies reuse proven AI configurations, streamline client onboarding, and maintain consistent agent behavior without rebuilding each agent manually. Super Agents are available under the **Agent Studio** asset category during Snapshot creation, refresh, and loading workflows.

* * *

**TABLE OF CONTENTS**

  * What Are Super Agents in Snapshots?
  * Key Benefits of Super Agents in Snapshots
  * What Transfers with a Super Agent?
  * Super Agents in the Snapshot Asset Selector
  * Conflict Checking When Loading Super Agents
  * Refreshing a Snapshot After Updating a Super Agent
  * How To Set Up Super Agents in Snapshots
  * Create a Snapshot That Includes a Super Agent
  * Load the Super Agent into Another Subaccount
  * Verify the Super Agent in the Destination Subaccount
  * Frequently Asked Questions
  * Related Articles


  


* * *

# **What Are Super Agents in Snapshots?**

  


Super Agents in Snapshots are reusable Agent Studio assets that can be copied from a source subaccount into other HighLevel subaccounts. A Snapshot packages the selected agent configuration so agencies can deploy the same AI-powered experience across clients, locations, or standardized account templates.

  


When a Super Agent is included in a Snapshot, HighLevel preserves its agent structure, configuration, connected Knowledge Bases, and version state. Supporting assets must also be selected when they are needed by the agent.

* * *

## **Key Benefits of Super Agents in Snapshots**

  


Packaging Super Agents in Snapshots reduces repetitive setup work while helping agencies deliver consistent AI experiences across multiple accounts.

  


  * **Faster client onboarding:** Deploy prebuilt Super Agents without recreating their configuration for every new client.  
  


  * **Consistent AI experiences:** Reuse tested prompts, instructions, triggers, capabilities, and agent behavior across subaccounts.  
  


  * **Scalable deployment:** Distribute one or more Super Agents to multiple clients or business locations.  
  


  * **Flexible asset selection:** Include individual Super Agents independently or package them with other Snapshot assets.  
  


  * **Simplified updates:** Refresh a Snapshot after changing an agent in the source subaccount, then distribute the updated asset to linked accounts.  
  


  * **Reusable agency solutions:** Share configured agents through Snapshot links or include them in broader account templates.


  


* * *

## **What Transfers with a Super Agent?**

  


Understanding what a Snapshot preserves helps you prepare the source subaccount and identify any supporting assets that must be selected separately.

  


A Super Agent Snapshot can preserve:

  * Agent flow structure

  * Node configurations

  * Prompts and instructions

  * Triggers

  * Skills and capabilities

  * Connected Knowledge Bases when the required Knowledge Base assets are selected

  * Agent version state, such as Draft, Staging, or Production

  * Selected supporting assets


  


Snapshots transfer selected configuration assets rather than live account activity or customer records. Integrations, third-party connections, credentials, and other account-specific resources may require additional setup in the destination subaccount.

  

    
    
    **Important:** Review the agent’s dependencies before creating the Snapshot. If the Super Agent relies on a Knowledge Base, workflow, Custom Value, or another selectable asset, include that supporting asset in the Snapshot.

* * *

## **Super Agents in the Snapshot Asset Selector**

  


The Snapshot asset selector organizes supported assets by product category. Super Agents appear beneath **Agent Studio** , allowing you to expand the category and select only the agents needed for a particular deployment.

  


You can use this asset selector when:

  * Creating a new Snapshot  
  


  * Refreshing an existing Snapshot  
  


  * Loading a Snapshot into a subaccount  
  


  * Pushing selected Snapshot assets to linked subaccounts


  


HighLevel also supports selecting individual assets rather than loading every asset contained in the Snapshot.

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076472939/original/W8W6GVxjQGXSa7Q9SG6CuMx2LnD-Bk6FLw.png?1784628209)**

* * *

## **Conflict Checking When Loading Super Agents**

  


Conflict checking helps identify selected Snapshot assets that may overlap with assets already present in the destination subaccount. Reviewing conflicts before loading reduces the risk of unintentionally replacing an existing configuration.

  


The asset-selection screen provides two options:

  * **Proceed to check conflicts:** Continue to the conflict-review step before loading the selected Super Agents.  
  


  * **Proceed without conflict check:** Start the load without reviewing possible conflicts first.


  


Use conflict checking when loading a Snapshot into an active subaccount that may already contain a related agent or earlier version. General Snapshot loading supports reviewing conflicting assets and deciding which selected items should be applied. 

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076473369/original/BFlJGmzaZi2z-raffc0oC2RaiMcyILsSxw.png?1784628379)**

  


After choosing to check conflicts, expand the destination subaccount to review the identified items and select the assets you want to apply.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076473649/original/JyEnlZza1H6n80C1GxTQAozsV6cK_qkqOQ.png?1784628471)

* * *

## **Refreshing a Snapshot After Updating a Super Agent**

  


Snapshots do not update automatically when an agent changes in the source subaccount. Refreshing the Snapshot captures the latest selected configuration and creates an updated Snapshot version for future loads or pushes.

  


**To refresh a Super Agent:**

  1. Make the required changes to the agent in the original source subaccount.  
  


  2. Return to **Agency View > Account Snapshots**.  
  


  3. Locate the Snapshot and click its **Refresh** icon.  
  


  4. Expand **Agent Studio**.  
  


  5. Select the updated Super Agent.  
  


  6. Select any new or modified supporting assets.  
  


  7. Click **Refresh**.  
  


  8. Wait for HighLevel to finish fetching the selected assets.


  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076473857/original/gZ1q_wBrMO7jXd5VKpRDQLkUDg3-EQ98Kw.png?1784628576)**

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076474098/original/XthFMSkWPAS-1Y6T_wbaPGkMxfZYRAp0LQ.png?1784628720)**  


After refreshing, use the applicable Snapshot loading or push-update workflow to distribute the selected changes. Updates pushed from an agency Snapshot are available to linked subaccounts within that agency; external recipients generally need an updated shared Snapshot.

* * *

## **How To Set Up Super Agents in Snapshots**

  


Preparing the source agent and selecting its required assets helps ensure that the destination subaccount receives a complete, usable configuration. Review the agent before creating the Snapshot, then verify its settings after loading.

###   


### **Create a Snapshot That Includes a Super Agent**

  1. Open the source subaccount and confirm that the Super Agent contains the configuration you want to reuse.  
  


  2. Switch to **Agency View**.  
  


  3. Navigate to **Account Snapshots**.  
  


  4. Click **Create New Snapshot**.  
  


  5. Enter a descriptive Snapshot name.  
  


  6. Select the source subaccount containing the Super Agent.  
  


  7. Continue to the asset-selection step.  
  


  8. Expand **Agent Studio**.  
  


  9. Select the Super Agent or Super Agents you want to include.  
  


  10. Select any supporting assets required by the agents, such as applicable Knowledge Bases, workflows, or Custom Values.  
  


  11. Review the selected assets.  
  


  12. Click **Create** to save the Snapshot.


  


HighLevel creates Snapshots from assets already configured in a source subaccount; the Snapshot itself is not built independently from scratch.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076474265/original/OE0JF1k_PgdFextNgRGehvtzC1_ik7UvCQ.png?1784628816)

* * *

### **Load the Super Agent into Another Subaccount**

  1. From **Agency View** , open **Sub-Accounts**.  
  


  2. Locate the destination subaccount.  
  


  3. Open its three-dot menu and select **Manage Client**.  
  


  4. Open **Actions** and select **Load Snapshot**.  
  


  5. Choose the Snapshot containing the Super Agent.  
  


  6. Select the destination subaccount when prompted.  
  


  7. At the **Assets** step, expand **Agent Studio**.  
  


  8. Select the Super Agents you want to load.  
  


  9. Choose one of the following:

     * Click **Proceed to check conflicts** to review possible conflicts.  
  


     * Click **Proceed without conflict check** to continue directly.  
  


  10. When using conflict checking, expand the destination subaccount and review the available selections.  
  


  11. Click **Proceed** to start loading the selected assets.  
  


  12. Wait for the loading process to finish.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076474600/original/vIP43johIVbtdDc7cSES06LkXe3IninAQw.png?1784628984)**

* * *

### **Verify the Super Agent in the Destination** **Subaccount**

  1. Open the destination subaccount.  
  


  2. Navigate to **AI Agents > Agent Studio**.  
  


  3. Open the **Super Agents** tab.  
  


  4. Confirm that the transferred agent appears in the list.  
  


  5. Open the agent and review its:

     * Name and description

     * Triggers

     * Skills

     * Capabilities

     * Knowledge Base configuration

     * Instructions

     * Required integrations or account-specific connections  
  


  6. Test the agent in the destination account.  
  


  7. Publish or activate it when it is ready for use.


  


Some copied assets may require integrations, permissions, approvals, credentials, or destination-specific configuration before they can operate correctly.

******![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076474707/original/QQeLExgm4XzMmYg1kF7hMNABhnihojWoMw.jpeg?1784629036)******

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076474806/original/0jRgSjcRDYwraOlj1fsNRBYp6wX-w1HH4Q.png?1784629102)**  


* * *

## **Frequently Asked Questions**

  


**Q: Can I include more than one Super Agent in a Snapshot?**  
A: Yes. Expand the Agent Studio category and select the individual agents you want to package.

  


**Q: Do I need to include every Snapshot asset when copying a Super Agent?**  
A: No. Snapshot asset selection is granular. Select the Super Agent and any supporting assets it needs rather than loading unrelated assets.

  


**Q: Why is my transferred agent missing its Knowledge Base content?**  
A: Confirm that the required Knowledge Base was selected when the Snapshot was created or refreshed. Snapshots package the assets selected in the asset picker.

  


**Q: Should I use conflict checking when loading a Super Agent?**  
A: Conflict checking is recommended when the destination account may already contain a related agent or earlier version. It gives you an opportunity to review possible overlaps before the selected assets are applied.

  


**Q: Does editing the source Super Agent automatically update the Snapshot?**  
A: No. Refresh the Snapshot and select the modified agent to capture its latest configuration.

  


**Q: Will a transferred Super Agent run immediately?**  
A: Review and test the agent after loading. Account-specific integrations, permissions, credentials, or other connections may need to be configured in the destination subaccount before the agent can operate as intended. 

  


**Q: Can I push an updated Super Agent to multiple subaccounts?**  
A: Yes. After refreshing the Snapshot, use the push-update workflow to select linked subaccounts and the assets that should receive the update.

  


**Q: Can Super Agents be distributed through shared Snapshots?**  
A: Agent Studio agents can be packaged for distribution through Snapshot links, and the dedicated Agent Studio Snapshot workflow also supports broader sharing or Marketplace use. Review all dependencies before distributing the Snapshot.

* * *

### **Related** **Articles**

  * [Snapshots – Overview](<https://help.gohighlevel.com/support/solutions/articles/48000982511-snapshots-overview>)

  * [Creating New Snapshots in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/48000982512-creating-new-snapshots-in-highlevel>)

  * [Load Snapshots Into Existing Sub-Account](<https://help.gohighlevel.com/support/solutions/articles/48000982582-load-snapshots-into-existing-sub-account>)

  * [Refresh or Update Snapshots](<https://help.gohighlevel.com/support/solutions/articles/48000982583-refresh-or-update-snapshots>)

  * [How to View Snapshot Assets](<https://help.gohighlevel.com/support/solutions/articles/155000005917-how-to-view-snapshot-assets>)

  * [How to Share Snapshots](<https://help.gohighlevel.com/support/solutions/articles/48000982513-how-to-share-snapshots>)

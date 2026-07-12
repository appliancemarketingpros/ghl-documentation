# Graph Builder Copy, Paste, and Bulk Delete in Agent Studio

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007645-graph-builder-copy-paste-and-bulk-delete-in-agent-studio](https://help.gohighlevel.com/support/solutions/articles/155000007645-graph-builder-copy-paste-and-bulk-delete-in-agent-studio)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

Graph Builder copy, paste, and bulk delete help users quickly duplicate, reuse, and remove selected nodes inside the Agent Studio canvas. Use these editing tools to reuse proven node groups, clean up outdated branches, and speed up agent-building workflows without rebuilding sections manually. These tools are designed for selected nodes or flow sections, not for cloning an entire agent.

* * *

**TABLE OF CONTENTS**

  * What are Graph Builder Copy, Paste, and Bulk Delete?
  * Key Benefits of Graph Builder Copy, Paste, and Bulk Delete
  * When To Use Copy, Paste, and Bulk Delete
  * Permissions and Important Notes
  * Supported Actions and How They Work
    * Copy one or more nodes
    * Paste copied nodes into the same graph
    * Paste copied nodes into another Agent Studio tab
    * Preserve copied connections
    * Generate fresh IDs for pasted nodes
    * Delete multiple selected nodes
    * Use keyboard shortcuts
  * How to Set Up Graph Builder Copy, Paste, and Bulk Delete
  * Shortcut Reference
  * Best Practices for Reusing Node Groups
  * Frequently Asked Questions
  * Related Articles


* * *

## **What are Graph Builder Copy, Paste, and Bulk Delete?**

Graph Builder copy, paste, and bulk delete are canvas-level editing tools in Agent Studio. They allow users to copy selected nodes, paste them into the same or another supported Agent Studio tab, preserve connections between copied nodes, and delete multiple selected nodes at once.

  


Copied nodes are pasted with fresh IDs so they behave as separate nodes from the originals. This makes it easier to reuse flow sections while keeping the agent graph organized and editable.

* * *

## **Key Benefits of Graph Builder Copy, Paste, and Bulk Delete**

  


Graph Builder editing tools help users work faster when building or maintaining agent flows. Instead of recreating node groups manually, users can duplicate useful sections, update pasted settings, and remove unnecessary branches with fewer clicks.

  


  * **Faster graph building** : Copy existing nodes instead of recreating them from scratch.  
  


  * **Easier flow reuse** : Paste copied node groups into another Agent Studio tab to reuse logic across agents.  
  


  * **Preserved internal connections** : When you copy multiple connected nodes, the connections between the copied nodes are rebuilt automatically after paste.  
  


  * **Cleaner graph editing** : Bulk delete helps remove multiple unwanted nodes in one action.  
  


  * **Better canvas organisation** : Pasted nodes appear with an offset so they do not stack directly on top of the original selection.  
  


  * **Reliable duplication** : Newly pasted nodes receive unique IDs to help prevent conflicts in your graph.  
  


  * **More efficient keyboard-based editing** : Standard keyboard shortcuts make common graph actions quicker and more intuitive.


* * *

## **When To Use Copy, Paste, and Bulk Delete**

  


Copy, paste, and bulk delete are useful when you need to make repeated graph edits or reuse an existing flow pattern. These actions are best for selected node groups, test branches, and reusable sections of an agent graph.

  


Use these tools when you need to:  
  


  * Reuse a proven node group.  
  

  * Duplicate a flow section for testing.  
  

  * Rebuild a similar branch without starting from scratch.  
  

  * Copy a logic pattern into another Agent Studio tab.  
  

  * Remove unused or outdated node groups.  
  

  * Clean up test branches after debugging.  
  

  * Speed up repetitive graph-editing tasks.


* * *

## **Permissions and Important Notes**

  


Graph Builder editing actions depend on user access and the current Agent Studio editing context. Reviewing important behavior before copying, pasting, or deleting helps prevent accidental changes to the agent flow.

  


**Important notes:**

  


  * Users need access to Agent Studio and permission to edit the agent.  
  

  * Copy, paste, and bulk delete work inside the Graph Builder canvas.  
  

  * Copied nodes are pasted with fresh IDs.  
  

  * Connections between copied nodes are preserved when the connected nodes are included in the selection.  
  

  * Connections to nodes outside the copied selection may need to be reconnected manually.  
  

  * Pasted nodes may appear offset to avoid overlapping the original nodes.  
  

  * Pasted nodes should be reviewed before publishing.  
  

  * Use snapshots or templates when cloning, sharing, or installing a full agent structure.


* * *

## **Supported Actions and How They Work**

  


Each editing action is designed to make the Graph Builder canvas easier to manage. Understanding how copied nodes, pasted nodes, preserved connections, and bulk delete behave helps users make changes confidently.

###   


### **Copy one or more nodes**

  


Select one or more nodes in the Graph Builder canvas, then use the available copy action or keyboard shortcut to copy the selected nodes.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071006220/original/4ooccAlU34FPP0lPA1C3E2f_6jQExqhWEg.png?1778490885)

###   


### **Paste copied nodes into the same graph**

  


Paste copied nodes into the current Graph Builder canvas or another supported Agent Studio tab. Pasted nodes appear as separate nodes with fresh IDs.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071005962/original/F1inb8ccRyYpNSf3cIWAjgBXmHeEO2gumA.png?1778490732)

###   


### **Paste copied nodes into another Agent Studio tab**

  


Copied nodes can also be pasted into another open Agent Studio tab. This helps you reuse flow sections between different agents without rebuilding the structure manually.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071008797/original/IpCwxa2w_VPOjSJtF1Ic7mtwLtgODiliHQ.png?1778491782)

###   


### **Preserve copied connections**

  


Connections between copied nodes are preserved when all connected nodes are included in the copied selection. Connections to nodes outside the selection may not be preserved and should be reviewed after pasting.

  


  


### **Generate fresh IDs for pasted nodes**

  


Each pasted node receives a new unique ID. This helps keep the graph stable and avoids conflicts with the original nodes.

  


  


### **Delete multiple selected nodes**

  


Bulk delete allows you to remove multiple selected nodes in one action. This is useful when cleaning up test branches, outdated logic, or extra copied nodes you no longer need.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071009103/original/e1mGvI7u44qrzAFYX_zMk9YegKNYIJWnlA.gif?1778491905)

###   


### **Use keyboard shortcuts**

  


The feature supports familiar keyboard shortcuts so you can perform common graph-editing actions quickly. A shortcut guide is also available in the product for quick reference.

* * *

## **How to Set Up Graph Builder Copy, Paste, and Bulk Delete**

  


Using these tools correctly can save significant time when building or updating agent flows. Following a clear process helps ensure you duplicate the right nodes, preserve useful connections, and avoid unnecessary cleanup later.

  


  1. Open **Agent Studio** and go to the graph you want to edit.  
  


  2. Select the node you want to copy, or select multiple nodes if you want to duplicate a larger flow section.  
  


  3. Use the appropriate keyboard shortcut to copy the selected node or nodes.  
  


     * **Windows** : `Ctrl + C`  
  


     * **Mac** : `Cmd + C`  
  


  4. Paste the copied content where needed.

     * To paste into the same graph, stay on the current canvas and use the paste shortcut.  
  


     * To paste into another graph, open the destination agent in another **Agent Studio** tab and use the paste shortcut there.  
  


     * **Windows** : `Ctrl + V`  
  


     * **Mac** : `Cmd + V`  
  


  5. Review the pasted nodes on the canvas. They should appear slightly offset from the original location so they are easier to identify.  
  


  6. Confirm that the copied nodes and any preserved internal connections match your intended flow.  
  


  7. Update any node-specific settings or paths if you want the duplicated flow to behave differently from the original.  
  


  8. To remove nodes you no longer need, select one or more nodes and use the delete shortcut supported in Graph Builder.  
  


  9. Save and publish your changes after confirming the updated graph works as expected.


* * *

## **Shortcut Reference**

  


Keyboard shortcuts make graph editing much faster, especially when working with larger or repeatable node patterns. Learning the core shortcuts can help you build and clean up graphs with fewer clicks.

  


  * **Copy selected node or nodes**  
  


    * Windows: `Ctrl + C`  
  


    * Mac: `Cmd + C`  
  


  * **Paste copied node or nodes**  
  


    * Windows: `Ctrl + V`  
  


    * Mac: `Cmd + V`  
  


  * **Bulk delete selected node or nodes**  
  


    * Use the delete shortcut available in Graph Builder for your device.  
  


    
    
    HighLevel also includes a keyboard shortcut guide in the product so you can reference supported shortcuts while working in Agent Studio.

* * *

## **Best Practices for Reusing Node Groups**

  


Copy and paste can speed up graph building even more when paired with a thoughtful structure. Reusing clean, well-organised node groups makes it easier to maintain consistency across agents and reduce setup time for similar use cases.  
  


  * Copy complete logic blocks when you want to reuse a proven path rather than rebuilding each node individually.  
  


  * Review pasted nodes before publishing to make sure the duplicated flow still matches your intended use case.  
  


  * Rename or adjust duplicated nodes when testing variations so the graph remains easy to read.  
  


  * Use bulk delete to remove old branches, test nodes, or extra copies that are no longer needed.  
  


  * For full agent replication or sharing across broader environments, use snapshots rather than relying on node-level copy and paste.


* * *

## **Frequently Asked Questions**

  


**Q: Can I copy more than one node at a time?**  
A: Yes. Graph Builder supports copying a single node or multiple selected nodes at once.

  


  


**Q: What happens to the connections between copied nodes?**

A: When connected nodes are copied together, the connections between those copied nodes are rebuilt automatically after paste.

  


  


**Q: Can I paste copied nodes into another Agent Studio tab?**  
A: Yes. The feature supports cross-tab pasting between Agent Studio tabs.

  


  


**Q: Why do pasted nodes appear slightly moved from the original nodes?**  
A: Pasted nodes are placed with an offset so they do not stack directly on top of the original nodes, which makes them easier to find and edit.

  


  


**Q: Do pasted nodes keep the same ID as the original nodes?**  
A: No. Each pasted node gets a new unique ID.

  


  


**Q: Can I delete multiple nodes at the same time?**  
A: Yes. Bulk delete allows you to remove multiple selected nodes in one action.

  


  


**Q: Does this replace snapshots for cloning an entire agent?**  
A: No. Copy and paste is useful for node-level reuse inside Graph Builder, while snapshots are better suited for cloning or sharing a full agent structure.

  


  


**Q: Is there a shortcut guide available in the product?**  
A: Yes. HighLevel includes a keyboard shortcut guide to help you reference supported shortcuts while using Agent Studio.

* * *

## **Related Articles**

  


  * [Agent Studio Overview](<https://help.gohighlevel.com/support/solutions/articles/155000007393-agent-studio-overview>)  
  


  * [How to Use the AI Agent Studio in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000006058-how-to-use-the-ai-agent-studio-in-highlevel>)  
  


  * [How to Clone and Share Agent Studio Agents Using Snapshots](<https://help.gohighlevel.com/support/solutions/articles/155000007504-how-to-clone-and-share-agent-studio-agents-using-snapshots>)  
  


  * [Agent Studio - Router Tool (AI & Conditional Router)](<https://help.gohighlevel.com/support/solutions/articles/155000007404-agent-studio-router-tool-ai-conditional-router->)

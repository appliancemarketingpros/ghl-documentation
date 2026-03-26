# Refresh or Update Snapshots

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000982583-refresh-or-update-snapshots](https://help.gohighlevel.com/support/solutions/articles/48000982583-refresh-or-update-snapshots)  
**Category:** Account Snapshots  
**Folder:** Snapshots

---

When you make changes to a client sub-account (like new workflows, forms, or funnels), your existing snapshot does not update automatically. To capture these new changes and make them available for future imports or updates, you need to manually refresh the snapshot.

* * *

**TABLE OF CONTENTS**

  * How to Refresh a Snapshot
  * Handling Failed Assets during Refresh
  * Workflow Contact Cleanup After Snapshot Refresh
  * What Happens When You Click “Push Updates”?
  * Quick Tips


* * *

# **How to Refresh a Snapshot**

  


  1. Go to your Agency View and click the **Account Snapshots** tab from the left-hand menu  
  

  2. Find the snapshot you want to update and click the **Refresh** icon next to that snapshot  
  

  3. Select which new or modified assets you want to include  
  

  4. Click **Refresh** to finalize the update.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155059137335/original/4ImXJgLPogiQje4C__bwGTGY17ytoezW_g.gif?1764053794)  
  

    
    
    **Note:** After you click **Refresh** , HighLevel loads the selected assets from the source sub-account. You’ll see a progress indicator showing how many assets have been loaded. If some assets fail to load, the refresh will still continue for the others instead of stopping the entire process.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155059751597/original/KaN1CEBWntC56zsL_DSczkAWr18LzgSRwA.png?1764725377)

* * *

## **Handling Failed Assets during Refresh**

  


If one or more assets fail to load during a refresh, they will be marked as failed while the rest of the selected assets continue processing.

  


You can retry loading only the failed assets instead of restarting the entire refresh. This helps you fix temporary issues (like intermittent timeouts) without blocking the overall snapshot update.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155059751665/original/6rEEssPXG7lNT-jUk3kLLk6ZwDavXwMUIA.png?1764725603)

* * *

## **Workflow Contact Cleanup After Snapshot Refresh**

  


If a snapshot refresh removes steps inside workflows that were created from the snapshot (for example, deleting a wait step), HighLevel automatically removes any contacts that were waiting on the deleted step so they don’t get stuck.

  


What you’ll see:  
  


  1. A one-time heads-up appears the next time you open an affected workflow (shown only when it applies).  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064759193/original/CMYs9reyZPN0_CYDFRSRENDtRlHYVACoTg.png?1770890041)  
  

  2. In **Execution Logs** , the workflow records an entry labeled “Removed by - Snapshot Refresh” with more details in the side panel.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064759370/original/gjFq-I3Wq8aVLo4u1Pc4XOyD0kax7TOgcw.png?1770890085)  


    
    
    **Note:** This applies only to workflows created from snapshots when a refresh deletes steps. Directly deleting a step in a workflow already removes waiting contacts.
    

* * *

## **What Happens When You Click “Push Updates”?**

  


After refreshing a snapshot, you’ll see the **“Push Update”** button available for that snapshot. Clicking it lets you:  
  


  1. **Select which sub-accounts** (that previously imported this snapshot) should receive the update  
  

  2. **Choose the assets to push**(e.g., only workflows, or specific forms)  
  

  3. **Manually sync updates** into those sub-accounts without reloading the entire snapshot  
  


[ ](<https://help.gohighlevel.com/support/solutions/articles/48000982587-pushing-loading-snapshot-updates-to-client-accounts>)[Watch the detailed video here](<https://help.gohighlevel.com/support/solutions/articles/48000982587-pushing-loading-snapshot-updates-to-client-accounts>)
    
    
    **Note:** Updates only push to sub-accounts inside your own agency. External agencies must re-import using a new link.

* * *

## **Quick Tips**

  


  * Always refresh your snapshot before sharing or pushing updates  
  

  * Use the Push Update feature to sync selected changes to client accounts  
  

  * Pushed updates are selective, not destructive - existing data stays safe

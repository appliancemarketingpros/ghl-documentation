# Copy Custom Contact Views Using Snapshots

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007851-copy-custom-contact-views-using-snapshots](https://help.gohighlevel.com/support/solutions/articles/155000007851-copy-custom-contact-views-using-snapshots)  
**Category:** Account Snapshots  
**Folder:** Snapshots

---

Custom Contact Detail Page views help teams organize contact records around specific workflows, roles, and priorities. With snapshot support, agency admins can now include custom contact views in snapshots and reuse them across multiple sub-accounts. This saves setup time, reduces repetitive configuration, and helps maintain consistent contact layouts across client accounts.

* * *

**TABLE OF CONTENTS**

  * What is Copying Custom Contact Views Using Snapshots?
  * Key Benefits of Copying Custom Contact Views Using Snapshots
  * Important Requirements and Limits
  * Imported Views and Default View Behavior
  * Custom Fields and Imported Contact Views
  * How To Setup Custom Contact Views in Snapshots
  * Step 1: Go to Account Snapshots
  * Step 2: Name the Snapshot and Select the Source Sub-Account
  * Step 3: Select Contact Detail Views
  * Step 4: Push the Snapshot Update to Linked Sub-Accounts
  * Step 5: Verify the Custom Views in the Destination Sub-Account
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Copying Custom Contact Views Using Snapshots?**

  


Custom Contact Detail Page views let admins control how contact records appear inside a sub-account, including layout structure, panels, fields, modules, and visibility settings. Snapshot support allows those custom views to be captured from one sub-account and reused in other sub-accounts through Account Snapshots.

  


Instead of rebuilding the same Contact Detail Page views manually in every sub-account, admins can create or update a snapshot, select the custom views they want to include, and push those views to linked sub-accounts.

* * *

## **Key Benefits of Copying Custom Contact Views Using Snapshots**

  


Reusable custom views help agencies standardize contact management across multiple sub-accounts while reducing manual setup work. This is especially useful when several client accounts need the same Sales, Support, Admin, or  
Operations contact layouts.  
  


  * **Reduced Manual Setup:** Create a custom contact view once and reuse it across multiple sub-accounts instead of rebuilding it manually.  
  

  * **Consistent Contact Layouts:** Standardize how teams view and manage contact records across accounts.  
  

  * **Faster Sub Account Configuration:** Include custom views as part of a snapshot-based setup process.  
  

  * **Scalable Customization:** Maintain role-based or workflow-based contact layouts across multiple client accounts.  
  

  * **Improved Admin Efficiency:** Help agency admins manage contact page customization from one reusable source account.


* * *

## **Important Requirements and Limits**

  


A successful snapshot setup depends on using a source sub-account that already contains the custom Contact Detail Page views you want to reuse. Reviewing view limits and permissions before creating the snapshot helps prevent incomplete or unexpected results.

  

    
    
    Each sub-account includes 1 default Contact Detail View.
    
    Admins can create or import up to 4 additional custom Contact Detail Views, for a total of 5 views per sub-account.
    
    Custom Contact Detail Page views must exist in the source sub-account before they can be added to a snapshot.
    

  


* * *

## **Imported Views and Default View Behavior**

  


Imported Contact Detail Views are added as custom layouts in the destination sub-account, but they do not replace the built-in default view. Each sub-account keeps its own default Contact Detail View so the location always has a baseline contact record layout available.

  


Contact Detail Views behave differently from assets like funnels or workflows. A snapshot can import the layout and field configuration, but it does not carry over the default-view status from the source sub-account. Even if the imported view was the default in the source sub-account, it is imported as a custom view in the destination sub-account.

  


Choosing **Override** does not make the imported view the default. Override only affects how conflicting imported configurations are handled. It does not change which Contact Detail View the destination sub-account treats as its default.

  


After deployment, open **Contact Detail Views** in the destination sub-account and assign the imported layout to the users or groups who should use it. This controls which layout those people see when viewing contact records.

* * *

## **Custom Fields and Imported Contact Views**

  


Imported Contact Detail Views rely on the destination sub-account’s available fields. When a field used in the source view does not exist in the destination sub-account, HighLevel skips that field during mapping instead of blocking the import.

  


This allows the view import to continue even when the destination sub-account does not perfectly match the source sub-account. After import, review the copied layout to confirm that all expected fields appear. If any fields are missing, create or map the required custom fields in the destination sub-account, then update the view as needed.

* * *

## **How To Setup Custom Contact Views in Snapshots**

  


Proper setup ensures the custom views from the source sub-account are included in the snapshot and made available in the destination sub-account. Follow these steps from Agency View to create the snapshot, select the views, and push the update.

  


#### **_Step 1: Go to Account Snapshots_**  
  


  1. Switch to Agency View.  
  

  2. Click Account Snapshots.  
  

  3. Click Create New Snapshot.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070782429/original/ZYMoX2O9SclymNrjAsXfUAi5Gdg_SS_XwQ.png?1778148831)  
  


#### _**Step 2: Name the Snapshot and Select the Source Sub-Account**_  
 _**  
**_

  1. Enter a clear snapshot name.  
  

     * **Example:** “Sales Contact Views Template”  
  

     * **Example:** “Client Contact Detail Layouts”  
  

  2. Select the sub-account that contains the custom Contact Detail Page views you want to copy.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070782488/original/guWR7hQK2cJQfDBiVNMzXy7fQjXXPVStrw.png?1778148891)

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070782563/original/McuHk2k80xy6gG0OYVQZnqX6rsXR9byIsg.png?1778148948)

  


  


#### **_Step 3: Select Contact Detail Views_**  
  


  1. In the asset selection screen, locate Contact Detail Views.  
  

  2. Expand the category to view the available custom views.  
  

  3. Select the custom views you want to include in the snapshot.  
  

  4. Click Create.  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070782676/original/QU3RKvNEtO73_xL1pKBX2PntrbcFw7H7Yg.png?1778149015)  
  


#### **_Step 4: Push the Snapshot Update to Linked Sub-Accounts_**  
  


  1. Open the snapshot that contains the selected Contact Detail Views.  
  

  2. Choose the option to push the update.  
  

  3. Select the linked sub-account or sub-accounts that should receive the custom views.  
  

  4. Confirm the update.


  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070783044/original/_dSgoaT2jtTMZ0TUuEIj5KyI3-rhBkXPxQ.gif?1778149258)  
  


#### **_Step 5: Verify the Custom Views in the Destination Sub-Account_**  
** _  
_**

  1. Open the destination sub-account.  
  

  2. Go to Contacts.  
  

  3. Open the Contact Detail Page customization area.  
  

  4. Confirm that the copied custom views are available.  
  

  5. Review the layout to make sure the correct fields, panels, modules, and view structure appear as expected.


* * *

## **Frequently Asked Questions**

  


**Q: Can I copy custom Contact Detail Page views from one sub-account to another?  
** Yes. Custom Contact Detail Page views can be included in snapshots and reused across sub-accounts.

  


**Q: Do I need to recreate custom views manually in every sub-account?**  
No. Once the view exists in the source sub-account, you can include it in a snapshot and push it to linked sub-accounts.

  


**Q: How many Contact Detail Views can a sub-account have?**  
Each sub-account has 1 default Contact Detail View and can have up to 4 additional custom views created manually or added by snapshot import, for a total of 5 views.

  


**Q: Will the imported view become the default Contact Detail View in the destination sub-account?**  
No. A view that is default in the source sub-account does not become default in the destination sub-account after import. It is imported as a custom view.

  


**Q: Are users copied with the custom view?**  
No. Users are not copied with imported Contact Detail Views. After deployment, assign the imported view to the users or groups who should use it inside the destination sub-account.

  


**Q: What happens if the destination sub-account does not have the custom fields used in the source view?****  
**The import is not blocked. Fields that do not exist in the destination sub-account are skipped during mapping. Review the imported view afterward to confirm the correct fields appear.

  


**Q: What should I check if the copied view does not appear as expected?**  
Confirm the view was selected under Contact Detail Views, the snapshot update was pushed to the correct sub-account, users or groups were assigned to the imported view, and any required custom fields exist in the destination sub-account.

* * *

## **Related Articles**  
**  
**

  * [Creating Custom Objects using Snapshots](<https://help.gohighlevel.com/en/support/solutions/articles/155000004922>)  
  

  * [Creating New Snapshots in HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/48000982512>)  
  

  * [Refresh or Update Snapshots](<https://help.gohighlevel.com/en/support/solutions/articles/48000982583>)  
  

  * [Load Snapshots Into Existing Sub-Account](<https://help.gohighlevel.com/en/support/solutions/articles/48000982582>)  
  

  * [How to View Snapshot Assets](<https://help.gohighlevel.com/en/support/solutions/articles/155000005917>)  
  

  * [Snapshots - Overview](<https://help.gohighlevel.com/en/support/solutions/articles/48000982511>)

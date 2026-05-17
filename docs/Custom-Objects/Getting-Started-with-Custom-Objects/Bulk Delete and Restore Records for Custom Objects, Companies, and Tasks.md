# Bulk Delete and Restore Records for Custom Objects, Companies, and Tasks

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007925-bulk-delete-and-restore-records-for-custom-objects-companies-and-tasks](https://help.gohighlevel.com/support/solutions/articles/155000007925-bulk-delete-and-restore-records-for-custom-objects-companies-and-tasks)  
**Category:** Custom Objects.  
**Folder:** Getting Started with Custom Objects

---

Bulk delete gives you a faster way to remove multiple Custom Object, Company, or Task records from HighLevel without deleting each record one at a time. This is especially helpful after imports, cleanup projects, deduplication work, or large-scale data resets. Deleted records from supported bulk deletion jobs can be restored from the Bulk Actions page within 60 days, helping reduce the risk of accidental data loss.

* * *

**TABLE OF CONTENTS**

  * What is Bulk Delete and Restore for Custom Objects, Companies, and Tasks?
  * Key Benefits of Bulk Delete and Restore
  * Supported Record Types
  * What Happens When Records Are Bulk Deleted?
  * How To Setup Bulk Delete for Custom Objects, Companies, and Tasks
  * How To Restore Bulk-Deleted Records
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Bulk Delete and Restore for Custom Objects, Companies, and Tasks?**

  


Bulk delete allows you to select multiple records from a list view and delete them in one action. For Custom Objects, this introduces multi-select deletion directly from the Custom Objects list view. For Companies and Tasks, the previous 100-record limit for bulk deletion has been removed, allowing larger cleanup actions without breaking work into smaller batches.

  


When records are deleted, HighLevel removes their relations, associations, and association labels. The related records themselves are not deleted. Bulk-deleted records can be reviewed and restored from the Bulk Actions page within 60 days.

* * *

## **Key Benefits of Bulk Delete and Restore**

  


Bulk delete helps teams manage large record sets more efficiently while keeping recovery options available for supported deletion jobs. This makes it easier to clean up outdated, duplicate, or incorrectly imported records without relying on repetitive manual deletion.  
  


  * **Faster Cleanup:** Delete multiple Custom Object, Company, or Task records in one action instead of removing each record individually.  
  

  * **Improved Custom Object Management:** Use list-view multi-select to bulk delete Custom Object records directly from the record list.  
  

  * **No 100 Record Limit for Companies and Tasks:** Delete larger groups of Company or Task records without batching deletion jobs in groups of 100.  
  

  * **Safer Large Scale Deletion:** Restore eligible bulk-deleted records from the Bulk Actions page within 60 days.  
  

  * **Better Job Visibility:** Track deletion progress, status, and stats from the Bulk Actions page.  
  

  * **Cleaner Record Relationships:** Remove the deleted records’ relations, associations, and association labels while keeping the related records themselves intact.


* * *

## **Supported Record Types**

  


Bulk delete is available for specific record types that support list-view selection and deletion actions. Understanding where this feature applies helps ensure you use the correct cleanup workflow for each module.

  
Supported record types include:  
  


  * Custom Object records  
  

  * Company records  
  

  * Task records


  
For Custom Objects, bulk delete is available from the Custom Objects list view using multi-select checkboxes. For Companies and Tasks, bulk delete supports larger deletion jobs because the previous 100-record cap has been removed.

* * *

## **What Happens When Records Are Bulk Deleted?**

  


Bulk deletion removes the selected records from the applicable module and also clears the deleted records’ connected relationship data. This helps prevent deleted records from continuing to appear in related record associations or labels after removal.

  


When a record is deleted:  
  


  * The selected record is deleted.  
  

  * Relations connected to the deleted record are removed.  
  

  * Associations connected to the deleted record are removed.  
  

  * Association labels connected to the deleted record are removed.  
  

  * Related records themselves are not deleted.


  


For example, deleting a Company record does not delete the contacts, opportunities, or other records that may have been related to that Company. However, the association between the deleted Company and those related records is removed.

  

    
    
    **Important:** Confirm whether restored records regain their previous relations, associations, and association labels before relying on restore for relationship recovery.

  

    
    
    **Before Confirming a Bulk Delete:**
    
    Review any filters applied to the list view.
    
    Confirm the selected records are the records you intend to delete.
    
    Export important data before large cleanup actions when needed.
    
    Make sure your team understands that relations, associations, and association labels are removed when records are deleted.
    
    Review the Bulk Actions page after deletion to confirm job progress and completion.
    
    Restore eligible deletion jobs within 60 days if records were deleted by mistake.

  


* * *

## **How To Setup Bulk Delete for Custom Objects, Companies, and Tasks**

  
Bulk delete does not require a complex setup process. Once records are available in the list view, users can select multiple records, confirm deletion, and monitor the deletion job from the Bulk Actions page.

  
To bulk delete records:  
  


  1. Open the relevant area in HighLevel, Custom Objects/Companies/Tasks.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071158602/original/6nLncX04MovZsJQYSukA1hi0-fRansin3A.png?1778598383)  
  

  2. Go to the list view for the records you want to delete.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071158825/original/BP6WNhCrxf2_j83-fvxSD3RjcgTY74cOJQ.png?1778598480)  
  

  3. Use the checkboxes to select the records you want to remove.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071159056/original/LxMUYDAZZXjxqKwXs3xeN81ZCvBjYLFhhg.png?1778598539)  
  

  4. Click Delete.  
  

  5. Review the confirmation message carefully.  
  

  6. Confirm the deletion.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071159164/original/BOz0049RBYD-HbrwV4d0sbLflRgy9Q1Iqw.png?1778598580)  
  

  7. Go to the Bulk Actions page in the sub-account.  
  

  8. Review the deletion job to check progress, completion status, and stats.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071159238/original/Qendp-8mCaip9FWsDqrORR5Ht70Z_0CWaQ.png?1778598617)


* * *

## **How To Restore Bulk-Deleted Records**

  


The Bulk Actions page keeps a record of supported bulk deletion jobs, allowing you to restore eligible deleted records within the recovery window. Restoring from the original deletion job helps recover records that were deleted accidentally or during a cleanup that needs to be reversed.

  
To restore deleted records within 60 days:  
  


  1. Go to Bulk Actions in the sub-account.  
  

  2. Locate the deletion job for the records you want to restore.  
  

  3. Click the three-dot menu for the deletion job.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071159901/original/MmLJBFu-pxjTYUaALvM7AoJn4VF_Bad-7Q.png?1778598902)  
  

  4. Click Restore.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071159765/original/bNHpCakY41B-NBYzXSpahwmx8M4c2D6ONw.png?1778598840)  
  

  5. Review the confirmation message.  
  

  6. Confirm the restore action.  
  

  7. Monitor the restore progress from the Bulk Actions page.


* * *

## **Frequently Asked Questions**

  
**Q: Can I bulk delete Custom Object records now?  
** A: Yes. Custom Object records can now be selected from the list view using checkboxes and deleted in bulk.

  
**Q: Is there still a 100-record limit for bulk deleting Companies and Tasks?  
** A: No. The previous 100-record cap for bulk delete on Companies and Tasks has been removed.

  
**Q: Where can I check the progress of a bulk delete?  
** A: Go to the Bulk Actions page in the sub-account to review progress, stats, and completion status.

  
**Q: Can I restore records after bulk deleting them?  
** A: Yes. Supported bulk-deleted records can be restored from the Bulk Actions page within 60 days.

  
**Q: Does deleting a record delete related records too?  
** A: No. Related records themselves are not deleted. However, the deleted record’s relations, associations, and association labels are removed.

  
**Q: What happens after the 60-day restore window ends?  
** A: Records should be restored within 60 days from the Bulk Actions page. After that window, the deletion may no longer be recoverable from the Bulk Actions restore option.

* * *

## **Related Articles**  
**  
**

  * [Bulk Actions For Contacts& SmartLists](<https://help.gohighlevel.com/en/support/solutions/articles/48001167703>)  
  

  * [Restore Deleted Contacts or Undo Bulk Deletes](<https://help.gohighlevel.com/en/support/solutions/articles/48001211386>)  
  

  * [List View for Custom Objects: Sort, Filter, and Manage Records](<https://help.gohighlevel.com/en/support/solutions/articles/155000004029>)  
  

  * [Creating and Updating Custom Object Records](<https://help.gohighlevel.com/en/support/solutions/articles/155000004023>)  
  

  * [Task Management](<https://help.gohighlevel.com/en/support/solutions/articles/155000004498>)  
  

  * [Export Companies (CSV Download)](<https://help.gohighlevel.com/en/support/solutions/articles/155000007394>)

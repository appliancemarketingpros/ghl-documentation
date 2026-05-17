# Bulk Delete for Custom Object Records

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007906-bulk-delete-for-custom-object-records](https://help.gohighlevel.com/support/solutions/articles/155000007906-bulk-delete-for-custom-object-records)  
**Category:** Custom Objects.  
**Folder:** Managing Custom Object Records

---

Bulk Delete lets you remove multiple Custom Object records from the list view in a single action. Use it to clean up stale, test, or mis-imported records without opening each one individually.

* * *

**TABLE OF CONTENTS**

  * What is Bulk Delete for Custom Objects?
  * Key benefits
  * How to bulk delete Custom Object records
  * What happens when a Custom Object record is deleted
  * How to recover deleted Custom Object records
  * Frequently Asked Questions
  * Related Articles


* * *

# What is Bulk Delete for Custom Objects?

Bulk Delete is a list-view action on Custom Objects that lets you select multiple records using checkboxes and delete them in one go.

You can select records individually, select all records on a page, or apply filters and search first and then select from the filtered results.

* * *

# Key benefits

  * Remove multiple Custom Object records in a single action.
  * Clean up records directly from the list view without opening each one.
  * Recover deleted records within 60 days from the Bulk Actions page.


* * *

# How to bulk delete Custom Object records

1\. Go to the desired **Custom Objects** in your sub-account

  


  


2\. On the list view, use the checkboxes on the left of each row to select the records you want to delete. Use the header checkbox to select all records on the page.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071007269/original/6X6EC85JdsSafppjkv6gW4C-sMxQ39fwwQ.jpeg?1778491214)

  


  


3\. Click **Delete** from the bulk actions bar that appears.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071007313/original/wQevRoBbGQJkiqRQGyWweMWV5kO2l_yCcw.jpeg?1778491247)

  


4\. Confirm the action in the dialog.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071007411/original/RKy1s07VkrFeIedg_BGDNGa6SLWTbCxzXw.jpeg?1778491300)

  


5\. You can check the progress and logs in the bulk actions page

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071007753/original/cRmWII4FAwDoO4sfhQAKUDNhIpmvUgyWGg.jpeg?1778491376)

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071007730/original/Rg9khG3lGEN1xdstBhi51tU_y-lDPsOSiQ.png?1778491365)

  


  


* * *

# What happens when a Custom Object record is deleted

When you delete a Custom Object record, the record itself and all of its field values are removed.

All relations and associations on the deleted record are also removed, including:

  * Associations to related **Notes** and **Tasks**
  * Associations to related **Contacts** , **Companies** , and **Opportunities**
  * Associations to other **Custom Object records**
  * Any **association labels** applied to those relationships


The related Notes, Tasks, Contacts, Companies, Opportunities, or other Custom Object records themselves are not deleted — only the link between them and the deleted record is removed.

* * *

# How to recover deleted Custom Object records

Bulk-deleted Custom Object records can be restored within **60 days** of deletion from the **Bulk Actions** page. After 60 days, the records are permanently removed and cannot be recovered.

To restore deleted records:

  


1\. Go to **Bulk Actions** in your sub-account.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071007774/original/BRlikpZ9Wss_f_MvIZHzjrItnE8QGEFYmQ.png?1778491396)

  


2\. Locate the relevant job row and click the **three-dot menu** on the right. Click **Restore**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071007866/original/2aWH300_6pYvScelCRACitPeYVGLs6XOmA.png?1778491424)

  


3\. Confirm the action in the dialog.

  


The restore runs as a new job and will appear in the Bulk Actions table. Once it completes, the records will be back on the list view along with their field values and associations.

* * *

# Frequently Asked Questions

**Q: Can I bulk delete records from a filtered or searched list view?**

Yes. Apply your filters or search first, then use the checkboxes to select records from the filtered results.

  


**Q: How long do I have to restore deleted Custom Object records?**

About 60 days from the date of deletion. After that, the records are permanently removed.

  


**Q: Does bulk delete remove associated Notes and Tasks?**

No. Deleting a Custom Object record removes the _association_ to related Notes and Tasks, but does not delete the Notes or Tasks themselves.

  


**Q: Are associations restored when I restore a deleted record?**

Yes. When you restore a record from the Bulk Actions page, its previous associations and association labels are restored along with the record.

# How to Bulk Import Companies Using a CSV File

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007403-how-to-bulk-import-companies-using-a-csv-file](https://help.gohighlevel.com/support/solutions/articles/155000007403-how-to-bulk-import-companies-using-a-csv-file)  
**Category:** CRM  
**Folder:** Import / Export

---

Bulk Import for Companies lets you add or update Company records in HighLevel using a CSV file and a guided import wizard. This article explains how the import flow works, how to map fields safely, and where to review results in Bulk Actions.

* * *

**TABLE OF CONTENTS**

  * What is Bulk Importing Companies?
  * Key Benefits of Bulk Importing Companies
  * Prerequisites for Bulk Importing Companies
  * Common Mistakes to Avoid
  * Import Modes Explained
  * How to Bulk Import Companies
  * Duplicate Handling & Unique Fields
  * Update Empty Values Restrictions
  * Monitor Import Status
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Bulk Importing Companies?**

  


Bulk Importing Companies lets you create and update Company records in HighLevel by uploading a CSV file and following a guided, multi-step import flow. The wizard helps you choose how records should be created or updated, map CSV columns to Company fields with preview data, and verify everything before starting the import.

  

    
    
    **Important:** Import supports **only CSV (.csv) files**. Excel (.xlsx) and Google Sheets links are not supported.
    

* * *

## **Key Benefits of Bulk Importing Companies**

  


  * **Faster CRM setup:** Add hundreds or thousands of companies in minutes using a CSV.  
  


  * **Controlled updates:** Choose whether to create new records, update existing ones, or do both.  
  


  * **Safer data changes:** Prevent accidental data wipes by skipping updates that would overwrite fields with empty values.  
  


  * **Cleaner matching:** Use Company ID-based duplicate detection to update the correct records.  
  


  * **Confidence before importing:** Review mapped fields on a verification screen before the import begins.  
  


  * **Better auditability:** Track imports in Bulk Actions and download a report when complete.


* * *

## **Prerequisites for Bulk Importing Companies**

  


Before starting your import:

  


### **User Permissions**

  


  * You must have **Admin access** to perform imports.


  


### **File Requirements**

  


  * File format must be **.csv**

  * Maximum file size: **30 MB**

  * Only **one sheet/tab**

  * The first row must contain headers

  * Headers should match existing standard or custom fields


  


### **Field Preparation**

  


  * Required fields must contain valid values

  * Custom fields must already exist in your account

  * If updating records, ensure you include the correct identifier (e.g., Record ID)


* * *

# **Common Mistakes to Avoid**

  


  * Missing required fields
  * Blank primary field values
  * Incorrect Record IDs when using Update mode
  * Unique field conflicts
  * CSV headers that don’t match CRM field names


  


Always test with a small file first.

* * *

# **Import Modes Explained**

  


When uploading your CSV, you’ll choose one of three modes:

  


  1. **Create  
**  
Creates new records only.  
  

     * Requires the Primary field
     * Existing records will not be updated
     * Duplicate handling follows unique field rules (if applicable)  
  

  2. **Update**  
  
Updates existing records only.  
  

     * Requires Record ID or unique fields in case of custom objects
     * Rows without a matching Record ID/unique field will be skipped  
  

  3. **Create & Update  
**  
Creates new records and updates existing ones.  
  

     * If Record ID or unique field matches → record updates
     * If no match → record is created
     * Unique field rules apply if configured  
  


![](https://jumpshare.com/share/g691h2JFVRQSb475En4b+/Screenshot+2026-03-05+at+20.24.44.png)

* * *

# **How to Bulk Import Companies**

  


###  _**Step 1:** Navigate to Import_

  


  1. Go to **Contacts** > **Companies.**  
  

  2. Click on **Import**.  
  
![](https://jumpshare.com/share/vObVgcea8q4BNqbvGqgz+/Screen+Shot+2026-03-05+at+20.45.50.png)  
  

  3. Choose the **Companies** object.  
  

  4. Click on **Next**.  
  
![](https://jumpshare.com/share/bzwKdRb4iwNmbGftPohS+/Screen+Shot+2026-03-05+at+20.49.04.png)  
  


### _**Step 2:** Upload CSV File_

  


  1. Upload your **CSV** file.  
  

  2. Choose your **import****mode.**  
  

  3. If applicable, select the **unique field** to deduplicate on.  
  


  4. Click on **Next**.  
  
![](https://jumpshare.com/share/CYiCwKESy882eemWakVN+/Screen+Shot+2026-03-05+at+20.54.14.png)  
  


### _**Step 3:** Map Columns to Fields_

  


Match each CSV column to the correct CRM field.

  


  1. Required fields must be mapped.  
  


  2. Unmapped columns can be ignored.  
  


  3. Fields successfully mapped will show a green indicator.  
  


  4. Errors or warnings will be highlighted.  
  


  5. **Don’t Update Empty Values**

  


**If enabled:** Blank cells in your CSV will NOT overwrite existing values.

  


**If disabled:** Blank cells will clear existing values (except restricted fields).

  


  6. Once done, click on **Next**.  
  
![](https://jumpshare.com/share/tVKlQoiBn4lvqHQaIJLJ+/Screen+Shot+2026-03-05+at+20.57.02.png)  
  


### **_Step 4:_**_Review and Import_

  


  1. Review your data and mapping settings before starting the import to ensure accuracy and completeness.  
  

  2. Once done, click on the **Start Bulk Import** button.  
  
![](https://jumpshare.com/share/CPGTA0LzJW92B0ZPfxvg+/Screen+Shot+2026-03-05+at+21.02.58.png)


* * *

# **Duplicate Handling & Unique Fields**

  


If your Company or Custom Object contains unique fields:

  


  * You must select Record ID or one unique field as the deduplication field (if multiple are mapped).  
  


  * The system checks other unique fields for conflicts.  
  


  * If a non-selected unique field conflicts, that row will fail.


  


This ensures clean, conflict-free data.

  


![](https://jumpshare.com/share/RbRmBgyNUVTnE9huhHdj+/z1g9Q4S3C-mO0RqByyBiH5pDfeglXcoYdA.jpeg)

* * *

# **Update Empty Values Restrictions**

  


The following cannot be updated to empty:

  


  * Primary field  
  


  * Required fields


  


These protections prevent accidental data loss.  
  
![](https://jumpshare.com/share/Ljd4IuvRFVpx0yoFaudt+/Screen+Shot+2026-03-05+at+23.28.37.png)

* * *

# **Monitor Import Status**

  


All imports can be tracked in **Bulk Actions**.

  


From Bulk Actions you can:

  


  * View status (Processing, Completed, Failed)  
  


  * Pause, Resume, or Cancel (while running)  
  


  * View detailed statistics  
  


  * Download error logs  
  


![](https://jumpshare.com/share/WUOhwSLunkPKe1yq4Lmw+/Screen+Shot+2026-03-05+at+23.30.29.png)

* * *

## **Frequently Asked Questions**

  


**Q: Can I import multiple Custom Objects at once?**

No. Only one Custom Object can be imported at a time.

  


**Q: Can I import system fields like Created At?**

No. System fields cannot be modified through imports.

  


**Q: What happens if unique fields conflict?**

That specific row will fail. The rest of the import continues.

  


**Q: Can I undo an import?**

No. Imports cannot be reversed. Always validate your CSV before starting.

  


**Q: Where do I see past imports?**

Go to Bulk Actions to view import history and statistics.

* * *

### **Related Articles**

  


  * [CSV File Format for Importing](<https://help.gohighlevel.com/support/solutions/articles/155000005143>)  
  


  * [Importing Contacts Using a CSV File](<https://help.gohighlevel.com/en/support/solutions/articles/155000004432>)  
  


  * [Importing Opportunities Using a CSV File ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002517>)  
  


  * [Managing Custom Objects ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004023>)  
  


  * [Managing Companies](<https://help.gohighlevel.com/en/support/solutions/articles/48001223777>)

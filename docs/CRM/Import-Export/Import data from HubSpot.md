# Import data from HubSpot

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007947-import-data-from-hubspot](https://help.gohighlevel.com/support/solutions/articles/155000007947-import-data-from-hubspot)  
**Category:** CRM  
**Folder:** Import / Export

---

HubSpot Importer helps you move important HubSpot CRM data into HighLevel faster. This article walks you through importing your HubSpot data (contacts, deals, custom fields, and pipelines) and reviewing the import results so you can spot and fix any errors.

  

    
    
    HubSpot Importer is currently in beta and available only for for select users. If you do not see the **Import from HubSpot** option, the feature may not be enabled for your account yet.

* * *

**TABLE OF CONTENTS**

  * What is HubSpot Importer?
    * Key Benefits of HubSpot Importer
    * Before You Start
    * What Data You Can Import from HubSpot
    * How To Use the HubSpot Importer
    * Troubleshooting
    * Frequently Asked Questions
    * Related Articles


* * *

# **What is the HubSpot Importer?**

  


HubSpot Importer makes it easier to switch from HubSpot to HighLevel. Instead of rebuilding your CRM setup by hand, you can connect HubSpot, choose what to bring over, and start the import from inside HighLevel.

  


This helps speed up onboarding by bringing over important data and structure, including Contacts, Opportunities, Custom Fields, Pipelines, Stages, and Custom Folders. After the import finishes, HighLevel shows a report so you can see what imported successfully, what failed, and what may need review.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071283807/original/pim64uGu8zjNNEiRSkIRiaTyFgFPDECW6w.png?1778710589)

* * *

## **Key Benefits of HubSpot Importer**

  


  * **Faster Migration:** Import supported HubSpot CRM data directly into HighLevel without relying only on manual CSV exports.  
  


  * **Preserved Structure:** Bring HubSpot Deals into HighLevel as Opportunities while keeping supported Pipelines and Stages organized.  
  


  * **Custom Data Continuity:** Import supported HubSpot Contact and Deal Properties as HighLevel Custom Fields.  
  


  * **Transparent Reporting:** Review import totals, successful records, errors, warnings, object-level results, and record-level messages after the import finishes.


* * *

## **Before You Start**

  


  * Use a clean account when possible. Importing into an account that does not already have manually created data makes errors and duplicates easier to review.  
  


  * Turn on **Allow duplicates** for both Contacts and Opportunities before you start. You can re-enable de-duplication after the import is complete. Leaving duplicate-blocking on causes a lot of avoidable errors during a HubSpot import.  
  

  * The import runs in the background. You can close the window and return later to review progress.  
  


  * It is recommended to use English as the account language.  
  

  * It is recommend to test imports in a new or non-production location before importing into an actively used location.


* * *

## **What Data You Can Import from HubSpot**

  


The HubSport Importer currently supports Contacts, Opportunities (Deals), Companies, Custom Fields (Properties), Custom Folders, Pipelines, Stages, Emails, Notes and Tasks.

  


When Deals are imported as Opportunities, their pipeline and stage structure is preserved when supported by the importer. This helps keep your sales process familiar after moving from HubSpot to HighLevel.

  


Migration Type| What It Does  
---|---  
Contacts migration| Brings HubSpot contact records into HighLevel.  
Opportunities migration| Imports HubSpot Deals as HighLevel Opportunities.  
Companies migration| Imports HubSpot companies as new records into HighLevel.  
Custom Fields migration  
| Maps HubSpot Contact and Deal Properties to HighLevel Custom Fields.  
  
Pipelines & Stages migration| Preserves the full pipeline structure, including stages.  
Custom Folders migration| Carries over folder organization for supported imported data.  
Email migration| Brings over all of your emails from HubSpot into HighLevel  
Tasks migration| Brings your reminders and to-dos into HighLevel.  
  
  


For unsupported objects, use your broader migration plan or the manual migration steps in the [HubSpot to HighLevel migration guide](<https://help.gohighlevel.com/en/support/solutions/articles/155000003388>).

* * *

## **Limitations and Considerations**

  


  * **Pipelines & Opportunities:** Pipelines and pipeline stages are imported. An opportunity can be associated with up to 10 additional contacts. Also an opportunity with no contacts associated to it cannot be imported.  
  

  * **C****ustom Fields:** Custom field mapping is based on field keys. If a conflicting field key already exists in HighLevel, the import may fail. HubSpot calculated fields are imported as Single Line Text fields.  
  

  * **Files & Attachments: **File attachments are supported for Contacts and Opportunities.  
  

  * **Contacts:** If an imported contact is deleted in HighLevel and the importer is run again, the contact will be imported again. If the deleted contact is later restored, duplicate contacts may be created.  
  

  * **Notes:** A note can be associated with only one record of each object type. For example, a note can be linked with one contact, one opportunity. Currently - notes cannot be associated to companies.  
  

  * **Tasks:** Recurring tasks are not supported. A task can be associated with up to 10 records of each object type. For example, a task can be linked with 10 contacts, 10 opportunities or 10 companies.  
  

  * **Associations:** Some associations may not be imported due to platform limits. Customers should validate critical associations after migration.  
  

  * **Emails:** Imported emails from HubSpot will be read only.


* * *

## **How To Use the HubSpot Importer**

  


####  _**Step 1:** Open Import Data_

  


From Contacts (or Companies or Opportunities), open the Import menu in the top-right and select Import data. 

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071283631/original/mrGot9kMZ6vWQcy9ipDvtgU9TgFqcPNjfw.png?1778710020)

  


  


#### ** _Step 2:_**_Select HubSpot Import_

  


Click **Connect HubSpot** in the right card to start a HubSpot import.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071283846/original/X7WVxhtleGKXmzVjV53-SfB2ZqcQm-yMqg.jpeg?1778710712)

  


  


#### _**Step 3:** Authenticate your HubSpot account_

  


Login to your HubSpot account and authenticate.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071283851/original/WdRVxYJ6SazmFNqAn7zPWklQKQ2pQ7mcMQ.png?1778710776)  
  


#### _**Step 4:** Review the Quick Tips_

  


Once your key is verified, the import wizard opens at **Get started**. This step shows a quick walkthrough video and a few tips:  
  


  * Clean up duplicates in HubSpot before importing.  
  


  * Back up your current data before importing.  
  


  * Review field mappings before you start the import.  
  


When you're ready, click **Continue**.

  
![The Get started step of the import wizard, with a quick-tips video, link to the import guide, and tips for a successful import.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278754/original/nb6rXC9j854J7if5BkHk9L-yeoEVgdIPEQ.png?1778701200)

  


  


#### _**Step 5:** Select What to Import_

  


Choose which HubSpot objects to bring over:  
  


  * **Contacts** : People you track (leads, customers, prospects).  
  


  * **Tasks:** track to-dos, follow-ups, and reminders linked to your records.  
  


  * **Deals:** Track pipeline value and status. Deals are imported as **Opportunities**.  
  
Importing Deals requires Contacts. Contacts will be auto-selected if you pick Deals.
  * **Companies** : Brings over your company object records as Companies.


  
Tick the boxes for what you want, then click **Continue**.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078262193/original/9J14TQ92R36XCt6EAI5P7VvEAC6Sa_yM9w.png?1786548570)

#### _**Step 6:** Review What is Included_

  


The wizard automatically includes the related data needed to keep your records complete and connected:  
  


  * **Contacts:** all properties (standard + custom fields), notes, emails  
  


  * **Tasks:** associations.  
  


  * **Deals:** all properties, pipelines, notes, associations.
  * **Companies** : properties and associations.  
  
Pipeline stages are imported along with pipelines. You don't need to recreate them.  
  


**T****wo things to watch for with custom fields:**  
  


  * **Custom fields are mapped by key.** If a custom field with the same key already exists in your account, the import will throw an error for that field. Rename or remove the existing one before importing if you want a clean mapping.  
  


  * **Mismatched name vs. label.** If a custom field's internal name and display label are different in HubSpot, you may see issues during import. Reviewing your HubSpot custom fields and aligning name/label before importing avoids surprises.  
  


Click **Continue** to move on.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261235/original/jpWs8pZkJ4ht6uPqRgZjg0UrNOZcQVo9UQ.png?1786547999)

####   


#### _**Step 7:** Confirm Record Counts_

  


Before the import starts, the wizard shows what will be brought over and how many records are involved. For each row you'll see:  
  


  * **HubSpot data** : what's in HubSpot (e.g., Contacts – records, Deals – pipelines).  
  


  * **Imported as** : what it becomes in your account (e.g., Contacts – custom fields, Opportunities – pipelines).  
  


  * **Records found** : how many records will be imported.


  

    
    
    **Note:** The **Records found** count for custom fields can differ from what you see in HubSpot's UI. The wizard counts only fields it can map and import, so a small gap between the two numbers is expected.

  


Optionally click the **Edit** (pencil) icon next to contact properties or deal properties to select the specific properties to include.

  


Click **Confirm and start import** to kick it off. Confirm once more in the dialog that follows.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261342/original/kSvGt3X3jjOcvSgWTLBsj8ESpnlpHeztiA.png?1786548053)

  
You can also choose to modify and bring in only certain custom fields from HubSpot and not all of them.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261390/original/5kwnilw8ChlaQMKJIKL0SjmR1fn7CSNS_A.png?1786548079)

#### _**Step 8:** Your Import is Running_

  


You'll see a confirmation at the top of the page: **Your HubSpot import has started and is running in the background.** The **Import history** table below shows the in-progress run with a live **Processing %** status.

  


You can close the window or navigate away, the import keeps running. Come back to this page anytime to check progress.  
  
![A success toast at the top reading Your HubSpot import has started, with the Import history table below showing the in-progress run.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278809/original/9uc3aQKiKVGx_k1Z43H4upPq_LByvJhacQ.png?1778701307)  
  


#### _**Step 9:** Open Import Details (Object View)_

  


When you're ready to review results, click the **stats icon** in the **Actions** column of an import row. The **Import details** modal opens.  
  


The four cards at the top give you the headline numbers:  
  


  * **Total records:** everything the import touched.  
  


  * **Success:** records that imported cleanly (with the success rate).  
  


  * **Errors:** records that didn't import.  
  


  * **Imported with warnings:** records that imported but have something worth reviewing.


  
**Object view** (the default tab) summarizes each object: how many succeeded, how many errored, and overall status.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261790/original/P_qYFR7xV5eP3ezjJ3da9jUyfMG-W57eXg.png?1786548354)  


#### _**Step 10:** Drill into Individual Records_

  


Switch to the **Record view** tab to see every record one row at a time.  
  


Use the filters at the top:  
  


  * **Objects:** narrow to Contacts, Contacts – Custom field, Opportunities, etc.  
  


  * **Status:** filter by **Success** , **Error** , or **Imported with warnings**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261814/original/fwWBJSqFQiURRDSnfzLISs1TF70kzSnWWw.png?1786548363)  
  


#### _**Step 11:** Review and Fix Errors_

  


Switch the **Status** filter to **Error** to see every record that failed. Each row tells you which object failed and why, with the HubSpot record ID in the message so you can find it back in HubSpot.

  


Click **Download** in the bottom-left to export the full error list as a CSV, useful for fixing data in HubSpot, then re-running the import.

  


Common error causes are covered in the Troubleshooting and FAQ sections below.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261819/original/RflIwLxZKQ8TXd3tmJ_nV82idHVgrEw3rw.png?1786548374)

* * *

## **Troubleshooting**

  


#### **The "Records found" count is lower than what HubSpot shows.**

The wizard's count includes only fields the import can actually map and bring over. Some HubSpot fields are excluded (for example, fields with unsupported types), so you may see a small gap between HubSpot's UI and the count in the import preview. The records that don't make it into the count are the ones the import would skip anyway.

  


#### **I see errors saying "Couldn't import contact with HubSpot record ID…"**

That message tells you exactly which HubSpot contact failed. Common reasons:

  * **The contact has a file attached to a field.** File imports aren't supported yet — any contact (or deal) with a file attachment will throw an error. Workaround: download the file from HubSpot, remove the attachment from that field, then re-run the import. The file itself can be re-attached manually after import.  
  

  * **Custom field key collision.** Custom fields are mapped by their internal key. If a field with the same key already exists in the destination, the import errors on that field. Rename or delete the existing field before importing.  
  

  * **Custom field name and label don't match.** When a HubSpot field's name and label differ, the importer can get confused about which one to use. Aligning them in HubSpot before importing usually clears it up.


* * *

## **Frequently Asked Questions**

  


**Q: Can I re-import or pick up where I left off?**

Yes, start a new import from the Import data page. Each run is logged separately in Import history, so you can compare runs and check the error CSV from a previous attempt before re-running.

  


**Q: Does the import overwrite existing records?**

By default, no. Imported records are added alongside whatever's already in your account. That's why we recommend importing into a clean account — and why "Allow duplicates" should be on during the import (see Before you start).

  


**Q: Where can I see the full list of errors?**

Open Import details from any import row, switch to Record view, set Status to Error, then click Download to export the full list as a CSV.

* * *

## **Related Articles**

  


  * [Hubspot to HighLevel (Migration Guide)](<https://help.gohighlevel.com/en/support/solutions/articles/155000003388>)  
  

  * [Importing Contacts and Opportunities via CSV](<https://help.gohighlevel.com/en/support/solutions/articles/155000003905>)  
  

  * [Zoho to HighLevel (Migration Guide)](<https://help.gohighlevel.com/en/support/solutions/articles/155000003316>)

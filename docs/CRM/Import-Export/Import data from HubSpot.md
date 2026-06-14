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

  


The HubSport Importer currently supports Contacts, Opportunities (Deals), Custom Fields (Properties), Custom Folders, Pipelines, Stages, Notes and Tasks.

  


When Deals are imported as Opportunities, their pipeline and stage structure is preserved when supported by the importer. This helps keep your sales process familiar after moving from HubSpot to HighLevel.

  


Migration Type| What It Does  
---|---  
Contacts migration| Brings HubSpot contact records into HighLevel.  
Opportunities migration| Imports HubSpot Deals as HighLevel Opportunities.  
Custom Fields migration| Maps HubSpot Contact and Deal Properties to HighLevel Custom Fields.  
Pipelines & Stages migration| Preserves the full pipeline structure, including stages.  
Custom Folders migration| Carries over folder organization for supported imported data.  
Tasks migration| Brings your reminders and to-dos into HighLevel.  
  
  


Other HubSpot objects (Companies, Tickets, Engagements, Workflows, etc.) are not yet included and are coming soon.

  


For unsupported objects, use your broader migration plan or the manual migration steps in the [HubSpot to HighLevel migration guide](<https://help.gohighlevel.com/en/support/solutions/articles/155000003388>).

* * *

## **Limitations and Considerations**

  


  * **Pipelines & Opportunities:** Pipelines and pipeline stages are imported. An opportunity can be associated with up to 10 additional contacts.  
  

  * **C****ustom Fields:** Custom field mapping is based on field keys. If a conflicting field key already exists in HighLevel, the import may fail. HubSpot calculated fields are imported as Single Line Text fields.  
  

  * **Files & Attachments: **File attachments are supported for Contacts and Opportunities.  
  

  * **Contacts:** If an imported contact is deleted in HighLevel and the importer is run again, the contact will be imported again. If the deleted contact is later restored, duplicate contacts may be created.  
  

  * **Notes:** A note can be associated with only one record of each object type. For example, a note can be linked with one contact, one opportunity and one company.  
  

  * **Tasks:** Recurring tasks are not supported. A task can be associated with up to 10 records of each object type. For example, a task can be linked with 10 contacts, 10 opportunities and 10 companies.  
  

  * **Associations:** Some associations may not be imported due to platform limits. Customers should validate critical associations after migration.


* * *

## **How To Use the HubSpot Importer**

  


####  _**Step 1:** Open Import Data_

  


From Contacts (or Opportunities), open the Import menu in the top-right and select Import data. 

  
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


  
Tick the boxes for what you want, then click **Continue**.  
  


![The Select objects step showing two cards: Contacts and Deals, with checkboxes to choose which to import.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278773/original/nT85rW9mnb8lOhAzBt0-0HB5Lv3J8LeRqA.png?1778701230)  
  


#### _**Step 6:** Review What is Included_

  


The wizard automatically includes the related data needed to keep your records complete and connected:  
  


  * **Contacts:** all properties (standard + custom fields), notes  
  


  * **Tasks:** associations.  
  


  * **Deals:** all properties, pipelines, notes, associations.  
  
Pipeline stages are imported along with pipelines. You don't need to recreate them.  
  


**T****wo things to watch for with custom fields:**  
  


  * **Custom fields are mapped by key.** If a custom field with the same key already exists in your account, the import will throw an error for that field. Rename or remove the existing one before importing if you want a clean mapping.  
  


  * **Mismatched name vs. label.** If a custom field's internal name and display label are different in HubSpot, you may see issues during import. Reviewing your HubSpot custom fields and aligning name/label before importing avoids surprises.  
  


Click **Continue** to move on.

  
![The Review included data step showing Contacts \(Properties\) and Deals \(Properties and Pipelines\) included by default.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278794/original/u8FoSSVv1uvMeNggxsVU10-RKbPNOCDkOw.png?1778701266)  
  


#### _**Step 7:** Confirm Record Counts_

  


Before the import starts, the wizard shows what will be brought over and how many records are involved. For each row you'll see:  
  


  * **HubSpot data** : what's in HubSpot (e.g., Contacts – records, Deals – pipelines).  
  


  * **Imported as** : what it becomes in your account (e.g., Contacts – custom fields, Opportunities – pipelines).  
  


  * **Records found** : how many records will be imported.


  

    
    
    **Note:** The **Records found** count for custom fields can differ from what you see in HubSpot's UI. The wizard counts only fields it can map and import, so a small gap between the two numbers is expected.

  


Optionally click the **Edit** (pencil) icon next to contact properties or deal properties to select the specific properties to include.

  


Click **Confirm and start import** to kick it off. Confirm once more in the dialog that follows.  
  
![The Preview and import step showing a Confirm import details table with HubSpot data, Imported as, and Records found counts.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278805/original/Z-_MD9oRaYaV-PAkZDKlaGQvF0GhKPRiEQ.png?1778701293)

  
  


#### _**Step 8:** Your Import is Running_

  


You'll see a confirmation at the top of the page: **Your HubSpot import has started and is running in the background.** The **Import history** table below shows the in-progress run with a live **Processing %** status.

  


You can close the window or navigate away, the import keeps running. Come back to this page anytime to check progress.  
  
![A success toast at the top reading Your HubSpot import has started, with the Import history table below showing the in-progress run.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278809/original/9uc3aQKiKVGx_k1Z43H4upPq_LByvJhacQ.png?1778701307)  
  


#### _**Step 9:** Open Import Details (Object View)_

  


When you're ready to review results, click the **eye icon** in the **Actions** column of an import row. The **Import details** modal opens.  
  


The four cards at the top give you the headline numbers:  
  


  * **Total records:** everything the import touched.  
  


  * **Success:** records that imported cleanly (with the success rate).  
  


  * **Errors:** records that didn't import.  
  


  * **Imported with warnings:** records that imported but have something worth reviewing.


  
**Object view** (the default tab) summarizes each object: how many succeeded, how many errored, and overall status.

  
![The Import details modal in Object view, showing total records, success, errors, and imported-with-warnings counts plus a per-object summary table.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278815/original/zKJLQBdvxJ4p4St10bqYnIcpVisDj9xgrg.png?1778701321)

  
  


#### _**Step 10:** Drill into Individual Records_

  


Switch to the **Record view** tab to see every record one row at a time.  
  


Use the filters at the top:  
  


  * **Objects:** narrow to Contacts, Contacts – Custom field, Opportunities, etc.  
  


  * **Status:** filter by **Success** , **Error** , or **Imported with warnings**.


  
![The Import details modal in Record view, filtered to Status = Success, showing successfully imported records.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278820/original/nx7JZoAveOBkgtxT9nOFwAV2FnTgUeV9kw.png?1778701335)  
  


#### _**Step 11:** Review and Fix Errors_

  


Switch the **Status** filter to **Error** to see every record that failed. Each row tells you which object failed and why, with the HubSpot record ID in the message so you can find it back in HubSpot.

  


Click **Download** in the bottom-left to export the full error list as a CSV, useful for fixing data in HubSpot, then re-running the import.

  


Common error causes are covered in the Troubleshooting and FAQ sections below.

![The Import details modal filtered to Status = Error, showing rows of failed records with error messages referencing HubSpot record IDs.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071278831/original/jYbzrfeK7K-Dqv6z5QkLmeIgOs7Vk9UD5Q.png?1778701352)

* * *

## **Troubleshooting**

  


#### **The Verify & Connect button gives me an error.**

Double-check that your service key starts with `pat-` and that all four read-only scopes 

`crm.objects.contacts.read`, `crm.objects.deals.read`, `crm.schemas.contacts.read`, `crm.schemas.deals.read`) are attached to the key. If it still fails, generate a fresh key in HubSpot and try again.

  


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

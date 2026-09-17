# Bulk Import Companies

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008505-bulk-import-companies](https://help.gohighlevel.com/support/solutions/articles/155000008505-bulk-import-companies)  
**Category:** CRM  
**Folder:** Import / Export

---

CRM Data Management

# Bulk Import Companies

Upload and manage hundreds of Company records at once using CSV files with our guided 4-step import wizard.

What You'll Learn

This article explains how to use the Bulk Import feature to create and update Company records in your HighLevel CRM using CSV files. You'll learn how to navigate the import wizard, map fields correctly, handle duplicates, and track import results.

By the end of this guide, you'll be able to migrate large datasets into your CRM efficiently while maintaining data integrity and avoiding common import errors.

Labs Feature

This feature is currently available in Labs. To access it, navigate to your Subaccount settings, select Labs, and enable "Company and Custom Object Import" before proceeding with the steps in this article.

Table of Contents

1

What is Bulk Import for Companies?

2

Key Benefits

3

Enabling Company and Custom Object Import in Labs

4

How to Import Companies

5

Understanding the 4-Step Import Wizard

6

Tracking Imports with Bulk Actions

7

Best Practices for Company Imports

8

Related Articles

9

Frequently Asked Questions

1

## What is Bulk Import for Companies?

Bulk Import for Companies is a CSV-based import tool that allows you to create and update multiple Company records in HighLevel CRM simultaneously. The feature uses a guided 4-step wizard (Start → Upload → Map → Verify) that helps you upload data files, map fields to the correct Company properties, detect duplicates, and review your import before execution.

The wizard includes smart field mapping with preview data, duplicate detection based on Company ID, and the option to prevent overwriting existing field values with empty data. After submitting your import, you can track progress and view detailed statistics through the dedicated Bulk Actions page.

This feature is designed to simplify large-scale CRM migrations and eliminate manual data entry for agencies and businesses managing multiple company records.

2

## Key Benefits

The Bulk Import feature provides several advantages for managing Company data at scale:

**Faster CRM Migration** — Import hundreds of Company records in minutes instead of creating them manually one by one.

**Duplicate Control** — Automatically detect and handle duplicate companies based on Company ID to maintain clean data.

**Flexible Update Options** — Choose to create only, update only, or create and update companies in a single import operation.

**Data Protection** — Enable the "Don't update to empty value" option to prevent accidental deletion of existing field data.

**Detailed Audit Statistics** — View success, error, and warning counts after import completion, plus download detailed reports for troubleshooting.

**Reduced Operational Overhead** — Eliminate repetitive data entry tasks and minimize manual errors during CRM setup.

3

## Enabling Company and Custom Object Import in Labs

Before you can import Company records, you must enable the feature through the Labs section of your Subaccount settings. This feature is currently in Labs, meaning it is available for early access testing and may receive updates based on user feedback.

Step 1

Navigate to Labs

Go to your Sub account settings and select the **Labs** tab from the left sidebar.

Step 2

Enable the Import Feature

Locate the toggle labeled **Company and Custom Object Import** and turn it on.

Step 3

Verify Access

Once enabled, navigate to the **Companies** section in your CRM to confirm the **Import** button is visible.

4

## How to Import Companies

Follow these steps to initiate a bulk import of Company records using a CSV file:

Step 1

Access the Import Tool

Navigate to **Companies** in your HighLevel dashboard and click the **Import** button.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079261949/original/Q9Ym3wnxaYCrvaa_kHp_Izv1kU-7kHii0A.png?1787665753)

Step 2

Select Companies

In the object selection screen, choose **Companies** as the object type you want to import.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079262333/original/8bQeesRxXhg7dKKEP2EpNNfwlo6wjwfCuQ.png?1787665940)

Step 3

Upload Your CSV File

Click the upload area and select your prepared CSV file containing the Company data you want to import.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079262442/original/QiUUA5JXJtwSRhC_57ewI5cxscQcY03w7Q.png?1787666006)

Step 4

Choose Import Behavior

Select one of three options: **Create companies** (new records only), **Update companies** (existing records only), or **Create & update companies** (both).  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079262512/original/T4OO1vCbv8Lte3tJ6p_8PifsuAz5mMnUGQ.png?1787666041)

Step 5

Set Duplicate Detection Criteria

Select **Company ID** as the field to use for identifying duplicate records during import.

Step 6

Map CSV Columns to Company Fields

In the field mapping screen, match each column in your CSV file to the corresponding Company field in HighLevel. Preview data from your CSV helps confirm correct mappings.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079262607/original/2MZDW5BoSVb-_4NvkON7NHpIusHuSExpYQ.png?1787666122)

Step 7

Review and Verify

On the verification screen, review all your import settings, including field mappings and duplicate handling rules. Optionally enable **Don't update to empty value** to prevent overwriting existing data with blank fields.

Step 8

Start the Import

Click **Start Import** to begin processing your file.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079262758/original/s-tqgMCD0za3coI2HqYfMIBVr2WIvmNZSw.png?1787666217)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079262793/original/y14FIOT6U8O1n_zRGIiStC0C03q-IUbvAw.png?1787666248)

Step 9

Monitor Progress

Track the import status under **Bulk Actions – Companies** in your dashboard.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079262850/original/i-MRwWtgg6EHXaWJOW7TsQof6VNX3KBRjg.png?1787666299)

5

## Understanding the 4-Step Import Wizard

The Bulk Import wizard guides you through four distinct phases to ensure accurate data transfer:

Phase 1

Start

Select the object type (Companies) and define your import behavior—whether you want to create new records, update existing ones, or do both.

Phase 2

Upload

Upload your CSV file and choose the criteria for duplicate detection (typically Company ID).

Phase 3

Map

Match each CSV column to a corresponding Company field. The wizard displays sample data from your file to help you confirm correct mappings.

Phase 4

Verify

Review all your settings before submitting. This screen includes the option to enable "Skip empty values" to protect existing data from being overwritten by blank CSV cells.

Note

Always verify your field mappings carefully in the Map phase. Incorrect mappings can result in data being placed in the wrong fields, which may require manual cleanup or re-importing.

6

## Tracking Imports with Bulk Actions

After you submit an import, HighLevel processes the file in the background. You can monitor the progress and review detailed results using the Bulk Actions – Companies dashboard.

The Bulk Actions page displays key statistics for each import:

**Success Count** — The number of Company records successfully created or updated.

**Error Count** — The number of records that failed to import due to data validation issues or system errors.

**Warning Count** — The number of records imported with potential issues that may require review.

You can also download a detailed import report that includes line-by-line results, error descriptions, and warnings. This report is useful for auditing, troubleshooting failed records, and ensuring data integrity after large imports.

Tip

Download the import report immediately after completion to preserve a record of the import operation. This is especially helpful for compliance, auditing, or debugging issues that may arise later.

7

## Best Practices for Company Imports

Follow these recommendations to ensure smooth and accurate Company imports:

Practice 1

Prepare Your CSV File Carefully

Ensure your CSV file is properly formatted with clear column headers, consistent data types, and no unnecessary special characters. Remove any duplicate rows before uploading.

Practice 2

Review Field Mappings Thoroughly

Always double-check the field mappings in the Map phase. Verify that data from each CSV column matches the correct Company field in HighLevel to avoid placing information in the wrong properties.

Practice 3

Enable "Skip Empty Value"

When updating existing records, enable this option to prevent empty CSV cells from overwriting populated fields in HighLevel. This protects your existing data from accidental deletion.

Practice 4

Test with a Small Sample First

Before importing thousands of records, test the process with a small CSV file containing 10–20 rows. Verify the results in Bulk Actions to confirm mappings and settings are correct.

Practice 5

Download Import Reports for Auditing

After each import, download the detailed import report from the Bulk Actions page. Keep these reports for record-keeping, troubleshooting, and compliance purposes.

Pro Tip

If your import includes a large number of records (500+), break it into smaller batches of 200–300 rows. This makes it easier to identify and fix errors without needing to re-upload massive files.

8

## Related Articles

  * [How to Import Contacts in HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/155000003905>)
  * [CSV File Formatting Guidelines for CRM Imports](<https://help.gohighlevel.com/en/support/solutions/articles/155000005143>)
  * [Managing Company Records in HighLevel CRM](<https://help.gohighlevel.com/en/support/solutions/articles/155000004555>)


9

## Frequently Asked Questions

Q: Is there a limit to how many Company records I can import at once?

There is no strict limit mentioned in the feature documentation. However, for best results and easier error management, consider breaking very large imports (1,000+ rows) into smaller batches of 200–500 records.

Q: Can I rollback an import if I make a mistake?

The Bulk Import feature does not include an automated rollback function. Once an import completes, you would need to manually delete or update records, or re-import corrected data. This is why testing with a small sample file first is strongly recommended.

Q: What happens if I upload a CSV with duplicate Company IDs?

The duplicate detection system identifies records based on the criteria you select (typically Company ID). If duplicates are detected and you've chosen the "Update companies" or "Create & update companies" option, HighLevel will update the existing records instead of creating duplicates.

Q: Do I need to include Company IDs in my CSV file?

If you're creating new companies, Company IDs are not required—HighLevel will generate them automatically. If you're updating existing records or using duplicate detection, including the Company ID in your CSV ensures accurate matching.

Q: What does "Don't update to empty value" mean?

This setting prevents the import from overwriting existing field values in HighLevel with blank cells from your CSV. For example, if a Company record already has an address but your CSV has an empty address cell, enabling this option will keep the existing address instead of deleting it.

Q: Can I import custom fields for Companies?

Yes. During the field mapping step, you can map CSV columns to any custom fields you've created for Companies in HighLevel. The wizard will display all available fields, including custom ones.

Q: Where can I download the import report?

After your import completes, navigate to **Bulk Actions – Companies** in your dashboard. Find the completed import in the list and click the download button to retrieve the detailed import report.

Q: Do I need to enable the Labs feature for every sub account?

Yes. The Company and Custom Object Import feature must be enabled individually in the Labs section of each subaccount where you want to use it.

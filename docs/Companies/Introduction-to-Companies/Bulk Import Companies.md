# Bulk Import Companies

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008400-bulk-import-companies](https://help.gohighlevel.com/support/solutions/articles/155000008400-bulk-import-companies)  
**Category:** Companies  
**Folder:** Introduction to Companies

---

CRM Management

# Bulk Import Companies

Upload CSV files to create and update company records at scale using HighLevel's guided import wizard.

What You'll Learn

This article covers HighLevel's bulk company import feature, which allows you to upload CSV files to create and update company records in your CRM.

You'll learn how to enable the feature through Labs, navigate the four-step import wizard, map fields accurately, handle duplicates, and track import progress with detailed statistics.

Labs Feature

This feature is currently available through HighLevel Labs. You must enable "Company and Custom Object Import" in your subaccount Labs settings before you can access the bulk import functionality.

Table of Contents

1

What is Bulk Import for Companies?

2

Key Benefits

3

Enabling Company and Custom Object Import

4

How to Import Companies

5

Understanding the Import Flow

6

Tracking Import Progress

7

CSV Preparation Checklist

8

Frequently Asked Questions

9

Related Articles

1

## What is Bulk Import for Companies?

Bulk Import for Companies is a CSV-based import tool that allows you to create and update company records in your HighLevel CRM at scale. The feature uses a guided, four-step wizard that walks you through uploading your file, mapping fields, handling duplicates, and verifying data before the import begins.

The import process supports three modes: creating new companies, updating existing companies, or both creating and updating companies in a single operation. Duplicate detection is handled using the Company ID field, ensuring that existing records are updated correctly rather than duplicated.

After an import completes, HighLevel provides detailed statistics broken down by success, error, and warning counts, along with a downloadable report for auditing and troubleshooting.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077955654/original/1FVwnBZNwCRf4G1Wfz_XV1yjljiAdfV8bg.png?1786246881)**

2

## Key Benefits

Bulk company import streamlines CRM data management and reduces the operational overhead of manual record creation. This feature is especially valuable for agencies migrating client data or SMBs consolidating company information from multiple sources.

**Faster CRM Migration** — Import hundreds or thousands of company records in minutes rather than entering them individually.

**Smart Duplicate Control** — Automatically detect and update existing companies based on Company ID to prevent duplicates.

**Field-Level Protection** — Enable the "Don't update to empty value" option to prevent accidental data overwrites when updating existing records.

**Detailed Import Statistics** — Review success, error, and warning counts after each import to identify and resolve issues quickly.

**Audit Trail** — Download comprehensive import reports for compliance, troubleshooting, and record-keeping.

3

## Enabling Company and Custom Object Import

Before you can use bulk company import, you must enable the feature through HighLevel Labs. Labs features are experimental or early-access capabilities that require manual activation at the subaccount level.

Step 1

Navigate to Labs Settings

Go to your **Subaccount** and select **Labs** from the settings menu.

Step 2

Enable Company and Custom Object Import

Locate the **Company and Custom Object Import** toggle and turn it on.

Step 3

Verify Access

Navigate to the **Companies** section of your CRM and confirm that the **Import** button is visible.

4

## How to Import Companies

Follow these steps to start a bulk import of company records. Make sure your CSV file is properly formatted and contains the data you want to import before beginning.

Step 1

Open the Companies Import Wizard

Navigate to **Companies** in your HighLevel CRM and click the **Import** button.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077955661/original/c8GQRG6z8wRZTctfPVw3AFyJEg6p_lQkLQ.png?1786246895)**

Step 2

Select Companies as the Import Object

In the object selection screen, choose **Companies** from the available import types.

Step 3

Upload Your CSV File

Click to upload your CSV file or drag and drop it into the upload area.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077955663/original/Z_nEWh5sDVvpHa7zCRX5fMq7MvHkhsmJ_w.png?1786246910)**  


Step 4

Choose Import Behavior

Select one of three options: **Create companies** , **Update companies** , or **Create & update companies**.

Step 5

Configure Duplicate Detection

Select **Company ID** as the duplicate detection criteria. This ensures existing records are updated rather than duplicated.

Step 6

Map CSV Columns to Company Fields

Match each column in your CSV to the corresponding company field in HighLevel. Preview data is shown to help confirm your mappings are correct.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077955675/original/2FuQNg_DWW7G5I2n68cZ58J7EY4u7YrSNQ.png?1786246960)**

Step 7

Review and Verify Your Import

Review the verification screen to confirm all settings and mappings are correct. If updating existing records, consider enabling **Don't update to empty value** to prevent overwriting existing data with blank fields.

Step 8

Start the Bulk Import

Click **Start Bulk Import** to begin processing your file.

Pro Tip

Always Review Field Mappings Before Importing

Double-check that each CSV column is mapped to the correct company field to prevent data mismatches and import errors.

5

## Understanding the Import Flow

The bulk company import process is divided into four distinct stages. Each stage validates and prepares your data before moving to the next step.

Stage 1

Start

Select the object type (Companies) and choose your import behavior (create, update, or both).

Stage 2

Upload

Upload your CSV file and configure duplicate detection criteria (typically Company ID).

Stage 3

Map

Match CSV columns to HighLevel company fields. Preview data is displayed to help confirm accurate mappings.

Stage 4

Verify

Review all settings, mappings, and import options before submitting. Enable field-level protection if you want to prevent empty values from overwriting existing data.

Tip

The wizard shows preview data during the mapping stage so you can confirm that each column contains the expected information before finalizing your import.

6

## Tracking Import Progress

After starting a bulk import, HighLevel provides a dedicated tracking page where you can monitor the status of your import jobs and review detailed statistics.

Navigate to **Bulk Actions – Companies** to view all active and completed imports. Each import displays a progress indicator and, once complete, provides a breakdown of success, error, and warning counts.

**Success Count** — Number of company records that were successfully created or updated.

**Error Count** — Number of records that failed to import due to validation issues or system errors.

**Warning Count** — Number of records that imported with non-critical issues (e.g., missing optional fields).

**Downloadable Report** — A detailed CSV report containing all import results, including error messages and affected records.

Best Practice

Always download the import report after completion for auditing and troubleshooting. This report contains detailed error messages that can help you correct issues in your CSV before re-importing.

7

## CSV Preparation Checklist

Properly formatting your CSV file before uploading will reduce errors and ensure a smooth import process. Follow these guidelines to prepare your data.

**Use UTF-8 Encoding** — Save your CSV file with UTF-8 encoding to prevent character display issues.

**Include a Header Row** — The first row should contain column names that clearly describe each field.

**Include Company IDs for Updates** — If updating existing companies, ensure your CSV contains the HighLevel Company ID for each record.

**Remove Unnecessary Columns** — Only include columns you want to import to simplify field mapping.

**Validate Data Types** — Ensure numeric fields contain only numbers, date fields use consistent formatting, and text fields don't exceed field length limits.

**Test with a Small File First** — Import a small sample (10–20 records) to confirm field mappings and settings before uploading your full dataset.

Warning

Enabling "Don't update to empty value" is recommended when updating existing records. Without this option, empty cells in your CSV will overwrite existing data in HighLevel, potentially causing data loss.

8

## Frequently Asked Questions

Q: Is there a limit to how many companies I can import at once?

HighLevel does not specify a hard limit in the release documentation, but for best performance and easier troubleshooting, it's recommended to import files in batches of 1,000–5,000 records. Very large imports may take longer to process.

Q: Can I undo an import after it has been processed?

There is no built-in rollback feature. Once an import completes, the changes are permanent. If you need to remove imported records, you would need to delete them individually or use bulk delete actions if available. Always test with a small sample import first.

Q: How do I find the Company ID for existing records?

You can export your existing companies from HighLevel to get a CSV file that includes the Company ID field. This exported file can then be used as a template for updating records, ensuring each row contains the correct ID.

Q: What happens if my CSV contains a company that already exists?

If you select "Create & update companies" or "Update companies" as your import behavior, HighLevel will update the existing record instead of creating a duplicate, as long as the Company ID matches. If you select "Create companies" only, duplicates may be created.

Q: What does the "Don't update to empty value" option do?

When enabled, this option prevents empty cells in your CSV from overwriting existing data in HighLevel. For example, if a company record already has a phone number and your CSV has that field blank, the existing phone number will be preserved rather than deleted.

Q: Can I import custom fields during the bulk company import?

Yes, you can map CSV columns to custom company fields during the field mapping step. Make sure your custom fields are already created in HighLevel before starting the import.

Q: Where can I download the import report after completion?

Navigate to **Bulk Actions – Companies** and locate the completed import job. Click the download icon or link to retrieve the detailed report, which includes success, error, and warning details for each record.

Q: What file format is required for the import?

The bulk import tool accepts CSV (Comma-Separated Values) files. Make sure your file is saved with UTF-8 encoding and includes a header row with descriptive column names.

9

## Related Articles

?

[Understanding Duplicate Detection in HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/48001202210>)

Learn how HighLevel identifies and handles duplicate records during imports and manual entry.

⚙️

[Using HighLevel Labs Features](<https://help.gohighlevel.com/en/support/solutions/articles/155000003588>)

Explore experimental and early-access features available through HighLevel Labs settings.

?

[ Custom Fields for Companies in HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/155000008031>)

Create and manage custom fields to capture additional company information specific to your business needs.

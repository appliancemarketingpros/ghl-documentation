# Bulk Import Companies Using a CSV File

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007403-bulk-import-companies-using-a-csv-file](https://help.gohighlevel.com/support/solutions/articles/155000007403-bulk-import-companies-using-a-csv-file)  
**Category:** CRM  
**Folder:** Import / Export

---

CRM Management

# Import Companies (Custom Objects) Using a CSV File

Import Company records in bulk using a CSV file to quickly migrate data, update existing Companies, or synchronize Company information in HighLevel.

What You'll Learn

This article explains how to import Company records in bulk using CSV files. The bulk import tool provides a guided workflow for uploading, mapping, verifying, and processing Company records while helping reduce errors through field validation and duplicate detection.

Whether you're moving data from another CRM or updating existing records, this feature streamlines Company management at scale.

Table of Contents

1

What is Company Bulk Import?

2

Key Benefits of Company Bulk Import

3

Prerequisites

4

Common CSV Preparation Mistakes

5

Import Modes Explained

6

How to Import Companies

7

Understanding Record IDs

8

Duplicate Detection and Unique Fields

9

Update Empty Values

10

Monitor Import Status

11

Best Practices

12

Frequently Asked Questions

1

## What is Company Bulk Import?

Company Bulk Import allows you to create new Company records, update existing ones, or perform both actions simultaneously by uploading a CSV file. The guided import wizard walks you through preparing your file, mapping columns to Company fields, reviewing the import, and monitoring progress through Bulk Actions.

Using the correct import mode and properly mapped fields helps maintain accurate Company data while reducing manual work and improving data consistency across your CRM.

2

## Key Benefits of Company Bulk Import

Company Bulk Import simplifies large-scale data management while giving you control over how records are created and updated.

**Save Time** — Import hundreds or thousands of Company records instead of creating them individually.

**Flexible Import Modes** — Create new Companies, update existing ones, or perform both operations in a single import.

**Smart Field Mapping** — Match CSV columns to HighLevel Company fields before importing.

**Duplicate Protection** — Prevent unwanted duplicate Companies using Record IDs and unique fields.

**Review Before Importing** — Verify mappings and import settings before processing records.

**Import Monitoring** — Track import progress, warnings, and errors through Bulk Actions.

**Detailed Reporting** — Download reports to review successful imports and troubleshoot failed records.

3

## Prerequisites

Preparing your CSV correctly before importing significantly reduces validation errors and ensures your Company data imports successfully.

Important

Before starting, verify you have permission to access the Companies module, Company Management is enabled for your account, and your CSV file meets all formatting requirements.

Before starting, verify the following:

  * You have permission to access the Companies module.
  * Company Management is enabled for your account.
  * Your CSV file is saved in .csv format.
  * The first row contains column headers.
  * Required Company fields are included.
  * Data is clean and consistently formatted.
  * Custom Company fields already exist if you intend to import values into them.


Best Practice

Before importing thousands of Companies, perform a test import using a small CSV containing 5–10 records to confirm mappings and formatting.

4

## Common CSV Preparation Mistakes

Many import errors occur because of formatting issues within the CSV file. Reviewing your data beforehand helps prevent failed imports and unnecessary cleanup.

Warning

Avoid the following common mistakes that cause import failures and data quality issues.

Avoid the following:

  * Missing required fields
  * Blank header rows
  * Duplicate column names
  * Invalid date formats
  * Extra spaces within important values
  * Incorrect email or phone number formatting (if applicable)
  * Unsupported special characters
  * Empty columns that are not needed


5

## Import Modes Explained

Choosing the correct import mode ensures HighLevel handles each record exactly as intended.

Note

Select the import mode carefully based on whether you're adding new Companies, updating existing ones, or performing both operations.

Mode 1

Create

Use Create when importing Companies that do not already exist in HighLevel. This mode only creates new Company records.

**Example:** You are migrating Companies from another CRM into HighLevel for the first time.

Mode 2

Update

Use Update when modifying existing Company records. This mode requires a reliable identifier, such as the Company Record ID, to locate the correct Company before updating it.

**Example:** You need to update Company phone numbers or addresses without creating new Companies.

Mode 3

Create & Update

Use Create & Update when your CSV contains a combination of existing and new Companies. Existing Companies are updated while Companies that do not exist are created automatically.

**Example:** You receive a monthly Company export from another system containing both new customers and updates to existing ones.

6

## How to Import Companies

Following the guided import wizard helps validate your data before processing and minimizes import errors.

Step 1

Start the Import

  * Navigate to Contacts.
  * Select Companies.
  * Click Import.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077795160/original/imh1skE8vj94nacg0XT2EI1ejEjO4ColZA.png?1786018925)

  


Choose the appropriate import mode (Create, Update, or Create & Update) and click Next.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077795278/original/aspnbS99kFscr1-ND9QPjkJwELsx1udrCg.png?1786018988)

Step 2

Upload Your CSV File

Upload the CSV containing your Company records. HighLevel validates the uploaded file before moving to the mapping stage.

Ensure:

  * Headers are included.
  * Required fields exist.
  * File formatting is correct.


Click Next.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077795355/original/w7zC9A9QrUUrXuruCSfqQJxTlImGd0nOYQ.png?1786019046)

Step 3

Map Company Fields

Field mapping determines where each CSV column will be imported inside HighLevel. Review every mapped field carefully.

For each column:

  * Verify the detected Company field.
  * Adjust mappings if necessary.
  * Ignore unnecessary columns.
  * Confirm custom fields map correctly.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077795486/original/L19SLaoA2tBXnRLlIU7ummwYS3EXN5QZFQ.png?1786019101)

  


HighLevel attempts to map columns automatically whenever possible. Click Next.

Note

Review field mappings carefully before proceeding. Incorrect mappings can result in data appearing in wrong fields or import failures.

Step 4

Verify Import Settings

Before processing begins, review the import summary.

Confirm:

  * Import mode
  * Number of records
  * Field mappings
  * Duplicate handling settings
  * Update Empty Values option


If everything looks correct, click Start Bulk Import.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077795612/original/6ta8Ggb4RfsC94fj_5H1xFV_U5L6360XcQ.png?1786019143)

7

## Understanding Record IDs

Record IDs uniquely identify each Company within HighLevel. Using Record IDs during update imports ensures the correct Company is modified, even if multiple Companies share similar names.

Important

If Record IDs are unavailable, configure an appropriate unique Company field for duplicate matching whenever possible.

Example:

Company| Record ID  
---|---  
ABC Manufacturing| 672918  
XYZ Logistics| 918234  
  
Updating by Record ID eliminates ambiguity during bulk updates.

8

## Duplicate Detection and Unique Fields

Duplicate detection helps prevent accidental creation of multiple Company records representing the same business.

Depending on your import mode, HighLevel compares incoming records using Company Record ID, configured unique Company fields, or existing Company records.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077795728/original/5GjKt3b9B1MxF3G5S8UFNOIAEhFcsjpDCQ.png?1786019214)

Note

If duplicate conflicts occur, review the import report after processing to identify affected records.

Possible outcomes include:

  * New Company created
  * Existing Company updated
  * Duplicate detected
  * Validation error generated


9

## Update Empty Values

The Update Empty Values option determines how blank cells in your CSV affect existing Company information.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077795817/original/_wHauQ0KR3MqZ4nWgcryc6OyNvkTA8YmYA.png?1786019260)

Warning

When Update Empty Values is enabled, blank CSV cells will overwrite existing Company data. Use this option carefully to avoid accidental data loss.

When Enabled

Blank values overwrite existing Company data

**Example:**

Current Phone Number: (555) 123-4567

CSV Phone Number: (blank)

**Result:** The Phone Number is cleared.

When Disabled

Blank cells are ignored

Existing Company values remain unchanged. This is the recommended option when performing routine updates and your CSV does not intentionally clear information.

10

## Monitor Import Status

Bulk Actions allows administrators to monitor every Company import from start to finish.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077795888/original/cjh0PUjm4gU6kAl6EWeaueavxRmYudk1MQ.png?1786019298)

Pro Tip

Download error reports immediately if validation issues occur. This makes it easier to correct failed records and re-import only the affected Companies.

Each import displays:

  * Status
  * Records processed
  * Successful imports
  * Warnings
  * Failed records
  * Completion time


Available actions may include:

  * View Details
  * Pause
  * Resume
  * Cancel (when available)
  * Download Error Report
  * Download Success Report


11

## Best Practices

Following recommended import practices helps improve accuracy and reduces cleanup after importing.

**Export existing Company data before performing large update imports** — This provides a backup that can be used if you need to review or restore information after an import.

**Test imports with a small sample first** — Perform a test import using 5–10 records to confirm mappings and formatting before processing thousands of Companies.

**Verify custom fields before uploading** — Create custom Company fields before importing your CSV. HighLevel will not automatically create missing custom fields.

**Review mappings carefully** — Double-check that CSV columns map to the correct CRM fields before proceeding. Incorrect mappings can result in data appearing in wrong fields or import failures.

**Avoid unnecessary blank values** — Clean your data before importing and consider disabling Update Empty Values to prevent accidental data loss.

**Monitor Bulk Actions after every import** — Track import progress and review completion status to identify any errors or warnings that require attention.

**Download error reports immediately** — If validation issues occur, download the error report to correct affected records and re-import only those Companies.

**Confirm imported Companies by reviewing several records** — After completion, verify a sample of imported Companies to ensure data imported correctly.

12

## Frequently Asked Questions

Q: Can I import new and existing Companies at the same time?

Yes. Use the Create & Update import mode.

Q: Can I stop an import after it starts?

Depending on the import status, Bulk Actions may allow you to pause or cancel an active import.

Q: What happens if duplicate Companies are found?

HighLevel evaluates duplicate records using Record IDs and configured unique fields. The affected records are updated, skipped, or flagged depending on your import settings.

Q: Can I import custom Company fields?

Yes. Existing custom Company fields can be mapped during the Field Mapping step.

Q: Will HighLevel automatically create missing custom fields?

No. Create custom Company fields before importing your CSV.

Q: Can I edit field mappings before starting the import?

Yes. Review and adjust mappings during the Field Mapping step before confirming the import.

Q: What should I do if some records fail?

Download the error report from Bulk Actions, correct the affected records in your CSV, and import only those records again.

Q: Should I export my Companies before updating them?

Yes. Exporting your existing Company data provides a backup that can be used if you need to review or restore information after an import.

Q: Does importing Companies automatically create associations with Contacts or Opportunities?

No. Company imports only create or update Company records. Associations must be managed separately where supported.

Q: **Can I undo an import?**

  


No. Imports cannot be reversed. Always validate your CSV before starting.

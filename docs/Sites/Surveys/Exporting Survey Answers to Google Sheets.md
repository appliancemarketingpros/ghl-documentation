# Exporting Survey Answers to Google Sheets

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000979917-exporting-survey-answers-to-google-sheets](https://help.gohighlevel.com/support/solutions/articles/48000979917-exporting-survey-answers-to-google-sheets)  
**Category:** Sites  
**Folder:** Surveys

---

Surveys · Google Sheets

# How to Send Survey Responses to Google Sheets in HighLevel

Automatically send new survey submissions to Google Sheets using a workflow, or export existing survey responses directly from HighLevel.

+. mmmlkn n jjjj 

Overview

HighLevel lets you automatically send survey submission data to Google Sheets using a workflow. This is useful when you want new responses organized in a spreadsheet for reporting, team review, or additional processing without manually copying information.

Important

Exporting existing survey submissions and automatically sending future submissions to Google Sheets are two different processes. Use the native **Export** option for existing submissions and a **Workflow** for automatic Google Sheets updates.

Table of Contents

1\. What Does Sending Survey Responses to Google Sheets Do?

2\. Export vs Automatic Google Sheets Sync

3\. Before You Begin

4\. Prepare Your Google Sheet

5\. Create the Workflow

6\. Add the Survey Submitted Trigger

7\. Add the Google Sheets Action

8\. Map Data to Google Sheets

9\. Test and Publish the Workflow

10\. Export Existing Survey Submissions

11\. Troubleshooting

12\. Frequently Asked Questions

13\. Related Articles

## 1\. What Does Sending Survey Responses to Google Sheets Do?

Using a HighLevel workflow, you can automatically add information to Google Sheets whenever a contact submits a selected survey.

**Typical workflow**

**Survey Submitted → Google Sheets → Create Spreadsheet Row**

You can send information such as:

  * Contact name
  * Email address
  * Phone number
  * Survey-related contact fields
  * Submission information
  * Other values available to the workflow


## 2\. Export vs Automatic Google Sheets Sync

Choose the method based on whether you need existing responses or want future survey submissions sent automatically.

Method| Best For| How It Works  
---|---|---  
**Export Survey Submissions**|  Existing responses| Export submissions from HighLevel and receive a download link by email.  
**Google Sheets Workflow**|  Future submissions| A workflow runs after a survey is submitted and sends mapped data to Google Sheets.  
  
## 3\. Before You Begin

Prepare the required survey, Google account, and spreadsheet before building the workflow.

  * A published HighLevel survey
  * A Google account connected to the HighLevel sub-account
  * A Google Sheet where the data will be added
  * Column headers for the information you want to store
  * Access to **Automation → Workflows**
  * Premium Triggers & Actions enabled when required for the Google Sheets action


**Note:** Google Sheets is a Premium Workflow Action. Availability and usage charges can depend on the agency's current Premium Triggers & Actions configuration.

## 4\. Prepare Your Google Sheet

Set up the destination spreadsheet before configuring the workflow so the required columns are ready for mapping.

  1. Open Google Sheets.
  2. Create a new spreadsheet or open an existing one.
  3. Select the worksheet where survey information should be added.
  4. Create a header row for the information you want to store.


Name| Email| Phone| Feedback| Submission Date  
---|---|---|---|---  
  
## 5\. Create the Workflow

Create a workflow that will run when the selected survey is submitted.

  1. In your HighLevel sub-account, go to **Automation → Workflows**.
  2. Create a new workflow or open an existing workflow.
  3. Add a new workflow trigger.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080735682/original/FSBMIUPSGhoCrytlIH0mUVNvBkkcgn--4A.png?1789140782)**

## 6\. Add the Survey Submitted Trigger

The **Survey Submitted** trigger starts the workflow when a contact submits a survey.

  1. Select **Survey Submitted** as the workflow trigger.
  2. Add the **Survey is** filter.
  3. Select the survey whose submissions you want to send to Google Sheets.
  4. Save the trigger.


**Tip:** Use the **Survey is** filter when only one survey should send information to this Google Sheet.

## 7\. Add the Google Sheets Action

Add a Google Sheets workflow action after the trigger to send the submission information to the selected spreadsheet.

  1. Click **\+ Add Action**.
  2. Search for and select **Google Sheets**.
  3. Select the appropriate action, such as **Create Spreadsheet Row**.
  4. Select the connected Google account.
  5. Select the required spreadsheet.
  6. Select the worksheet where the information should be added.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080738868/original/tfK76_zgSvEQeRG6qN2mGO9pKkTYLAiVHQ.png?1789142272)**

## 8\. Map Data to Google Sheets

Match the HighLevel values available in the workflow with the corresponding columns in your Google Sheet.

  1. Select the HighLevel value you want to send.
  2. Map it to the appropriate Google Sheets column.
  3. Repeat for each required field.
  4. Save the action.


Google Sheets Column| Example HighLevel Value  
---|---  
Name| Contact Name  
Email| Contact Email  
Phone| Contact Phone  
Feedback| Relevant mapped field  
  
**Important:** Not every survey answer automatically becomes a contact field. If you need a specific response in a workflow, confirm that the value is available in the workflow data picker or stored in an appropriate mapped field.

**Screenshot:** Show the Google Sheets field-mapping area with HighLevel values mapped to the corresponding spreadsheet columns.

## 9\. Test and Publish the Workflow

Test the workflow before relying on it for live survey submissions.

  1. Save the workflow configuration.
  2. Publish the workflow.
  3. Submit the selected survey using a test contact.
  4. Open the destination Google Sheet.
  5. Confirm that a new row was created.
  6. Verify that each value appears under the correct column.


**Result:** Future qualifying survey submissions can now send the mapped information to the selected Google Sheet automatically.

## 10\. Export Existing Survey Submissions

If you need survey responses that have already been submitted, use HighLevel's native export option instead of the workflow method.

  1. Go to **Sites**.
  2. Open **Surveys → Submissions**.
  3. Use the survey filter to select the required survey.
  4. Click **Export**.


HighLevel sends a download link for the exported survey submissions to your email.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080739057/original/hKOvAxYsvynIxgjS5GZk5YkYui2Xn2EcBQ.png?1789142382)**

## 11\. Troubleshooting

Use these checks if survey submissions are not appearing in the expected Google Sheet.

**The workflow does not run**

Confirm that the workflow is published, the **Survey Submitted** trigger is configured correctly, and the **Survey is** filter points to the intended survey. Review the workflow execution history to confirm whether the contact entered the workflow.

**No row appears in Google Sheets**

Confirm that the correct Google account, spreadsheet, and worksheet are selected. Review the workflow execution history to check whether the Google Sheets action completed successfully.

**Data appears in the wrong columns**

Open the Google Sheets workflow action and review the field mapping. Confirm that each HighLevel value is mapped to the intended spreadsheet column.

**A survey answer is missing**

Check how the survey question is configured and confirm that the required value is available to the workflow before mapping it to Google Sheets.

## 12\. Frequently Asked Questions

Can I automatically send new survey submissions to Google Sheets?

Yes. Use the **Survey Submitted** workflow trigger followed by an appropriate Google Sheets workflow action, such as **Create Spreadsheet Row**.

Can I export existing survey submissions without creating a workflow?

Yes. Go to **Sites → Surveys → Submissions** , select the appropriate survey, and use **Export**. HighLevel sends a download link for the exported submissions to your email.

Can the same contact submit a survey more than once?

Yes. HighLevel tracks survey submissions independently, even when the same contact submits the survey multiple times.

Does every survey answer automatically update the contact record?

No. Responses connected to mapped contact fields can update those fields. Other responses remain available in the survey submission record.

Is the Google Sheets workflow action free?

Google Sheets is a **Premium Workflow Action**. Availability and charges depend on your agency's current Premium Triggers & Actions configuration.

## 13\. Related Articles

  * [ How to Access and Export Survey Submissions ](<https://help.gohighlevel.com/en/support/solutions/articles/48000979915>)
  * [ Workflow Trigger - Survey Submitted ](<https://help.gohighlevel.com/en/support/solutions/articles/155000003259>)
  * [ Guide to Google Sheets Premium Workflow Action ](<https://help.gohighlevel.com/en/support/solutions/articles/48001238162>)

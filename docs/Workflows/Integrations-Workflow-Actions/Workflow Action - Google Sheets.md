# Workflow Action - Google Sheets

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003294-workflow-action-google-sheets](https://help.gohighlevel.com/support/solutions/articles/155000003294-workflow-action-google-sheets)  
**Category:** Workflows  
**Folder:** Integrations Workflow Actions

---

**TABLE OF CONTENTS**

  * Overview
  * Action Name
  * Action Description
  * Action Details
  * Example


  


## Overview

The **Google Sheets** action allows you to send data from your workflow directly into a Google Sheets spreadsheet. This is a premium action, which means each execution incurs additional charges. This action is ideal for keeping records, tracking data, and organising information in a structured format within a Google Sheet.

  


## Action Name

**Google Sheets**

  


## Action Description

The **Create Spreadsheet Row** action is used to add a new row of data into a specified Google Sheets spreadsheet. This action can automatically log information such as ticket details, user information, or any other relevant data that needs to be recorded.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032225222/original/mO8g2rTWNdoF7JOCphoy3e8eXA9K-ktP7w.png?1725445694)

  


Field| Description| Mandatory  
---|---|---  
Action Name| The name of the action, identifying what it will do. For this action, it's set to "Create Spreadsheet Row".| Yes  
Action| Defines the specific operation to be performed on Google Sheets. Options include creating a row, updating a cell, etc. For this action, it's "Create Spreadsheet Row".| Yes  
Choose an Account| The Google account linked to your HighLevel platform that has access to the desired Google Sheet.| Yes  
Drive| Specifies the Google Drive where the spreadsheet is located. Typically set to "My Drive" for personal documents.| Yes  
Spreadsheet| Select the specific Google Sheets document where the data will be sent. This field lists all accessible spreadsheets in the chosen account.| Yes  
Worksheet| The specific worksheet within the selected spreadsheet where the new row will be added. Worksheets are individual tabs within a Google Sheets document.| Yes  
Refresh Headers| A button that updates the available columns based on the current headers in the selected worksheet. This ensures data is mapped correctly to the columns.| No  
Starting Column| Specifies the starting column for where the data will be inserted. Maps data to the correct column based on the Google Sheet's headers.| Yes  
Ending Column| Specifies the ending column for where the data will be inserted. Allows you to define a range of columns to populate with data.| Yes  
Dynamic Fields| These fields appear based on the columns in your spreadsheet. Each column is represented here, and you can specify what data should be inserted into each one. Example fields include Ticket ID (A) and Subject (B).| Yes  
  
  


### **How to Configure the Action**

  1. **Add the Action to Workflow** : Drag and drop the **Google Sheets** action into your desired workflow.
  2. **Select Action Type** : Choose "Create Spreadsheet Row" from the Action dropdown.
  3. **Choose Google Account** : Select the linked Google account that has access to your Google Sheets.
  4. **Select Drive** : Typically, select "My Drive" unless you are using a shared drive.
  5. **Select Spreadsheet and Worksheet** : Choose the specific Google Sheets document and the corresponding worksheet tab where you want to add the data.
  6. **Map Data Fields** : Use the Starting Column and Ending Column to define the range. Map the workflow data to the corresponding columns in the Google Sheet by entering values or using custom values.
  7. **Refresh Headers** : Click this if you’ve made recent changes to the Google Sheet’s headers to ensure the data aligns correctly.


  


## Example

  * **Trigger** : New Support Ticket Created
    * **Condition** : A new support ticket is generated from a contact.
    * **Action** : Google Sheets - Create Spreadsheet Row
      * **Drive** : My Drive
      * **Spreadsheet** : "Support_Analysis_2023"
      * **Worksheet** : "September"
      * **Starting Column** : Ticket ID (A)
      * **Ending Column** : Subject (B)
      * **Ticket ID** : Insert the ticket ID using custom values.
      * **Subject** : Insert the ticket subject using custom values.


  


By integrating the **Google Sheets** action within workflows, you can automate data entry tasks, ensuring critical information is logged accurately and consistently, reducing manual errors and saving time.

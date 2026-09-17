# Workflow Action - Create & Update Multiple Rows in Google Sheets

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002097-workflow-action-create-update-multiple-rows-in-google-sheets](https://help.gohighlevel.com/support/solutions/articles/155000002097-workflow-action-create-update-multiple-rows-in-google-sheets)  
**Category:** Workflows  
**Folder:** Workflow Builder

---

Workflow Action - Create & Update Multiple Rows in Google Sheets helps you create new spreadsheet entries or update existing ones in bulk within a single HighLevel workflow. This article covers what the feature does, when to use each action type, and how to set it up correctly in Google Sheets.

  


* * *

**TABLE OF CONTENTS**

  * What is Workflow Action - Create & Update Multiple Rows in Google Sheets? 
  * Key Benefits of Create & Update Multiple Rows in Google Sheets Action
  * Prerequisites
  * How to Use the Action to Create Multiple Row(s) in Google Sheets
    * How Create Multiple Spreadsheet Row(s) Works
    * How to Pass Multiple Rows into the Action
    * Best use cases
  * How to Use the Action to Update Multiple Row(s) in Google Sheets
    * When to use this option
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Workflow Action - Create & Update Multiple Rows in Google Sheets? **

  

    
    
    **Note:** This is a **premium** **action**. Using this action will **incur** **additional** **charges** **per** **execution**.
    

  


Workflow Action - Create & Update Multiple Rows in Google Sheets allows HighLevel workflows to create or update more than one spreadsheet row during a single automation flow. This makes it easier to work with repeated or grouped data, especially when you need to log multiple entries, sync structured records, or update several spreadsheet values at once.

  


This functionality is part of the Google Sheets Premium Workflow Action and expands what you can do beyond a single-row action. Instead of sending data one row at a time, you can configure your workflow to write or modify multiple rows more efficiently while keeping your spreadsheet organized.

* * *

## **Key Benefits of Create & Update Multiple Rows in Google Sheets ****Action**

  


  * **Faster data logging** : Create multiple spreadsheet rows in one workflow action instead of repeating the same setup several times.  
  


  * **Better organization** : Keep related records together in Google Sheets when workflows generate grouped or repeated data.  
  


  * **Less manual work** : Reduce the need to add or edit rows by hand after a workflow runs.  
  


  * **Improved accuracy** : Map spreadsheet columns directly to workflow data to lower the risk of copy-and-paste errors.  
  


  * **More flexible updates** : Update several row values in a defined spreadsheet range when records need to be changed.


* * *

## **Prerequisites**

  


A successful setup depends on having the spreadsheet and workflow prepared before mapping any fields. Taking a moment to confirm permissions, headers, and sheet structure can prevent broken mappings, incorrect updates, or missing data later.

  


  * Make sure your Google account is connected in HighLevel.  
  


  * Confirm that the spreadsheet is stored in the correct Google Drive.  
  


  * Add clear column headers in the first row of the worksheet.  
  


  * Review the worksheet tab name before selecting it in the action.  
  


  * Make sure Google Sheets premium workflow actions are enabled for the account if required.  
  


  * Refresh headers in the action whenever columns are added, renamed, or reordered.


* * *

## **How to Use the Action to Create Multiple Row(s) in Google Sheets**

  


Create Multiple Spreadsheet Row(s) is best when your workflow needs to add new entries to Google Sheets rather than change rows that already exist. This is useful for writing repeated records, storing grouped data, or sending multiple values into a spreadsheet during one workflow execution.

  


  1. Go to **Automations** > **Workflows**.  
  
![](https://jumpshare.com/share/0JWEsWQU9NawnWRXArkh+/Screen+Shot+2026-04-06+at+21.20.01.png)  
  


  2. Create a **new** **workflow** or **edit** an **existing** one.  
  
![](https://jumpshare.com/share/BXEsCvFYK7i5WsZpbUNj+/Screen+Shot+2026-04-06+at+21.21.45.png)  
  


  3. **Add** a relevant **trigger** like Contact Created, Form Submitted, etc.  
  
![](https://jumpshare.com/share/u1UFwknt8WsBsvkvjHaE+/GIF+Recording+2026-04-08+at+20.15.07.gif)  
  


  4. Click on the **+** button to add an Action.  
  


  5. Search for **Google** **Sheets** action and **click** **on it to select the action**.  
  


  6. **Connect** your **location's** Google Account.  
  
![](https://jumpshare.com/share/FZLxmIbexGB6cmaB4lRS+/GIF+Recording+2026-04-08+at+20.16.38.gif)  
  


  7. After connecting your Google Account, select **Create Multiple Spreadsheet Row(s)** from the **Action dropdown**.  
  
![](https://jumpshare.com/share/VKJM23utsNxLgvLCF5lt+/Screen+Shot+2026-04-08+at+20.24.33.png)  
  


  8. All your **integrated** **Google** **accounts** in your **sub** **account** will be displayed in the dropdown menu for you to choose from. **Select any 1**.  
  


  9. Now select the **Drive** in which your spreadsheet resides.  
  
![](https://jumpshare.com/share/2vicPz07nBCO9DeVN0Gt+/Screen+Shot+2026-04-08+at+20.32.09.png)  
  


  10. After selecting the drive, in the next dropdown you will get a list of all the **spreadsheets** present in the drive. Select the one in which you want to make the changes and also **select** the **worksheet**.  
  
![](https://jumpshare.com/share/JENuPFXLxh7AFgXgbu6T+/Screen+Shot+2026-04-08+at+20.33.53.png)  
  


  11. If you need to update the headers in the sheet, you can click the "**Refresh** **Headers** " button to fetch the latest header values from the sheet. This ensures that your data is correctly mapped to the correct columns in the sheet and that your workflow is up-to-date with the latest sheet configurations.  
  
![](https://jumpshare.com/share/BMPXz4FX5YgDdSrxq9po+/Screen+Shot+2026-04-08+at+20.38.37.png)  
  


  12. Selecting Start column and End Column in the worksheet - When sending data to a Google Sheets document using our workflow system, the **sheet's first row is automatically considered the header row** , and **each Column is labeled based on the header values in that row**.  
  


  13. By providing this functionality, our system makes it easy to automate data management processes and ensure the accuracy of your data workflows.  
  


  14. Click on **Save Action**.  
  
![](https://jumpshare.com/share/Ws0DiAH8zry7zNA6izw6+/GIF+Recording+2026-04-08+at+20.49.42.gif)  
  


### **How Create Multiple Spreadsheet Row(s) Works**

  


Create Multiple Spreadsheet Row(s) only creates multiple rows when the **workflow run receives your data as an** **array (list) of row objects**.

  


  * **Each****object** in the **array** becomes **one****spreadsheet****row**.  
  

  * If the workflow run only has data for a single record (for example, one contact enrolled into the workflow), the action will write **one row** , which may feel the same as a single-row create action.  
  

  * The action d**oes not automatically “wait” and batch contacts** that enter the workflow at different times. It **writes whatever array is available in that single workflow execution**.


  


**Example array (creates 3 rows)**

  


[

{

"Name": "Sam",

"Email": "sam@test.com",

"Status": "New"

},

{

"Name": "Arjun",

"Email": "arjun@example.com",

"Status": "In Progress"

},

{

"Name": "Meera",

"Email": "meera@example.com",

"Status": "Completed"

}

]

  


**Example 2:**

  

    
    
    [
      { FirstName: "John", LastName: "Doe", Email: "john@email.com" },
      { FirstName: "Jane", LastName: "Smith", Email: "jane@email.com" }
    ]
    

  


### **How to Pass Multiple Rows into the Action**

  


To create multiple rows in one workflow execution, the workflow must start with (or build) an array of row objects. Common ways to do this include:

  


  * **Inbound Web-hook Trigger** that sends a JSON payload containing an array of rows.  
  

  * **A web-hook based integration** where a previous step returns an array that you map into this action.  


  

    
    
    **Note:** If you need to write thousands of existing contacts (for example, 5,000 contacts already in the CRM), enrolling contacts one-by-one will trigger separate workflow runs and will not batch them automatically.
    

  


### **Best use cases**

  


  * Logging repeated workflow outputs into a spreadsheet.  
  


  * Recording grouped entries from a single automation.  
  


  * Saving multiple related data points for tracking or reporting.


* * *

## **How to Use the Action to Update Multiple Row(s) in Google Sheets**

  


Update Multiple Spreadsheet Row(s) is useful when spreadsheet rows already exist and the workflow needs to modify values within a selected row range. This helps maintain accurate records without creating duplicate entries and is helpful when existing spreadsheet data needs to stay current over time.

  


  1. Go to **Automations** > **Workflows**.  
  
![](https://jumpshare.com/share/0JWEsWQU9NawnWRXArkh+/Screen+Shot+2026-04-06+at+21.20.01.png)  
  


  2. Create a **new** **workflow** or **edit** an **existing** one.  
  
![](https://jumpshare.com/share/BXEsCvFYK7i5WsZpbUNj+/Screen+Shot+2026-04-06+at+21.21.45.png)  
  


  3. **Add** a relevant **trigger** like Contact Created, Form Submitted, etc.  
  
![](https://jumpshare.com/share/u1UFwknt8WsBsvkvjHaE+/GIF+Recording+2026-04-08+at+20.15.07.gif)  
  


  4. Click on the **+** button to add an Action.  
  


  5. Search for **Google** **Sheets** action and **click** **on it to select the action**.  
  


  6. **Connect** your **location's** Google Account.  
  
![](https://jumpshare.com/share/FZLxmIbexGB6cmaB4lRS+/GIF+Recording+2026-04-08+at+20.16.38.gif)  
  


  7. After connecting your Google Account, select **Update Multiple Spreadsheet Row(s)** from the **Action dropdown**.  
  
![](https://jumpshare.com/share/AiPRH2CBOeXcZIS7MMZQ+/Screen+Shot+2026-04-08+at+20.59.28.png)  
  


  8. All your **integrated** **Google** **accounts** in your **sub** **account** will be displayed in the dropdown menu for you to choose from. **Select any 1**.  
  


  9. Now select the **Drive** in which your spreadsheet resides.  
  
![](https://jumpshare.com/share/y3riMM76YT9ad9YH5t0J+/Screen+Shot+2026-04-08+at+21.08.50.png)  
  


  10. After selecting the drive, in the next dropdown you will get a list of all the **spreadsheets** present in the drive. Select the one in which you want to make the changes and also **select** the **worksheet**.  
  
![](https://jumpshare.com/share/xI9dyp1lqWRJ8Kc1nvHm+/Screen+Shot+2026-04-08+at+21.13.37.png)  
  


  11. Enter the **row** **number** from which you would like to update the sheet.  
  


  12. Selecting **Start column** and **End Column** in the worksheet: When sending data to a Google Sheets document using our workflow system, the sheet's first row is automatically considered the header row, and each Column is labeled based on the header values in that row.  
  


  13. If you need to update the headers in the sheet, you can click the "**Refresh** **Headers** " button to fetch the latest header values from the sheet. This ensures that your data is correctly mapped to the correct columns in the sheet and that your workflow is up-to-date with the latest sheet configurations.  
  


  14. By providing this functionality, our system makes it easy to automate data management processes and ensure the accuracy of your data workflows.  
  
![](https://jumpshare.com/share/C8GCswkgzYdlhgLw20lI+/Screen+Shot+2026-04-08+at+21.19.54.png)  
  


  15. Click on **Save Action**.  
  
![](https://jumpshare.com/share/0m3kf2wvKYTK7AAbJSDw+/Screen+Shot+2026-04-08+at+21.22.20.png)  
  


### **When to use this option**

  


  * The spreadsheet row already exists.  
  


  * You need to replace or refresh values in current records.  
  


  * You want to avoid adding duplicate rows for the same data set.


* * *

## **Frequently Asked Questions**

  


**Q: What is the difference between Create Multiple Spreadsheet Row(s) and Update Multiple Spreadsheet Row(s)?**  
Create Multiple Spreadsheet Row(s) adds new spreadsheet entries. Update Multiple Spreadsheet Row(s) changes values in rows that already exist.

  


**Q: How is Create Multiple Spreadsheet Row(s) different from creating a single row?**

Create Multiple Spreadsheet Row(s) can write many rows in one workflow execution, but only when you pass an **array of row objects**. If your workflow execution only has one record’s data, it will create one row.

  


**Q: Does this action automatically batch contacts enrolled into the workflow?**

No. Workflows do not automatically collect multiple contacts and send them as a single batch. To write multiple rows in one request, your workflow run must already contain a batch array (commonly sent via an Inbound Webhook).

  


**Q: Do I need headers in my Google Sheet?**  
Yes. Clear headers help HighLevel recognize the available columns for mapping and reduce setup errors.

  


**Q: Why should I refresh headers?**  
Refreshing headers updates the available column names inside the workflow action after changes are made to the spreadsheet.

  


**Q: What happens if I choose the wrong worksheet tab?**  
The workflow may write data to the wrong location or fail to map the expected columns correctly.

  


**Q: Can I limit which columns are used?**  
Yes. The Starting Column and Ending Column fields define the column range available for mapping.

  


**Q: When should I use multiple-row actions instead of a standard row action?**  
Use multiple-row actions when your workflow needs to create or update several spreadsheet rows as part of the same process.

  


**Q: Can I update existing rows without creating duplicates?**  
Yes. Use Update Multiple Spreadsheet Row(s) when the target rows already exist and only the values need to be changed.

  


**Q: Why is my new column not showing in the workflow action?**  
The action may still be using an older sheet structure. Click Refresh Headers after adding or renaming spreadsheet columns.

* * *

### **Related Articles**

  


  * [Workflow Action - Google Sheets](<https://help.gohighlevel.com/en/support/solutions/articles/155000003294>)  
  


  * [Guide to Google Sheets Premium Workflow Action](<https://help.gohighlevel.com/en/support/solutions/articles/48001238162>)  
  


  * [Workflow Builder Walkthrough](<https://help.gohighlevel.com/en/support/solutions/articles/155000001254>)

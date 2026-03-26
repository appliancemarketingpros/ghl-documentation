# Workflow Trigger - Contact Tag

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001213546-workflow-trigger-contact-tag](https://help.gohighlevel.com/support/solutions/articles/48001213546-workflow-trigger-contact-tag)  
**Category:** Workflows  
**Folder:** Workflow Builder

---

Tags are a way of categorizing your contacts. You can tag any contact in your contacts list with one or more tags to help you find it again later. Tags are used for searching, browsing, sorting, and organizing content. They also allow you to fire off automation, bulk Emails, SMS, etc. In this article, we will be covering How a Tag can fire off a Workflow.

* * *

**Covered in this Article:**

**What does the Contact Tag Workflow trigger do?**

**What can cause a tag to get added or removed?**

Added/Removed manually via the contacts list (single contact or bulk action):

Added/Removed via a workflow:

Added (only) via third-party integration tools like Zapier:

Added via a CSV import

* * *

## **What does the Contact Tag Workflow trigger do?**

  


The contact tag workflow trigger step checks if any tag is added to a contact or removed from a contact.  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48215643927/original/NxWCYmWtbjepAgd2ROUG-Rvoomj2nwA94g.png?1649877321)**

  
  
You can specify via Filters if you want it to get fired off by a tag getting added or by a tag getting removed. It will fire off for both instances if you do not specify that.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48252865701/original/Wz2eN9U-q9b5FwqGLoyJ_xRol2mbx2MNGw.png?1663948521)

* * *

## **What can cause a tag to get added or removed?**

**  
**

Tags can get added or removed by the following means, and hence fire off a workflow with the trigger step set to Contact Tag with a filter for Tag Added or Tag Removed in case of removals:**  
**  


### **Added/Removed manually via the contacts list (single contact or bulk action):**

### **  
**

You can add tags to a contact or a group of contacts by going to the Contacts List > Selecting the contact(s) > Clicking on the Add tag button. You can Click the Remove Tag button to remove tags.  
**  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48252876878/original/adTvReZ-L4adHf_xcda9ps55YmfXj7K8Lw.gif?1663951791)****  
**  
**Added/Removed via a workflow:**

**  
**

Workflow actions can be used to add or remove tags. Leads that enter a published workflow and reach the add or remove tag action get their tag added or removed.  
**  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48253120218/original/MGuMOlailh9Jmn5kJr0F-ktq3ejUu8GU8A.gif?1664191236)  
**

  
**Added (only) via third-party integration tools like Zapier:**

**  
**

You can use many third-party integration tools to get tags added to your contacts in the CRM. Zapier is one of the most commonly used 3rd party integration tools to make actions happen inside the CRM in response to changes in external apps you may be running. Tags cannot be removed through this method.**  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48253137580/original/3hyA-CiV129r5_T-E-nRbcrNn8N10SVtmQ.gif?1664195112)**

###   


###   
**Added via a CSV import**

  


You can add tags during a CSV import process by having a tags column with a tags column header in the CSV and have tags written out for each contact in that column. You can insert commas and multiple tags for each contact in the same cell.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48253155778/original/bMA50nptY7VxrlZ4Xn6nuRg6MYuD-_Qecw.gif?1664198566)

  


  


You can also add tags during a CSV import by the advanced options of the import process:

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48253160766/original/dLXRneYYvywN9EzigyuPf2g9vD2bEM61HA.gif?1664199340)

  


  
**Please Note:**

  

    
    
     CSV Imports are also used to update the tags of existing contacts, if Allow Duplicate contacts is turned off and the Email and Phone of the contacts being imported is the same as the already existing ones.

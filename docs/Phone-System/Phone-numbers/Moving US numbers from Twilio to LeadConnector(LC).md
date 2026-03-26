# Moving US numbers from Twilio to LeadConnector(LC)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001240108-moving-us-numbers-from-twilio-to-leadconnector-lc-](https://help.gohighlevel.com/support/solutions/articles/48001240108-moving-us-numbers-from-twilio-to-leadconnector-lc-)  
**Category:** Phone System  
**Folder:** Phone numbers

---

**OVERVIEW**  
  
This article provides a step-by-step guide to help agencies or clients move their US local and toll-free Twilio phone numbers into an LC Phone sub-account (within HighLevel), ensuring seamless SMS and voice functionality within the platform.

  

    
    
    **IMPORTANT** : For the process of moving numbers from **Twilio to LC** , customers will need to contact both **HighLevel Support** and **Twilio Support** to facilitate the migration successfully.

  


  

    
    
    **IMPORTANT** : This article is specifically for moving your US local or toll free numbers. For non US (other international countries) refer to [Migrating International Numbers (Twilio to LC Phone)](<https://help.gohighlevel.com/support/solutions/articles/155000005131-migrating-international-numbers-twilio-to-lc-phone->)

* * *

**TABLE OF CONTENTS**

  * Before Moving Your US Twilio Number
  * Key Benefits of moving your US phone number to LC
  * What Is the LC Phone System?
  * Moving Numbers from Client’s Twilio to LC Phone
    * Step 1: Get the Gaining Sub-account SID
    * Step 2: Submit a Ticket to Twilio
  * Final Checklist
  * Frequently Asked Questions
  * Related Articles


* * *

## **Before Moving Your US Twilio Number**

  


There are a few important things to check and prepare to ensure a smooth and successful migration of your Twilio number to an LC Phone sub-account. This section outlines the necessary steps, access, and information you’ll need to complete the migration without issues.

  


  * Access to the client’s Twilio account (must be the account owner).  
  


  * The **Location ID** of the High-Level sub-account where the number will be migrated.  
  


  * A support request was submitted to **HighLevel Support** to obtain the **Gaining Sub-account SID** (LC Phone's Twilio sub-account SID for that location).  
  


  * If the number is **international** , required **regulatory bundles and addresses** must already be approved in Twilio.


* * *

## **Key Benefits of moving your US phone number to LC**

  


  * Centralizes all communication within the HighLevel ecosystem.  
  


  * Enables use of LC Phone features like call tracking, automation, and SMS workflows.  
  


  * Simplifies billing and phone number management for agencies.  
  


  * Provides faster support and troubleshooting through native LC Phone infrastructure.


* * *

## **What Is the LC Phone System?**

  


LC Phone is HighLevel’s built-in phone system that operates via a Twilio ISV (Independent Software Vendor) connection. When you move a client’s Twilio number into their LC Phone sub-account, the number becomes fully managed inside HighLevel without needing a separate Twilio integration. This creates a more stable and feature-rich experience for users. For more, visit [What is LC - Phone System?](<https://help.gohighlevel.com/support/solutions/articles/48001223546-what-is-lc-phone-system->)

* * *

## **Moving Numbers from Client’s Twilio to LC Phone**

  


This section provides a step-by-step guide on how to migrate phone numbers from a client’s Twilio account to an LC Phone sub-account within HighLevel. Follow these instructions carefully to ensure the migration is completed successfully, allowing the number to be fully integrated into the HighLevel platform for seamless communication and management.

  


### **Step 1:** Get the Gaining Sub-account SID

  


  * Go to the sub-account (location) in HighLevel where you want to move the number, and note down the **Location ID** to create a ticket in HighLevel Support.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045914528/original/5DfMUuKIRZ_jxYqO-fVDm-8FQtX5SjBR0g.png?1746016502)  
  


  * Submit a support ticket to **HighLevel** and request the **Gaining Sub-account SID** for this Location (Sub-account)ID.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045914728/original/B_LUxHgCOD_NfyxmBwM7GYe9vHgzWUYr_g.gif?1746016632)  
  


### **Step 2:** Submit a Ticket to Twilio

  


Once you receive the Gaining Sub-account SID from HighLevel Support, you will need to **contact Twilio Support** to **initiate the migration process**. Follow these steps to submit the **support ticket to Twilio** :

  


  * Log in to the client’s Twilio account.  
  


  * Go to [Twilio Support](<http://www.twilio.com>) and create a new ticket.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045917090/original/cfnDcBV885dz3ce5LIjPYnPa7pct4nmZLQ.gif?1746017948)


  


  

    
    
    **_Tip_** _: Sample Format when creating a ticket with Twilio Support_  
      
    **Subject:** Request to Move Phone Number(s) to New Sub-account  
      
    **Priority:** P3 – General  
      
    **CC:** migration@leadconnectorhq.com  
      
    **Message Template:**  
      
     Hi Twilio Support,   
    I would like to move the following phone numbers to a new sub-account -  PASTE_TWILIO_NUMBER_HERE   
    **Losing sub-account SID** -  E.g. AC8a0eac4ea7651eba06137bbf1a907df62d . Replace your own Twilio sub-account SID here where the number is currently in   
    **Gaining sub-account SID** - please contact HighLevel support to get the ISV location's Twilio sub-account SID for you  
    Time-frame: ASAP   
    This migration is essential for business continuity. Please process this request at your earliest convenience.  
    Thanks!

  


  

    
    
    **IMPORTANT** : Once you submit the ticket, Twilio will review your request and respond via the email address you provided. If you have any questions or need help at any point, feel free to contact **HighLevel Support** —we’re here to assist you through the process.

* * *

## **Final Checklist**

  


  * Only the **Twilio account owner** can initiate and authorize the number migration.  
  

  * If migrating **international numbers** , ensure that all **regulatory compliance steps** (such as approved bundles and addresses) are completed in Twilio before submitting the request.  
  

  * The average migration time is typically **24–72 hours** , depending on Twilio's processing time.  
  

  * Always **CC`migration@leadconnectorhq.com`** in your support ticket to ensure proper coordination with the LeadConnector team.


* * *

## **Frequently Asked Questions**

  


**Q: Will my SMS workflows or call tracking be interrupted during the move?**  
There may be a brief downtime during migration. Plan to move numbers during low-traffic hours.

  


  


**Q: Can I move numbers from multiple Twilio accounts into one LC Phone account?**  
Yes, but each migration must be submitted separately and authorized by the original account owner.

  


  


**Q: What happens to billing after migration?**  
The number will be billed through HighLevel (LC Phone), not through the client’s personal Twilio account.

  


  


**Q: This article mentions US local or toll-free numbers. Can I follow the same process for international numbers?**  
No, this process applies only to **US local and toll-free numbers**. For migrating **international numbers** , please refer to this article: [ Migrating International Numbers (Twilio to LC Phone)](<https://help.gohighlevel.com/support/solutions/articles/155000005131-migrating-international-numbers-twilio-to-lc-phone->)

* * *

## **Related Articles**

  * [ Migrating International Numbers (Twilio to LC Phone)](<https://help.gohighlevel.com/support/solutions/articles/155000005131-migrating-international-numbers-twilio-to-lc-phone->)

  * [What is LC - Phone System?](<https://help.gohighlevel.com/support/solutions/articles/48001223546-what-is-lc-phone-system->)

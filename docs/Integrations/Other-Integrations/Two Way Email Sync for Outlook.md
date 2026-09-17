# Two Way Email Sync for Outlook

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001229663-two-way-email-sync-for-outlook](https://help.gohighlevel.com/support/solutions/articles/48001229663-two-way-email-sync-for-outlook)  
**Category:** Integrations  
**Folder:** Other Integrations

---

Outlook Two-Way Email Sync creates a bidirectional connection between a user’s personal Outlook inbox and HighLevel, allowing supported one-to-one email conversations to stay synchronized across both platforms. Messages sent from HighLevel can appear in Outlook, while replies and emails from existing contacts can sync back into HighLevel Conversations, helping users maintain a complete contact history without constantly switching between systems.

  


**TABLE OF CONTENTS**

  * Key Benefits of Outlook Two-Way Email Sync
  * How to Connect Outlook Two Way Email sync?
  * How Outlook Two-Way Email Sync Works
  * Emails Started in HighLevel
  * Emails Received From Existing HighLevel Contacts
  * Emails Sent From Outlook to a New Contact
  * Other functionalities
  * Email Types and Sender Behavior
  * Outlook Two-Way Sync Limitations
  * Frequently Asked Questions
  * Related Articles


  


## **Key Benefits of Outlook Two-Way Email Sync**

  


  * **Centralized conversations:** Keep supported Outlook email conversations visible in HighLevel alongside other contact activity.  
  

  * **Two-way communication:** Send individual emails from HighLevel and keep supported replies synchronized with Outlook.  
  

  * **Existing-contact synchronization:** Incoming Outlook emails from existing HighLevel contacts can appear in Conversations automatically.  
  

  * **Contact creation with BCC:** Add a new contact and conversation to HighLevel when initiating an Outlook email to someone who is not already a contact.  
  

  * **Personal sending identity:** Use the connected Outlook account for supported one-to-one emails rather than relying on the sub-account email provider for those messages.


  


* * *

## **How to Connect Outlook Two Way Email sync?**

  


1\. Open the appropriate **sub-account** in HighLevel, then go to **Settings > My Profile**, 

2\. Scroll to **Email (2-way sync)** , select **Outlook** , and click **Connect**.

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079018246/original/UF8TDp8T6iMMbyzlsrNttM4Z7RiKf3nNAA.gif?1787321044)**

  


4\. Sign in with the Outlook or Microsoft 365 account you want to connect, review and approve the permissions

requested by HighLevel/LeadConnector, 

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079026807/original/iduvTs9ZPGNj5NxZg21qkobvDTumG9TE-g.png?1787325751)

  


5\. Return to **Settings > My Profile > Email (2-way sync)** and confirm that the Outlook email address appears as connected.

  


In "Settings" > "My Profile" scroll down to the section "Email (2-way sync)" to view your email in the connection status.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079027358/original/jwODgjOBbOIbGeeUY6bjdPvr6qIjm2ix4g.png?1787325925)

* * *

## **How Outlook Two-Way Email Sync Works**

  


The way a message enters the conversation determines whether it can synchronize automatically. Knowing these common scenarios helps prevent confusion when a message appears in Outlook but does not immediately appear in HighLevel.

  


### Emails Started in HighLevel

When you send an individual email from HighLevel using your connected Outlook account, the email thread can remain synchronized between HighLevel and Outlook. Subsequent supported replies in that thread can continue appearing in both places.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079028052/original/9jKWVxztSXpqPYq39PZArS1ggHZ7A1of3Q.png?1787326168)

  


  


### **Emails Received From Existing HighLevel Contacts**

  


When an existing HighLevel contact sends an email to the connected Outlook inbox, the incoming message can synchronize into that contact's conversation in HighLevel. Replies in the supported thread can continue syncing between the two platforms.

Emails from contacts who are also users in the same sub-account are not synchronized. This protects potentially confidential communication between HighLevel users.

  


### **Emails Sent From Outlook to a New Contact**

  


Outlook two-way sync does not reliably capture every cold inbound or outbound email involving someone who is not already represented as a HighLevel contact. When sending a new email from Outlook to someone who is not yet a contact, use the HighLevel BCC address in the Cc or Bcc field. This can create the contact and conversation in HighLevel so future supported communication can synchronize.

  1. Sync the contact.


  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48274410786/original/O95R2YOy0ICNsr69vc64B2WeyxEaBLfNwQ.png?1673365182)

  
  
  
All subsequent messages in the email thread (initiated from the CRM) will be in sync. Outbound  
emails sent from your email will start reflecting in the CRM and vice versa. 

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48274411519/original/Qcf30hK4rYTieaYlqtiX7wPtH3YSk14exw.png?1673365274)  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48274411984/original/iRhDXxDWcE5l-Tq60A1ApVfKpQYbnuowfw.png?1673365374)

  
  
  


**Please note**
    
    
    Attachments of up to **3 MB** size work across this sync, any attachments larger than this size will cause the message to not sync over. 
    **Supported file types:** JPG,JPEG,PNG,MP4,MPEG,ZIP,RAR,PDF,DOC,DOCX,TXT

  


  


* * *

## **Other functionalities**

  


**Update Email:** This helps users change their connected email ID to another one without disconnecting the previous connection.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48274412595/original/K7lc8soEvt0eZrmsM_N1Bi4SkEDNDfhIsA.png?1673365506)

  


New outbound emails from the CRM will start syncing with the newly added email address. Upcoming messages in the previously connected email ID (same thread) will stop syncing between the CRM & personal email. 

  


**Disconnect Email:** This will disconnect their connection and stop the sync with the CRM. Once disconnected, emails or messages will not sync between both platforms.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48274412884/original/-1hFYB1PHiPT0S6vhujtn2BPxSBXrHPIAA.png?1673365574)

  


  


* * *

## **Email Types and Sender Behavior**

  


Outlook Two-Way Email Sync is intended primarily for direct, one-to-one conversations. Bulk and automated messages use different sending infrastructure, so they should not be expected to behave like personal Outlook conversations.

  


  * **Individual emails:** Supported one-to-one emails can use the connected Outlook account and synchronize with the personal inbox.  
  

  * **Bulk emails:** Bulk email sending is handled separately from personal two-way sync and may use the configured sub-account email provider.  
  

  * **Workflow and automation emails:** Automated emails are sent through the configured sub-account-level provider rather than through the user's personal Outlook two-way sync. These messages do not synchronize with the Outlook inbox in the same way as individual emails.


* * *

## **Troubleshoot Outlook Two-Way Email Sync**

  


### **My Profile Is Missing**

  


The **My Profile** tab is available when the user is added to the sub-account currently being viewed. If you cannot see My Profile:

  1. Confirm that you are inside the intended sub-account rather than the agency-level view.
  2. Verify that your user has been added to that sub-account.
  3. If appropriate for your access level, use **Login As** for a user of that sub-account.
  4. Return to **Settings** and check for **My Profile** again.


* * *

## **Outlook Two-Way Sync Limitations**

  * Emails from contacts who are also sub-account users are not synchronized because they may contain confidential user-to-user communication.  
  

  * Gmail/Outlook two-way sync does not reliably capture cold inbound email from unknown senders; HighLevel documents inbound email from existing contacts as supported for this configuration.  
  

  * Workflow and automation email is sent through the configured sub-account email provider rather than the personal Outlook connection.  
  

  * Removing or disconnecting a synchronized account stops new synchronization, but previously synchronized email remains available.  
  

  * Historical messages from before a personal inbox connection was established are not backfilled through two-way sync.


* * *

## **Frequently Asked Questions**

### **Q: Does connecting Outlook import my historical email?**

No. Messages from before the integration was connected are not synchronized retroactively. Only supported conversations after the connection is established can sync.

**  
**

### **Q: Why can I not see My Profile?**

The **My Profile** tab is available when the user has been added to the sub-account currently being viewed. Verify that you are in the correct sub-account and that your user has access to it before troubleshooting Microsoft permissions.

  


### **Q: What should I do if Reconnect is not displayed?**

Verify that you are in the correct sub-account and that the Outlook mailbox appears under **Settings > Email Services**. If the mailbox is present but the expected reconnect or account-management control is still missing, contact HighLevel Support instead of repeatedly reauthorizing Microsoft permissions.

  


### **Q: When should I contact HighLevel Support?**

Contact HighLevel Support if reconnecting does not restore synchronization, the same permission error continues after verifying the correct Microsoft account and permissions, or the expected HighLevel controls are unavailable. Include the affected email address, error details, screenshots, provider, approximate start time, and troubleshooting steps already completed.

* * *

  


### Related Articles

  * [Getting Started - Connect Personal Inbox](<https://help.gohighlevel.com/support/solutions/articles/155000005066/?utm_source=chatgpt.com>)
  * [Email Failure: Insufficient Permission for 2-Way Sync](<https://help.gohighlevel.com/support/solutions/articles/155000006053/?utm_source=chatgpt.com>)
  * [Connect Google to Use Gmail for Email](<https://help.gohighlevel.com/support/solutions/articles/48001235216-how-to-set-up-two-way-email-sync-for-gmail?utm_source=chatgpt.com>)
  * [Inbound Email Workflow Trigger in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email?utm_source=chatgpt.com>)


* * *

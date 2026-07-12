# Email Failure: Insufficient Permission for 2-Way Sync

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006053-email-failure-insufficient-permission-for-2-way-sync](https://help.gohighlevel.com/support/solutions/articles/155000006053-email-failure-insufficient-permission-for-2-way-sync)  
**Category:** Integrations  
**Folder:** Other Integrations

---

The "Email Failure: Insufficient Permission for 2-Way Sync" error occurs when HighLevel no longer has the required permissions to access your connected email account (such as Gmail or Outlook). This typically happens when:  
  


  * Email account permissions have been revoked.  
  

  * Your email provider requires you to reauthorize the connection.  
  

  * Your account security settings have changed.  
  

  * The connected mailbox has been disconnected or expired.


  
Reconnecting your email account restores the required permissions and allows two-way email sync to function normally.

* * *

**TABLE OF CONTENTS**

  * Before You Begin: Verify the Error Message
  * Why This Happens
  * How to Resolve the Issue
  * Step 1: Open Email Services
  * Step 2: Reconnect the Email Account
  * Step 3: Verify the Connection
  * If the Problem Persists
  * If the issue continues after completing these steps, contact HighLevel Support with:
  * Frequently Asked Questions
  * Related Troubleshooting
  * Still Need Help?


* * *

## **Before You Begin: Verify the Error Message**

  


This article applies only if you see one of the following messages:  
  


  * **Email Failure:** Insufficient Permission for 2-Way Sync  
  

  * Insufficient Permission  
  

  * Errors indicating HighLevel no longer has permission to access your connected inbox


  
This article does not apply to these errors:  
  


Error Message| Likely Cause| Recommended Action  
---|---|---  
Insufficient funds to send email| Email sending credits or wallet balance are insufficient| Refer to the Email Credits or Billing documentation.  
Authentication Failed| Invalid SMTP credentials| Review your SMTP configuration.  
Email quota exceeded| Sending limits reached| Check your email provider's sending limits.  
Domain not verified| Email authentication or DNS issue| Verify your sending domain.  
  
  

    
    
    **Important:** If your error says "Insufficient funds to send email," this is not a permissions issue. Reconnecting your inbox will not resolve the problem. Instead, review your email credits, wallet balance, or billing configuration.

* * *

## **Why This Happens**

  


This error usually occurs when HighLevel loses authorization to your connected email provider.  
  


Common reasons include:  
  


  * Your Google or Microsoft account permissions were revoked.  
  

  * You changed your email account password.  
  

  * Your organization's security policy invalidated existing OAuth tokens.  
  

  * The connected email account was removed or disconnected.  
  

  * Your email provider requires you to grant permissions again after a security update.


* * *

## **How to Resolve the Issue**

  


#### ** _Step 1: Open Email Services_**  
  


  1. Navigate to Settings.  
  

  2. Select Email Services.  
  

  3. Locate the connected email account.


####   
**_Step 2: Reconnect the Email Account_**

  
If the account displays an error or requires attention:  
  


  1. Click Reconnect (or remove and reconnect the mailbox if necessary).  
  

  2. Sign in using the correct email account.  
  

  3. Review the requested permissions.  
  

  4. Select Allow to grant HighLevel access.  
  


    
    
    **Note:** Granting all requested permissions is required for two-way email synchronization to function properly.

  


  


#### **_Step 3: Verify the Connection_**

  
After reconnecting:  
  


  * Confirm the email account shows as Connected.  
  

  * Send a test email.  
  

  * Verify that:  
  

    * The email is sent successfully.  
  

    * Replies appear in Conversations.  
  

    * Email synchronization resumes normally.


###   
**_If the Problem Persists_**

  
If reconnecting the email account does not resolve the issue:  
  


  * Disconnect and reconnect the mailbox again.  
  

  * Ensure you're signing in with the correct email account.  
  

  * Verify that your Google Workspace or Microsoft 365 administrator has not restricted third-party app permissions.  
  

  * Confirm that no recent security policy changes have removed HighLevel's access.  
  

  * Try reconnecting from an incognito/private browser window.


###   
**_If the issue continues after completing these steps, contact HighLevel Support with:  
_**

  * The affected email address  
  

  * A screenshot of the error  
  

  * The email provider (Google Workspace, Gmail, Outlook, Microsoft 365, etc.)  
  

  * The approximate time the error first occurred


* * *

## **Frequently Asked Questions**

  


**Q. Does reconnecting delete my emails?**

A. No. Reconnecting only restores authorization between HighLevel and your email provider. Existing emails remain intact.

  
**Q. Why did this happen if it was working before?**

A. Email providers periodically invalidate authorization tokens after password changes, security updates, administrator policy changes, or permission revocations.

  
**Q. Does this affect sending and receiving emails?**

A. Yes. Without the required permissions, HighLevel may be unable to send emails, sync incoming messages, or display replies in Conversations.

* * *

## **Related Troubleshooting**

  
If your error message is different, refer to the appropriate troubleshooting guide:  
  


  * Insufficient funds to send email — [Email Failure: Insufficient Permission for 2-Way Sync](<https://help.gohighlevel.com/en/support/solutions/articles/155000006053>)  
  

  * SMTP Authentication Failed — [Setting Up SMTP Providers](<https://help.gohighlevel.com/en/support/solutions/articles/48001059689>)  
  

  * Domain Verification Failed — [Email authentication and DNS setup](<https://help.gohighlevel.com/en/support/solutions/articles/155000006793>)  


* * *

## **Still Need Help?**

  


If you've completed all the steps above and continue to receive the "Insufficient Permission for 2-Way Sync" error, contact HighLevel Support and include:  
  


  * The exact error message  
  

  * Your email provider  
  

  * Screenshots of the error  
  

  * Steps you've already attempted


  
Providing this information will help expedite troubleshooting.

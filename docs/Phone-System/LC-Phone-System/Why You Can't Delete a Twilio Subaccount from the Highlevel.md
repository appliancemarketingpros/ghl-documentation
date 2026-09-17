# Why You Can't Delete a Twilio Subaccount from the Highlevel?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005822-why-you-can-t-delete-a-twilio-subaccount-from-the-highlevel-](https://help.gohighlevel.com/support/solutions/articles/155000005822-why-you-can-t-delete-a-twilio-subaccount-from-the-highlevel-)  
**Category:** Phone System  
**Folder:** LC Phone System

---

If your HighLevel account uses an externally managed Twilio account, you cannot permanently close that Twilio subaccount from the HighLevel interface. The Twilio subaccount remains controlled through your Twilio account, so final closure must be completed in Twilio. Before closing it, confirm whether you need to keep any phone numbers, recordings, voicemails, or other phone-system assets, because closing the wrong account too early can interrupt migration or cause permanent data loss.

* * *

**TABLE OF CONTENTS**

  * What is an Externally Managed Twilio Subaccount?
  * Key Considerations Before Closing a Twilio Subaccount
  * Determine What You Actually Want to Remove or Move
  * Before You Close an External Twilio Subaccount
  * How To Close an External Twilio Subaccount
  * Frequently Asked Questions
    * Related Articles


# **What is an Externally Managed Twilio Subaccount?**

  


An externally managed Twilio subaccount is a Twilio account object that belongs to your own Twilio account rather than HighLevel's LC Phone environment. HighLevel can use that Twilio connection for calling and messaging, but permanent Twilio account management remains under the control of the Twilio account owner.

  


This is different from a **HighLevel sub-account** , also called a **location**.

  


  * **HighLevel sub-account/location:** A business or client account inside your HighLevel agency.


  


  * **Twilio subaccount:** An account managed within Twilio that can contain phone numbers and telephony configuration.


  


Deleting a HighLevel location and closing a Twilio subaccount are separate actions with different consequences. HighLevel location deletion has its own workflow and 24-hour reversal period, while closing an externally managed Twilio subaccount is handled in Twilio.

* * *

## **Key Considerations Before Closing a Twilio Subaccount**

  


Closing a Twilio subaccount can affect phone numbers, historical phone assets, and migrations that are still in progress. Confirm what you actually want to remove before taking a permanent action.

  


  * **Confirm the account type:** Make sure you are trying to close a Twilio subaccount rather than delete a HighLevel location.


  


  * **Protect phone numbers you need:** Move or migrate any phone numbers you want to keep before closing the Twilio subaccount.


  


  * **Preserve historical assets:** Download recordings or voicemails you need before losing access to the original Twilio environment.


  


  * **Review messaging compliance:** A2P and other phone-system registrations may need to be completed again after migration.


  


  * **Avoid unnecessary closure:** Removing one phone number does not require closing the entire Twilio subaccount.


  


  * **Treat closure as permanent:** Only close the Twilio subaccount after confirming that its remaining assets are no longer needed.


  


HighLevel's migration guidance specifically warns against deleting, releasing, disabling, or disconnecting phone numbers while a migration is in progress unless instructed to do so.

* * *

## **Determine What You Actually Want to Remove or Move**

  


Several different tasks can appear to be a “delete Twilio” problem even though they require different workflows. Identifying the intended outcome first helps prevent unnecessary service interruption or number loss.

###   


### **Delete a HighLevel Sub-Account or Location**

  


If your goal is to remove the entire HighLevel business/location, use the HighLevel sub-account deletion process instead of closing a Twilio subaccount.

HighLevel locations are deleted from Agency View and include a **24-hour reversal period** before deletion becomes permanent.

  


### **Remove a Single Phone Number**

  


If you only want to remove one phone number, you generally do not need to close the entire Twilio subaccount.

HighLevel provides a separate process for removing applicable Twilio-connected phone numbers from a sub-account. Releasing a number is permanent and can make that number available for another customer to purchase, so confirm that you no longer need it first.

###   


### **Move a Number to Another HighLevel Sub-Account**

  


If you want to keep the number but assign it to another HighLevel sub-account, use the appropriate number-move process.

  


HighLevel's **Move Numbers** tool supports eligible moves within the same agency, including:

  


  * LC Phone → LC Phone

  * Twilio → Twilio when both sub-accounts use the same Master Twilio account


  


Different account structures or provider changes require a different migration path.

###   


### **Move from Twilio to LC Phone**

  


If your goal is to stop using your own Twilio account and move to LC Phone, migrate the numbers and applicable sub-account configuration first.

  


Do not close the Twilio subaccount before the migration is complete.

HighLevel now supports migration from an external Twilio account to LC Phone, with the existing phone service remaining active while supported migrations are processed.

###   


### **Permanently Close the External Twilio Subaccount**

  


If you no longer need the Twilio subaccount, its phone numbers, or any remaining data, close it directly from your Twilio account.

  


HighLevel cannot permanently close an externally managed Twilio subaccount on your behalf because that account remains under your Twilio ownership.

* * *

## **Before You Close an External Twilio Subaccount**

  


Reviewing the Twilio subaccount before closure helps prevent the loss of phone numbers and historical assets that do not automatically transfer to another phone environment.

  


Before closing the Twilio subaccount, review:

  


  * Phone numbers you need to retain.

  * Existing migrations or number transfers.

  * Historical call recordings.

  * Voicemails.

  * Phone routing and number assignments.

  * Messaging compliance or A2P registrations.

  * Any workflows or business processes that depend on the existing number.


* * *

### **Preserve Phone Numbers**

  


If you want to keep a phone number, complete the supported migration or move first.

For supported cross-account migrations such as **Twilio → LC Phone** , HighLevel Support coordinates the migration. Current HighLevel documentation states that users should not manually delete, release, disable, or disconnect the number while the move is in progress.

  


### **Preserve Recordings and Voicemails**

  


Historical call recordings and voicemails do not automatically transfer from Twilio to LC Phone.

Download any recordings or voicemail assets you need before closing the Twilio account or losing access to it.

###   


### **Review Messaging Registration**

  


When moving from your own Twilio account to LC Phone, applicable A2P 10DLC registration does not automatically migrate.

  


Affected sub-accounts must complete the applicable registration again through the HighLevel Trust Center after moving to LC Phone.

  


**Moving from Twilio to LC Phone**

  


Migrating to LC Phone allows HighLevel to manage calling and messaging through its built-in phone system instead of requiring your own third-party Twilio connection. Complete the migration before closing the old Twilio environment so your existing numbers can be preserved.

  


The current HighLevel migration flow is:

  


  1. Move the agency to **LC Phone** , if it has not already been connected.

  2. Go to **Agency Settings → Phone Integration → Sub Account Settings**.

  3. Locate the applicable sub-account.

  4. Select **Link to LeadConnector**.

  5. Allow the migration to complete.

  6. Confirm that the expected phone numbers appear under LC Phone.

  7. Recomplete any applicable messaging registrations.

  8. Test inbound and outbound calling and messaging.

  9. Download any historical Twilio recordings or voicemails that need to be retained.

  10. Close the old Twilio subaccount only after confirming that it is no longer needed.


  


Existing sub-accounts are not automatically migrated simply because the agency switches to LC Phone. They must be linked individually.

* * *

## **How To Close an External Twilio Subaccount**

  


Closing an externally managed Twilio subaccount should be the final step after any required number migrations and data preservation are complete. Because HighLevel does not own that external Twilio account, closure must be performed directly in Twilio.

###   


### **Step 1: Confirm That Nothing Needs to Be Migrated**

  


Before opening Twilio:

  1. Confirm that you no longer need the phone numbers in the subaccount.

  2. Verify that any required number migration or port has completed.

  3. Download recordings or voicemails you want to retain.

  4. Confirm that required phone-system configuration has been recreated elsewhere.


  


Do not proceed if a phone-number migration is still in progress.

###   


### **Step 2: Open Your Twilio Account**

  


  1. Sign in to the Twilio account that owns the subaccount.

  2. Open the **Subaccounts** area.

  3. Locate the subaccount you want to close.


###   


### **Step 3: Open the Subaccount Options**

  


  1. Locate the applicable Twilio subaccount.

  2. Open its **More Options** menu.

  3. Select **Close Subaccount**.


  


HighLevel's existing documentation identifies **Close Subaccount** as the Twilio-side action used for this process.

###   


### **Step 4: Confirm the Closure**

  


Review Twilio's closure warning carefully before confirming.

Closing the subaccount is permanent, so complete this step only after verifying that you no longer need its remaining data or telephony assets.

###   


### **Step 5: Verify Your HighLevel Phone Configuration**

  


After closure:

  


  1. Return to HighLevel.

  2. Confirm the intended phone system is active.

  3. Verify that required phone numbers are present.

  4. Test inbound and outbound calling.

  5. Test SMS where applicable.

  6. Confirm phone routing and assignments.


  


If you migrated to LC Phone, also verify applicable messaging compliance or A2P registration before resuming regulated messaging.

* * *

## **Frequently Asked Questions**

  


**Q: Is a Twilio subaccount the same as a HighLevel sub-account?**  
No. A HighLevel sub-account is a business/location inside your agency. A Twilio subaccount is managed inside a Twilio account and can contain telephony resources. They are separate account structures.

  


**Q: Can HighLevel close my externally managed Twilio subaccount?**  
No. An externally managed Twilio subaccount remains under your Twilio account, so permanent closure must be performed in Twilio.

  


**Q: Does this article apply to LC Phone?**  
No. This article specifically addresses externally managed Twilio subaccounts. LC Phone is HighLevel's built-in phone system and is managed through HighLevel.

  


**Q: Should I close Twilio before migrating my phone numbers to LC Phone?**  
No. Complete the number migration first. HighLevel specifically advises against manually deleting, releasing, disabling, or disconnecting numbers while a migration is in progress.

  


**Q: Can I keep my phone number when moving from Twilio to LC Phone?**  
Supported Twilio → LC Phone migrations can move eligible numbers into LC Phone. Use the appropriate HighLevel migration process before closing the old Twilio subaccount.

  


**Q: Do recordings and voicemails move to LC Phone automatically?**  
No. Historical recordings and voicemails remain associated with the previous Twilio account and should be downloaded if you need to retain them.

  


**Q: Can I remove one phone number without closing the whole Twilio subaccount?**  
Yes. Removing or releasing a phone number is a separate process from closing the Twilio subaccount.

  


**Q: Can I move a phone number to another HighLevel sub-account instead?**  
Yes, in supported scenarios. HighLevel's Move Numbers tool supports eligible same-agency moves, while other provider or account combinations use the migration process.

  


**Q: Does A2P registration move automatically from Twilio to LC Phone?**  
No. Applicable A2P 10DLC registrations from the previous Twilio environment must be completed again through HighLevel after migration to LC Phone.

* * *

### **Related Articles**

  


  * [Moving Phone Numbers: Migration Guide](<https://help.gohighlevel.com/support/solutions/articles/155000006369>)

  * [How to Migrate an Agency and Sub-Account to LC Phone](<https://help.gohighlevel.com/support/solutions/articles/48001204027>)

  * [Moving Phone Numbers Across Accounts](<https://help.gohighlevel.com/support/solutions/articles/48001240107>)

  * [Move Phone Numbers Between Sub-Accounts](<https://help.gohighlevel.com/support/solutions/articles/48001203968-moving-numbers-tool-across-sub-accounts>)

  * [How to Delete a Subaccount/Location](<https://help.gohighlevel.com/support/solutions/articles/48001184862-how-to-delete-a-subaccount-location>)

  * [Deleting / Resetting a Twilio Number](<https://help.gohighlevel.com/support/solutions/articles/48000981428-deleting-resetting-a-twilio-number>)

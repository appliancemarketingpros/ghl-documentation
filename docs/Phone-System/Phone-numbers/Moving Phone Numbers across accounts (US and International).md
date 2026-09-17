# Moving Phone Numbers across accounts (US and International)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001240107-moving-phone-numbers-across-accounts-us-and-international-](https://help.gohighlevel.com/support/solutions/articles/48001240107-moving-phone-numbers-across-accounts-us-and-international-)  
**Category:** Phone System  
**Folder:** Phone numbers

---

Phone Number Migration

Moving Phone Numbers Across Accounts (US and International)

Move phone numbers between LC Phone and Twilio, or between LC Phone sub-accounts in different agencies, using a Support-coordinated migration process.

Overview

Phone numbers can be moved between LC Phone and Twilio or between LC Phone sub-accounts that belong to different agencies. The exact information required depends on the migration direction and whether the number is US-based or international.

HighLevel Support coordinates these supported cross-account migrations end-to-end, so you do not need to open a separate Twilio Support ticket. Preparing the correct Account SID, Location ID, phone numbers, and any applicable regulatory information helps prevent delays.

This guide explains which migration path to use, what to prepare, how to submit the request, and what to verify after the numbers move.

Important

Do not manually delete, release, disable, or disconnect a phone number while a migration is in progress unless HighLevel Support specifically instructs you to do so. Wait until Support confirms the move is complete and you have tested the number in the destination environment.

Table of Contents

What is Phone Number Migration Across Accounts? Key Benefits of the Phone Number Migration Process Supported Migration Scenarios What You Need Before Migrating How to Set Up a Phone Number Migration Across Accounts Moving International Phone Numbers What to Check After the Migration Troubleshooting Phone Number Migrations Frequently Asked Questions Related Articles

# **What is Phone Number Migration Across Accounts?**

Phone number migration moves an existing phone number from one supported phone environment to another without requiring you to purchase a replacement number. HighLevel Support coordinates supported LC Phone → Twilio, Twilio → LC Phone, and LC Phone → LC Phone migrations when the LC Phone sub-accounts belong to different agencies.

This process is different from **porting**. Migration is used when moving supported LC Phone or Twilio-managed numbers across compatible accounts. If the number currently belongs to a non-Twilio external carrier, use the phone-number porting process instead.

## **Key Benefits of the Phone Number Migration Process**

A coordinated migration allows businesses to retain established phone numbers while changing the account or phone environment that manages them. Preparing the required information before submitting the request helps reduce delays and makes post-migration validation easier.

  * **Keep Existing Numbers:** Move eligible phone numbers instead of replacing numbers customers already know.
  * **Centralized Coordination:** HighLevel Support coordinates supported cross-account moves from request through cutover.
  * **Clearer Migration Planning:** Required IDs and regulatory details can be prepared before the migration request is submitted.
  * **Support for Multiple Numbers:** Multiple eligible numbers can be included in the same migration request.
  * **Post-Migration Validation:** Calls, SMS, compliance, routing, and number assignments can be verified after cutover before normal traffic resumes.


## **Supported Migration Scenarios**

The correct migration path depends on the phone system currently holding the number and where the number needs to go. Use the table below to identify the correct process before collecting IDs or submitting a request.

Migration| When to Use It| Process  
---|---|---  
**LC Phone → Twilio**|  Move an LC Phone-managed number into the customer's own Twilio account.| HighLevel Support coordinates the migration.  
**Twilio → LC Phone**|  Move a number from the customer's Twilio account into an LC Phone sub-account.| HighLevel Support coordinates the migration.  
**LC Phone → LC Phone, Different Agencies**|  Move an LC Phone number between sub-accounts that belong to different HighLevel agencies.| HighLevel Support coordinates the inter-agency move.  
**LC Phone → LC Phone, Same Agency**|  Move a number between two LC Phone sub-accounts under the same agency.| Use the in-app **Move Numbers** tool instead of this cross-account process.  
**External Carrier → HighLevel**|  The number is held by a carrier outside the supported LC Phone/Twilio migration paths.| Use the phone-number porting process.  
  
**No separate Twilio ticket is required for the three cross-account scenarios covered by this article.** Submit the required migration information to HighLevel Support and the migration will be coordinated for you.

## **What You Need Before Migrating**

Gathering the correct identifiers before contacting Support prevents unnecessary back-and-forth. The information required changes depending on the migration direction, so confirm the source and destination before submitting your request.

Scenario| Prepare  
---|---  
**LC Phone → Twilio**|  Gaining Twilio Account SID, HighLevel Location ID for the affected LC Phone sub-account, phone number(s), and preferred cutover window.  
**Twilio → LC Phone**|  Losing Twilio Account SID, destination HighLevel Location ID, phone number(s), and preferred cutover window.  
**LC Phone → LC Phone, Different Agencies**|  Destination Location ID, phone number(s), preferred cutover window, and source Location ID when available.  
**International Number**|  Applicable Regulatory Bundle SID, Address SID, destination Location ID when applicable, phone number(s), country, number type, and preferred cutover window.  
  
Phone Number Format

Provide each phone number in **E.164 format** whenever possible. For example, a US number should be submitted as **+1XXXXXXXXXX**.

**Security:** Do not include your Twilio Auth Token, password, payment information, or other credentials in a standard migration ticket unless HighLevel Support specifically provides an approved method for submitting that information.

## **How to Set Up a Phone Number Migration Across Accounts**

The migration begins by identifying the source and destination, collecting the required account identifiers, and submitting one complete request to HighLevel Support. Providing all required details in the initial request gives the migration team the information needed to coordinate the cutover.

### **Step 1: Identify the Migration Direction**

Confirm whether the number is moving from LC Phone to Twilio, from Twilio to LC Phone, or between LC Phone sub-accounts in different agencies. This determines which Account SID or Location ID must be included.

### **Step 2: Find the Twilio Account SID When Required**

The Twilio Account SID identifies the Twilio account involved in a US LC Phone ↔ Twilio migration.

  * **LC Phone → Twilio:** Provide the **gaining Twilio Account SID** for the destination Twilio account.
  * **Twilio → LC Phone:** Provide the **losing Twilio Account SID** where the number currently resides.
  * **LC Phone → LC Phone across different agencies:** A Twilio Account SID is generally not required for this LC-to-LC move.


In Twilio, open the **Account Dashboard** and locate **Account Info**. Copy the Account SID for the applicable account.

![Twilio Account Dashboard showing the Account SID under Account Info](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054160307/original/o5oSPy13Wa2SCDElTiah8rlKOI8s74LdwQ.jpeg?1758293602)

The Twilio Account SID is available from the Account Dashboard under Account Info. Only the Account SID is required for the standard migration request.

### **Step 3: Find the HighLevel Location ID**

The Location ID, also called the Sub-account ID, identifies the HighLevel sub-account involved in the migration. For Twilio → LC Phone and inter-agency LC Phone moves, the destination Location ID is especially important. For LC Phone → Twilio, include the Location ID of the affected LC Phone sub-account so Support can identify the source location.

  1. Open the applicable HighLevel sub-account.
  2. Go to **Settings → Business Profile**.
  3. Locate and copy the **Location ID**.


![HighLevel Business Profile Settings showing the Location ID](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054160913/original/MuHzpQF5_gS-jMkoIU47bJNg2hvRs4tLqA.png?1758293832)

The Location ID is available in Settings → Business Profile for the applicable HighLevel sub-account.

### **Step 4: Submit the Migration Request to HighLevel Support**

Submit one HighLevel Support request containing all migration details. Support will coordinate the supported cross-account migration and notify you when the number is ready for validation.

Include in the Request

  * Migration direction: LC Phone → Twilio, Twilio → LC Phone, or LC Phone → LC Phone across different agencies
  * Phone number(s) in E.164 format
  * Applicable Twilio Account SID for US LC Phone ↔ Twilio moves
  * Applicable HighLevel Location ID(s)
  * Regulatory Bundle SID and Address SID for applicable international numbers
  * Country and number type for international numbers
  * Your preferred cutover window


![HighLevel Support flow for submitting a migration request](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045972735/original/ruMK9XOl0NIlCzM2UaF8MuauyxRqZpVpiw.gif?1746109415)

Contact HighLevel Support and provide the migration details in one request so the phone team can coordinate the move.

## **Moving International Phone Numbers**

International phone numbers can require country- and number-type-specific regulatory information before they can be moved. Preparing the correct Regulatory Bundle and Address information before submitting the migration request helps prevent the transfer from being blocked by compliance requirements.

Prepare the Following

  * **Regulatory Bundle SID** applicable to the number's country and number type
  * **Address SID**
  * Destination Location ID when applicable
  * Phone number(s), including country code
  * Country and number type, such as local, mobile, or toll-free
  * Preferred cutover window


### **Check Regulatory Approval Before the Move**

Regulatory requirements vary by country and number type. Confirm that any required Address or Regulatory Bundle is current and approved and that the submitted documentation matches the destination requirements.

[ Learn how to create Regulatory Bundles and Addresses → ](<https://help.gohighlevel.com/support/solutions/articles/48001213216-regulatory-bundle-and-address-creation-for-sub-accounts>)

## **What to Check After the Migration**

A successful number move does not guarantee that every routing, messaging, compliance, or user setting in the destination environment is already configured. Validate the number immediately after Support confirms the migration so issues can be identified before normal call or SMS traffic resumes.

  1. **Confirm the number appears in the destination environment.**
  2. **Place an inbound test call** from another phone.
  3. **Place an outbound test call** from the migrated number.
  4. **Test inbound and outbound SMS** when messaging is enabled.
  5. **Review call routing, forwarding, voicemail, user assignments, and workflow references.**
  6. **Review A2P 10DLC status.** A2P registration is associated with the account/sub-account environment and should not be assumed to transfer with the number. Complete or verify registration in the destination and attach applicable numbers to the approved campaign.
  7. **Review Toll-Free Verification and country-specific compliance.** Confirm the migrated number meets the destination environment's current compliance requirements before relying on SMS.
  8. **Keep the migration ticket open until validation is complete.**


**Historical recordings and voicemails:** Moving the phone number does not migrate historical recordings or voicemail assets into a new phone environment. Download any historical assets you need to retain before losing access to the source environment.

## **Troubleshooting Phone Number Migrations**

Migration delays are commonly caused by missing identifiers, regulatory requirements, incorrect destination information, or post-migration configuration. Start with the migration ticket and confirm that the source, destination, and phone numbers match the original request.

Support is asking for additional information

Confirm that the ticket includes the phone numbers, migration direction, applicable Twilio Account SID, HighLevel Location ID, and regulatory information for international numbers.

An international number is not moving

Verify that the applicable Regulatory Bundle and Address are approved for the correct country and number type. Country-specific requirements can delay the move until compliance information is complete.

The number moved, but SMS is not working

Review the destination's A2P 10DLC, Toll-Free Verification, SMS permissions, and other applicable compliance requirements. A phone-number move does not automatically guarantee messaging compliance in the destination account.

The number moved, but calls are routing incorrectly

Review the destination number's forwarding settings, voicemail, user assignments, call routing, and any workflows or automations that reference the number.

You are moving numbers inside the same agency

Do not use the cross-account process when both eligible LC Phone sub-accounts belong to the same agency. Use the in-app **Move Numbers** tool under Agency Settings → Phone Integration.

## **Frequently Asked Questions**

Q: Do I need to open a separate Twilio Support ticket?

No. For the supported LC Phone → Twilio, Twilio → LC Phone, and LC Phone → LC Phone across different agencies scenarios covered here, submit the required information to HighLevel Support. HighLevel coordinates the migration end-to-end.

Q: How long does a cross-account migration take?

A typical migration can take approximately 1–2 business days after Support has all required information. International numbers or migrations requiring additional regulatory review can take longer. Support will confirm the applicable cutover window.

Q: Can I migrate multiple phone numbers in one request?

Yes. Include all applicable phone numbers in a single list and clearly identify the source and destination. For larger lists, organize the numbers so Support can validate each number during the migration.

Q: Does A2P 10DLC registration move with the phone number?

Do not assume it does. A2P status is associated with the account or sub-account environment rather than only the phone number. After migration, verify or complete A2P registration in the destination and confirm that applicable numbers are attached to an approved campaign before relying on A2P messaging.

Q: Do historical call recordings and voicemails migrate?

No. Historical recordings and voicemail assets do not move automatically with the phone number. Download any historical assets you need to retain before you lose access to the source phone environment.

Q: Should I disable or delete LC Phone before moving the number to Twilio?

Do not manually delete, release, or disable the number during the migration unless HighLevel Support instructs you to do so. Wait until the migration is confirmed and you have tested the number in the destination environment.

Q: What if both sub-accounts are in the same HighLevel agency?

Eligible same-agency LC Phone → LC Phone moves should use the built-in **Move Numbers** tool under Agency Settings → Phone Integration instead of the cross-account Support process described here.

Q: Is moving an LC Phone or Twilio number the same as porting?

No. The migration process covered here moves eligible LC Phone or Twilio numbers between supported account environments. If the number belongs to a different external carrier, use the phone-number porting process.

### **Related Articles**

[ Moving Phone Numbers: Migration Guide ](<https://help.gohighlevel.com/support/solutions/articles/155000006369-moving-phone-numbers-migration-guide>) [ Moving Numbers Between Sub-Accounts (Same Agency) ](<https://help.gohighlevel.com/support/solutions/articles/48001203968-moving-numbers-tool-across-sub-accounts>) [ Regulatory Bundle and Address Creation for Sub-Accounts ](<https://help.gohighlevel.com/support/solutions/articles/48001213216-regulatory-bundle-and-address-creation-for-sub-accounts>) [ Porting Options: US In-App vs International Manual Process ](<https://help.gohighlevel.com/support/solutions/articles/48001211919>) [ How to Migrate an Agency and Sub-Account to LC Phone ](<https://help.gohighlevel.com/support/solutions/articles/48001204027>)

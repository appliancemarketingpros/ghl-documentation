# Moving Numbers Between Sub-Accounts (Same Parent Account)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008620-moving-numbers-between-sub-accounts-same-parent-account-](https://help.gohighlevel.com/support/solutions/articles/155000008620-moving-numbers-between-sub-accounts-same-parent-account-)  
**Category:** Phone System  
**Folder:** LC Phone System

---

Phone Number Management

Moving Numbers Between Sub-Accounts (Same Parent Account)

Use the Move Numbers tool to transfer eligible phone numbers between sub-accounts under the same parent account while keeping the number customers already use.

Overview

The Move Numbers tool allows eligible phone numbers to be transferred between sub-accounts that belong to the same parent account. It supports moves between compatible platform-managed phone environments and compatible connected-provider environments.

The in-app workflow currently supports United States and Canada numbers. Other countries, provider conversions, and unsupported provider-account configurations require a different migration process.

This guide explains eligibility, prerequisites, how to complete the move, what does and does not transfer, and what to verify afterward.

Important

Moving a phone number does not automatically move sub-account-level messaging registration, contacts, conversations, analytics, historical call assets, or every number-level configuration. Review compliance, routing, automations, and assignments in the destination after the move.

Table of Contents

What is the Move Numbers Tool? Key Benefits of the Move Numbers Tool Supported and Unsupported Move Scenarios What You Need Before Moving Numbers How to Move Numbers Between Sub-Accounts What Happens After a Number Is Moved? Troubleshooting and Known Limitations Frequently Asked Questions Need Help?

# **What is the Move Numbers Tool?**  
  


Move Numbers is an account-level tool that reassigns eligible phone numbers from a **source sub-account** to a **destination sub-account** under the same parent account. It eliminates the need to purchase a replacement number when an existing number simply needs to be managed by another sub-account.

The tool is designed for compatible phone environments. Platform-managed numbers can move between compatible platform-managed sub-accounts, while connected-provider numbers can move when both sub-accounts belong to the same connected-provider parent account.

## **Key Benefits of the Move Numbers Tool**  
  


Moving a number under the same parent account provides a faster way to reorganize phone ownership without replacing established business numbers. Understanding the eligibility requirements before starting helps prevent failed transfers and incorrect destination assignments.

  * **Keep Existing Numbers:** Preserve phone numbers customers already recognize while changing the sub-account that manages them.
  * **In-App Transfer:** Complete eligible same-parent-account moves without submitting a manual migration request.
  * **Move Multiple Numbers:** Transfer multiple eligible numbers in the same operation.
  * **Clear Source and Destination Selection:** Choose exactly which sub-account the numbers are leaving and where they should go.
  * **Post-Move Control:** Review routing, messaging compliance, workflows, and assignments before resuming normal traffic.


## **Supported and Unsupported Move Scenarios**  
  


The Move Numbers tool works only when the source and destination meet specific phone-system and account requirements. Confirm the scenario below before attempting an in-app transfer.

Scenario| In-App Move?| What to Do  
---|---|---  
**Platform-managed → platform-managed, same parent account**| **Yes**|  Use Move Numbers.  
**Connected provider → connected provider, same provider parent account**| **Yes**|  Use Move Numbers.  
**Connected provider → connected provider, different provider parent accounts**| **No**|  The in-app tool cannot complete this move. Contact the connected provider's Support team.  
**Connected provider ↔ platform-managed phone service**| **No**|  Use the appropriate provider-migration process instead.  
**US and Canada numbers**| **Yes, when otherwise eligible**|  Use Move Numbers.  
**Numbers outside the US and Canada**| **No**|  Contact Support and follow the applicable international migration process.  
**Sub-accounts under different parent accounts**| **No**|  Use the cross-account phone-number migration process.  
  
**Changing phone providers is not a same-account move.** If the number must change between a connected provider and the platform-managed phone service, use the applicable provider-migration process instead of Move Numbers.

## **What You Need Before Moving Numbers**  
  


Confirming account access, phone-system compatibility, and the correct destination before starting reduces the chance of moving a number to the wrong sub-account or encountering an unsupported configuration.

  * Have the required administrative access to the source and destination sub-accounts.
  * Confirm both sub-accounts belong to the same parent account.
  * Confirm whether the number uses the platform-managed phone service or a connected provider.
  * For connected-provider numbers, confirm both sub-accounts belong to the same provider parent account.
  * Confirm the phone numbers are in the United States or Canada for the in-app workflow.
  * Identify the destination **Location ID** when needed to distinguish similar sub-account names.


### **Find the Destination Location ID**

The Location ID uniquely identifies a sub-account and can help confirm the correct destination. Open the destination sub-account and go to **Settings → Business Profile**.

![Business Profile settings showing the Location ID](https://jumpshare.com/share/CXgGvlch4TfF6DNIAzet+/Screen+Shot+2026-08-14+at+18.07.40.png)

The Location ID appears in Settings → Business Profile for the applicable sub-account.

## **How to Move Numbers Between Sub-Accounts**  
  


The Move Numbers workflow requires you to select the source and destination sub-accounts first, then choose the eligible phone numbers to transfer. Review each selection carefully because the destination becomes the sub-account responsible for those numbers.

### **Step 1: Open the Move Numbers Tool**  
  


Move Numbers is available from the account-level phone integration settings, where phone configuration for sub-accounts is managed.

  1. Open **Settings**.
  2. Go to **Phone Integration**.
  3. Open the **Sub Account Settings** tab.
  4. Click **Move Numbers**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080069959/original/uIEXAa2LWuSqi63tMFiyBIBludQ3iuY1KA.png?1788504306)

Open Phone Integration → Sub Account Settings and select Move Numbers.

### **Step 2: Select the Source and Destination Sub-Accounts**  
  


The source is the sub-account that currently owns the number. The destination is the sub-account that should own the number after the transfer.

  1. Choose the **Source sub-account**.
  2. Choose the **Destination sub-account**.
  3. Confirm both selections before choosing phone numbers.


### **Step 3: Select the Phone Numbers to Move**  
  


Only numbers eligible for the selected source and destination configuration are available. The current interface allows up to **10 phone numbers per move**.

  1. Select the checkbox beside each phone number you want to transfer.
  2. Select up to **10 numbers** for the current move.
  3. Review the selected numbers and destination.
  4. Click **Move Numbers**.


![Move Numbers window showing source and destination sub-accounts and selected phone numbers](https://jumpshare.com/share/68hkKk2TK4agWb0yILt6+/Screen+Shot+2026-08-14+at+18.11.10.png)

Select the source, destination, and eligible phone numbers, then click Move Numbers. Up to 10 phone numbers can be selected per move.

### **Step 4: Verify the Number in the Destination Sub-Account**  
  


A phone number appearing in the destination confirms the ownership change, but routing, messaging, and number-level configuration should still be reviewed before normal traffic resumes.

  1. Open the destination sub-account.
  2. Confirm the phone number appears in the destination phone-number list.
  3. Review number-level settings.
  4. Complete the post-move validation checklist below.


## **What Happens After a Number Is Moved?**  
  


Moving the phone number changes which sub-account manages it, but does not automatically recreate every setting, compliance association, or historical asset in the destination. Review the destination immediately after the move to help prevent missed calls or failed messages.

Item| What to Expect| Action  
---|---|---  
**Phone Number**|  Moves to the destination sub-account.| Confirm it appears in the destination.  
**A2P 10DLC**|  Registration status is associated with the sub-account and does not move with the number.| Verify destination registration and attach the number to the appropriate approved campaign.  
**Toll-Free Verification**|  Do not assume verification automatically transfers with the number.| Confirm the number's verification status after the move.  
**Contacts, Conversations & Analytics**| These are not transferred simply because the phone number moves.| Manage or migrate business data separately when required.  
**Historical Recordings & Voicemails**| Historical assets do not automatically move with the phone number.| Download anything that must be retained before access to the source is removed.  
  
### **Post-Move Validation Checklist**  
  


A quick validation confirms that the destination is ready to receive calls and messages from the moved number.

  * Confirm the number appears in the destination sub-account.
  * Review forwarding and inbound call routing.
  * Review call recording, voicemail, call whisper, and related number settings.
  * Review user assignments.
  * Review workflows, automations, campaigns, and other areas that reference the number.
  * Verify A2P 10DLC or Toll-Free Verification when messaging is used.
  * Place an inbound and outbound test call.
  * Send an inbound and outbound test SMS when messaging is enabled.


## **Troubleshooting and Known Limitations**  
  


If Move Numbers is unavailable, a number does not appear, or the transfer fails, verify the phone environment, provider account, country, and source/destination configuration first. These requirements determine whether the in-app tool can complete the move.

Different Connected-Provider Parent Accounts

Numbers under different connected-provider parent accounts cannot be transferred with the in-app Move Numbers tool. Contact the connected provider's Support team for assistance.

Phone Environment Mismatch

Do not use Move Numbers to convert between a connected provider and the platform-managed phone service. Use the appropriate migration process instead.

Number Is Outside the United States or Canada

The in-app Move Numbers workflow currently supports US and Canada numbers. Contact Support for numbers in other countries.

Missing International Regulatory Configuration

International migrations can require an approved Regulatory Bundle and Address SID in the destination. Complete the required regulatory setup before following the applicable international migration process.

You Need to Move More Than 10 Numbers

The current interface allows up to 10 numbers to be selected per move. Complete additional moves for any remaining eligible numbers.

An Eligible Move Still Fails

If both sub-accounts are under the same parent account, use compatible phone environments, and the numbers otherwise meet the eligibility requirements, contact Support with the source Location ID, destination Location ID, and affected phone number(s).

## **Frequently Asked Questions**  
  


Q: How many phone numbers can I move at once?

The current Move Numbers interface allows a maximum of 10 phone numbers per move. Complete another move for additional eligible numbers.

Q: Does A2P 10DLC registration move with the phone number?

No. A2P status is associated with the sub-account rather than only the phone number. Verify the destination registration and attach the moved number to the appropriate approved campaign.

Q: Does Toll-Free Verification automatically move with a toll-free number?

Do not assume it does. Confirm the toll-free number's verification status and destination messaging configuration after the move.

Q: Can connected-provider numbers move between sub-accounts?

Yes, when both sub-accounts use compatible connected-provider numbers under the same provider parent account and otherwise meet the Move Numbers eligibility requirements.

Q: Can I move numbers between different provider parent accounts?

Not with the in-app Move Numbers tool. Contact the connected provider's Support team for assistance with moves between different provider parent accounts.

Q: Can I change phone providers with Move Numbers?

No. Changing between a connected provider and the platform-managed phone service is a provider migration rather than a same-provider sub-account move.

Q: Do contacts and conversations move to the destination sub-account?

No. Moving the phone number changes the number's assignment; it does not transfer contacts, conversations, or analytics between sub-accounts.

Q: Which countries are supported by the in-app Move Numbers tool?

The in-app tool currently supports United States and Canada numbers. Contact Support for numbers in other countries.

## **Need Help?**  
  


If Move Numbers is unavailable, a transfer fails, or the moved number does not work as expected in the destination, review the items below before contacting Support.

Before Contacting Support

  * Confirm the source and destination sub-accounts are under the same parent account.
  * Confirm both sub-accounts use compatible phone environments.
  * For connected-provider numbers, confirm both sub-accounts belong to the same provider parent account.
  * Confirm the number is a US or Canada number for the in-app workflow.
  * Confirm you are selecting no more than 10 numbers per move.
  * Review A2P 10DLC or Toll-Free Verification after the move.
  * Review call routing, voicemail, assignments, and automations.
  * Test inbound and outbound calls and SMS.


Still Need Help?

Include the following information when contacting Support so the issue can be reviewed efficiently:

  * Source Location ID
  * Destination Location ID
  * Affected phone number(s)
  * Whether the numbers use the platform-managed phone service or a connected provider
  * Country of the affected number(s)
  * Whether the number appears in the destination
  * Whether inbound and outbound calls are working
  * Whether inbound and outbound SMS are working
  * Any errors or screenshots showing the issue

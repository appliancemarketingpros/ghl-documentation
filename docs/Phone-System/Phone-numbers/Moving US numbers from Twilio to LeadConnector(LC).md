# Moving US numbers from Twilio to LeadConnector(LC)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001240108-moving-us-numbers-from-twilio-to-leadconnector-lc-](https://help.gohighlevel.com/support/solutions/articles/48001240108-moving-us-numbers-from-twilio-to-leadconnector-lc-)  
**Category:** Phone System  
**Folder:** Phone numbers

---

LC Phone

# Moving US Phone Numbers from Twilio to LC Phone

Migrate your US phone numbers from your Twilio account to HighLevel's LC Phone system and manage calling, SMS, and messaging registration in one platform.

What You'll Learn

This guide walks you through migrating US local and toll-free phone numbers from your Twilio account to HighLevel's LC Phone system.

You'll learn what information to gather before migration, how to submit a migration request, what moves with the phone number, and how to verify calling, SMS, and messaging registration after the cutover.

Table of Contents

1

What is Phone Number Migration?

2

Key Benefits

3

What Moves with the Phone Number?

4

Before the Migration

5

How to Move a US Number from Twilio to LC Phone

6

Verify the Number After Migration

7

Related Articles

8

Frequently Asked Questions

1

## What is Phone Number Migration?

Phone number migration transfers control of a US local or toll-free phone number from one phone system provider to another. When you migrate a phone number from your Twilio account to HighLevel's LC Phone system, the number becomes managed by LC Phone for all future calling, SMS, and messaging functionality.

This migration process changes which platform manages the number but does not automatically move historical data, call recordings, or messaging registration from your Twilio account.

HighLevel Support coordinates the migration end-to-end after you provide the required account and phone number identifiers.

2

## Key Benefits

Migrating your US phone numbers from Twilio to LC Phone centralizes phone management inside HighLevel and provides access to native LC Phone features.

**Centralized Phone Management** — Manage calling and messaging directly inside HighLevel without switching between platforms.

**Native HighLevel Features** — Use LC Phone functionality such as call tracking, workflows, and messaging automation.

**Simplified Billing** — Manage phone usage and number charges through HighLevel.

**Streamlined Support** — Troubleshoot LC Phone issues through HighLevel Support.

3

## What Moves with the Phone Number?

Moving a phone number changes which phone system manages the number. It does not automatically migrate historical phone-system data from the original Twilio account.

Asset| Migration Behavior  
---|---  
Phone number| Moves to LC Phone  
Future calls and SMS| Route through LC Phone after cutover  
Historical Twilio recordings| Do not automatically migrate  
Historical voicemails| Do not automatically migrate  
Contacts and Conversations| Are not transferred as part of phone number migration  
A2P / Toll-Free registration| Must be verified after migration and may require re-registration  
  
Important

A2P registration may need to be completed again after moving from your own Twilio account to LC Phone. Existing A2P registration from Twilio does not automatically migrate to LC Phone. After migration, complete or verify A2P registration in HighLevel and confirm each applicable US local number is associated with the correct approved Campaign before resuming A2P messaging.

Toll-Free Numbers

After migration, confirm the number's Toll-Free Verification status before resuming messaging. Verification status should not be assumed to transfer automatically.

4

## Before the Migration

Preparing the destination location and preserving information you may need later reduces disruption during the cutover.

Checklist Item

Confirm the destination Sub-account ID

Identify the HighLevel Sub-account ID (Location ID) where the phone number will reside after migration.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080012211/original/pPDXz1VZqFxEPZgeOfM1L_pGevfoEioNtQ.png?1788439872)

Checklist Item

Confirm the losing Twilio Account SID

Locate the Twilio Account SID currently holding the phone number. This identifier is required for the migration request.

Checklist Item

Create a list of all numbers being migrated

Format phone numbers in E.164 format (e.g., +1XXXXXXXXXX) when possible.

Checklist Item

Download any Twilio recordings or voicemails that must be retained

Historical recordings and voicemails do not automatically migrate to LC Phone. Export and save any critical assets from your Twilio account before migration.

Checklist Item

Review the number's A2P or Toll-Free registration status

Check whether the number has active A2P 10DLC or Toll-Free Verification in Twilio. You may need to re-register or verify the number in HighLevel after migration.

Checklist Item

Note existing call-forwarding or routing behavior

Document how the number currently routes calls and SMS so you can replicate this configuration in LC Phone.

Checklist Item

Identify workflows or integrations that reference the phone number

Check HighLevel workflows, third-party integrations, and automations that may use the phone number. Update these configurations after migration if needed.

Checklist Item

Choose a preferred low-traffic cutover window

Include a preferred migration time in your HighLevel Support request to minimize impact on calling and messaging.

Note

For non-US numbers, use the [international number migration guide](<https://help.gohighlevel.com>).

5

## How to Move a US Number from Twilio to LC Phone

HighLevel Support coordinates the migration end-to-end after you provide the required identifiers and cutover preferences.

Step 1

Locate the Twilio Account SID currently holding the phone number

Find the losing Twilio Account SID in your Twilio console. This identifier is required to initiate the migration.

Step 2

Locate the destination HighLevel Sub-account ID (Location ID)

Identify the HighLevel Sub-account ID where the phone number will reside after migration.

Step 3

Open a HighLevel Support ticket

Submit a support request through the HighLevel Help Center. Include the following information:

  * Phone number(s) you want to migrate (preferably in E.164 format, e.g., +1XXXXXXXXXX)
  * Losing Twilio Account SID
  * Destination HighLevel Sub-account ID (Location ID)
  * Preferred cutover window (date and time)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080012571/original/9msPvePhifZRdTEUw-p_1ZB6VnKoUNMq7g.gif?1788439990)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080012762/original/IaQIz83Oq1zjqTRdKU2P-S11rwKujtRWYg.png?1788440069)


Step 4

HighLevel Support coordinates the migration and confirms when the number is live

HighLevel Support processes the migration request and notifies you when the phone number has been successfully moved to LC Phone.

Step 5

Test inbound and outbound calling and SMS after completion

Verify that the phone number is functioning correctly in LC Phone by testing calls and messages.

  


Migration Timing

Migration timing depends on receiving all required information and the scheduled cutover. HighLevel Support will confirm the migration window once the request is ready to process.

6

## Verify the Number After Migration

Testing the number immediately after cutover confirms that voice, SMS, routing, and messaging registration are working correctly in LC Phone.

Verification Step

Confirm the number appears in the correct HighLevel sub-account

Check the phone numbers list in the destination sub-account to verify the number has been added.

Verification Step

Place an outbound call

Make a test call from the migrated number to confirm outbound calling works.

Verification Step

Place an inbound call

Call the migrated number from an external phone to verify inbound calling routes correctly.

Verification Step

Send an outbound SMS

Send a test message from the migrated number to confirm outbound SMS works.

Verification Step

Send an inbound SMS

Send a message to the migrated number from an external phone to verify inbound SMS routing.

Verification Step

Verify call forwarding or routing

Confirm that call forwarding and routing rules match your intended configuration.

Verification Step

Verify the number assignment to the correct user or team

Check that the number is assigned to the correct user or team in HighLevel.

Verification Step

Confirm A2P Campaign association for applicable local numbers

For US local numbers, verify that the number is attached to an approved A2P Campaign in HighLevel's Trust Center before resuming A2P messaging.

Verification Step

Confirm Toll-Free Verification for applicable toll-free numbers

For toll-free numbers, confirm the Toll-Free Verification status before resuming messaging. Verification status should not be assumed to transfer automatically.

Verification Step

Review workflows and integrations that use the number

Check HighLevel workflows and third-party integrations to confirm they reference the correct phone number after migration.

Post-Migration Success

Once all verification steps are complete, the phone number is ready for production use in LC Phone.

7

## Related Articles

  * [Moving Phone Numbers: Migration Guide](<https://help.gohighlevel.com/en/support/solutions/articles/155000006369>)
  * [Moving Phone Numbers Across Accounts (US and International)](<https://help.gohighlevel.com/en/support/solutions/articles/48001240107>)
  * [Migrating International Numbers from Twilio to LC Phone](<https://help.gohighlevel.com/en/support/solutions/articles/48001240108>)
  * [How Do I Migrate My Agency and Sub-Account to LC Phone?](<https://help.gohighlevel.com/en/support/solutions/articles/48001204027>)
  * [A2P Campaign Registration: Step-by-Step Guide and FAQs](<https://help.gohighlevel.com/en/support/solutions/articles/155000002380>)
  * [Moving Numbers Between Sub-Accounts (Same Agency)](<https://help.gohighlevel.com/en/support/solutions/articles/48001203968>)


8

## Frequently Asked Questions

Q: Will my existing A2P registration move from Twilio to LC Phone?

Not automatically. A2P registration from your own Twilio account may need to be completed again through HighLevel after moving to LC Phone. Confirm that each applicable phone number is attached to the correct approved Campaign before resuming A2P messaging.

Q: Will Toll-Free Verification transfer with my number?

Do not assume it will transfer automatically. Confirm the verification status after migration before resuming messaging.

Q: Will calling or SMS be interrupted during the migration?

A brief interruption may occur during the cutover. Include a preferred low-traffic migration window in your HighLevel Support request and test inbound and outbound calls and SMS as soon as the migration is confirmed complete.

Q: What if I need to reverse the migration?

Reply to the existing HighLevel Support ticket immediately. Rollback feasibility depends on the migration stage, carrier, and timing.

Q: Do I need to contact Twilio Support to migrate my number?

No. HighLevel Support coordinates migrations end-to-end. You only need to provide the losing Twilio Account SID, destination HighLevel Sub-account ID, and phone numbers in your HighLevel Support request.

Q: Will my historical Twilio call recordings and voicemails migrate to LC Phone?

No. Historical recordings and voicemails do not automatically migrate. Download and save any critical assets from your Twilio account before migration.

Q: How long does a phone number migration take?

Migration timing depends on receiving all required information and the scheduled cutover. HighLevel Support will confirm the migration window once the request is ready to process.

Q: Can I migrate international phone numbers using this process?

No. This guide applies to US local and toll-free numbers only. For non-US numbers, use the international number migration guide.

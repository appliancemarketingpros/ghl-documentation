# How do I migrate my agency and sub-account over to LC Phone?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001204027-how-do-i-migrate-my-agency-and-sub-account-over-to-lc-phone-](https://help.gohighlevel.com/support/solutions/articles/48001204027-how-do-i-migrate-my-agency-and-sub-account-over-to-lc-phone-)  
**Category:** Phone System  
**Folder:** LC Phone System

---

Phone System Migration

How to Migrate an Agency and Sub-Account to LC Phone

Move your agency off a third-party telephony provider and onto the built-in LeadConnector Phone system, then bring your existing sub-accounts along.

Overview

LC Phone removes the need to integrate a third-party telephony provider (Twilio, Plivo, etc.) in order to send or receive SMS/calls in the CRM. With LC Phone, sending and receiving SMS/calls works right out of the box.

LC Phone is now available to every agency, there's no separate access request or validation step before you begin. Read more about it [here](<https://help.gohighlevel.com/support/solutions/articles/48001223546>).

Table of Contents

1

Why LC Phone?

2

Step 1 — Switch Your Agency to LC Phone

3

Step 2 — Move Existing Sub-Accounts to LC Phone

4

Frequently Asked Questions

1

## Why LC Phone?

Moving to LC Phone gives you:

  * A one-click quick start — no separate Twilio/Plivo account to configure.
  * Better, real-time billing.
  * Increased security and a better message delivery rate.


Good to Know

Once your agency is connected to LC Phone, **Automatically Link Phone System** is enabled by default for newly created sub-accounts.

Agencies can change this preference under:   
**Settings → Phone Integration → Account Creation**.

Existing sub-accounts are not migrated automatically, you'll link the existing sub-accounts you want to migrate using Step 2 below.

2

## Step 1 — Switch Your Agency to LC Phone

Before you can move any sub-accounts, your agency itself needs to be switched over to the LeadConnector phone system.

Where to Go

Go to **Settings → Phone Integration → Agency Settings** tab and click **Switch to LeadConnector Phone System**.

Important — A2P Registration Must Be Completed Again

A2P 10DLC registration from your own Twilio account does not migrate to LC Phone. If an affected sub-account was previously registered for A2P through your Twilio account, it must complete A2P registration again through the HighLevel Trust Center after moving to LC Phone, and the applicable registration fees will apply again.

Once the new A2P registration is approved, confirm that each applicable phone number is attached to the approved campaign before resuming A2P messaging.

Connected

Once confirmed, your agency is on LC Phone, the Agency Settings tab now shows a "Connected to LeadConnector" summary with usage insights. All new sub-accounts created from this point forward are automatically on LC Phone.

Move your existing sub-accounts over with Step 2.

3

## Step 2 — Move Existing Sub-Accounts to LC Phone

From the agency level, go to **Settings → Phone Integration → Sub Account Settings** tab. This table lists every sub-account and its current phone-system status under **Managed By**.

Step A

Find the sub-account

Use the **Search sub-accounts by...** box to find the sub-account by name. A sub-account not yet on LC Phone shows **Not available** under Managed By.

Step B

Open the row menu

Click the ⋮ (three-dot) icon at the right-hand end of that sub-account's row.

Step C

Link to LeadConnector

Select **Link to LeadConnector** from the menu, review the confirmation prompt, and confirm to kick off the migration.

![The Sub Account Settings table, showing the row-level menu used to link a sub-account](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079669088/original/LfZxqCKyMbETER0cpmdmdV3a338QQiCC4Q.png?1788163543)

The Sub Account Settings table, showing the row-level menu used to link a sub-account.

You don't need to do anything else during this phase — the old sub-account keeps working normally on its existing provider while the migration processes in the background. Once the phone numbers have moved, the sub-account switches over automatically and **Managed By** updates to a green ✓ LC Phone badge.

![Phone Integration Sub Account Settings table view](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079669235/original/YPyoqVNQrKPo5KGpi_56yyEBpmCe3r0n2g.png?1788163616)

Phone Integration → Sub Account Settings, showing each sub-account's phone-system status under Managed By.

Tip

Sub-accounts are linked one at a time from this table. If you're moving a large number of them, use **Export** above the table to get a full list first, then work through it and track which ones show the LC Phone badge.

US/Canada Sub-Accounts

A Regulatory Bundle is not required for US or Canadian phone numbers. Select **Link to LeadConnector** to begin the migration.

The existing phone service remains active while the migration is processing. Once migration is complete, **Managed By** will update to ✓ LC Phone.

**Important:** If the sub-account uses A2P 10DLC, A2P registration from the previous Twilio account does not migrate and must be completed again under LC Phone.

Migration processing time can vary. If the migration remains pending beyond the expected processing window, contact HighLevel Support.

Non-US/Canada Sub-Accounts

Depending on the country and number type, you may need an approved Regulatory Bundle and Address before the number can be migrated.

In the sub-account, go to: **Settings → Phone System → Regulatory Bundles**.

Create and submit the required Address and Regulatory Bundle. Once approved, return to **Agency Settings → Phone Integration → Sub Account Settings** and follow Step 2 to continue the migration. Migration time can vary depending on the country, number type, and regulatory requirements.

Historical Recordings and Voicemails

Historical call recordings and voicemails are not transferred to LC Phone during migration. They remain associated with the previous Twilio account. Download any historical recordings or voicemail assets you need to retain before closing the Twilio account or losing access to it.

After the Migration

Once **Managed By** shows ✓ LC Phone:

  * Confirm all expected phone numbers are present in the sub-account.
  * Complete A2P registration again for applicable US local numbers that previously used A2P through the old Twilio account.
  * Once A2P is approved, confirm the applicable phone numbers are attached to the approved campaign.
  * Verify any required Toll-Free or country-specific compliance status.
  * Test one inbound and outbound voice call.
  * Test inbound and outbound SMS where applicable.
  * Confirm phone routing and number assignments are configured as expected.


4

## Frequently Asked Questions

Q: What are the benefits of moving to the LC Phone system?

One-click quick start, better cost with real-time billing, and increased security with a better delivery rate.

Q: What happens to existing sub-accounts when the agency onboards onto LC Phone?

Existing sub-accounts are not moved automatically when the agency switches. You'll link the existing sub-accounts you want to migrate individually using the **Link to LeadConnector** flow in Step 2.

Q: In which countries is LC Phone available?

LC Phone is available for all countries. Regulatory bundles are supported — [learn more here](<https://help.gohighlevel.com/support/solutions/articles/48001213216>).

Q: Will SaaS re-billing work if I move sub-accounts to LC Phone?

Yes — SaaS rebilling continues to work with the LC Phone system.

Q: What are the costs of LC Phone vs. Twilio?

LC Phone pricing follows Twilio's underlying rates. Actual charges vary by country, service, carrier fees, and applicable HighLevel discounts. Refer to the current [Phone System Pricing & Billing Guide](<https://help.gohighlevel.com/support/solutions/articles/48001223556>) for the latest pricing.

Q: Where can I see my sub-account phone usage?

Export all sub-account phone usage from **Agency Settings → Billing → See Details** (under Credits). The **Phone Integration → Agency Settings** tab also shows a live Insights & Usage summary once you're connected to LeadConnector. Inside a sub-account, check **Settings → Phone Numbers → Usage Summary**.

Q: If I switch to LC Phone, does it apply to one sub-account or all of them?

Existing sub-accounts are not migrated automatically. You choose which existing sub-accounts to migrate using **Phone Integration → Sub Account Settings**.  
  
For newly created sub-accounts, **Automatically Link Phone System** is enabled by default. Agencies can change this preference under: **Settings → Phone Integration → Account Creation**.  
  
If an existing LC Phone sub-account needs to move to its own Twilio account, follow the supported LC Phone → Twilio migration process.

Q: If I switch to LeadConnector and need an international number, how do I proceed?

Set up a Regulatory Bundle from the sub-account's Phone Numbers tab — see [Regulatory Bundle and Address Creation for Sub-Accounts](<https://help.gohighlevel.com/en/support/solutions/articles/48001213216>). Once the bundle is set up, the number can be moved to LC Phone.

Q: Can specific sub-accounts continue using their own Twilio account?

Yes. An individual sub-account can use its own Twilio account instead of LC Phone. If the location is already using LC Phone and has phone numbers that must be retained, complete the supported [LC Phone → Twilio number migration](<https://help.gohighlevel.com/support/solutions/articles/48001240107>) before disabling the LC Phone connection.

Q: My Twilio account is currently suspended — can I still move to LeadConnector?

No — you'll need to resolve the suspension with Twilio support first before migrating. See [Why is your account suspended](<https://help.gohighlevel.com/en/support/solutions/articles/48001207676>).

Q: Will call recordings be lost when a sub-account switches from Twilio to LC Phone?

Recordings don't transfer over automatically, but they remain archived in the sub-account's existing Twilio account and can be downloaded manually for safekeeping.

Q: How do I know a sub-account finished migrating?

Check the Managed By column on the Sub Account Settings table — it switches from Not available to a green ✓ LC Phone badge once the linked numbers have finished moving over. The row's ⋮ menu also changes from Link to LeadConnector to SMS Compliance / Delete Connection.

Q: Do I still need to "validate" LC Phone access before starting?

No. LC Phone is available to all agencies by default now, so there's nothing to validate — go straight to Step 1 above.

Related Articles

What is LC Phone System? [Regulatory Bundle and Address Creation for Sub-Accounts](<https://help.gohighlevel.com/en/support/solutions/articles/48001213216>) Toll-Free Number Registration for LC Phone (US/Canada) LC Phone Messaging Policy LC Phone Pricing Structure

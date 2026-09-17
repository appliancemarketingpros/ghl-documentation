# HighLevel API Migration Guide: How to Move to Private Integrations

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008488-highlevel-api-migration-guide-how-to-move-to-private-integrations](https://help.gohighlevel.com/support/solutions/articles/155000008488-highlevel-api-migration-guide-how-to-move-to-private-integrations)  
**Category:** Developer Resources  
**Folder:** Developer Resources

---

**This simple, step-by-step guide will help you transition your connected apps (like Zapier, Make, or custom tools) from old, legacy API keys to HighLevel’s new, secure****Private Integration Tokens****.**

HighLevel API v1 reached end-of-support on December 31, 2025. Existing v1 integrations may continue to work, but they are no longer maintained or supported.

HighLevel directs users of legacy API keys to migrate to Private Integrations, which provide scoped access through Private Integration Tokens (PITs)

### Critical rule before starting

Do NOT update or edit your existing, active automations. Doing so might break your current setups. Instead, you will:

  * Keep your existing automations running.

  * Create brand-new automations alongside them using the new APIs.

  * Test the new ones.

  * Delete the old automations and your old API key only after everything works perfectly.


## Step-by-Step Migration Guide

Unlike v1 API keys, which provide broad access to account data, Private Integrations allow you to select the specific scopes and permissions an integration can access. Private Integrations can be created at both the Agency and Sub-Account level.

### Step 1: Check where you are using your old API key

Identify which third-party tools or automations are currently using your legacy HighLevel API key.

  * Make a list of these tools (e.g., Zapier, Make, n8n, custom web forms, etc.).

  * Identify what they do (e.g., "Zapier: Adds new leads to HighLevel from Facebook").


### Step 2: Create a "Private Integration" in HighLevel

Private Integrations are the safe replacement for old API keys. Instead of giving a tool access to your entire account, you can choose exactly what it is allowed to see.

  * Important: Create a separate Private Integration for each tool you connect (e.g., one for Zapier, one for Make, one for n8n). Do not share one token across multiple tools.


How to create it:

  1. Log into HighLevel.

  2. Go to Settings and look for Private Integrations (available at both the Agency and Sub-Account levels).

  3. Click Create Private Integration.

  4. Give it a clear name (like "Zapier Lead Sync") and description.

  5. Select Scopes: Choose only the specific permissions that specific tool needs (e.g., if Zapier only reads contacts, check only the "Contacts" permission).

  6. Click Save to generate your Private Integration Token.

  7. CRITICAL: Copy and save this token somewhere secure immediately. HighLevel will only show this token once, and you cannot view it again later.


### Step 3: Build NEW automations in your external tools

Instead of editing your live, existing automations, you must create new ones.

  1. Open your automation tool (like Zapier or Make).

  2. Create a brand-new automation (or duplicate your existing one to keep it as a backup).

  3. In this new automation, connect your HighLevel account using the new Private Integration Token you copied in Step 2.

     1. Note: If the tool asks for authentication headers, the token is sent as: Authorization: Bearer <YOUR_NEW_TOKEN>.

  4. Build the steps of your automation using the current, modern HighLevel API endpoints. (If you are using built-in app integrations like Zapier's HighLevel app, ensure you select the latest actions and versions available).

     1. Latest API Documentation URL: https://marketplace.gohighlevel.com/docs/


### Step 4: Test your brand-new automations

Before making the switch, test the new setup to ensure it runs correctly.

  * Run a test lead or action through your new automation.

  * Check HighLevel to make sure the data arrived correctly.

  * Verify that your selected permissions (scopes) in Step 2 were sufficient.


### Step 5: Turn off the old and delete the old keys

Once your new automations are working perfectly:

  5. Turn on your brand-new automations to make them live.

  6. Turn off or pause your old, legacy automations.

  7. Remove and delete the old, legacy API key from your external tools and HighLevel settings. This ensures your account remains secure and that no old processes run in the background.


## Maintenance and Best Practices

  * Rotate your tokens: HighLevel recommends generating a new token (rotating) every 90 days for maximum security.

  * Grace Period: When rotating tokens, HighLevel keeps both the old and new tokens active for 7 days so you have plenty of time to copy the new token into your tools without any service interruption.

  * Do not assume the migration is only an authentication change. API requests and responses may differ between the legacy and current APIs.

  * HighLevel's current APIs use the Version request header, and newer APIs may use named versions such as v3. Use the version specified by the documentation for the endpoint you are implementing.

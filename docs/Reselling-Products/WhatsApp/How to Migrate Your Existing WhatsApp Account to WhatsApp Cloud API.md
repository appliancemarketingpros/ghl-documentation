# How to Migrate Your Existing WhatsApp Account to WhatsApp Cloud API

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007590-how-to-migrate-your-existing-whatsapp-account-to-whatsapp-cloud-api](https://help.gohighlevel.com/support/solutions/articles/155000007590-how-to-migrate-your-existing-whatsapp-account-to-whatsapp-cloud-api)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# How to Migrate Your Existing WhatsApp Account to WhatsApp Cloud API

If you're using CRM and want to connect your existing WhatsApp business number to WhatsApp Cloud API, you first need to migrate that number. This is a required step — you can't simply add a number that's already registered on WhatsApp (personal or business app) to the Cloud API without disconnecting it first.

**Needs validation from Meta documentation:** This guide describes the standard migration path, where the number is fully removed from the WhatsApp or WhatsApp Business app before it can run on the Cloud API. Meta's WhatsApp Coexistence feature now offers an alternative for eligible accounts: it lets the same number run on both the WhatsApp Business App and the Cloud API at once, without deleting the app account, through a separate onboarding flow. If you want to keep using the number on your phone, check whether Coexistence is available in your region and for your number before following the delete-and-migrate steps below.

## Why Migration Is Necessary

When you try to add a phone number that's already active on WhatsApp to the Cloud API (via Meta's Business Manager or CRM's WhatsApp integration), you'll see an error like this:
    
    
    "This number is registered to an existing WhatsApp account. To use this number, disconnect it from the existing account. Then, return to this page and re-enter the number. Note: It may take up to 3 minutes for the number to become available."

This happens because WhatsApp doesn't allow a number to be active on two platforms at once through the standard connection path. You need to delete or unlink the number from the standard WhatsApp or WhatsApp Business app before it can be used with the Cloud API inside CRM. In practice, if the number was previously linked to a WhatsApp Business API account through another provider, Meta may require a longer cooldown of several weeks rather than a few minutes before it's eligible again.

## What You'll Lose (and What You Won't)

Before you migrate, keep this in mind:

**Your phone number** stays the same**Your business profile** can be recreated on the Cloud API| **Your chat history** will not transfer — it stays on the old device/appThe number will be **temporarily unavailable** (usually up to 3 minutes) during the switch  
---|---  
  
## Step-by-Step: How to Migrate Your Number

1| Back Up Your Chat History (Optional)If you want to keep a local copy of your conversations before disconnecting:

  * **WhatsApp:** Go to Settings → Chats → Chat Backup and back up to Google Drive or iCloud.
  * **WhatsApp Business:** Same path — Settings → Chats → Chat Backup.

This is optional since the backup won't transfer to the Cloud API, but it's good practice.  
---|---  
2| Delete Your WhatsApp Account (or Unlink the Number)You need to remove the number from the existing WhatsApp or WhatsApp Business app.On WhatsApp (Personal):

  1. Open WhatsApp on your phone.
  2. Go to Settings → Account → Delete Account.
  3. Select your country code and enter your phone number.
  4. Tap Delete My Account.

On WhatsApp Business App:

  1. Open WhatsApp Business.
  2. Go to Settings → Account → Delete Account.
  3. Enter your number and confirm.

This deletes your WhatsApp account tied to that number — not your phone number itself. Your SIM and number are unaffected.  
---|---  
3| Wait Up to 3 MinutesAfter deleting, Meta's system takes a short time to release the number. Wait 2–3 minutes before proceeding.  
---|---  
4| Add the Number in CRMNow head into CRM and connect your WhatsApp number via the Cloud API:

  1. In your CRM sub-account, go to Settings → Integrations → WhatsApp.
  2. Click Connect WhatsApp.
  3. Follow the Meta Business Manager flow (you'll be asked to log into Facebook and select or create a Meta Business account).
  4. When prompted to add a phone number, enter the number you just freed up.
  5. Verify it via OTP (SMS or call).

If it still shows the "number is registered" error, wait another 2–3 minutes and try again.  
---|---  
5| Set Up Your WhatsApp Business Profile in CRMOnce connected, configure your business profile:

  * **Business Display Name** — the name customers will see
  * **Category** — choose the closest match to your business type
  * **Profile photo and description**

This information is managed through Meta's Business Manager but will reflect inside CRM's conversations.  
---|---  
6| Start Automating in CRMWith the Cloud API connected, you now unlock the full power of WhatsApp inside CRM:

  * **Bulk messaging** — send campaigns to your contact lists via WhatsApp
  * **Workflow automations** — trigger WhatsApp messages based on pipeline stage, form submissions, appointments, and more
  * **Two-way conversations** — manage replies in the CRM Conversations inbox
  * **WhatsApp templates** — create and send pre-approved message templates for outbound outreach
  * **CRM integration** — all WhatsApp activity logs against your contacts automatically

  
---|---  
  
## Common Issues & Fixes

Problem| Fix  
---|---  
"Number is already registered" error| Wait 3–5 minutes after deleting the account and try again  
OTP not received| Make sure the number can receive SMS or calls; try the call option  
Number shows as pending in Meta Business Manager| Verify your Meta Business account is approved and your phone number is added correctly  
WhatsApp messages not showing in CRM| Check that the webhook is properly configured under your CRM WhatsApp settings  
  
## Final Tips

  * Use a dedicated business number for your Cloud API connection — avoid using your personal WhatsApp number.
  * If you're managing multiple client sub-accounts in CRM, each sub-account needs its own unique phone number.
  * Once on Cloud API through this standard path, you cannot use that number on the regular WhatsApp or WhatsApp Business app simultaneously — unless your account is eligible for Coexistence.


Migrating your number is a one-time step, and once it's done, you have the full flexibility of the WhatsApp Cloud API working seamlessly inside CRM — automations, campaigns, CRM data, and two-way messaging all in one place.

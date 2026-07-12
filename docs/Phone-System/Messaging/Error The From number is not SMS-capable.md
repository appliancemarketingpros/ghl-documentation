# Error: The "From" number is not SMS-capable.

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001180919-error-the-from-number-is-not-sms-capable-](https://help.gohighlevel.com/support/solutions/articles/48001180919-error-the-from-number-is-not-sms-capable-)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Troubleshooting

Error: The "From" number is not SMS-capable.

Why this error happens and how to fix it — capability, ownership, A2P (US), and formatting.

Overview

Seeing **"The From phone number is not SMS-capable phone number"**? This guide explains why it happens and how to fix it — covering capability, ownership, A2P (US), and formatting.

Table of Contents

1

What Is the Error

2

Quick Fix Checklist

3

Common Causes & How to Resolve

4

Special Cases

5

Frequently Asked Questions

1

## What Is the Error: The "From" number is not SMS-capable.

This error appears when an outbound SMS/MMS is attempted from a number that isn't eligible to send SMS for the selected destination, account, or configuration. The most common root causes are: the number isn't SMS-capable, it's not on your account/location, it's not linked to an approved A2P campaign (US 10DLC), or the From value is misconfigured (e.g., invalid format or incompatible sender type).

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075494305/original/UkLpydj_v9oxn28YO5WuT9nac8VJt9vLNw.png?1783504951)

2

## Quick Fix Checklist

  * Verify the **From number** belongs to this sub-account/location and is SMS-capable.
  * Use E.164 format in the From field (e.g., +15551234567).
  * For **US 10DLC** , make sure the number is attached to an approved A2P campaign (Messaging Service → attached numbers).
  * If using a Short Code, the To and From must be in the **same country**.
  * If using an Alphanumeric Sender ID, confirm the destination country supports it.
  * If you manage numbers in **Twilio Console** , ensure the number is capable and owned by your account (not another Master account).


Tip

If this error started after a recent move or configuration change, re-check number ownership (agency vs. sub-account), campaign assignments, and any Messaging Service changes.

3

## Common Causes & How to Resolve

Cause 1

Phone Number Is Not SMS-Capable

Some phone numbers are voice-only or don't support SMS in certain countries.

  * **LC Phone:** Go to **Settings → Phone Numbers** , open the number, and confirm **Messaging** is enabled.
  * **Twilio:** In Console, open the number and verify that **Capabilities** include **SMS**.
  * **Fix:** Use an SMS-capable number or purchase/assign one that supports messaging.


![Confirming SMS capability on a phone number](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055133988/original/b9UogWLOJbT-yTuqQM8pRVkWLbH9JhLXhQ.png?1759442856)

Tip

For using the Phone Number Assignment feature, refer to: [How to use this phone assignment feature for SMS/Voice capable only](<https://www.loom.com/share/075fefb6c4a345529aa761a3af973a1d?sid=651ce97b-2ecf-4e64-8818-bfa7312ee7cb>).

Cause 2

The Number Isn't Valid for Your Account/Destination

The **From** must be a number **owned by (or hosted to)** your account and valid for the target country.

  * **Short Codes:** Must be in the **same country** as the destination.
  * **Hosted/Trial/other account numbers:** Not valid until fully owned and SMS-enabled on your account.
  * **Fix:** Send from a number on your account that's allowed for the destination.


Cause 3

A2P 10DLC (US) Configuration Missing or Wrong

US local 10DLC numbers must be tied to an **approved A2P campaign**.

  * **LC Phone:** Confirm the number is linked to your approved **Brand/Campaign**.
  * **Twilio:** Attach the number to the correct **Messaging Service** that's tied to the approved campaign.
  * **Fix:** Complete A2P registration and link the number; retry after approval.


Cause 4

Formatting or Sender Type Issues

  * **E.164 required:** Use `+` and country code.
  * **Alphanumeric Sender ID:** Only supported in specific countries (not US/CA person-to-person).
  * **Fix:** Correct the **From** format or choose a supported sender type for the destination.


Cause 5

Number Recently Moved or Not in This Location

If the number was **moved between sub-accounts** or providers, the **From** selector or automations may still reference the old number.

**Fix:** Re-select the active number in **Conversations** , **Campaigns/Workflows** , and **Messaging settings**.

4

## Special Cases

  * **Toll-Free (US/CA):** Requires **Toll-Free Verification** for reliable delivery. If unverified, messages may fail or be filtered.
  * **International:** Some countries block A2P from long codes; use **Alphanumeric Sender ID** (if supported) or an approved sender per country rules.
  * **Different Master Twilio account:** If your number lives under a different **Master** account, it isn't valid for this account's sends. Move it first or send from a number on this account.


5

## Frequently Asked Questions

Q: Does this error mean the number is suspended?

Not necessarily. It usually means the number cannot send SMS for the current configuration. Check capability, ownership, and A2P linking.

Q: Can I send from a short code to another country?

No. Short codes are **country-specific** ; use a local short code for the destination country or another supported sender type.

Q: We just ported/added a number and still see this error — why?

Provisioning or campaign linking can take time. Confirm SMS capability and, for the US, that the number is attached to your approved campaign.

Q: What if I don't see my number in the From dropdown at all?

This usually means the number isn't assigned to the current sub-account/location, or it hasn't finished provisioning. Confirm the number's location assignment under Settings → Phone Numbers.

Q: Does this error affect MMS as well as SMS?

Yes. If a number isn't SMS-capable or isn't valid for the destination, MMS sends from the same number will fail for the same underlying reason.

Q: How long does A2P campaign approval typically take?

Approval timelines vary by carrier and campaign type, and can range from a few hours to several business days. Sends will keep failing with this error until the number is fully linked to an approved campaign.

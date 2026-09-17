# WhatsApp Business API Error #131037 — Display Name Approval Required

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007730-whatsapp-business-api-error-131037-display-name-approval-required](https://help.gohighlevel.com/support/solutions/articles/155000007730-whatsapp-business-api-error-131037-display-name-approval-required)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# WhatsApp Business API Error #131037 — Display Name Approval Required

5 min read

ERROR MESSAGE

`(#131037) WhatsApp provided number needs display name approval before message can be sent`

If you're seeing this error when attempting to send messages through your WhatsApp Business Account (WABA) in CRM, it means your phone number's display name has not yet been approved by Meta. Until approval is granted, the number is unable to send or receive messages through the platform.

**Needs validation from Meta documentation:** Several current sources describe error 131037 as most commonly tied to the free WhatsApp-provided test number (a +1-555 number), and note that Meta no longer requires display name review as a mandatory step to start messaging on a standard, self-supplied Cloud API number. If a client hits this error on their own registered business number, confirm whether it's actually a name-change re-review or BSP migration (as described below) rather than a first-time approval gate, since the underlying cause differs slightly by scenario.

## Why Does This Error Occur?

Every WhatsApp Business phone number must have a Meta-approved display name before it can be activated for messaging. When you register a new number under a WhatsApp Business Account, Meta reviews the display name to verify it complies with WhatsApp's naming and business policies.

**Important:** If your display name is still **Under Review** or has been **Rejected** , all outbound and inbound messaging will be blocked — resulting in error #131037.

This can happen in two common scenarios:

  * **Scenario 1:** You recently added a new phone number to your WABA and the display name is still pending Meta's review.
  * **Scenario 2:** You recently migrated your number to a new Business Solution Provider (BSP), which can trigger a fresh display name review.


## How to Fix This Error

1| Log in to Meta Business ManagerGo to `business.facebook.com` and sign in with the account connected to your WABA.  
---|---  
2| Navigate to Your WhatsApp AccountOpen `Business Settings → Accounts → WhatsApp Accounts`, then select the relevant WABA.  
---|---  
3| Open the Phone Numbers TabLocate the phone number triggering the error. You will see the current Display Name Status — it will show one of: _Pending Review_ , _Approved_ , or _Rejected_.  
---|---  
4| Take Action Based on Your Status| STATUS: PENDING REVIEWNo action needed. Wait for Meta to complete the review — this typically takes **24 to 48 hours**. The error will resolve automatically once approved.| STATUS: REJECTEDClick **Edit Display Name** in Meta Business Manager and resubmit. Ensure the name clearly represents your business and follows WhatsApp's display name guidelines.  
---|---  
5| Wait for or Confirm ApprovalOnce approved, the error resolves automatically and messages will flow normally through CRM.  
---|---  
  
## Display Name Best Practices

When resubmitting a rejected display name, keep [Meta's guidelines](<https://www.facebook.com/business/help/757569725593362>) in mind to avoid another rejection:

  * Use your actual business or brand name — do not use a generic or misleading name.
  * Avoid names that impersonate other businesses or individuals.
  * The display name must align with your registered business identity or website.
  * Do not include URLs, phone numbers, or promotional language in the display name.


**Migrating from another BSP?** If you recently moved your number to CRM from another Business Solution Provider, the display name review may restart under your new Business Manager. Always check the approval status in Meta before attempting to send messages after a migration.

## Quick Reference Summary

Error Code| Root Cause| Resolution  
---|---|---  
`#131037`| Display name is pending review or has been rejected by Meta| Check status in Meta Business Manager → wait for approval or resubmit a compliant display name

# Error 131042 — Business Eligibility Payment Issue

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007938-error-131042-business-eligibility-payment-issue](https://help.gohighlevel.com/support/solutions/articles/155000007938-error-131042-business-eligibility-payment-issue)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

Troubleshooting GuideError 131042 — Business Eligibility Payment IssueUnderstand why WhatsApp messages are blocked with error code 131042, what payment issues trigger it, and how to fix it step by step.  
---  
What you'll learn| + What error 131042 means| + All known causes| + Step-by-step fix| + How to prevent it  
---|---|---|---  
  
* * *

**TABLE OF CONTENTS**

  * What is Error 131042?
  * Known Causes
  * How to Resolve It
  * How to Prevent It
  * Related Error Codes
  * Frequently Asked Questions


* * *

What is Error 131042?Business Eligibility Payment Issue — messages are blocked because of a problem with your payment method or billing setup in Meta  
---  
  
Error **131042** is a WhatsApp Cloud API error officially titled **"Business Eligibility Payment Issue"**. It occurs when WhatsApp cannot find a valid payment method to cover the conversation-based fees for your account. Until the payment issue is resolved, **outgoing messages will be completely blocked**.

This is what the error looks like in the API response:
    
    
    "errors": [
      {
        "code": 131042,
        "title": "Business Eligibility Payment Issue",
        "details": "Message failed to send because there are restrictions on how many messages can be sent from this phone number."
      }
    ]
    
    
    **Important:** This error is related to your **Meta WhatsApp Business Account billing** — not your CRM subscription. Even if your CRM account is active and paid, you still need a separate valid payment method set up inside Meta Business Manager to cover WhatsApp API conversation fees.

* * *

Known CausesAll officially documented reasons for this error from Meta's documentation  
---  
  
According to Meta's official documentation, error 131042 occurs when **one or more** of the following conditions are present:

1\. No payment method linked to the WhatsApp Business AccountA payment account has not been attached to your WhatsApp Business Account (WABA). This is the most common cause. Note that adding a payment method to your Meta Business Suite does not automatically link it to your specific WABA — it must be explicitly assigned.  
---  
2\. Credit limit exceededYour payment account has reached or exceeded its credit limit. WhatsApp blocks outgoing messages when the account cannot be charged for new conversations.  
---  
3\. Credit line is inactive or not setThe credit line for the payment account is either inactive or has not been configured. This can happen when a payment method was added but not properly activated for WhatsApp billing.  
---  
4\. WhatsApp Business Account is deleted or suspendedIf the WhatsApp Business Account linked to your phone number has been deleted or suspended by Meta — due to a policy violation or inactivity — messages cannot be sent.  
---  
5\. Timezone or currency settings are missing or incorrectly setMeta requires the timezone and currency to be correctly configured in your WhatsApp Business Account settings. Incorrect or missing settings can block message sending even if a payment method is present.  
---  
6\. MessagingFor request pending or declinedIf you are sending messages on behalf of another business (as a tech provider or agency), and the MessagingFor request has not been approved or has been declined, messages will be blocked.  
---  
7\. Free conversation tier exceeded without a valid payment methodWhatsApp provides 1,000 free service conversations per month. Once this limit is reached, a valid payment method must be on file. If no payment method is added, all new conversations beyond the free tier will be blocked.  
---  
8\. Tax information not specified in Meta Business ManagerThis is a commonly overlooked cause. Meta requires tax information to be added in the Business Manager for billing to work properly. Even if a valid payment method is linked, missing tax details can trigger error 131042.  
---  
9\. Outstanding payment duesA previous billing cycle charge failed — for example, because the card expired or had insufficient funds — and there are unpaid dues on the account. Meta blocks further message sending until all outstanding charges are cleared.  
---  
  
* * *

How to Resolve ItWork through these steps in order to identify and fix the payment issue  
---  
  
Step 1 **Check that a payment method is linked to your WhatsApp Business Account**

Log in to **business.facebook.com** and navigate to your WhatsApp Business Account settings.

| 1 Go to **Meta Business Suite** > **Settings** > **Billing & Payments**  
---  
| 2 Click **Accounts** > **WhatsApp Business Accounts**  
---  
|  3 Find the WABA that is showing the error and click the **three dots (...)** > **View Details**  
---  
|  4 If no payment method is shown, click **Add Payment Method** and complete both setup steps  
---  
      
    
    Adding a payment method to Meta Business Suite is not the same as linking it to your WABA. You must complete both steps: add the card **and** assign it to the specific WhatsApp Business Account.

Step 2 **Check for outstanding payment dues and clear them**

In the same Billing & Payments section, check whether there are any failed or pending charges on your account. If there are outstanding dues, pay them to unblock your account. Common reasons for failed charges include:

| \- Expired credit or debit card  
\- Card declined due to insufficient funds  
\- Bank blocked an international or recurring charge from Meta  
\- A small verification charge ($1) from Meta failed at card setup  
---  
  
Step 3 **Verify the credit limit has not been exceeded**

In the Billing & Payments section, check your credit line status. If the limit has been reached, update your payment method to a card with a higher limit, or request a credit line increase from Meta. Once the credit line is cleared, message sending will resume.

Step 4 **Check and correct your timezone and currency settings**

In your WhatsApp Business Account settings in Meta Business Suite, verify that **timezone** and **currency** are correctly set for your region. Incorrect or missing settings can block billing even when a valid payment method is present. Note that once set, timezone and currency cannot always be changed — contact Meta Support if you need to correct them.

Step 5 **Add your tax information to Meta Business Manager**

This is one of the most commonly overlooked fixes. Even with a valid payment method, missing tax details can trigger error 131042.

| 1 Go to **Meta Business Manager** > **Settings** > **Business Info**  
---  
|  2 Scroll down to the **Tax Information** section  
---  
| 3 Enter your tax ID or GST/VAT number as required for your country  
---  
| 4 Save and retry sending a message to test if the error is resolved  
---  
  
Step 6 **Verify your WhatsApp Business Account is active and not suspended**

Log in to **Meta Business Suite** and check the status of your WhatsApp Business Account. If it shows as restricted, disabled, or suspended, review Meta's policy enforcement notification and follow the steps provided to appeal or restore access. A suspended WABA will block all messaging regardless of payment method.

Step 7 **Contact support if the error persists after all steps above**

If you have completed all the steps above and messages are still failing, contact our support team with the following information:

  * Your WhatsApp Business Account (WABA) ID
  * The phone number ID affected
  * A screenshot of your current Billing & Payments status in Meta Business Suite
  * The full API error response including any `fbtrace_id` values
  * Confirmation of which steps above you have already completed

  
---  
  
* * *

How to Prevent ItBest practices to keep your billing setup healthy and avoid disruption  
---  
| **Add a valid payment method before you start sending** — set up billing in Meta Business Suite before going live. Do not wait until messages start failing  
---  
| **Use a credit card rather than a debit card** — Meta strongly prefers credit cards for recurring API billing. Debit cards with international restrictions frequently fail at billing time  
---  
| **Monitor your billing status in Meta Business Manager regularly** — check for failed payments, low credit, or billing warnings before they become a problem  
---  
| **Keep your card details up to date** — update your payment method before your card expires to avoid failed billing cycles  
---  
| **Complete your tax information during initial setup** — add your tax ID or VAT number in Meta Business Manager when you first set up your account, not after errors appear  
---  
| **Enable billing notifications in Meta Business Suite** — turn on email alerts for payment failures and billing threshold warnings so you are notified before messages stop sending  
---  
  
* * *

Related Error CodesOther account and billing errors you may encounter  
---  
Error Code| Title| Description  
---|---|---  
131031| Account Locked| Your WABA has been restricted or disabled for violating a platform policy. Review Meta's policy enforcement guidance.  
130497| Country Messaging Restricted| Your WABA is restricted from messaging users in certain countries. Complete a scaling path to unlock cross-country messaging.  
131026| Message Undeliverable| Message could not be delivered — can be caused by invalid number, blocked contact, or frequency capping.  
131048| Spam Rate Limit Hit| Too many users have marked your messages as spam. Your quality rating has dropped and messaging is restricted.  
  
* * *

Frequently Asked QuestionsCommon questions about error 131042  
---  
Q: My CRM subscription is active and paid — why am I still getting this error?Error 131042 is not related to your CRM subscription. It is triggered by a payment issue on your **Meta WhatsApp Business Account**. Your CRM billing and Meta's WhatsApp API billing are completely separate. You need a valid payment method set up inside Meta Business Manager specifically for WhatsApp API usage.  
---  
Q: How quickly does the error resolve after I add a payment method?In most cases, the error clears **immediately** once a valid payment method is correctly linked and all dues are cleared. In some cases, it may take up to 24 hours for Meta's eligibility status to refresh. If it has not resolved after 24 hours, contact support.  
---  
Q: I have added my card but the error is still appearing — what could I be missing?The most commonly missed fix is **tax information**. Even if your card is correctly linked, missing tax details in Meta Business Manager can cause this error to persist. Check your Business Info settings and ensure your Tax ID or VAT number has been entered. Also confirm the card is not experiencing a verification hold — check your bank statement for a small pending charge from Meta.  
---  
Q: Does this error affect all message types or only specific ones?Error 131042 blocks **all outgoing messages** that require billing — which includes Marketing, Utility, and Authentication template messages, as well as any conversation that falls outside the free tier. The 1,000 free service conversations per month are not affected unless you have also hit the free tier limit without a payment method on file.  
---  
Q: Can I use a debit card instead of a credit card?Meta accepts some debit cards, but **credit cards have a significantly higher success rate** for WhatsApp API billing. Debit cards that block international or recurring transactions will fail at billing time and trigger error 131042. If you are using a debit card and experiencing issues, switching to a credit card is recommended.  
---  
Quick SummaryError 131042 means WhatsApp cannot find a valid payment method for your account. Start by checking that a payment method is linked to your specific WABA in Meta Business Suite — not just your Business Manager. Clear any outstanding dues, verify your timezone and currency settings, and add your tax information. In most cases the error resolves immediately once billing is correctly set up. Contact support if the issue persists after completing all steps.  
---

# How to Analyze an Agency's Spending on LC Communications

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001225291-how-to-analyze-an-agency-s-spending-on-lc-communications](https://help.gohighlevel.com/support/solutions/articles/48001225291-how-to-analyze-an-agency-s-spending-on-lc-communications)  
**Category:** Email  
**Folder:** LC Communication Billing

---

Billing & Usage

Agency Spend Analytics for LC Communications

Track, analyze, and manage your agency's spend on LC Phone, LC Email, and WhatsApp — all from one dashboard.

Overview

In your agency account, we provide features that help you analyze your agency's spend on LC Communications (LC Phone, LC Email, WhatsApp, etc.).

Table of Contents

1

How to check your agency's credit balance

2

What does my agency's credit balance mean?

3

Viewing a historical summary of your spend

4

Drilling down into a single transaction

5

How and when is my card charged?

6

How can I rebill usage to my clients?

7

How can I download all transactions as a CSV?

8

Further analyzing this data

9

Paying both LC Communications and a previous provider

10

FAQ

11

Related Articles

Video Walkthrough

1

## How to check your agency's credit balance

Step 1

Switch to Agency View

Switch to your **Agency View** from the account switcher.

![Switching to Agency View](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48262037925/original/oeNjlf3jhoA6LeYvFAc8lHr15QgtLTe7fw.png?1667918295)

Step 2

Open Agency Settings

Click on **Agency Settings**.

![Agency Settings menu](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261834015/original/W6NvyvEwHqCuc1MnNr_YRXbTxpLGGJgHjg.png?1667850709)

Step 3

Go to Billing → Wallet & Transactions

Click on the **Billing tab** > **Wallet & Transactions** to see your current credit balance.

![Wallet and Transactions page](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005371766/original/B-yiXc9rcjilpNwHRemOlg3Z_fbhTWyr0Q.png?1692215238)

2

## What does my agency's credit balance mean?

When you use communication features like SMS, Calls, Voicemail drops, emails, or WhatsApp messages, the cost associated with those communications is deducted from this credit balance. This is sometimes also referred to as a **wallet**.

Please also refer to:

  * [LC Phone pricing structure](<https://help.gohighlevel.com/support/solutions/articles/48001223556-lc-phone-pricing-structure>)
  * [LC Email pricing structure](<https://help.gohighlevel.com/support/solutions/articles/48001220605-what-is-lc-email-i-want-to-know-more#LC---Email-Pricing>)
  * WhatsApp pricing structure (coming soon)


Note

As of Nov 1, 2022, our rates in the US are 10% cheaper than Twilio and approximately 8% cheaper than Mailgun. Thank you to our agencies for the overwhelming response — more power to you.

3

## Viewing a historical summary of your spend

You can see a detailed, message-by-message log of transactions by clicking on **Detailed Transactions**.

![Detailed Transactions button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005371794/original/Vr9Y1Zm7N14yg1nZe5hycpBCyV6A6IYQSg.png?1692215282)

This page gives you:

  * A unified view of all logs across all your sub-accounts (locations)
  * A summary of your month-over-month spend for the last 3 months, broken out by category


![Spend summary by category](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005371944/original/Hc8PqLNSu7EaPOHkxFBYT0iQ2kUMbzgyog.png?1692215382)

![Month-over-month spend detail](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005371932/original/0d46HEaKXh-4VKKHZH0x_qDEnwJwZ8-a6w.png?1692215338)

Expanding all categories gives you a summary of your spending by month for each individual category.

Note

Summary data refreshes once daily, so you may need to wait up to 24 hours for the most accurate reporting.

4

## Drilling down into a single transaction

We provide a detailed drill-down of each transaction or message, accessible by clicking the transaction ID in the log table.

![Transaction log table](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005372049/original/_pDVo1dTOvElF8Ada-sce5wC_gkGPVmNCQ.png?1692215652)

![Transaction detail drill-down](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005372259/original/xV7_CNrZa7u-aYsXs43_lDOl0I_b8fKVoA.png?1692216263)

5

## How and when is my card charged?

Based on your auto-recharge rules on the **Agency Settings → Billing** page, we charge your card with the **recharge amount** once your credit balance falls below the **threshold**.

Example 1

![Auto-recharge example 1](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005371956/original/bTjK9GY6rbnURLKw3qJYbHoAjA03txZmeQ.png?1692215425)

This is also the default setting. Here, once your credit balance goes below $10, your agency's credit card is charged $10 to bring your balance up to $20.

Example 2

![Auto-recharge example 2](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005371999/original/Pibi0RvAq-2lS-RffH8af9tSImjAdY1qZQ.png?1692215539)

Here, your agency's card is charged $200 once your credit balance goes below $50, bringing your balance up to $250.

Important

When a charge to your credit card fails, we notify **all agency admins** on the account. SMS, calls, emails, and other communications for all your clients are interrupted if your credit balance drops below $0.

Heads Up

Delays in payment processing can result in a one-time charge for double the recharge amount if your balance falls below $0. If your balance goes negative, the first recharge charge is applied to bring it back above $0. If that charge doesn't raise your balance above the set threshold, a second charge equal to the auto-recharge amount is applied. In total, this could result in a charge of double the recharge amount.

6

## How can I rebill usage to my clients?

If you're on the Pro plan or higher

LC Communications is designed to work better with SaaS than Twilio or Mailgun. Some inherent benefits include:

  * Instantaneous billing (no lag from Twilio webhooks)
  * A built-in ramp for new sub-accounts (locations) so a new client doesn't spike your bill — helping your agency's cash flow
  * Error rate and bounce rate monitoring to identify bad lists
  * Opt-out and unsubscribe monitoring for spam reduction
  * Carrier complaint and violation monitoring for AUP violations, protecting sender reputation


On the Pro plan or higher, you can rebill this usage to your clients using SaaS Mode (Phone & Email rebilling), including a markup to make a profit on the rebilling.

What Changed

We no longer apply a markup when rebilling **carrier charges** and **A2P 10DLC charges** — the original charges pass through without any additional markup. If you expected earnings to be exactly 2x, 3x, or 3.5x your spend, note that compliance and carrier fee charges are excluded from markup.

Please refer to:

  * [Connecting your agency's Stripe account to collect rebilling payments](<https://help.gohighlevel.com/support/solutions/articles/48001171910-how-to-connect-stripe-to-your-agency-dashboard>)
  * [How to enable email rebilling](<https://help.gohighlevel.com/support/solutions/articles/48001188579-email-re-billing>)
  * [General SaaS Mode setup and phone rebilling](<https://help.gohighlevel.com/support/solutions/articles/48001177740-activate-saas-mode-request-payment-and-configure-twilio-rebilling>)


Rebilling works so that the platform invoices you for usage, then invoices your clients on your behalf. Funds you collect from clients are deposited into your connected Stripe account.

![Rebilling invoice flow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261853138/original/CX077tEWPXWK2FNhPjTfqMc_nCO_fDxkrg.jpg?1667859306)

  * Your agency receives an invoice from the platform with platform branding
  * Sub-accounts (your client locations) receive an invoice from you, with your logo and branding as configured in your Stripe account


This system is always prepaid, meaning your agency collects money upfront and maintains positive cash flow.

If you're on the Starter or Freelancer plan

You can download a CSV report for the month and charge your clients using platform invoices or an external billing platform.

Note

LC Communication rebilling without markup for Freelancer accounts is planned for a future release.

7

## How can I download all transactions as a CSV?

You can download all LC Communication (Phone, Email & WhatsApp) charges as a CSV by clicking the export button in the top right.

![Export button for transactions](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005372008/original/XBLz8LAIdJcYErtnYvRi7xhrvykahEQ6Gg.png?1692215595)

![CSV export preview](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005372066/original/82KcMZk5JfAtG-NaW6PUU4Ovi5wYAWlsYQ.png?1692215674)

Pro Tip

This data is for agency users only. Don't share these reports directly with clients — they will see your discounted pricing (platform-to-agency pricing).

![Transaction export sample](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48262038776/original/xNHy_3v37JouzCN7rDB8cwfqYEoIZZcIxg.png?1667918416)

Note

We can provide the last 1,000,000 (1 million) transactions due to storage limits.

8

## Further analyzing this data

A walkthrough with instructions for deeper cost analysis is coming soon — check back shortly.

9

## Paying both LC Communications and a previous provider (Twilio or Mailgun/SMTP)

By design, LC Communications (LC Phone & LC Email) is enabled for your clients going forward. This means your existing clients may still be on the old provider (Twilio for calls and SMS, Mailgun/SMTP for emails). During this transition, you may be invoiced both for LC Communications usage and by Twilio, Mailgun, or other SMTP providers for usage on older sub-accounts.

The easiest way to resolve this is to move all existing clients over to LC Phone & LC Email and close out your accounts with other providers.

Important

Certain assets, like call recordings, do not migrate over. If you need access to call recordings or logs for compliance or HIPAA regulations, keep your Twilio account operating in a dormant state.

10

## FAQ

Q: What happens if a payment fails?

If SMS and email charges are left unpaid, we stop all outbound emails and SMS.

Q: What happens to my balance if I cancel?

We can refund the credit to the credit card linked to your agency account.

Q: My wallet has a balance, but I can't send SMS or email — why?

Your balance needs to stay at or above 50% of your configured "when balance is lower than" threshold for LC Phone and LC Email. If it drops below 50% of that threshold, outbound emails and SMS are stopped.  
  
If your agency sends high volume, raise this threshold so auto-recharge kicks in sooner — otherwise you risk running out of headroom before the recharge triggers.

![Auto-recharge threshold setting](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005372072/original/kkMQhM9I0LM7_6ejO8X4YfM_BT0bnp_5Wg.png?1692215699)

For example, if "when balance is lower than" is set to $10, your wallet needs to stay above $5 to send outbound emails and SMS. This safeguards the account from going negative.

Q: Can I customize my auto-recharge amount and threshold?

Yes. Both values are configurable from Agency Settings → Billing, so you can tune how often and how much your card is charged based on your sending volume.

Q: Does my credit balance expire?

No, credit balances don't expire — they carry forward and are drawn down as communications are sent across your sub-accounts.

Q: Can I see spend broken out by individual sub-account?

Yes. The detailed transactions log and CSV export both include a unified view across all sub-accounts (locations), so you can filter or sort by client.

Related Articles

[Why is my SMS cost so high?](<https://help.gohighlevel.com/en/support/solutions/articles/48001203458>) [What is LC Phone System?](<https://help.gohighlevel.com/en/support/solutions/articles/48001223546>) [LC Phone pricing structure](<https://help.gohighlevel.com/en/support/solutions/articles/48001223556>) [How to migrate an agency and sub-account to LC Phone](<https://help.gohighlevel.com/en/support/solutions/articles/48001204027>) [LC Phone messaging policy](<https://help.gohighlevel.com/en/support/solutions/articles/48001213941>) [What is LC Email? I want to know more](<https://help.gohighlevel.com/en/support/solutions/articles/48001220605>) [How to migrate my agency over to LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>)

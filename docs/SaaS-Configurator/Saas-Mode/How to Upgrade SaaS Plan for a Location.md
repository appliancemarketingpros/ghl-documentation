# How to Upgrade SaaS Plan for a Location

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001207110-how-to-upgrade-saas-plan-for-a-location](https://help.gohighlevel.com/support/solutions/articles/48001207110-how-to-upgrade-saas-plan-for-a-location)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

SaaS • Plan Changes • Subscription Sync

How to Upgrade or Downgrade a SaaS Plan for a Location

Upgrading or downgrading a SaaS plan changes the client's subscription tier, billing, and feature access. For eligible SaaS V1 subscriptions sold through a selling sub-account, supported plan changes now keep the Stripe subscription and corresponding sub-account subscription aligned. This helps current product, price, invoice, and tax data stay consistent after future upgrades or downgrades.

What You'll Learn

This guide explains SaaS V1 and V2 plan-change behavior, how to enable client-initiated upgrades and downgrades, how eligible V1 subscriptions stay synchronized after a supported plan change, and what to expect for billing, invoices, taxes, and historical subscription mismatches.

Important

**SaaS V1 and SaaS V2 use different billing architectures.** SaaS V1 continues to use Stripe as its system of record. The new V1 subscription bridge does not convert V1 subscriptions into V2 subscriptions; it keeps the corresponding subscription in the V1 selling sub-account aligned when a supported upgrade or downgrade occurs.

Table of Contents

1

What is Upgrading or Downgrading a SaaS Plan?

2

Key Benefits of SaaS Plan Changes

3

SaaS V1 vs. SaaS V2 Plan-Change Behavior

4

SaaS V1 Subscription Sync After a Plan Change

5

How To Set Up Client Plan Changes

6

How Clients Change Their SaaS Plan

7

Agency-Side SaaS V1 Plan Changes

8

Frequently Asked Questions

9

Related Articles

1

# What is Upgrading or Downgrading a SaaS Plan for a Location?

Upgrading or downgrading a SaaS plan moves a client sub-account from one configured SaaS subscription tier to another. A plan change can affect billing, product and price information, feature access, usage limits, and when applicable, the client's billing interval.

Clients can perform supported self-service plan changes when the appropriate SaaS Configurator settings are enabled. Agencies can also manage plan changes according to the billing architecture used by the subscription.

For eligible SaaS V1 subscriptions sold through a selling sub-account, supported upgrades and downgrades now synchronize the Stripe subscription with the corresponding subscription stored in that selling sub-account.

2

## Key Benefits of SaaS Plan Changes

Well-configured upgrade and downgrade workflows give clients flexibility while helping agencies keep plan access and billing data aligned. The new V1 subscription bridge also reduces the chance of stale product, price, invoice, or tax information after supported plan changes.

**Revenue Growth:** Self-service upgrades let clients move to higher-value plans when they need additional capabilities.

**Billing Accuracy:** Eligible SaaS V1 plan changes keep the Stripe subscription and corresponding selling-sub-account subscription aligned.

**Invoice Accuracy:** Sub-account invoices can reflect the current product and price after a supported V1 upgrade or downgrade.

**Tax Accuracy:** Tax can be recalculated using current plan information instead of stale subscription data after an eligible plan change.

**Feature Control:** Plan-based settings determine which features and apps become available when the change takes effect.

**Churn Reduction:** Configurable downgrade reasons and optional deflection offers can help retain customers considering a lower plan.

3

## SaaS V1 vs. SaaS V2 Plan-Change Behavior

SaaS V1 and V2 can coexist, but they use different billing systems of record. Identifying which architecture owns the subscription is important before changing billing details or troubleshooting plan-change behavior.

Behavior| SaaS V1| SaaS V2  
---|---|---  
**Billing system of record**|  Stripe| HighLevel through the selected Agency Sub-Account  
**New subscription bridge**|  Applies to eligible V1 subscriptions sold through the supported selling-sub-account workflow.| Not the scope of this V1 bridge because V2 already uses the Agency Sub-Account architecture.  
**Billing interval changes**|  Managed according to the Stripe/V1 subscription configuration.| Monthly and annual intervals can be changed as part of a supported plan change.  
**Proration**|  May be handled through the V1/Stripe billing workflow.| **No proration** for tier changes, billing interval changes, or combined tier and interval changes.  
  
### SaaS V2 Billing Interval Changes

SaaS V2 clients can move between monthly and annual billing while changing to another supported SaaS plan. This allows the tier and billing interval to be selected in the same plan-change experience.

**Important:** SaaS V2 does not support proration for plan-tier changes, billing-interval changes, or changes that combine both.

4

## SaaS V1 Subscription Sync After a Plan Change

Eligible SaaS V1 subscriptions can exist in both Stripe and the selling sub-account used to sell the SaaS plan. The subscription bridge keeps these two records aligned when a supported SaaS upgrade or downgrade occurs, reducing billing differences between the systems.

Before the Subscription Bridge| With the Subscription Bridge  
---|---  
The SaaS plan change updated the Stripe subscription.| The supported SaaS plan change updates the Stripe subscription **and** the corresponding selling-sub-account subscription.  
The selling-sub-account subscription could continue referencing an older product or price.| The selling-sub-account subscription receives the current product and price information.  
Invoices generated from stale sub-account subscription data could reference incorrect plan details.| Invoices generated from the selling sub-account can reflect the current product and price after the plan change.  
Tax could be calculated using outdated plan information.| Tax is recalculated against the current plan information when the supported plan change occurs.  
  
### Which SaaS V1 Subscriptions Are Covered?

The bridge is intended for the SaaS V1 selling pattern where the SaaS product is created in Stripe, imported into an agency-owned selling sub-account, and sold from that sub-account through a supported payment link or funnel.

**Supported pattern:** SaaS Plan → Stripe Product → Product imported into the selling sub-account → Subscription sold through the selling sub-account → Supported SaaS upgrade or downgrade.

### Historical Subscription Mismatches

The subscription bridge is not a retroactive backfill. If the Stripe subscription and selling-sub-account subscription became mismatched before this behavior was introduced, the existing mismatch is not automatically repaired simply because the bridge is now available.

**Existing mismatches:** A future supported upgrade or downgrade can update both records through the new flow. Until a qualifying plan change occurs, older mismatches may remain.

### What the New Sync Does Not Guarantee

The subscription bridge is tied to supported SaaS upgrade and downgrade events. Avoid extending this behavior to unrelated subscription changes unless that workflow explicitly supports the same synchronization.

  * Do not assume arbitrary manual edits made directly in Stripe trigger the same bridge.
  * Do not assume cancellations, pauses, resumptions, or failed-payment states use this upgrade/downgrade synchronization unless documented separately.
  * The V1 bridge does not change SaaS V2 architecture.
  * Stripe remains the SaaS V1 billing system of record.


5

## How To Set Up Client Plan Changes

Plan-change permissions determine whether clients can manage upgrades or downgrades without contacting your agency. Configure these settings before directing clients to Company Billing so the intended plans and actions are available.

### Allow Upgrades for All Future SaaS Clients

The agency-level upgrade setting applies your preferred self-service behavior to SaaS accounts created through the SaaS Configurator moving forward.

  1. Sign in to your **Agency** account.
  2. Open **SaaS Configurator**.
  3. Open **Advanced Settings**.
  4. Enable **Allow sub-account admins to upgrade their subscription**.
  5. If clients should receive new plan features and apps immediately after upgrading, enable **Add New Plans Features and Apps Upon Upgrading**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791576/original/kJoICfb8Cd9YhngyWP0xAimdoBt_-bKLmQ.png?1789247807)

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791578/original/1Nblpes9hZRTFImH5wleyKYlkuBpHh3uGA.png?1789247863)

### Allow Upgrades for a Specific Client

Per-client controls let you enable self-service upgrades for an individual sub-account without changing the agency-wide default for other clients.

  1. Sign in to your agency account.
  2. Go to **Sub-accounts**.
  3. Find the client sub-account and select **⋯ > Manage Client**.
  4. Enable **Allow sub-account admins to upgrade their subscription**.
  5. Enable **Add New Plans Features and Apps Upon Upgrading** if the upgraded feature set should become available immediately.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791588/original/GrykPcD4gLGceumsyE25X0tFT6butC-B9A.png?1789247910)

![Per-client SaaS upgrade permissions](https://jumpshare.com/share/tFgldzrcAp6bsYEORmyr+/Screenshot+2025-12-09+at+8.08.11%E2%80%AFPM.png)

### Configure Client-Initiated Downgrades

Downgrades use separate settings from the upgrade permission. You can decide whether clients may downgrade themselves, collect downgrade reasons, and optionally configure retention offers before a lower-tier plan is scheduled.

Configure downgrade behavior in **SaaS Configurator > Downgrade Settings**. Eligible downgrades take effect according to the configured downgrade flow, typically at the start of the next billing cycle. See [How to Configure Downgrade Settings for SaaS Clients](<https://help.gohighlevel.com/support/solutions/articles/155000006450-how-to-configure-downgrade-settings-for-saas-clients>).

6

## How Clients Change Their SaaS Plan

Clients can manage available plan changes from their billing area when your agency has enabled the relevant self-service permissions. The exact options shown depend on the client's current plan, plan category and level, currency, architecture, and your configured upgrade or downgrade rules.

### Client Upgrade Flow

The upgrade flow lets an eligible client select a higher plan and complete the associated billing change from Company Billing.

Step 1

Open Company Billing

Sign in to the client sub-account and go to **Settings > Company Billing**.

![Company Billing page inside a client sub-account](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155060236383/original/Y9q2Uq2hSKlLAnk2V2fnBESOlVoeW1IxWA.png?1765292095)

Step 2

Select Upgrade

Click **Upgrade** to view the plans available to the client.

![Upgrade action in Company Billing](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155060236426/original/kNndbG7aeuo39PgK2NDdrM2htx9BaHwRhg.png?1765292134)

Step 3

Choose the New Plan

Select the destination SaaS plan. Available choices depend on the configured plan category, level, pricing, currency, and client eligibility.

![Available SaaS plans shown during the upgrade flow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155060236668/original/PA1QyQasuchZqKo6CZqlMkTHULfeNbvy4A.png?1765292284)

Step 4

Review Billing Options

Review the plan price and available billing interval options. For SaaS V2 subscriptions, monthly and annual billing can be changed as part of the supported plan change.

![Plan change screen showing billing interval options](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48283852490/original/kFYGhwqxIrVkK_C_8uqXFaTt6SBcEmhZZQ.png?1677442334)

Step 5

Confirm the Plan Change

Review the final billing information and select **Confirm & Pay**. If immediate feature access is enabled by the agency, the client can receive the new plan's configured features and apps when the upgrade completes.

![Confirm and Pay step for a SaaS plan upgrade](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48283852530/original/RMElQ7DTY-E66queGSyUWLBgJ01MOLS23A.png?1677442426)

**Eligible SaaS V1 subscriptions:** When the supported upgrade completes, the subscription bridge updates both the Stripe subscription and the corresponding subscription in the selling sub-account.

### Client Downgrade Flow

When self-service downgrades are enabled, clients can initiate a move to a lower plan from their billing settings. Downgrades can include a required reason and optional retention offer, and eligible changes are scheduled according to your downgrade configuration.

**Typical client path:** Account Settings → Billing → Modify Subscription → Downgrade.

**Downgrade timing:** If a downgrade is scheduled for the start of the next billing cycle, the V1 subscription synchronization should be understood as occurring when the qualifying downgrade takes effect—not merely when the client first requests it.

7

## Agency-Side SaaS V1 Plan Changes

SaaS V1 continues to use Stripe as its billing system of record, so agencies may still need to work with the customer's Stripe subscription in legacy or manual scenarios. Direct Stripe edits should be treated separately from the supported SaaS upgrade/downgrade event that triggers the new subscription bridge.

**Important:** Do not assume an arbitrary manual Stripe edit automatically updates the corresponding subscription in the selling sub-account. The new bridge is documented for supported SaaS upgrade/downgrade events. After a direct Stripe edit, verify the subscription state and client feature access.

### Find the SaaS V1 Customer in Stripe

Use the client's invoice information to identify the correct Stripe customer before making a manual V1 subscription change. This helps avoid modifying the wrong customer record.

  1. Open the client sub-account and go to **Settings > Company Billing**.
  2. Select **View** for an invoice in Billing History.
  3. Copy the invoice number.
  4. Search for that invoice in Stripe and open it.
  5. Select the customer shown in the invoice's billing details to open the correct Stripe customer profile.


![Company Billing invoice history](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48179191623/original/YgHpXmm6kMJ-ZXFtH_ampYMSw6Qq10CdJQ.png?1642180932)

![Invoice number used to locate the Stripe customer](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48179191948/original/28_J0a_IQe8l30wGT2UWHt0iDyTkxAwCqQ.png?1642181036)

![Stripe invoice details used to identify the SaaS customer](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48179192675/original/IxhpfGaIOK5uxgGt3WgUba37jlPIW6ybQg.png?1642181198)

### Change the SaaS V1 Subscription in Stripe

For a manual V1 change, edit the customer's existing Stripe subscription carefully and confirm the intended price and billing behavior before saving.

  1. Open the customer's active subscription in Stripe.
  2. Select the edit control for the subscription.
  3. Remove the current price and add the correct price for the destination SaaS plan.
  4. Review any Stripe proration or billing adjustments that apply to the V1 change.
  5. Save the subscription update.


![Stripe subscription edit control](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48179204701/original/tW6N-xWl8eQg9Slvwr0PISwUriI_BCJgzg.png?1642183950)

![Stripe subscription price selection](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48179205217/original/qgQsQVyZBOJFYg9daBCfeUTldUzQNuxs2A.png?1642184088)

![Stripe subscription update and proration options](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48179205549/original/YHLzV6ZB7SuwdPZgJPqUR47CJ458GKHFgQ.png?1642184206)

### Verify Feature Access and Subscription Alignment

After a direct Stripe change, verify the client's plan access in the agency and confirm that any corresponding selling-sub-account subscription reflects the intended state. Manual Stripe edits are not the same as a supported SaaS plan-change event.

  1. Return to the agency view and open the client's account details.
  2. Verify that the client's accessible features match the intended destination plan.
  3. Save any required feature-access changes.
  4. If the subscription was originally sold through a V1 selling sub-account, verify that the sub-account subscription is not left with stale product or price information.


![Agency account details used to verify SaaS plan feature access](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791562/original/8YyjlynWu_RqI0QbCorzn3HBRX9lME5YWA.png?1789247677)

8

## Frequently Asked Questions

Q: Does a supported SaaS V1 upgrade update both Stripe and the selling-sub-account subscription?

Yes, for eligible V1 subscriptions created through the supported selling-sub-account pattern. The supported upgrade flow updates the Stripe subscription and the corresponding subscription inside the selling sub-account.

Q: Does the same synchronization apply to downgrades?

Yes, when an eligible SaaS V1 downgrade goes through the supported plan-change flow. If the downgrade is scheduled for a later billing date, the synchronized plan change occurs when the downgrade takes effect.

Q: Are older V1 subscription mismatches automatically repaired?

No. Existing mismatches are not automatically backfilled. A future supported upgrade or downgrade can update both subscription records through the new bridge.

Q: Will invoices use the new product and price after an eligible V1 plan change?

Yes. Keeping the selling-sub-account subscription aligned allows invoices generated from that subscription to reference the current product and price after the supported plan change.

Q: Is tax recalculated after an eligible V1 upgrade or downgrade?

Yes. The synchronized subscription uses the current plan information so tax can be recalculated against the updated plan instead of stale product or price data.

Q: Does manually editing a Stripe subscription guarantee the same V1 synchronization?

No automatic guarantee should be assumed for arbitrary direct Stripe edits. The bridge is documented for supported SaaS upgrade and downgrade events. Verify the corresponding selling-sub-account subscription after a manual Stripe change.

Q: Why doesn't the destination plan appear for my client?

Check plan category and level alignment, currency, client self-service permissions, and the pricing configuration associated with the destination plan.

Q: Can clients receive upgraded features immediately?

Yes, when **Add New Plans Features and Apps Upon Upgrading** is enabled for the applicable client or SaaS setup.

Q: Can SaaS V2 clients switch between monthly and annual billing?

Yes. SaaS V2 subscriptions can switch between monthly and annual billing as part of a supported plan upgrade or downgrade. SaaS V2 does not support proration for tier changes, billing-interval changes, or combined tier and interval changes.

9

### Related Articles

[ Getting Started with the SaaS Configurator ](<https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator>) [ How to Configure Downgrade Settings for SaaS Clients ](<https://help.gohighlevel.com/support/solutions/articles/155000006450-how-to-configure-downgrade-settings-for-saas-clients>) [ Automatic Tax Calculation with Stripe for SaaS Subscriptions ](<https://help.gohighlevel.com/support/solutions/articles/155000007789-automatic-tax-calculation-with-stripe-for-saas-subscriptions>) [ Payments - What is listed on the Subscriptions page? ](<https://help.gohighlevel.com/support/solutions/articles/48001225935>) [ SaaS Configurator - Modify Plan Category and Plan Level ](<https://help.gohighlevel.com/support/solutions/articles/155000006506>) [ How to Cancel SaaS Sub-Account for Your Client ](<https://help.gohighlevel.com/support/solutions/articles/48001216453>)

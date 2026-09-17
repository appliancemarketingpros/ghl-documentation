# Getting Started with the SaaS Configurator

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator](https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

SaaS • Configurator • V1 & V2

Getting Started with the SaaS Configurator

The SaaS Configurator helps agencies package, price, sell, and manage recurring SaaS plans for client sub-accounts. It supports both Stripe-based SaaS V1 and Agency Sub-Account-based SaaS V2 architectures. This guide explains how to choose the right architecture, create plans, sell subscriptions, onboard customers, and understand how eligible SaaS V1 subscriptions stay aligned after supported plan changes.

What You'll Learn

Learn how SaaS V1 and V2 differ, connect the appropriate payment provider, create plan categories and SaaS plans, sell through funnels or checkout links, onboard customers, and manage the subscription lifecycle after the initial sale.

Important

**SaaS V1 and SaaS V2 are separate billing architectures.** SaaS V1 remains Stripe-based, while SaaS V2 uses an Agency Sub-Account as the billing system of record. The SaaS V1 subscription bridge described in this guide keeps eligible selling-sub-account subscriptions aligned after supported upgrades and downgrades; it does not convert V1 subscriptions into V2.

Table of Contents

1

What is the SaaS Configurator?

2

Key Benefits of the SaaS Configurator

3

SaaS V1 vs. SaaS V2

4

How To Set Up the SaaS Configurator

5

Selling SaaS

6

SaaS V1 Subscription Sync After Plan Changes

7

Onboarding Customers

8

Running V1 and V2 in Parallel

9

Frequently Asked Questions

10

Related Articles

1

# What is the SaaS Configurator?

The SaaS Configurator is HighLevel's built-in tool for packaging platform access into recurring SaaS subscription plans. Agencies can define pricing, features, snapshots, add-ons, usage billing, and other plan settings while controlling how customers purchase and access their sub-accounts.

HighLevel supports two SaaS billing architectures: SaaS V1 and SaaS V2. Both can be managed from the SaaS Configurator, but they differ in where products, subscriptions, and billing records are maintained.

2

## Key Benefits of the SaaS Configurator

The SaaS Configurator centralizes the core components needed to sell recurring software access. This gives agencies a repeatable way to package services, automate onboarding, and manage different billing architectures from one SaaS management experience.

**Recurring Revenue:** Package access into monthly or annual SaaS plans instead of manually billing each client.

**Flexible Billing Architecture:** Use Stripe-based SaaS V1 or Agency Sub-Account-based SaaS V2 according to your payment-provider and billing needs.

**Automated Onboarding:** Provision client sub-accounts, apply snapshots, and establish plan access after successful SaaS checkout.

**Plan Control:** Define features, pricing, categories, trials, credits, add-ons, and usage-based billing from the SaaS plan configuration.

**Subscription Accuracy:** Eligible SaaS V1 subscriptions sold through a selling sub-account can keep Stripe and the corresponding selling-sub-account subscription aligned after supported upgrades and downgrades.

3

## SaaS V1 vs. SaaS V2

SaaS V1 and V2 are separate billing architectures rather than sequential versions that require migration. Understanding which system owns the subscription helps you choose the correct setup, payment provider, and troubleshooting workflow.

Architecture| SaaS V1| SaaS V2  
---|---|---  
**System of record**|  Stripe| HighLevel through the selected Agency Sub-Account  
**Payment providers**|  Stripe| Supported payment providers connected to the Agency Sub-Account  
**Products managed in**|  Stripe| HighLevel  
**Billing interval changes**|  Handled according to the V1/Stripe subscription workflow| Monthly and annual intervals can be changed as part of a supported plan upgrade or downgrade  
**Proration for plan changes**|  Can be handled through the V1/Stripe billing workflow| **Not supported** for tier changes, interval changes, or combined tier and interval changes  
  
**Architecture guardrail:** The SaaS V1 subscription bridge does not change the V1 system of record. Stripe continues to own the V1 subscription even when the corresponding subscription in a selling sub-account is synchronized after a supported plan change.

For a deeper architectural comparison, see [SaaS V1 vs SaaS V2: What's the Difference?](<https://help.gohighlevel.com/support/solutions/articles/155000007968-saas-v1-vs-saas-v2-what-s-the-difference->)

![SaaS Configurator showing SaaS V1 and V2 plan architecture](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791739/original/oKVP0iEdTJ8Pr4vlDVXx0LUwJr00Ryf77w.png?1789248979)

4

## How To Set Up the SaaS Configurator

Proper setup establishes which billing architecture owns your subscriptions and ensures customers can purchase the correct plans. Complete the payment-provider configuration before creating plans so pricing, products, and subscription records are associated with the intended system.

### Before You Begin

Confirm the required agency access and payment-provider configuration before creating your first SaaS plan. The prerequisites differ depending on whether you are using V1 or V2.

  * You have the appropriate **Agency Admin** access.
  * **For SaaS V1:** You have a Stripe account available to connect to the agency.
  * **For SaaS V2:** You have an Agency Sub-Account with a supported payment provider configured under **Payments > Integrations**.


### Connect Stripe for SaaS V1

SaaS V1 uses Stripe as the billing system of record, so the agency Stripe connection must be established before creating V1 plans and prices.

  1. Go to **Agency View > Settings > Stripe**.
  2. Click **Connect with Stripe** and complete the connection flow.
  3. Return to **Agency View > SaaS Configurator** and continue to plan creation.


![Stripe connection settings for SaaS V1](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791740/original/eDVGERxqfbrobEbDttVkZK1ckaFR7LIgqw.png?1789248995)

### Select an Agency Sub-Account for SaaS V2

SaaS V2 uses a designated internal Agency Sub-Account to manage products, subscriptions, and payments. Select the sub-account that should serve as the billing system of record before creating V2 plans.

  1. Go to **Agency View > SaaS Configurator > Configure**.
  2. Click **Select Sub-Accounts**.
  3. Choose the Agency Sub-Account and click **Add Sub-Account**.
  4. Confirm that a supported payment provider is configured under **Payments > Integrations** inside that sub-account.


![Selecting an Agency Sub-Account for SaaS V2](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791748/original/lXfzX3TdKpBrVXh1vuX7ssX763xsJQ_uyQ.png?1789249029)

**What is an Agency Sub-Account?** It is an internal sub-account owned by the agency and used for agency operations. In SaaS V2, it serves as the billing system of record for the SaaS products and subscriptions associated with it.

### Create a Plan Category

Plan categories organize related plans into upgrade and downgrade paths. Keeping compatible plans in the same category helps determine which destination plans customers can select later.

  1. Open **SaaS Configurator > Advanced Settings**.
  2. Click **Add New Category**.
  3. Enter a category name and select the currency.
  4. Click **Save**.


**Currency:** Plans within the same category should use the same currency. If you sell in multiple currencies, use separate categories so customers are presented with compatible upgrade and downgrade options.

**Plan changes:** Supported upgrades and downgrades do not require disabling and re-enabling SaaS. Changing a plan's category or level can affect which plan-change paths are available to customers, so review category structure carefully before editing it.

![Creating a SaaS plan category](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791759/original/-X8x81EQ_vM1X9E7zM-2a_IM3aqJUUMhlw.png?1789249056)

### Create a SaaS Plan

A SaaS plan defines what the customer pays and what they receive. Configure the plan details carefully because pricing, feature access, snapshots, add-ons, and usage rules become part of the customer's subscription experience.

  1. In **SaaS Configurator** , click **Add Your Plan**.
  2. Select the applicable payment processor or billing architecture.
  3. Configure the plan details, category, pricing, features, snapshot, add-ons, Marketplace apps, trial or credits, and usage billing as needed.
  4. Select at least one product feature for the plan.
  5. Review the configuration and save the plan.


Configuration| Purpose  
---|---  
**Plan Details**|  Name and customer-facing plan information  
**Category**|  Determines related upgrade and downgrade paths  
**Pricing**|  Monthly and/or annual subscription pricing  
**Features & Snapshot**| Controls access and optional automatic sub-account configuration  
**Add-ons**|  Optional paid capabilities customers can select  
**Marketplace Apps**|  Eligible third-party apps bundled with the plan  
**Trial & Credits**| Trial duration and complimentary-credit behavior  
**Usage Billing**|  Usage-based or per-unit charges configured for the plan  
  
**At least one feature is required:** Select one or more features before saving a SaaS plan. A plan cannot be completed without a product feature selected.

![Feature selection required for a SaaS plan](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080791768/original/wKG6o0ot67Mz6XeWrBNzIAx9a7FuN-6zZA.png?1789249089)

5

## Selling SaaS

SaaS plans can be sold through a branded funnel or through a direct SaaS checkout link. The sales workflow differs between V1 and V2 because V1 products originate in Stripe while V2 products are managed from the selected Agency Sub-Account.

### Sell SaaS V1 Through a Selling Sub-Account Funnel

The V1 funnel workflow brings the Stripe-based SaaS product into a selling sub-account so it can be placed on an order form. This is also the selling pattern associated with the V1 subscription synchronization behavior described later in this guide.

  1. Switch to the sub-account used to sell the SaaS subscription.
  2. Go to **Payments > Products > Import From Stripe**.
  3. Find the SaaS Stripe product and import the applicable price.
  4. Go to **Sites > Funnels**.
  5. Add the imported SaaS product to a supported order form and publish the funnel.


For detailed import instructions, see [Import Products / Price From Stripe](<https://help.gohighlevel.com/support/solutions/articles/48001202184>).

**When a V1 Stripe price changes:** Re-import the updated price into the selling sub-account before selecting it in a funnel or website. Updating the SaaS plan or Stripe price does not automatically replace the product price already selected on an existing funnel order form.

### Sell SaaS V2 Through an Agency Sub-Account Funnel

V2 products are created and managed through the Agency Sub-Account, so they can be selected directly from that sub-account's Payments and funnel tools without importing them from Stripe.

  1. Switch to the applicable **Agency Sub-Account**.
  2. Go to **Payments > Products** and confirm the SaaS product is available.
  3. Go to **Sites > Funnels** and add the SaaS product to the appropriate order form.


### Generate a Direct SaaS Checkout Link

A direct checkout link provides a faster sales option when you do not need a full funnel. The link can be shared through email, proposals, social channels, or buttons on another webpage.

  1. Open **SaaS Configurator > Plans & Pricing**.
  2. Locate the SaaS plan.
  3. Click **Copy Sale Link**.
  4. Share the checkout link with the customer.


**Subscription-sync scope:** The V1 bridge described below applies to eligible subscriptions using the selling-sub-account workflow. Do not assume every SaaS Configurator checkout method uses the same selling-sub-account subscription path unless that workflow is specifically documented.

6

## SaaS V1 Subscription Sync After Plan Changes

Eligible SaaS V1 subscriptions sold through a selling sub-account can have a Stripe subscription and a corresponding subscription record inside that selling sub-account. Supported SaaS upgrades and downgrades now update both records so plan information does not remain stale in the selling sub-account.

Before| After a Supported V1 Plan Change  
---|---  
The SaaS plan change could update Stripe while the corresponding selling-sub-account subscription remained on older plan data.| The supported plan change updates Stripe and the corresponding selling-sub-account subscription in the same flow.  
The selling-sub-account subscription could reference an outdated product or price.| The current product and price are synchronized to the corresponding subscription.  
Downstream invoices could use stale plan information.| Invoices generated from the selling-sub-account subscription can reflect the current plan information.  
Applicable tax could be based on older plan information.| When tax applies, it can be recalculated using the current plan information after the qualifying plan change.  
  
**Covered V1 pattern:** SaaS plan → Stripe product → product imported into the selling sub-account → subscription sold from that selling sub-account → supported SaaS upgrade or downgrade.

**Not retroactive:** Existing Stripe and selling-sub-account subscription mismatches are not automatically backfilled. A future qualifying upgrade or downgrade can update both records through the new synchronization flow.

**Manual Stripe edits:** Do not assume arbitrary changes made directly in Stripe automatically trigger the V1 subscription bridge. The synchronization described here is tied to supported SaaS upgrade and downgrade events.

7

## Onboarding Customers

SaaS onboarding connects a successful subscription purchase to the client's sub-account, feature access, and any configured snapshot. Understanding what happens at checkout helps distinguish initial provisioning from later subscription lifecycle events such as upgrades and downgrades.

### New Customer Through SaaS Checkout

When a new customer successfully completes a supported SaaS checkout, the configured SaaS workflow provisions the subscription and corresponding sub-account access.

  1. **Payment is confirmed** through the applicable billing architecture.
  2. **The sub-account is created or linked** to the customer as applicable.
  3. **The configured snapshot is applied** when a snapshot is attached to the SaaS plan.
  4. **Customer access is established** according to the onboarding workflow.
  5. **The subscription becomes active or trialing** according to the plan configuration.


**After onboarding:** For eligible SaaS V1 subscriptions sold through the selling-sub-account workflow, a later supported upgrade or downgrade can update both the Stripe subscription and the corresponding selling-sub-account subscription.

### Manually Add SaaS to an Existing Sub-Account

Use the manual SaaS subscription flow when the client already has a sub-account and needs to be placed on a SaaS plan without creating a new location through checkout.

  1. Go to **Agency View > Sub-Accounts**.
  2. Open the target sub-account and select **Manage Client**.
  3. Open the **SaaS** area and select **Add a SaaS Subscription**.
  4. Select the applicable payment processor.
  5. Choose or create the customer profile.
  6. Select the SaaS plan.
  7. If needed, configure a **Special Price** for that specific client.
  8. Complete the payment flow so the subscription can be linked to the sub-account.


**Special Prices:** A special price can be useful for promotional pricing, enterprise agreements, or grandfathered rates because it applies to that client without changing the public plan price.

8

## Running SaaS V1 and V2 in Parallel

Agencies can operate V1 and V2 plans at the same time. Keeping the architectures separate lets existing Stripe-based V1 subscriptions continue while new plans use V2 where its billing architecture is a better fit.

  * Both architectures can appear in the SaaS Configurator.
  * V1 subscriptions continue to use Stripe as the billing system of record.
  * V2 subscriptions use the selected Agency Sub-Account as the billing system of record.
  * The V1 subscription bridge does not migrate or convert a V1 subscription into V2.


![SaaS V1 and V2 plans displayed together in the SaaS Configurator](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072206393/original/ap8aymH8MT0wjfQmKQJZezy4G72EvQbtmw.png?1779793072)

### Where to Troubleshoot Billing

Start troubleshooting in the system of record for the subscription. This helps avoid making a billing change in the wrong architecture.

Architecture| Start Here  
---|---  
**V1**|  Stripe and the SaaS V1 subscription configuration  
**V2**|  The selected Agency Sub-Account and its Payments module  
  
9

## Frequently Asked Questions

Q: Does the new V1 subscription bridge make SaaS V1 the same as SaaS V2?

No. Stripe remains the SaaS V1 system of record. The bridge only keeps the corresponding selling-sub-account subscription aligned after supported V1 upgrades and downgrades.

Q: Are existing V1 subscription mismatches automatically fixed?

No. The synchronization is not a retroactive backfill. A future qualifying upgrade or downgrade can update both the Stripe and selling-sub-account records.

Q: Does manually editing a V1 subscription in Stripe guarantee the selling-sub-account subscription will update?

No automatic guarantee should be assumed for arbitrary manual Stripe edits. The bridge is documented for supported SaaS upgrade and downgrade events.

Q: Do I need to disable and re-enable SaaS when a customer changes plans?

No. Supported upgrade and downgrade workflows do not require disabling and re-enabling SaaS simply to move a customer between eligible plans.

Q: What happens if I change a V1 Stripe price used on a funnel?

Import the updated Stripe price into the selling sub-account and update the product or price selected on the applicable funnel or website.

Q: Can SaaS V2 customers move between monthly and annual billing?

Yes. SaaS V2 can change between monthly and annual billing as part of a supported plan upgrade or downgrade. SaaS V2 does not support proration for tier changes, interval changes, or combined tier and interval changes.

Q: Can I operate V1 and V2 plans at the same time?

Yes. V1 and V2 can coexist in the SaaS Configurator while retaining their separate systems of record and payment workflows.

10

### Related Articles

[ SaaS V1 vs SaaS V2: What's the Difference? ](<https://help.gohighlevel.com/support/solutions/articles/155000007968-saas-v1-vs-saas-v2-what-s-the-difference->) [ How to Upgrade or Downgrade a SaaS Plan for a Location ](<https://help.gohighlevel.com/support/solutions/articles/48001207110-how-to-upgrade-saas-plan-for-a-location>) [ SaaS Configurator - Modify Plan Category and Plan Level ](<https://help.gohighlevel.com/support/solutions/articles/155000006506>) [ Import Products / Price From Stripe ](<https://help.gohighlevel.com/support/solutions/articles/48001202184>) [ Automatic Tax Calculation with Stripe for SaaS Subscriptions ](<https://help.gohighlevel.com/support/solutions/articles/155000007789-automatic-tax-calculation-with-stripe-for-saas-subscriptions>) [ How to Configure Downgrade Settings for SaaS Clients ](<https://help.gohighlevel.com/support/solutions/articles/155000006450-how-to-configure-downgrade-settings-for-saas-clients>)

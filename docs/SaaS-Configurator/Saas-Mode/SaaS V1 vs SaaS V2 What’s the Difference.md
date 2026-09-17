# SaaS V1 vs SaaS V2: What’s the Difference?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007968-saas-v1-vs-saas-v2-what-s-the-difference-](https://help.gohighlevel.com/support/solutions/articles/155000007968-saas-v1-vs-saas-v2-what-s-the-difference-)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

SaaS • V1 • V2

SaaS V1 vs SaaS V2: What's the Difference?

HighLevel supports two different SaaS billing architectures: SaaS V1 and SaaS V2. V1 uses Stripe as its billing system of record, while V2 uses an Agency Sub-Account and can support multiple payment providers. Understanding how the architectures differ helps you choose the right setup for billing, subscription management, plan changes, and client onboarding.

What You'll Learn

Learn how SaaS V1 and V2 differ, where subscriptions are managed, how payment providers work, which billing capabilities are currently different, and how the SaaS V1 subscription bridge keeps eligible subscription records aligned after supported plan changes.

Important

**SaaS V2 is not an upgrade or replacement for SaaS V1.** They are separate billing architectures and can operate side by side. The SaaS V1 subscription bridge improves synchronization for eligible V1 subscriptions without changing Stripe's role as the V1 system of record.

Table of Contents

1

What is the Difference Between SaaS V1 and SaaS V2?

2

Key Benefits of Understanding SaaS V1 vs SaaS V2

3

SaaS V1 Architecture

4

SaaS V2 Architecture

5

SaaS V1 Subscription Sync After Plan Changes

6

Current Feature Differences

7

Which SaaS Version Should You Choose?

8

How To Set Up the Right SaaS Billing Architecture

9

Frequently Asked Questions

10

Related Articles

1

# What is the Difference Between SaaS V1 and SaaS V2?

SaaS V1 and SaaS V2 provide two different ways to manage recurring SaaS subscriptions. The primary difference is where the subscription is owned and managed: V1 uses Stripe as the system of record, while V2 uses an Agency Sub-Account. This architectural difference affects payment-provider options, subscription management, integrations, and some billing capabilities.

Area| SaaS V1| SaaS V2  
---|---|---  
**System of record**|  Stripe| Selected Agency Sub-Account  
**Products managed in**|  Stripe| HighLevel through the Agency Sub-Account  
**Primary payment-provider model**|  Stripe| Multiple supported payment providers  
**Plan-change proration**|  Available through supported V1/Stripe workflows| Not supported  
**Monthly ↔ annual changes**|  Handled through supported V1/Stripe subscription workflows| Supported as part of a qualifying upgrade or downgrade  
  
2

## Key Benefits of Understanding SaaS V1 vs SaaS V2

Choosing the architecture that matches your billing requirements helps prevent subscription-management issues later. Understanding the differences also makes it easier to determine where to configure payments, troubleshoot billing, and manage future plan changes.

  * **Billing Clarity:** Know which system owns the subscription and where billing changes should be managed.
  * **Payment Flexibility:** Choose Stripe-based V1 or V2 with a supported Agency Sub-Account payment provider.
  * **Feature Planning:** Identify billing and recovery capabilities that differ between V1 and V2 before onboarding customers.
  * **Accurate Plan Changes:** Understand how upgrades, downgrades, billing intervals, and proration behave for each architecture.
  * **Better Troubleshooting:** Start in Stripe for V1 billing issues or the appropriate Agency Sub-Account for V2 billing issues.


3

## SaaS V1 Architecture

SaaS V1 is the longer-established Stripe-based architecture. Stripe remains the system of record for the SaaS subscription, while HighLevel connects the client sub-account to the applicable SaaS and billing configuration.

  * Stripe is the SaaS V1 system of record.
  * The agency connects Stripe at the agency level.
  * V1 SaaS products and prices originate in Stripe.
  * Stripe-native billing capabilities can be used where supported.
  * Some V1 sales workflows also create a corresponding subscription record inside the sub-account used to sell the subscription.


**Best fit:** SaaS V1 is a strong choice when your agency uses Stripe and relies on Stripe-native billing capabilities or SaaS functionality that is not currently available in V2.

4

## SaaS V2 Architecture

SaaS V2 uses a selected Agency Sub-Account to manage SaaS products, subscriptions, and payment-provider configuration. This enables SaaS billing to operate more directly through HighLevel's Payments and CRM ecosystem instead of relying on Stripe as the subscription system of record.

  * The selected Agency Sub-Account is the SaaS V2 billing system of record.
  * Products and subscriptions are managed through HighLevel.
  * V2 can use multiple supported payment providers configured through the Agency Sub-Account.
  * Subscription activity can integrate more closely with CRM, contacts, workflows, and other HighLevel tools.
  * Monthly and annual billing intervals can be changed as part of a supported plan upgrade or downgrade.


**Proration:** SaaS V2 does not support proration for tier changes, billing-interval changes, or plan changes that combine both.

5

## SaaS V1 Subscription Sync After Plan Changes

Some SaaS V1 subscriptions are sold by importing the Stripe-based SaaS product into a selling sub-account and using that product in a funnel or supported payment flow. These subscriptions can have both the Stripe subscription and a corresponding subscription record in the selling sub-account. Supported SaaS upgrades and downgrades now keep those records aligned.

Before| After a Qualifying V1 Plan Change  
---|---  
Stripe could update while the selling-sub-account subscription retained older plan information.| Stripe and the corresponding selling-sub-account subscription are updated in the same supported plan-change flow.  
The selling-sub-account record could reference an outdated product or price.| The current product and price can remain aligned.  
Invoices generated from stale sub-account information could reference the previous plan.| Downstream invoices can reflect the current synchronized plan information.  
Applicable tax calculations could use older plan information.| When tax is already configured and applicable, current plan information can be used for recalculation.  
  
**Covered V1 pattern:** SaaS plan → Stripe product → product imported into a selling sub-account → subscription sold through that selling sub-account → supported SaaS upgrade or downgrade.

**Not retroactive:** Historical mismatches between Stripe and an existing selling-sub-account subscription are not automatically backfilled. A future qualifying upgrade or downgrade can update both records through the supported synchronization flow.

**Manual Stripe edits:** Do not assume that arbitrary subscription changes made directly in Stripe trigger this synchronization. The bridge is documented for supported SaaS upgrade and downgrade events.

6

## Current Feature Differences

The two architectures do not currently provide identical subscription-management capabilities. Review the differences that matter to your billing model before selecting an architecture for new SaaS plans.

Capability| SaaS V1| SaaS V2  
---|---|---  
**Proration for supported subscription plan changes**|  Available through supported V1/Stripe billing workflows| Not currently supported  
**Coupon/discount deflections during downgrade or cancellation flows**|  Available where supported| Not currently supported  
**Self-service reactivation**|  Available in supported V1 flows| Not currently supported  
**Primary subscription payment-method updates**|  Available through supported V1/Stripe workflows| Not currently supported in the same self-service flow  
**Monthly ↔ annual plan changes**|  Supported through applicable V1/Stripe workflows| Supported as part of a qualifying upgrade or downgrade; no proration  
  
7

## Which SaaS Version Should You Choose?

Neither architecture is universally better. The right choice depends on your payment provider, required subscription-management features, and how closely you want SaaS billing connected to HighLevel's CRM and Payments ecosystem.

### Choose SaaS V1 When

V1 is better suited to agencies that primarily use Stripe and depend on Stripe-native or V1-specific subscription capabilities.

  * Stripe is your preferred SaaS payment processor.
  * You require supported proration workflows.
  * You rely on discount/coupon deflection behavior.
  * You want to use Stripe-native subscription-management capabilities.


### Choose SaaS V2 When

V2 is better suited to agencies that need multi-provider flexibility or want subscription management centered inside an Agency Sub-Account.

  * You want to use a supported provider other than Stripe.
  * You want products and subscriptions managed through HighLevel.
  * You want tighter CRM and workflow integration.
  * You do not rely on the V1-only capabilities listed above.


8

## How To Set Up the Right SaaS Billing Architecture

Selecting the billing architecture before creating and selling plans helps keep products, payment providers, subscription records, and future plan-change behavior consistent. Review the requirements below before configuring your first plan.

  1. **Identify your payment-provider requirement.** If SaaS billing must use Stripe, V1 may fit. If you need another supported provider, review V2.
  2. **Review required billing capabilities.** Confirm whether your workflow depends on proration, deflections, reactivation, or other architecture-specific behavior.
  3. **For V1, connect Stripe at the agency level.** Stripe will remain the SaaS subscription system of record.
  4. **For V2, select an Agency Sub-Account.** Configure the appropriate supported payment provider inside that sub-account.
  5. **Create compatible plan categories and pricing.** Plan hierarchy determines future upgrade and downgrade paths.
  6. **Test the intended checkout and plan-change flow.** Confirm the subscription is created in the expected architecture before scaling the setup.


Screenshot Description

SaaS Configurator showing V1 and V2 plan cards, including the V2 label and associated Agency Sub-Account so users can visually distinguish the two billing architectures.

**Running both architectures:** An agency can maintain existing V1 plans while also creating V2 plans. Each subscription continues to follow the system of record associated with its architecture.

9

## Frequently Asked Questions

Q: Is SaaS V2 replacing SaaS V1?

No. They are separate billing architectures and can operate side by side.

Q: Does the V1 subscription bridge change the V1 system of record?

No. Stripe remains the SaaS V1 system of record. The bridge synchronizes the corresponding selling-sub-account subscription after supported plan changes.

Q: Are old V1 subscription mismatches automatically repaired?

No. Historical mismatches are not automatically backfilled. A future qualifying upgrade or downgrade can update both records.

Q: Can SaaS V2 clients switch between monthly and annual billing?

Yes. Monthly and annual billing intervals can be changed as part of a supported V2 upgrade or downgrade. Proration is not supported.

Q: Will a direct manual change in Stripe always synchronize to the V1 selling-sub-account subscription?

No. Do not assume arbitrary direct Stripe changes invoke the subscription bridge. The synchronization applies to supported SaaS upgrade and downgrade events.

Q: Does the V1 bridge automatically enable Stripe Tax?

No. Stripe Tax and applicable tax configuration must already be enabled and configured. The bridge only helps current plan information stay aligned after a qualifying plan change.

Q: Can an agency use V1 and V2 at the same time?

Yes. V1 and V2 plans can coexist while each subscription continues to use its own billing architecture and system of record.

10

### Related Articles

[ Getting Started with the SaaS Configurator ](<https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator>) [ How to Upgrade or Downgrade a SaaS Plan for a Location ](<https://help.gohighlevel.com/support/solutions/articles/48001207110-how-to-upgrade-saas-plan-for-a-location>) [ How to Configure Downgrade Settings for SaaS Clients ](<https://help.gohighlevel.com/support/solutions/articles/155000006450-how-to-configure-downgrade-settings-for-saas-clients>) [ SaaS Configurator - Modify Plan Category and Plan Level ](<https://help.gohighlevel.com/support/solutions/articles/155000006506>) [ Automatic Tax Calculation with Stripe for SaaS Subscriptions ](<https://help.gohighlevel.com/support/solutions/articles/155000007789-automatic-tax-calculation-with-stripe-for-saas-subscriptions>) [ Special Prices for SaaS Sub-Accounts ](<https://help.gohighlevel.com/support/solutions/articles/155000006380-special-prices-for-saas-sub-accounts>)

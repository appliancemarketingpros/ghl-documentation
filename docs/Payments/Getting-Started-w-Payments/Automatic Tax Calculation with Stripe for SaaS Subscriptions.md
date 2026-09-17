# Automatic Tax Calculation with Stripe for SaaS Subscriptions

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007789-automatic-tax-calculation-with-stripe-for-saas-subscriptions](https://help.gohighlevel.com/support/solutions/articles/155000007789-automatic-tax-calculation-with-stripe-for-saas-subscriptions)  
**Category:** Payments  
**Folder:** Getting Started w/ Payments

---

SaaS • Stripe Tax • Billing

Automatic Tax Calculation with Stripe for SaaS Subscriptions

Automatic Tax Calculation with Stripe helps SaaS V1 agencies calculate applicable taxes using Stripe Tax without maintaining tax rates manually. Agencies can configure tax registrations, product tax codes, tax behavior, and category-level overrides from the SaaS Configurator. For eligible SaaS V1 subscriptions, supported plan changes can also use updated plan information when applicable tax is recalculated.

What You'll Learn

Learn how Stripe Tax works with SaaS V1, configure tax registrations and tax codes, choose inclusive or exclusive pricing behavior, apply category-level overrides, and understand how applicable tax behaves after supported SaaS plan changes.

Important

**Automatic Tax for SaaS subscriptions is available for Stripe-based SaaS V1.** It is not currently supported for SaaS V2 or non-Stripe SaaS payment providers. Enabling or changing tax settings does not retroactively update existing active subscriptions.

Table of Contents

1

What is Automatic Tax Calculation with Stripe?

2

Key Benefits

3

Automatic, Inclusive, and Exclusive Tax Behavior

4

Product Tax Codes for SaaS

5

Category-Level Tax Overrides

6

Tax Recalculation After SaaS V1 Plan Changes

7

How To Set Up Automatic Tax Calculation with Stripe

8

Frequently Asked Questions

9

Related Articles

1

# What is Automatic Tax Calculation with Stripe?

Automatic Tax Calculation with Stripe allows SaaS V1 agencies to use Stripe Tax to calculate applicable tax for SaaS subscriptions. Tax calculations are based on factors such as configured tax registrations, the customer billing address, product tax treatment, and the tax behavior selected for the SaaS offer.

Agencies configure the SaaS tax experience from **SaaS Configurator > Automatic Tax**, while tax registrations are managed through the connected Stripe account. Stripe then performs supported tax calculations during applicable billing events.

**Tax and compliance notice:** HighLevel does not provide tax, legal, or compliance advice. Your agency is responsible for determining where it must register, collect, report, and remit tax. Consult a qualified tax professional for guidance specific to your business and jurisdictions.

2

## Key Benefits of Automatic Tax Calculation with Stripe

Automating applicable tax calculations can reduce manual billing work and provide more consistent tax treatment across supported SaaS transactions. The configuration remains flexible enough to support different tax classifications, pricing strategies, and SaaS categories.

  * **Automated Tax Calculation:** Stripe Tax calculates applicable tax using your registrations, customer information, and selected product tax treatment.
  * **Flexible Pricing:** Choose Automatic, Inclusive, or Exclusive tax behavior based on how you want pricing presented.
  * **Product Classification:** Select a Product Tax Code that helps Stripe determine the appropriate treatment for your SaaS product.
  * **Category-Level Control:** Override global settings for individual SaaS categories when different offers need different tax behavior.
  * **Billing Transparency:** Applicable taxes can be reflected in checkout and billing totals based on the configured tax behavior.
  * **Plan-Change Consistency:** For eligible V1 subscriptions already using applicable tax configuration, supported upgrades and downgrades can use current plan information when tax is recalculated.


3

## Automatic, Inclusive, and Exclusive Tax Behavior

Tax behavior controls whether applicable tax is included in the configured price or added separately. Choosing the correct behavior helps keep displayed pricing consistent with your billing strategy and the markets where you sell.

Tax Behavior| How It Works  
---|---  
**Automatic**|  Uses exclusive pricing in the United States and Canada and inclusive pricing in other supported jurisdictions.  
**Inclusive**|  Applicable tax is included within the displayed price instead of being added on top.  
**Exclusive**|  Applicable tax is calculated separately and added on top of the configured base price.  
  
![SaaS automatic tax settings showing available tax behavior options](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232083/original/Z93B6K2yiVGlCNFXbBhe_ZMga9uH3ZUs3Q.png?1777473608)

4

## Product Tax Codes for SaaS

A Product Tax Code classifies what you sell so Stripe Tax can apply the appropriate tax treatment in supported jurisdictions. Selecting a code that matches your SaaS product is an important part of producing useful automatic tax calculations.

  * Go to **SaaS Configurator > Automatic Tax**.
  * Locate **Product Tax Code**.
  * Choose the tax code that best represents the SaaS product or service you sell.
  * Click **Save**.


**How the code is used:** The code selected in the SaaS Configurator is used by Stripe Tax when determining the applicable tax treatment. Choose the classification based on what you sell and guidance from your tax professional.

![SaaS automatic tax settings showing the Product Tax Code selection](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232027/original/mGhjjkjyrNe0ZOzSAoYfqbZENIulUY7uIg.png?1777473582)

5

## Category-Level Tax Overrides

Category-level overrides let agencies use different tax behavior for specific SaaS categories without changing the global configuration for every plan. An override takes precedence over the default tax settings for the selected category.

  * Scroll to **Category Level Overrides** in the Automatic Tax settings.
  * Select the edit option next to the category you want to customize.
  * Enable or disable tax collection for that category.
  * Choose the desired tax behavior, such as Inclusive, Exclusive, or the default configuration.
  * Save the override.


![SaaS automatic tax settings showing category-level tax overrides](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232126/original/hMo-B2DT7fnyCWgeJrgvl9B1EcHJkcBEBg.png?1777473634)

6

## Tax Recalculation After SaaS V1 Plan Changes

For eligible SaaS V1 subscriptions sold through a selling sub-account, supported upgrades and downgrades can update both the Stripe subscription and the corresponding selling-sub-account subscription. When the subscription is already configured for applicable tax, the updated plan information can be used when tax is recalculated.

Plan-Change Stage| Tax Impact  
---|---  
**Before the supported change**|  The subscription continues using its existing applicable tax configuration and current plan information.  
**Supported upgrade or downgrade**|  The qualifying V1 flow updates the current product and price in Stripe and the corresponding selling-sub-account subscription.  
**Applicable tax recalculation**|  When tax is already configured and applicable, current plan information can be used to determine the updated taxable amount.  
  
**This does not enable tax on an existing subscription.** If Automatic Tax was not already configured for the subscription under the supported tax setup, a plan change should not be treated as automatically enabling Stripe Tax.

**Not retroactive:** Existing subscription, invoice, or tax-data mismatches are not automatically backfilled. The synchronization applies when a qualifying SaaS upgrade or downgrade occurs through the supported flow.

**Manual Stripe changes:** Do not assume arbitrary edits made directly to a Stripe product, price, subscription, or tax setting invoke the selling-sub-account synchronization. The bridge is documented for supported SaaS upgrade and downgrade events.

7

## How To Set Up Automatic Tax Calculation with Stripe

Proper tax configuration starts with enabling Automatic Tax in the SaaS Configurator and then defining the registrations, classification, and pricing behavior Stripe Tax should use. Review the complete configuration before selling new SaaS subscriptions so applicable taxes are calculated from the intended settings.

### Step 1: Enable Automatic Tax Collection

Enabling Automatic Tax makes the SaaS V1 tax configuration available for new or otherwise eligible subscription flows going forward.

  1. From **Agency View** , go to **SaaS Configurator > Automatic Tax**.
  2. Turn **Enable automatic tax collection for SaaS products** ON.


### Step 2: Configure Tax Registrations

Tax registrations identify the jurisdictions where your agency has configured tax collection. These registrations are managed through Stripe and then reflected in the SaaS tax configuration.

  1. Under **Tax Registrations** , click **Manage Tax Registrations**.
  2. Complete or update the applicable registrations in your connected Stripe account.
  3. Return to the SaaS tax settings and confirm the registrations are available.


![Stripe Tax configuration showing tax registration and collection settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070231962/original/LotPwvHAB2eR9tx4AQGJwd-7lBpO72E4Hg.png?1777473531)

### Step 3: Select the Product Tax Code

The Product Tax Code helps Stripe identify what type of product is being sold and determine the applicable treatment in supported jurisdictions.

  1. Locate **Product Tax Code**.
  2. Choose the code that best represents your SaaS product.
  3. Click **Save**.


![Product Tax Code selector for SaaS Automatic Tax](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232027/original/mGhjjkjyrNe0ZOzSAoYfqbZENIulUY7uIg.png?1777473582)

### Step 4: Configure Tax Behavior

The default tax behavior determines whether applicable tax is included in the configured price or added separately when a category-specific override is not present.

  1. Locate **Tax Behaviour**.
  2. Choose **Automatic** , **Inclusive** , or **Exclusive**.
  3. Click **Save**.


![Tax behavior selector showing Automatic, Inclusive, and Exclusive options](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232083/original/Z93B6K2yiVGlCNFXbBhe_ZMga9uH3ZUs3Q.png?1777473608)

### Step 5: Configure Category-Level Overrides

Use an override when one SaaS category needs different tax collection or pricing behavior from the global default.

  1. Scroll to **Category Level Overrides**.
  2. Click the edit icon for the category.
  3. Configure whether tax collection is enabled.
  4. Choose the category's tax behavior.
  5. Save your changes.


![Category Level Overrides for SaaS Automatic Tax](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232126/original/hMo-B2DT7fnyCWgeJrgvl9B1EcHJkcBEBg.png?1777473634)

### Step 6: Test the Checkout Experience

Testing before selling to customers helps confirm that the intended tax configuration, pricing behavior, and totals are being used.

  1. Create a test subscription using the intended SaaS offer.
  2. Use customer information appropriate for the jurisdiction you are testing.
  3. Review the tax amount and final total.
  4. Confirm the displayed result matches the configured Inclusive, Exclusive, or Automatic behavior.


![SaaS checkout displaying calculated tax and the final subscription total](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232160/original/d45e8ZWgq_N8WY0JGS1mOopnDjVB3eKDKg.png?1777473654)

**Existing active subscriptions:** Turning on Automatic Tax or changing the tax configuration does not retroactively rewrite the tax configuration of existing active subscriptions. Tax settings apply according to the supported subscription lifecycle going forward.

8

## Frequently Asked Questions

Q: Is Automatic Tax available for SaaS V2?

No. This SaaS Automatic Tax configuration is currently documented for Stripe-based SaaS V1 and is not available for SaaS V2 or non-Stripe SaaS payment providers.

Q: Does enabling Automatic Tax update all existing active subscriptions?

No. Tax configurations apply going forward and do not retroactively update existing active subscriptions simply because the settings are enabled or changed.

Q: Can an existing V1 subscription have tax recalculated after a plan change?

If an eligible V1 subscription is already using applicable tax configuration, a supported SaaS upgrade or downgrade can use the updated plan information when applicable tax is recalculated. This does not automatically enable tax on subscriptions that were not previously configured for it.

Q: Do historical tax or subscription mismatches get corrected automatically?

No. Historical mismatches are not automatically backfilled. The new synchronization behavior applies to qualifying SaaS plan changes going forward.

Q: Will changing a subscription directly in Stripe trigger the SaaS V1 bridge?

Do not assume that arbitrary direct Stripe changes trigger the selling-sub-account synchronization. The bridge is documented for supported SaaS upgrade and downgrade events.

Q: What happens if I choose the wrong Product Tax Code?

The selected code affects how Stripe Tax classifies the SaaS product. Choose a code that accurately represents what you sell and consult a qualified tax professional if you are unsure which classification applies.

Q: Can different SaaS categories use different tax behavior?

Yes. Category Level Overrides can enable or disable tax collection for a category and apply a category-specific tax behavior that takes precedence over the global default.

9

### Related Articles

[ Configure Automatic Tax Collection for Your SaaS Subscriptions Using Stripe ](<https://help.gohighlevel.com/support/solutions/articles/155000007358-configure-automatic-tax-collection-for-your-saas-subscriptions-using-stripe>) [ Getting Started with the SaaS Configurator ](<https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator>) [ How to Upgrade or Downgrade a SaaS Plan for a Location ](<https://help.gohighlevel.com/support/solutions/articles/48001207110-how-to-upgrade-saas-plan-for-a-location>) [ SaaS V1 vs SaaS V2: What's the Difference? ](<https://help.gohighlevel.com/support/solutions/articles/155000007968-saas-v1-vs-saas-v2-what%E2%80%99s-the-difference->) [ How to Configure Downgrade Settings for SaaS Clients ](<https://help.gohighlevel.com/support/solutions/articles/155000006450-how-to-configure-downgrade-settings-for-saas-clients>) [ Reselling Products - Global Tax Compliance ](<https://help.gohighlevel.com/support/solutions/articles/155000007637-reselling-products-global-tax-compliance>)

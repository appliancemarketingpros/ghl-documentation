# Stripe Troubleshooting | Why is my Stripe Plan not shown in the Funnel Products?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001158124-stripe-troubleshooting-why-is-my-stripe-plan-not-shown-in-the-funnel-products-](https://help.gohighlevel.com/support/solutions/articles/48001158124-stripe-troubleshooting-why-is-my-stripe-plan-not-shown-in-the-funnel-products-)  
**Category:** Sites  
**Folder:** Funnels and Websites

---

Stripe • Funnel Products • Troubleshooting

Stripe Plan Not Showing in Funnel Products: Troubleshooting

Stripe plans must first exist as products inside the HighLevel sub-account where you are building the funnel before they can be selected in supported funnel checkouts. If a Stripe plan is missing, its price may not have been imported yet, may be in Test mode, may already have been imported, or may not qualify for import. This guide explains the current Stripe product-import workflow and the most common reasons a recurring price does not appear.

What You'll Learn

Learn which Stripe prices can be imported, how to import an eligible recurring price into the correct sub-account, how SaaS V1 and SaaS V2 differ, and how to troubleshoot a Stripe plan that is missing from Funnel Products.

Important

The **Import From Stripe** workflow applies to eligible recurring or subscription prices. One-time prices and metered recurring prices cannot be imported through this recurring-price workflow. For SaaS V1 funnel sales, also confirm that the selling sub-account is connected to the same Stripe account used by the agency.

Table of Contents

1\. What Is Importing a Stripe Plan for Funnel Products?  
2\. Key Benefits of Importing Stripe Products  
3\. Prerequisites and Limitations  
4\. SaaS V1 vs. SaaS V2: Which Product Source Should You Use?  
5\. How To Import a Stripe Plan for Funnel Products  
6\. Troubleshooting a Stripe Plan That Does Not Appear  
7\. Frequently Asked Questions  
8\. Related Articles

1

# What Is Importing a Stripe Plan for Funnel Products?

Importing a Stripe plan creates the corresponding HighLevel product and recurring price inside the selected sub-account so the product can be used in supported payment experiences such as funnel order forms.

A product does not become selectable in a funnel simply because it exists in Stripe. The eligible recurring price must first be imported into the same HighLevel sub-account where the funnel is being configured.

For SaaS V1, this workflow is also used when an agency creates a Stripe-based SaaS plan and then imports that SaaS product into the agency-owned selling sub-account before adding it to a funnel or supported payment flow.

2

## Key Benefits of Importing Stripe Products

Importing an eligible Stripe price gives HighLevel the product and pricing information required to use that item within supported checkout experiences in the selected sub-account.

  * **Funnel Availability:** Imported products and recurring prices can be selected in supported funnel order forms.
  * **Centralized Product Management:** Imported products become visible under **Payments → Products** in the applicable sub-account.
  * **Recurring Billing Support:** Eligible recurring Stripe prices can be brought into HighLevel without manually rebuilding the original subscription product.
  * **SaaS V1 Selling Support:** Agencies using the SaaS V1 workflow can import Stripe-based SaaS products into the selling sub-account before selling them through a funnel.


3

## Prerequisites and Limitations

Confirm that the Stripe price meets the current import requirements before troubleshooting the funnel itself. A price that is not eligible for import cannot become available through this workflow.

Requirement| What It Means  
---|---  
**Recurring / Subscription price**|  The Stripe price must use recurring subscription billing.  
**Live mode**|  The price must exist in Stripe Live mode. Test-mode prices are not eligible for the live import workflow.  
**Not metered**|  Metered recurring prices cannot be imported through this workflow.  
**Not previously imported**|  A Stripe price that has already been imported will no longer appear as an available option under **Import From Stripe**.  
**Correct sub-account**|  Import the price into the same sub-account where the funnel will sell the product.  
**SaaS V1 Stripe connection**|  For the SaaS V1 selling-sub-account pattern, the agency and the selling sub-account should use the same Stripe account.  
  
**One-time prices:** One-time Stripe prices cannot be imported through the recurring-price import workflow. Create the applicable one-time product or price directly in HighLevel instead.

4

## SaaS V1 vs. SaaS V2: Which Product Source Should You Use?

SaaS V1 and SaaS V2 use different billing architectures. Identifying which architecture owns the product prevents unnecessary Stripe troubleshooting and ensures you use the correct funnel-product workflow.

Architecture| System of Record| Funnel Product Workflow  
---|---|---  
**SaaS V1**|  Stripe| Import the applicable Stripe SaaS product and price into the selling sub-account, then select it in the funnel.  
**SaaS V2**|  Selected Agency Sub-Account| Confirm the SaaS product exists under **Payments → Products** in the selected Agency Sub-Account, then select it directly in the funnel. Stripe import is not the V2 product-source workflow.  
  
**SaaS V1 subscription-sync note:** Eligible SaaS V1 subscriptions sold through a selling sub-account can now keep the Stripe subscription and corresponding selling-sub-account subscription aligned after supported upgrades or downgrades. This does not replace the initial Stripe product-import requirement, and it does not retroactively repair older mismatches unless a qualifying plan change occurs.

5

## How To Import a Stripe Plan for Funnel Products

Import the eligible Stripe price into the same HighLevel sub-account where the funnel is being configured. After the import completes, confirm the product exists under Payments before adding it to the checkout.

  1. Open the HighLevel sub-account where the product will be sold.
  2. Select **Payments** from the left navigation menu.
  3. Select **Products**.
  4. Click **Import From Stripe**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081130352/original/aXDWiozf0sJe8I-NJFYK5QjPwxdtN4M9pw.png?1789610903)

  5. Search for the applicable Stripe product.
  6. Review the available recurring prices.
  7. Select the eligible product and price you want to import.
  8. Complete the import.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081130354/original/O3i0h-3jl2uwUv2zOkJKgq3n7-3T9BguPw.png?1789610929)

  9. Confirm that the imported product appears under **Payments → Products**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081130313/original/4b9YL8bLTIwpZd56txU9Obk5RVmniXU5YA.png?1789610776)

  10. Select **Sites** from the left navigation menu.
  11. Select **Funnels**.
  12. Open the funnel where the product will be sold.
  13. Open the applicable order form or product configuration.
  14. Select the imported HighLevel product and recurring price.
  15. Save and publish the funnel after its checkout configuration has been tested.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081130369/original/NMFxrBLVuXJrBYRQg3-YWG0J3SUs1R6TWQ.png?1789610960)

6

## Troubleshooting a Stripe Plan That Does Not Appear

Identify where the product is missing before changing its configuration. A plan missing from the Stripe import selector has different causes from a product that has already been imported but is missing from a funnel.

Issue| What To Check  
---|---  
**The price was already imported**|  Previously imported Stripe prices are removed from the available **Import From Stripe** choices. Check **Payments → Products** before assuming the import failed.  
**The price is in Stripe Test mode**|  The import workflow requires an eligible Live-mode Stripe price. A Test-mode price will not appear as the live recurring price used by the funnel.  
**The price is one-time**|  One-time Stripe prices cannot be imported through this recurring-price workflow. Create the applicable one-time product or price directly in HighLevel.  
**The price is metered**|  Metered recurring prices are not supported by the recurring Stripe price import workflow.  
**The product is being imported into the wrong sub-account**|  The product must exist under **Payments → Products** in the same sub-account where the funnel is being configured.  
**The SaaS V1 agency and selling sub-account use different Stripe accounts**|  Compare the Stripe connection under **Agency View → Settings → Stripe** with the Stripe connection under the selling sub-account's **Payments → Integrations**. The supported V1 funnel workflow expects the same Stripe account.  
**The price was changed directly in Stripe**|  Stripe-side pricing changes do not automatically update the corresponding HighLevel product or price. Import the new eligible Stripe price as a new HighLevel product or price according to the supported workflow.  
**A SaaS V1 product was created in the SaaS Configurator but never imported into the selling sub-account**|  Creating a V1 SaaS plan in the agency does not by itself make the Stripe product available in a selling sub-account's funnel. Import the applicable Stripe product into that selling sub-account first.  
**You are using SaaS V2**|  SaaS V2 uses the selected Agency Sub-Account as the system of record. Confirm the product exists in that sub-account rather than troubleshooting the V1 Stripe import path.  
  
**Quick diagnostic:** If you can see the product under **Payments → Products** but not in the funnel, troubleshoot the funnel and confirm you are working in the same sub-account. If you cannot see the price under **Import From Stripe** , verify eligibility, Live mode, prior-import status, and the Stripe account connection first.

7

## Frequently Asked Questions

Q: Why can I see my product in Stripe but not in my funnel?

For the Stripe-based import workflow, the eligible recurring price must first be imported into the applicable HighLevel sub-account. Check **Payments → Products** before configuring the funnel.

Q: Why can't I find my Stripe price under Import From Stripe?

Confirm that the price is recurring, is in Live mode, is not metered, and has not already been imported. For SaaS V1, also confirm the selling sub-account is connected to the correct Stripe account.

Q: Can I import a one-time Stripe price?

Not through the recurring Stripe price import workflow. One-time products or prices should be created directly in HighLevel.

Q: Can I import a metered recurring price?

No. Metered recurring prices are not supported by this Stripe recurring-price import workflow.

Q: I changed the price directly in Stripe. Will the HighLevel product update automatically?

No. Stripe-side pricing changes do not automatically update the corresponding HighLevel price. Import the new eligible Stripe price using the supported import workflow.

Q: Why did a previously imported Stripe price disappear from the import list?

Stripe prices that have already been imported are no longer shown as available import choices. Check **Payments → Products** for the existing product.

Q: Do the agency and selling sub-account need the same Stripe account for SaaS V1?

Yes, for the documented SaaS V1 selling-sub-account funnel workflow, confirm that the Stripe account connected at the agency level matches the Stripe account connected to the selling sub-account.

Q: Does the new SaaS V1 subscription sync make a missing product appear in the funnel?

No. The V1 subscription-sync enhancement applies after supported upgrades or downgrades for eligible subscriptions. The Stripe product still needs to be imported into the selling sub-account before it can be used in the funnel.

Q: Does SaaS V2 use the same Stripe import workflow?

No. SaaS V2 uses the selected Agency Sub-Account as its system of record. Confirm that the product exists in that sub-account's Payments area and select it from the funnel there.

### Related Articles

  * [ Import Products / Price From Stripe ](<https://help.gohighlevel.com/support/solutions/articles/48001202184>)
  * [ Getting Started - Connect Stripe ](<https://help.gohighlevel.com/support/solutions/articles/155000005073>)
  * [ Getting Started with the SaaS Configurator ](<https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator>)
  * [ How to Import Stripe Products into SaaS Configurator ](<https://help.gohighlevel.com/support/solutions/articles/155000006287>)
  * [ SaaS V1 vs SaaS V2: What's the Difference? ](<https://help.gohighlevel.com/support/solutions/articles/155000007968-saas-v1-vs-saas-v2-what-s-the-difference->)
  * [ How to Set Up Products & Start Selling Online ](<https://help.gohighlevel.com/support/solutions/articles/155000005071/>)

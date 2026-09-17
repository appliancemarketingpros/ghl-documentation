# Reselling Products - Global Tax Compliance

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007637-reselling-products-global-tax-compliance](https://help.gohighlevel.com/support/solutions/articles/155000007637-reselling-products-global-tax-compliance)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

Global Tax Compliance for Reselling Products helps agencies configure tax collection, tax invoices, and tax reports for products and services resold to sub-accounts. Powered by Stripe Tax, this feature supports tax handling across 100+ countries from the HighLevel dashboard. This article explains how the feature works, what agencies need before setup, how collection modes and usage tax treatments apply, how taxable products and Stripe Tax Codes are configured, and where to access tax invoices and reports.

* * *

**TABLE OF CONTENTS**

  * What is Global Tax Compliance for Reselling Products?
  * Key Benefits of Global Tax Compliance for Reselling Products
  * Prerequisites
  * Important Tax Responsibility Notice
  * How Stripe Tax Works
  * Collection Modes
  * Tax Treatment on Usage Products
  * Taxable Products and Stripe Tax Codes
  * Global Default Settings
  * Tax Invoices and Reports
  * How To Setup Global Tax Compliance for Reselling Products
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Global Tax Compliance for Reselling Products?**

  

    
    
    **Important:** Tax Remittance Is Your Responsibility. This feature helps you collect and report taxes accurately. Remitting the collected taxes to the relevant tax authorities is the agency's responsibility.
    

  


Global Tax Compliance for Reselling Products helps agencies configure tax collection, tax invoices, and tax reports for products and services resold to sub-accounts. Powered by Stripe Tax, this feature supports tax handling across 100+ countries and helps agencies manage tax settings directly from the HighLevel dashboard.

  


Global Tax Compliance for Reselling Products allows agencies to manage sales tax, VAT, GST, and other applicable tax collection across multiple jurisdictions when reselling products to sub-accounts. It supports US state-level registrations, Canadian province-level registrations, EU VAT, OSS Union, OSS Non-Union, IOSS, and VAT/GST regimes across Asia Pacific, Latin America, the Middle East, and Africa.

  


This feature applies to resold products such as usage-based products, SaaS subscriptions, and marketplace apps. Agencies can collect taxes from sub-accounts on wallet recharges or based on actual monthly usage, manage tax registrations and product tax codes, generate tax invoices, and download tax reports by sub-account and jurisdiction.

* * *

## **Key Benefits of Global Tax Compliance for Reselling Products**

  


  * **100+ Countries Supported:** Configure tax collection across supported Stripe Tax jurisdictions, including US state-level sales tax, Canadian GST/HST/PST by province, EU VAT, OSS Union, OSS Non-Union, IOSS, and VAT/GST regimes across Asia Pacific, Latin America, the Middle East, and Africa.  
  


  * **Stripe Tax-Powered Calculations:** Use Stripe Tax to calculate taxes based on business address, tax registrations, product tax codes, and the sub-account billing address.  
  


  * **Automatic Jurisdiction Sync:** Jurisdictions registered in Stripe Tax sync into HighLevel automatically.  
  


  * **Flexible Collection Modes:** Choose Automatic collection through Stripe Tax or Manual handling outside HighLevel for each jurisdiction.  
  


  * **Usage Tax Treatment Options:** Apply tax when a sub-account recharges its wallet or based on actual monthly usage.  
  


  * **Full Product Coverage:** Configure taxability for usage-based products, SaaS subscriptions, and marketplace apps.  
  


  * **Product Tax Code Mapping:** Map products to Stripe Tax Codes for jurisdiction-level classification.  
  


  * **Global Default Settings:** Configure defaults once so new jurisdictions inherit them automatically.  
  


  * **Tax Invoices and Reports:** Generate invoices per sub-account and jurisdiction, download reports by period, and export reports in bulk ZIP format.  
  


  * **Sub-Account Invoice Access:** Allow sub-accounts to access their own invoices from their billing section.


* * *

## **Prerequisites**

  


Please review the following before configuring Tax Compliance:

  


  1. **All sub-accounts must have a valid billing address:** Tax jurisdiction matching depends entirely on the sub-account's billing address, including a valid zip code. If a sub-account does not have a valid address on file, the system cannot determine which tax rules apply and taxes will not be collected. Make sure all relevant sub-accounts have this configured before enabling tax collection.  
  

  2. **You****must have a connected Stripe account:** Tax Compliance uses Stripe Tax for all tax registration, calculation, and reporting. Your agency's Stripe connected account is required for all tax operations.  
  

  3. **Jurisdictions must be registered in Stripe Tax first:** Before configuring tax collection for a jurisdiction in HighLevel, you must complete the registration for that jurisdiction in Stripe. HighLevel will then sync and display your registered jurisdictions automatically.  
  

  4. **Stripe Tax may have additional charges:** Enabling Automatic collection mode uses Stripe Tax for calculations. Depending on your Stripe plan, Stripe Tax may apply additional per-transaction fees. Review your Stripe plan before enabling automatic mode.


* * *

## **Important Tax Responsibility Notice**

  

    
    
    **Note:** Always **consult a qualified tax advisor** before relying on this feature for compliance purposes. HighLevel and Stripe Tax do not guarantee the accuracy of tax calculations.

  


Tax tools can help automate collection and reporting, but they do not replace professional tax guidance. Agencies are responsible for understanding where they must register, how collected taxes should be verified, and when taxes must be remitted to the appropriate tax authorities.

  


Tax calculations are provided through Stripe Tax, a third-party provider. HighLevel makes no representations, warranties, or guarantees regarding the accuracy, completeness, or reliability of any tax calculations.

  


**Agencies are solely responsible for:**

  


  * Registering with applicable tax authorities

  * Configuring tax registrations in Stripe Tax

  * Verifying all tax calculations before filing or remitting taxes

  * Remitting collected taxes to the correct tax authorities

  * Confirming tax treatment for their products, services, jurisdictions, and business model


* * *

## **How Stripe Tax Works**

  


Stripe Tax determines tax rates by evaluating the agency’s business information, registered jurisdictions, product classifications, and the billing location of the sub-account being charged. This helps automate tax calculation while still requiring the agency to confirm that their tax setup matches their legal obligations.

  


Global Tax Compliance is powered by Stripe Tax. Stripe uses the agency’s business address, tax registrations, product tax codes, and the sub-account’s billing address to determine and apply tax rates on transactions across supported jurisdictions.

  


Stripe maintains tax research resources to monitor law changes across supported countries. HighLevel does not independently verify these rates.

  


Before configuring tax collection for a jurisdiction in HighLevel, complete the registration for that jurisdiction in Stripe Tax. HighLevel then syncs and displays registered jurisdictions automatically.

* * *

## **Collection Modes**

  


Collection modes determine whether HighLevel applies tax automatically through Stripe Tax or whether the agency handles tax outside the platform. Choosing the correct mode is important because it controls whether HighLevel applies tax for a registered jurisdiction.

  


  * **Automatic:** Stripe Tax applies rates to transactions based on the agency’s configuration, tax registrations, product tax codes, and the sub-account’s billing address.  
  


  * **Manual:** HighLevel applies no tax for that jurisdiction. The agency handles tax calculation, collection, invoicing, reporting, and remittance entirely outside HighLevel.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070632977/original/7Y46OAPdSOY5cB6wIlDkhQqs0vjEMVNC7Q.jpeg?1777995840)

* * *

## **Tax Treatment on Usage Products**

  


Usage products can be taxed when wallet funds are added or after actual monthly usage is calculated. The right option depends on how the agency wants to collect tax for usage-based products and how their tax advisor recommends handling wallet-based billing.

  


Treatment| How It Works  
---|---  
**On Recharge**|  Tax is calculated and charged when the sub-account adds funds to their wallet. For example, a $10 top-up at 20% tax means the sub-account is charged $12, with $10 going to the wallet and $2 applied to tax.  
**At Month End**|  Tax is calculated based on actual monthly usage and charged to the wallet at the start of the following month. If the wallet balance is too low, it can go negative and trigger an auto-recharge.  
  
  


If you switch from On Recharge to At Month End, the switch is scheduled for a future date to avoid mid-period disruptions. Both the old and new treatment will have defined date windows showing when each treatment is active.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070630109/original/cBPEft1VKDqleP2pPJBioJdrYMZ6lXv-8w.jpeg?1777994573)

* * *

## **Taxable Products and Stripe Tax Codes**

  


Product taxability controls which resold products are subject to tax in each jurisdiction. Stripe Tax Codes help classify products correctly so Stripe Tax can apply jurisdiction-specific rules based on the product type.

Agencies can configure taxability for:

  


  * Usage-based products, including SMS, WhatsApp, AI, calls, and email

  * SaaS subscriptions

  * Marketplace apps


  


For each jurisdiction, choose which products are taxable. You can use preset tax codes matched from Stripe, customize tax codes per product, or mark specific products as non-taxable.

  


Products can also be configured in Global Settings and overridden per jurisdiction when needed. Jurisdiction-specific settings can have their own collection mode, tax treatment, and product taxability configuration.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070630170/original/ZajZWmsfsie9YpTFBzgFi2ECqZZ-4OVJrg.jpeg?1777994608)

* * *

## **Global Default Settings**

  


Global defaults reduce repetitive setup when agencies collect tax across multiple jurisdictions. New jurisdictions can inherit these defaults automatically, while still allowing agencies to adjust individual jurisdiction settings when needed.

  


Use Global Settings to configure default tax behavior once. New jurisdictions inherit these settings automatically, helping keep collection mode, tax treatment, and product taxability consistent as new registrations are added.  
  


Each jurisdiction can still be configured separately when a specific region requires different tax handling.  
  


![](https://jumpshare.com/share/ndDGMdoPkV6djFCWA660+/Screen+Shot+2026-05-05+at+21.11.51.png)

* * *

## **Tax Invoices and Reports**

  


Tax invoices and reports give agencies the records needed to review collected taxes by sub-account, jurisdiction, and period. These records support reporting workflows, but agencies remain responsible for filing and remitting taxes to the correct authorities.

  


Global Tax Compliance generates tax invoices per sub-account and jurisdiction. Agencies can view tax reporting data in the Tax Reports tab, download individual reports by period, or request a bulk ZIP file sent to their email.

  


Sub-accounts can access their own invoices from their billing section.

  


**Important:** This feature handles tax collection and reporting only. Tax remittance to the relevant tax authorities is the agency’s responsibility.  
  


![](https://jumpshare.com/share/6ZpJBjZkQmhmyAlrcqQC+/Screen+Shot+2026-05-05+at+20.55.42.png)

* * *

## **How To Setup Global Tax Compliance for Reselling Products**

  


Proper setup ensures HighLevel can display registered jurisdictions, apply the selected collection mode, and generate the correct invoice and reporting records. Complete Stripe Tax registration first, then configure each jurisdiction in HighLevel.

  


  


  1. Go to **Agency** **Settings.**  
  
**![](https://jumpshare.com/share/fajkx50IJGp7iucaYydU+/Screen+Shot+2026-05-05+at+19.42.05.png)**  
  


  2. Click on**Stripe > ****Tax Compliance**.  
  
![](https://jumpshare.com/share/dAbN9IVMFJIk3tKmVA35+/Screen+Shot+2026-05-05+at+19.43.44.png)  
  


  3. **Review** the **tax** **jurisdictions** **synced** from **Stripe** **Tax**.  
  


     * These are the jurisdictions you have configured in Stripe Tax.  
  


     * **Learn more from Stripe:** <https://docs.stripe.com/tax/how-tax-works>  
  
![](https://jumpshare.com/share/H9ZxYymVg0fB2W7qqoiw+/Screen+Shot+2026-05-05+at+20.20.50.png)  
  


  4. Click on the **Action** button for the jurisdiction where you want to start collecting taxes.  
  
![](https://jumpshare.com/share/7tCpXrQDYNg6gwo6dKuB+/Screen+Shot+2026-05-05+at+20.23.35.png)  
  


  5. Select the **Collection Mode**.  
  


     * Choose **Automatic** to use Stripe Tax calculations. (**Stripe Charges Apply**)  
  


     * Choose **Manual** if your agency will handle tax calculation, collection, invoicing, reporting, and remittance outside HighLevel.  
  


  6. Click on **Next**.  
  
![](https://jumpshare.com/share/CCUKaopFfXUCIOX5qJOV+/Screen+Shot+2026-05-05+at+20.34.48.png)  
  


  7. Select **Tax Treatment on Usage Products**.  
  


     * Choose **At Wallet Recharge** to apply tax when the sub-account adds funds to their wallet.  
  


     * Choose **At Month End** to apply tax based on actual monthly usage at the start of the following month.  
  


  8. Click on **Next**.  
  
![](https://jumpshare.com/share/NX5aD8AbYCb2VzxvEXvh+/Screen+Shot+2026-05-05+at+20.39.20.png)  
  


  9. Select **Taxable Products**.  
  


     * Use preset Stripe Tax Codes, customize codes per product, or mark products as non-taxable.  
  


     * Choose which products are subject to tax for the jurisdiction.  
  


  10. Click on **Next**.  
  
![](https://jumpshare.com/share/HWVbtibaIoXoi2RRAckg+/Screen+Shot+2026-05-05+at+20.42.48.png)  
  


  11. Complete the **Legal Confirmation**.  
  


     * Read the Terms of Service and legal confirmation.  
  


     * **Check** the "**I understand and agree to the terms outlined above"** box.  
  


     * This acknowledges that tax calculations are handled by Stripe Tax and that HighLevel does not guarantee tax accuracy.  
  


  12. Type **I Agree** (ALL CAPS) and click on **Finish Setup**.  
  
![](https://jumpshare.com/share/jCN7d4GecBXf5X9E5jIC+/Screen+Shot+2026-05-05+at+20.45.27.png)


* * *

## **Frequently Asked Questions**

  


**Q: Which countries and jurisdictions are supported?**

Global Tax Compliance supports 100+ countries through Stripe Tax. US state-level and Canadian province-level registrations are supported with jurisdiction-specific matching logic. Supported regions also include EU VAT, OSS Union, OSS Non-Union, IOSS, and VAT/GST regimes across Asia Pacific, Latin America, the Middle East, and Africa.

  


**Q: Can I have different tax settings for different jurisdictions?**

Yes. Global Settings provide defaults, but each jurisdiction registration can have its own collection mode, tax treatment, and product taxability configuration.

  


**Q: What happens if I switch from On Recharge to At Month End?**

The switch is scheduled for a future date to avoid mid-period disruptions. Both the old and new treatment will have defined date windows showing when each is active.

  


**Q: Can I exempt specific products from tax?**

Yes. In both Global Settings and per-jurisdiction configuration, you can mark specific usage-based products, subscription products, or marketplace apps as non-taxable.

  


**Q: How are tax reports generated?**

Tax reports are automatically generated based on collected tax data. You can view them in the Tax Reports tab, download individual reports, or request a bulk ZIP file sent to your email.

  


**Q: Do I need a Stripe account?**

Yes. Tax Compliance uses Stripe Tax for tax registration, calculation, and reporting. Your agency’s connected Stripe account is required for tax operations.

  


**Q: What if my sub-accounts do not have a billing address?**

Tax jurisdiction matching will not work without a valid billing address, including zip code, on the sub-account. Taxes will not be collected for those sub-accounts until an address is added.

  


**Q: Does HighLevel remit collected taxes for agencies?**

No. Global Tax Compliance helps with tax collection, invoices, and reports. Remitting collected taxes to the relevant tax authorities is the agency’s responsibility.

  


**Q: What happens when a jurisdiction is set to Manual?**

HighLevel applies no tax for that jurisdiction. The agency handles tax calculation, collection, invoicing, reporting, and remittance outside HighLevel.

  


**Q: Can sub-accounts access their own tax invoices?**

Yes. Sub-accounts can access their own invoices from their billing section.

* * *

### **Related Articles**

  


  * [Automatic Tax Calculation with Stripe for SaaS Subscriptions: ](<https://help.gohighlevel.com/en/support/solutions/articles/155000007789>)  
  


  * [Rebilling, Reselling, and Wallets Explained](<https://help.gohighlevel.com/en/support/solutions/articles/155000002095>)

  


  * [How to Manage Stripe Payment Methods inside HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/155000005164>)  
  


  * [How to Configure International Automatic Taxes in HighLevel ](<https://help.gohighlevel.com/en/support/solutions/articles/155000005563>)  
  


  * [Reselling and Rebilling through SaaS V2 Payment Providers](<https://help.gohighlevel.com/en/support/solutions/articles/155000005083>)

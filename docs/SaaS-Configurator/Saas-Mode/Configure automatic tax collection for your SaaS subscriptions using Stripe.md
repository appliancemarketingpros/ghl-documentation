# Configure automatic tax collection for your SaaS subscriptions using Stripe

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007358-configure-automatic-tax-collection-for-your-saas-subscriptions-using-stripe](https://help.gohighlevel.com/support/solutions/articles/155000007358-configure-automatic-tax-collection-for-your-saas-subscriptions-using-stripe)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

This feature allows SaaS agencies on the SaaS V1 (Stripe-based) system to define where taxes are collected, how they are calculated, and whether prices are inclusive or exclusive of tax. All configurations sync directly with Stripe Automatic Taxes and apply to new or reactivated subscriptions going forward.

  

    
    
    This feature is not available for SaaS V2 or non-Stripe payment providers.

  


**TABLE OF CONTENTS**

      * Step 1: Enable Automatic Tax Collection
      * Step 2: Configure Tax Registrations
      * Step 3: Select Product Tax Code
      * Step 4: Configure Tax Behavior
      * Step 5: Configure Category-Level Overrides (Optional)
  * Topic 1: Important Behavior Notes
  * Topic 2: Tax & Compliance Disclaimer


* * *

### **Step 1: Enable Automatic Tax Collection**

  * Navigate to **SaaS Configurator → Automatic Tax**.

  * Toggle **Enable automatic tax collection for SaaS products** to ON.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064754879/original/Jw6c5RKJx5VT7_7vTFwG6oqsECZT1PETzQ.png?1770887932)


  


### **Step 2: Configure Tax Registrations**

  * Under **Tax Registrations** , click **Manage Tax Registrations**.

  * You will be redirected to your connected Stripe account.

  * Add or manage the jurisdictions (countries/states) where you are required to collect taxes.

  * Once configured in Stripe, the registrations will be visible inside HighLevel.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064754901/original/4Ij_0yF8V7tMfzmcrglQO0LziHCiOQalqA.png?1770887947)
    
    
    Stripe automatically calculates taxes based on the customer’s billing address and your registered jurisdictions.

  


### **Step 3: Select Product Tax Code**

  * Under **Product Tax Code** , choose the appropriate tax code from the dropdown.

  * Click **Save**.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064754924/original/MRUKOshVSHro3aGkKl_h2XTMzWlLlydPyQ.png?1770887961)**
    
    
    **The selected tax code determines how Stripe calculates taxes for your SaaS products.
    Choose a tax code based on the type of product you sell and guidance from your local tax consultant.**

  


  


### **Step 4: Configure Tax Behavior**

  * Under **Tax Behaviour** , select your preferred default tax setting:

    * **Automatic** – Uses exclusive pricing in the US & Canada, inclusive pricing in all other jurisdictions.

    * **Inclusive** – Taxes are included in the displayed price.

    * **Exclusive** – Taxes are added on top of the displayed price.

  * Click **Save**.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064754954/original/6TM0ZMg4SKwReBEWPEQkwjiI0CMbRqt6qg.png?1770887988)**

  


### **Step 5: Configure Category-Level Overrides (Optional)**

  * Scroll to **Category Level Overrides**.

  * Click the edit icon next to a category.  
You can:

    * Enable or disable tax collection for that category

    * Customize tax behavior (Inclusive/Exclusive/Default)

  * Save your changes.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064754996/original/SwM6kBUBq_eLhY_4p_JCnwujSeVEtg-pgQ.png?1770887999)**
    
    
    **Overrides here apply only to the selected category and take precedence over global settings.**

* * *

# Topic 1: Important Behavior Notes

  * All tax configurations apply **going forward only**.

  * Existing active subscriptions are **not updated retroactively**.

  * If settings are changed mid-billing cycle, active subscriptions retain their original tax configuration.

  * If a subscription becomes inactive (failed payment/cancellation) and is later reactivated, the **latest tax settings** will apply.

  * This feature is available only for agencies using **Stripe in SaaS V1**. SaaS V2 and other payment providers are not supported.


  


# Topic 2: Tax & Compliance Disclaimer

HighLevel does not provide tax, legal, or compliance advice. Agencies are solely responsible for determining their tax obligations. Please consult a qualified local tax professional to ensure proper configuration based on your jurisdiction and business model.

  


#   


###   


###

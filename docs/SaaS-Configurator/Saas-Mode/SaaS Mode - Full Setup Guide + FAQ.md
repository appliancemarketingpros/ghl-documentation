# SaaS Mode - Full Setup Guide + FAQ

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001184920-saas-mode-full-setup-guide-faq](https://help.gohighlevel.com/support/solutions/articles/48001184920-saas-mode-full-setup-guide-faq)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

HighLevel SaaS Mode allows agencies to sell HighLevel as their own branded software platform while automating subscriptions, billing, onboarding, and account creation.This guide covers the essential setup steps for launching SaaS Mode successfully.

* * *

**TABLE OF CONTENTS**

  * What is SaaS Mode?
  * Why Use SaaS Mode?
  * Agency Setup
  * Special Prices for SaaS Sub-Account
  * Why is my sub-account not created?
  * Frequently Asked Questions
  * Related Articles


  


* * *

## **What is SaaS Mode?**  
  


SaaS Mode allows agencies to:  
  


  * Sell HighLevel under their own brand  
  

  * Create recurring subscription plans  
  

  * Automate sub-account creation  
  

  * Rebill usage and premium services  
  

  * Manage subscriptions directly inside HighLevel


* * *

## **Why Use SaaS Mode?**  
  


Benefits include:  
  


  * White-labeled platform experience  
  

  * Automated recurring billing  
  

  * Subscription management  
  

  * Automated client onboarding  
  

  * Scalable recurring revenue


* * *

# **Agency Setup**  
  


Before selling SaaS plans, complete the following setup steps:  
  


### **Connect Stripe**  
  


Navigate to:  
  


**Agency View → Settings → Stripe Connect**  
  


Connect your Stripe account to enable SaaS billing.  
  


Stripe is currently the only supported payment provider for SaaS Mode.

###   
**Configure SaaS Plans**  


  

    
    
     You can now create SaaS V2 plans directly inside SaaS Configurator with no redirects to an agency sub-account. You can still create or edit V2 plans from the agency sub-account if preferred.

  


Navigate to:  
  


**Agency View → SaaS Configurator**  
  


Inside SaaS Configurator you can:  
  


  * Create SaaS plans  
  

  * Configure pricing  
  

  * Set trial periods  
  

  * Attach snapshots  
  

  * Configure rebilling  
  

  * Enable plan features  
  
  


### **![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070953098/original/5uNxEoxK99qE0I2jzk-se8-_Owlz74320w.gif?1778375780)**

* * *

## **Important Notes**  
  


  * Agencies can create up to 20 SaaS plans  
  

  * SaaS plans should not be deleted directly inside Stripe  
  

  * Stripe card payments are required for SaaS onboarding


* * *

## **Build Your SaaS Sales Page**  
  
**1\. Import SaaS Plans into Your Selling Location**

Navigate to:  
  


**Payments → Products → Import from Stripe**

Copy the Stripe Product/Price ID from SaaS Configurator and import it into your sub-account.

##   
**2\. Create Your Funnel or Website**

  
Navigate to:  
  


**Sites → Funnels**  
  


Then:  
  


  * Create a sales page  
  

  * Add your SaaS products  
  

  * Add a 1-Step or 2-Step Order Form


* * *

# **Special Prices for SaaS Sub-Accounts**  
  


Special Prices allow agencies to create custom pricing for individual sub-accounts without changing their public SaaS plans.

Use cases include:  
  


  * Promotional pricing  
  

  * Enterprise agreements  
  

  * Temporary discounts  
  

  * Legacy pricing


##   
**Create a Special Price**  
  


  1. Open **Manage Client**  
  

  2. Go to the **SaaS** tab  
  

  3. Click **Add a SaaS Subscription**  
  

  4. Select a plan  
  

  5. Click **Create a Special Price**  
  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070953147/original/gMeZpPdKS_TPq8-n8TW67hGbE7zzO7rteQ.png?1778376390)**

  
  


  * Custom amount  
  

  * Currency  
  

  * Billing interval  
  


  7. Click **Save Price**  
  


  * Special Price popup modal screenshot  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070953144/original/UN8FSSVFdt1S1kfQ-8Bjt0Ian1iQcweXUg.png?1778376351)


* * *

## **Reactivating Cancelled Special-Price Subscriptions**  
  


When reactivating a cancelled subscription using a Special Price, the payment modal now correctly displays the configured custom pricing amount.

No additional setup is required.

* * *

## **Updated “Switch to SaaS” Experience**  
  


HighLevel has updated the “Switch to SaaS” experience with:  
  


  * Cleaner visual layout  
  

  * Simplified onboarding guidance  
  

  * Clearer explanation of SaaS benefits  
  

  * Improved activation flow  
  


The SaaS activation process itself remains unchanged.

* * *

## **Troubleshooting**  
  


### **Why is my sub-account not created?**  
  


Possible causes:  
  


  * Product is not a SaaS price  
  

  * Purchase occurred in Stripe test mode  
  

  * PayPal was used  
  

  * Email already exists in HighLevel


* * *

## **Frequently Asked Questions**  
  


**Q: Is Stripe required for SaaS Mode?**  
A: Yes. Stripe is currently the only supported payment provider for SaaS subscriptions.  
  


**Q: Can I create custom pricing for a specific client?**  
A: Yes. Use Special Prices during SaaS activation.  
  


**Q: Will reactivated subscriptions display the correct Special Price amount?**  
A: Yes. Reactivated subscriptions now correctly display the configured custom price.  
  


**Q: Can clients upgrade or downgrade plans later?**  
A: Yes. Plans can be managed through Company Billing or Manage Client.  
  


**Q: Did the SaaS activation process change?**  
A: No. The setup flow remains the same. The update only refreshes the onboarding experience.

##   


* * *

## **Related Articles**  
  


  * [Convert Existing Sub-Account to SaaS Mode Subscription](<https://help.gohighlevel.com/en/support/solutions/articles/48001188055>)  
  

  * [How to Upgrade/Downgrade a SaaS Plan for a Location](<https://help.gohighlevel.com/en/support/solutions/articles/48001207110>)


#

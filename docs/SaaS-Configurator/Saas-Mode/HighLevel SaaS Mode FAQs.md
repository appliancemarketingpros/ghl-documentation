# HighLevel SaaS Mode FAQs

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002129-highlevel-saas-mode-faqs](https://help.gohighlevel.com/support/solutions/articles/155000002129-highlevel-saas-mode-faqs)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

This guide covers common questions related to billing, SaaS configuration, sub-accounts, payments, and verification.

* * *

**TABLE OF CONTENTS**

  * Billing & Wallet
    * Q. How do I delete the last card from the billing page?
    * Q. Why do card changes reflect across multiple sub-accounts?
    * Q. Why can’t the client add payment details?
    * Q. Why can’t Indian clients add payment details?
    * Q. Why are auto-recharges failing?
    * Q. What happens when SaaS is disabled?
  * Welcome Email
    * Q. Why are custom values not populated?
    * Q. What is the default subject of the welcome email?
    * Q. Why is the default email sent instead of my custom email?
    * Q. Who receives the welcome email?
    * Q. How do I fix the wrong sub-account for welcome email?
  * Sub-Accounts & Subscriptions
    * Q. Why are duplicate sub-accounts created?
    * Q. Why aren’t sub-accounts created via funnels?
    * Q. How do I move a subscription between sub-accounts?
    * Q. Why can’t I upgrade a plan?
    * Q. How do I transfer SaaS accounts to another agency?
  * SaaS Configurator & Plans
    * Q. Why is “Invalid price currency” shown?
    * Q. How do I disconnect Stripe Connect?
    * Q. Why can’t I disconnect Stripe (error about active clients)?
    * Q. Why are SaaS V1 or V2 plans not visible?
    * Q. What is the difference between SaaS V1 and V2?
    * Q. Can I use SaaS V1 and V2 together?
  * Security & Verification
    * Q. Why is 2FA required even if turned off?
    * Q. Why is rebilling not enabled / not moved to LC?
    * Q. Why is the sub-account showing “Manual Verification Pending”?
    * Q. Why is the sub-account “Paused due to pending approval”?
  * Dashboard & Visibility
    * Q. Why is the Agency Dashboard not visible?


* * *

## **Billing & Wallet**

  


### **Q. How do I delete the last card from the billing page?**

  


If only one card is present, it cannot be removed from the sub-account billing page.

  


Workarounds:

  


  * Delete the card directly from Stripe (if you have access to the customer)  
  

  * For SaaS V2, card management may only be available at the agency level


  


  


### **Q. Why do card changes reflect across multiple sub-accounts?**

  


This happens when multiple sub-accounts share the same Stripe Customer ID.

  


Solution: Assign different Stripe customers per sub-account:

  


  * Disable SaaS for the sub-account  
  

  * Re-enable using:  
  

    * Share link  
  

    * Request via SMS/email


  


### **Q. Why can’t the client add payment details?**

  


**Common errors:**

  


  * No such customer  
  

  * stripe.confirmPayment()...


  


**Possible reasons:**

  


  * Stripe customer was deleted  
  

  * Stripe account was changed  
  

  * Sub-account transferred between agencies


  


**Solution:**

  * Disable and re-enable SaaS to recreate mapping


  


  


### **Q. Why can’t Indian clients add payment details?**

  


Due to RBI regulations, a billing address is required.

  


**Solution** : Add billing address in Stripe dashboard

  


  


### **Q. Why are auto-recharges failing?**

  


Auto-recharge does not support 3DS-only cards.

  


**Solution** :

  


  * Use a card that supports 3DS but is not 3DS-only  
  

  * Alternatively, use manual recharge


  


  


### **Q. What happens when SaaS is disabled?**

  


  * Subscription is cancelled  
  

  * Wallet is permanently deleted  
  

  * Agency must handle refunds manually  
  


After disabling:

  


  * Agency receives wallet balance via email  
  

  * Can refund or add credits manually


  


  


## **Welcome Email**

  


### **Q. Why are custom values not populated?**

  


Custom values must be configured in:  
  
SaaS Configurator → Advanced Settings. Direct edits in sub-accounts are not supported.

  


  


### **Q. What is the default subject of the welcome email?**

  


"Activate your account"

  


  


### **Q. Why is the default email sent instead of my custom email?**

  


This happens if the template is missing from: [Do Not Edit] SaaS Configurator Templates

  


**Solution** :

  


  * Reset Agency Welcome Email (via support)


  


  


### **Q. Who receives the welcome email?**

  


All newly created users in a sub-account.

  


  


### **Q. How do I fix the wrong sub-account for welcome email?**

  


Reset the Agency Welcome Email via support

* * *

## **Sub-Accounts & Subscriptions**

  


### **Q. Why are duplicate sub-accounts created?**

  


When purchases are made via:

  


  * Stripe  
  

  * Funnels  
  

  * Sale links


  


A new sub-account is created automatically.

  


To avoid this: Use manage Client page for existing accounts.

  


  


### **Q. Why aren’t sub-accounts created via funnels?**

  


Check if the product is tagged as an Agency Plan.

  


Notes: Test mode purchases do not create sub-accounts

  


  


### **Q. How do I move a subscription between sub-accounts?**

  1. Ensure both sub-accounts use the same Stripe customer  
  

  2. Disable SaaS (without cancelling subscription) on source account  
  

  3. Reload target account → subscription attaches automatically


  


  


### **Q. Why can’t I upgrade a plan?**

  


The sub-account may already be on the highest plan in its category.

  


Q. Why can’t I switch between monthly and annual SaaS plans?

  


For SaaS V2 subscriptions, billing interval changes are not currently supported on existing subscriptions.

  


Supported SaaS V2 plan changes:

  
Monthly → Monthly

  


Yearly → Yearly

  


Not supported for SaaS V2:

  


Monthly → Yearly

  
Yearly → Monthly

  


These options are hidden in the upgrade flow to prevent incorrect billing. This limitation applies only to SaaS V2 subscriptions. SaaS V1 subscriptions are unaffected because Stripe manages interval changes natively.

###   
**Q. How do I transfer SaaS accounts to another agency?**

  


  1. Disable SaaS for all sub-accounts  
  

  2. Transfer sub-accounts  
  

  3. Handle wallet balances manually


* * *

## **SaaS Configurator & Plans**

  


### **Q. Why is “Invalid price currency” shown?**

  


**Occurs when:**

  


  * Price currency ≠ category currency


  


**Fix** :

  * Update price in SaaS Configurator  
  

  * Then update currency in Stripe


  


**Note** :

  


  * Currency cannot be changed if:  
  

    * Sale links exist  
  

    * Active subscriptions exist


  


  


### **Q. How do I disconnect Stripe Connect?**

  


Stripe cannot be disconnected if active SaaS billing depends on it.

  


**Steps** :  
  


  1. Go to Agency Settings → Stripe Connect  
  

  2. Identify blocked sub-accounts  
  

  3. Disable SaaS for those accounts  
  

  4. Retry disconnect


### **  
**

### **Q. Why can’t I disconnect Stripe (error about active clients)?**

  


SaaS is still enabled on sub-accounts using that Stripe account

  


**Solution** : Disable SaaS for all affected sub-accounts first

  


  


### **Q. Why are SaaS V1 or V2 plans not visible?**

  


This depends on selection during SaaS setup:

  


  * Stripe selected → SaaS V1  
  

  * Agency Sub-account selected → SaaS V2


  


**Fix** :

  


  * Disable SaaS  
  

  * Re-enable with correct option


  


  


### **Q. What is the difference between SaaS V1 and V2?**

  


**SaaS V1:**

  


  * Stripe only  
  

  * Configured at agency level


  


**SaaS V2:**

  


  * Multiple providers (Stripe, NMI, Authorize.net, Square)  
  

  * Configured per sub-account


  


  


### **Q. Can I use SaaS V1 and V2 together?**

  


No. A sub-account can only use one mode at a time.

  


  


**Q. Why can’t I switch between monthly and annual plans?**

  


  * SaaS V1: Allows switching  
  

  * SaaS V2: Only same billing interval allowed


* * *

## **Security & Verification**

  


### **Q. Why is 2FA required even if turned off?**

  


  * Email verification is mandatory  
  

  * Only phone verification can be disabled


  


  


### **Q. Why is rebilling not enabled / not moved to LC?**

  


Because the account is in verification pending state.

  


**Fix** :

  * Complete verification (email/phone)  
  

  * Or manually verify via Manage Client


  


  


### **Q. Why is the sub-account showing “Manual Verification Pending”?**

  


This is due to:

  


  * Pending email/phone verification (not pause setting)


  


**Important** :

  


  * Does NOT block access  
  

  * Required during first phone number purchase


  


  


### **Q. Why is the sub-account “Paused due to pending approval”?**

  


This is controlled by:SaaS Configurator → Security → Pause new sub-accounts

  


**Solution** :  
  


  * Approve or reject from:  

    * Manage Client page  
  

    * Requests section


* * *

## **Dashboard & Visibility**

  


### **Q. Why is the Agency Dashboard not visible?**

  


Controlled by visibility setting:

  


  * Only Me → Only owner can see  
  

  * All Admins → All admins can see


  


**Fix** :

  * Update in: Agency Settings → Stripe


* * *

**Need More Help?** If your issue isn’t listed: Contact Support

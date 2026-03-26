# Set Up Your MarketplacApp Pricing

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001217-set-up-your-marketplacapp-pricing](https://help.gohighlevel.com/support/solutions/articles/155000001217-set-up-your-marketplacapp-pricing)  
**Category:** Developer Resources  
**Folder:** Developer Resources

---

Monetizing your app on the Highlevel developer app marketplace presents various avenues. This guide walks you through the options and tells you how to set them up.

* * *

**TABLE OF CONTENTS**

  * Where can I configure my app's pricing?
  * Select payment collection preference (Within the Highlevel platform, recommended)
  * External payment page (Not recommended) 
  * What pricing models can I offer?
  * How to use it as a Developer?
  * How to Use it as an Agency
  * Reselling & markup behavior (agencies)
  * Distribution Types and Pricing Models
  * Offering Free-trial
  * Key Points to Remember
  * Usage-based pricing 
  * How your earnings are calculated
  * Earnings Dashboard
  * Payout
  * Frequently Asked Questions


* * *

## **Where can I configure my app's pricing?**

  


Log in to your [Marketplace - Developer account](<https://marketplace.gohighlevel.com/>), click on your app and select the 'Pricing' option from the left menu.

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034622435/original/xppr0jO6LqPc7JuWCYBN4KN_bAw8tnB5Ng.png?1728892235)**

* * *

## **Select payment collection preference (Within the Highlevel platform, recommended)**

  


This method permits customers (both agencies and sub-accounts) to pay for the app within the HighLevel platform. We handle the payment processing and ensure timely payouts to developers.

  


  1. Enable agencies to re-sell these apps to their end sub-accounts, enhancing wider adoption and engagement for your app  
  

  2. Use granular pricing modules offered by HighLevel Marketplace platform such as free-trials, etc.  
  

  3. Streamlined collection and reconciliation of payments.


* * *

## **External payment page (Not recommended)**

  


If you'd rather manage your app's pricing on your platform, choose this option and provide the redirect URL for your external payment page. Customers will get redirected to your payment page during the installation process and upon successful payment the app will be installed in their account.

  


Add the redirect URL for the payment page.

  


**Note:**

  * Initially selecting an external payment page allows for later changes to the Highlevel platform. But, once live with internal payment collection, you cannot switch to an external page. Such a change necessitates deleting and recreating the app.  
  

  * Agencies cannot resell apps with external payment preference, which reduces your app's adoption chances.


* * *

## **What pricing models can I offer?**

  


Your app can have one of three pricing models, all of which are configurable using Pricing Plans:

  


  1. Free
  2. Paid - Subscription
  3. Paid - One-time
  4. Freemium - Combination of Free and Paid plans  
  


You can optionally offer Free-trials on any of the above pricing models.

* * *

## **How to use it as a Developer?**

  


**A) Configure your billing meter**

  * Go to App → Pricing → Billing Meters and create (or edit) a meter with Module Type = Custom Event (API).  
  

  * Set Price Type: Dynamic  
  

  * Enter Minimum and Maximum price, add a Pricing Page URL (recommended for transparency), and set a Default Price per Unit.  
  

  * Save changes.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155059526643/original/nmVf0EJvUoU0PbD-X8eIrV5hPcXzjBtr2Q.png?1764452995)

  


B) Charge the wallet via API

  * Use the existing[ Create Wallet Charge API](<https://marketplace.gohighlevel.com/docs/ghl/marketplace/charge>). Include the new, optional price field when you want to apply a dynamic per-unit price for that charge.  
  

  * If price is omitted, the meter’s Default Price per Unit is applied.


* * *

## **How to Use it as an Agency**

  


  * In your app’s Pricing section, end users see the price range for dynamic meters and a link to the Pricing Page URL.  
  

  * **Visibility note** : The Pricing Page URL is visible to agency admins only, not to sub-accounts.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155059526677/original/9gvj0eyVVzq4GNTd2fNZb-C20RIZyxma6g.png?1764453310)

* * *

## **Reselling & markup behavior (agencies)**

  


  * Agencies can configure a flat per-unit markup when reselling apps' service (app reselling).  
  

  * Because markups change effective end pricing, the Pricing Page URL is hidden from sub-accounts to avoid confusion.  
  

  * Example: If an SMS base price is $1.00 (UK) and $1.50 (France), an agency can add a $0.50 markup so sub-accounts pay $1.50 (UK) and $2.00 (France).


  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155059526690/original/aqMQVwqhOu3K2FAyWm_D72UFuNyeitDvzg.png?1764453401)**

* * *

## **Distribution Types and Pricing Models**

  


To understand distribution types, [**please refer to this article**](<https://help.gohighlevel.com/support/solutions/articles/155000002141-marketplace-app-distribution-type#Summary>).

  


In this section, let's understand how you may customise your distribution type based on who you want to charge.

Let's assume that the agency in the following example has set a flat 5% markup on all Marketplace Apps.

  


**Distribution Model**| **App Pricing Model (with example)**| **Agency pays**| **Sub-account Pays to agency**| **Developer Makes**  
---|---|---|---|---  
**Target User: Agency**|  Monthly: $50/month| $50/month| -| $50/month  
One-time: $50| $50 One-time| -| $50 One-time  
**Target User: Sub-account |**  
**Who can install? : Agency & Sub-account**| Monthly: $10/month| $10/month| $10.5/month**  
**| $10/month  
One-time: $10| $10 One-time| $10.5 One-time| $10 One-time  
**  
Target User: Sub-account |  
Who can install? : Agency Only**  
**  
**| Monthly: $50/month|  $50/month| **-**|  $50/month  
One-time: $50| $50 One-time| -| $50 One-time  
**Differential pricing enabled**  
** _(Monthly)_**  
  
Agency Price:$50/month  
  
Sub-account Price:  
$10/month| $50/month  
+  
$10/month per sub-account| $10.5/month| **$50/month  
+  
$10/month per sub-account  
**  
**Differential pricing enabled**  
** _(One-Time)_**  
  
Agency Price:$50  
  
Sub-account Price:  
$10| $50 One-time  
+  
$10 One-time per sub-account| $10.5 One-time| $50 One-time  
+  
$10 One-time per sub-account  
  
##   


Here's how you setup differential pricing for apps with **Target User: Sub-account |****Who can install? : Agency Only:**

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034686628/original/mS_pY98lXhO1D7j7bF6F8mqCrHdO73QlDQ.jpeg?1728959419)**

* * *

## **Offering Free-trial**

**  
**

**  
**

**  
**

**  
**

Drive adoption of your app by offering free-trial - full-experience of the app for a limited duration of time.

You can offer anywhere between 1 - 90 days of free-trial to your users.

**  
**

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030099991/original/hIs1ghkZosk4Ne8nnEWigzGTJZ-RgcSo_g.png?1722327989)**

  


**  
**

The subscription will initiate automatically after the trial period ends.

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030100131/original/mqhcRPfmMCy3Mc65safT30BwLlJ67uS2OA.png?1722328082)**

* * *

## **Key Points to Remember**

  


  1. Free trial config is at the app-level, and applies to all pricing plans in your app.  
  

  2. A user can avail free trial only once per app within a period of 90 days.  
  

  3. Your users will receive a notification a 24 hours before the trial period ends giving them a heads-up about the upcoming charges.  
  

  4. In case of payment failures after free-trial, GHL will notify the users and try to charge them again for 3 consecutive days. After 3 consecutive days of payment-failure, the app will be uninstalled from the user's account.  
  

  5. You can track free-trial period through [AppInstall webhook](<https://highlevel.stoplight.io/docs/integrations/889f37581bd0e-o-auth-2-0>) and [Get Installed Locations API](<https://highlevel.stoplight.io/docs/integrations/aeed19d08490e-get-location-where-app-is-installed>).


* * *

## **Usage-based pricing**

  


**[](<mailto:marketplace@gohighlevel.com\]>)**

Here's a loom demonstrating the steps to configure Usage-based pricing on your marketplace apps.

  


  


  


If your app has service whose price may vary, you can opt for dynamic pricing option.

  


  


  

    
    
    **IMPORTANT** : **[Here's the link to API Docs for Usage-based Pricing](<https://marketplace.gohighlevel.com/docs/ghl/marketplace/wallet-charges>).**

* * *

## **How your earnings are calculated**

  


Your revenue stems from app installations on the Highlevel platform. We currently do not deduct any commission. You receive the entire payment from our customers. However, agencies can markup the price when reselling to sub-accounts. For instance:

  


Say, a Sub-account app is priced as follows:

  * Developer Pricing: $10/month
  * Agency Resale Price: $12/month


  


Here's how the resultant transactions when a sub-account installs the app:

  * Sub-account Charge: $12/month
  * Agency Charge: $10/month
  * Developer Earnings: $10/month


* * *

## **Earnings Dashboard**

  


Track your revenue in the 'Earnings Dashboard'. For a live, paid app:

  


  * Total Earnings: Cumulative earnings till date.  
  

  * Total Installs: Number of app installations.  
  

  * Active Accounts: Current active/installed accounts.  
  

  * Use the table below for detailed insights and apply filters as needed.


  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155010503781/original/5iwskODmD8lq09A6MWsLX3qzs2iJB7TQIQ.png?1697694564)**

* * *

## **Payout**

  


We've partnered with Tipalti to facilitate developer payouts, ensuring you have a smooth and efficient transaction process.

  


### **How Does the Payout Process Work?**

  


  * Developer partners who are eligible for a payout will receive an email invitation to register with Tipalti. This 3-step registration process guides you through everything necessary to ensure compliance and to receive payouts from us.  
  

  * After your account is set up and ready, you will begin receiving payouts from Highlevel. The billing cycle is monthly, with payments sent on the 15th of each month for all earnings accrued in the previous month.


  
If you've already set up Tipalti and your payment status is marked as "submitted," then your payout is in process. Depending on your chosen payout method, you should expect to see the payment within 1-3 days.

  


To know more about how this works, click here - [Tipalti Payout Process](<https://help.gohighlevel.com/support/solutions/articles/48001208136-affiliate-payouts-where-how-when-can-i-get-paid->) [](<https://help.gohighlevel.com/support/solutions/articles/48001208136-affiliate-payouts-where-how-when-can-i-get-paid->)**[](<https://help.gohighlevel.com/support/solutions/articles/48001208136-affiliate-payouts-where-how-when-can-i-get-paid->)[](<https://help.gohighlevel.com/support/solutions/articles/48001208136-affiliate-payouts-where-how-when-can-i-get-paid->)[](<https://help.gohighlevel.com/support/solutions/articles/48001208136-affiliate-payouts-where-how-when-can-i-get-paid->)**

* * *

## **Frequently Asked Questions**

  


**Q: What is the purpose of the new “price” parameter in the API?**

It enables developers to set a dynamic per-unit charge during a billing event, allowing pricing to reflect current, variable service costs.

  


  


**Q: What happens if the “price” parameter is omitted from the API call?**

The system defaults to the Default Price per Unit previously configured for the billing meter.

  


  


**Q: How do agencies benefit from dynamic pricing?**

Agencies can use dynamic pricing to display a clear price range and configure flat markups on services, ensuring transparent and competitive pricing for sub-accounts.

  


  


**Q: Who can view the Pricing Page URL?**

The Pricing Page URL is visible solely to agency administrators, keeping pricing details clear and preventing confusion among sub-accounts.

  


  


**Q: Can dynamic pricing be applied to services beyond SMS?**

Yes, dynamic pricing is ideal for any service with variable costs, including telephony and other geo-based APIs.

  


  


**Q: What steps are involved in setting up a dynamic billing meter?**

You must configure the meter in HighLevel by selecting Dynamic as the Price Type, entering pricing limits and a Pricing Page URL, and integrating the updated API with the optional “price” parameter.

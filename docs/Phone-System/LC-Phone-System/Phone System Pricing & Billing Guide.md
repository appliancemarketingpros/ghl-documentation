# Phone System Pricing & Billing Guide

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001223556-phone-system-pricing-billing-guide](https://help.gohighlevel.com/support/solutions/articles/48001223556-phone-system-pricing-billing-guide)  
**Category:** Phone System  
**Folder:** LC Phone System

---

This guide outlines the full pricing structure for the native Phone system within HighLevel. It covers everything from phone number costs, SMS/MMS messaging, voice calling rates, and carrier passthrough fees, to rebilling options for agencies using SaaS mode. However, the pricing for our Phone System is the same amount as Twilio. All the prices shown for our Phone features are listed in USD. 

* * *

**TABLE OF CONTENTS**

  * Pricing Based on the Most Used Product Categories
    * Phone Numbers
    * Messaging Service - SMS
    * Messaging Service - MMS
    * Voice Calls
    * Number Intelligence
    * Other Charges
  * Frequently Asked Questions
  * Related Articles


* * *

## **Pricing Based on the Most Used Product Categories**

  


This pricing guide outlines costs based on the most commonly used Phone product categories — including local/toll-free numbers, messaging (SMS/MMS), voice calls, and optional rebilling charges for SaaS agencies.

  


**Please Note: A list of country-specific prices PDFs are attached at the bottom of the page.**

  


### **1\. Phone Numbers**

  


All the phone numbers are charged monthly based on the number types. Below is the list of pricing for different number types available in the US/Canada:

  


  1. Local Numbers: $1.15 / month  
  

  2. Toll-Free Numbers: $2.15 / month


  


For all the other countries, please refer to the country-specific pricing PDFs attached at the bottom of the page.

  


### **2\. Messaging Service - SMS**

  


The SMS pricing is based on the number of segments a message has, the pricing in US/Canada is as follows:

  


Country| Outbound SMS  
Pricing are based / segment| Inbound SMS  
Pricing are based / segment  
---|---|---  
US| $0.00747 | $0.00747   
Canada| $0.00747 | $0.00747   
  
  


**Note: The above charges include a 10% discount on the $0.0083 list price.  
**  
This pricing is both for the local and toll-free numbers. For all the other countries, the pricing will also be based on Twilio's pricing. (Please refer to the attached PDF at the bottom of the page).

  


### **3\. Messaging Service - MMS**

  
The MMS pricing is based on the number of segments a message comprising of, the pricing for US/Canada and Australia are as follows: 

  


  


Country| Outbound MMS  
Pricing are based / segment| Inbound MMS  
Pricing are based / segment  
---|---|---  
US| $0.0220| $0.0165 (Local Numbers)  
$0.0200 (Toll-free Numbers)  
Canada| $0.0220| $0.0165 (Local Numbers)  
$0.0200 (Toll-free Numbers)  
Australia| $0.3500| $0.3500 (Local Numbers)  
$0.3500 (Toll-free Numbers)  
  
  


  


For all the other countries, the pricing will also be based on Twilio's pricing.  
(Please refer to the attached PDF at the bottom of the page).

  


### 

Tip: For calculating segments and understanding more about how to calculate the per SMS and MMS cost, refer to How to Calculate SMS and MMS Costs

  


### **4\. Voice Calls**

  


The cost of voice calls depends on call duration (per minute). Below is a detailed breakdown for US and Canada.

  


**Outbound Calls**

  
Total Cost: $0.0166 per minute

  
**Breakdown:**  
  


  * Outbound USA: $0.0126/min  
  
(includes 10% discount on list price of $0.014)  
  

  * Client Minutes: $0.004/min


  


**Inbound Calls**

  
Inbound calls generally consist of two legs:  
  


  1. Incoming call to your HighLevel number (from the caller)  
  

  2. Forwarded call to wherever you answer it , e.g., web, mobile, desk phone, or another number


  
Charges apply for both legs, depending on where you answer.

  


If Answered on Web, Mobile, or Deskphone

  
Total Cost: $0.01165 per minute

  


**Breakdown:  
**

  * Incoming Call (USA): $0.00765/min  
  
(includes 10% discount on list price of $0.0085)  
  

  * Client Minutes: $0.004/min


  
**Note: Voice AI calls may add $0.004/min if the provider uses SIP infrastructure.**

  


If Answered on a USA Forwarding Number

  
Total Cost: $0.02 per minute

  
**Breakdown:  
**

  * Incoming Call (USA): $0.00765/min  
  

  * Outgoing Call (to your forwarding number): $0.0126/min


  


**Explanation:**  
  
If you forward your HighLevel number to a US phone number or any other phone number you’ll pay for both the incoming and outgoing portions of the call.

  


**Note- The above example illustrates pricing for a US number. Actual rates vary by country based on Twilio’s pricing**

  


**Important Notes**  
  


  * **International Forwarding:  
**  
If you forward incomming call to an international number (e.g., UK mobile), the second leg follows Twilio’s international rates, which are higher.  
  
View Twilio’s Local, Mobile, and Toll-Free International Rates  
  

  * **Regional Exceptions:  
**  
Calls to Alaska and Yukon Territory follow Twilio’s regional pricing and are not billed at the standard US/Canada rates.  
  

  * **Other Countries:  
**  
For all other regions, pricing is based on Twilio’s international call rates.  
  

  * **Billing Rounding:  
**  
Calls are billed in full minutes.  
  
Any partial minute is rounded up to the next whole minute.  
  

  * Call Reporting: Reports display the exact call duration, even if billing rounds up.  
  


  * **Example:  
**

Type| Number of Calls| Actual Duration in call reports| Billed Duration  
---|---|---|---  
Example| 2 calls| 45 seconds each (1m 30s total)| 2 minutes total  
  
> Summary:  
> Call reporting shows precise durations for transparency, while billing uses the rounded-up minute for calculation.


  


**Please Note:** The outbound calls have 2 legs so the cost of an outbound call will be $0.0180 ($0.014 for Outbound call + $0.004 for the webApp/MobileApp leg which dialer uses to initiate the call (Client Minutes))

  


### **5\. Number Intelligence**

  


Number Intelligence is a bundle of three functions. All three are turned on/off together, refer to Number Intelligence - Number Validation, Spam Detection, and Unknown Caller

  


  * **Number Validation ($0.005/call):** Before sending an SMS, check if the number is valid, if invalid do not send the SMS.  
  

  * **Spam Detection ($0.005/test):** When receiving an incoming US call, test it for spam, mark is "spam likely" if it fails the test.  
  

  * **Name Lookup ($0.01/lookup):** When receiving an incoming US call, if the number is not on a contact or the contact name is empty, look up the caller's name.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155046385293/original/IOcn1VJ_JgjQlfYevr5Wtxu-qwGaCbGz3w.png?1746791119)

  


  


### Number Format Lookups: All the number formats look up to support calls are free of cost.  
  
**6\. A2P Pricing**

  


Here’s how A2P Brand and Campaign registration fees apply for both Low Volume and High Volume campaigns:

  


Type| One-Time Brand & Campaign Registration Fee| Monthly Campaign Fee| Daily Segment Limit| Notes  
---|---|---|---|---  
Low Volume (LV)| $24.49875(includes $3 Fast Track fee)| $11.025 per campaign| 6,000 segments/day| For smaller businesses or limited messaging volumes.  
High Volume (HV)| $71.90625(includes $3 Fast Track fee)| $11.025 per campaign| 600,000 segments/day| For frequent or large-scale messaging use cases.  
  
>   
> 
> 
> Important:
> 
>   * Monthly campaign fees are determined by The Campaign Registry (TCR) and apply as soon as the campaign is reviewed, regardless of whether it is approved or rejected. Users must delete the campaign if they do not wish to continue being charged.  
>   
> 
>   * The $3 Fast Track fee ensures faster campaign approval and is included in the one-time registration cost.
> 


  
New: A2P campaign resubmissions are now free. The $15 A2p resubmission charge has been removed. You can resubmit a campaign at no cost while addressing carrier feedback. However, the following fields cannot be edited during resubmission:  
  


  * Campaign use-case  
  

  * Opt-in message  
  


If you need to update any of these fields, you’ll need to create a new campaign, which will be charged as usual.

  


Please note: While resubmissions are free, Campaigns rejected due to disallowed content may be subject to applicable charges. 

###   


### **7\. 5% Markup on Select Categories**

  


Certain pricing categories carry a **5% markup applied at the location level**. This markup is added on top of the base cost for the following categories and is not subject to the standard configured rebilling structure.

### **Categories with 5% Markup**

Category| Description  
---|---  
**SMS Carrier Fees**|  The 5% markup applies on top of all SMS carrier surcharges passed through from the recipient's carrier (AT&T, T-Mobile, Verizon, etc.)  
**MMS Carrier Fees**|  The 5% markup applies on top of all MMS carrier surcharges, including fees for both inbound and outbound MMS messages  
**A2P Registration Fees**|  The 5% markup applies to both the one-time Brand & Campaign registration fees and the ongoing monthly campaign fees for Low Volume and High Volume campaigns  
**Verified Caller ID**|  The 5% markup applies to Verified Caller ID charges. Note: This is a billing-only category and is not part of the standard usage categories  
**RCS Messaging Carrier Fees**|  The 5% markup applies to any carrier fees associated with RCS (Rich Communication Services) messaging  
  
### **How the 5% Markup Works**

  * The markup is applied **at the location level** , meaning it is calculated and added per sub-account/location.
  * This markup is **separate from configured rebilling**. Unlike usage categories that follow the rebilling configuration, these five categories always carry the fixed 5% surcharge regardless of other rebilling settings.
  * The 5% is calculated on the **base cost** of the applicable charge before being billed to the location.  
  


**Example:**

If the SMS carrier fee for a message to an AT&T subscriber is $0.0035 (outbound), the amount billed after the 5% markup would be:

> $0.0035 × 1.05 = **$0.003675**

Similarly, if a Low Volume A2P Brand & Campaign registration fee is $24.49875, the amount billed with the markup applied would be:

> $24.49875 × 1.05 = **$25.7237**

###  What Is NOT Included in the 5% Markup

The following categories are governed by **configured rebilling** rather than the flat 5% markup:

  * Transcription
  * Amazon Polly (Text-to-Speech)
  * Chat users / Group messaging users
  * Answering machine detection
  * Number validation
  * Incoming call spam intelligence
  * Call recording
  * Caller ID lookup
  * Carrier lookups
  * All inbound and outbound calls (voice)
  * All inbound and outbound SMS/MMS messages
  * IVR calls, Workflow calls, Voicemail drops
  * Phone numbers (Local, Toll-Free, Mobile)


###   
**8\. Other Charges**

  


Below are some additional categories that are also charged at the same price as Twilio:

  


  * Client Minutes for Calling ($0.004 per minute, already included in the outgoing call charges shared above, SaaS rebilling applies)  
  

  * Call Recording ($0.0025 per minute of recording, SaaS rebilling applies)  
  

  * Call Recording storage ($0.0005 per minute of recording per month, SaaS rebilling applies)  
  

  * Call Transcription ($0.024 per minute, SaaS rebilling applies)  
  

  * Answering Machine Detection ($0.0075 per call where it is used, SaaS rebilling applies)  
  

  * Voicemail drops ($0.0180 / minute, SaaS rebilling applies, same charge as an outgoing call)  
  

  * Conference Calls ($0.0018 - $0.0040 per minute per participant depending on region used, SaaS rebilling applies)  
  

    * **US:** $0.0018 /participant/minute  
  

    * **Dublin:** $0.0025 /participant/minute  
  

    * **Tokyo:** $0.0030 /participant/minute  
  

    * **Singapore:** $0.0030 /participant/minute  
  

    * **Sydney:** $0.0030 /participant/minute  
  

    * **Sau Paulo:** $0.0040 /participant/minute  
  

    * Conference Call charges are only applied for warm transferred calls, workflow calls  
  

  * **Carrier Charges  
**
    1. SMS carrier fees are charges that are applied by the recipients carrier to the sender, These charges + SMS charge is the total cost to send an SMS. Some carriers charge fees on long code SMS (messages sent from a 10-digit US/Canada number). Other carriers only charge fees for SMS sent from a Short code number.  
  

    2. There are additional carrier fees per message that are automatically applied based on the end-user's destination and carrier.  
  
Carrier| SMS Outbound*| SMS Inbound*| MMS Outbound*| MMS Inbound*  
---|---|---|---|---  
AT&T| $0.0035| $0.0035| $0.0090| $0.0090  
T-Mobile| $0.0045| $0.0025| $0.0100| $0.0100  
Verizon| $0.0045| $0.0070| $0.0070| -  
US Cellular| $0.0050| $0.0100| $0.0100| $0.0100  
All other carriers| $0.0040| $0.0100| $0.0100| -  


  


  * Amazon Polly Text-to-Speech charges (The new, enhanced speech feature costs US$0.00084 per 100 characters of text).


* * *

## **Frequently Asked Questions**

  


**Q: Why am I being charged for incoming SMS?  
**

The native phone system charges for both inbound and outbound SMS at the same rate  
  
**Q.Will SaaS re-billing work if I move sub-accounts on the native Phone System?**

Yes, SaaS rebilling will continue to work with the native Phone System.

  


**Q. Which all categories have a 10% discount applicable?**

  * Phone Numbers [Only US and Canada] [For all types of numbers]
  * SMS [Only from US/Canada to US/Canada] [For both Inbound and Outbound]
  * Voice Calls [Only from US/Canada to US/Canada] [For both Incoming and Outgoing Calls] [Excluding products mentioned in Other Charges]


  


**Q. I was billed $20 right away. However, I haven't called anyone yet and have only created one phone number. Is this expected?**

Yes, the wallet would have auto-recharged as soon as the balance is below the amount set in the wallet configurator.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155005564786/original/LsyKT0vWYm4k7X1MIzIZo8qANAZpZCjRAg.png?1692383874)

  


**Q.Will I be charged if I encounter an error when sending an SMS?**

If there's an internal error with the native Phone system before the message is handed off to the phone provider, you won't be charged. However, charges apply to every message where a delivery attempt has been made, regardless of the final delivery status. This includes messages sent from toll-free numbers, A2P numbers, and those not deliverable due to country restrictions or other factors. We urge users to be fully informed and cautious before sending messages, as refunds will not be provided for undelivered SMS.

  


**Q. Why am I getting charged for Call Recording Storage even though I didn't record calls recently?**

Any Call Recording stored incurs storage charges. This means older call recordings also incur these storage charges. 

Call Recording Storage is billed daily per sub-account (instead of once at month-end). Your total monthly amount should not change—only the billing frequency has changed. You may see one Call Recording Storage transaction per day, and during the initial switch you may see multiple “catch-up” transactions for prior days.

If you want to avoid these charges:  
  


  * Retain recent call recordings and delete older ones using the feature "Automatically Delete Older Recordings" under Sub-account settings > Phone Numbers > Advanced Settings > Voice Calls > Call Recording  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155052319944/original/6bu5Rpi3Tvbe1A7uJHPFW4AwnlFO_mRSXQ.png?1756137193)  
  

  * Delete all call recordings to avoid all storage charges. Set the time period in the above feature to 1 day and disable call recording for future calls


  


**Q. Why do I pay for Conference Call charges for all outgoing calls (even the ones without call transfer)?**

Our outgoing call flow is optimized to be seamless, with lower waiting times and quicker transfers. Thus, we initiate a Conference Call for all outgoing calls as per our standard call flow implementation.  
  


**Q. Does the 5% markup apply in addition to the configured rebilling?**

The 5% markup applies to a specific set of categories (SMS carrier fees, MMS carrier fees, A2P registration fees, Verified Caller ID, and RCS messaging carrier fees) at the location level. These are separate from the usage categories that fall under configured rebilling. If a category is under configured rebilling, the 5% markup does not apply to it.

* * *

## **Related Articles**  
**  
**

  * [What is LC (Lead Connector) Phone System?](<https://help.gohighlevel.com/en/support/solutions/articles/48001223546>)  
  

  * [How do I migrate my agency and sub-account over to LC Phone?](<https://help.gohighlevel.com/en/support/solutions/articles/48001204027>)  
  

  * [Regulatory Bundle and Address Creation for Sub-Accounts](<https://help.gohighlevel.com/en/support/solutions/articles/48001213216>)  
  

  * [Toll-Free Number Verification Guide for LC - Phone (US/Canada)](<https://help.gohighlevel.com/en/support/solutions/articles/48001222300>)  
  

  * [LC - Phone Messaging Policy](<https://help.gohighlevel.com/en/support/solutions/articles/48001213941>)


Attachments (3)

[ csv Sms_Pricing.csv  
55 KB ](</helpdesk/attachments/155069176114>)

[ csv NumbersPricing_Updated.csv  
8.55 KB ](</helpdesk/attachments/155069177045>)

[ numbers Voice_Pricing.numbers  
403 KB ](</helpdesk/attachments/155073522625>)

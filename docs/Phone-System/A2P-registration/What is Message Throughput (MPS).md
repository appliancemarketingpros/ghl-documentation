# What is Message Throughput (MPS)?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004527-what-is-message-throughput-mps-](https://help.gohighlevel.com/support/solutions/articles/155000004527-what-is-message-throughput-mps-)  
**Category:** Phone System  
**Folder:** A2P registration

---

A2P 10DLC message throughput is the speed at which SMS message segments can be sent through an approved Campaign using registered 10-digit numbers in the United States. It is measured in**message segments per second** **(MPS).** Most short SMS messages count as one segment, while longer messages, emojis, or special characters may use multiple segments. Throughput affects how fast messages are sent, but it does not guarantee delivery or prevent carrier filtering.

* * *

**TABLE OF CONTENTS**

  * What is A2P 10DLC Throughput
    * How Trust Scores Affect Throughput
    * Throughput, Queues, and Sending Delays
    * Throughput by Brand Type
    * Standard Brand Throughput
    * Mixed and Marketing Campaign Throughput
    * Low Volume Standard Brand Throughput
    * Sole Proprietor Brand Throughput
    * Account-Based Rate Limits
    * How To Check A2P Brand and Campaign Information in HighLevel
    * How To Improve Throughput Readiness
    * Frequently Asked Questions
    * Related Articles


* * *

# **What is A2P 10DLC Throughput**

  


A2P 10DLC throughput applies to businesses sending SMS over registered U.S. 10-digit long code (10DLC) numbers.

Common use cases include:

  * Appointment reminders

  * Marketing campaigns

  * Lead follow-ups

  * Customer notifications

  * Review requests

  * Two-factor authentication

  * Account updates  
  


Toll-Free messaging, international messaging, and Canadian 10DLC messaging may follow different rules depending on number type, route, and destination.

* * *

## ******How Trust Scores Affect Throughput**

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074636089/original/gAGa2GuaO161LhNJpB_TGuu2ibi7QR57bQ.png?1782515536)

  


A Trust Score is a score assigned during **Standard Brand** registration with The Campaign Registry (TCR - the 3rd party that administers the US wireless carriers' new registration system). Trust Scores apply to Standard Brands and help determine available throughput. Higher Trust Scores may qualify for higher throughput.  
  


Trust Scores may be influenced by:

  * Legal business name accuracy

  * EIN or Tax ID match

  * Business address consistency

  * Website quality

  * Privacy Policy and Terms of Service availability

  * Brand footprint

  * Consistency between submitted and public business information  
  


    
    
    HighLevel does not assign or manually change Trust Scores.

* * *

## **Throughput, Queues, and Sending Delays**

  
The following diagram provides a visual overview of how message throughput, queuing, and delivery work together during high-volume sending.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074637125/original/qcPAElX3SAldvUIvDWvcNy83T0XXa4ZYcg.png?1782519985)

* * *

## **Throughput by Brand Type**

  
Brand type determines which throughput rules apply. The following tables show the maximum approved SMS throughput for each Brand type and Campaign type. Identify whether the account uses a Standard Brand, Low Volume Standard Brand, or Sole Proprietor Brand before reviewing the tables.

* * *

## **Standard Brand Throughput**

  


Standard Brands are registered businesses using an EIN or Tax ID. Throughput is determined by Campaign type and, when applicable, Trust Score.  
  


Trust Score| Total SMS MPS Toward Major U.S. Networks| AT&T SMS MPS| T-Mobile SMS MPS| Verizon SMS MPS  
---|---|---|---|---  
75–100| 225| 75| 75| 75  
50–74| 120| 40| 40| 40  
1–49| 12| 4| 4| 4  
0 / Low Volume Standard Brand| 12| 4| 4| 4  
  
  


Messages to US Cellular are based on major network throughput up to 8 MPS. Messages to other minor U.S. carriers are 1 MPS per phone number.

* * *

## **Mixed and Marketing Campaign Throughput**

  


Trust Score| Total SMS MPS Toward Major U.S. Networks| AT&T SMS MPS| T-Mobile SMS MPS| Verizon SMS MPS  
---|---|---|---|---  
75–100| 225| 75| 75| 75  
50–74| 120| 40| 40| 40  
1–49| 12| 4| 4| 4  
0 / Low Volume Standard Brand| 12| 4| 4| 4  
Low Volume Mixed Campaign, regardless of Trust Score| 3.75| 1.25| 1.25| 1.25  
  
  


Messages to US Cellular are based on major network throughput up to 8 MPS. Messages to other minor U.S. carriers are 1 MPS per phone number.

* * *

## **Low Volume Standard Brand Throughput**

  


Low Volume Standard Brand registration is for businesses with an EIN or Tax ID and lower SMS volume needs.

Low Volume Standard Brands have fixed lower throughput and do not receive the same throughput potential as fully vetted Standard Brands.

* * *

## **Sole Proprietor Brand Throughput**

  


Sole Proprietor Brand registration is for individuals or small businesses without an EIN or Tax ID. This path does not use Trust Score-based throughput. Sole Proprietor Brands use fixed throughput limits and are intended for lower-volume messaging.  
  


Total SMS MPS Toward Major U.S. Networks| AT&T SMS MPS| T-Mobile SMS MPS| Verizon SMS MPS  
---|---|---|---  
2.25| 0.25| 1 per number| 1 per number  
  
* * *

## **Account-Based Rate Limits**

  


Account-based rate limits may cap total sending speed across multiple Campaigns.

  1. For example, if several Campaigns each have approved throughput but the account-level limit is lower than the combined total, the account-level limit controls total sending speed. Messages above that rate may queue.


* * *

## **How To Check A2P Brand and Campaign Information in HighLevel**

  


  1. Go to **Settings.**

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074964168/original/vzqHZGOPSOWgLEPeHNrPzsh4J3CPDkpwOA.png?1782915791)  
  

  2. Open**Phone System > Trust Center,** review your A2P registration details, then open Brands & Campaigns to check Brand status, Campaign status, use case, and any required fixes.  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074964453/original/9OCvdN8bf08-v9Iz5VsPM9LbJG00Yv-ByQ.png?1782915919)**


* * *

## **How To Improve Throughput Readiness**

  
Accurate registration details help carriers evaluate your Brand and Campaign. Use these best practices:  
  


  1. Match the legal business name to EIN or Tax ID records.

  2. Use the correct business address and contact information.

  3. Make sure the website represents the business.

  4. Add a visible Privacy Policy.

  5. Add visible Terms of Service.

  6. Explain how contacts opt in to SMS.

  7. Match sample messages to the Campaign use case.

  8. Choose the accurate use case, not the highest-throughput option.

  9. Resolve required fixes before resubmitting.


* * *

## **Frequently Asked Questions**

  


**Q : Does a higher Trust Score guarantee delivery?**  
No. Delivery also depends on consent, content, filtering, DND, opt-outs, and recipient status.  
  


**Q : Does MMS use the same throughput?**  
MMS may be handled differently because media size, carrier handling, and formatting can affect processing.

  


**Q : Does this apply outside the United States?**  
This article focuses on U.S. A2P 10DLC long-code messaging. Other countries or routes may have different rules.  
  


**Q : Does Toll-Free Messaging use these limits?**  
No. Toll-Free messaging uses a separate registration and throughput model.  
  


**Q : Does LC Phone use these limits?**  
If LC Phone sends SMS through A2P 10DLC long-code routes, A2P throughput rules may apply.  
  


**Q : Does adding more phone numbers increase throughput?**  
Not automatically. Throughput is generally assigned at the Campaign level.

* * *

## **Related Articles**

  


  * [](<https://help.gohighlevel.com/support/solutions/folders/155000000021?utm_source=chatgpt.com>)[What is A2P 10 DLC: Brand and Campaign Registration](<https://help.gohighlevel.com/en/support/solutions/articles/155000002380>)  
  

  * [Registering Your A2P Brand](<https://help.gohighlevel.com/en/support/solutions/articles/155000008140>)  
  

  * [A2P Campaign Registration: Step by Step Guide and FAQs](<https://help.gohighlevel.com/support/solutions/articles/155000004539-a2p-campaign-registration-step-by-step-guide-and-faqs?utm_source=chatgpt.com>)  
  

  * [A2P 10DLC Campaign Use Cases](<https://help.gohighlevel.com/support/solutions/articles/155000000235-a2p-10dlc-campaign-use-cases?utm_source=chatgpt.com>)  
  

  * [A2P 10DLC Brand Approval Best Practices](<https://help.gohighlevel.com/support/solutions/articles/155000000508-a2p-10dlc-brand-approval-best-practices?utm_source=chatgpt.com>)  
  

  * [A2P 10DLC Messaging Fees: Registration, Monthly, and Carrier Costs](<https://help.gohighlevel.com/support/solutions/articles/155000005200-a2p-10dlc-messaging-fees-registration-monthly-and-carrier-costs?utm_source=chatgpt.com>)

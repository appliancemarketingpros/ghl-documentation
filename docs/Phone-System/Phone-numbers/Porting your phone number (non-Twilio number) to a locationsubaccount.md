# Porting your phone number (non-Twilio number) to a location/subaccount

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001211919-porting-your-phone-number-non-twilio-number-to-a-location-subaccount](https://help.gohighlevel.com/support/solutions/articles/48001211919-porting-your-phone-number-non-twilio-number-to-a-location-subaccount)  
**Category:** Phone System  
**Folder:** Phone numbers

---

This guide is for bringing a number from an **external carrier** (not already on Twilio) into a **HighLevel Location** (sub‑account). It covers what to gather, how to submit the port request, and what to do on the cut‑over day.

Please prepare the information mentioned in the article and complete the **[Porting Form](<https://link.gohighlevel.com/widget/form/qX47XEC8HsDtrGkmbjFQ>).**

  

    
    
    **IMPORTANT** : We are currently able to port in numbers from the **United States only**. For any other country's porting please refer to [Let's port your phone number](<https://twlo.my.salesforce-sites.com/InternationalPorting>). If a Letter of Authorization (LOA) is required, use this [template](<https://docs.google.com/document/d/1RITNwdQukTgXIp9KOUbFexLr8GdlW3yy2g-nLvI_Aps/edit?tab=t.0>).
    This process typically takes **2-4 weeks** , and we will provide updates via **email**.

  


* * *

**TABLE OF CONTENTS**

  * What is Porting? 
  * Prerequisites
  * What Counts as an Acceptable Billing Statement
  * If You Are Porting a Google Voice Number
  * If You Are Porting a Landline or VoIP Number
  * Decide Your Destination Carrier (Important)
  * Submit Your Port Request
    * Step 1: Gather documents
    * Step 2: Complete the High-Level Porting Form (US numbers)
    * Step 3: Approval & FOC (Firm Order Commitment)
  * After the Port — Compliance & Deliverability
  * Frequently Asked Questions


* * *

## **What is Porting?**

  


Porting a number is the transfer of a phone number between two telecom service providers. The process involves providing the right documentation to prove ownership of the number as well as the execution of the transfer between the current provider and the new provider. 

  


When you’re ready to port your number, you’ll just need to send us a signed Letter of Authorization (LOA) that matches the service information your current carrier has on file. Once you submit your LOA, we’ll handle coordination with your current carrier to complete the port. 

  


The porting process takes between two and four weeks from when you submit the required documentation for port requests of fewer than 50 numbers and six to eight weeks for larger, more complex ports. During this process, you’ll have full access to your phone number, as there is no downtime associated with porting a phone number. 

  


You can find the[ Porting form here. ](<https://link.gohighlevel.com/widget/form/qX47XEC8HsDtrGkmbjFQ>)

* * *

## **Prerequisites**

  


  * **Location ID** for the destination sub‑account (where the number will live).  
  


  * **Account details with your current carrier** (account #, PIN / last 4 SSN for wireless, service address).  
  


  * **Recent phone bill** (PDF; must be legible).  
  


  * **Letter of Authorization (LOA)** signed by the **authorized person** on the account (typically within the last 15–30 days, see country notes).  
  


  * **Customer Service Record** (or equivalent) from your current carrier.


  

    
    
    **IMPORTANT PLEASE READ**  
      
     1. All Wireless Numbers REQUIRE a Pin for Port Requests. Providing a incorrect or fake pin in this box will cause the port request to be rejected by our carrier.  
      
    3. Please double check with your provider to make sure your wireless number has a pin and the pin is correct to avoid delays in the number porting process  
      
    4. If you are porting multiple numbers. Please check if there are multiple unique pins per number, if your carrier/provider allows a single pin for multiple numbers please note this in the wireless number pin field above.  
      
    5. Landline and Toll Free Port Request may not need a pin

  


  

    
    
    **Please Note:** **Name & address must match** your carrier records exactly. PO Boxes are not accepted as service addresses.

* * *

## **What Counts as an Acceptable Billing Statement**

  


  * A billing statement is a document from your current phone provider that shows your account ownership and the phone number(s) you want to port.  
  


  * Accepted documents include a PDF bill, an invoice, or an account summary page from your provider portal—as long as it clearly shows the required details.


* * *

## **If You Are Porting a Google Voice Number**

  
If your number is registered with **Google Voice** , please take a **screenshot** of your Google Voice settings page.  
Make sure the screenshot includes:  
  


  * Your **phone number** , and  
  


  * Your **email address**  
  


### 
    
    
     Make sure the screenshot is not cropped and shows the full browser/app page header where the Google account/email is visible

  


### **Minimum Required Fields**

  


  * Phone number(s) being ported  
  


  * Account owner’s name  
  


  * Provider name (your current carrier)  
  


  * Statement date (must be within the last 90 days)


* * *

## **If You Are Porting a Landline or VoIP Number**

  
If you’re porting a **Landline or VoIP number** , please provide your **latest monthly billing statement** from your current provider.  
  
Your document must include:  
  


  * The **phone number(s)** you’re attempting to port  
  


  * The **account owner’s name**


###   
**Additional Requirements**

  


  * The billing statement **must not be older than 90 days**.  
  


  * The **latest billing statement** is preferred for faster processing.  
  


  * If your provider doesn’t issue a bill, you may submit:  
  


    * A **receipt of your phone number purchase** , or  
  


    * A **screenshot from your account portal** showing the phone number(s) and owner’s name.  
  


  * If you’re porting multiple numbers, **a separate billing statement for each number** is preferred.


* * *

## **Decide Your Destination Carrier (Important)**

  


Not sure which you’re on? In your Location, go to **Settings → Phone System**. If you see **LC Phone** branding and no Twilio SID, you’re on LC Phone. If you see **Twilio Account SID/Auth Token** , you’re on Twilio.

  


  1. **LC Phone (LeadConnector)** — Choose this option if your Location Currently uses LC Phone or you want HighLevel to host/operate the number. Our team submits the port with our carrier partners and keeps you updated.  
  


  2. **Twilio** — Choose this if your Location is connected to **your own Twilio project/sub‑account**. Our team submits the port to **Twilio** for you (you’ll still manage A2P/Toll‑Free and webhooks in Twilio after the port).


* * *

## **Submit Your Port Request**

  


The LC Phone porting form currently accepts United States numbers only. For international ports, use Twilio International Porting (or use the [Twilio](<https://twlo.my.salesforce-sites.com/InternationalPorting>) path and submit via the Twilio interface).

  


### _**Step 1:** Gather documents_

  


  1. **LOA (Letter of Authorization)** — signed by the authorized person.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054088072/original/p8t77kH58TytiJCfz2_KPn1CSL11YbTg5g.png?1758222144)

  
**Note** \- The **company name field** (as shown in the screenshot) on the **LOA** can be **left blank**.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155058842655/original/V_oYDFgRxSYGkU7SwhxqzMDOuQTepdCtLw.png?1763638695)

  


  2. **Latest phone bill** — clear/legible **PDF** , provided by the phone carrier.  
  


  3. **List of numbers to port** — in **E.164** format (e.g., `+15551234567`).  
  


  4. **Location ID** — destination sub‑account. _(Find it in the Location:_**_Settings → Business Profile_** _.)_  
  
_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054088147/original/x_YH0z1VALLLlkJeQKy9xQErsE4uQaYjwA.png?1758222300)_  


  5. **Carrier account details** — account # and **PIN/Passcode** for any **wireless** numbers.


  


  


### _**Step 2:** Complete the High-Level Porting Form (US numbers)_

  


  * **Agency Relationship Number.**

  * **Contact name + email** (support updates go to this email).  
  


  * **Location ID** (destination).  
  


  * **Customer/Business legal name** and **service address** — must match the carrier’s records exactly.  
  


  * **Landline/Toll‑Free numbers** (if any).  
  


  * **Wireless numbers** (if any) + **Account # + PIN/Last 4 SSN**.  
  


  * **Upload required PDFs:** LOA and Billing Statements.


  


After filling in the required information, check the consent boxes and submit the porting form. Expect a brief service impact during the port window. Keep the old carrier active until completion.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054088581/original/RaM3J1q1AfqHnQ-1Jd-KLOz6H_vDkdDgDQ.png?1758222739)

  


  

    
    
    **Please Note:** Your Letter of Authorization and Billing Statement(s) must be **PDF** files and cannot exceed **4MB**.

  


  


### _**Step 3:** Approval & FOC (Firm Order Commitment)_

  


  * After submission, you’ll receive **status updates via email**.  
  


  * When approved, the carrier issues a **FOC date/time window**. Same‑day or date‑specific ports are **not guaranteed**.


* * *

## **After the Port — Compliance & Deliverability**

  


After your number ports in, complete the checks below to ensure calls and messages flow reliably and aren’t blocked.

  


  * **A2P 10DLC (US 10‑digit local SMS):** Your messaging numbers must be registered to an **approved Brand & Campaign**. Unregistered traffic to US handsets is blocked by carriers.  
  

  * **Toll‑Free (US/CA):** Complete **Toll‑Free Verification** before sending messaging at scale. New verification submissions are adding extra business fields; see our Toll‑Free guide for current requirements.  
  


  * **International:** Ensure any required **Regulatory Bundles/Addresses** are approved to avoid call/SMS failures.


* * *

## **Frequently Asked Questions**

  


  


**Q. Where can I find the porting form?**

Here is a link to the [Porting Form.](<https://link.gohighlevel.com/widget/form/qX47XEC8HsDtrGkmbjFQ>)

  


  


**Q. Can you port on a specific date/time?**  
Carriers do not guarantee exact dates/times. We’ll request preferences where available and confirm the port window once the carrier issues **FOC**.

  


  


**Q. Will SMS history move with the number?**  
No. Porting moves the number; it does not migrate historic logs/conversations. Export any critical history from your prior provider.

  


  


**Q. Can I change destination (LC Phone ↔ Twilio) after I submit?**  
No, the request once submitted cannot be changed. However, reach out to HighLevel support for any assistance.

  


  


**Q. Do I need to cancel my old carrier?**  
Only after the port completes and you’ve verified calls/messages are working in HighLevel.

# Avoid Call Loops When Routing Calls to Internal Phone Numbers

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007297-avoid-call-loops-when-routing-calls-to-internal-phone-numbers](https://help.gohighlevel.com/support/solutions/articles/155000007297-avoid-call-loops-when-routing-calls-to-internal-phone-numbers)  
**Category:** Phone System  
**Folder:** LC Phone System

---

This article explains why call loops occur, where HighLevel displays warnings, and how to configure call routing to help prevent failed or disconnected calls.

  


**TABLE OF CONTENTS**

  * How Call Loops Can Occur?
  * Why This Matters
  * Warning Behavior
  * Warning Message
  * Where You’ll See This Warning
  * Recommended Best Practices


* * *

# **How Call Loops Can Occur?**

  


HighLevel gives you the flexibility to use your **HighLevel (GHL) phone number** across different parts of your account, including as your **business phone number** and in advanced call routing setups. This allows experienced users to design custom call flows that fit their specific use cases.

  


That said, certain configurations, such as using a GHL phone number as a **call forwarding destination,** can unintentionally create call loops if not set up correctly. These loops may cause some calls to fail or disconnect.

  


To help you stay informed without limiting your flexibility, HighLevel now displays a **warning message** in places where using a GHL phone number could potentially lead to call issues. This way, you can proceed confidently while understanding the possible impact of your setup.

* * *

## **Why This Matters**

  


A call loop occurs when a call is repeatedly routed back into the same phone system instead of reaching its intended destination. Understanding this behavior helps you avoid routing configurations that may interrupt inbound calls.

  


A call loop may result in:

  


  * Calls failing to connect  
  

  * Calls disconnecting unexpectedly  
  

  * Inbound calls not reaching the intended recipient


  


Advanced routing configurations can still use HighLevel phone numbers when appropriate, but the call flow must be configured carefully to prevent calls from being routed back to the same number.

* * *

## **Warning Behavior**

  


HighLevel uses an informational warning rather than blocking the configuration entirely. This allows you to continue using advanced routing setups while making you aware of the potential risk before saving your changes.

  


### Warning Message

  


The warning displayed when a potential call-loop configuration is detected states:

  


Using your CRM phone number here may cause some calls to fail because it can create a call loop. Learn more

  

    
    
    **Note:** The warning is informational only and does not prevent you from saving your settings.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063655402/original/MzNef-iZi8FVagb9RHSjU1O16NK2o0eRWg.png?1769593232)

* * *

## **Where You’ll See This Warning**

  


The warning appears when you attempt to use a **HighLevel phone number** in the following areas:

  


  * **Phone Number Settings** (Call Forwarding)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064142083/original/I32GuMvd7eNfYys2LwnYmsxbJ0fr0yKN0A.png?1770190760)  
  


  * **Business Profile** (Business Phone Number)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064145873/original/wla5TqCjgtzBd1pKHWjPlpXC0-owI63K_Q.png?1770193469)  
  


  * **Staff Profile** (User Phone Number)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064145024/original/nAEqLwqJlyIvy4CYaFAe7wwuCKdf0EsJUw.png?1770192956)  
  


  * **Number Pool**  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064145329/original/FyDxbZqA_oMgojVAo1e_bStPVe2y1aop4Q.png?1770193144)**


* * *

## **Recommended Best Practices**

  


To avoid call issues:

  


  * Use an **external phone number** (mobile, landline, or VoIP) for call forwarding whenever possible.  
  


  * If you choose to use a GHL phone number:  
  


    * Ensure your call flow does **not route calls back to the same number**

    * Test your setup thoroughly after saving changes

    * Monitor call logs for failed or dropped calls

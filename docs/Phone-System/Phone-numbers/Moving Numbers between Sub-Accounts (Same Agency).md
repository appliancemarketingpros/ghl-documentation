# Moving Numbers between Sub-Accounts (Same Agency)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001203968-moving-numbers-between-sub-accounts-same-agency-](https://help.gohighlevel.com/support/solutions/articles/48001203968-moving-numbers-between-sub-accounts-same-agency-)  
**Category:** Phone System  
**Folder:** Phone numbers

---

This guide shows how to move phone numbers between sub‑accounts inside a single Agency using the built‑in Move Numbers tool. It covers LC Phone → LC Phone and Twilio → Twilio (same master account) moves, plus common errors and what to do if the in‑app move isn’t available (see[ Moving Phone Numbers: Migration Guide](<https://help.gohighlevel.com/support/solutions/articles/155000006369-moving-phone-numbers-migration-guide>)).

* * *

**TABLE OF CONTENTS**

  * What is Moving Numbers?
  * Prerequisites Before Moving Numbers
  * How to Move Numbers Between Sub‑Accounts
  * Troubleshooting & Known Limitations
  * Frequently Asked Questions
  * Related Articles


* * *

## **What is Moving Numbers?**

  


Move Numbers is an in‑app workflow in Settings → Phone Integration that reassigns existing phone numbers from a **source** sub‑account to a **destination** sub‑account **within the same Agency**. Eligibility at a glance:

  


  * **LC Phone ↔ LC Phone (same Agency):** Supported in-app.  
  


  * **Twilio ↔ Twilio (same Master Twilio account):** Supported in-app.  
  


  * **Different Master Twilio accounts:** Not supported in-app—contact **Twilio Support**.  
  


  * **Geography:** The in-app tool currently supports **US & Canada** numbers. For other countries, please open a **HighLevel Support** ticket.  
  


  * **A2P:** A2P status is at the sub‑account level and **does not move** with the phone number; reattach the correct brand/campaign after moving.


* * *

## **Prerequisites Before Moving Numbers**

  


  * Make sure you have admin access to the **source** and **destination** sub‑accounts.  
  


  * Identify the **destination Location ID** (a.k.a. Sub‑account ID): **Settings → Business Profile**.  
  
![](https://jumpshare.com/share/CXgGvlch4TfF6DNIAzet+/Screen+Shot+2026-08-14+at+18.07.40.png)  
  


  * Confirm which phone system the number uses today:  
  


    * **LC Phone** (LeadConnector)  
  


    * **Twilio** connected at the Agency level


* * *

## **How to Move Numbers Between Sub‑Accounts**

  


###  _**Step 1:** Move Numbers_

  


Navigate to the **Agency Settings → Phone Integration.** Under Sub-account Settings**,** click on **Move Numbers**.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054686537/original/1dFVtkd41G6bPk1bHpYSwn3bBHjHlTSbGg.png?1758893164)

  


  


### _**Step 2:** Select Source and Destination Sub-account and Phone Numbers to Move_

  


Choose the **Source** and **Destination** sub‑account (search by name or paste the Location ID). **Select** the **phone** **number(s)** you want to move and click on **Move Numbers**.

  


**![](https://jumpshare.com/share/68hkKk2TK4agWb0yILt6+/Screen+Shot+2026-08-14+at+18.11.10.png)**

  


  

    
    
    **Please Note:** Review the summary and click Move Numbers to start the transfer. Numbers will appear in the destination sub‑account once complete. After the move, re‑check number‑level settings (forwarding, recordings, whispers, etc.). Verify call/SMS flows, automations, and user assignments as needed.

* * *

## **Troubleshooting & Known Limitations**

  


If the **Move Numbers** action is unavailable or fails, common causes include:

  


  1. **Different Twilio master accounts:** Numbers under a different Twilio master can’t be moved in‑app. Contact Twilio Support in this case.  
  

  2. **Missing regulatory configuration (international):** Some countries (e.g., AU +61) require approved **Regulatory Bundles** and an **Address SID** in the **destination**. Configure those first, then follow the relevant migration guide.  
  


  3. **Provider mismatch:** If you’re converting **Twilio ↔ LC Phone** , follow the dedicated [conversion articles](<https://help.gohighlevel.com/support/solutions/articles/155000006369-moving-phone-numbers-migration-guide>) rather than the in‑app move.  
  


  4. **Country support (US & Canada in-app): **The in-app tool currently moves **US & Canada** numbers. For other countries, please create a **HighLevel Support** ticket.


* * *

## **Frequently Asked Questions**[](<https://help.gohighlevel.com/support/solutions/articles/48001177283>)

  


**Q. Can I move multiple numbers at once?**  
Yes, select multiple numbers in **Move Numbers**.

  


**Q. Do A2P/Toll‑Free approvals transfer automatically?**  
A2P Status will not be moved as it is at a sub-account level, not at phone number level.

  


**Q. Can I move Twilio numbers between sub-accounts?**  
Yes, as long as both sub-accounts use Twilio numbers under the same Master Twilio account.

  


**Q. Can I move a Twilio number between different Master Twilio accounts?**  
No. The in-app tool does not support moves between different Master Twilio accounts. Contact **Twilio Support** for assistance.

  


**Q. Which countries are supported by the Move Numbers tool?**  
The in-app tool currently supports phone numbers in the **United States and Canada**. For numbers in other countries, contact **HighLevel Support**.

  


**Q. Do I need admin access to move phone numbers?**  
Yes. Make sure you have the required admin access to both the source and destination sub-accounts.

* * *

### **Related Articles**

  


  * [How to Purchase a Phone Number](<https://help.gohighlevel.com/en/support/solutions/articles/155000003226>)  
  

  * [Moving Phone Numbers: Migration Guide](<https://help.gohighlevel.com/en/support/solutions/articles/155000006369>)  
  

  * [Moving US numbers from Twilio to LeadConnector(LC)](<https://help.gohighlevel.com/en/support/solutions/articles/48001240108>)

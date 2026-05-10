# Email Blocking for Invalid or Restricted Recipient Domains

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007880-email-blocking-for-invalid-or-restricted-recipient-domains](https://help.gohighlevel.com/support/solutions/articles/155000007880-email-blocking-for-invalid-or-restricted-recipient-domains)  
**Category:** Email  
**Folder:** General

---

HighLevel blocks outbound emails before sending when the recipient email domain is invalid or restricted for security reasons. This prevents sends to domains that can increase security risk or lead to failed delivery.

* * *

**TABLE OF CONTENTS**

  * What is Restricted Domain Blocking?
  * Key benefits of Restricted Domain Blocking
  * How it works
  * What you will see
  * How to resolve
  * Frequently asked questions
  * Related articles


* * *

# **What is Restricted Domain Blocking?**

  


Restricted domain blocking is a pre-send validation that prevents outbound email when a contact’s email domain (the part after `@`) is invalid or restricted. When the block triggers, HighLevel does not attempt to send the email.

* * *

## **Key benefits of Restricted Domain Blocking**

  


  * **Reduces failed sends:** Stops emails that would likely fail delivery.  
  

  * **Protects deliverability:** Helps reduce risk to sender reputation.  
  


  * **Improves security:** Prevents sending to domains HighLevel restricts for security reasons.


* * *

## **How it works**

  


  * HighLevel validates the recipient email address domain before sending.  
  


  * If the domain is invalid or restricted, HighLevel blocks the send.  
  


  * The contact’s email cannot be used for outbound communications until it is updated.


  


![](https://jumpshare.com/share/ipA5rS1VXQct4HANnoqA+/image+%283%29+%282%29.png)

* * *

## **What you will see**

  


When an email address is blocked, HighLevel shows an inline warning under the contact’s **Email** field:

  


This email address is invalid as the domain is restricted for security reasons.

  


![](https://jumpshare.com/share/Mm7ljWEF1FhCL3PETxJK+/image+%284%29+%281%29.png)

* * *

## **How to resolve**

  


  1. Confirm the email address is correct, especially the domain after `@`.  
  


  2. Update the contact with a valid email address on a permitted domain.  
  


  3. If this is a business-critical recipient domain, contact Support and include:  
  


     * The recipient domain (example: `example.com`)  
  


     * Where you saw the warning (Contact record, Conversations, Campaigns, Workflows, etc.)  
  


     * The sub-account name or ID  
  


     * The sending method (LC Email, Mailgun, custom SMTP)


* * *

## **Frequently asked questions**

  


**Q: Can I still send to an email address that shows this warning?**

No. HighLevel blocks the send before it leaves the platform when the recipient domain is invalid or restricted.

  


**Q: Can I override or bypass the block?**

No. You must update the contact with a valid email address on a permitted domain.

  


**Q: Where do I see the warning?**

You see an inline warning under the contact’s Email field.

  


**Q: Does HighLevel attempt delivery anyway?**

No. When this warning appears, HighLevel does not attempt to send the email.

  


**Q: How do I prevent this from happening?**

Verify recipient email addresses during intake and correct typos (especially the domain after @) before attempting to send.

* * *

### **Related articles**

  


  * [How to Enable and Rebill LC Email Verification ](<https://help.gohighlevel.com/en/support/solutions/articles/48001235221>)  
  


  * [Email Error Library for supported SMTPs ](<https://help.gohighlevel.com/en/support/solutions/articles/48001209322>)  
  


  * [Recipient Policy Block - Bypass Server Restrictions](<https://help.gohighlevel.com/en/support/solutions/articles/155000006942>)

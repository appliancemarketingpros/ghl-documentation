# ACH - bank transfer support on NMI

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007497-ach-bank-transfer-support-on-nmi](https://help.gohighlevel.com/support/solutions/articles/155000007497-ach-bank-transfer-support-on-nmi)  
**Category:** Payments  
**Folder:** Payment integrations, methods and settings

---

## FAQs  
  


**Q. My client just paid, but the ACH transaction is still showing as processing.**  
**A.** This is normal. ACH transfers can take up to 5 business days to reach a final status, depending on the payer’s bank. We recommend providing services only after the payment status changes to **Success**.

  
**Q. I am not getting the ACH option on an invoice.**  
**A.** If the feature is already enabled in Labs, please verify that ACH is also enabled on the NMI side. If the issue still continues after that, please contact our Support team for further assistance.  
  


**Q. I do not see the option to add a bank account for recurring invoices and subscriptions.**  
**A.** This is expected in the current V1 release. At this time, recurring invoices and subscriptions can only be started using a bank account that has already been saved. To save a bank account, you must first collect a payment through an invoice. Once the bank account is saved, it can be used for future recurring debits through recurring invoices and subscriptions. It would appear like this -  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066745227/original/_mue_KDC-vqm2EuynGQhjTtyWTuc2vCyaQ.png?1773294789)  
  
  
  


**Q. Do I need to enable anything else on the NMI side?**  
**A.** Yes. Please make sure the required webhooks for settlements and payment status updates are enabled in your NMI dashboard. You can refer to NMI’s documentation here for setup steps: `https://docs.nmi.com/reference/overview#where-to-setup`  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066745248/original/_luknz0QvbAsEAjw1eMM9PMT5vYb5ovD-w.png?1773294853)

  
URL to be used - <https://backend.leadconnectorhq.com/payments/nmi/webhook>  
  
Events to be enabled - 

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066745238/original/i6Ygq2T4nGL39aAUOg6V9m0V94_dtkXhyA.png?1773294833)

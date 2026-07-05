# WhatsApp Delivery Status under Workflows

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002491-whatsapp-delivery-status-under-workflows](https://help.gohighlevel.com/support/solutions/articles/155000002491-whatsapp-delivery-status-under-workflows)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# WhatsApp Delivery Status in Workflows  
  
In this article, we will discuss how to use WhatsApp delivery status inside workflows.

Table of Contents

Prerequisite for Using WhatsApp Under Workflows Recipe for WhatsApp Delivery Status How to Use WhatsApp Delivery Status Inside Workflows Frequently Asked Questions

* * *

Prerequisite for Using WhatsApp Under Workflows

✓WhatsApp needs to be subscribed and enabled on the location account. You can refer to WhatsApp Sub-Account Setup for setting up WhatsApp on your sub-account.

✓If you want to send business-initiated conversations, ensure that you have an approved template in place. See How to Create a WhatsApp Template.

* * *

Recipe for WhatsApp Delivery Status

You can use the pre-built WhatsApp Delivery Status recipe under Automations.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155026559813/original/ZM-GKrgtuPHvnIQs2Hf9h5Ha4pN9Dw-ZPQ.png?1716560015)

* * *

How to Use WhatsApp Delivery Status Inside Workflows

1

Go to Automation > Create Workflow > Start from Scratch

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155026487798/original/z68RVmgwwDv2YtzvBuVA-wo_E-KciAficw.png?1716466176)

2

Add Trigger > WhatsApp Action > Select WhatsApp Template

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155026488035/original/hoDiVPGKoAsE_pckEFA48JDT2al-Wra58A.png?1716466391)

3

Enable toggle "Wait for WhatsApp Message Delivery Status" > Save Action

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155026488147/original/LW8bIaKeBl2uhQONwMLuXWnlKAm3lkm5Kg.png?1716466458)

4

Add Action > If/Else

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155026488215/original/IJ34vqlnZ-VHR7aR7JEV2TWNiduHXY8RzA.png?1716466538)

5

Select Contact Details > Valid WhatsApp > Add conditions for True and False

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155026492804/original/HRodQYCR8yD7hbpwb9-03RiNm5UOJdoD-w.png?1716469670)

6

Add failover to SMS/Email for the False and None branch

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155026493561/original/CnwlstxlE20N-ywEH1GHMiuf3IBYEkrQyQ.png?1716470151)

* * *

Frequently Asked Questions

Q: What is the WhatsApp delivery status support feature?

WhatsApp delivery status support in workflows enhances your communication strategies by allowing you to incorporate conditional logic based on the delivery status of WhatsApp messages.

Q: How can I use the WhatsApp delivery status in my workflows?

You can use If/Else conditions based on Valid WhatsApp status to determine the next steps in your workflow. This enables more dynamic and responsive communication strategies.

Q: What is the purpose of the toggle for holding contacts in the workflow?

The toggle holds the contact in the workflow until the delivery status is received from Meta. This ensures that the workflow waits for the delivery status before proceeding to the next step.

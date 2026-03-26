# Domain Transfer-out to Cloudflare

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005176-domain-transfer-out-to-cloudflare](https://help.gohighlevel.com/support/solutions/articles/155000005176-domain-transfer-out-to-cloudflare)  
**Category:** Settings  
**Folder:** Domain Purchase / Transfer

---

This article outlines the steps required to transfer a domain to a different Cloudflare account. It consists of a pre-requisite, preparation steps, and the transfer process.

* * *

**TABLE OF CONTENTS**

  * Prerequisite
  * Prepare to Transfer
      * Step 1: Add the Domain as a Website to the New Account and Select a Plan
      * Step 2: Obtain the Account ID and Share with Us
  * Transfer
  * “Invalid Nameservers” Status


* * *

## **Prerequisites**

  


A Cloudflare account where domains has to be transferred should exist and you should have access to it.

* * *

## **Prepare to Transfer**

  


####  _**Step 1:** Add the Domain as a Website to the New Account and Select a Plan_

  


  1. Login to your Cloudflare account where you want to transfer your domain.  
  

  2. Click **\+ Add** then select **Connect a domain**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541161/original/gVVHcsIW5QonlscmH3R5-YwnheyNszfwvg.png?1773091141)  
  

  3. Enter the domain name to be transferred and click **Continue**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541180/original/65gJErz2EfCjyuCSJ6u23UJFGhREXOF5fg.png?1773091219)  
  

  4. Select the **Free** plan or a **Paid** plan.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541191/original/w7clqIe9U_CEp-gGmzhQNpK78eeRdSoIsA.jpeg?1773091290)  
  

  5. Cross-check your scanned DNS records with your current DNS records. You can find your current DNS records here:  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541199/original/NzCoal8RZ8tmFp3uFfnoo8KSCkI-IRQQTA.jpeg?1773091337)  
  

  6. If the scanned records match with the existing records, then hit **Continue to Activation**. If not, manually add/remove the scanned records to match existing records.  
  
Ensure **proxy is turned OFF** for all records before clicking 'Continue to Activation'. There isn't a need a change nameservers at this step.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541215/original/_Kcx_bTIL4_t4G4MaH2E5Xs9l-aVkFwc6Q.jpeg?1773091385)  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541214/original/Q9ZihH0a9DQzvpUhaTNM5iXoaLzaqD9bog.jpeg?1773091378)**


  


  


#### _**Step 2:** Obtain the Account ID and Share with Us_

  


Once you have completed all above process, obtain the **account ID** of your Cloudflare account and share it with us. To obtain the account ID, extract the alphanumeric value from the URL.

  
**Example:** In this case, this is the account ID: `0d2031c4bcda5980204101c44294740c`

  


`![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541313/original/ZgkAPa5NXYZ1HWPeiNZJxUzhM5x2vgGVaw.jpeg?1773091646)`

* * *

## **Transfer**

  


Once all 2 steps above are completed, we will initiate the transfer process from our end. You can expect the transfer to get completed within **24 hours** after we initiate it. Then you need to approve the transfer by following these steps:

  


  1. Go to **Manage****Domains** under **Domain****Registration** in the left navigation menu and click on **Manage** button for the given domain.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541338/original/jh7NDLyHrVE1FxwbXaXJdZNp5h_aolVBwQ.jpeg?1773091752)  
  

  2. Accept the transfer request.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541348/original/IozVBYypZNlTQHRSFXUG-KnpFUBecHvCRg.png?1773091763)  
  

  3. You can expect the transfer to get completed within 24 hours after you accept it. Once transfer is successful, status will turn to **Active** for that domain under **Manage Domains**. If you find 'Invalid Nameserver' status in **Account Home** for that domain, please wait for a few hours and then check again.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066541351/original/s3tD_v2Uu3THwztcXS8ZW4GkxRBH84v-9g.jpeg?1773091778)


* * *

## **“Invalid Nameservers” Status**

  


After the transfer has been accepted, the domain may temporarily show “Invalid Nameservers” in the Account Home section. Don’t worry, this is expected behavior.

  


This warning typically resolves itself automatically within 24 hours post-transfer. No action is needed from your side.

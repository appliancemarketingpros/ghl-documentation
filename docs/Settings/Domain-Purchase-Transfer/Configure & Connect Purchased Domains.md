# Configure & Connect Purchased Domains

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004674-configure-connect-purchased-domains](https://help.gohighlevel.com/support/solutions/articles/155000004674-configure-connect-purchased-domains)  
**Category:** Settings  
**Folder:** Domain Purchase / Transfer

---

When you purchase a domain through HighLevel, you can manage its DNS records and connect it to supported HighLevel Sites without leaving the platform. This article explains where to find your purchased domain, how to manage its DNS records, and how to connect it to a Funnel, Website, Store, or Blog.

**IMPORTANT:** This article applies to domains purchased through HighLevel. If you purchased the domain from another registrar, use the external domain connection process instead.

## Table of Contents

  * What Is Purchased Domain Configuration?
  * Key Benefits of Purchased Domain Configuration
  * Supported DNS Records
  * How to Manage a Purchased Domain
  * How to Add a DNS Record
  * How to Connect a Purchased Domain
  * Using a Root Domain for More Than One Site
  * Frequently Asked Questions
  * Related Articles


* * *

## **What Is Purchased Domain Configuration?**  
  


Purchased Domain Configuration lets you manage a domain that was purchased directly through HighLevel. Because HighLevel manages the domain registration, you can view and update supported DNS records from the sub-account instead of signing in to a separate registrar.  
  


You can use Purchased Domain Configuration to:  
  


  * Add, edit, or remove supported DNS records.  
  

  * Connect the domain to a Funnel, Website, Store, or Blog.  
  

  * Review the domain's status and renewal information.  
  

  * Manage the domain from the same HighLevel sub-account where it was purchased.


* * *

## **Key Benefits of Purchased Domain Configuration**  
  


Managing a purchased domain inside HighLevel keeps common domain tasks in one place and reduces the need to work between multiple platforms.  
  


  * **Centralized DNS Management:** Add and manage supported DNS records directly in HighLevel.  
  

  * **Faster Site Connection:** Connect the domain to supported HighLevel Sites using the guided connection flow.  
  

  * **Clear Domain Status:** Review whether the domain is still being configured or is active and ready to manage.  
  

  * **No External Registrar Login:** For domains purchased through HighLevel, common DNS changes can be completed without opening another registrar account.  
  


* * *

## **Supported DNS Records**  
  


HighLevel supports managing the following DNS record types for purchased domains.  
  


  * **A:** Points a domain or hostname to an IPv4 address.  
  

  * **CNAME:** Points one hostname to another hostname.  
  

  * **AAAA:** Points a domain or hostname to an IPv6 address.  
  

  * **MX:** Identifies the mail servers responsible for receiving email for the domain.  
  

  * **TXT:** Stores text-based information commonly used for domain verification and email authentication.


**IMPORTANT:** Be careful when changing DNS records that are already in use. Incorrect changes can affect websites, email, or other services connected to the domain.

* * *

  


## **How to Manage a Purchased Domain**  
  


Use the Purchased Domains area to open the domain's configuration and choose whether you want to manage DNS records or connect the domain to a HighLevel site.  
  


  1. From the sub-account, click **Settings**.

  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078640875/original/NRPJ6JZa-IqYj12DJ3fkm-PcEOjXO0CL0w.png?1787000945)**  


  2. Open**Domains** and locate the domain under **Purchased Domains**.  
  


If the domain is still being prepared, its status may show **Setting up your Domain** and the Configure button may not yet be available.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078640886/original/Zbf-hXjAbM6g6ubxgB6nKN8JBOVhFsPpjg.png?1787000966)**  
  


  3. Once the domain shows**Active** , click **Configure**.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078640893/original/DhRgPk_tDZD5WVAHdBo92d9pyWvbvGEz2g.png?1787000989)**  


  4. The domain configuration page gives you two primary options:  
  

     * **Add Record:** Manually add a DNS record.  
  

     * **Connect this domain:** Connect the domain to a supported HighLevel Sites asset.  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078640904/original/8qrlHGFHowdUGLiq-CkS89gpTBVSaxxQxw.png?1787001031)**


* * *

## **Purchased Domain Status Troubleshooting**

### **Expected Domain Status**

After purchase, the domain may show **Setting up your Domain**.

Once setup is complete, the domain should show **Active** and the **Manage** option should become available.

HighLevel states that domain registration usually takes about **1 minute**.

### When Manage Becomes Available

The **Manage** option should appear after the domain becomes **Active**.

If the domain is still setting up, you may need to wait until provisioning is complete.

**Screenshot placeholder:** Show an **Active** domain with the **Manage** option.

###   


### What “**Renews"** on: -” Means

  


**“Renews on”** is the date when the purchased domain is scheduled to renew for another registration period.

For example, if it says **Renews on: September 10, 2027** , the domain is expected to renew on that date, assuming renewal remains enabled and the account can be charged.

### **  
**

### **What to Check**

Before contacting Support:

  * Confirm the domain appears under **Settings > Domains > Purchased Domains**.

  * Check the current domain status.

  * Refresh the page.

  * Check whether **Manage** is available.

  * Look for any error messages.

  * Note what appears next to **Renews on**.


### **When to Contact Support**

Contact HighLevel Support if the domain stays in setup longer than expected, **Manage** does not become available, or you see an error.

Include the following:

  * Domain name

  * Screenshot of the domain status

  * What appears next to **Renews on**

  * Approximate purchase date and time

  * Any error message shown


This information helps Support review the domain provisioning status.

##   


##   


## **How to Add a DNS Record**  
  


Manual DNS management is useful when you need to add a specific record for a website, email service, verification process, or another connected service.  
  


  1. From the purchased domain configuration page, click **Add Record**.  
  

  2. Select the required DNS record **Type**.  
  

  3. Enter the **Name** or host value.  
  

  4. Enter the required destination or content value.  
  

  5. Select the **TTL** value.  
  

  6. Click **Save**.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078640914/original/IRAzXxADU4GYbWuddTzG-YTN3NIdNYI5MA.png?1787001076)**

The fields shown can vary depending on the DNS record type you select.  
**  
**

### **Root Domain A Records**  
  


When pointing a root domain, avoid creating multiple A records for the same root hostname unless your configuration specifically requires them.  
  


Multiple A records for the same root domain can create DNS resolution conflicts, especially when HighLevel needs to automatically add the required A record.

* * *

## **How to Connect a Purchased Domain**  
  


The **Connect this domain** option uses a guided flow to associate the purchased domain with content you built in HighLevel.  
  


  1. From the domain configuration page, click **Connect this domain**.  
  

  2. Confirm the domain you want to connect.  
  


You can also choose whether to include the **www** version of the domain when that option is available.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078640816/original/YB1QC958yRgWZ6H0SchbF3m_tngVvi2MFw.png?1787000774)**

  


  3. Click**Continue** and follow the prompts to add the required DNS records.  
  

  4. Select what you want to connect the domain to:  
  

     * Funnel  
  

     * Website  
  

     * Store  
  

     * Blog  
  

  5. Choose the specific asset from the dropdown.  
  

  6. Review any available additional options, then click **Proceed to finish**  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078640806/original/vdiXE14iPfsSdCtxx4y_P5FxXqqk4PsFeQ.png?1787000741)

  
  


  7. After configuration is complete, return to the purchased domain page and review the DNS records.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078640800/original/T4gxDDuer8gKvf56fCO6ZNMn3dIkHo7vRg.png?1787000716)**


**NOTE:** DNS changes may take time to propagate across the internet. If the connected domain does not work immediately, allow time for the DNS changes to update before troubleshooting further.

* * *

## **Using a Root Domain for More Than One Site**  
  


A single root domain should normally be connected to one primary site type at a time. For example, you would not use the same root domain as the direct address for both a Website and a separate Store.  
  


If you need different experiences on the same domain family, use subdomains such as:  
  


  * `[www.example.com](<//www.example.com>)`  
  

  * `[store.example.com](<//store.example.com>)`  
  

  * `[blog.example.com](<//blog.example.com>)`  
  


This lets each subdomain point to a different destination without creating a conflict on the root domain.

##   
**Frequently Asked Questions**  
  


**Q: Can I manage a domain in HighLevel if I purchased it somewhere else?**

You can connect an externally purchased domain to HighLevel, but the Purchased Domain Configuration described in this article is specifically for domains purchased through HighLevel. External domains may require DNS changes at the registrar or DNS provider.  
  


**Q: What DNS records can I manage for a purchased domain?**

You can manage A, CNAME, AAAA, MX, and TXT records from the purchased domain configuration area.  
  


**Q: Why is the Configure button unavailable?**

If the domain is still being set up, configuration may not yet be available. Wait until the purchased domain shows an Active status, then open Configure.  
  


**Q: Do I need to verify a domain purchased through HighLevel manually?**

Domains purchased directly through HighLevel are handled within the HighLevel domain-purchase system, so you do not need to complete the same external registrar verification process used when connecting a third-party domain.  
  


**Q: Can I connect the same root domain to both a Funnel and a Website?**

A root domain should be connected to one site type at a time. Use subdomains when you need separate destinations for different assets.  
  


**Q: Why isn't my domain working immediately after I changed the DNS?**

DNS changes are not always immediate. Propagation can take time, so wait for the DNS update to complete before assuming the configuration has failed.  
  


**Q: What happens if my HighLevel account is canceled but I still own a domain purchased through HighLevel?**

If you can no longer access the domain management area after cancellation, use HighLevel's dedicated purchased-domain release process.

###   


* * *

### **Related Articles**  
  


  * [](<https://help.gohighlevel.com/support/solutions/articles/155000003610-how-to-purchase-domain-step-by-step>)[ How to Purchase a Domain in HighLevel | Step-by-Step ](<https://help.gohighlevel.com/en/support/solutions/articles/155000003610>)  
  

  * [](<https://help.gohighlevel.com/support/solutions/articles/155000005132-connecting-your-domain-on-ghl-a-guide>)[ Connecting Your Domain on HighLevel - A Guide ](<https://help.gohighlevel.com/en/support/solutions/articles/155000005132>)  
  

  * [](<https://help.gohighlevel.com/support/solutions/articles/48001153720-how-to-set-up-root-domain-subdomain-for-your-funnels-websites->)[ How to Set Up a Root Domain/Subdomain for Funnels/Websites ](<https://help.gohighlevel.com/en/support/solutions/articles/48001153720>)

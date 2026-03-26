# Mailgun - Overview

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981677-mailgun-overview](https://help.gohighlevel.com/support/solutions/articles/48000981677-mailgun-overview)  
**Category:** Email  
**Folder:** MailGun

---

Mailgun is the email delivery service that powers bulk sending in HighLevel. In this article, you’ll learn what Mailgun is, how pricing works, which domains or subdomains to use, and the pros and cons of different setup options so you can choose the best configuration for your agency and clients.

* * *

**TABLE OF CONTENTS**

  * What is Mailgun?
  * Key Benefits of Using Mailgun with HighLevel
  * How Much Will Mailgun Cost?
  * What Domain Should I Use?
  * Related Articles


* * *

# **What is Mailgun?**

  


Mailgun is a third-party service we use to send emails in bulk. Similar to how we use Twilio to send text messages and calls. For new onboarding agencies, you will be using [LC email](<https://help.gohighlevel.com/en/support/solutions/articles/48001220605>) by default, which is living under our Mailgun account.

  

    
    
    **Note:** For complete step-by-step instructions on how to setup Mailgun in HighLevel, see this [article](<https://help.gohighlevel.com/en/support/solutions/articles/48001219824>).

* * *

## **Key Benefits of Using Mailgun with HighLevel**

  


  * **Reliable bulk email sending** \- Send large volumes of emails through a dedicated, reputable email infrastructure.  
  


  * **Branded sending domains** \- Use your own domain or subdomains so emails look professional and on-brand.  
  


  * **Flexible setup options** \- Choose between one shared subdomain or multiple client-specific subdomains based on your needs.  
  


  * **Better deliverability control** \- Optimize DNS and MX records to improve inbox placement and reduce issues from poor-quality lists.


* * *

## **How Much Will Mailgun Cost?**

  

    
    
    **Note:** Learn more about Mailgun [pricing](<https://www.mailgun.com/pricing/>) here.

  


  * Mailgun's **Basic plan** starts at **$15/Month**.  
  

  * Mailgun's **Foundation plan** starts at **$35/Month**.  
  

  * Mailgun's **Scale plan** starts at **$90/Month**.


* * *

## **What Domain Should I Use?**

  


We recommend using a subdomain with Mailgun, like "mg.mydomain.com". Using a subdomain you will be able to send emails from your root domain e.g. "you@mydomain.com".

  


If using a subdomain please make sure that you configure MX records for the subdomain for optimal delivery. This is configured within your Mailgun account. 

  


Note: You can only add domains you own. You will need to update the domain's DNS records to verify that you are an authorized owner or sender for this domain.

  


There are two different ways to set up Mailgun with HighLevel:

  


Sub-domains  
| Pros:| Cons:  
---|---|---  
**1\. One Sub-domain**  
You can set up one sub-domain in Mailgun for your marketing agency domain and use that same sub-domain for email sending across all of your client accounts in HighLevel  
| 

  * Easy setup - only need to set up one subdomain for your domain which you already have access to
  * Emails are white-labeled to your marketing agency domain or you can buy a generic domain so it will not show any agency branding

  
| If your domain gets disabled (gets a bad score due to bounce rates) email will stop working for all of your clients since all of their accounts are powered by the same domain.  
The solution: don't send spammy emails to poor email addresses :-)  
  
**2\. Multiple Sub-domains**  
  
You can set up a subdomain in Mailgun for each of your client's domains and use that subdomain for sending for their specific HighLevel account. Once you set up a unique domain/subdomain for each location to capture cold inbound emails. [Learn more about Cold Email Inbound Setup here.](<https://help.gohighlevel.com/support/solutions/articles/48001185801-cold-email-inbound-setup>)  
| 

  * Emails are white-labelled per the client domain 
  * If a client's domain gets disabled email only goes down for their client account

  
| Difficult setup - time-consuming having to set up a subdomain for all of your clients and getting access to each of their domains  
  
  
* * *

## **Related Articles**

  


  * [](<https://help.gohighlevel.com/en/support/solutions/articles/155000002369>)[](<http://Frequently%20Asked%20Questions%20Currently%20no%20frequently%20asked%20questions.%20Submit%20feedback%20on%20this%20article%20to%20help%20is%20add%20questions%20to%20this%20section!%20%20Related%20Articles%20How%20To%20Connect%20Your%20Google%20Calendar>)[Step-by-step guide to set up Mailgun](<https://help.gohighlevel.com/en/support/solutions/articles/48001219824>)  
  

  * [Mailgun Setup Checklist](<https://help.gohighlevel.com/en/support/solutions/articles/48001175336>)  
  

  * [How to setup Replies in MailGun](<https://help.gohighlevel.com/en/support/solutions/articles/48000987293>)  
  

  * [Mailgun: Private API Key Setup](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>)

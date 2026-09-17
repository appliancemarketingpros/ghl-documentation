# How to Use Custom Menu Links in SaaS Plans

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004196-how-to-use-custom-menu-links-in-saas-plans](https://help.gohighlevel.com/support/solutions/articles/155000004196-how-to-use-custom-menu-links-in-saas-plans)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

This article explains how to use Custom Menu Links (CMLs) in SaaS plans to streamline the process of adding 3rd-party solutions to HighLevel. With this feature, agencies can automatically apply CML configurations to new sub-accounts when they subscribe to a specific SaaS plan, improving efficiency and enhancing SaaS offerings.

* * *

**TABLE OF CONTENTS**

  * What Are Custom Menu Links?
    * Benefits Of Custom Menu Links
    * Create Custom Menu Links
    * Getting the user's context within the Custom Menu Link  

    * How to Add Custom Menu Links in SaaS Plans
    * Frequently Asked Questions


# **What Are Custom Menu Links?**

  


Custom Menu Links (CMLs) allow agencies to embed 3rd-party solutions, such as AI tools, inventory management systems, or virtual assistant tools, directly into the HighLevel app. By linking these tools through iframes, agencies can offer an integrated experience to their users.

* * *

## **Browse Custom Menu Links Across Multiple Pages**

  


The Custom Menu Links selection window includes pagination for agencies with large link libraries.

  


1\. Select the links you want to attach.  
  


2\. Use Previous, Next, or the page numbers to browse more links.  
  


3\. Click Attach Selected.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076600695/original/dDyRKIazQ7zO6ofs00vX3xLmA7OcVgNavg.png?1784727494)

* * *

## **Benefits Of Custom Menu Links**

  


Many SaaS businesses offer additional solutions alongside HighLevel features as part of their service package. With this functionality, Custom Menu Links can now be tied directly to SaaS plans. When a new sub-account subscribes to a plan, the associated Custom Menu Links are automatically applied without requiring manual setup.

  


  * **Auto Deployment** : Automating CML setup for new sub-accounts eliminates manual configuration.  
  

  * **Enhanced User Experience** : Embedded solutions feel like a native part of the HighLevel app.  
  

  * **Consistency** : Ensures that all sub-accounts subscribing to a plan receive the same setup.  
  

  * **Plan-Level Configuration** : Add CMLs directly to SaaS plans, ensuring all new sub-accounts inherit the links.  
  

  * **Easy Updates** : Add or modify CMLs in existing SaaS plans, and changes will apply to all future sub-accounts that subscribe to the plan.  
  

  * **Scalability** : Simplifies onboarding as your SaaS offering grows.


* * *

## **Create Custom Menu Links**

  


Navigate to **Agency Account > Settings > Custom Menu Links** > Create New or Edit. Fill out the settings. In the URL field you can use **Custom Values** , for example: http://url.com/{{location.id}}?value={{custom_values.my_value}}. These {{string}} are called Merge Fields and a full list is here: [List of Merge Fields](<https://help.gohighlevel.com/en/support/solutions/articles/48001078171>).

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048499152/original/JRURct4F_iUPvfhPe1W3ng8flnjjEvlPKA.png?1750269694)

* * *

## **Getting the user's context within the Custom Menu Link**

  


While creating the Custom Menu Link, you can set the URL like this:

https://test.com/test?fname={{user.first_name}}&lname={{user.last_name}}&location_id={{location.id}}&custom_value_example={{custom_values.example_field_name}}

  


This way, when a user clicks on the link, HighLevel will dynamically replace the param variables with actual values based on the user's context. You can extract these params from the URL and get the user's context.

  


**Supported params to CML**

user.first_name

user.last_name

user.name

user.phone

user.email

location.id

location.name

location.city

location.state

location.country

location.address

location.email

location.phone

location.postal_code

location.full_address

location.website

location.logo_url

location_owner.first_name

location_owner.last_name

location_owner.email

custom_values.{CUSTOM_VALUE_NAME}

  


## **How to Add Custom Menu Links in SaaS Plans**

  


###  _**Step 1:** Create a New SaaS Plan_

  


  * Log in to your HighLevel agency dashboard.  
  

  * Navigate to the **SaaS Configurations** section.  
  

  * Select **Create New Plan.**


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155036925372/original/c564q4W1JOz5DAJIuSvQMu9e9MpGO1rYjg.png?1732131751)

  


  


### _**Optional:** Update Existing SaaS Plans_

  


  * For existing plans, you can add new Custom Menu Links.  
  

  * Sub-accounts subscribing to these updated plans in the future will automatically receive the new CMLs.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155036925363/original/ldJfpgDfKghGztYkQh83822u3uZZTWuo4Q.png?1732131734)

  


  


### _**Step 2:** Add Custom Menu Links_

  


  * Go to the **Custom Menu Links** section within the SaaS plan configuration.  
  

  * Add the 3rd-party solutions you want to embed using the iframe URLs.  
  

  * Assign names and organize the CMLs as needed for the end-user experience.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155036925318/original/sNXOkIbtL_Drx4AR-7MMREIkW8i-3c5s_w.png?1732131622)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155036925410/original/C0W5LvDMwm24BnY07Zhm3cBCMPXuMsufRw.png?1732131786)

  


### _**Step 3:** Save and Apply the Plan_

  


  * Save your changes to the SaaS plan.  
  

  * Any new sub-accounts subscribing to this plan will automatically receive the configured Custom Menu Links.


* * *

## **Frequently Asked Questions**

  


**Q: What happens to existing sub-accounts when I update a SaaS plan with new Custom Menu Links?**  
Updates to a SaaS plan only apply to new sub-accounts subscribing to the plan. Existing sub-accounts must be manually updated with the new CMLs.

  


  


**Q: Can I edit or remove Custom Menu Links after they are applied to sub-accounts?**  
Yes, you can edit or remove Custom Menu Links in SaaS plans, but changes will only affect new sub-accounts subscribing to the plan.

  


  


**Q: Are Custom Menu Links limited to specific 3rd-party solutions?**  
No, you can embed any tool or solution that supports iframes via a URL.

  


  


**Q: Can I use this feature for non-SaaS accounts?**  
Custom Menu Links are primarily intended for SaaS plans. For non-SaaS accounts, CMLs must be manually added.

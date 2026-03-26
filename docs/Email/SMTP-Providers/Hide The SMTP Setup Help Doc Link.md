# Hide The SMTP Setup Help Doc Link

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001065654-hide-the-smtp-setup-help-doc-link](https://help.gohighlevel.com/support/solutions/articles/48001065654-hide-the-smtp-setup-help-doc-link)  
**Category:** Email  
**Folder:** SMTP Providers

---

This help article provides a brief guide on how to hide the SMTP setup help doc link

  


**TABLE OF CONTENTS**

  * How to remove/hide the SMTP setup help doc link

  * Log into your HighLevel account, go to Settings

  * Related Articles


  


* * *

  


## **How to remove/hide the SMTP setup help doc link**

If you don't want your clients to see this link:

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032853011/original/eP8muhxmKz6vk0vz9iAKhy17sMVPvCBtdA.jpg?1726245732)

  


## **Log into your HighLevel account, go to Settings > Agency Settings then scroll down to the Custom CSS field and paste the following code: **

  

    
    
    .hl__smtp-help-doc {
    display: none;
    }

  


This will hide the SMTP setup help doc link. If you decide to display the SMTP setup help doc link again later, simply remove the code from the custom CSS field above

* * *

# **Related Articles**

  * [](<https://help.gohighlevel.com/en/support/solutions/articles/155000002369>)[How to setup SMTP providers ](<https://help.gohighlevel.com/a/solutions/articles/48001059689?portalId=48000045315>)

# How To Attach Files to MMS Using Custom Values

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001218845-how-to-attach-files-to-mms-using-custom-values](https://help.gohighlevel.com/support/solutions/articles/48001218845-how-to-attach-files-to-mms-using-custom-values)  
**Category:** Workflows  
**Folder:** Workflow Builder

---

Custom values are exceptionally powerful and versatile. In this guide, we will cover how you can use custom values to send MMS messages within workflows. 

  


Custom values are great for leveraging snapshots and your favorite workflow(s). Its a quick and simple setup making your automation more scalable and exciting. 

  


* * *

#### **Covered in this article**

#### **How to attach Custom Values URLs to SMS messages**

#### **Troubleshooting**

    * #### What is the maximum MMS size when sending SMS?

    * #### What are the support file types for MMS when sending via SMS?

    * #### My custom value does not work when the message is sent?  
  


* * *

# **How to attach Custom Values URLs to SMS messages**

  


## **Step 1:** Setup your custom value URL 

**Head into the location settings > Custom Values > \+ Add Custom Value > Enter MMS URL**

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48240187218/original/Cq5T3LD3wiScR2JwiibCexevGo9I4SOlLQ.gif?1658417559)

  


##   


  


  


## **Step 2:** Head into your workflow where you would like to send the MMS

Now that you are in your workflow make sure to attach the custom value as an attachment. You will need to copy and paste the value

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48240188567/original/PDE7_BYhWRlwXQ1KbFOTDcncrlAhAotBGQ.gif?1658417802)

  


**Please note:**
    
    
    There are strict requirements to MMS sizes when it comes to different carriers. _These_ _limitations are set by the carriers_.
    
    **For more info on the correct size requirements by carrier, please check out**What is the maximum MMS size when sending SMS?

  


  


  


  


  


* * *

# **Troubleshooting**

  


### **What is the maximum MMS size when sending SMS?**

**Carrier**| **Long code MMS attachment size**| **Toll-Free MMS attachment size**| **Shortcode MMS attachment size**  
---|---|---|---  
AT&T| 0.6 MB| 0.6 MB| 0.6 MB  
Sprint| 1.4 MB| 0.6 MB| 1.4 MB  
T-mobile| 1.5 MB| 0.6 MB| 1.0 MB  
Verizon| 0.675 MB| 0.6 MB| 1.2 MB  
  
  


  


### **What are the support file types for MMS when sending via SMS?**

  * jpeg
  * png
  * gif


###   


### **My custom value does not work when the message is sent?**

Please double-check to make sure:

  1. There are no spaces in your custom value URL, you can test this by adding it to a dummy funnel and previewing the page. If the MMS appears the custom value works, please proceed to the next step below
  2. The MMS URL meets the size requirement for the provided carrier (see question above)

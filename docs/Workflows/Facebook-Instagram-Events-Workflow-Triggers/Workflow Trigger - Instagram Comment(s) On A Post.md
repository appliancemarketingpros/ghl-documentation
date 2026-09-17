# Workflow Trigger - Instagram Comment(s) On A Post

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004646-workflow-trigger-instagram-comment-s-on-a-post](https://help.gohighlevel.com/support/solutions/articles/155000004646-workflow-trigger-instagram-comment-s-on-a-post)  
**Category:** Workflows  
**Folder:** Facebook/Instagram Events Workflow Triggers

---

This trigger fires when there is a comment on your Instagram post(s).

* * *

**TABLE OF CONTENTS**

  * What Is The Trigger - Instagram Comment(s) On A Post?
    * Where To Find This Trigger
    * Components
    * Filters
      * Page Is + Post Type + Post Is
      * Contains Phrase OR Exact Match
      * Track First Level Comment Only
    * Frequently Asked Questions


* * *

# **What Is The Trigger - Instagram Comment(s) On A Post?**

  


This trigger is fired when a comment on your Instagram post(s) matches the filters you set. 

* * *

## **Where To Find This Trigger**

##   


Navigate to Automations > Workflows > Workflow Builder > Triggers > Facebook/Instagram Events.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041830962/original/L9pXyb2ALo5ULdcFeYUy0T6VYpOyoO-wRw.jpeg?1739902001)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041831350/original/46MFAXXN7ivLHEZi5jJITh3R3RFPEcN9zw.png?1739902649)

* * *

## **Components**

There are four (4) primary components of the Workflow Trigger - Instagram Comment(s) On A Post:

  


  1. **Choose A Workflow Trigger:** By default this option is set to this trigger. You can change it to a different trigger if you want.  
  

  2. **Workflow Trigger Name:** By default this is just the name of the trigger. You can edit this to give it a clearer name that is visible in the Workflow.  
  

  3. **Filters:** This is where you select the criteria for firing the trigger in the right situation. More details in the next section.  
  

  4. **Track First Level Comments Only:** This toggle, when off, will allow the trigger to fire for all nested comments. When it is toggled on, then the trigger will only fire for the top (first) comment, not for comments under that comment.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041831384/original/6Ce-Rwd62Mg6NBY35w_eh41WpIfq_p66-w.png?1739902707)

* * *

## **Filters**

  


Detailed description of the filters:

  


Filter Level 1| Options  
---|---  
Page Is| List of your account's pages  
Post Type  
  
| Published Post (all posts on your business page)  
Custom Post (enter a URL)  
Post is| List of the posts that match your Page Is + Post Type settings  
Contains Phrase| Phrase = "I bought from you"  
Comment = "I bought from you yesterday" --> Pass  
Comment = "I bought one from you" --> Fail  
Comment = "how much" --> Fail  
Exact Match| Phrase = "I bought from you"  
Comment = "I bought from you" --> Pass  
Comment = "I bought from you yesterday" --> Fail  
Comment = "I bought one from you" --> Fail  
  
  


  


### **Page Is + Post Type + Post Is**

  


First select the page from Page Is, then select the type of post from Post Type, then you can select the post itself from Post Is.

  


**_Step 1: Select the Page_**

  


Select Standard Fields > Page Is and then the page from the list.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041831411/original/8CdKJJyt-KHiyQ9u9FFZEPG_LDKCS1Nl3A.png?1739902781)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041831479/original/tvHzg5VvNtl1or3g4RyJUsQETiIrz9dEAA.png?1739902917)

  


  


**_Step 2: Select the post type_**

  


Select Published Post to pick from a list or Custom Post to enter a URL.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041830957/original/5smhFAlN2W3h3Ufg9WrD7zVrqb_7LWtvAw.jpeg?1739902001)

  


  


** _Step 3: Identify the exact post_**

  


If you used Published Post, then pick from the list, and if you used Custom Post, enter the direct URL.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041830959/original/QgLcGzSJlU_yu4JQsPGv92RDNLxdUPAEtQ.jpeg?1739902002)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041830961/original/tOlAMbpzythpz_CBJFtWIpYNC06JaKsy9A.jpeg?1739902002)

* * *

### **Contains Phrase OR Exact Match**

###   


After you have identified the exact post, you can use either the Contains Phrase filter or the Exact Match filter. 

  


  * **Contains Phrase:** the trigger will fire if the body of the comment contains one of the exact text strings you provide.  
  

  * **Exact Match:** the trigger will fire if the entire body of the comment exactly matches one of the text strings you provide.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041830958/original/VXaZqRiMQLv0vjxMBVhtcP7sqHT5lYfwkQ.jpeg?1739902002)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041830964/original/oudpvop2MK-VyOCAWk55cgPMouFiDOjYhg.jpeg?1739902002)

* * *

### **Track First Level Comment Only**

  


You can use the toggle to turn on/off 1st level comment only.

  


  * **Toggle On:** the trigger will only fire for the first comment in a chain, not for comments under a comment.  
  

  * **Toggle Off:** the trigger will fire for any comment, even if it's nested under other comments.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155041830963/original/JM8x0HqYuN35fNB2rYm4BspMSf4USIjDAQ.jpeg?1739902002)

* * *

## **Frequently Asked Questions**

  


**Q: Can the trigger Instagram Comment(s) on post work for Facebook?**

No, this trigger only works for Instagram. You can use the identical [Facebook Comment(s) on post](<https://help.gohighlevel.com/en/support/solutions/articles/155000004645>) trigger for Facebook.

  


**Q: What actions should I use with the trigger Instagram Comment(s) on post?**

Use the Recipe Instagram Comment Automation to see an example of how to use this trigger in a workflow. Review the article [Facebook & Instagram Comment Automation](<https://help.gohighlevel.com/en/support/solutions/articles/155000002055>) and the actions [Reply In Comment](<https://help.gohighlevel.com/en/support/solutions/articles/155000003302>) and [Instagram Interactive Messenger](<https://help.gohighlevel.com/en/support/solutions/articles/155000003301>).

  


**Q: Can the Comment On Post trigger create an infinite loop?**

No, automatic comments will not create an infinite loop. The workflow triggers automatically ignore any comments posted by workflow actions.

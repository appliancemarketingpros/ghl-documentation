# Using Google/Gmail/Google Workspace as your SMTP Provider

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001148427-using-google-gmail-google-workspace-as-your-smtp-provider](https://help.gohighlevel.com/support/solutions/articles/48001148427-using-google-gmail-google-workspace-as-your-smtp-provider)  
**Category:** Email  
**Folder:** SMTP Providers

---

This comprehensive guide walks you through creating app-specific account passwords with 2-step verification, focusing on Gmail SMTP integration. It is particularly useful for users in the Philippines who face connection difficulties.  
  


  * **What it does:** “Connecting Gmail/Google Workspace as an SMTP provider lets HighLevel send emails through a specific Google mailbox using SMTP credentials.  
  


  * **What it does not do:** “This does not connect your entire Google Workspace domain for sending and receiving across the whole HighLevel account. SMTP is not an inbox sync.  
  


  * If you want inbox-style sending/receiving (two-way email sync), use the dedicated Gmail integration instead of SMTP.


* * *

**TABLE OF CONTENTS**

  * Create App-Specific Passwords for Accounts with 2 Step Verification On:
  * How to Enable 2 Step Verification
  * FAQs


* * *

  


## **Create App-Specific Passwords for Accounts with 2 Step Verification On:**

  


**Please Note:**

  


Please use a VPN when trying to connect to Gmail SMTP for Users in the Philippines

  


Learn why I can't use My Free Email Address As The SMTP.

  


1\. Go to [Google.com](<//Google.com>)  
  


2\. Click on your icon on the top right

  
3\. Make sure you choose the correct Google Account that you want to integrate with

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833278/original/cBhUzmY3La5GZZwXvM3OMG8vqD9WTqPbmg.jpg?1721852088)

  


4\. Click on Manage your Google Account

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833321/original/LjrfYH8Kd5YruR33CxYenH5LMyQ19mVIyg.jpg?1721852173)

  


5\. Click on Security

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833331/original/MohhWMeCisTVcfoPi_ck-e3pkOt4f9LWXg.jpg?1721852215)

  


  


6\. Scroll down further to locate the section Signing in to Google.

  


Make sure 2-step verification is enabled. You must turn on 2-step verification to see the App Passwords option.

  


If 2-step verification is missing, the option to allow users to turn on 2-step verification is off in Google Admin. Please contact the Google Workspace admin to follow this article to enable the option.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833345/original/dgjp8iRg7ROhI3zCpydanj95cNEOA3_8qQ.jpg?1721852257)

  


7\. Once 2-step verification is enabled, Click on App passwords

  
Make sure the right email is selected from the dropdown.

  
Type password

  
Click on Next

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833353/original/Yuqm2m5Z6l9okF-x_K2Bi0-T6bHUlxBq8g.jpg?1721852300)

  


8\. Scroll down to find App Passwords >

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833359/original/wmjlCrW8apM5BKayQDx-EgTl5wYzp8OTJg.jpg?1721852346)

  


  


9\. Type an App Name, e.g. SMTP integration > Click on Create

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833368/original/QWcTs6VuvnHMzOrDn9JKneopb6sDd0_Apw.jpg?1721852383)

  


10\. Drag to copy the app password and paste it as the password when integrating Gmail SMTP

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833391/original/4wirhZnoZlKRTI5JvPnE0nHUJ_ZT6n9ygA.jpg?1721852437)

  


11\. On the top left

  
A. Search for a sub-account if you want to integrate Gmail SMTP for a location

  
B. Switch to Agency View if you want to integrate Gmail SMTP across all locations in agency settings

https://app.gohighlevel.com/settings/email_services

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833401/original/uxI0YbgNvy7V9Qn91j4PZUXMw7S87ObXTg.jpg?1721852474)

  


12\. A. Search for a sub-account if you want to integrate Gmail SMTP for a location

  
Once you are in the sub-account

  
Click on Settings at the bottom left.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833415/original/8KEl6pb42BGgeghI5dIcnsqg3ZZOKYvDMg.jpg?1721852516)

  


13\. Scroll further on the sidebar menu to Click on Email Services

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833750/original/fTO5GLS_XJjVFTIibzgJlmYfwehR1E3lgA.jpg?1721853374)

  


14\. Click on Add Service on the top right

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833764/original/qSz0YHh1HVBtlSVzTecjwvGeXWDJrFhIKA.jpg?1721853416)

  


15\. Click on the dropdown to Select Provider > Select Gmail

  
Paste the copied App Password that we generated just now in the Password field:

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833789/original/rXR7TCEAoXCVlnZBRBskg_NMfbs6Ne9_RA.jpg?1721853459)

  


16\. Enter your Gmail Login Email and click Save; done!

  

    
    
    Replies go to the email address configured as the sender/reply-to. If you are only using SMTP, replies may not automatically appear in HighLevel Conversations unless reply tracking is configured.

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833797/original/4C2NbT4Wk2TSRkrXEMthNWGS7A7hQSdVuQ.jpg?1721853495)

* * *

## **How to Enable 2 Step Verification**

  


1\. Go to [Google.com](<//Google.com>)  
  


2\. Click on the 9 dots menu here on the top right  
  


3\. Scroll down to click on Admin  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833832/original/4glC2LOOhpzwnyaKwaLz8BQn-jwttUqHWQ.jpg?1721853561)

  


  


Go to the Main menu on the top left  
  


Click on Security > Authentication > 2-step verification  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833860/original/2K196ddVHhG5SWYVASTYqaXj8VtvjlGEkw.jpg?1721853601)

  


  


  


Ensure the option to Allow users to turn on 2-Step Verification is enabled.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833874/original/MhT34FFFI0qCg8IxNBj57Bzqm8Ox0fjO5A.jpg?1721853652)

  


Refresh the manage your Google account page to see if 2-Step Verification shows up now:  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029833878/original/FF5DD42oyY7rGfEeIQnZ7rH5DBmxJdIjYw.jpg?1721853684)

* * *

## **FAQs**

  


**Q: If our company uses Google Workspace, why do I have to enter a specific email address during setup?**  
Because SMTP authentication is tied to **one mailbox account**. HighLevel needs a single Gmail/Workspace login email and its app password to send mail through Google’s SMTP servers.”

  


**Q: What is the benefit of using an app-specific password for Gmail SMTP integration?**

An app-specific password provides an additional layer of security and allows the app to access your Gmail account without you needing to input your password each time.

  


**Q: What is the significance of 2-step verification in the context of Gmail SMTP integration?**

2-step verification provides extra security to your account. When you set up an app-specific password, Google requires that you have 2-step verification enabled to ensure your account is protected.

  


**Q: Why is it recommended to use a VPN while connecting to Gmail SMTP users in the Philippines?**

A VPN can help bypass regional restrictions and add an extra layer of security when connecting to Gmail SMTP. It might be particularly beneficial for users in certain regions like the Philippines.

  


**Q: Can I use the same app-specific password for multiple applications?**

No, Google recommends creating a unique app-specific password for each application to enhance your account's security.

  


**Q: What should I do if the 2-step verification option is not showing up on my Google account?**

If the 2-step verification option is not appearing, it could mean the feature is turned off in your Google Admin settings. You would need to contact your Google Workspace admin to enable the option.

  


**Q: I have enabled 2-step verification and created an app-specific password, but my integration still isn't working. What can I do?**

Ensure you have entered the app-specific password correctly during integration. If you're still having issues, it's best to contact Gmail support.

  


**Q: Can I still use my regular Gmail password once I've set up an app-specific password?**

Yes, you can. An app-specific password does not replace your regular password but is used for specific apps to access your Gmail account.

  


**Q: Does that mean every email sent will appear to recipients as if it came from that Gmail account?**  
Usually, yes. Many SMTP providers (including Google) expect the **sender address** to match the authenticated mailbox. If the ‘From’ address doesn’t match the connected SMTP email, delivery can fail or the message can show ‘sent via’ behavior.

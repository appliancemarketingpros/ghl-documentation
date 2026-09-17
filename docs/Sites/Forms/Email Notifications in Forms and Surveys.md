# Email Notifications in Forms and Surveys

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001640-email-notifications-in-forms-and-surveys](https://help.gohighlevel.com/support/solutions/articles/155000001640-email-notifications-in-forms-and-surveys)  
**Category:** Sites  
**Folder:** Forms

---

Email Notifications let you notify team members when someone submits a Form or Survey. You can also use **Auto Responder** to automatically send a confirmation email to the person who submitted it.

  


This article explains how to configure notification recipients, customize the email, attach submission details when supported, and test your setup.

* * *

**TABLE OF CONTENTS**

  * What Are Email Notifications and Auto Responder?
  * Open Notification Settings
  * Configure Email Notifications
  * Attach Submission Details as a PDF
  * The PDF is generated from the submission record when the email is sent.
  * Configure Auto Responder
  * How to View Survey Responses After Receiving an Email Notification
  * Frequently Asked Questions


* * *

# **What Are Email Notifications and Auto Responder?**

  


**Email Notification** sends an alert to one or more designated email addresses whenever a Form or Survey is submitted.

  


**Auto Responder** sends an automatic email to the person who submitted the Form or Survey.

You can use these features to:

  * notify team members about new submissions,  
  

  * acknowledge the submitter automatically,  
  

  * customize the email subject, sender name, and reply-to address,  
  

  * and attach submission details as a PDF when supported.


* * *

## **Open Notification Settings**

  1. Go to **Sites > Forms** or **Sites > Surveys**.  
  

  2. Open an existing Form or Survey, or create a new one.  
  

  3. In the builder, select the **Notifications** tab.


  


The Notifications panel lets you configure internal Email Notifications and Auto Responder emails.

* * *

# **Configure Email Notifications**

  


  1. Open the **Notifications** tab.  
  

  2. Enable **Email Notification**.  
  

  3. Configure the available fields:


  * **Subject** — Enter the notification subject. If left blank, HighLevel uses the Form or Survey name.  
  

  * **Email (To)** — Enter one or more email addresses that should receive the notification.  
  

  * **Reply-to Email** — Enter the email address that should receive replies to the notification.  
  

  * **Sender Name** — Enter the name displayed as the sender. If left blank, HighLevel uses the applicable sub-account or agency name.


  4. Click **Save**.


  

    
    
    **Note:** Email notifications use email credits. Confirm that your account has sufficient credits.

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076942042/original/GDdHD5uUbhTTETzjwHu0CFkHJKFzo7aMog.png?1785160653)

##   


## **Attach Submission Details as a PDF**

  
When the PDF attachment option is enabled, HighLevel can include a PDF containing the submitted responses with the notification email.

  


The PDF is generated from the submission record when the email is sent.

To configure it:

  1. Open the Form or Survey.  
  

  2. Select the **Notifications** tab.  
  

  3. Enable **Email Notification** or **Auto Responder** , depending on where you want the attachment sent.  
  

  4. Enable the available option to attach the submission as a PDF.  
  

  5. Save your changes.


**Note:** Available PDF options can depend on the builder and submission type.

####   
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076942278/original/kwKXiDwHIumUlBcZ9rhnX7hL9wUz927b2g.png?1785160702)

  


  
The PDF is generated from the submission record when the email is sent.

  


#### ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064679075/original/egAEc1KiVMiWY-gZxSylv4XPEWXrN123Zg.png?1770811503)

####   


**Steps**  
  


  1. Open the form or survey editor and click the Notification tab open notifications.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076942482/original/sN5uVYaYGhWDzNb9aQIP4zjOKZ36KmL-hQ.png?1785160784)  
  

  2. Enable Email Notification or Auto Responder.  
  

  3. Auto Responder sends an automated email to the person who submits the form (email includes a copy of the information they entered in the form).  
  


  4. Save your changes.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076942515/original/LI1ZKg19SaF6hafvDFiMGDNBZ_1CSZC-tA.png?1785160813)


* * *

## **Configure Auto Responder**

  


Auto Responder sends an automatic email to the person who submits the Form or Survey.

  1. Open the **Notifications** tab.  
  

  2. Enable **Auto Responder**.  
  

  3. Configure the available fields:


  * **Subject** — Enter the email subject. If left blank, HighLevel uses the Form or Survey name.  
  

  * **Reply-to Email** — Enter the email address that should receive replies from the submitter.  
  

  * **Sender Name** — Enter the sender name. If left blank, HighLevel uses the sub-account name.


  4. Save your changes.


  


  

    
    
    **Note:** The Reply-to Email configured for Auto Responder applies to the email sent to the submitter. It does not change the Reply-to Email used for the internal Email Notification.****

  

    
    
    **Test Your Notification Settings:** After saving the form or survey, open its preview and submit a test response. Confirm that the internal notification and Auto Responder email reach the intended recipients.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076942623/original/dIVyrbNpxS6lNQ7uFvwq-NVYjPyiE2kjzQ.png?1785160848)

* * *

# **How to View Survey Responses After Receiving an Email Notification**

  


Email notifications serve as alerts only and do not include full survey responses. To view responses:

  


**Steps:**  
  


  1. Navigate to **Sites** from the left-hand menu.  
  


  2. Select the **Surveys** tab, then click **Submissions**.  
  


  3. Review the list of submissions with timestamps and answers.  
  


  4. Click an individual entry to see all responses.


* * *

# **Frequently Asked Questions**

  


**Q: Can I send email notifications conditionally, based on how someone answers a form or survey question?**

No, native email notifications in the Form Notification sidebar apply to all submissions equally. If you want conditional routing (for example, send to one team member if the answer is “Option A” and another if it’s “Option B”), you’ll need to use **Workflows**. The “Form Submitted” workflow trigger allows you to set conditions and route notifications accordingly.

  


**Q: Can I Notify More Than One Team Member?**

Yes. Add multiple valid recipient email addresses in the **Email (To)** field.

  


**Q: What Is the Difference Between Email Notification and Auto Responder?**

**Email Notification** alerts your team or designated recipients about a new submission.

**Auto Responder** sends an automatic email to the person who submitted the Form or Survey.

  


**Q: Do Auto Responder emails count toward my email credit usage just like notifications?**

Yes. Both **Email Notifications** (sent to your team) and **Auto Responder emails** (sent to the submitter) consume email credits from your account. If your credits are exhausted, neither type of email will send until credits are added. You can monitor credit usage in your account’s email reporting or billing area.

  


**Q: What happens if I enter multiple emails in the “Email (To)” field and one of them is invalid? Will the others still receive the notification?**

Yes. Notifications will still be delivered to valid addresses. Invalid addresses will fail silently and not block delivery to other recipients. However, it’s recommended to regularly verify the addresses entered in the “Email (To)” field to avoid repeated delivery failures.

  


**Q: Can I use dynamic merge fields (like {{user.email}} or {{contact.email}}) in the “Email (To)” field for notifications?**

Currently, merge fields are not supported in the “Email (To)” field. You must enter static email addresses. If you need notifications to go to dynamic recipients, set up a **Workflow** triggered by the form submission and use workflow actions to send email to the appropriate contact or user.

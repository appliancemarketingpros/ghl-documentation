# Set Defaults for Custom Values in Emails

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007825-set-defaults-for-custom-values-in-emails](https://help.gohighlevel.com/support/solutions/articles/155000007825-set-defaults-for-custom-values-in-emails)  
**Category:** Marketing  
**Folder:** Templates

---

Learn how to use default values for custom fields to keep your emails personalized, polished, and free from awkward blanks when contact information is missing.  
  


**TABLE OF CONTENTS**

  * What is it?
  * Benefits:
  * How would this work?
    * Scenario 1: Missing First Name
    * Scenario 2: Subject Line Personalization
  * How to Edit a Default Value
  * FAQs


###   
**What is it?**

Custom values make your emails feel more personal by automatically pulling information from a contact record — for example:

  
`Hi {{contact.first_name}}`  
  


Without a default, if the contact record did not contain a first name, the email would display a blank space instead.

  
Now, you can set a **default value** for custom values directly inside the email editor. This ensures your emails always look polished and complete, even when contact information is missing.

  


###   
**Benefits:**

  * **Keeps your emails sounding natural and complete** , even when contact information is missing, so recipients never see awkward gaps or broken sentences in your messaging.
  * **Prevents blank spaces from appearing in subject lines, preview text, and email content** , helping every email look polished, intentional, and professionally formatted before it reaches the recipient.
  * **Allows you to maintain personalization without depending on perfect CRM data** , making it easier to send engaging emails to contacts who may have incomplete or partially filled records.


  


  


### **How would this work?**  
  


#### _**Scenario 1: Missing First Name**_

Custom value:  
`Hi {{contact.first_name}}`

Default value:  
`there`

  


Results:

  * `Hi Sarah` (if first name exists)
  * `Hi there` (if first name is missing)


  


#### **_Scenario 2: Subject Line Personalization_**

Subject:  
`{{contact.first_name}}, your appointment is confirmed`

Default value:  
`there`

  


Results:

  * `John, your appointment is confirmed`
  * `There, your appointment is confirmed`


  


### **How to Edit a Default Value**

  1. Create or edit an email, template, workflow email, or campaign email.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071238013/original/FOpJQcuR0JF9W2pxa-c1k5rYBWhLPo6o5g.png?1778677591)
  2. Add a custom value using the custom value picker, or simply type/paste the custom value key directly into the editor. 
  3. Click on the custom value tag inside the editor.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071236710/original/YR7pQQBN4GkUq2pXj5TpP469otIhr3SBHw.png?1778677060)
  4. The edit modal will open, allowing you to configure a default value.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071236678/original/MMffNX-rqz5YW3pGRK7Ff-n8v7zr8MibQQ.png?1778677047)
  5. Add, update, or remove the default value as needed.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071236806/original/NuXrWhVq9TZFDqBsMuyVg6_2d2qKTOMYMg.jpeg?1778677105)
  6. Save your changes to apply the updated default value.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071238063/original/Bv4aUJfuRF9xaCZCYypv965Jij5wkwOuSw.png?1778677613)


  


### **FAQs**

1\. Can I set one global default for all custom values?

Not currently. Default values are configured individually for each custom value usage, giving you more flexibility based on the context of the email.

  


2\. Will the default value replace existing contact information?

No. If the contact field contains data, the actual contact value will always be used. The default only appears when the field is empty.

  


3\. Can I use default values in subject lines and preview text?

Yes. Default values can be used in subject lines, preview text, and email body content.

  


4\. Where can I use this feature?

You can use default values in workflow emails, campaign emails, bulk actions, and email templates.

  


5\. How do I know if a custom value already has a default?

Custom values with no default appear as grey tags. Once a default is added, the tag turns green.

  


6\. Can I edit the default value later?

Yes. Simply click on the custom value tag again to reopen the edit modal and update the default value.

  


7\. What happens if I do not set a default value?

If the contact field is empty and no default is configured, the email may display a blank space where the custom value is used.

  


8\. Can same custom values have different defaults if used twice in the email?

Yes. Each custom value usage can have its own unique default value depending on the message and context.

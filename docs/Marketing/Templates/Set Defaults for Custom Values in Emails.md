# Set Defaults for Custom Values in Emails

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007825-set-defaults-for-custom-values-in-emails](https://help.gohighlevel.com/support/solutions/articles/155000007825-set-defaults-for-custom-values-in-emails)  
**Category:** Marketing  
**Folder:** Templates

---

Default values help keep personalized emails complete when contact information is missing. Learn how default values work, where they can be used, how to recognize them in the editor, and how to add fallback text to custom values in HighLevel emails.

* * *

* * *

# **What are Default Values for Custom Values in Emails?**

  


Personalizing emails with custom values is a powerful way to make messages feel more relevant, but missing contact data can create awkward blanks. For example, an email may display “Hi ,” instead of “Hi Sarah,” when the contact’s first name is not saved.

  


When the related contact field is empty, HighLevel displays the default value you configured for that specific custom value usage instead of leaving the space blank.

  


You can add default values to custom values, also commonly used as merge tags, in subject lines, preview text, and email body content across email campaigns, workflow emails, bulk emails, and email templates.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071829515/original/jzoheuCcD2paS9LKd2j_cPV2IQe9-eKuOA.png?1779294916)

* * *

## **Key Benefits of Default Values for Custom Values**

  


  * **Cleaner Personalization:** Prevents blank spaces when contact fields such as first name, company name, or appointment details are missing.  
  


  * **More Professional Emails:** Keeps subject lines, preview text, and email content polished before they reach the recipient.  
  


  * **Flexible Messaging:** Allows different default values for the same custom value in different email contexts.  
  


  * **Works with Incomplete CRM Data:** Helps you personalize emails even when some contact records are incomplete.  
  


  * **Better Email Readability:** Keeps messages natural and complete, so recipients do not see awkward gaps or broken sentences.


* * *

## **How Default Values Work**

  


Default values only display when the contact field is missing or empty. They do not update, replace, or overwrite the contact’s saved CRM data. You can even use a different default value each time the same custom value appears, even within the same email. 

  


For example, if _{{contact.first_name}} _appears twice in one email, one instance can use "_there_ " as the fallback while another instance can use "_friend"_.

  


  


_**Example 1: Missing First Name**_

  


 _Hey{{contact.first_name}}, we are so glad that you signed up!_

  


**Default Value:** "_there"_

  


**Results:**

  * If first name exists: "_Hey Sarah, we are so glad that you signed up!"_
  * If first name doesn't exist: "_Hey there, we are so glad that you signed up!"_


  


  


**_Example 2: Subject Line Personalization_**

  


 _"__Hi{{contact.first_name}}, your appointment is confirmed"_

**  
**

**Default Value:** _"friend"_

  


**Results:**

  * If first name exists: _"__Hi John, your appointment is confirmed"_
  * If first name doesn't exist: _"__Hi friend, your appointment is confirmed"_


* * *

## **Visual Indicators for Default Values**

  


Custom value tags use visual indicators to help you identify whether a default value has been configured. These indicators make it easier to review an email before sending and confirm which personalization values have fallback text. Hovering over a configured custom value shows the default value tooltip.

  


  1. **Green highlighted custom value:** A default value has been set.  
  


  2. **Standard/Grey custom value:** No default value has been set.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071826354/original/BwDu1LWBs-onKEljQ9wwcXB6-xwX4vHwhA.png?1779292905)

* * *

## **How To Set Default Values for Custom Values in Emails**

  


  1. Create or edit an email, template, workflow email, bulk email action or campaign email. Add or locate the custom value you want to personalize, such as _{{contact.first_name}}._  
  
_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071827538/original/dHBKZljgIpQgk17fSo7UE2NLeJzgLr6vFA.png?1779293570)_  
  

  2. Click on the custom value to open the Default Text Editor.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071827651/original/mCN4zIMYdbA1mg5esW3NNJwalVQM-UuXuQ.png?1779293686)  
  

  3. In the Default Text Editor, enter the fallback text you want to display when the value is missing. Click **Save**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071827763/original/tr0Hdf6lYXxxcG-wrREQgeWE0_5NXJ36KQ.png?1779293777)  
  


  4. Confirm the custom value is highlighted in green, indicating that a default value has been set.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071827949/original/vV4NV7fJYZVhgFGkZntqJzMj52woAULmKg.png?1779293835)

  
  


* * *

## **How to set defaults using syntax?**

  
  
You can directly add this syntax in the email builder:  
  
`_{{default contact.firstname "there"}}_`  
  
Example: this will use the contact’s first name when available, and fall back to **“there”** when `{{contact.firstname}}` is blank.  
  


  


## **Frequently Asked Questions**

**  
**

****Q: Can I set one global default for all custom values?****

Not currently. Default values are configured individually for each custom value usage, giving you more flexibility based on the context of the email.

**  
**

**Q: Will the default value replace existing contact information?**

No. If the contact field contains data, the actual contact value will always be used. The default only appears when the field is empty.

**  
**

**Q: Can I use default values in subject lines and preview text?**

Yes. Default values can be used in subject lines, preview text, and email body content.

**  
**

**Q: Where can I use this feature?**

You can use default values in workflow emails, campaign emails, bulk actions, and email templates.

**  
**

**Q: How do I know if a custom value already has a default?**

Custom values with no default appear as grey tags. Once a default is added, the tag turns green.

**  
**

**Q: Can I edit the default value later?**

Yes. Simply click on the custom value tag again to reopen the edit modal and update the default value.

**  
**

**Q: What happens if I do not set a default value?**

If the contact field is empty and no default is configured, the email may display a blank space where the custom value is used.

**  
**

**Q: Can the same custom value have different defaults if used more than once in an email?**

Yes. Each custom value usage can have its own unique default value depending on the message and context.

* * *

## **Related Articles**

  


  * [How to use Custom Values](<https://help.gohighlevel.com/en/support/solutions/articles/48001161575>)  
  

  * [List of Merge Fields](<https://help.gohighlevel.com/en/support/solutions/articles/48001078171>)  
  

  * [Overview of Merge Fields & Custom Variables](<https://help.gohighlevel.com/en/support/solutions/articles/155000004390>)  
  

  * [How to Preview & Test Your Email Campaigns/Templates](<https://help.gohighlevel.com/en/support/solutions/articles/48001215382>)

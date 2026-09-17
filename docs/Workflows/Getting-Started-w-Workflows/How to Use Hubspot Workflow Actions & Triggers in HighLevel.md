# How to Use Hubspot Workflow Actions & Triggers in HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007955-how-to-use-hubspot-workflow-actions-triggers-in-highlevel](https://help.gohighlevel.com/support/solutions/articles/155000007955-how-to-use-hubspot-workflow-actions-triggers-in-highlevel)  
**Category:** Workflows  
**Folder:** Getting Started w/ Workflows

---

Connect HubSpot directly to HighLevel Workflows so your CRM stays clean, synchronized, and responsive in real time. This guide explains the HubSpot workflow trigger and actions, how to set them up, and practical ways to use them for contact sync, deduplication, and lifecycle-based nurturing.

* * *

**TABLE OF CONTENTS**

  * What is HubSpot Workflow Actions & Triggers?
  * Key Benefits of HubSpot Workflow Actions & Triggers
  * Supported HubSpot Trigger
  * Supported HubSpot Actions
  * How To Set Up HubSpot Workflow Actions & Triggers
  * Setting Up the HubSpot New Contact Created Trigger
  * Setting Up the HubSpot Create Contact Action
  * Common Use Cases
  * Frequently Asked Questions 
    * Related Articles


* * *

# **What is HubSpot Workflow Actions & Triggers?**

  


HubSpot Workflow Actions & Triggers allow you to connect HubSpot with HighLevel workflows so data can move between both systems through automation. This helps teams create HubSpot contacts, find existing HubSpot contacts, and start HighLevel workflows when new HubSpot contacts are created. By using HubSpot inside Workflow Builder, you can reduce manual data entry, prevent duplicate contacts, and keep sales or marketing processes moving more consistently.

  


HubSpot actions and triggers are available inside HighLevel Workflow Builder. A trigger starts the workflow when a specific HubSpot event occurs, while actions perform tasks in HubSpot after the workflow begins.

* * *

## **Key Benefits of HubSpot Workflow Actions & Triggers**

  


  


HubSpot workflow automation helps teams connect contact activity across systems without manually copying information from one CRM to another. These benefits are especially useful when HighLevel is used for marketing automation, lead capture, or customer communication while HubSpot is used for CRM management.

  


  * **Automated contact creation:** Create HubSpot contacts from HighLevel workflow events such as form submissions, appointments, tags, or other workflow triggers.


  


  * **Reduced duplicate records:** Search for an existing HubSpot contact before creating a new one to help keep HubSpot contact records clean.


  


  * **Faster lead routing:** Trigger follow-up workflows in HighLevel when a new HubSpot contact is created.


  


  * **Flexible field mapping:** Send standard and custom contact information from HighLevel into HubSpot contact properties.


  


  * **Improved workflow consistency:** Build repeatable automations that reduce manual steps for sales, marketing, and operations teams.


  


  * **Better CRM coordination:** Keep HubSpot and HighLevel processes aligned when both platforms are part of your business workflow.


* * *

## **Supported HubSpot Trigger**

  


The HubSpot trigger starts a HighLevel workflow when a matching event happens in HubSpot. This allows HighLevel to respond automatically when new contact activity begins in HubSpot.

  


### **New Contact Created**

  


The **New Contact Created** trigger starts a HighLevel workflow when a new contact is created in the connected HubSpot account.

  


Use this trigger when you want HighLevel to take action after a new HubSpot contact is added, such as sending notifications, creating tasks, applying tags, or starting follow-up communication.

* * *

## **Supported HubSpot Actions**

  


HubSpot actions allow HighLevel workflows to send or retrieve contact information from HubSpot. These actions should be configured carefully so the correct contact data is mapped, searched, or created.

  


**Internal Review Note:** Confirm the exact supported action list before publishing. The existing article references five actions in some areas but only lists two actions in another section. The final article should only include actions that are currently available in production.

###   


### **Create Contact**

  


The **Create Contact** action creates a new contact in HubSpot using information mapped from the HighLevel workflow.

Use this action when a HighLevel event captures a new lead or customer and you want that person added to HubSpot automatically.

  


Common mapped fields may include:

  


  * First name
  * Last name
  * Email
  * Phone
  * Company name
  * Website
  * Lifecycle stage
  * Lead source
  * Custom HubSpot properties


  

    
    
    **Tip:****Use a Find Contact action before Create Contact to check whether the contact already exists in HubSpot.**

  


###   


### **Find Contact**

  


The **Find Contact** action searches HubSpot for an existing contact based on a selected identifier, such as email address.

  


Use this action before creating a new HubSpot contact so the workflow can check whether a matching contact already exists.

  


Common uses include:

  


  * Preventing duplicate HubSpot contacts.
  * Routing contacts differently when a match is found.
  * Confirming whether a lead already exists in HubSpot before creating a record.
  * Using workflow conditions based on whether the contact was found.


###   


### **Get Contact by ID**

  


The **Get Contact by ID** action retrieves a HubSpot contact using the contact’s HubSpot record ID.

  


Use this action when a previous workflow step already has the HubSpot contact ID and you need to retrieve more details about that contact.

  


Common uses include:

  


  * Looking up contact data after a HubSpot trigger.
  * Pulling HubSpot contact properties into later workflow steps.
  * Verifying a specific HubSpot record before continuing the workflow.


  


  


### **Search Contact by Email**

  


The **Search Contact by Email** action searches HubSpot for a contact using the email address provided in the workflow.

  


Use this action when email is the most reliable way to identify whether a HubSpot contact already exists.

  


Common uses include:

  


  * Matching HighLevel contacts to HubSpot contacts.
  * Avoiding duplicate HubSpot records.
  * Branching workflow logic based on whether an email match exists.


###   


### **Create Association**

  


The **Create Association** action creates a relationship between HubSpot records, such as associating a contact with a company or deal.

  


Use this action when your HubSpot workflow needs connected records to stay organized for sales or account management.

  


Common uses include:

  


  * Associating a HubSpot contact with a company.
  * Associating a HubSpot contact with a deal.
  * Connecting related HubSpot records after a contact is created or found.


* * *

## **How To Set Up HubSpot Workflow Actions & Triggers**

  


A successful setup requires connecting HubSpot, selecting the correct trigger or action, mapping the right fields, and testing before publishing. Testing is especially important because it confirms that HighLevel can access HubSpot records and send data in the expected format.

  


### **Connect HubSpot in Workflow Builder**

  


  1. Go to **Automation** in HighLevel.
  2. Open an existing workflow or create a new workflow.
  3. Click **Add New Trigger** or **Add Action** , depending on what you want to configure.
  4. Select **Apps**.
  5. Choose **HubSpot**.
  6. Click **Connect** or **Connect Now**.
  7. Authorize the HubSpot account you want to use.
  8. Review the requested permissions.
  9. Complete the authorization.
  10. Return to HighLevel and confirm that HubSpot is connected.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072050244/original/lwYVqNwwW5u4fYPoA25WYFhOLm9ajxmS-g.png?1779530590)

  


  


## **Setting Up the HubSpot New Contact Created Trigger**

  


The New Contact Created trigger is useful when HubSpot is the starting point for a workflow. Once a new contact is created in HubSpot, HighLevel can continue the automation with follow-up actions, notifications, tasks, or internal processes.

  


  1. Go to **Automation** in HighLevel.
  2. Open the workflow where you want HubSpot to trigger the automation.
  3. Click **Add New Trigger**.
  4. Select **HubSpot**.
  5. Choose **New Contact Created**.
  6. Confirm the connected HubSpot account.
  7. Configure any available trigger settings.
  8. Click **Save Trigger**.
  9. Use **Test Trigger** or **Find New Records** to confirm that HighLevel can detect HubSpot contact records.
  10. Publish the workflow when testing is successful.


  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072050325/original/lPh6V0W9bX29EQV2d55QeGTOhqpmeJVoHA.png?1779530677)

  


  


## ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072050481/original/XZXVVYCfe4FMqr6OTSF61oBiSXxRw5bZ9g.jpeg?1779530928)

  


  


## **Setting Up the HubSpot Create Contact Action**

  


The Create Contact action sends contact data from a HighLevel workflow into HubSpot. Accurate field mapping ensures that each HubSpot contact is created with the right name, email, phone number, and custom property values.

  


  1. Open the workflow where you want to create a HubSpot contact.
  2. Add the workflow trigger that should start the process.
  3. Click **Add Action**.
  4. Select **HubSpot**.
  5. Choose **Create Contact**.
  6. Confirm the connected HubSpot account.
  7. Map the required HubSpot fields.
  8. Map any optional HubSpot properties needed for your process.
  9. Save the action.
  10. Test the action.
  11. Review the test result in HighLevel and confirm the contact was created in HubSpot.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072050394/original/QOAT2Iroh-iwUlMwvQkqqIqhO7OiLI0Txg.png?1779530760)

  


  


  


##   


## ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072050467/original/loJwUTpv7T_2-XWC9JNM2SppKBclolRSLA.jpeg?1779530902)

  


  


**Recommended field mapping example:**

  


  * HubSpot First Name → HighLevel Contact First Name
  * HubSpot Last Name → HighLevel Contact Last Name
  * HubSpot Email → HighLevel Contact Email
  * HubSpot Phone → HighLevel Contact Phone
  * HubSpot Company → HighLevel Contact Company Name
  * HubSpot Lead Source → Workflow source, form name, or custom value


* * *

## **Common Use Cases**

  


HubSpot workflow actions and triggers are useful when HubSpot and HighLevel are both part of the customer journey. These examples show how teams can automate contact creation, contact lookup, and follow-up processes.

###   


### **Create a HubSpot Contact from a HighLevel Form Submission**

  


Use this workflow when leads enter HighLevel through a form and need to be created in HubSpot.

  


Example workflow:

  1. Trigger: Form Submitted.
  2. Action: Search Contact by Email or Find Contact.
  3. If/Else: Contact found?
  4. If no, Create Contact in HubSpot.
  5. If yes, continue with the next follow-up step.


###   


### **Start a HighLevel Workflow When a HubSpot Contact Is Created**

  


Use this workflow when HubSpot is the source of new contact creation and HighLevel should handle follow-up actions.

  


Example workflow:

  1. Trigger: HubSpot New Contact Created.
  2. Action: Send internal notification.
  3. Action: Add tag in HighLevel.
  4. Action: Create task or assign user.
  5. Action: Send follow-up communication if appropriate.


###   


### **Prevent Duplicate Contacts in HubSpot**

  


Use this workflow when multiple lead sources may send the same person into HubSpot.

  


Example workflow:

  1. Trigger: Contact Created, Form Submitted, or another HighLevel trigger.
  2. Action: Search HubSpot by email.
  3. If contact exists, skip Create Contact.
  4. If contact does not exist, Create Contact.


###   


### **Associate a HubSpot Contact with a Company or Deal**

  


Use this workflow when a contact should be connected to another HubSpot record for account management or sales tracking.

  


Example workflow:

  1. Trigger: Contact created or updated in HighLevel.
  2. Action: Find or Create HubSpot Contact.
  3. Action: Retrieve the company or deal record ID.
  4. Action: Create Association.
  5. Test the association inside HubSpot.


* * *

## **Frequently Asked Questions**

**Q: Are HubSpot actions premium workflow actions?**

Yes. All five HubSpot actions (Create Contact, Find Contact, Get Contact by ID, Search Contact by Email, Create Association) are premium and consume premium action credits at the standard automation rate.

  


**Q: Is the New Contact Created trigger premium too?**

No. The premium designation applies to the **actions**. The New Contact Created trigger is powered by a HubSpot webhook and can fire without consuming premium action credits, though any premium actions you add after it will still bill as usual.

  


**Q: Do I need a paid HubSpot plan to use this integration?**

No. The integration works with HubSpot’s free CRM tier. Some advanced features on the HubSpot side (like certain workflow automations or specialized property types) may require paid Marketing or Sales Hub plans, but those limits are set by HubSpot, not HighLevel.

  


**Q: How does deduplication work when creating HubSpot contacts?**

Email is the primary deduplication key for HubSpot contacts. To avoid duplicates, use **Search Contact by Email** before **Create Contact** , then only create a new record when no match is found.

  


**Q: Can I create or update custom properties on HubSpot contacts from a workflow?**

Yes. The Create Contact action supports any property defined on the HubSpot Contact object (standard or custom). Create the property in HubSpot first, then map the appropriate workflow variable to it. Unknown property names are ignored by HubSpot on submit.

  


**Q: What is Create Association used for in real workflows?**

Create Association links a contact to a Company, Deal, or Ticket in HubSpot. This is useful for account-based selling, deal automation, and support workflows where you want all related records connected and visible from both sides.

  


**Q: Can I use workflow variables in HubSpot fields?**

Yes. All HubSpot action fields support inline workflow variables (for example, `` or date/time helpers). This lets you dynamically map form responses, contact fields, or values from previous steps into HubSpot properties.

  


**Q: Will New Contact Created fire for contacts created by imports or other integrations?**

Yes. The trigger fires for any new contact created in HubSpot—via forms, manual entry, imports, or other integrations unless you restrict it with filters. Use trigger filters to narrow enrollment to specific sources or lifecycle stages if needed.

  


**Q: What happens if a HubSpot action fails (for example, due to an invalid email)?**

If an action like Create Contact fails, the error is logged in the workflow execution details. The workflow can continue based on your branching; for critical paths, add a fallback branch (for example, notify an admin or log to a Slack channel) when an error occurs.

  


**Q: Can I use multiple HubSpot steps in the same workflow?**

Yes. You can chain multiple HubSpot triggers and actions (where applicable) within a single workflow—for example, trigger on New Contact Created, then Find Contact in HighLevel, Create Contact in HighLevel, and finally Create Association back in HubSpot for that same contact.

* * *

### **Related Articles**

  


  * [Getting Started with Workflows](<https://help.gohighlevel.com/a/solutions/articles/155000002288?portalId=48000045315>)


  


  * [Import Data from HubSpot (HubSpot Importer)](<https://help.gohighlevel.com/a/solutions/articles/155000007947?portalId=48000045315>)


  


  * [Hubspot to HighLevel (Migration Guide)](<https://help.gohighlevel.com/a/solutions/articles/155000003388?portalId=48000045315>)


  


  * [Workflow Action – Create Company or Associated Contact](<https://help.gohighlevel.com/a/solutions/articles/155000006574?portalId=48000045315>)


  


  * [Workflow Action – Update Contact Field](<https://help.gohighlevel.com/a/solutions/articles/48001214441?portalId=48000045315>)

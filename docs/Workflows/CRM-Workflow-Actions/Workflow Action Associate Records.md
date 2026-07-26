# Workflow Action: Associate Records

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007718-workflow-action-associate-records](https://help.gohighlevel.com/support/solutions/articles/155000007718-workflow-action-associate-records)  
**Category:** Workflows  
**Folder:** CRM Workflow Actions

---

**TABLE OF CONTENTS**

  * Overview
  * Prerequisites
  * Steps
  * Use cases


##   
Overview

The **Associate Records** workflow action allows you to automatically associate records across your CRM based on matching field values.

  


You can create associations between Contacts, Companies, Opportunities, and Custom Objects, depending on the object the workflow runs on and the associations configured in your sub-account.

  


The action is available in **Contact, Company, and Custom Object workflows**.

  
You can use this action to:

  * Associate records across supported CRM objects and Custom Objects based on the associations configured in your sub-account.
  * Find records using one or more field-based filters.
  * Use merge fields from the enrolled record as filter values.
  * Associate the earliest created, latest created, or all matching records.
  * Apply an existing association label.
  * Create associations between different objects.


  
When multiple filters are added, a record must meet all the conditions to qualify.

  


**  
**
    
    
    **Note:** Associate Records is currently available through Labs. To enable it, go to **Settings → Labs** , find **Associate Records Workflow Action** , and turn it on for the sub-account.

  


  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069568500/original/JLV2x7psJNLhTHPD2KgG-1ARnc7oc3cMag.png?1776754582)

## **![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076480878/original/2fmspHg8voBB3BnO0Ym5crxNyFkK4J4MTQ.png?1784631630)**  


## Prerequisites

Before using the Associate Records action, make sure that:

  1. The source and target objects are available in the sub-account.
  2. An association has been created between the two objects.
  3. The records contain fields that can be used to identify the correct matches.


Associations can be created under:

**Settings → Objects → Select an object → Associations**

For example, to associate Contacts with Property records, an association must first be created between the **Contact** and **Property** objects.

Only applicable user-defined association labels are available for selection in this action. If the target object or association label does not appear, review the association configuration between the two objects.

  


  


## Steps

  


**I. Action Name**

Enter a name for the workflow step. This field is used only to identify the action inside the workflow builder.

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076482509/original/BwDeBSse-eLCKxQjAYCc9galHrxEZnzYHw.png?1784632340)**

  


**II. Create Association With (Required)** -

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076482711/original/kQMLU69mrIzfxbEmarWAHC29sOl-F7TOcw.png?1784632481)**  


Select the object containing the records you want to find and associate with the record enrolled in the workflow.

The available options depend on:

  * The object the workflow runs on
  * The associations configured in the sub-account
  * Whether the relationship is user-defined or managed natively by HighLevel


Only supported target objects appear in the dropdown.

For example:

  * A Contact workflow can associate a Contact with a Custom Object, such as Property or Policy.
  * A Custom Object workflow can associate its record with a Contact, Company, Opportunity, or another Custom Object, provided a supported association exists.


To create associations between additional objects, go to:

**Settings → Objects → Select an object → Associations**

  


> **Note:** Contact-to-Opportunity associations are not supported through this action. Use the native Opportunity association instead.

  


**III. Filter Records to Associate**

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076496383/original/zf_mw_qQShMxZpXyLcVvSpPuNZBs404Kaw.png?1784638556)**  


The rules used to find the right target record(s). Each filter contains:

  * **Field:** A field from the selected target object.
  * **Operator:** The condition used to evaluate the field.
  * **Value:** A fixed value or a merge field from the enrolled record, where required


Click + Add field to add more filter rows. Multiple rows are combined using AND logic — all must match for a record to qualify.

  


Example filters:

Field| Operator| Value  
---|---|---  
Bedrooms| Equals| Contact’s preferred bedrooms  
City| Is| Contact’s preferred city  
Property Type| Is| Contact’s preferred property type  
Property Name| Is not empty| No value required  
  
  


  


**IV. When Multiple Records Match (Required)**

Decides what happens when more than one target record matches your filter:

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076496632/original/U38cN9_k-zQXAdSksukdFr9r1WjEiu7VgQ.png?1784638676)

**  
**

  * **Associate with earliest created record:** Associates the enrolled record with the oldest matching record.
  * **Associate with latest created record:** Associates the enrolled record with the newest matching record.
  * **Associate with all matching records:** Associates the enrolled record with every matching record, subject to the association’s configured limits.


  
When all matching records are selected, associations are processed in bulk and may take a short time to appear.

  


  


**V. Association Label**

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076496817/original/RUwjjUrFWoQ4u9FFsaI_eA35T4fVzyvPZQ.png?1784638771)

Select the label that describes the relationship between the records, such as **Policy Holder** , **Primary Contact** , or **Potential Buyer**.

  


This field is required when displayed.

When associating a Company with a Contact, or a Contact with a Company, the standard Company and Contact relationship is applied automatically, so this field is not displayed.

  


##   


## Use cases

  


**Use case 1 : Real Estate - Associate a Buyer with Matching Properties**

  


A real estate agency stores its listings in a **Property** Custom Object. When a buyer submits their preferences, the workflow automatically associates the contact with properties that match their requirements.

  


**Setup**

  * Trigger → Contact Created
  * Create Association With → Property
  * Filter Records to Associate:


  * Bedrooms Equals {{contact.preferred_bedrooms}}
  * City Is {{contact.preferred_city}}
  * Property Type Is {{contact.preferred_property_type}}


  * When Multiple Records Match → Associate with all matching records
  * Association Label → Potential Buyer


  


What this unlocks: The contact is automatically connected with all suitable properties, allowing the agency to manage matching listings and follow-ups without manually linking records.

  


****Use case** 2: Insurance - Link a New Policy to the Policyholder**

  


An insurance agency stores policies in a **Policy** Custom Object. When a Policy record is created, the workflow finds the correct contact and associates the policy with them.

  


**Setup**

  * Trigger → Policy Record Created 
  * Create Association With → Contact
  * Filter Records to Associate:
    * Phone Is {{policy.policyholder_phone}}
  * When Multiple Records Match → Associate with latest created record
  * Association Label → Policy Holder


  


What this unlocks: Every policy lands on the right contact record automatically. Renewal reminders, claim notifications, and cross-sell campaigns all reference the exact policy — no manual linking by the service team.

  


  


**Example 3: Home Services - Route New Jobs to the Right Technician**

  


A plumbing company stores service requests in a **Job** Custom Object and manages technicians as Contacts. When a Job record is created, the workflow finds a technician serving the same ZIP code and associates them with the job.

  


**Setup**

  * Trigger → Job Record Created
  * Create Association With → Contact
  * Filter Records to Associate:
    * Service Zip Equals {{job.zip_code}}
    * Role Is "Technician"
  * When Multiple Records Match → Associate with earliest created record
  * Association Label → Assigned Technician


  


What this unlocks: Each job is automatically connected with a matching technician, helping dispatchers quickly identify who should handle the job without manually linking the records.

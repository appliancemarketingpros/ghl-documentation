# Workflow Action – AI Extract Data

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007992-workflow-action-ai-extract-data](https://help.gohighlevel.com/support/solutions/articles/155000007992-workflow-action-ai-extract-data)  
**Category:** Workflows  
**Folder:** Workflow AI Workflow Actions

---

**_This article explains how to use the AI Extract Data action in workflows to pull structured data from unstructured text. You’ll find step-by-step configuration instructions, details on available templates and data types, practical use cases, and answers to common questions._**

  
  


**TABLE OF CONTENTS**

  * Overview
  * Key Benefits
  * Action Details
  * How to Configure
  * Using Extracted Data in Downstream Actions
  * Use Cases
  * Frequently Asked Questions  
  


## **Overview**

The AI Extract Data action uses AI to extract structured data fields from any unstructured text input – such as an email body, webhook payload, SMS message, or AI-generated output. You define the fields you want to extract (e.g., name, email, phone, order ID), and the AI parses the input and returns those fields as structured variables that can be used in subsequent workflow actions. This eliminates the need to manually parse unstructured data or build complex conditional logic to extract information from free-form text.

**Note:****This is a premium action. Each execution incurs additional charges.**

## **Key Benefits**  
  


  * **Parse Any Unstructured Input:** Extract structured fields from email bodies, webhook payloads, SMS messages, GPT outputs, form responses, and more.
  * **Flexible Data Schema:** Define exactly the fields you need to extract, with support for multiple data types (Text, Email, Phone, Number, Date).
  * **Pre-built Templates:** Get started instantly with templates for common extraction patterns like contact information, lead details, order data, and events.
  * **Additional Context for Accuracy:** Provide optional context about the input format to improve extraction accuracy.
  * **Downstream Variable Access:** Every extracted field becomes a variable you can use in subsequent workflow actions – update contact fields, send personalized messages, create opportunities, and more.


## **Action Details**

**Field**| **Description**  
---|---  
**Action Name**|  A custom name for the action. Defaults to “AI extract data.”  
**Extract From ***|  The unstructured text input from which data will be extracted. Select a custom value (e.g., an email body, webhook payload, SMS content, or output from a previous action). This is a required field.  
**Additional Context**|  Optional supplementary context to help the AI extract data more accurately. For example: “The content is a Zillow lead notification email. Phone numbers may appear in different formats.”  
**Templates**|  Pre-built extraction templates for common use cases: Contact info, Lead details, Order info, and Event. Selecting a template auto-populates the data fields. You can modify, add, or remove fields after applying.  
**Data Fields**|  The structured fields to extract from the input. Each field has a Name (variable key), Type (Text, Email, Phone, Number, or Date), and an optional Description to guide the AI.  
  
  


## **How to Configure**

**Step 1: Add the Action**

In your workflow, click the + icon to add a new action, then search for AI extract data and select it.

**Step 2: Set the Input Source**

In the Extract From field, use the custom value picker to select the input you want to parse. This can be any text-based value from earlier in the workflow, such as an email body, a webhook payload field, an SMS message, or the output from a previous AI action.

**Step 3: Add Context (Optional)**

In the Additional Context field, provide any supplementary information that might help the AI extract data more accurately. For example, you might specify the format of the source (e.g., “This is a Zillow lead notification email. Phone numbers may appear in different formats.”). This field also supports custom values.

****

**_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071768255/original/fgR65QM15BubX0_CBonGl1fcf2mZXrx4Ow.png?1779268762)The AI Extract Data action panel with Extract From, Additional Context, and Data sections._**

**Step 4: Define Data Fields**

In the Data section, define the fields you want the AI to extract. You have two options:

Option A – Use a Template: Click one of the pre-built templates (Contact info, Lead details, Order info, or Event) to auto-populate a set of commonly used fields. You can then modify, add, or remove fields as needed.

Option B – Define Custom Fields: Click \+ Add data to manually create each field. For each field, provide:

  * **Name:** The variable key for this field (e.g., full_name, order_id, total_amount). This becomes the variable name in downstream actions.
  * **Type:** The data type – Text, Email, Phone, Number, or Date. This helps the AI identify and format the extracted value correctly.
  * **Description (Optional):** A hint to guide the AI on what to look for (e.g., “Phone number with area code, e.g. +1 (555) 234-5678”). Adding a description improves extraction accuracy.


 _![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071768360/original/fTL4NGmdnAHh6JDmA_q9xplj814mUfTdfw.png?1779268792)Custom data fields defined manually with Name, Type, and Description._

**Step 5: Save the Action**

Click Save action to save the configuration. The extracted data fields will be available as variables in all subsequent actions in the workflow.

**Templates**

Templates provide pre-built sets of data fields for common extraction patterns. Selecting a template auto-populates the fields, which you can then customize. The following templates are available:

**Contact Info**

**Extracts standard contact information. Pre-populated fields:**

**Name**| **Type**| **Description**  
---|---|---  
full_name| Text| The person’s full name, e.g. Sarah Johnson  
email| Email| Email address, e.g. sarah@example.com  
phone| Phone| Phone number with area code, e.g. +1 (555) 234-5678  
  
****

**_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071768452/original/YWqbBlXSDGuni-TPXzoi1kFxX-RgHq-Jig.png?1779268822)The Contact info template auto-populates full_name, email, and phone fields._**

**Order Info**

**Extracts order and transaction data. Pre-populated fields:**

**Name**| **Type**| **Description**  
---|---|---  
order_id| Text| Order or transaction ID, e.g. ORD-2026-48291  
items| Text| Items or services ordered, e.g. 3x Widget Pro, 1x Stand  
total_amount| Number| Total monetary amount, e.g. 2450.00  
order_date| Date| Date the order was placed  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071768498/original/pRNq15yQ6vxlKnJZirM5qT8FNUxGDvCqHw.png?1779268857)**

**_The Order info template auto-populates order_id, items, total_amount, and order_date fields._**

  
  


## **Using Extracted Data in Downstream Actions**

**Every data field you define in the AI Extract Data action becomes available as a variable in all subsequent workflow actions. You can reference these extracted values using the custom value picker in any downstream action.**  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071768925/original/37WFLyFHoS07SIpi-Ox72oJhe4HWG5x2LQ.png?1779269061)**

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071768968/original/QWztB-53kVmW5lMReqc7i2Y4J6n5uH2Rhw.png?1779269077)**  


For example, if you defined a field named full_name with type Text, you can use it in a subsequent Update Contact action to set the contact’s name, or in a Send Email action to personalize the message.

##   
**Use Cases**

**1\. Parsing Lead Notification Emails**

Scenario: You receive lead notification emails from a third-party platform (e.g., Zillow, Realtor.com) in your inbox. Each email contains the lead’s name, phone number, and property interest, but in unstructured text. You want to automatically extract and save this information to the contact record.

**Setup:**

  * **Trigger:** Inbound Email
  * **Action 1:** AI Extract Data – Extract From: email body. Context: “Zillow lead notification email. Phone numbers may appear in different formats.” Template: Contact info.
  * **Action 2:** Update Contact – Map extracted full_name, email, and phone to contact fields.


**2. Extracting Order Data from Webhook Payloads**

Scenario: An external system sends order confirmation data via webhook, but the payload is a raw text block rather than structured JSON. You need to extract the order ID, items, and total amount to create an opportunity or update a custom field.

**Setup:**

  * **Trigger:** Inbound Webhook
  * **Action 1:** AI Extract Data – Extract From: webhook body. Template: Order info.
  * **Action 2:** Create Opportunity – Use extracted order_id as name, total_amount as monetary value.


##   
**Frequently Asked Questions**

**Q: What types of input can I extract data from?**

Any text-based input available in the workflow – email bodies, webhook payloads, SMS messages, GPT/AI outputs, form response text, or any custom value from a previous action.

**Q: Do I have to use a template, or can I define my own fields?**

Templates are optional. You can use a template as a starting point and modify it, or skip templates entirely and define your own custom fields from scratch using the + Add data button.

**Q: What data types are supported?**

Five data types are supported: Text (general string), Email (email address), Phone (phone number), Number (numeric value), and Date (date value). Choosing the correct type helps the AI identify and format the extracted value accurately.

**Q: What does the Description field do?**

The Description is an optional hint that guides the AI on what to look for. For example, adding “Phone number with area code, e.g. +1 (555) 234-5678” helps the AI correctly identify and format phone numbers. More specific descriptions lead to more accurate extractions.

**Q: How do I use the extracted data in the next step?**

Each extracted field becomes a variable available in the custom value picker of all subsequent actions. For example, if you defined a field named “full_name,” you can reference it in an Update Contact, Send Email, or any other action downstream.

**Q: What happens if the AI can’t find a field in the input?**

If the AI cannot find a matching value for a defined field, that field’s variable will be empty. Your workflow should account for this by using If/Else branches or by checking for empty values before using them in critical actions.

**Q: Does the Additional Context field improve results?**

Yes. Providing context about the input format (e.g., “This is a Zillow lead notification email” or “The payload contains order data from Shopify”) helps the AI understand the structure and extract more accurately. It’s optional but recommended for non-standard or complex inputs.

**Q: Is this a premium action?**

Yes. The AI Extract Data action incurs additional charges per execution. The premium badge is visible at the top of the action panel when configuring it.

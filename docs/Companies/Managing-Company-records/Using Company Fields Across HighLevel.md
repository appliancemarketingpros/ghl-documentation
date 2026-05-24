# Using Company Fields Across HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008006-using-company-fields-across-highlevel](https://help.gohighlevel.com/support/solutions/articles/155000008006-using-company-fields-across-highlevel)  
**Category:** Companies  
**Folder:** Managing Company records

---

This article explains how to use **Company fields** — both standard and custom — as **custom values** (merge fields) in Workflows, Email Builder, Email Campaigns, Conversations, Documents & Contracts, Bulk Actions, and Conversation AI.

  


**TABLE OF CONTENTS**

  * Overview
  * Where Company Fields Can Be Used
  * Supported Fields
  * How to Use Company Fields
  * Points to Remember


# Overview

Company fields store business-level information such as name, website, address, industry, or any custom attributes you've defined on the Company object. These fields can be inserted as **custom values** in any supported tool to personalize content based on the Company associated with a Contact.

Company fields appear under a dedicated **Company** group inside the **Custom Value Picker**.

  


  


# Where Company Fields Can Be Used

Company fields are supported across:

  * **Workflows** — any action that supports custom values (Send Email, Send SMS, Update Contact, Internal Notification, etc.)
  * **Email Builder** — email templates and email content
  * **Email Campaigns** — campaign emails sent to multiple recipients
  * **Conversations** — 1:1 messages
  * **Documents & Contracts** — contracts, proposals, and agreement templates
  * **Bulk Actions** — bulk send operations
  * **Conversation AI** — AI agent responses


  


# Supported Fields

Both **standard** and **custom** Company fields can be selected from the Custom Value Picker:

**Standard fields:**

  * Name
  * Email
  * Phone
  * Website
  * Address
  * City
  * State
  * Country
  * Postal Code
  * Description


**Custom fields:**

  * Any custom field defined on the Company object (Text, Number, Date, Dropdown, etc.)


  


# How to Use Company Fields

  1. Open any supported tool (e.g., Email Builder, a Workflow Send Email action, or a Document template)
  2. Click the **Custom Value Picker** icon in the editor toolbar.
  3. Select **Company** from the field group list.
  4. Pick the standard or custom Company field you want to insert (e.g., **Name** , **Website** , or a custom field like **Industry**).
  5. The corresponding custom value tag (e.g., `{{business.name}}`) is inserted at the cursor.
  6. Save your changes. At runtime, the tag resolves to the Company associated with the Contact.


* * *

# Points to Remember

  * Company fields resolve based on the Company associated with the Contact.
  * If a Contact has no Company associated, the custom value tag resolves to blank.
  * If a Company field (standard or custom) is empty, the corresponding tag renders as blank — no fallback text is inserted.
  * Updates to a Company's field values reflect the next time a custom value is resolved.
  * New custom fields added to the Company object automatically appear in the Custom Value Picker.

# Pre-Built A2P Campaign (Widget-First) Registration Flow

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007437-pre-built-a2p-campaign-widget-first-registration-flow](https://help.gohighlevel.com/support/solutions/articles/155000007437-pre-built-a2p-campaign-widget-first-registration-flow)  
**Category:** Phone System  
**Folder:** A2P registration

---

**Overview**

  


The **Quick Setup (** Pre-Built A2P Campaign) registration flow is a structured campaign submission experience designed to:

  * Improve compliance accuracy

  * Reduce carrier rejections

  * Eliminate manual compliance writing

  * Prevent classification errors

  * Streamline the A2P registration process


This flow enforces a **Chat Widget–based opt-in method** and automatically applies carrier-aligned compliance standards.

By locking required compliance elements and auto-generating mandatory disclosures, the system significantly reduces submission errors and approval delays.

  


> **Note:** This campaign registration flow is not available for:
> 
>   * Mixed use-case campaigns
> 
>   * Sole Proprietor (Sole-prop) campaigns
> 
> 


* * *

**Accessing the Pre-Built Campaign Flow**

  


Users can now select **“Quick Setup”** when starting Campaign Registration in the Standard A2P flow.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155068347197/original/_TzRHItSj4GNDEfvgKcqQoQCVZ3VFoWQNw.png?1775130286)

  


This guided experience:

  * Enforces **Chat Widget as the only opt-in method**

  * Automatically generates compliant consent language

  * Locks required compliance elements

  * Prevents financial and marketing misclassification

  * Reduces rejection risk

  * Automatically attaches the compliant widget to the campaign  
  


    
    
    **IMPORTANT NOTE-_READ BEFORE SELECTING "CHAT WIDGET"_**
    
    If you are selecting **Chat Widget** for your A2P campaign
    You **MUST remove consent checkboxes** from all other forms on your website. 
    Having consent checkboxes on other forms while using Chat Widget as your opt-in method may result in Campaign rejection. 
    
    **Before Proceeding: **
    
    **1.** Remove consent checkboxes from all website forms
    **2.** Ensure Chat Widget is the only opt-in method being used
    
    

  


* * *

## **Messaging Use Case Selection**

Messaging Use Case Selection defines the type of messages your campaign will send and determines how the campaign is categorized during registration.

The flow includes a structured two-step selection process.

### **Step 1: Message Type**

  


Option| Description  
---|---  
**Marketing / Promotional**|  Advertising, offers, sales, promotions  
**Transactional / Non-Marketing**|  Informational or service-related messages  
  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155068347327/original/HdjtIRW1tkzKPIn5WGJo2lp99t8TL9yEXg.png?1775130351)**

###   


### **Step 2: Use Case Selection**

  


The available use cases depend on the selected message type.

#### If **Marketing / Promotional** is selected

  * Only **Marketing** is available.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066293348/original/rOr7djVCvi1tJ1A7ZSosefkilG92cQ53QA.png?1772721869)


#### If **Transactional/Non Marketing** is selected:

  * the system automatically assigns **Customer Care**.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155068348315/original/ZR2MPyamENkPW5og0h4Bpj1V5rQquS2Pbw.png?1775130790)


  


For transactional Chat Widget campaigns, use case selection is not shown as a user choice.

  


### _**Why This Structure Matters**_

This controlled selection process:

  * Prevents incompatible combinations

  * Reduces classification errors

  * Aligns campaigns with carrier requirements

  * Decreases rejection rates


* * *

## **Automatic Age Gating (Carrier-Compliant)**

Age gating is automatically enforced when:

  * Age-gated content is selected![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066294376/original/OS_H8g6TfRLYN55pKf4TK8C3F3ZbTGcg1g.png?1772722275)  


### When Triggered:

Action| System Behavior  
---|---  
Age-gated checkbox selected| Date of Birth (DOB) field appears  
DOB field| Mandatory and non-removable  
Submission| Blocked until DOB is completed  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066296762/original/mjIq_2hR4l_m2WgQwQUdX3n2rGXyU0-_XA.png?1772723455)

  


**Note** \- 1. If age-gated content is not selected, the DOB field does not appear.

2\. This ensures automatic compliance for regulated industries.

* * *

## **Auto-Generated Compliance Widget**

The system automatically generates a compliant Chat Widget that includes:

  * Business name injected into disclosure language

  * Required disclosure text

  * STOP/HELP instructions

  * Data rate disclosure

  * Message frequency disclosure

  * Campaign attachment

  * Embed code generation![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066294824/original/Lg7XRWmVgS3i3vFeBDo4aFqjPsYvnoR3Ug.png?1772722469)


###   


### **Locked Compliance Controls**

Users cannot:

  * Edit disclosure text

  * Remove required fields

  * Add custom compliance fields

  * Modify compliance language

  * Select alternative opt-in methods


This ensures consistent compliance and reduces manual errors.

* * *

## **Widget Structure**

###  _Required (Locked Fields)_

Field| Status  
---|---  
Phone Number| Mandatory  
Disclosure Block| Locked  
STOP/HELP Language| Locked  
Data Rate Disclosure| Locked  
Message Frequency Disclosure| Locked  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066295506/original/UgErNUBlbBNpcwjCJ6vPhSYMIjG5AnMBEQ.png?1772722830)  


###  _Conditional_

Field| Condition  
---|---  
Date of Birth| Mandatory if age-gating is triggered  
  
###   


###  _Optional_

Field| Editable?  
---|---  
Name| Yes  
Message Field| Yes  
UI Styling (colors/header only)| Yes  
  
  


###  _Removed_

Removed Item| Reason  
---|---  
Email Field| Not required for SMS compliance  
Custom Compliance Fields| Prevents deviation from carrier-approved language  
Editable Disclosure Text| Prevents compliance violations  
Opt-in Method Selector| Widget-only enforcement  
  
* * *

## **Marketing Consent Checkbox**

For **Marketing / Promotional** campaigns:

  * A dedicated **Marketing Consent checkbox** is now included.

  * The checkbox is mandatory before submission.

  * Users cannot proceed without explicitly confirming marketing consent.


This adds an additional compliance safeguard for promotional messaging.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066296668/original/Wf6gwwvCWuN9KmbMNqbkcrm0nQDLFF6pRw.png?1772723418)

* * *

## **Read-Only Widget Preview**

Users can preview:

  * The full widget

  * Disclosure placement

  * DOB field (if triggered)


The preview is non-editable to maintain compliance integrity.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066296401/original/wICXY-axuBqoD1HbSoU0oxLSTfXfX2b_xw.png?1772723258)

  


* * *

## **Compliance Reminder When Copying Widget Code**

When you click **Continue** , you are presented with a compliance reminder that highlights an important requirement:

  * The **Chat Widget must be the only SMS opt-in method on the website.**

  * Users must **remove SMS consent checkboxes or disclosures from all other website forms** such as contact forms, lead forms, landing page forms, or appointment forms.


This reminder helps ensure businesses configure their websites correctly before proceeding with the campaign setup and helps prevent **A2P campaign rejections due to multiple SMS opt-in methods.**

##   
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066854772/original/k5Njw-GEEyQXQg8dizfZJv44Vnx0tRxumA.png?1773391071)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066854687/original/EXcCdsGidT7eBzLVhuR0iCt1kASqMGEPtA.png?1773391048)

* * *

## **Final Consent Review**

Prior to submission:

  * Required fields are auto-filled

  * Compliance sections are locked

  * Sample messages are generated

  * Opt-in method is defined

  * Website compliance checklist confirmation is required


This final review ensures that all compliance elements are correctly configured before submission.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066855028/original/V5w2tgoDCQkKy28Vu4_0A5bghCeqXRiHOA.png?1773391203)

  


At this stage, users cannot:

  * Edit disclosure text

  * Remove required fields

  * Add consent checkboxes

  * Edit any compliance fields

  * Select alternative opt-in methods


All compliance elements remain non-editable to ensure consistency and prevent submission errors.  
  
**Note** \- The **Business Website Compliance Checklist** now includes an additional confirmation item requiring users to verify that:

  * The **Chat Widget is the only SMS opt-in method on the website** , and

  * **SMS consent checkboxes or disclosures have been removed from all other website forms or flows.**


This ensures customers review and acknowledge this requirement **earlier in the campaign setup process.**

**  
**

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066855139/original/yzPSJ7QLJtUtzr4hveLOD3BSKaUc95Eh-A.png?1773391261)**

  


* * *

**AI Validation for Chat Widget Installation**

  


We now automatically validate that the **LeadConnector Chat Widget** is present on the **business website URL submitted during Brand setup**.

  


This **AI-based validation scans the website** to confirm that the chat widget has been correctly installed. The validation occurs when users **click on “Review Application”** , triggering a **Compliance Review** that checks whether the LeadConnector chat widget is integrated on the website.

  


This helps prevent campaign submissions where the chat widget has **not yet been integrated** , reducing the likelihood of **campaign rejections due to missing or incorrect SMS opt-in implementation**.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066857743/original/jD9yeaagMx-NiKaUvGgqZ_gB-Q-93x6p2A.png?1773392731)  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066857767/original/nj-FiiQ_hU6E95tOUuSf2eDryjr2ZAunSA.png?1773392745)

  


### **Additional compliance checks for Chat Widget campaigns**

  


The Pre-Built A2P Campaign (Widget-First) flow includes additional compliance checks to help reduce carrier rejections for Chat Widget campaigns.

  


**Chat Widget installation validation**

  


Before submission, HighLevel validates that the LeadConnector Chat Widget is present on the business website used in the registration flow.

  


**Compliance reminder when copying widget code**

  


When you copy the Chat Widget installation code, HighLevel reminds you that the chat widget must be the only SMS opt-in method on the website. Remove SMS consent checkboxes or disclosures from other website forms or flows before you continue.

  


**Website compliance checklist update**

  


The Business Website Compliance Checklist includes a confirmation that the chat widget is the only SMS opt-in method on the website and that other website forms or flows do not contain SMS consent checkboxes or disclosures.

  


**Required confirmation before submission**

  


Before you submit the campaign, you must confirm that:

  


the chat widget is the only SMS opt-in method on the website, and

other website forms or flows do not include SMS consent checkboxes or disclosures.

* * *

### **Required Confirmation Before Campaign Submission**

  


After the compliance validation is completed and users click **Submit Application** , a **Submission Review Confirmation** dialog appears.

  


Before the campaign can be submitted, users must confirm compliance by selecting the required checkboxes acknowledging that.  
  


Once these confirmations are checked, users can proceed with the submission.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066858418/original/jJOxkBL4VBipM66djomZDNLHL-jgPxrXlQ.png?1773393077)

  


* * *

### **Privacy Policy & Terms of Service Requirements**

  


In addition to configuring the Chat Widget correctly, customers must ensure that their **website’s Privacy Policy and Terms of Service (TOS)** are compliant and clearly available on their website.

Even though **LeadConnector’s Terms of Service are used for the Chat Widget** , the **customer’s own website policies must still meet carrier compliance requirements**.

Specifically, the customer’s **Privacy Policy must include a non-sharing clause** stating that mobile information will not be shared with third parties for marketing purposes.

The Privacy Policy must include language similar to the following:

> **No mobile information will be shared with third parties/affiliates for marketing/promotional purposes. Information sharing to subcontractors in support services, such as customer service, is permitted. All other use case categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties.**

Ensuring that the **Privacy Policy and Terms of Service are present and compliant** helps meet carrier guidelines and reduces the risk of **A2P campaign rejection**.

* * *

## **Who Can Use This Flow**

  


The Pre-Built A2P Campaign (Widget-First) registration flow is available to:

  * Agencies submitting new A2P campaigns

  * Sub-accounts registering new campaigns

  * Marketing-only campaigns

  * Transactional-only campaigns

  * Campaigns that include age-gated content


> **Not available for:**
> 
>   * Mixed use-case campaigns
> 
>   * Sole Proprietor (Sole-prop) campaigns
> 
> 


* * *

## **Key Benefits**

  * Reduced rejection rates

  * Automatic age-gating compliance

  * Prevention of financial and marketing misclassification

  * Faster submission process

  * Elimination of manual compliance writing


The Pre-Built A2P Campaign (Widget-First) flow provides a structured, compliance-focused registration experience designed to improve approval outcomes and simplify campaign setup.

* * *

**Frequently Asked Questions**  
  
**Q1. What if my Mixed Use Case or Sole Proprietor campaign was rejected?**  
If a Mixed Use Case or Sole Proprietor campaign is rejected, it cannot be resubmitted using the new registration flow. You will need to delete the previously rejected campaign and submit a brand-new campaign instead.

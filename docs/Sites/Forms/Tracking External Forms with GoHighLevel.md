# Tracking External Forms with GoHighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006092-tracking-external-forms-with-gohighlevel](https://help.gohighlevel.com/support/solutions/articles/155000006092-tracking-external-forms-with-gohighlevel)  
**Category:** Sites  
**Folder:** Forms

---

Capture form submissions from external websites directly into HighLevel with zero manual setup. The enhanced External Tracking feature automatically detects supported forms like Gravity Forms, WPForms, and custom HTML forms, then sends submissions into your CRM in real time. This eliminates the need for Zapier, webhooks, or custom integrations while improving attribution and lead tracking accuracy.

* * *

**TABLE OF CONTENTS**

  * What is External Tracking?
  * Key Benefits of External Tracking
  * Automatic Form Detection
  * Smarter Field Mapping
  * How To Setup External Tracking
  * Supported Form Requirements
  * Workflow Triggers
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is External Tracking?**

  


External Tracking is a lightweight script that connects your external website activity to HighLevel, allowing you to track page views and automatically capture form submissions from third-party sites.

  


With the latest enhancement, External Tracking now **automatically detects DOM-based forms and captures submissions without requiring manual configuration** , making it significantly easier to track leads from platforms like WordPress, Shopify, Wix, and custom-built websites.

* * *

## **Key Benefits of External Tracking**

  


External Tracking simplifies lead capture and improves visibility into external website performance, helping you make better marketing and automation decisions.  
  


  * **Automatic Form Detection** : detects supported forms like Gravity Forms, WPForms, and custom HTML automatically  
  


  * **Real-Time Submission Capture** : instantly captures submissions without delays or integrations  
  


  * **Automatic Contact Creation** : creates or updates contacts immediately after submission  
  


  * **Smarter Field Mapping** : maps fields intelligently to existing contact properties and custom fields  
  


  * **Attribution Tracking** : captures UTM parameters, page URLs, and session data  
  


  * **Multi-Form Support** : tracks multiple forms on the same page independently  
  


  * **Zero Configuration** : no need for Zapier, webhooks, or manual mapping


* * *

## **Automatic Form Detection**

  


External Tracking scans your website for supported forms rendered directly in the DOM, allowing most modern form builders to work instantly after installation. This removes the need for manual validation and ensures a seamless experience when capturing leads from external sites.

  


Supported forms include:  
  


  * WordPress forms (Gravity Forms, WPForms, Contact Form 7)  
  


  * Custom HTML forms  
  


  * No-code website builders


  


Forms embedded via iframes or third-party widgets are not supported.

* * *

## **How DOM-Based Form Tracking Works**

  


DOM-based tracking means the form and its fields must exist as readable HTML elements on the page. The tracking script looks for standard form structures and input fields that are available in the page DOM.

  


A supported form usually includes:  
  


  * A valid <form> HTML element  
  

  * Input fields that include name attributes  
  

  * Fields that are visible and available in the DOM  
  

  * An email field, when contact creation or contact matching is needed


  


External Tracking works best with forms that behave like standard website forms. This includes many WordPress forms, custom HTML forms, and forms created by no-code website builders.

  


External Tracking does not read form fields that are hidden inside an iframe or controlled entirely by a third-party widget that does not expose the form inputs on the page.

* * *

## **Smarter Field Mapping**

  


Field mapping is handled automatically using intelligent matching, ensuring that captured data aligns with your contact records without requiring manual setup. This improves data accuracy and reduces the need for post-submission cleanup.  
  


  * Matches fields using name, label, and existing custom fields  
  


  * Stores unmapped fields safely for later use  
  


  * Supports multiple field types (text, dropdowns, checkboxes, dates, etc.)  
  


  * Displays only relevant fields in the UI


* * *

## **How To Setup External Tracking**

  


Correct installation ensures that all external form submissions and page activity are captured reliably, enabling accurate reporting and automation.

  


#### **_Step 1:_**_**Get Your Tracking Script**_  
  


  1. Go to **Settings → External Tracking**  
  


  2. Click **Copy Script**


  


**External Tracking settings page showing the script and “Copy Script” button**  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752503/original/PEbTy-wfjvfZsuQJypzzxeTFbcVRL8_WKg.png?1776919977)

  


This script is unique to your account and acts as the connection between your website and HighLevel. Do not modify the tracking ID.

  


**Script snippet with the tracking ID visible**  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752513/original/_T9VxSyR9yLjp6UyNwfqypd3MlMM0s74qQ.png?1776920030)**

####   
  
** _Step 2:_**_**Install the Script on Your Website**_  
  


Paste the script before the closing </body> tag of your website so it loads on every page and can detect forms automatically.  
  

    
    
    <script   src="https://link.yourdomain.com/js/external-tracking.js"  data-tracking-id="tk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"> </script>

  
**Example WordPress dashboard where the script will be added**  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752553/original/sAUQARomgMeV_2GuJllMXptbI6f8pqjbHg.png?1776920144)

  
This can be implemented across multiple platforms including WordPress, Shopify, Wix, Webflow, or any custom HTML site.

####   
**_Step 3:_**_**Add Script to Your Form or Page (Optional Example)**_

  


Although global installation is recommended, you can also place the script directly inside a form using an HTML block. This is often used in page builders or form editors for quick implementation.

  


**WordPress Forms list selecting a form to edit**  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752573/original/KaqUzxaURWq0ideowuFnIThRvJbP3W67hw.png?1776920210)

  
  
Once inside the form builder, you can insert the script into an HTML block to ensure it loads with the form.

  


**HTML block inside a form with the tracking script added**  
  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752588/original/14h5hfN1lT-aYVORbhTN2D1vcD5t15njYQ.png?1776920267)**

####   
  
** _Step 4:__Submit the Form_**

  


After installation, simply submit the form as a user would. The system will automatically detect the form and capture all supported field data without additional configuration.

  


**Example external form (Gravity Form) filled out on a webpage**  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752600/original/ZwdYAbvbZ4a43xtCiBXwH1cew7rPHjno4w.png?1776920353)  
  
Once submitted, the form behaves normally from the user’s perspective while sending data to HighLevel in the background.

  


**Form submission confirmation message displayed to the user**

  
**  
**

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752617/original/ItwMwlIOQGbm8mdOtsToSRCEOKwWWtWeYg.png?1776920388)**

  


####   
** _Step 5:_**_**View Submissions in HighLevel**_

  


Captured submissions are instantly available inside HighLevel, allowing you to review and manage incoming leads.  
  


  1. Navigate to **Sites → Forms → Submissions**  
  


  2. Select **External Forms** to filter results


  


**Submissions dashboard displaying captured external form entries**  
  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752659/original/knFztL656p1sAnifrtNMrAnFM3vRGnlSAw.png?1776920515)**

####   
  
** _Step 6:_**_**View Contact & Activity Details**_

  


Each submission is also attached to a contact record, providing full visibility into the captured data and user activity. This allows you to use the information for segmentation, automation, and follow-up.

  


**Activity details panel showing captured fields and unmapped data**  
  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069752668/original/3y8r9SW91P_TP_thMpjHzChzr0GXuNxc0w.png?1776920564)**

* * *

## **Supported Form Requirements**

  


External Tracking works automatically when forms meet basic structural requirements, ensuring reliable detection and data capture.  
  


  * Must use a valid <form> HTML element  
  


  * Fields must include name attributes  
  


  * An email field should be present  
  


  * Fields must be visible in the DOM


  


Not supported:  
  


  * Iframe-based forms  
  


  * Popup widgets without real form elements  
  


  * Third-party scripts that do not expose inputs


* * *

## **Workflow Triggers**

  


External Tracking enables automation based on user behavior, allowing you to respond to leads instantly and efficiently.  
  


  * **Page View Trigger** : fires when a visitor lands on a page with the tracking script (even anonymously)  
  


  * **Form Submission Trigger** : fires when a detected form is submitted


  


Available filters:  
  


  * Domain  
  


  * Page path  
  


  * External form name  
  


  * UTM parameters


* * *

## **Frequently Asked Questions**

  


**Q: Do I need to configure anything after installing the script?**

No. Form detection and submission tracking happen automatically.

  


**Q: Does this work with Gravity Forms and WPForms?**

Yes. Most DOM-based WordPress forms are supported out of the box.

  


**Q: Can multiple forms on the same page be tracked?**

Yes. Each form is detected and tracked independently.

  


**Q: Are iframe-based forms supported?**

No. Only forms rendered directly in the DOM are supported.

  


**Q: Where can I view submissions?**

In Forms → Submissions, as well as within contact records and activity logs.

  


**Q: What happens to unmapped fields?**

They are stored safely and can be used later for mapping or workflows.

* * *

## **Related Articles**

  


  * [](<https://help.gohighlevel.com/en/support/solutions/articles/155000006092>)[](<https://help.gohighlevel.com/en/support/solutions/articles/155000006092>)[Tracking External Forms with GoHighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/155000006092>)  
  

  * [Typeform – Actions & Triggers in Workflows](<https://help.gohighlevel.com/en/support/solutions/articles/155000006676>)

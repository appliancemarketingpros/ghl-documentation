# Workflow Action - Add To Google Analytics

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003367-workflow-action-add-to-google-analytics](https://help.gohighlevel.com/support/solutions/articles/155000003367-workflow-action-add-to-google-analytics)  
**Category:** Workflows  
**Folder:** Integrations Workflow Actions

---

**TABLE OF CONTENTS**

  * Overview
  * Action Name
  * Action Description
  * Action Details
    * How to Configure
  * Example
  * Suggested Triggers
  * Additional Notes


##   


## Overview

The "**Google Analytics** " action allows you to fire a custom event in your Google Analytics (GA) account. This action supports Google Analytics 4 (GA4) and Universal Analytics (UA). It can be used to track specific user interactions or behaviours on your website or app in GA for better insights.

  


## Action Name

**Google Analytics**

  


## Action Description

This action enables you to send custom events directly to Google Analytics (GA4 or UA) by specifying details like the Measurement ID, Event Name, API Secret, and Event Value.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032467697/original/EPGRuaUplacZu8Hmn3TIPtOaMraBVEhRcg.png?1725821507)

  


### How to Configure

  1. **Action Name** : Set the name of the action (e.g., "Add to Google Analytics").
  2. **Action Type** : Select either "Google Analytics 4" or "Universal Analytics" based on your setup.
  3. **Measurement ID** : Enter the Measurement ID for your GA4 property.
  4. **Event Name** : Specify the event name that will appear in GA4/UA (e.g., "purchase", "page_view").[ Refer here for the event naming rules by google](<https://support.google.com/analytics/answer/13316687?hl=en>)
  5. **API Secret** : Input the API secret from your GA4 setup to securely send event data.
  6. **Event Value** : Optionally, pass a value related to the event, like revenue or clicks.


  


Field Name| Description| Mandatory  
---|---|---  
Measurement ID| The unique ID for your Google Analytics property in GA4| Yes  
Event Name| The name of the event you want to trigger in GA4 or UA| Yes  
API Secret| A secret key generated in Google Analytics to send data securely| Yes  
Event Value| The value or parameter you want to pass along with the event| No  
  
  


## Example

You can use this action to track when a user completes a form submission on your website by firing a "Form Submitted" event in Google Analytics. The Measurement ID will link the event to the correct property, and the API secret ensures the data is securely transmitted.

###   


## Suggested Triggers

  * **Form Submission** : Trigger this action when a form on your website is submitted, sending event data to GA.
  * **Page Visit** : Trigger the event when a user visits a specific page, like a product page, to track user behavior.
  * **Tag Added** : When a user tag is added (e.g., "New Lead"), this action could send an event to GA tracking that change.
  * **Appointment Booked** : Fire an event when a user books an appointment to track how many appointments are made through your system.
  * **Product Purchase** : Trigger this action when a product is purchased and send relevant information to Google Analytics (e.g., purchase value).


###   


## Additional Notes

  * Make sure that Google Analytics is correctly configured in your system before using this action.
  * Events sent to Google Analytics can be used for reporting, segmentation, and marketing automation.
  * Ensure that the Measurement ID and API secret are accurate for successful event tracking.

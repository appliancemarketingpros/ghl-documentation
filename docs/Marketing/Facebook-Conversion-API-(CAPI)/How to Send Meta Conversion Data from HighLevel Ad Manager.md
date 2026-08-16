# How to Send Meta Conversion Data from HighLevel Ad Manager

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002478-how-to-send-meta-conversion-data-from-highlevel-ad-manager](https://help.gohighlevel.com/support/solutions/articles/155000002478-how-to-send-meta-conversion-data-from-highlevel-ad-manager)  
**Category:** Marketing  
**Folder:** Facebook Conversion API (CAPI)

---

Sending conversion data from HighLevel to Meta helps improve campaign measurement, attribution, and optimization by connecting meaningful customer actions back to your ads. HighLevel Ad Manager lets you create and manage conversion pixels that can be used with Meta Conversion API workflows. This guide explains how to create a conversion pixel, understand the available event types, and prepare it for use with your Meta advertising workflows.

* * *

# **What is an Ad Manager Conversion Pixel?**

Ad Manager conversion pixels help connect actions that occur in HighLevel with your Meta advertising activity. Creating the conversion pixel gives HighLevel the information needed to identify the conversion source when a supported Meta Conversion API event is sent through a workflow.

  


A conversion pixel created in HighLevel Ad Manager includes a generated **Pixel ID** and supporting configuration that can be used when sending Funnel Events or Lead Events to Meta.

Creating the pixel is one part of the conversion-tracking process. To send the conversion event to Meta, you must also configure the appropriate **Meta Conversion API** action in a HighLevel workflow.

[Learn how to send a Meta Conversion API action for Ad Manager](<https://help.gohighlevel.com/support/solutions/articles/155000003691-how-to-send-a-meta-conversion-api-action-for-ad-manager->).

****

* * *

## **Key Benefits of Ad Manager Conversion Pixels**

  


  * **Improved Conversion Tracking:** Connect supported customer actions in HighLevel with your Meta advertising activity.

  * **Better Attribution:** Provide Meta with additional conversion signals that can help associate customer actions with advertising interactions.

  * **Campaign Optimization:** Give Meta more conversion data to use when optimizing campaigns toward meaningful customer actions.

  * **Lead Journey Visibility:** Track events that occur as leads submit forms, book appointments, or move through pipeline stages.

  * **Flexible Event Tracking:** Use the same conversion pixel with supported Funnel Events and Lead Events.

  * **Simplified Workflow Setup:** When using the Ad Manager connection type in the Meta Conversion API workflow action, eligible Ad Manager pixels are available for selection and HighLevel manages the access token.

  * **Audience and Retargeting Support:** Conversion and audience data can support broader Meta advertising strategies when configured appropriately.


  


* * *

  


## **Funnel Events and Lead Events**

  


Funnel Events are generally used for customer actions that originate from a HighLevel funnel, website, form, survey, appointment booking, or order form.

Supported workflow triggers can include:

  * Form Submitted

  * Survey Submitted

  * Customer Booked Appointment

  * Order Form Submission


For more detailed Funnel Event configuration, see [How to set up a Funnel Event Pixel for Facebook Conversion API](<https://help.gohighlevel.com/support/solutions/articles/48001236281>).

  


### **Lead Events**

Common supported triggers include:

  * Facebook Lead Form Submission

  * Pipeline Stage Change


Lead Events can be useful for sending later-stage outcomes—such as qualification or pipeline progression—back to Meta.

For detailed Lead Event requirements and attribution setup, see [Facebook Conversion Leads Walkthrough](<https://help.gohighlevel.com/support/solutions/articles/48001233833-facebook-conversion-leads-walkthrough>).

> **Important:** Successful attribution depends on the contact having the appropriate Meta attribution information. Depending on the event and configuration, identifiers such as FBCLID or Facebook Lead ID may be used to associate the conversion with the original Meta interaction.

* * *

## **How Conversion Pixels Work With Meta CAPI Workflows**

  


Creating a conversion pixel in Ad Manager prepares the conversion asset, while the Meta Conversion API workflow action determines when conversion data is actually sent to Meta.

When configuring a **Meta Conversion API** action in a workflow, HighLevel provides two connection types:

  * **Integrations**

  * **Ad Manager**


Using the **Ad Manager** connection type simplifies setup because conversion pixels available in Ad Manager are pre-populated for selection. HighLevel also manages the access token, so you do not need to manually generate and paste one into the workflow action.

The workflow trigger and Event Type must match the customer activity you want to report. For example, a form submission may be configured as a Funnel Event, while movement through a pipeline stage for a Meta lead may be configured as a Lead Event.

[Learn more about configuring the Meta Conversion API action for Ad Manager](<https://help.gohighlevel.com/support/solutions/articles/155000003691-how-to-send-a-meta-conversion-api-action-for-ad-manager->).

* * *

## **How To Setup an Ad Manager Conversion Pixel**

  1. Navigate to **Marketing → Ad Manager** in your HighLevel sub-account, then click the **Settings** button to open **Ad Manager Settings**.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078360502/original/pweu3LarV3Ub8U3lIFfYdB9iBBITvh8cmw.png?1786632122)


  


  


2\. Select the **Conversions** tab, review the available conversion pixels, then click **Create new conversion pixel**.

  


![](https://jumpshare.com/share/C5X11PXlQKABtbO62taf+/Screen+Shot+2026-08-13+at+10.32.02+AM.png)

  


  


**3.** Enter a name for the conversion pixel. **Complete** the creation process.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078368890/original/vRn1uFv6VQQwiM17cR7YZN0eZ6AxXbHejw.png?1786635510)  
  
  

    
    
    ****Confirm that the new pixel appears under the Conversions tab.**
    **Newly created conversion pixels initially display their available conversion information in Ad Manager and can then be selected when configuring supported Meta Conversion API workflows.****

HighLevel manages the access token when the **Ad Manager** connection type is selected.

  13. Save the action, then save and publish the workflow.


For complete workflow instructions, see [How to send a Meta Conversion API action for Ad Manager](<https://help.gohighlevel.com/support/solutions/articles/155000003691-how-to-send-a-meta-conversion-api-action-for-ad-manager->).

> 
>     ****Note:** HighLevel supports custom mapping for certain Meta conversion parameters. When custom mapping is enabled, you can map FBCLID for Funnel Events or Facebook Lead ID for Lead Events. Custom values take priority over system defaults when provided.
>     
>     **Compliance Note:** Meta applies restrictions to custom audiences and custom conversions that contain or imply certain prohibited or sensitive information. Review your conversion names and configurations to make sure they comply with Meta requirements. See [Meta: Custom Audiences and Conversions restrictions](<https://help.gohighlevel.com/support/solutions/articles/155000006301-meta-custom-audiences-and-conversions-restrictions>) for additional details.
>     
>     
>     **

##   


## Frequently Asked Questions

  


**Q: Does creating a conversion pixel automatically send data to Meta?**  
No. You also need to add the **Meta Conversion API** action to a workflow so HighLevel can send the conversion event to Meta.  
  


**Q: Do I need to create a Meta access token?**  
No. If you select **Ad Manager** as the connection type, HighLevel manages the access token for you.  
  


**Q: Can I use the same pixel for different event types?**  
Yes. The same conversion pixel can be used for supported Funnel Events and Lead Events.  
  


**Q: Why is my conversion not showing in Meta?**  
The contact may be missing the Meta tracking information needed to match the conversion to the original ad interaction.

  


**Q: Should I choose a Funnel Event or Lead Event?**  
Choose a **Funnel Event** for actions such as form submissions, surveys, appointments, or order forms. Choose a **Lead Event** for Meta lead form submissions or lead progress through your CRM.

* * *

### Related Articles

  * [How to send a Meta Conversion API action for Ad Manager](<https://help.gohighlevel.com/support/solutions/articles/155000003691-how-to-send-a-meta-conversion-api-action-for-ad-manager->)

  * [How to set up a Funnel Event Pixel for Facebook Conversion API](<https://help.gohighlevel.com/support/solutions/articles/48001236281>)

  * [Facebook Conversion Leads Walkthrough](<https://help.gohighlevel.com/support/solutions/articles/48001233833-facebook-conversion-leads-walkthrough>)

  * [Facebook Conversions API Trigger in Workflows](<https://help.gohighlevel.com/support/solutions/articles/48001185099-facebook-conversions-api-trigger-in-workflows>)

  * [Create Custom Audiences in HighLevel Ad Manager](<https://help.gohighlevel.com/support/solutions/articles/155000003236>)

  * [Meta: Custom Audiences and Conversions restrictions](<https://help.gohighlevel.com/support/solutions/articles/155000006301-meta-custom-audiences-and-conversions-restrictions>)


* * *

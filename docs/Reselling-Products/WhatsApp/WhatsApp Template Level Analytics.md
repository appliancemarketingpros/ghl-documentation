# WhatsApp: Template Level Analytics

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003714-whatsapp-template-level-analytics](https://help.gohighlevel.com/support/solutions/articles/155000003714-whatsapp-template-level-analytics)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# WhatsApp Template-Level Analytics

Gain powerful insights and optimize your messaging strategy with per-template performance data

Table of Contents

  * • How to View WhatsApp Template Insights
  * • How to View WhatsApp Template Button Clicks
  * • FAQs


The Template-Level Analytics feature in the CRM's WhatsApp integration empowers businesses with detailed performance insights for each messaging template. Previously, users had limited visibility into how well their messages were performing. Now, you can track essential engagement metrics like:

  * Number of messages **sent** , **delivered** , and **read**
  * **Button click** data for interactive templates (URL buttons, Quick Replies)


These insights help you fine-tune your messaging, improve engagement, and drive better customer experiences.

* * *

## How to View WhatsApp Template Insights
    
    
    Note: Template analytics describe the number of times a template has been sent, delivered, and read, and the number of times [URL buttons](<https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/components#url-buttons>) or [Quick Reply buttons](<https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/components#quick-reply-buttons>) in the template have been clicked. This report option isn't available for the Coex integration.

1

Go to **Settings > WhatsApp > Templates**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034279043/original/XkJX_4JnB0qp4KzDt6adAdaqSaOF-0XFnw.png?1728371385)

2

Search for the template and click on **Reports**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034279173/original/B79VtQLcqP2DTb2uCUBd7N6_fshManl3Gg.png?1728371494)

3

Click on the **Deliverability** tab.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034279302/original/DjQBt07teasQrwzZCz8IlPCdw3SVxSfzPg.png?1728371578)

4

Select **Start Date** and **End Date**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034279992/original/iJmmR1tGFbcDss5w3JZhZJH5jsomWmw5dw.png?1728372099)

### Metrics Displayed

  * **Sent:** Message sent (1 gray tick)
  * **Delivered:** Message delivered (2 gray ticks)
  * **Read:** Message opened (blue ticks)


* * *

## How to View WhatsApp Template Button Clicks
    
    
    Note: Button click analytics are only available for templates categorized as MARKETING or UTILITY.

1

Go to **Settings > WhatsApp > Templates**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034279043/original/XkJX_4JnB0qp4KzDt6adAdaqSaOF-0XFnw.png?1728371385)

2

Search for the template and click on **Reports**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034279173/original/B79VtQLcqP2DTb2uCUBd7N6_fshManl3Gg.png?1728371494)

3

Click on **Button Clicks**.
    
    
    URL Buttons: URL buttons load the specified URL in the device's default web browser when tapped by the app user. Templates are limited to two URL buttons.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034280847/original/YeU3rRykCkczLkqTy79z6DM4D5aOt1oExw.png?1728372758)
    
    
    Note: WABAs owned by or shared with Meta Business Accounts in the European Union, United Kingdom, or Japan, or that have a business phone number with a country calling code from any of those countries or regions, are not supported.

### About URL Buttons

  * Open a specified URL in the user's web browser
  * Max: **2 URL buttons** per template


* * *

## FAQs

Q. What is the Template-Level Analytics feature?

The Template-Level Analytics feature provides detailed insights into the performance of individual WhatsApp templates. Businesses can monitor key metrics such as the number of messages sent, delivered, and read, as well as track button clicks for templates that include interactive elements like URL or Quick Reply buttons.

Q. How can I view WhatsApp template insights?

Navigate to Settings > WhatsApp > Templates, search for the desired template, and click on Reports. Under the Deliverability section, you can view metrics like sent, delivered, and read counts for that template.

Q. What is a Quick Reply button?

Quick Reply buttons are custom text-only buttons that immediately message you with the specified text string when tapped by the app user. A common use case is a button that allows your customer to easily opt out of marketing messages.

Templates are limited to 10 Quick Reply buttons. If using Quick Reply buttons with other buttons, buttons must be organized into two groups: Quick Reply buttons and non-Quick Reply buttons. If grouped incorrectly, the API will return an error indicating an invalid combination.

**Valid groupings:**

  * Quick Reply, Quick Reply
  * Quick Reply, Quick Reply, URL, Phone
  * URL, Phone, Quick Reply, Quick Reply


**Invalid groupings:**

  * Quick Reply, URL, Quick Reply
  * URL, Quick Reply, URL


Q. What type of button click data is available?

Button click analytics are available for templates categorized as either MARKETING or UTILITY. The system tracks how many times users click on interactive buttons like URL buttons or Quick Reply buttons, providing real-time data on user engagement.

Q. How many buttons can be included in a template?

Templates are limited to two URL buttons and can have up to 10 Quick Reply buttons. The buttons need to be grouped correctly — Quick Reply buttons cannot be mixed in the same group with other button types like URL buttons.

Q. Can I track button clicks for templates used in the European Union, United Kingdom, or Japan?

No, button click analytics are not supported for WhatsApp Business Accounts (WABAs) owned by or shared with Meta Business Accounts in the European Union, United Kingdom, or Japan, or if the business phone number is from one of these regions.

Q. What kind of granularity is available for template analytics?

Template analytics are available with daily granularity. You can select a custom date range to view performance data for a specific time period, such as daily or weekly, by setting the start and end dates.

Q. Can I track URL button clicks in WhatsApp templates?

Yes, URL button clicks are tracked in the analytics for templates that contain URL buttons. When clicked, the URL button opens the specified link in the user's default web browser. These templates can have up to two URL buttons.

Q. What are the benefits of using template-level analytics?

Template-level analytics allow businesses to gain actionable insights into the performance of their messages, helping optimize communication strategies. It helps identify which templates are driving engagement, such as which buttons users are interacting with, and provides visibility into the delivery and read rates of messages. This data allows businesses to refine their templates and improve customer engagement and conversion rates.

# Workflow Trigger - Order Fulfilled

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003254-workflow-trigger-order-fulfilled](https://help.gohighlevel.com/support/solutions/articles/155000003254-workflow-trigger-order-fulfilled)  
**Category:** Workflows  
**Folder:** Opportunity Workflow Triggers

---

**TABLE OF CONTENTS**

  * Overview
  * Trigger Name
  * Trigger Description
  * How to Configure
  * Example


##   


## Overview

The "**Order Fulfilled** " trigger automates processes when an order has been completed. It can be used to send thank-you messages, initiate customer feedback requests, or update inventory and accounting systems.

### 

  


## Trigger Name

**Order Fulfilled**

  


## Trigger Description

This trigger is activated when an order status changes to fulfilled. It ensures timely follow-up actions are taken, enhancing customer satisfaction and streamlining backend processes.

  


## How to Configure

  * **Choose a Workflow Trigger:** Select "Order Fulfilled" from the trigger options.
  * **Workflow Trigger Name:** Name your trigger, such as "Order Fulfilled".
  * **Filters:** Utilize filters to specify conditions under which the workflow should run. For example, you can filter based on cart value, order type, etc.


  


Value| Description| Mandatory  
---|---|---  
Cart Value| Filter orders based on their cart value.| Optional  
Select Operator| Choose comparison operators like Equals to, Greater than, Less than, etc.| Optional  
  
  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032021676/original/SFfIE-n_CA6Edf4qZYKKWJhExZOqzfymHg.png?1725186602)

  


## Example

**Scenario:** A company wants to send a thank-you email to customers who make a purchase with a cart value greater than $100.

  * **Configuration:**
    * **Trigger:** Order Fulfilled
    * **Filters:**
      * **Cart Value:** Greater than
      * **Value:** $100
  * **Actions:** Once the trigger is activated:
    1. Send an automated thank-you email to the customer.
    2. Update the CRM to mark the customer as a "VIP Customer."
    3. Add a follow-up task in the sales team's calendar to offer a special discount on the next purchase.


  


This configuration ensures that high-value customers receive personalized follow-ups, enhancing the relationship and encouraging repeat business.

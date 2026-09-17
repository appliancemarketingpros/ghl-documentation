# Workflow Action - Stripe One Time Charge

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003366-workflow-action-stripe-one-time-charge](https://help.gohighlevel.com/support/solutions/articles/155000003366-workflow-action-stripe-one-time-charge)  
**Category:** Workflows  
**Folder:** Payments Workflow Actions

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

The "**Stripe One Time Charge** " action allows you to trigger a one-time charge in Stripe for a fixed amount to a specific customer within your Stripe account. This action is useful for collecting payments without requiring recurring subscriptions or payment plans.

  


## Action Name

**Stripe One Time Charge**

  


## Action Description

This action triggers a one-time charge in Stripe for a set amount to a designated customer. It requires a valid Stripe Customer ID, amount, description, and currency to process the charge.

  


## Action Details

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032467636/original/PdJCwJ8ssxtID0-al7VwSXqM7w1dC1-GtA.png?1725821253)

  


### How to Configure

  1. **Action Name:** Set a recognizable action name, such as "Stripe One Time Charge."
  2. **Stripe Customer ID:** Enter or select the Stripe Customer ID for the customer to be charged.
  3. **Description:** Provide a brief description of the charge (optional).
  4. **Amount:** Enter the amount to charge the customer.
  5. **Currency:** Select the appropriate currency for the transaction.


  


Field Name| Description| Mandatory  
---|---|---  
Stripe Customer ID| The unique identifier for the Stripe customer to be charged| Yes  
Description| A description of the charge (e.g., for tracking or notes)| No  
Amount| The amount to be charged to the customer| Yes  
Currency| The currency in which the amount will be charged| Yes  
  
##   


## Example

A business could use this action to charge a customer for a single service, such as a one-time consultation fee of $150, with USD as the currency. After the payment is triggered, the amount will be processed through Stripe and linked to the specified customer’s account.

###   


## Suggested Triggers

Here are some suggested triggers to use with the "Stripe One Time Charge" action:

  1. **Form Submission** : Automatically charge a customer when they submit a form indicating that they are ready to make a purchase or request a service.
  2. **Tag Added** : Trigger a one-time charge when a specific tag (e.g., “Ready to Purchase”) is added to the customer’s profile.
  3. **Appointment Confirmed** : Charge customers automatically after confirming an appointment for services.
  4. **Order Completed** : Trigger a charge when an order is marked as completed within your system.
  5. **Email Link Clicked** : Automatically charge customers who click a payment-related link in an email.


###   


## Additional Notes

  * Make sure you have set up Stripe integration in your system before using this action.
  * Ensure the Stripe Customer ID is valid to avoid charge failures.
  * Use this action for one-time payments only. For recurring payments, consider other Stripe-related actions like subscriptions.
  * This stripe one-time charge action was not designed for sub accounts to charge their contacts it's meant for agencies to charge the sub account admins.

# Workflow Action - Go To

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003377-workflow-action-go-to](https://help.gohighlevel.com/support/solutions/articles/155000003377-workflow-action-go-to)  
**Category:** Workflows  
**Folder:** Contact Workflow Actions

---

**TABLE OF CONTENTS**

  * Overview
  * Action Name
  * Action Description
  * Action Details
  * Example


##   


## Overview

The Go-To event allows you to jump contacts from one place to another in Workflows. This action enables you to direct contacts to specific points in the workflow based on certain criteria or triggers.  By using the "Go To" action, you can streamline your workflows, ensuring that contacts receive tailored experiences based on their interactions or behaviours.  


  


## Action Name

Go To

  


## Action Description

Using the "Go To" action you can send a contact to another action in the workflow. This action is useful when you want to send the contact through another branch or sending the contact back to few actions if a certain condition is not met.

A point to remember is that the "Go To" action can only be added as a last step of a workflow or a branch. It can't be added between actions.

  


## How to Configure

#### **Step-b****y-Step Guide**

  1. **Navigate to Workflow Actions:** Access the automation or workflow settings in your platform.
  2. **Choose a Workflow Action:** Select "Go To" from the list of available actions.
  3. **Name Your Action:** Enter a descriptive name for the trigger, such as "Go to Wait action."
  4. **Save:** Click on Save button.
  5. **Configure:** All the actions will be highlighted and you can click on the action where you want the contact to proceed.
  6. **De-link -** Now what if you want to change the action which was selected earlier. Click on the "Disconnect GoTo" icon under the Go To action and then you can select another action where you want the contact to proceed.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032494801/original/6T4ziuakZxJbvLDr-KR0osap6pfhl091zw.png?1725874453)

## Example

Sending Emails to customers who have purchased the items

  


**Scenario:** An online retailer wants to re-engage customers who have not purchased the items and don't want to send an email to the customers who have already bought.

  


**Trigger Setup:**

  * **Trigger:** Abandoned Checkout
  * **Name:** Abandoned Checkout
  * **Filters:**
    * **Duration (minutes):** 10 (trigger the workflow if the cart is abandoned for more than 10 minutes)
    * **Cart Value:** Greater than 50 (trigger the workflow only if the cart value exceeds $50)


  


**Workflow Actions:**

  1. **Email Notification:** Send a personalized email to the customer, reminding them of the items left in their cart and offering an incentive (e.g., discount).
  2. **Wait:** Wait for 1 day
  3. **If/Else:** Add if else condition to check if the user has "Purchased" tag. The contact will go through the first branch if the tag is present and the None branch if tag is not present.
  4. **Email (Branch 2):** Send another email to the contact reminding them of the abandoned cart.
  5. **Wait (Branch 2):** Add a wait step with a condition if tag added is "Purchased"
  6. **Go To (Branch 1):** Add a Go to action that will take the contact directly to the wait step in the second branch


  


**Outcome:** This automation helps recover potentially lost sales by re-engaging customers who abandoned their carts and do not send an email to the customers who have already purchased the items.

  


##   
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032494587/original/Rtrqp4TltAdaz3-j9_Qomcr-c0n_Wouhow.jpeg?1725874371)

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032494687/original/kJ9A12CFzqzpstlRanspr6h5SF3PDCgyPg.png?1725874395)

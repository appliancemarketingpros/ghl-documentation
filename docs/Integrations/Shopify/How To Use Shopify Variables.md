# How To Use Shopify Variables

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001203898-how-to-use-shopify-variables](https://help.gohighlevel.com/support/solutions/articles/48001203898-how-to-use-shopify-variables)  
**Category:** Integrations  
**Folder:** Shopify

---

## **How to Use The Below Table:**

  


This table shows the variables you can insert into emails, SMS, and other workflow actions when a Shopify trigger runs. To use a variable, copy it exactly as shown in the ‘Shopify Variable format’ column (including the double curly braces). Example: {{order.id}}.

  


Variables only populate when the workflow is triggered by the event types shown in the YES/– columns. If a column shows ‘–’, that variable will be blank for that trigger.

  

    
    
    YES = the variable is included in that trigger’s payload and should populate.
    
    – = the variable is not included for that trigger, so it will not populate.

  


Use the ‘Data Sample’ column to understand the kind of value you will receive.

* * *

## **Where to Paste Shopify variables**

  


Use Shopify variables anywhere you see a message editor or text field that supports variables, such as:  
  


  * Workflow Email body  
  


  * Workflow SMS body  
  


  * Workflow internal notification text  
  


  * Custom values are not required—Shopify variables come from the trigger payload.


  


**_Shopify Variable Details_**| ** _Shopify Variable format_**| ** _Data Sample_**| ** _Abandoned Checkout Trigger_**| ** _Order Placed Trigger_**  
---|---|---|---|---  
** _Order Info_**|   
|   
|   
|   
  
Order id| {{[order.id](<http://order.id/>)}}| 1900968798308| YES| YES  
Order number| {{order.number}}| 1044| -| YES  
Order status URL| {{order.order_status_url}}| link to order| -| YES  
Abandoned checkout URL| {{order.abandoned_checkout_url}}| link to abandoned checkout| YES| -  
Created at| {{order.created_at}}| 2021-10-21T11:47:12+05:30| YES| YES  
Created on| {{order.created_on}}| default format 10-20-2021| YES| YES  
Currency| {{order.currency}}| $| YES| YES  
Currency code| {{order.currency_code}}| USD| YES| YES  
  
|   
|   
|   
|   
  
** _Customer Info_**|   
|   
|   
|   
  
First Name| {{order customer.first_name}}| John| YES| YES  
Last Name| {{order.customer.last_name}}| Carter| YES| YES  
Email| {{order.customer.email}}| [johncarter@gmail.com](<mailto:johncarter@gmail.com>)| YES| YES  
Phone| {{order.customer.phone}}| 18989898989| YES| YES  
  
|   
|   
|   
|   
  
** _Order Value_**|   
|   
|   
|   
  
Total Cart Price| {{order.total_cart_price}}| 99.00| -| YES  
Discount Code| {{order.discount_code}}| TESTDISC20| -| YES  
Total Discount Value| {{order.total_discounts}}| 11.99| -| YES  
Order has discount?| {{order.has_discount}}| true/false| -| YES  
Subtotal Price| {{order.subtotal_price}}| 88.99| -| YES  
Total Shipping Price| {{order.total_shipping_price}}| 14.49| -| YES  
Total Price| {{order.total_price}}| 102.99| -| YES  
  
|   
|   
|   
|   
  
** _Customer Billing Address_**|   
|   
|   
|   
  
Contact Name| {{order.billing_address.name}}| John Carter| -| YES  
Address Company| {{order.billing_address.company}}| Marvel Inc.| -| YES  
Address 1| {{order.billing_address.address1}}| 890| -| YES  
Address 2| {{order.billing_address.address2}}| Fifth Avenue, Manhattan| -| YES  
Province| {{order.billing_address.province}}| New York City| -| YES  
Zip| {{order.billing_address.zip}}| 10128| -| YES  
Country| {{order.billing_address.country}}| United States| -| YES  
  
|   
|   
|   
|   
  
** _Customer Shipping Address_**|   
|   
|   
|   
  
Contact Name| {{order.shipping_address.name}}| John Carter| -| YES  
Address Company| {{order.shipping_address.company}}| Marvel Inc.| -| YES  
Address 1| {{order.shipping_address.address1}}| 890| -| YES  
Address 2| {{order.shipping_address.address2}}| Fifth Avenue, Manhattan| -| YES  
Province| {{order.shipping_address.province}}| New York City| -| YES  
Zip| {{order.shipping_address.zip}}| 10128| -| YES  
Country| {{order.shipping_address.country}}| United States| -| YES  
Order requires shipping?| {{order.requires_shipping}}| true/false| -| YES  
  
|   
|   
|   
|   
  
  
|   
|   
|   
|   
  
  
|   
|   
|   
|   
  
  
|   
|   
|   
|   
  
** _Advanced Variables_**|   
|   
|   
|   
  
Order/Abandoned cart items(*Coming Soon)| {{#each Order line_items as | item |}}|   
| YES| YES  
  
| item.id|   
|   
|   
  
  
| item.image|   
|   
|   
  
  
| item.title|   
|   
|   
  
  
| item.quantity|   
|   
|   
  
  
| item.price|   
|   
|   
  
  
| item.line_price|   
|   
|   
  
  
| {{/each}}|   
|   
|   
  
  
|   
|   
|   
|   
  
Order Tax Details(*Coming Soon)| {{#each Order tax_lines as | tax |}}|   
| -| YES  
  
| tax.title|   
|   
|   
  
  
| tax.rate|   
|   
|   
  
  
| tax.price|   
|   
|   
  
  
| {{/each}}|   
|   
|   
  
  
|   
|   
|   
|   
  
  
|   
|   
|   
|   
  
  
|   
|   
|   
|   
  
  
  


## **Examples**

  


### **Example 1: Abandoned Checkout Reminder**  


  


Add this exact example text:  
  


  * **Trigger:** Abandoned Checkout  
  


  * **SMS Example:** Hi {{order.customer.first_name}}, you left items in your cart. Finish checkout here: {{order.abandoned_checkout_url}}  
  


  * **Note:** The abandoned checkout URL only populates for Abandoned Checkout triggers (YES under that trigger).


  
This uses variables shown in the table: `order.customer.first_name` and `order.abandoned_checkout_url` and reinforces that it’s trigger-dependent.

###   
**Example 2: Order Confirmation**  
  
Add this exact example text:  
  


  * **Trigger:** Order Placed  
  


  * **Email Example:** ‘Thanks for your order #{{order.number}} placed on {{order.created_on}}. Total: {{order.total_price}} {{order.currency_code}}. Track: {{order.order_status_url}}  
  


  * **Note:** The order status URL populates for Order Placed triggers (YES under that trigger).


  
All these variables appear in the table.

* * *

## **Troubleshooting**

  * If a variable shows up blank, confirm you are using a trigger where that variable is marked YES in the table.  
  


  * Confirm the contact actually has that data in Shopify (for example, phone may be blank if the customer did not provide it).  
  


  * Copy/paste the variable exactly as shown. Missing braces or extra spaces can prevent substitution.

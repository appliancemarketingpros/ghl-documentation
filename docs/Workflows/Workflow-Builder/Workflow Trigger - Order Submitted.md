# Workflow Trigger - Order Submitted

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001228664-workflow-trigger-order-submitted](https://help.gohighlevel.com/support/solutions/articles/48001228664-workflow-trigger-order-submitted)  
**Category:** Workflows  
**Folder:** Workflow Builder

---

The Order Submitted trigger is a powerful new workflow trigger that allows businesses to upsell customers after they have submitted an order. This trigger works with both 1 Step and 2-Step order forms, giving businesses the flexibility to customize their upsells based on the type of order form used or types of products purchased.

  


#### **Covered in this Article:**

#### When does the Order Submitted trigger fire?

#### How is it different from the Order Form Submitted Workflow Trigger?

#### Using an Email Template to send an Order Confirmation via this Workflow

#### How do submission types filters work? 

#### Will this trigger impact existing Order form submission triggers?

#### What are the filter types, if/else conditions, and custom values I can use?

  


  


* * *

## **When does the Order Submitted trigger fire?**

  


**Please Note**
    
    
    Make sure that the **Allow Multiple** Setting is toggled on in the Workflow Settings if you want it to fire off for the same contact for an Upsell, right after it fires off for them for a Primary Product's purchase.
    
    If you put in a **wait step** which holds the first instance (which came from the purchase of the primary product) of the customer in the workflow, and they go ahead and purchase the upsell, since they would still be held inside the workflow, the Upsell purchase will not let them enter the workflow a second time. Try to avoid using wait steps in this workflow, feel free to use them if you **do not plan on selling Upsells or Bumps for the same product.**

  


* * *

The trigger runs upon a 1-Step or 2-Step order form submission and upsells. This trigger runs both when an order form is submitted, and again when an upsell purchase occurs; on either of these occasions it holds the product information. This means that if the end customer purchases products A and B on an order form and product C on an upsell, it will run two times (first for A and B purchase, and then for the upsell purchase)

  


**Please note:**
    
    
    This only works with **version 2** funnels. (Check out [this article](<https://help.gohighlevel.com/en/support/solutions/articles/48001204903>) for more details on V2 Funnels) If you are using a version 1 funnel, please upgrade to version 2 using the button shown below:
    ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48271898507/original/Jt_bZs48_YpDTe855zfIKEv09u7ptooXnA.png?1672223754)
    
    
    
    

  


* * *

## **How is it different from the Order Form Submitted Workflow Trigger?**

* * *

The following are the most significant differences between the Order Submitted and the Order Form Submitted Workflow Triggers:

  


  * The trigger does not run multiple times on multiple product purchases. The trigger contains a single checkout object sending info only a single time upon an order form submission, Even if that one order session consists of buying multiple products.
  * Ability to filter the trigger directly on the basis of the global product/price. The existing trigger does not provide this functionality


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48271902305/original/HkW1R_dgtia5VEH8lw5XtAJoMKdamm2xog.png?1672224456)

  


  * Ability to use order-related custom values inside the workflow. This contains custom values related to customers, order details, coupon information, and payment gateway


  


**Please Note:**
    
    
    These Custom values will **not** show up in the custom values drop down unless the Order Submitted Trigger is one of the workflow trigger steps.

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48271903161/original/GfNiNTpIzmqHoleW7RVRvGJKHUBrcM8vow.png?1672224689)

  


  * Use conditions related to order details or product details in the If branches to direct the workflow based on the cart value/products purchased/funnel 


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48271903365/original/Fy-l-g5na5xvLpx26kk97KGSVej6hjghwA.png?1672224749)

  


  


* * *

## **Using an Email Template to send an Order Confirmation via this Workflow**

  


* * *

The products purchased by a client can be populated using the Shopping Cart element on an email builder template and using that specific template to send out a confirmation email to the end customer. The Shopping Cart element will auto-populate the product line items along with the purchased quantities, product images, and line item prices. 

  


**Please Note:**
    
    
    The Shopping Cart element will also populate the product images added in the Payments ➝ Products page. In case no image is added for the product, the element will populate the default image on its own. **It is highly recommended to use custom product images while making use of the shopping cart element to avoid any default system-generated images.**

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48271904923/original/uMFRmaT5jF11XlibbTZhrwlAA9Slk44k0w.png?1672225164)

  


All you would need to make sure is that the **Shopping cart** element is added to Template, and the same template is added to the workflow in the **Send Email** action for the values to populate properly.

  


* * *

## **How do submission types filters work?**

**Primary** \- Filters if any primary product is purchased at the checkout on the order form. 

**Bump** \- Filters only if a bump product has been purchased on the order form. The trigger would not work if no bump product has been purchased

**Upsell** \- Filters only in case of upsell purchases. If the filter is set to upsell, the trigger would not run on an order form submission (purchase of a primary/bump product)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48271933980/original/qbQT79u8jkDAXIjo053ldP95IVhs9kG4kw.png?1672231859)  


* * *

## **Will this trigger impact existing Order form submission triggers?**

No, this should not make any changes to an existing order form submission trigger. However, we recommend using the Order submitted trigger to make use of the order-related custom values along with coupon information and product line items.

  


* * *

## **What are the filter types, if/else conditions, and custom values I can use?**

  


**Trigger**|   
| **Filter**| **Operators**| **Selectable items**  
---|---|---|---|---  
Order submission| 1| Product| is, is not| Global product name  
1a| Price| is, is not| Price Name  
2| Order Source| is, is not| Order form  
2a| Submission Type| is, is not| Primary, Bump, Upsell  
3| Funnel| is, is not| Funnel names  
3a| Page| is, is not| Page inside funnel  
3b| Product| is, is not| Funnel level products  
  
  


**If/Else**| **Filter**| **Operators**| **Selectable Items**  
---|---|---|---  
A| Order Source| is, is not| Order form  
B| Product| is, is not| Global product  
C| Payment Gateway| is, is not| Stripe, Paypal  
D| Order Total| Numeric operators| Numeric operators  
E| Submission Type| is, is not| Primary, Bump, Upsell  
F| Funnel| is, is not| Funnel names  
  
  


**Custom Value Category**| **Custom Value**  
---|---  
Order| Currency symbol ($)  
Currency code (USD)  
Cart Total  
Order total  
Coupon code  
Total discount  
Created on  
Created at  
  
| Order ID  
---|---  
Payment Gateway  
  
  


  


**Custom Value Category**| **Custom Value**  
---|---  
Order>Customer| ID  
---|---  
First Name  
Last Name  
Name  
Email  
Phone  
Full Address  
City  
State  
Country  
  
| Postal Code  
---|---

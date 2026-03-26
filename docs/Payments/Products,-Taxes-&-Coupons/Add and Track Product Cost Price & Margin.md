# Add and Track Product Cost Price & Margin

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007434-add-and-track-product-cost-price-margin](https://help.gohighlevel.com/support/solutions/articles/155000007434-add-and-track-product-cost-price-margin)  
**Category:** Payments  
**Folder:** Products, Taxes & Coupons

---

Track your product profitability by adding cost price and margin details to any product price or variant. This gives you a built-in way to understand what you earn on every sale, without needing external spreadsheets or manual calculations.

* * *

**TABLE OF CONTENTS**

  * What is Cost Price & Margin Tracking?
  * Key Benefits of Tracking Cost Price and Margin
  * Prerequisites
  * How to Enable Margin Tracking for Products
  * How to Enable Margin Tracking for Product Variants
  * How Cost Price & Margin Sync
  * How Cost Price Appears in Invoices & Calendars
  * Transactions CSV: Line Item Cost Price
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Cost Price & Margin Tracking?**

  


Product Cost Price & Margin are optional fields you can enable for any product or variant in HighLevel. Once enabled, they provide a structured and accurate view of each products profitability directly inside the Products module. When cost price is defined, it also flows into the Transactions CSV export as a dedicated **Line Item Cost Price** column, allowing profitability analysis at the transaction level.  
  


Knowing these terms will help keep your team aligned when tracking product cost price and margin:  
  


  * **Cost Price:** What the product costs your business to deliver or acquire (always ≥ 0).  
  


  * **Margin (Amount):** The difference between your selling price and cost price (Selling Price − Cost Price). Margin amount can be positive or negative.  
  


  * **Margin (Percentage):** Expresses that difference as a percentage of cost price ((Selling Price − Cost Price) ÷ Cost Price × 100). If cost price is 0, margin percentage is treated as 100%.


* * *

## **Key Benefits of Tracking Cost Price and Margin**

  


  * **Platform-Native Profitability Tracking:** Know your margin per product at a glance, without leaving the platform.  
  

  * **Automatic Calculations:** Enter either cost price or margin (Amount or Percentage) and the other calculates automatically.  
  

  * **Flexible:** Works for one-time and recurring products, across prices and variants.  
  

  * **Consistent Costs:** Cost price stays accurate even when invoice or calendar prices are manually overridden.  
  

  * **Export-Ready Data:** Export transaction-level cost data in CSV for finance and reconciliation workflows.


* * *

## **Prerequisites**

  


  * Access to **Payments** → **Products** in your account.  
  

  * At least one product created (new or existing).  
  

  * **Permissions:** Users need product create/edit permissions to configure cost price and margin.


* * *

## **How to Enable Margin Tracking for Products**

  


Cost Price and Margin are configured at the price level (for standard products) or variant level (for products with variants). The fields appear inside the Pricing section when creating or editing a product.

  


To track product cost price and margin, follow the steps below.

  


  


#### _**Step 1:** Navigate to Products_

  


In the left menu, click **Payments**. Then in the top ribbon, click **Products** to open the Products page.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066312095/original/QRHvMabHtkIQiXCMf2qvcvf3g7bcNK6wVg.png?1772731792)  
  


#### _**Step 2:** Create a Product_

  


Click the **\+ Create Product** button to create a new product, or click on an existing product to edit it.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066312144/original/YwAAhd9z1I3AN19DKvm9jsPlooLjeQNcpQ.png?1772731840)  
  


#### _**Step 3:** Go to the Pricing Section_

  


In the product creation or edit flow, scroll to the **Pricing** section. For existing products, click **Edit** next to the price you want to configure.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066312257/original/HUa0lCxjraGY5RsbENG4sz3_w82pq58Zlg.png?1772731934)  
  


#### _**Step 4:** Enable the Add Margin Checkbox_

  


Inside the Pricing section, check the **Add Margin** checkbox. This reveals the Cost Price and Margin fields. The checkbox is unchecked by default, enabling it does not affect existing transactions.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066312360/original/qDwDri7DUyGDEgektLq5l6l4mUj3s-3U3g.png?1772732014)

  


  


#### _**Step 5:** Enter Cost Price or Margin_

  


Select either amount or percentage based on what you would like the margin to be represented as. Then enter either value and the other calculates automatically based on your selling price:

  


  * **Cost Price:** The amount it costs your business to deliver this product. Cannot be a negative number.  
  

  * **Margin:** The profit above cost. Toggle between Amount and Percentage mode using the toggle next to the field.


  

    
    
    **Note:** If you check 'Add Margin' but leave both fields empty, the system treats Cost Price as equal to Selling Price and exports accordingly keeping the margin at 0.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066313691/original/K1o1pI6PZ0Kv4JyvoPwh95HyG7-gd22N-Q.png?1772733275)

  


  
  
  
#### _**Step 6:** Save the Product_

  


Click **Save**. Cost price and margin are now stored at the price level for this product and will be reflected in exports going forward.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066313766/original/IgeMZQSK3Ka6YR0XPItA8aPzO7gTlaTtCg.png?1772733326)

* * *

## **How to Enable Margin Tracking for Product Variants**

  


Cost Price and Margin are configured at the variant level for products with variants. To track product variant cost price and margin, follow the steps below.

  

    
    
    **Tip:** You must create variants for the product before enabling margin tracking.

  


  


#### _**Step 1:** Go to Variants_

  


In the product edit flow, go to the **Variants** section.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066314293/original/tLy01Y204evYH0FxhS8g31c4GIl3wAueqQ.png?1772733722)

  


  


#### _**Step 2:** Edit Variant_

  


Click **Edit** on the variant you want to configure.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066315987/original/XAIdNrWs-8KnDojbwRlNkYynQBTFgdN6jg.png?1772735346)

  


  


#### _**Step 3:** Enable the Add Margin Checkbox_

  


Inside the variant's Pricing section, check the **Add Margin** checkbox.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066316031/original/Llb4283rATlPQbS0THVZRIu7HBAbEa0LuQ.png?1772735388)

  


####   
**_Step 4:_**_Enter Cost Price or Margin_

  


Select either amount or percentage based on what you would like the margin to be represented as. Then enter either value and the other calculates automatically based on your selling price:

  


  * **Cost Price:** The amount it costs your business to deliver this product. Cannot be a negative number.  
  

  * **Margin:** The profit above cost. Toggle between Amount and Percentage mode using the toggle next to the field.


_  
_

_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066316062/original/gzftWcMpqc3VwcDMvHcU_Py1z58P24nRcw.png?1772735441)_  


  


#### _**Step 5:** Save and Repeat_

  


Save then repeat for each variant.

  

    
    
    **Tip:** Each price denomination and each variant combination has its own independent cost price and margin. This means you can track different margins per denomination (e.g., $25 vs $100 options) or per variant (e.g., Small vs Large).

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066316115/original/KFq7oXlGWk7uo1WfpoQV-DQxHrVT3ms7Xg.png?1772735490)

* * *

## **How Cost Price & Margin Sync**

  


The two fields stay in sync automatically based on the selling price. Switching modes or changing the selling price recalculates the dependent field instantly.

  


  


### **Amount Mode**

  


  * **Margin** = Selling Price − Cost Price  
  

  * **Cost Price** = Selling Price − Margin  
  

  * **Cost Price** must be greater than or equal to 0 (>= 0)  
  

  * **Margin** can be Positive or Negative


  


  


### **Percentage Mode**

  


  * **Margin %** = ((Selling Price − Cost Price) ÷ Cost Price) × 100


  

    
    
    **Tip:** A Margin % above 100% is not valid unlike Markup which can be above 100. Since a margin is divided by cost price, it is restricted on the upper limit of 100% and a lower limit of -100%.

  
  
  
  


### **When Selling Price Changes**

  


If you update the selling price of a product, the system automatically recalculates margin based on the existing cost price. Similarly, switching between Amount and Percentage mode recalculates the fields without data loss.

* * *

## **How Cost Price Appears in Invoices & Calendars**

  


In Invoices and Calendars, selling prices can be manually overridden at the line item level. In these cases, cost price behavior works as follows:

  


  * **Cost Price is always sourced from the original product price**. Currently it is not recalculated based on the overridden selling price.  
  

  * Margin is not recalculated at the invoice or calendar level.  
  

  * Setup fees on recurring products are excluded from margin logic.  
  

  * For subscription products, only the recurring amount is used for margin — not the setup fee.


* * *

## **Transactions CSV: Line Item Cost Price**

  


A new Line Item Cost Price column is available in the Transactions CSV export. This makes it possible to analyze profitability at the transaction and line item level.

  


  


### **How to Access the Export**

  


  1. Go to **Payments** → **Transactions**.  
  

  2. Click **Export CSV**.  
  

  3. The **Line Item Cost Price** column appears automatically for all products in a transaction where cost price has been defined.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066214875/original/Y0KxlOGHp7_JMeTBru-vfwd8pwQJd4f-sw.png?1772645261)

  


  


### **Column Behavior**

  


  * If cost price is defined for a product → the cost amount is shown.  
  

  * If cost price is not defined → the column is blank.  
  

  * For overridden prices in invoices or calendars → cost price from the original product is used.  
  

  * Applies to one-time payments, subscription payments, and partial payments.  
  

  * Partial payments: The full product cost price is shown, not a prorated amount.


  

    
    
    **Important:** Cost price data is not applied retroactively. Only transactions created after cost price is configured for a product will have this column populated.

* * *

## **Frequently Asked Questions**

  


**Q: Can I add cost price to existing products?**

Yes. Open any existing product, edit the price or variant, and check the Add Margin checkbox. This does not affect past transactions — only future ones will carry the cost data.

  


**Q: What happens if I leave the fields blank after checking Add Margin?**

If the Add Margin checkbox is checked but no values are entered, the system treats Cost Price as equal to the Selling Price. This value is passed through to CSV exports.

  


**Q: Is cost price visible to customers?**

No. Cost price is an internal field and is not displayed to customers at checkout, on receipts, or on invoices.

  


**Q: Can I set different cost prices per variant?**

Yes. Each variant combination has its own independent cost price and margin fields, so you can track different profitability per variant.

  


**Q: Does changing a product's selling price update the cost price automatically?**

No. When the selling price changes, the margin is recalculated based on the existing cost price — the cost price itself does not change. This keeps your input intact while margin stays accurate.

  


**Q: Can I bulk-edit cost prices across multiple products?**

Not in this release. Bulk cost price editing is planned for a future phase as part of the bulk edit feature.

  


**Q: Are setup fees included in margin calculations for recurring products?**

No. Setup fees are excluded from margin logic. Only the recurring amount is used when calculating cost price and margin for subscription products.

  


**Q: Are historical transactions updated when I add cost price to a product?**

No. Cost price data is not applied retroactively. Only transactions created after you configure cost price for a product will include the Line Item Cost Price in exports.

* * *

## **Related Articles**

  


  * [Export or Download Transactions as CSV](<https://help.gohighlevel.com/en/support/solutions/articles/155000007157>)  
  

  * [Getting Started - Create & Sell Products](<https://help.gohighlevel.com/en/support/solutions/articles/155000005071>)  
  

  * [How to Add Product Weights, Dimension, and SKU Information in Your Ecom Store](<https://help.gohighlevel.com/en/support/solutions/articles/155000002825>)  
  

  * [How to Create Invoices in HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/48001208702>)

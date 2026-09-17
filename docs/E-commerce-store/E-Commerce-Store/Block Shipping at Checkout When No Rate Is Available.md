# Block Shipping at Checkout When No Rate Is Available

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008685-block-shipping-at-checkout-when-no-rate-is-available](https://help.gohighlevel.com/support/solutions/articles/155000008685-block-shipping-at-checkout-when-no-rate-is-available)  
**Category:** E-commerce store  
**Folder:** E-Commerce Store

---

E-Commerce Settings

# Block Shipping at Checkout When No Rate Is Available

Prevent customers from completing checkout when no shipping method matches their delivery address, helping you avoid orders with unavailable or unintended free shipping.

What You'll Learn

This article explains how the Block Shipping at Checkout feature helps store owners control order fulfillment by preventing checkout when no valid shipping rate exists for the customer's delivery address.

You'll learn how to enable the setting, understand how shipping validation works across Checkout and Upsell pages, and customize the error message appearance to match your store branding.

Table of Contents

1

What is Block Shipping at Checkout?

2

Key Benefits

3

How Shipping Validation Works

4

Dynamic Cart Actions and Address Updates

5

Customizing Error Message Appearance

6

How to Enable Block Shipping at Checkout

7

Related Articles

8

Frequently Asked Questions

1

## What is Block Shipping at Checkout?

Block Shipping at Checkout is a setting that prevents customers from completing an order when no valid shipping method is available for their delivery address. This helps you avoid fulfillment issues caused by orders placed to locations you cannot ship to or orders that might receive unintended free shipping due to missing rate conditions.

The setting is located under Settings → Shipping & Delivery and is OFF by default. When enabled, the checkout process is blocked if the system successfully calculates shipping but finds no applicable rate for the customer's cart and delivery location.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080599253/original/K_jCMMXQY4PMuWvLSw-4JGE1CFg1b7lKCA.png?1789043513)

2

## Key Benefits

Enabling Block Shipping at Checkout provides control over order fulfillment and helps maintain accurate shipping cost calculations.

**Prevent Unfulfillable Orders** — Block checkout when no configured shipping rate matches the customer's delivery address, avoiding orders you cannot ship.

**Avoid Unintended Free Shipping** — Ensure customers cannot complete checkout with free or incorrect shipping when your rate conditions don't cover their location.

**Improve Customer Communication** — Display clear "Shipping not available" messages so customers understand why they cannot complete checkout.

**Maintain Store Branding** — Customize error message colors to match your store's visual identity across Checkout and Upsell pages.

**Preserve Existing Behavior** — The setting defaults to OFF, so your current checkout flow remains unchanged until you explicitly enable it.

3

## How Shipping Validation Works

When Block Shipping is enabled, HighLevel validates shipping availability at two key points in the customer journey to ensure a consistent experience.

Validation Point 1

Checkout Page

When the customer enters their delivery address on the Checkout page, the system calculates available shipping methods. If no valid rate is found for the cart and address combination, the checkout process is blocked and a "Shipping not available" message is displayed.

Validation Point 2

Upsell Element

If the customer accepts an upsell offer, the system re-validates shipping for the updated cart contents. If adding the upsell item makes the cart undeliverable to the customer's address, the "Shipping not available" message is shown and the order cannot proceed.

Important

Checkout is blocked only when shipping calculation succeeds but returns no applicable rate. If shipping calculation fails due to a system error, checkout is not blocked by this setting.

4

## Dynamic Cart Actions and Address Updates

When checkout is blocked due to unavailable shipping, customers have options to resolve the issue depending on their cart contents.

Cart Action 1

Remove Undeliverable Items

If the cart contains multiple items and only some cannot be shipped to the delivery address, customers can remove the undeliverable items to proceed with the remaining shippable items.

Cart Action 2

Clear the Cart

Customers can clear their entire cart and start over, allowing them to select different products or change their delivery address before adding items again.

Cart Action 3

Update Delivery Address

When the customer changes their delivery address in the checkout form, HighLevel automatically re-evaluates shipping availability. If the new address matches a configured shipping rate, the checkout block is lifted and the customer can complete their order.

Note

Digital-only carts are not affected by this setting, as shipping is not required for digital products. Checkout proceeds normally when all items in the cart are digital.

5

## Customizing Error Message Appearance

Store owners can customize the color of the "Shipping not available" error message to match their store's branding. This customization applies to both the Checkout page and the Upsell element, ensuring a consistent visual experience.

To customize the error message color, access your store's theme settings and modify the error text color value. The selected color will be applied wherever the shipping error message appears during the checkout process.

[Screenshot: Theme customization panel showing error message color picker for shipping validation messages]

Quick Tip

Test Your Shipping Configuration Before Enabling

Use a test order with different delivery addresses to verify your shipping zones and rate conditions work as expected before enabling Block Shipping at Checkout on your live store.

6

## How to Enable Block Shipping at Checkout

Follow these steps to enable the Block Shipping setting and configure your store to prevent checkout when no valid shipping rate is available.

Step 1

Navigate to Shipping Settings

In your HighLevel account, go to **Payment** > **Settings > Shipping & Delivery** to access your store's shipping configuration.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080599315/original/9l5LuwRTd3_qnYsIiTwl5bz6T0Ber5K_iA.png?1789043550)

Step 2

Enable Block Shipping Option

Locate the **Block Shipping** toggle and enable it. This activates checkout blocking when no valid shipping method is available for the customer's delivery address.

Step 3

Configure Shipping Zones and Rates

Set up your shipping zones, profiles, and rate conditions to define where you can ship and what rates apply. Ensure your configuration covers all regions you intend to serve.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080599352/original/jnl82Yu9RGROnj9jHzoS2iLmdCMxIgU92Q.png?1789043565)

Step 4

Publish Your Store

Save your changes and publish your store to apply the Block Shipping setting to your live checkout pages. Publishing clears the cache and ensures the latest configuration is active.

Pro Tip

If the setting does not appear to take effect immediately on your live store, republish the page or site to force a cache refresh and apply the latest configuration.

7

## Related Articles

  * [How to Configure Shipping Zones and Rates in HighLevel Stores](<https://help.gohighlevel.com/en/support/solutions/articles/155000002842>)
  * [Managing Checkout Settings for Your HighLevel Store](<https://help.gohighlevel.com/en/support/solutions/articles/155000004467>)
  * [Understanding Shipping Profiles and Conditions](<https://help.gohighlevel.com/en/support/solutions/articles/155000002842>)


8

## Frequently Asked Questions

Q: Does Block Shipping affect digital product orders?

No. Digital-only carts are not affected by the Block Shipping setting because shipping is not required for digital products. Customers can complete checkout normally when their cart contains only digital items.

Q: What happens if the setting is OFF?

When Block Shipping is OFF (the default state), your store behaves as it did before this feature was released. Customers can complete checkout even if no matching shipping rate is found, which may result in free or incorrect shipping being applied.

Q: When exactly does checkout get blocked?

Checkout is blocked only when shipping calculation succeeds but no applicable shipping rate is found for the customer's cart and delivery address. If shipping calculation fails due to a system error, this setting does not block checkout.

Q: Can customers see which items are causing the shipping issue?

Yes. When checkout is blocked, the "Shipping not available" message is displayed along with options to remove specific undeliverable items or clear the entire cart, depending on the cart contents.

Q: Does this setting apply to upsell offers?

Yes. Shipping is re-validated when a customer accepts an upsell offer. If adding the upsell item makes the cart undeliverable to the customer's address, the "Shipping not available" message is shown and the order cannot proceed.

Q: What should I do if the setting doesn't appear to work after enabling it?

If the Block Shipping setting does not take effect immediately on your live store, republish your page or site. This clears the cache and ensures the latest configuration is applied to the checkout process.

Q: Can I customize the "Shipping not available" message text?

Currently, you can customize the color of the error message to match your store branding, but the message text itself is fixed. Color customization applies to both the Checkout page and Upsell elements.

Q: What happens when a customer updates their delivery address?

Shipping availability is automatically re-evaluated when the customer changes their delivery address in the checkout form. If the new address matches a configured shipping rate, the checkout block is lifted and the customer can complete their order.

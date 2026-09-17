# How to Skip Credit Card Collection for $0 Orders in Forms and Surveys

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008519-how-to-skip-credit-card-collection-for-0-orders-in-forms-and-surveys](https://help.gohighlevel.com/support/solutions/articles/155000008519-how-to-skip-credit-card-collection-for-0-orders-in-forms-and-surveys)  
**Category:** Sites  
**Folder:** Forms

---

Forms & Surveys

# Zero-Dollar Checkout for Sell Products

Skip credit card collection on free orders using the Require Credit Card setting in Forms and Surveys

What You'll Learn

The Require Credit Card setting on the Sell Products element allows you to hide payment fields when an order totals $0 with no recurring charges. This article explains how to configure the setting, when payment fields are hidden, and how the feature handles edge cases like coupons, subscriptions, and Funnel-embedded forms.

You'll learn step-by-step setup instructions, key behaviors, and frequently asked questions about zero-dollar checkouts in Forms and Surveys.

Table of Contents

1

What is Zero-Dollar Checkout?

2

Key Benefits

3

How Payment Fields Are Hidden

4

How to Enable Zero-Dollar Checkout

5

Special Cases and Behaviors

6

Frequently Asked Questions

1

## What is Zero-Dollar Checkout?

Zero-Dollar Checkout allows customers to complete free orders in Forms and Surveys without entering credit card details. When a product order totals $0 and has no recurring charges scheduled, the payment fields are hidden automatically, creating a frictionless checkout experience for free offers.

The feature is controlled by a new Require Credit Card toggle on the Sell Products element. When disabled, the system evaluates the order total and recurring schedule—if both are zero, payment collection is skipped. Free orders are still recorded in submission and order history, maintaining complete tracking.

This functionality works across Forms and Surveys on desktop and mobile, and integrates with coupons, order bumps, and Funnel-embedded contexts.

2

## Key Benefits

Zero-Dollar Checkout improves conversion rates and user experience by removing unnecessary friction from free offers. The feature provides several operational and customer-facing advantages.

**Improved Conversion Rates** — Removing credit card requirements on free orders reduces abandonment and increases completion rates for lead magnets, free trials (when zero-cost today), and promotional products.

**Coupon-Driven Flexibility** — When a 100% discount coupon is applied, payment fields are hidden automatically as the total reaches $0, supporting dynamic promotional campaigns.

**Complete Order Tracking** — Free orders are created and recorded in submission history, ensuring analytics and reporting remain accurate.

**Backward Compatibility** — The setting defaults to ON (requiring card), so existing Forms and Surveys continue to behave exactly as before unless you choose to disable it.

**Cross-Platform Support** — The feature works consistently on desktop and mobile devices, ensuring a unified experience regardless of how customers access your forms.

**Safe Defaults** — If the system cannot confirm a $0 total (e.g., pricing summary fails to load), card collection is always shown to prevent payment failures.

3

## How Payment Fields Are Hidden

Payment fields are hidden automatically when the Require Credit Card toggle is disabled and specific conditions are met. The system evaluates the order in real time to determine whether to show or hide the payment section.

Condition 1

Order Total is $0

The combined price of all selected products, variants, and order bumps must equal zero. This includes base prices, quantity adjustments, and any applied coupons.

Condition 2

No Recurring Charges Scheduled

The order must not include any subscriptions, recurring payments, or free trials that will charge the customer in the future. Even if the total is $0 today, a card is required if a future payment is scheduled.

Condition 3

Total is Confirmed and Stable

The pricing summary must load successfully and remain stable. If a customer submits the form while the total is updating (e.g., after a product, variant, coupon, or order bump change), card collection is shown to prevent payment errors.

Note

If any condition fails or cannot be confirmed, the system defaults to showing the payment fields and collecting card details. This fail-safe behavior ensures that paid orders are never incorrectly processed as free.

When all conditions are met, the payment element is removed from the form entirely—customers proceed directly to submission without encountering card fields.

4

## How to Enable Zero-Dollar Checkout

Enabling Zero-Dollar Checkout requires disabling the Require Credit Card toggle on the Sell Products element in your Form or Survey. Follow these steps to configure the setting.

Step 1

Open the Form or Survey Builder

Navigate to the Form or Survey where you want to enable Zero-Dollar Checkout. Open the builder interface to access the element settings.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079392729/original/pqr9nSYrPynPZqnBYOTShEeUq4QmiK5riw.png?1787786060)

  


Step 2

Select the Sell Products Element

Click on the Sell Products element in your form. If you haven't added one yet, add a new Sell Products element from the element panel.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079392797/original/Z2nK3Dh4VSJ_yNzYzbiKn5YqEPs1unG2TQ.png?1787786344)

Step 3

Disable the Require Credit Card Toggle

In the element settings panel, locate the Require card for $0 orders toggle. Turn the toggle OFF to enable Zero-Dollar Checkout. When disabled, orders that total $0 with no recurring charges will hide payment fields automatically.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079392759/original/pLFiEHEALqlBfhpPlGzLAqYcdJW9LQtyzQ.png?1787786231)

Step 4

Save and Publish

Save your changes and publish the Form or Survey. The new behavior will apply immediately for any orders that meet the zero-dollar conditions.

Tip

The setting defaults to ON (requiring card), so you must manually disable it for each Sell Products element where you want to allow zero-dollar checkouts. This ensures existing forms continue to work as expected.

5

## Special Cases and Behaviors

Zero-Dollar Checkout handles several edge cases and special scenarios to ensure reliable payment processing. Understanding these behaviors helps you design forms that work correctly across different use cases.

Scenario 1

Funnel-Embedded Forms and Surveys

When a Form or Survey is embedded in a Funnel, the Funnel-level Require Credit Card setting takes precedence over the element-level setting. Configure the Funnel's payment settings to control zero-dollar behavior for embedded forms.

Scenario 2

Subscriptions and Free Trials

Subscriptions and free trials always require a credit card, even when the current charge is $0. A card is needed to process future recurring payments, so payment fields are shown regardless of the Require Credit Card setting.

Scenario 3

100% Discount Coupons

When a customer applies a 100% discount coupon that reduces the order total to $0, payment fields are hidden automatically as soon as the total updates. This works dynamically in real time as the customer interacts with the form.

Scenario 4

Unstable or Unconfirmed Totals

If the pricing summary fails to load, or if the customer submits the form while the total is still updating after a product, variant, coupon, or order bump change, the system shows payment fields and collects card details. This fail-safe prevents payment processing errors.

Scenario 5

Donation and Custom-Amount Payment Types

Donation and custom-amount payment types are out of scope for this feature. Their behavior is unchanged, and payment fields are always shown regardless of the Require Credit Card setting.

Scenario 6

Card Details Preservation on Paid Orders

Card details entered on paid orders are now preserved when changing quantity or applying a coupon. Customers no longer need to re-enter payment information when modifying their order.

Improvement

The payment element no longer briefly appears and disappears on $0 orders, creating a smoother visual experience. Additionally, Surveys embedded in Funnels now receive Funnel context correctly, ensuring consistent behavior across all form types.

6

## Frequently Asked Questions

Q: Does the Require Credit Card setting affect existing Forms and Surveys?

No. The setting defaults to ON (requiring card), so existing Forms and Surveys continue to work exactly as before. You must manually disable the toggle to enable zero-dollar checkouts.

Q: Are free orders still tracked in submission and order history?

Yes. Free orders are created and recorded, so submissions and order history remain complete. You can track all orders (free and paid) in your HighLevel account.

Q: What happens if a Form or Survey is embedded in a Funnel?

The Funnel-level Require Credit Card setting takes precedence over the element-level setting. Configure the Funnel's payment settings to control whether card collection is required for $0 orders in embedded forms.

Q: Do subscriptions and free trials require a credit card even when the total is $0?

Yes. Subscriptions and free trials always require a credit card, even when nothing is due today, because a card is needed to process future recurring charges.

Q: Can I use Zero-Dollar Checkout with coupon codes?

Yes. When a customer applies a 100% discount coupon that reduces the order total to $0, payment fields are hidden automatically as soon as the total updates. This works in real time as the customer interacts with the form.

Q: What happens if the pricing summary fails to load?

If the pricing summary fails to load or the total cannot be confirmed as $0, the system shows payment fields and collects card details. This fail-safe ensures that paid orders are never incorrectly processed as free.

Q: Does Zero-Dollar Checkout work on mobile devices?

Yes. Zero-Dollar Checkout is fully supported across desktop and mobile experiences, ensuring a consistent checkout flow regardless of device.

Q: Can I use this feature with donation or custom-amount payment types?

No. Donation and custom-amount payment types are out of scope for this feature. Their behavior is unchanged, and payment fields are always shown.

7

### Related Articles

[How to Use Products in Payment Element in Forms](<https://help.gohighlevel.com/support/solutions/articles/155000002546>)

[Payments Integration in Surveys | Collect Payments & Sell Products](<https://help.gohighlevel.com/support/solutions/articles/155000004641>)

[Getting Started with Coupons](<https://help.gohighlevel.com/support/solutions/articles/155000007524-getting-started-with-coupons>)

[Getting Started - Create & Sell Products](<https://help.gohighlevel.com/support/solutions/articles/155000005071/>)

[Create Forms & Surveys Inside the Site Builder](<https://help.gohighlevel.com/support/solutions/articles/155000006719-create-forms-surveys-inside-the-site-builder>)

[Forms - How to Setup and Use Order Bumps](<https://help.gohighlevel.com/support/solutions/articles/155000005767-forms-how-to-setup-and-use-order-bumps>)

# Payments - What Is Listed on the Subscriptions Page?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001225935-payments-what-is-listed-on-the-subscriptions-page-](https://help.gohighlevel.com/support/solutions/articles/48001225935-payments-what-is-listed-on-the-subscriptions-page-)  
**Category:** Payments  
**Folder:** Orders, Subscriptions, and Transactions

---

Payments • Subscriptions • Billing

Payments - What Is Listed on the Subscriptions Page?

The Payments Subscriptions page gives you one place to review recurring subscriptions created through supported payment and checkout flows. You can review customer, provider, amount, status, source, transaction, and other available subscription details without relying only on the payment provider dashboard. For eligible SaaS V1 subscriptions, supported plan changes can also keep the corresponding selling-sub-account subscription aligned with the current Stripe product and price.

What You'll Learn

Learn what appears on the Subscriptions page, how provider statuses are represented, which subscription information stays synchronized, what is excluded, and how eligible SaaS V1 plan changes affect the corresponding subscription record.

Important

The actions available for a subscription can depend on its payment provider, current status, and your Payments permissions. Subscription actions are managed from the Subscriptions area when supported, while eligible payment refunds are handled from **Payments > Transactions**.

Table of Contents

1

What is the Payments Subscriptions Page?

2

Key Benefits

3

What Is Listed on the Subscriptions Page?

4

What Is Shown in Subscription Details?

5

Subscription Statuses by Payment Provider

6

How Subscription Data Stays in Sync

7

What Is Not Listed?

8

How To Access and Use the Subscriptions Page

9

Frequently Asked Questions

10

Related Articles

1

# What is the Payments Subscriptions Page?

The Payments Subscriptions page is the central location for reviewing recurring subscription records created through supported payment flows in a sub-account. It brings provider, customer, source, billing, status, and available transaction information together so billing teams can monitor active and historical subscriptions without checking each provider separately.

2

## Key Benefits of the Payments Subscriptions Page

Keeping subscription information in one billing workspace makes it easier to monitor customers, investigate subscription issues, and manage supported lifecycle changes. The page also provides a consistent subscription view even when provider-specific terminology differs.

  * **Centralized Visibility:** Review recurring subscription records without opening each payment provider dashboard.
  * **Customer Context:** See customer, source, provider, amount, creation date, and status information together.
  * **Billing Tracking:** Review supported subscription transactions and current subscription details.
  * **Status Clarity:** Provider-specific subscription states are grouped into consistent subscription statuses.
  * **Subscription Management:** Eligible subscriptions can be updated, paused, resumed, canceled, or otherwise managed when the provider, status, and user permissions support the action.
  * **SaaS V1 Alignment:** Supported SaaS V1 upgrades and downgrades can keep the corresponding selling-sub-account subscription aligned with the current Stripe product and price.


3

## What Is Listed on the Subscriptions Page?

Subscriptions can reach the Payments area through more than one supported sales or billing flow. Understanding the source and fields shown on each record helps you determine where a subscription originated and which provider is managing it.

The page can include subscriptions created through supported sources such as:

  * Manual subscription creation, such as from a contact's Payments area, when supported by the selected provider.
  * Supported 1-Step and 2-Step Order Form subscription purchases.


Available list information can include:

  * Payment provider and subscription ID
  * Customer details
  * Source of subscription creation
  * Creation date
  * Subscription amount
  * Subscription status


4

## What Is Shown in Subscription Details?

Opening a subscription gives you more context than the list view alone. The available details help connect the subscription to its payment provider, original source, customer, and supported billing activity.

  * Payment provider information
  * Source of subscription creation
  * Available customer and billing details
  * Current subscription information
  * Subsequent transactions for supported Stripe-created subscriptions


### Metadata

Some subscriptions can include additional metadata captured during checkout or subscription creation, such as a company name or other supported contextual information.

5

## Subscription Statuses by Payment Provider

Payment providers can use different names for similar lifecycle states. HighLevel groups supported provider states into subscription statuses so teams can interpret subscription health more consistently from the Payments area.

HighLevel Status| Stripe State| PayPal State  
---|---|---  
**Trial**|  trialing| —  
**Active**|  active| active  
**Canceled**|  canceled| canceled  
**Suspended**|  —| suspended  
**Failed**|  incomplete_expired| —  
**Incomplete**|  incomplete, past_due| approval pending, approved  
**Unpaid**|  unpaid| —  
**Expired**|  —| expired  
  
**Provider-specific states:** The table shows how the documented Stripe and PayPal states are grouped on the Subscriptions page. A blank mapping means that provider does not use the listed state in this documented mapping.

6

## How Subscription Data Stays in Sync

Synchronization behavior depends on the payment provider and the type of subscription workflow involved. Separating general provider status synchronization from SaaS-specific plan-change synchronization prevents broader sync expectations than the platform supports.

### Stripe Subscriptions

For supported Stripe-created subscriptions, subscription status and received payment information can remain synchronized with Stripe. For example, when a supported subscription is canceled in Stripe, the corresponding subscription can reflect a Canceled status in the Subscriptions list.

### PayPal Subscriptions

PayPal-created subscriptions can appear in the Subscriptions list, but the documented PayPal behavior does not continuously synchronize subscription status or capture subsequent payments in the same way as Stripe.

SaaS V1 Plan-Change Sync

For an eligible SaaS V1 subscription sold through a selling sub-account, a supported SaaS upgrade or downgrade can update both the Stripe subscription and the corresponding selling-sub-account subscription. This keeps the current product and price aligned after the qualifying plan change.

**Not retroactive:** Historical mismatches between Stripe and an existing selling-sub-account subscription are not automatically backfilled. A future qualifying SaaS plan change can update both records through the supported synchronization flow.

**Direct Stripe edits:** Do not assume arbitrary changes made directly to a Stripe subscription automatically trigger the SaaS V1 selling-sub-account bridge. The bridge is documented for supported SaaS upgrade and downgrade events.

7

## What Is Not Listed on the Subscriptions Page?

Not every recurring payment or recurring billing configuration creates a record in the Payments Subscriptions list. Knowing the exclusions helps prevent a missing record from being mistaken for a synchronization problem.

  * **Failed initial subscription creation:** If the first payment fails while the order form is being submitted and the subscription is never successfully created, it is not registered as a subscription on this page.
  * **Recurring invoice templates:** Recurring templates created in the Invoices area are not listed as subscription records here.
  * **Membership-created subscriptions:** Subscriptions created inside the Memberships area are not included in this documented Subscriptions-page list.


**Initial payment failure:** An order-form contact can still be created even when the first subscription payment fails, so review the contact and payment activity separately if no subscription record appears.

8

## How To Access and Use the Subscriptions Page

Opening the Subscriptions page gives you access to recurring billing records and the actions supported for each subscription. Review the provider, status, and available actions before making a lifecycle change because available controls can vary by subscription.

### Step 1: Open the Subscriptions Page

  1. Open the applicable sub-account.
  2. Go to **Payments > Subscriptions**.


![Navigation to Payments and the Subscriptions page](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48264662842/original/nYrVD0WunUATbEJp7ykfwC3_o7wD2W2VNA.gif?1669047414)

### Step 2: Open a Subscription

  1. Find the subscription using the available customer, status, provider, or other list information.
  2. Open the subscription to review its details.
  3. Review the available actions before making changes.


### Step 3: Use the Appropriate Billing Action

Subscription and payment actions are handled in different areas:

  * **Update a supported subscription:** Use the available subscription actions to modify eligible products, quantities, dates, or other supported settings.
  * **Pause, resume, or cancel:** Use the subscription action when it is supported by the provider, status, and your permissions.
  * **Refund an eligible payment:** Go to **Payments > Transactions** and use the refund action on the applicable transaction.
  * **Export subscription records:** Use the available download/export action from the Subscriptions page when your permissions allow it.


9

## Frequently Asked Questions

Q: Can I change products or quantities without canceling and recreating a subscription?

For eligible subscriptions, yes. The Update action can modify supported products, quantities, and dates without recreating the subscription. Availability depends on the provider and subscription status.

Q: Do subscription updates change past transactions?

No. Supported subscription updates affect future billing behavior and do not rewrite completed historical transactions.

Q: Does a subscription export include the latest updated values?

Yes. Subscription exports use the latest available subscription data, including updated product or quantity information.

Q: Why can another user see a subscription but not update or cancel it?

Payments permissions can separately control subscription viewing, updating, pausing or resuming, cancellation, and other actions. The subscription's provider and status can also affect which actions are available.

Q: Does editing a SaaS V1 subscription directly in Stripe guarantee the selling-sub-account record will update?

No. Do not assume arbitrary direct Stripe edits trigger the SaaS V1 bridge. The synchronization is documented for supported SaaS upgrade and downgrade events.

Q: Will the SaaS V1 bridge automatically fix older Stripe and selling-sub-account mismatches?

No. Historical mismatches are not automatically backfilled. A future qualifying plan change can update both records through the supported plan-change synchronization flow.

10

### Related Articles

[ How to Modify Existing Subscriptions ](<https://help.gohighlevel.com/support/solutions/articles/155000006066-how-to-modify-existing-subscriptions>) [ How to Manage Refunds within the CRM ](<https://help.gohighlevel.com/support/solutions/articles/48001238332-how-to-manage-refunds-within-the-crm->) [ Export or Download Subscriptions as CSV ](<https://help.gohighlevel.com/support/solutions/articles/155000007159-export-or-download-subscriptions-as-csv>) [ Subscription Settings - Failed Payment Retries ](<https://help.gohighlevel.com/support/solutions/articles/155000004691-subscription-settings-failed-payment-retries>) [ Managing Granular Permissions for Payments ](<https://help.gohighlevel.com/support/solutions/articles/155000006470-managing-granular-permissions-for-payments>) [ How to Upgrade or Downgrade a SaaS Plan for a Location ](<https://help.gohighlevel.com/support/solutions/articles/48001207110>)

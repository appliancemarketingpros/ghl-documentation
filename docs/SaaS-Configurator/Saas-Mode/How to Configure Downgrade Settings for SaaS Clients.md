# How to Configure Downgrade Settings for SaaS Clients

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006450-how-to-configure-downgrade-settings-for-saas-clients](https://help.gohighlevel.com/support/solutions/articles/155000006450-how-to-configure-downgrade-settings-for-saas-clients)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

SaaS • Downgrades • Retention

How to Configure Downgrade Settings for SaaS Clients

Downgrade Settings in HighLevel let agencies give SaaS clients a self-service path to move to a lower plan while retaining control over timing and retention offers. Agencies can collect downgrade reasons, optionally present a discount to eligible clients, and review downgrade activity. For eligible SaaS V1 subscriptions, the downgrade lifecycle also determines when Stripe and the corresponding selling-sub-account subscription are synchronized.

What You'll Learn

Learn how to enable self-service downgrades, configure downgrade reasons and retention discounts, understand when a downgrade becomes effective, track activity, and recognize when eligible SaaS V1 subscription synchronization occurs.

Important

**Scheduling a downgrade does not immediately change the client's active plan.** The client keeps the current plan and features until the scheduled effective date. For an eligible SaaS V1 selling-sub-account subscription, synchronization occurs when the supported downgrade becomes effective.

Table of Contents

1

What are Downgrade Settings for SaaS Clients?

2

Key Benefits

3

Behavior & Billing Rules

4

SaaS V1 Subscription Sync at the Effective Date

5

How To Set Up the Downgrade Flow

6

Customer Downgrade Flow

7

Track Activity Using Downgrade Logs

8

Frequently Asked Questions

9

Related Articles

1

# What are Downgrade Settings for SaaS Clients?

Downgrade Settings in HighLevel's SaaS Configurator control whether sub-account admins can move themselves to a lower-tier SaaS plan. Agencies can enable or disable self-service downgrades, customize the reasons clients choose when downgrading, and optionally present eligible clients with a retention discount before the downgrade is scheduled. This creates a structured downgrade path while preserving visibility into churn reasons and outcomes.

2

## Key Benefits of Configuring Downgrade Settings for SaaS Clients

A structured downgrade experience gives clients more control while helping agencies preserve revenue, understand churn, and maintain predictable billing behavior. Configuring these settings before clients need them also reduces manual support work during plan changes.

  * **Self-Service Control:** Clients can initiate an eligible downgrade from their Billing area without contacting support.
  * **Churn Insight:** Configurable downgrade reasons help identify recurring pricing, adoption, or usability concerns.
  * **Revenue Protection:** Eligible V1 clients can be presented with an optional discount offer before the downgrade is scheduled.
  * **Predictable Billing:** This downgrade flow schedules the lower plan for the next billing cycle instead of changing the subscription mid-cycle.
  * **Auditability:** Activity Logs provide visibility into downgrade attempts, deflections, reasons, plans, and users.


3

## Behavior & Billing Rules

Downgrade timing determines when billing and feature access actually change. Understanding these rules helps agencies explain the client experience accurately and distinguish a scheduled downgrade from one that has already become effective.

  * **Monthly discount duration:** For eligible monthly subscriptions, the retention discount applies for the number of months configured by the agency.
  * **Annual discount duration:** For eligible annual subscriptions, the discount applies for one year.
  * **Scheduled effective date:** The downgrade takes effect at the start of the next billing cycle.
  * **No mid-cycle proration:** This scheduled downgrade flow does not create a mid-cycle refund or partial charge.
  * **Access until the change:** Clients keep their current-plan features until the scheduled effective date.
  * **Keep My Plan:** Clients can cancel a scheduled downgrade before its effective date and remain on the current plan.
  * **Upgrades remain available:** Eligible clients can still access supported upgrade options from Billing.


**Retention outcome:** If a client accepts the discount offer, the downgrade is canceled. The client remains on the current plan and the discount begins according to the configured billing-cycle behavior.

4

## SaaS V1 Subscription Sync at the Effective Date

Eligible SaaS V1 subscriptions sold through a selling sub-account can have both a Stripe subscription and a corresponding subscription record in that selling sub-account. Because a configured downgrade is future-effective, the subscription bridge should be understood in relation to the date the lower plan actually becomes active.

Stage| What Happens  
---|---  
**Downgrade scheduled**|  The current plan remains active. The client keeps current-plan features until the effective date.  
**Discount accepted**|  The downgrade is canceled, so no effective downgrade should be implied.  
**Keep My Plan selected**|  The scheduled downgrade is canceled before it becomes effective.  
**Downgrade becomes effective**|  For an eligible V1 selling-sub-account subscription, the supported plan-change flow updates Stripe and the corresponding selling-sub-account subscription.  
  
**After an eligible V1 downgrade becomes effective:** The current product and price can remain aligned between the supported subscription records, downstream invoices can reflect the new plan information, and applicable tax can be recalculated using current plan data when tax is already configured.

**Not retroactive:** Historical mismatches between Stripe and an existing selling-sub-account subscription are not automatically backfilled. A future qualifying plan change can update both records through the supported synchronization flow.

**Manual Stripe edits:** Do not assume arbitrary subscription changes made directly in Stripe trigger the selling-sub-account synchronization. The bridge is documented for supported SaaS upgrade and downgrade events.

5

## How To Set Up the Downgrade Flow

Configure the downgrade flow before enabling it for clients so the available reasons, retention offer, and timing match your agency's billing and retention strategy. The global setting controls whether eligible sub-account admins can access the self-service downgrade experience.

### Step 1: Enable Downgrades

Enabling the downgrade option makes the self-service downgrade action available to eligible client administrators. Keep the setting off if your agency wants all downgrade requests handled manually.

  1. From **Agency View** , go to **SaaS Configurator > Downgrade Settings**.
  2. Turn **Allow clients (account admins) to downgrade their subscription** ON or OFF.


**Note:** When the setting is disabled, clients do not see the self-service downgrade option in their billing settings.

![Downgrade Settings showing the self-service downgrade toggle](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055636163/original/6MCqa6RCirjMgSlvhG5mWVnvbhlUVOqp0w.png?1760022696)

### Step 2: Manage Downgrade Reasons

Downgrade reasons capture structured feedback at the moment a client considers moving to a lower plan. Use reasons that help your team identify actionable pricing, adoption, or product trends.

  * Start with the provided default reasons, such as pricing or feature-usage concerns.
  * Edit existing reasons to match your business.
  * Remove reasons that are not relevant.
  * Add new reasons up to the supported character limit.


**Tip:** Keep downgrade reasons concise and distinct so Activity Logs can reveal meaningful churn patterns instead of collecting overlapping answers.

![Downgrade Settings showing configurable downgrade reasons](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055636753/original/EvtUMBiiZSPNHGx9WhOrLYL3KxfotkYlZg.png?1760022917)

### Step 3: Configure Discount Offers

A retention discount can give an eligible V1 client a reason to remain on the current plan before the downgrade is scheduled. If the client accepts the offer, the downgrade is canceled and the client stays on the existing plan.

  1. Turn **Enable Discount Offer** ON.
  2. Enter the discount percentage.
  3. For monthly plans, configure the discount duration.
  4. Choose whether an eligible client can receive the offer more than once.
  5. Click **Save**.


**V1 only:** Discount deflections are currently available for supported SaaS V1 flows and are not currently supported for V2 downgrade flows.

![Downgrade Settings showing the optional retention discount configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055636962/original/fr9ngHUBRrS0WjOSf1pOP_rqYhstqxbENw.png?1760023052)

6

## Customer Downgrade Flow

The customer flow separates the decision to downgrade from the date the new plan becomes active. Clients first choose a reason and, when eligible, see the configured retention offer before the downgrade is scheduled for the next billing cycle.

  1. Go to **Account Settings > Billing > Modify Subscription > Downgrade**.

![Client Billing page showing the option to modify or downgrade a SaaS subscription](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055641814/original/ShuTPzhfpUw9C-zIvjIKyhuFxhhJslulzQ.png?1760025155)

  2. Select a **downgrade reason** from the agency's configured list.

![Client downgrade flow showing the downgrade reason selection](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055641644/original/jCP2Sxno3vYsMqrAZZEVdPTP-9tdeqp_5A.png?1760025062)

  3. If an eligible V1 retention offer is enabled, review the discount. If the client accepts it, the downgrade is canceled and the client remains on the current plan.

![Client downgrade flow showing the optional retention discount offer](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055642109/original/yjYjTg-bzxwKiSG1B_ixcHoWWKI_d8fQSQ.png?1760025322)

  4. If the client declines or skips the available deflection, the downgrade is scheduled for the **start of the next billing cycle**.

![Confirmation showing the scheduled SaaS downgrade and effective billing date](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055642158/original/AN8VI71V3yHvOC_GMXk2iBXVIAp5UrKvdg.png?1760025384)


**Before the effective date:** The client remains on the current plan. If they select **Keep My Plan** , the scheduled downgrade is canceled and the lower plan never becomes effective.

7

## Track Activity Using Downgrade Logs

Activity Logs help agencies identify why clients consider downgrading, which offers successfully retain clients, and which plan changes proceed. Exportable records also provide a useful audit trail for support and retention analysis.

  1. Go to **SaaS Configurator > Cancellation Settings** and scroll to **Activity Logs**.
  2. Review available information such as the sub-account, timestamp, outcome, downgrade reason, plan change, next billing date, and initiating user.
  3. Use **Download** to export the available activity data for reporting or deeper analysis.


![SaaS Configurator Activity Logs showing downgrade and deflection activity](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155055641370/original/mzlAFYkwYhiTGg7j_6mrFLzUaHQYxWb2UA.png?1760024918)

8

## Frequently Asked Questions

Q: Does scheduling a downgrade immediately change the client's V1 subscription?

No. The current plan remains active until the scheduled effective date. For an eligible V1 selling-sub-account subscription, the supported synchronization occurs when the qualifying downgrade becomes effective.

Q: What happens if the client accepts the discount?

The downgrade is canceled and the client remains on the current plan. The configured discount applies according to the applicable billing-cycle behavior.

Q: Can clients reverse a scheduled downgrade?

Yes. Before the effective date, the client can use **Keep My Plan** from the subscription-management flow to cancel the scheduled downgrade.

Q: Why doesn't a V2 client see the discount offer?

The downgrade discount deflection is currently supported for eligible V1 flows and is not currently available for V2 downgrade flows.

Q: Are existing V1 Stripe and selling-sub-account subscription mismatches automatically fixed?

No. Existing mismatches are not automatically backfilled. A future qualifying plan change can update both records through the supported synchronization flow.

Q: Does changing the subscription directly in Stripe guarantee the selling-sub-account record will sync?

No. Do not assume arbitrary manual Stripe edits trigger the bridge. The synchronization is documented for supported SaaS upgrade and downgrade events.

9

### Related Articles

[ How to Upgrade or Downgrade a SaaS Plan for a Location ](<https://help.gohighlevel.com/support/solutions/articles/48001207110-how-to-upgrade-saas-plan-for-a-location>) [ Getting Started with the SaaS Configurator ](<https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator>) [ SaaS V1 vs SaaS V2: What's the Difference? ](<https://help.gohighlevel.com/support/solutions/articles/155000007968-saas-v1-vs-saas-v2-what%E2%80%99s-the-difference->) [ How to Customize the SaaS Subscription Cancellation Flow ](<https://help.gohighlevel.com/support/solutions/articles/155000005634-how-to-customize-the-saas-subscription-cancellation-flow>) [ How to Cancel SaaS Sub-Account for Your Client ](<https://help.gohighlevel.com/support/solutions/articles/48001216453>) [ Account Billing Dashboard ](<https://help.gohighlevel.com/support/solutions/articles/155000004182-account-billing-dashboard>)

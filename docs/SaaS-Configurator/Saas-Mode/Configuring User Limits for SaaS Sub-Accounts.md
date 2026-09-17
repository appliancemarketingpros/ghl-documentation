# Configuring User Limits for SaaS Sub-Accounts

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001232-configuring-user-limits-for-saas-sub-accounts](https://help.gohighlevel.com/support/solutions/articles/155000001232-configuring-user-limits-for-saas-sub-accounts)  
**Category:** SaaS Configurator  
**Folder:** Saas Mode

---

SaaS • User Limits • Sub-Accounts

Configuring User Limits for SaaS Sub-Accounts

User Limits give agencies control over how many sub-account-level users can be added to SaaS sub-accounts. You can define the user allowance for a SaaS plan and override that limit for an individual client when needed. User Limits are available for SaaS V1 and SaaS V2 plans. This guide explains how User Limits work and how to configure them in the SaaS Configurator.

What You'll Learn

Learn how User Limits control sub-account-level users, how to configure plan-level allowances, which users count toward the limit, and how client-specific overrides work for SaaS sub-accounts.

Important

SaaS plans allow unlimited users by default unless a User Limit is enabled. The configured limit applies only to sub-account-level users; agency-level users assigned to the sub-account do not count toward the limit.

Table of Contents

1\. What Are User Limits for SaaS Sub-Accounts?  
2\. Key Benefits of User Limits for SaaS Sub-Accounts  
3\. Prerequisites and Limitations  
4\. How To Setup User Limits for a SaaS Plan  
5\. How To Override the User Limit for a Specific Sub-Account  
6\. Frequently Asked Questions  
7\. Related Articles

1

# What Are User Limits for SaaS Sub-Accounts?

User Limits let agencies control the maximum number of sub-account-level users that can be added to a SaaS sub-account. This makes it possible to include different user allowances as part of your SaaS packaging.

By default, SaaS plans allow unlimited users unless a User Limit is configured. The limit applies only to sub-account-level users. Agency-level users assigned to the sub-account do not count toward the configured limit.

User Limits are supported for both SaaS V1 and SaaS V2 plans.

2

## Key Benefits of User Limits for SaaS Sub-Accounts

User Limits help agencies package user allowances with SaaS plans while maintaining flexibility for individual clients who need a different number of users.

  * **Plan-Based User Allowances:** Define the maximum number of sub-account-level users available with a SaaS plan.
  * **Flexible SaaS Packaging:** Use different user allowances across SaaS plans to support different service tiers.
  * **Client-Specific Overrides:** Set a different User Limit for an individual SaaS sub-account without changing the underlying plan.
  * **Automatic Plan Alignment:** When a qualifying plan change applies a new plan limit, the sub-account can inherit the User Limit configured for that plan.


3

## Prerequisites and Limitations

Understanding which users count toward the limit helps you choose the appropriate allowance for each SaaS plan and prevents agency users from being included in the sub-account user calculation.

  * The feature applies to sub-accounts using SaaS plans.
  * User Limits are supported for SaaS V1 and SaaS V2 plans.
  * The configured limit applies only to sub-account-level users.
  * Agency-level users assigned to the sub-account do not count toward the limit.
  * SaaS plans allow unlimited users by default until a User Limit is enabled.
  * The User Limit controls how many sub-account-level users can be added to the SaaS sub-account.


4

## How To Setup User Limits for a SaaS Plan

Configuring a User Limit at the plan level defines the maximum number of sub-account-level users available to sub-accounts using that SaaS plan.

  1. From **Agency View** , select **SaaS Configurator**.
  2. Select **Plans & pricing**.
  3. Locate the SaaS plan you want to update.
  4. Select **Edit details**.
  5. Select the **Pricing** tab.
  6. Locate **User limit** and enable the toggle.
  7. Enter the maximum number of users allowed in the sub-account.
  8. Select **Save changes**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081131524/original/Nk9ocF5hab626Pz2h8hH0Sg7cHIfKkQE6g.png?1789615821)

**Plan behavior:** When a qualifying sub-account subscribes to or moves to the plan, the User Limit configured for that plan is applied to the sub-account.

5

## How To Override the User Limit for a Specific Sub-Account

An individual User Limit override lets an agency give a specific SaaS client a different user allowance without changing the standard limit for every sub-account using the same SaaS plan.

**Setup path pending verification:** Confirm the current navigation path to the individual sub-account User Limit before publishing step-by-step instructions for this override.

An individual sub-account override takes precedence over the User Limit configured for its SaaS plan.

Existing User Limits documentation states that upgrading to another SaaS plan resets the override and applies the User Limit configured for the new plan.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081131546/original/tTUhth6KUvXOPrpBZB06z6SPxDo4lgCZcA.png?1789615933)

6

## Frequently Asked Questions

Q: Are SaaS plans required to have a User Limit?

No. SaaS plans allow unlimited users by default unless a User Limit is enabled and configured.

Q: Do agency-level users count toward the User Limit?

No. The limit applies only to sub-account-level users. Agency-level users assigned to the sub-account do not count toward the limit.

Q: Are User Limits available for SaaS V1 and SaaS V2 plans?

Yes. User Limits are supported for both SaaS V1 and SaaS V2 plans.

Q: Can one SaaS sub-account have a different User Limit from its plan?

Yes. User Limits support an individual sub-account override, allowing a client to have a different limit from the SaaS plan's standard allowance.

### Related Articles

  * [ Getting Started with the SaaS Configurator ](<https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator>)
  * [ SaaS V1 vs SaaS V2: What's the Difference? ](<https://help.gohighlevel.com/support/solutions/articles/155000007968-saas-v1-vs-saas-v2-what-s-the-difference->)
  * [ How to Configure Contacts Limit for SaaS Sub-Accounts ](<https://help.gohighlevel.com/support/solutions/articles/155000001305-how-to-configure-contacts-limit-for-saas-sub-accounts>)

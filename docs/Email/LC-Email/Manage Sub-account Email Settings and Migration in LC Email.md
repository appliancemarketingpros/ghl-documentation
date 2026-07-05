# Manage Sub-account Email Settings and Migration in LC Email

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002222-manage-sub-account-email-settings-and-migration-in-lc-email](https://help.gohighlevel.com/support/solutions/articles/155000002222-manage-sub-account-email-settings-and-migration-in-lc-email)  
**Category:** Email  
**Folder:** LC Email

---

Email Management

Migrating Sub-Accounts to LC Email

Filter, migrate, and manage sub-account email providers — one at a time or in bulk — from Agency Settings.

What This Covers

This article explains how to filter sub-accounts by email provider, migrate individual or multiple sub-accounts to LC Email, assign dedicated domains, and answers common questions about domain sharing across sub-accounts.

Table of Contents

1

How to Filter Sub-Accounts' Email Providers

2

Migrate a Sub-Account to LC Email

3

Bulk Migration of Sub-Accounts to LC Email

4

Include LC Email Dedicated Domains for Sub-Accounts

5

Frequently Asked Questions

1

## How to Filter Sub-Accounts' Email Providers

Navigate to **Agency Settings → Email Services → Location Settings** and click the **Filter** button. All your sub-accounts' email service records will be displayed on the page.

![Agency Settings > Email Services > Location Settings with Filter button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252712/original/YmM2wAiqU-5jolPSNg2Yn16al7uTDzUjeA.jpg?1722446880)

Three Filter Options

**1\. LeadConnector** — Sub-accounts using LeadConnector as their default email service.

**2\. Mailgun** — Sub-accounts using Mailgun as their default email service.

**3\. Others** — Sub-accounts using their own third-party email service provider.

Filter Option 1

Filter by LeadConnector

Find all sub-accounts that use LeadConnector as their default email service. You can combine filters to narrow your search further — for example, filtering by both domain name and email verification status simultaneously.

  * Filter by dedicated domain name.
  * Filter by email verification enabled / disabled.


![Filter by LeadConnector options showing domain name and email verification filters](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252730/original/b3tXfxAa4jIefKeh_KPWLI_n0rYjeUzp-Q.jpg?1722446912)

Filter Option 2

Filter by Mailgun

Find all sub-accounts that use Mailgun as their default email service. You also have the option to filter by a specific Mailgun dedicated domain.

![Filter by Mailgun options showing dedicated domain filter](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252742/original/8HTaDVlXljCwRhzz-CWLg4TUNIMzjyR3ZQ.jpg?1722446942)

Filter Option 3

Filter by Other

Find all sub-accounts that use their own third-party email service providers (not LeadConnector or Mailgun).

2

## Migrate a Sub-Account to LC Email

To migrate a single sub-account to LC Email, follow these steps:

Step 1

Open Location Settings

Navigate to **Agency Settings → Email Services → Location Settings**.

Step 2

Select the Sub-Account

Find the sub-account you want to migrate and click the **Pencil (edit) icon** next to it.

![Sub-account list with Pencil icon for editing email settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252762/original/CbERxgMKRVh0fDJblhrCq0B2pqrYalFiaA.jpg?1722446970)

Step 3

Choose LeadConnector and Assign a Domain

Select **LeadConnector** as the email service. Then either select a dedicated domain or set the fallback to **Default (Agency default domain)**. Save your settings.

![LeadConnector selected with dedicated domain or fallback to agency default](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252804/original/_CkxDciIp9pJjtqrwmg3LGbLXZcn9jykQA.jpg?1722447017)

3

## Bulk Migration of Sub-Accounts to LC Email

You can migrate multiple sub-accounts at once using the Filter and Manage tools. The example below walks through migrating all Mailgun sub-accounts — the same approach applies to any provider filter.

Example Walkthrough

Transferring Mailgun Sub-Accounts to LC Email

Transfer all Mailgun sub-accounts, or only those using a specific Mailgun dedicated domain.

Step 1

Filter the Sub-Accounts

Navigate to **Agency Settings → Email Services → Location Settings** and click **Filter**. You have two options:

  * Select **Mailgun** to filter all Mailgun sub-accounts.
  * Select **Mailgun + a dedicated domain** to filter only sub-accounts tied to that specific domain.


Step 2

Select All Sub-Accounts

Once filtered, click the checkbox next to any location name, then use the **Select all** option in the table header to select every sub-account in the results.

![Filtered Mailgun sub-accounts with Select all checkbox option in table header](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252823/original/GcbDyOeWRb0jOej7fLya83evVbYNEEnXrA.jpg?1722447049)

Step 3

Open the Manage Panel

Click the **Manage** button and select **Migrate to LC** under Request type. Click **Confirm** to proceed to domain selection.

![Manage panel with Migrate to LC option selected under Request type](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252832/original/o4JAOKGUd8apM_iQShtIMdw_Jh-3lSWOkA.jpg?1722447078)

Step 4

Choose the Dedicated Domain and Confirm

Select the LC dedicated domain you want to assign to the migrated sub-accounts, then click **Confirm** to complete the migration.

![Domain selection screen for bulk migration with Confirm button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252857/original/g3YFjSvfTOQz18yXlC7aJ_HpfFqTqDkhng.jpg?1722447108)

4

## Include LC Email Dedicated Domains for Sub-Accounts

To assign or update the LC Email dedicated domain for a specific sub-account within your agency:

Step 1

Open Location Settings

Navigate to **Agency Settings → Email Services → Location Settings**.

Step 2

Edit the Sub-Account

Find the sub-account and click the **Pencil (edit) icon** next to it to open its email settings.

![Location Settings list with Pencil edit icon for a sub-account](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155030252871/original/03vYq26qmaasC-Daqia7g0g4t4NV3ACJ_g.jpg?1722447137)

Good to Know

By default, the agency's default dedicated domain is automatically shared with any sub-account that does not have its own dedicated domain assigned.

5

## Frequently Asked Questions

Q: Can I transfer a dedicated domain from one sub-account to another?

You have two options. You can delete the domain from the current sub-account and re-add it to the target sub-account. Alternatively, add the domain at the agency level and share it with one or more sub-accounts using the Manage → Migrate to LC workflow.

Q: Can I share an agency dedicated domain with sub-accounts?

Yes. Filter or search for the sub-accounts, click **Manage** , select **Migrate to LC** under Request type, and choose the agency domain to share. Note: by default, the agency's default dedicated domain is already shared with sub-accounts that don't have their own domain assigned.

Q: Can I share a sub-account's dedicated domain with other sub-accounts?

No. A domain created under a sub-account cannot be shared with the agency or with other sub-accounts. Only agency-level domains can be shared across sub-accounts.

Q: How do I migrate my entire agency over to LC Email?

For a full agency-level migration, see the related article: [How to Migrate My Agency Over to LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>).

Q: What happens to a sub-account's emails during migration?

The migration switches the sub-account's sending provider to LC Email. Any emails sent after migration will route through the newly assigned LC Email domain. In-flight sends at the time of migration may be affected, so plan migrations during low-traffic periods when possible.

Q: Can I filter sub-accounts by both domain and email verification status at the same time?

Yes. When filtering by LeadConnector, you can combine the domain name filter and the email verification enabled/disabled filter simultaneously to narrow your results.

Q: What is the fallback "Agency default domain" option?

When editing a sub-account's email settings, you can set the domain to **Fallback to Default** , which means the sub-account will use the agency's default dedicated domain for sending. This is the automatic fallback for sub-accounts without their own dedicated domain.

Related Articles

[How to Migrate My Agency Over to LC Email](<https://help.gohighlevel.com/a/solutions/articles/48001222501?portalId=48000045315>) [What is LC Email?](<https://help.gohighlevel.com/a/solutions/articles/48001220605?portalId=48000045315>) [How to Enable and Rebill LC Email Verification](<https://help.gohighlevel.com/en/support/solutions/articles/48001235221>) [How to Set Up Unsubscribe Links for LC Email](<https://help.gohighlevel.com/a/solutions/articles/48001225534?portalId=48000045315>)

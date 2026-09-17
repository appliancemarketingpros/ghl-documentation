# Sub-Account Bulk Actions & History

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008680-sub-account-bulk-actions-history](https://help.gohighlevel.com/support/solutions/articles/155000008680-sub-account-bulk-actions-history)  
**Category:** Agency View  
**Folder:** SaaS Configurator

---

Sub-Account Management

Sub-Account Bulk Actions & History in HighLevel

Manage multiple sub-accounts from one workflow, apply supported bulk actions, and review job-level results from Bulk Action History.

What You'll Learn

HighLevel Sub-Account Bulk Actions let agency admins select multiple sub-accounts and apply supported management changes without opening each account individually. Common workflows include enabling SaaS Mode, pausing sub-accounts, enabling rebilling, and managing supported account features, depending on plan, permissions, and configuration.

Bulk Action History provides a centralized record of submitted jobs so you can review the operation, status, user, completion details, and account-level successes or failures. This article explains how to select sub-accounts, use the available bulk actions, and verify results safely.

Bulk Action Availability

The exact actions shown under **Bulk Actions** can vary by agency plan, user permissions, SaaS configuration, feature availability, and the selected sub-accounts. Use the options displayed in your account as the source of truth for currently available workflows.

Table of Contents

1\. What is Sub-Account Bulk Actions & History? 2\. Key Benefits 3\. Before You Begin 4\. Supported Bulk Action Workflows 5\. How to Set Up and Use Bulk Actions 6\. Bulk Enable SaaS Mode 7\. Bulk Pause Sub-Accounts 8\. Review Bulk Action History 9\. Troubleshooting 10\. Frequently Asked Questions 11\. Related Articles

# **What is Sub-Account Bulk Actions & History?**  
  


Sub-Account Bulk Actions are agency-level management tools that apply one supported action to multiple selected sub-accounts. Instead of repeating the same process account by account, agency admins can filter or search the Sub-Accounts list, select the intended accounts, choose a bulk action, configure the required settings, and submit one job.

Bulk Action History complements this workflow by recording submitted jobs and exposing account-level results. This makes it easier to verify completion and investigate individual failures across a larger group of sub-accounts.

## **Key Benefits of Sub-Account Bulk Actions & History**  
  


Bulk management is most useful when several sub-accounts need the same operational change. Centralizing selection, configuration, and result tracking reduces repetitive work while giving administrators a clearer record of what was submitted and how each account processed.

  * **Faster Account Management:** Apply supported changes to multiple sub-accounts without opening each account individually.
  * **Filtered Selection:** Use search, filters, individual checkboxes, or Select all to target the intended accounts.
  * **Consistent SaaS Assignment:** Apply a selected SaaS plan to eligible sub-accounts through a guided workflow.
  * **Safer Pause Decisions:** Choose how SaaS subscriptions and applicable phone or A2P resources should be handled.
  * **Job-Level Visibility:** Review the operation, status, submitting user, creation time, and completion time.
  * **Failure Diagnostics:** Open job details to identify successful accounts, failed accounts, and available error information.


## **Before You Begin**  
  


Bulk actions can affect billing, access, subscriptions, and account-level resources across many sub-accounts at once. Confirm the selected accounts and understand the consequences of the chosen action before submitting the job.

  * Use an **Agency Admin** account with the permissions required for the action.
  * Use search or filters to narrow the Sub-Accounts list before choosing **Select all**.
  * For SaaS activation, confirm the payment-provider configuration and SaaS plan you intend to assign.
  * If different account groups need different SaaS plans, process them in separate jobs.
  * For pausing, decide whether active SaaS subscriptions should stop billing or continue billing while access is paused.
  * Review phone-number and A2P handling carefully because disconnecting and closing phone resources can permanently remove associated numbers and campaigns.


## **Supported Bulk Action Workflows**  
  


The Sub-Accounts page is the central entry point for agency-level bulk management. Available options depend on the account's plan and configuration, so the menu shown in your account determines which workflows can currently be used.

Bulk Workflow| Purpose  
---|---  
**Enable SaaS Mode**|  Apply an eligible SaaS billing configuration and selected SaaS plan to multiple existing sub-accounts.  
**Pause Sub-Account**|  Pause access for multiple sub-accounts while choosing how subscriptions and applicable phone or A2P resources should be handled.  
**Enable Rebilling**|  Configure supported rebilling or usage markup settings across multiple sub-accounts when available.  
**Other Supported Actions**|  Additional workflows may appear as HighLevel expands bulk management capabilities.  
  
## **How to Set Up and Use Sub-Account Bulk Actions**  
  


Every bulk workflow starts by selecting the correct sub-accounts. Use a focused selection whenever possible so the action applies only to the intended accounts, then review the action-specific confirmation before proceeding.

### **Step 1: Open and Select Sub-Accounts**

The Sub-Accounts list provides the search, filtering, selection, bulk-action, and history controls used throughout the workflow.

  1. From Agency View, go to **Sub-Accounts**.
  2. Use search, sort, date, column, or filter controls to narrow the list when needed.
  3. Select the checkbox beside each intended sub-account, or use **Select all** for the applicable selection scope.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080547580/original/0tkIGb8ibSr4lsCkgH8RnmMye8hyPBxD9A.png?1789014501)

### **Step 2: Choose a Bulk Action**

After one or more accounts are selected, the Bulk Actions menu becomes the starting point for the management workflows available to your account.

  1. Confirm the selected-account count.
  2. Click **Bulk Actions**.
  3. Choose the action you want to run.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080547575/original/VZ5VJB7333yLjDOwqfDZ8AzmjS-XC1nqKA.png?1789014490)

## **Bulk Enable SaaS Mode**

Bulk SaaS activation is useful when several existing sub-accounts should move to the same SaaS plan. The workflow asks you to choose the billing setup, select the plan, review the configuration, and confirm the accounts before the job is submitted.

### **Choose the Payment Provider**

Payment-provider options depend on the agency's SaaS billing configuration. Choose the applicable provider before selecting the SaaS plan.

  1. Choose **Enable SaaS** from Bulk Actions.
  2. Select the available payment-provider option.
  3. Click **Continue**.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080547568/original/03FDFdDjxvYyt4kOKMztm8uc7oCUMPC0LA.png?1789014481)

### **Select the SaaS Plan**

The selected plan applies to the sub-accounts included in the current bulk job. Review the billing interval, plan price, included features, and available options before selecting the plan.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080547566/original/99HcmOnPbGUsDTiJHT1uGQqKF2mtOKAIfw.png?1789014473)

### **Review and Confirm SaaS Activation**

The confirmation modal is the final checkpoint before the batch is submitted. Confirm the selected-account count and SaaS plan before proceeding.

  1. Review the number of selected sub-accounts.
  2. Confirm the selected SaaS plan and displayed price.
  3. Click **Proceed** when the configuration is correct.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080547562/original/4PIHMsDjnp6hYSW08jL_EhcUanQtQeWlkA.png?1789014465)

**Payment-method requirement:** A sub-account can be processed into SaaS Mode while the client still needs to provide payment information. If the required payment method is missing, the SaaS subscription may remain On Hold and access can remain restricted until valid payment details are added.

## **Bulk Pause Sub-Accounts**

Bulk pausing lets you restrict access for several sub-accounts in one job while deciding how active SaaS subscriptions and applicable phone or A2P resources should be treated. Billing and resource choices should be reviewed separately because pausing account access does not automatically stop every associated charge.

  1. Select the intended sub-accounts.
  2. Open **Bulk Actions** and choose **Pause Subaccount**.
  3. Under **Subscription Preferences** , choose whether to pause active subscriptions or keep charging clients while access is paused.
  4. Review the option for phone numbers and A2P campaigns.
  5. Click **Proceed** only after verifying the consequences of each selected option.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080547560/original/4fEixD_3Wkbgs1FxG701yZ7Vi2Ppp15HYQ.png?1789014456)

**Important:** Choosing to disconnect and close phone resources can permanently delete phone numbers and A2P campaigns associated with the selected sub-accounts. If the resources remain connected, applicable usage charges can continue while the sub-accounts are paused.

## **Review Bulk Action History**  
  


Bulk Action History provides the audit trail for submitted jobs and is the best place to verify whether a batch completed successfully. Review the job-level summary first, then open full details for any failures to isolate account-specific issues.

### **Open Bulk Action History**  
  


  1. Go to **Agency View → Sub-Accounts**.
  2. Click the **Bulk Action History** clock icon.
  3. Use the date range or available filters to locate the job.
  4. Review the **Job ID** , **Operation** , **Status** , **User** , **Created** , and **Completed** columns.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080547551/original/rN2cqG3RsHhvj3v5Hdyax4wIECrotDTzrw.png?1789014445)

### **Review Account-Level Results**

A completed bulk job can contain a mix of successful and failed sub-accounts. Open the job details to verify which accounts processed successfully and review available error information for accounts that did not complete.

  1. Click **Show Full Details** for the job.
  2. Review the sub-account ID, name, status, and Error Details.
  3. Compare the **Total Sub-Accounts** , **Success** , and **Failed** counts.
  4. Correct the underlying issue before retrying the supported action for failed accounts.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080547549/original/06Yh2PTKrBIMiWS8F105G-WJ-XXiJqOXZQ.png?1789014437)

## **Troubleshooting Sub-Account Bulk Actions**  
  


When a bulk action is missing, fails, or produces mixed results, verify eligibility and configuration before immediately resubmitting the entire batch. Bulk Action History can help determine whether the issue affects the full job or only specific sub-accounts.

Issue| What to Check  
---|---  
**The expected Bulk Action is missing**|  Check the agency plan, user permissions, account configuration, feature availability, and eligibility of the selected sub-accounts.  
**Enable SaaS cannot continue**|  Verify the SaaS billing configuration, payment provider, selected plan, and account eligibility.  
**SaaS activation completes but access is restricted**|  Check whether the client still needs to add a valid payment method and whether the subscription remains On Hold.  
**A paused account is still generating phone usage charges**|  Review whether phone resources were left connected. Pausing access does not automatically close associated phone resources.  
**Some accounts succeeded and others failed**|  Open Bulk Action History, select Show Full Details, and review the available error information for each failed account.  
**The job is still processing**|  Allow the job time to process, then refresh Bulk Action History before submitting a duplicate action.  
  
## **Frequently Asked Questions**  
  


Q: Who can use Sub-Account Bulk Actions?

Bulk-management availability can depend on the agency plan, user permissions, SaaS configuration, feature availability, and account eligibility. Use the options displayed in the Bulk Actions menu as the source of truth for your account.

Q: Can I apply different SaaS plans to different sub-accounts in one bulk job?

The bulk SaaS workflow applies the selected plan to the accounts included in that action. If different groups require different plans, run separate bulk actions.

Q: What happens if a client has no payment method when SaaS is enabled?

The sub-account can be processed into SaaS Mode, but the subscription may remain On Hold and access can remain restricted until the client provides valid payment details.

Q: Can I pause access but keep charging a SaaS client?

The bulk pause workflow can provide separate subscription preferences, including pausing active subscriptions or keeping client charges active while account access is paused.

Q: Does pausing a sub-account automatically stop phone-related usage charges?

No. Review the phone-number and A2P option in the pause workflow. If associated phone resources remain connected, applicable usage charges can continue.

Q: Can one bulk job contain both successful and failed sub-accounts?

Yes. Open Bulk Action History and review Show Full Details to see the result for each sub-account and any available failure information.

Q: Should I retry the entire bulk action if only one account fails?

Review the failed account's error details first. Correct the underlying issue, then retry only the affected account or accounts through the supported workflow.

Q: Where can I find previous bulk-action jobs?

From Agency View, open Sub-Accounts and click the Bulk Action History clock icon. Use the history table and Show Full Details to review previous jobs and account-level results.

### **Related Articles**  
  


[ How to Bulk Manage SaaS Sub-Accounts ](<https://help.gohighlevel.com/support/solutions/articles/155000005270-how-to-bulk-manage-saas-sub-accounts>) [ How to Enable SaaS Mode for Multiple Sub-Accounts in Bulk ](<https://help.gohighlevel.com/support/solutions/articles/155000005614>) [ SaaS Bulk Rebilling Setup for Multiple Sub-Accounts ](<https://help.gohighlevel.com/support/solutions/articles/155000005766>) [ Pause / Resume Sub-Accounts ](<https://help.gohighlevel.com/support/solutions/articles/48001230403/>) [ New Sub-Accounts List UI for $97 & $297 Agency Plans ](<https://help.gohighlevel.com/support/solutions/articles/155000005749>) [ Getting Started with the SaaS Configurator ](<https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator>)

# How to increase Messaging Limits?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006385-how-to-increase-messaging-limits-](https://help.gohighlevel.com/support/solutions/articles/155000006385-how-to-increase-messaging-limits-)  
**Category:** Phone System  
**Folder:** Messaging

---

Messaging · SMS

How to Increase Messaging Limits

Learn how Messaging Limits work, how they differ from Messaging Ramp, and how eligible agencies can adjust limits for supported sub-accounts.

Overview

Messaging Limits help agencies control outbound SMS usage for eligible HighLevel sub-accounts. Depending on the configuration, limits can be based on the number of messages or message segments and may apply at daily or monthly levels.

Important — Messaging Ramp

Messaging Ramp and Messaging Limits are separate systems. Sub-accounts using Messaging Ramp follow a level-based warm-up model and cannot edit their Ramp limits directly. Locations using the Messaging Limits model follow the configurable limits described in this article.

Table of Contents

1\. What Are Messaging Limits?

2\. Messaging Limits vs Messaging Ramp

3\. How to Increase Messaging Limits

4\. Who Can Increase Messaging Limits?

5\. What Happens When a Limit Is Reached?

6\. Messaging Limits and Workflows

7\. Provider and Carrier Restrictions

8\. Frequently Asked Questions

## 1\. What Are Messaging Limits?

Messaging Limits define how much outbound SMS usage is allowed for eligible sub-accounts.

Depending on your configuration, limits can be based on:

  * Number of SMS messages
  * Number of message segments
  * Daily usage
  * Monthly usage


About Message Segments

Longer SMS messages can be split into multiple message segments. Segment-based limits provide more precise control over actual messaging usage than simply counting the number of messages sent.

## 2\. Messaging Limits vs Messaging Ramp

Messaging Limits and Messaging Ramp control outbound messaging in different ways.

Model| How It Works  
---|---  
**Messaging Limits**|  Eligible agencies can configure supported outbound messaging limits for applicable sub-accounts.  
**Messaging Ramp**|  Uses a level-based warm-up system for LC Phone SMS/MMS sending. Locations on Ramp cannot directly edit their Ramp limits.  
  
## 3\. How to Increase Messaging Limits

Eligible agencies can manage Messaging Limits at the agency level or adjust the limit for an individual supported sub-account.

Option 1

Set the Agency-Level Default

Use the agency-level setting to define the default Messaging Limit configuration for eligible sub-accounts.

  1. Go to the **Agency Dashboard**.
  2. Navigate to **Phone Integration**.
  3. Select **Account Creation**.
  4. Configure the applicable daily or monthly limit using messages or segments.


This defines the agency-level default for eligible locations using the Messaging Limits model.

![Agency Dashboard messaging limit configuration screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054389175/original/NBeKu0YnzTLE-I4kFsltPBhP1gpESWL_-Q.png?1758631795)

![Daily limit set by number of messages or segments](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054386293/original/rFjiERegyWrDLvEHj2LozxO_e8fD4_rD7Q.png?1758630811)

**Note:** Sub-accounts that remain on Messaging Ramp continue to follow the Ramp model instead of the agency Messaging Limit configuration.

Option 2

Increase the Limit for One Sub-Account

Use this option when you want to change the Messaging Limit for a specific eligible sub-account.

  1. Open the desired **sub-account**.
  2. Open the applicable **Messaging Limit** settings in the Phone System area.
  3. Review the current usage and configured limit.
  4. Enter the new supported limit and save your changes.


The sub-account setting overrides the applicable default for that location.

**UI verification:** The exact sub-account navigation should be confirmed against the current HighLevel interface before publication because Phone System navigation can vary based on the messaging model available to the location.

![Sub-account Advanced Settings message limit field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054389260/original/hX2d1aS7WUYvru1KGdRVs4FdkpbQ3Zt28w.png?1758631829)

![Entering and saving a new sub-account message limit](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054385648/original/zHFsXFZmnNSlmU7Yw8AylRj65Ati3UaSow.png?1758630714)

## 4\. Who Can Increase Messaging Limits?

Agency Owners and Admins can increase supported Messaging Limits when the agency meets the applicable eligibility requirements.

  * If the agency has been on the platform for at least **3 months** and is not in a trial period, eligible users can update a sub-account's Messaging Limit.
  * If the agency does not meet the requirements or needs a limit beyond the available maximum, contact HighLevel Support for review.


## 5\. What Happens When a Messaging Limit Is Reached?

When a sub-account reaches its allowed outbound messaging limit, additional outbound SMS may be unavailable until capacity becomes available again or the applicable limit is increased.

HighLevel can display an in-app warning when the limit is reached. Depending on the account configuration, notification emails may also be sent to eligible recipients.

Inbound messaging can continue independently of some outbound sending restrictions.

![Messaging limit reached banner and email notification](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155054387801/original/SdY31EEQZNvQ3TdGXB8X_MgV2xJmAGiG-w.png?1758631355)

## 6\. Messaging Limits and Workflows

Messaging limits can also affect automated SMS actions in active workflows.

Important

If a workflow reaches a **Send SMS** action while outbound SMS is unavailable because a Messaging Limit or Ramp restriction has been reached, the SMS action can fail.

Failed SMS messages are not automatically retried after outbound sending becomes available. Review the workflow's **Execution Logs** to identify affected contacts.

## 7\. Provider and Carrier Restrictions

Increasing a HighLevel Messaging Limit does not override other messaging restrictions.

HighLevel, the connected phone provider, and mobile carriers can apply separate requirements related to:

  * Messaging registration
  * Carrier filtering
  * Throughput
  * Compliance
  * Opt-out rates
  * Delivery-error rates


**Best practice:** Scale messaging volume gradually and based on actual business needs. Sudden increases in volume can contribute to carrier filtering and deliverability problems.

## 8\. Frequently Asked Questions

Who can increase Messaging Limits?

Agency Owners and Admins can increase eligible limits when the agency meets the applicable eligibility requirements. If the agency does not qualify or needs a higher limit than the available maximum, contact HighLevel Support.

What is the difference between message-based and segment-based limits?

A message-based limit counts messages sent. A segment-based limit counts the individual SMS segments used by those messages. Longer SMS messages can contain multiple segments.

Does increasing my Messaging Limit guarantee delivery?

No. Increasing a HighLevel Messaging Limit does not override provider restrictions, carrier filtering, messaging registration, compliance requirements, or deliverability rules.

Is Messaging Ramp the same as Messaging Limits?

No. Messaging Ramp uses a level-based warm-up model, while Messaging Limits provide configurable sending limits for eligible locations.

What happens to workflow SMS messages after a limit is reached?

SMS actions that run while outbound messaging is unavailable can fail. Failed SMS actions are not automatically retried after sending becomes available again. Review Workflow Execution Logs for affected contacts.

Can I change the limit for only one sub-account?

Eligible sub-accounts using the Messaging Limits model can have a location-specific limit that overrides the applicable default. Locations using Messaging Ramp follow the Ramp model instead.

## Related Articles

  * [Messaging Ramp Progress Card](<https://help.gohighlevel.com/en/support/solutions/articles/155000005572>)
  * [LC - Phone Messaging Policy ](<https://help.gohighlevel.com/en/support/solutions/articles/48001213941>)
  * [Troubleshooting SMS Delivery Issues ](<https://help.gohighlevel.com/en/support/solutions/articles/48000981696>)
  * [What Is Message Throughput (MPS)? ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004527>)
  * [Best Practices for SMS Deliverability and Avoiding SMS Restrictions](<https://help.gohighlevel.com/en/support/solutions/articles/155000000079>)

# Track SMS Restriction History

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003568-track-sms-restriction-history](https://help.gohighlevel.com/support/solutions/articles/155000003568-track-sms-restriction-history)  
**Category:** Phone System  
**Folder:** Messaging

---

Messaging Compliance

SMS Restriction History

See any warnings or temporary restrictions on SMS sending in a sub-account — what happened, when, and why — so you can fix issues fast and stay compliant.

Overview

The SMS Restriction History dashboard gives you transparent visibility into any warnings or temporary restrictions applied to SMS sending in a sub-account.

It helps you understand what happened, when, and why, so you can quickly correct issues and keep messaging compliant.

Table of Contents

1

What is SMS Restriction History?

2

Where to find the SMS Restriction Log

3

Using the Restriction Log

4

Threshold guidance

5

What are the error and opt-out rates good for having a threshold?

6

Frequently Asked Questions

Video Walkthrough

1

## What is SMS Restriction History?

The **SMS Restriction History** dashboard provides businesses with a transparent way to track and manage their SMS sending activities. Logging warnings and restrictions helps you stay compliant with carrier guidelines and avoid disruptions in communication.

It is a read-only log showing warnings and temporary sending restrictions triggered by carrier- or policy-driven thresholds. Typical causes include:

  * Daily / weekly sending limit violations
  * High opt-out rate
  * High delivery error rate (including carrier filtering such as Error 30007)


Example

If a campaign generates a **6% opt-out rate** — above the 2–3% target you should stay under — the sub-account may receive a temporary restriction. The log captures the date, time, and additional details so you can investigate and avoid repeats.

2

## Where to find the SMS Restriction Log

Navigate to **Location → Settings → Phone system → Messaging**. In the **far-right tab** , click **Restriction History** to view events for the sub-account.

![SMS Restriction History tab under Messaging settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077988571/original/n051ivnJ-CvcP7TKzP7sK7P3mTCnzC0hiQ.png?1786347983)

Note — Filtering Options

On the right-hand side of the table, there are **Start Date** and **End Date** filters, allowing you to view restriction history for a specific time period.

The pagination control at the bottom ensures you can navigate through multiple pages of restriction records.

3

## Using the Restriction Log

The table lists each restriction event with:

  * **Date** — when the warning or restriction occurred
  * **Restriction Type** — Warning or Temporary Restriction
  * **Restriction Reason** — e.g., Opt-out rate exceeded threshold
  * **Percentage / Count** — the measured value at the time (e.g., opt-out %)
  * **Additional Details** — related metrics such as Error Rate


Heads Up

The restriction history is shown in **UTC**.

4

## Threshold guidance

Metric| Good| Target| Lockout (24 hours)  
---|---|---|---  
Opt-out rate| 0–1%| Stay below 2–3%| At 3%  
Delivery error rate| 0–6%| Keep under 10%| At 10%  
  
Important

After a lockout, review recent sends, content, list hygiene, and compliance settings before resuming.

5

## What are the error and opt-out rates good for having a threshold?

Factor 1

High Opt-Out Rate

A high opt-out rate indicates that contacts receiving your messages have objected, generated complaints, or marked your SMS as spam. A good opt-out rate is typically in the range of **0–1%**. Once the opt-out rate hits **3%** , the sub-account will be locked for sending text messages for 24 hours.

Factor 2

High Delivery Error Rate

A high delivery error rate indicates that you are sending SMS to contacts that are no longer in service, are unreachable, or use a non-SMS-capable device such as a landline. This may also mean that external carrier filters are refusing to deliver your SMS due to bad sending behavior in the past. A good error rate is typically in the range of **0–6%**. Once the error rate hits **10%** , the sub-account will be locked for sending text messages for 24 hours.

6

## Frequently Asked Questions

Q: Does Restriction History show real-time data?

It records **events with timestamps** ; use the date filters to explore specific windows of time.

Q: Will I see both warnings and temporary restrictions?

Yes — the log includes **warnings** and **temporary restrictions** along with the reason and measured values.

Q: How do I lower my error rate?

Clean your lists regularly, remove landlines, verify numbers during capture, and avoid content patterns that trigger carrier filtering.

Q: How long does a temporary restriction last?

When a sub-account hits a lockout threshold (opt-out rate at 3% or error rate at 10%), SMS sending is locked for **24 hours**. Use that window to review your recent sends and compliance settings before resuming.

Q: Why is the restriction history shown in UTC?

Restriction events are logged in **UTC** for consistency across sub-accounts and time zones. When cross-referencing an event with your own sending activity, convert the timestamp to your local time.

Q: Can I filter the log by date?

Yes. Use the **Start Date** and **End Date** filters on the right-hand side of the table to view a specific time period, and the pagination control at the bottom to move through multiple pages of records.

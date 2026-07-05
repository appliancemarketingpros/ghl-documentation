# Microsoft Smart Network Data Services (SNDS)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004151-microsoft-smart-network-data-services-snds-](https://help.gohighlevel.com/support/solutions/articles/155000004151-microsoft-smart-network-data-services-snds-)  
**Category:** Email  
**Folder:** LC Email

---

EMAIL DELIVERABILITY

IP Status Monitoring with Microsoft SNDS

Monitor the deliverability health of your dedicated IPs on Outlook and Hotmail before problems reach your inbox rate.

What You'll Learn

If you've purchased an IP subscription, you now have access to **IP Status Monitoring** through a Microsoft SNDS (Smart Network Data Services) integration. This lets you track your IPs' deliverability health on Microsoft platforms and catch potential issues before they hurt your sending reputation.

Table of Contents

1

What is Microsoft SNDS?

2

How to Use the IP Status Feature

3

Interpreting Key Metrics

4

How to Handle IP Blocking or High Spam Rates

5

Frequently Asked Questions

1

## What is Microsoft SNDS?

Microsoft SNDS is a tool that provides insight into the email activity of your IPs on Microsoft platforms, such as Outlook and Hotmail. It reports on IP health, spam complaints, filter results, and blocked status — giving you the information you need to keep your emails landing in the inbox instead of the spam folder.

2

## How to Use the IP Status Feature

Step 1

Access the IP Status Dashboard

Navigate to **Settings → Email Services → Postmaster Tools → Microsoft SNDS**.

![Navigating to Microsoft SNDS under Postmaster Tools](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035109257/original/RkEAgvx1tE7wc_8z2jcSbEll7Q5tyNZNBw.png?1729520424)

Step 2

Select the IP Address

You'll see a list of your IPs with metrics including:

  * **Filter Results** — the percentage of messages flagged as spam.
  * **Blocked Status** — whether the IP is blocked on Microsoft platforms.
  * **Trap Hits** — the number of messages flagged by spam traps.
  * **Complaint Rate** — the percentage of recipients who reported your emails as spam.


Step 3

Review the IP Health Overview

Click **View Details** for an in-depth look at the selected IP, including:

  * **Activity Period** — the timeframe of email activity.
  * **RCPT Commands and DATA Commands** — the volume of messages processed.
  * **Spam and Complaint Rates** — helps you understand the IP's reputation.


Step 4

Download CSV Reports

For advanced reporting, click **Download CSV** to export detailed activity for further analysis.

3

## Interpreting Key Metrics

![Microsoft SNDS key metrics overview](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035109530/original/zyeGdoevGu4d1ngOfTqb0vFFXK_V9gaHxQ.png?1729520626)

Metric| Healthy Range| What It Means  
---|---|---  
Filter Results| Below 10% spam| 10% or higher means some emails are being classified as spam. Review your sending practices, content, and lists.  
Blocked Status| No| "Yes" means your IP is blocked due to possible spam behavior or policy violations and needs immediate attention.  
Trap Hits| 0| One or more hits suggests your list contains invalid or suspicious addresses that should be cleaned.  
Complaint Rate| Below 0.1%| Above 0.1% means recipients are marking your emails as spam. Review your content and confirm opt-in.  
RCPT Commands| Aligned with volume| Total recipients who received your emails. Monitor to ensure volume matches your expected campaign size.  
DATA Commands| Aligned with volume| Total data payloads processed, reflecting messages transmitted. Keep consistent with planned sends to avoid triggering filters.  
Trap Message Period| 0 days| Number of days your emails were detected by spam traps. Any non-zero value requires immediate investigation.  
Red Days (Filter Result Issues)| 0| One or more red days means some days had higher spam rates or deliverability issues. Investigate the sending patterns for those periods.  
  
Tip

Check these metrics regularly rather than only after a deliverability problem shows up — catching a rising complaint rate or a Red Day early makes it much easier to fix before it affects your inbox placement.

4

## How to Handle IP Blocking or High Spam Rates

If your IP is blocked or shows a high spam rate, work through these steps:

Step 1

Review Your Metrics

Analyze recent activity, especially around trap hits and complaints.

Step 2

Clean Your Mailing Lists

Remove invalid or inactive addresses and confirm that all recipients have opted in.

Step 3

Request IP Delisting

If your IP is blocked, submit a delisting request using the [Microsoft Outlook Support page](<https://olcsupport.office.com/>).

Important

Blocked IPs and non-zero Trap Message Periods require immediate action — the longer a sending issue goes unaddressed, the harder it is to rebuild your reputation with Microsoft.

5

## Frequently Asked Questions

Q: Is IP Status Monitoring included with my IP subscription?

Yes. If you've purchased an IP subscription, IP Status Monitoring through Microsoft SNDS is available to you at no additional cost under **Settings → Email Services → Postmaster Tools**.

Q: Why don't I see any data for my IP yet?

Microsoft SNDS only reports on IPs with recent sending activity on its platforms. If your IP is new or hasn't sent much volume to Outlook or Hotmail recipients, data may take a few days to populate.

Q: Does this monitoring cover Gmail or Yahoo as well?

No. Microsoft SNDS only reports on activity for Microsoft-owned mailbox providers, such as Outlook and Hotmail. Other providers have their own postmaster tools that report separately.

Q: How often does the IP Status dashboard update?

Microsoft SNDS data typically refreshes daily. Check the dashboard regularly, especially after sending large campaigns, so you can catch issues like a rising complaint rate before they escalate.

Q: What should I do first if I see a Trap Hit?

Start by reviewing how the affected address entered your list. Remove it along with any other unengaged or unverified contacts, and confirm all remaining recipients have properly opted in before your next send.

Q: How long does a delisting request take once submitted?

Timelines vary by case, since Microsoft reviews each delisting request individually. In the meantime, continue cleaning your lists and monitoring your metrics so your IP is in good standing once it's delisted.

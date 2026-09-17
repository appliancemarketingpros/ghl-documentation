# Set Up Automatic Opt-Out and Sender Info Updates in Messaging Compliance

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006771-set-up-automatic-opt-out-and-sender-info-updates-in-messaging-compliance](https://help.gohighlevel.com/support/solutions/articles/155000006771-set-up-automatic-opt-out-and-sender-info-updates-in-messaging-compliance)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS/MMS Compliance

Auto-Updating Opt-Out & Sender Info

Keep ongoing SMS/MMS conversations compliant, consistent, and carrier-approved — automatically, without extra manual effort.

What You'll Learn

Staying compliant with SMS/MMS regulations can be complex, especially when managing multiple campaigns. This article explains how to use the **Automatically Add Opt-Out & Sender Info to Messages Periodically** feature to keep your conversations compliant, consistent, and carrier-approved.

You'll learn what the feature does, why it matters, and how to configure it step-by-step inside your account.

Table of Contents

1

What Is Auto-Updating Opt-Out & Sender Info?

2

Key Benefits

3

How to Set Up Auto-Updating Opt-Out Message & Sender Info

4

Frequently Asked Questions

1

## What Is Auto-Updating Opt-Out & Sender Info?

This feature is a built-in **compliance automation** that appends required **opt-out language** and **sender details** to your SMS/MMS conversations at regular intervals.

It ensures that ongoing conversations continue to meet standards set by **TCPA** , **CTIA** , **GDPR** , and **CCPA** , reducing the risk of regulatory penalties or message filtering.

Once configured, the system automatically refreshes compliance details such as “Reply STOP to unsubscribe” and your sender name without you having to manually add them to each conversation.

2

## Key Benefits

This automation is designed to simplify compliance and maintain healthy message deliverability across your campaigns.

**Continuous Compliance** — ensures required disclosures are periodically included in all active SMS/MMS threads.

**Customizable Frequency** — choose how often compliance details are refreshed, from 1 to 60 days (default: 30 days).

**Effortless Automation** — works in the background, reducing manual oversight and administrative time.

**Higher Deliverability** — keeps messages aligned with carrier and regulatory guidelines, minimizing spam filtering.

**Improved Transparency** — builds trust with recipients by maintaining clear sender identification and opt-out visibility.

Setup Guide

How to Set Up Auto-Updating Opt-Out Message & Sender Info

Each step below matches the order of actions shown in the screenshots for clear, visual guidance.

3

## How to Set Up Auto-Updating Opt-Out Message & Sender Info

Follow these steps to enable automatic compliance updates for your SMS/MMS conversations.

Before You Start

Per-Sub-Account Control

The **Enable Periodic Opt-Out** setting is controlled at the **sub-account (location)** level. Turn it on to automatically re-add sender info and opt-out language at regular intervals for ongoing conversations.

When to Turn It On

  * You want compliance language refreshed automatically for long-running threads.
  * You send recurring promotions or nurture messages and want consistent opt-out visibility.


When to Turn It Off

  * You only need the first-message compliance behavior and do not want periodic re-insertion.
  * You handle follow-up compliance language manually (not recommended).


Defaults

**New sub-accounts:** Enabled. **Existing sub-accounts:** Disabled.

The first outbound message behavior does not change — sender info and opt-out language still apply to the first outbound message in a conversation.

Step 1

Navigate to Settings

From your main dashboard, click **Settings** in the left navigation menu. This is where all system-level configurations are managed.

![Settings in the left navigation menu](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673225/original/yZgrKyZ9AcEayLR6sDrBaDBdQZlwxZJaCw.png?1761216175)

Step 2

Open Phone Numbers under Settings

In the Settings menu, select **Phone Numbers**. This area manages your messaging, voice, and compliance configurations for all connected phone numbers.

![Phone Numbers under Settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673278/original/WTbY05gedpMahf3YSOnahPlXukZiPinAlg.png?1761216199)

Step 3

Go to the Messaging Tab

At the top of the Phone System page, click the **Messaging** tab. This tab includes all settings related to message delivery, compliance, and analytics.

![Messaging tab on the Phone System page](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673422/original/2wbAd271moAAxe1W8ncGA8exNhbEJu5WEg.png?1761216266)

Step 4

Open the Messaging Compliance Section

Inside the Messaging tab, select the **Messaging Compliance** sub-tab. This section contains compliance-related controls, including opt-out messaging, sender details, and periodic compliance automation.

![Messaging Compliance sub-tab](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056674386/original/FxUg3VFlGjspu6zvIkKGR4clWcaR3AteTw.png?1761216797)

Step 5

Add an Opt-Out Message

Adding an opt-out message ensures every outbound SMS contains a clear unsubscribe option — a key requirement under TCPA and CTIA.

  1. Enable **Make SMS compliant by adding an opt-out message**.
  2. Enter your opt-out text (for example, _Reply STOP to Unsubscribe!_).
  3. Click **Customize** to open the edit window.


![Opt-out message setting](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056674022/original/jeMAi8xivw2q9V6PvjJlmnCrTv6aYceASw.jpeg?1761216668)

![Customize opt-out message window](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673569/original/x8XDsGR49AM0etDpm0OCYtagrTc6AagZaA.png?1761216353)

Step 6

Add Sender Information

Including sender details adds transparency, helping recipients identify who the message is from — improving trust and compliance.

  1. Enable **Make SMS compliant by adding sender information**.
  2. Enter your business name or sender signature (e.g., _Thanks, Chase Sandbox_).
  3. Click **Customize** to edit the sender text and placement.


![Sender information setting](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673590/original/g-bRefMYWPlWdqOebKPqWo7ayLT9vLZtOA.png?1761216397)

![Sender information field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673630/original/nCMHAol7dqbw0oRe0zk2pM-evl90G77HDw.png?1761216437)

![Customize sender information window](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673661/original/7ELeLgKBhoaHye4fRFc_EDgPGoFY8H3vRw.png?1761216458)

Step 7

Enable Periodic Opt-Out

Periodic opt-out ensures ongoing conversations remain compliant by re-adding sender and opt-out details automatically after the selected interval — maintaining regulatory adherence and message deliverability without manual updates.

  1. Toggle **Enable Periodic Opt-Out** **On** (or **Off** to disable periodic re-insertion for this sub-account).
  2. In **Include Sender ID & Opt-Out Message Every [X] Days**, choose your interval (1–60 days).
  3. Click **Save** to apply your changes.


![Enable Periodic Opt-Out setting with day interval](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673866/original/87ks2l_4vkI5uxEsv_gWl7Stfo3sLKS-5Q.png?1761216523)

Step 8 · Optional

Apply Regional Restrictions

Optionally, enable **Block any SMS/MMS to Texas recipients or from Texas area-code numbers** if applicable to your region. This ensures compliance with state-specific messaging regulations.

![Regional restrictions setting](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155056673894/original/o63j_NXEFxCnQZ9WoLvJtKiFQegtUrL1yQ.png?1761216556)

4

## Frequently Asked Questions

Q: Does this automation update previous conversations?

No. The automation applies only to **new and ongoing** conversations. Past messages remain unchanged.

Q: How does the system determine when to re-add opt-out information?

The automation uses the **frequency interval** you set (for example, every 30 days). It automatically tracks message threads and refreshes compliance information once the interval elapses.

Q: Can I disable this feature if I handle compliance manually?

Yes. While the automation is integrated for consistent protection, you can adjust the frequency to a longer interval or disable it temporarily by unchecking the **Enable Periodic Opt-Out** box.

Q: How does this feature affect message deliverability and carrier filtering?

Carriers often filter or block messages missing proper sender or opt-out details. By keeping your messages compliant and updated, this feature helps maintain higher delivery rates and prevents carrier penalties or message suppression.

Q: What interval should I choose?

You can set any interval from **1 to 60 days**. The default of **30 days** works well for most senders — it keeps opt-out language visible without over-repeating it. Choose a shorter interval for high-frequency campaigns and a longer one for low-volume, long-running threads.

Q: Is this setting applied to all sub-accounts at once?

No. **Enable Periodic Opt-Out** is controlled at the **sub-account (location)** level, so you configure it individually for each sub-account. New sub-accounts have it enabled by default, while existing sub-accounts have it disabled.

Q: Will the first outbound message still include compliance details?

Yes. The first-message behavior does not change — sender info and opt-out language still apply to the first outbound message in a conversation, regardless of whether periodic opt-out is enabled.

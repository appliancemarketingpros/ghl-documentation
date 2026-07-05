# ESP Block Monitoring and Progressive Email Enforcement

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008003-esp-block-monitoring-and-progressive-email-enforcement](https://help.gohighlevel.com/support/solutions/articles/155000008003-esp-block-monitoring-and-progressive-email-enforcement)  
**Category:** Email  
**Folder:** Email Delivery Troubleshooting

---

EMAIL DELIVERABILITY

ESP Block Monitoring & Progressive Email Enforcement

How the platform detects rising ESP blocks, warns you, and pauses sending to protect your sender reputation.

Overview

The platform monitors ESP blocks to help protect sender reputation and email deliverability. When mailbox providers reject too many emails from a sub-account, the platform may send a warning email or temporarily pause email sending. This article explains how ESP block enforcement works, what each warning means, and what to do if your email sending is paused.

Table of Contents

1

What is ESP Block Monitoring and Progressive Email Enforcement?

2

Key Benefits of ESP Block Monitoring

3

How ESP Block Enforcement Works

4

Warning Email: Risk of Suspension

5

12-Hour Temporary Suspension

6

In-App Suspension Banner

7

24-Hour Temporary Suspension

8

Future Enforcement: Permanent Suspension

9

How to Prevent ESP Block Enforcement

10

What to Do If Your Email Sending Is Paused

11

Frequently Asked Questions

12

Related Articles

1

## What is ESP Block Monitoring and Progressive Email Enforcement?

ESP blocks happen when mailbox providers such as Gmail, Outlook, or Yahoo reject emails due to sender reputation, authentication, engagement, content, or sending behavior. Monitoring these blocks helps protect your sub-account and the broader email infrastructure the platform relies on.

The platform's ESP Block Monitoring and Progressive Email Enforcement system automatically reviews ESP block activity at the sub-account level. When block activity exceeds healthy thresholds, the platform may send a warning email, temporarily pause email sending, or apply future enforcement if repeated issues continue.

2

## Key Benefits of ESP Block Monitoring

ESP block monitoring helps identify deliverability risks early and gives users time to correct sending issues before they cause long-term reputation damage.

**Sender Reputation Protection** — helps prevent continued sending when mailbox providers are rejecting emails.

**Improved Deliverability** — reduces harmful sending signals that can affect inbox placement.

**Early Warning** — notifies users before email sending is temporarily paused.

**Platform Protection** — helps protect shared email infrastructure across the platform.

**Automatic Enforcement** — works automatically without manual setup.

3

## How ESP Block Enforcement Works

Progressive enforcement gives users time to correct email sending issues before stronger restrictions are applied. The process starts with a warning and may move to temporary sending pauses if ESP block activity continues.

Enforcement may be applied in this order:

  1. A warning email is sent when ESP block activity rises above healthy levels.
  2. If excessive blocks continue, email sending may be paused for 12 hours.
  3. If the issue happens again, email sending may be paused for 24 hours.
  4. In a future enforcement phase, repeated suspension occurrences may lead to permanent suspension of email sending capability for the affected sub-account.


4

## Warning Email: Risk of Suspension

A warning email is sent when ESP block activity rises above healthy levels. This gives you time to review your email setup, sending volume, and contact quality before sending is paused.

The warning email may include:

  * Your current Email Service Provider block rate
  * The recommended healthy threshold
  * Why mailbox providers may be blocking emails
  * Recommended next steps
  * A link to an ESP block resolution guide


![ESP block warning email example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071942251/original/HvPdA1uVgvjt9WfVCNWjN62HSVL1gVcYbQ.png?1779385099)

5

## 12-Hour Temporary Suspension

If excessive ESP blocks continue after the warning, email sending for the affected sub-account may be paused for 12 hours. Sending resumes automatically after the suspension window ends.

During the 12-hour suspension:

  * Email sending is temporarily disabled for the affected sub-account.
  * A suspension notification email is sent.
  * The account may show an in-app warning banner.
  * The banner may show when email services are expected to resume.


![12-hour suspension notification example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071942312/original/6Hfl8RwOgR9PzIpMqQehCYI284Q_zqD-cA.png?1779385153)

6

## In-App Suspension Banner

The in-app banner appears inside the platform when email sending is blocked due to a high number of spam blocks from email providers. This helps users quickly identify why sending is unavailable.

The banner may show:

  * That email sending is blocked
  * The reason sending is blocked
  * The expected resume time
  * A **Learn more** button


![In-app suspension banner example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071942631/original/5w0IqRkiUf3ESXFcZX4hzI_1O8NNj0WcDw.png?1779385483)

7

## 24-Hour Temporary Suspension

Repeated ESP block issues can indicate that the original sending problem was not fully resolved. A longer suspension gives the account more time to correct the cause before sending resumes.

If ESP block issues happen again after the first temporary suspension, email sending for the affected sub-account may be paused for 24 hours.

Use this time to:

  * Review email analytics
  * Confirm SPF, DKIM, and DMARC are configured correctly
  * Reduce send volume
  * Send only to engaged contacts
  * Clean inactive or low-quality contacts from your lists


8

## Future Enforcement: Permanent Suspension

Permanent enforcement is intended to protect sender reputation and platform-wide deliverability when repeated ESP block issues continue after temporary pauses. Agencies will be notified before permanent enforcement is implemented.

Important

In a future phase, if a sub-account experiences repeated suspension occurrences, email sending capability for that sub-account may be permanently suspended.

9

## How to Prevent ESP Block Enforcement

ESP block enforcement is automatic, so there is no setup required. The best way to avoid warnings or suspensions is to maintain healthy sending practices.

To reduce ESP blocks:

  * Confirm SPF, DKIM, and DMARC are configured correctly.
  * Send to engaged contacts first.
  * Avoid sudden increases in sending volume.
  * Remove invalid, inactive, bounced, or unengaged contacts.
  * Review email content for spam-like wording, broken links, or misleading subject lines.
  * Monitor email analytics and bounce classifications.
  * Reduce sending temporarily if ESP blocks increase.


10

## What to Do If Your Email Sending Is Paused

A temporary pause means mailbox providers are rejecting too many emails from the sub-account. Use the pause window to correct the issue before sending resumes.

Recommended actions:

  * Stop non-essential campaigns.
  * Review recent sends and identify any volume spikes.
  * Check email authentication records.
  * Review ESP block categories in Email Analytics.
  * Clean your contact list.
  * Prioritize your most engaged contacts.
  * Resume sending carefully after the pause ends.


11

## Frequently Asked Questions

Q: What is an ESP block?

An ESP block happens when a mailbox provider rejects an email due to deliverability, reputation, authentication, content, or engagement concerns.

Q: Is ESP block monitoring automatic?

Yes. ESP block monitoring is enabled automatically at the sub-account level.

Q: What happens after a warning email?

If ESP block activity continues, email sending may be temporarily paused.

Q: How long does the first suspension last?

The first temporary suspension lasts 12 hours.

Q: How long does a repeated suspension last?

Repeated ESP block issues may result in a 24-hour suspension.

Q: Does sending resume automatically?

Yes. Sending resumes automatically after the temporary suspension window ends.

Q: How can I reduce ESP blocks?

Review authentication, reduce send volume, clean your lists, improve email content, and send to engaged contacts.

Q: Can ESP block enforcement become permanent?

In a future phase, repeated suspension occurrences may lead to permanent email sending suspension for the affected sub-account.

Related Articles

[Email Service Provider Block Detected – Immediate Action Required to Restore Email Sending](<https://help.gohighlevel.com/en/support/solutions/articles/155000007341>) [Email Authentication Errors – Fix SPF, DKIM, and DMARC Issues](<https://help.gohighlevel.com/en/support/solutions/articles/155000006793>) [Email Authentication – DMARC](<https://help.gohighlevel.com/en/support/solutions/articles/48001224630>)

# LC Email: Email Service Provider Block Detected - Immediate Action Required to Restore Email Sending

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007341-lc-email-email-service-provider-block-detected-immediate-action-required-to-restore-email-sending](https://help.gohighlevel.com/support/solutions/articles/155000007341-lc-email-email-service-provider-block-detected-immediate-action-required-to-restore-email-sending)  
**Category:** Email  
**Folder:** LC Email

---

Email Deliverability

New ESP Block Policy

Understand how ESP block rates, warnings, and temporary suspensions work — and what you need to do before the policy takes effect.

Implementation Timeline

**Effective Date: 12th Feb 2026.** This new ESP Block Policy will be implemented on 12th Feb 2026. Current users will receive advance notification and have time to review their email practices before enforcement begins.

**What you should do now:** review your current bounce classification data, implement recommended email authentication and best practices, clean your email lists and improve content quality, and monitor your ESP block rates closely.

Table of Contents

1

What Are ESP Blocks?

2

ESP Block System

3

What You'll See When Blocked

4

How to Request Permanent Unblock

5

Why This Matters

6

Next Steps

7

Support Resources

8

Time-Sensitive Actions

9

Important Reminders

10

ESP Block Lock — AUP Update (Aug 13th 2026)

11

Frequently Asked Questions

1

## What Are ESP Blocks?

ESP blocks occur when major email providers (Gmail, Yahoo, Outlook, etc.) reject your emails due to:

  * Authentication failures (DMARC, SPF, DKIM issues)
  * Poor sender reputation
  * Content that appears spam-like
  * Policy violations
  * Technical configuration problems


Why This Matters

Unlike regular bounces, ESP blocks are calculated separately and trigger immediate restrictions to protect your long-term email deliverability.

2

## ESP Block System

The block system escalates through three temporary blocks, with warning emails sent before each one. Here is the full progression:

ESP Block Rate| Action| Duration| Block Level  
---|---|---|---  
3%| Warning Email Sent| Immediate notification| Pre-Block Warning  
5%| Email sending suspended| 12 hours| 1st Block  
3% (after 1st block)| Critical Warning Email Sent| Immediate notification| Pre-2nd Block Warning  
5% (after 1st block)| Email sending suspended| 24 hours| 2nd Block  
3% (after 2nd block)| Final Warning Email Sent| Immediate notification| Pre-3rd Block Final Warning  
5% (after 2nd block)| PERMANENT SUSPENSION| Permanent| 3rd Block — FINAL  
  
Critical

All blocks are reset after 7 consecutive days of maintaining ESP block rates below 1%.

Good to Know

In this release, email sending will not be permanently disabled. Each block will be temporary and limited to a 24-hour duration only.

3

## What You'll See When Blocked

If your email service is **blocked** due to **ESP Block Detected** , you will see the following error message displayed as a **top banner** inside the affected subaccount:

Email sending is blocked due to a high number of spam blocks from email providers.

![ESP block error banner displayed inside the subaccount](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064792608/original/5TW75eQ0t8kTt0vQOwFX3kr_-mcIEgdcDQ.png?1770907247)

This block is enforced to protect email deliverability and prevent further reputation damage with Email Service Providers (ESPs).

4

## How to Request Permanent Unblock

Permanent unblocking **cannot be done automatically**. Reach out to your agency owner in order to unblock the same.

Note

Agency owners review each request manually before lifting a permanent suspension to ensure the underlying deliverability issues have been addressed.

5

## Why This Matters

Protecting Your Business

  * ESP blocks damage your sender reputation permanently
  * Poor reputation leads to emails landing in spam folders
  * Reduced deliverability impacts your business revenue
  * Recovery can take weeks or months without proper action


Industry Standards

  * Major ESPs are increasingly strict about email quality
  * Authentication requirements are now mandatory
  * Content filtering has become more sophisticated
  * Sender reputation affects all future campaigns


6

## Next Steps

Step 1 — Analyze

Use the Bounce Classification to understand your specific ESP blocks.

Step 2 — Fix

Address the identified issues using our detailed support guides.

Step 3 — Monitor

Track your improvements through the analytics dashboard.

Step 4 — Verify

Ensure fixes are working before resuming normal sending.

7

## Support Resources

Bounce Classification

  * Access detailed ESP block analysis
  * View error categories and volumes
  * Get specific recommendations for your account
  * Monitor improvement progress


**Category-Specific Support Guides.** Each ESP block category in your analytics dashboard links to detailed fix guides:

**DMARC Authentication Failures**

**Domain / IP Reputation Issues**

**Content and Spam Filtering**

**Technical Configuration Problems**

**And more...**

8

## Time-Sensitive Actions

Before Policy Implementation

  * Complete email authentication setup
  * Clean all email lists thoroughly
  * Optimize email content and templates
  * Test email delivery across major providers
  * Monitor analytics dashboard daily


Within 24 Hours of Warning

  * Review analytics data immediately
  * Identify top 3 ESP block categories
  * Begin implementing critical fixes (authentication, major content issues)


Within 48 Hours of Block

  * Complete all technical fixes
  * Clean email lists and remove problematic content
  * Test email delivery to major providers


Ongoing

  * Monitor analytics dashboard daily
  * Maintain email best practices
  * Regular list hygiene and engagement monitoring


9

## Important Reminders

  * **ESP blocks are separate from regular bounces** — they require immediate attention.
  * **Each provider has different requirements** — use analytics to see provider-specific issues.
  * **Prevention is better than cure** — implement proper email practices from the start.
  * **Time is critical** — delays in fixing issues can lead to permanent restrictions.
  * **You have 30 days to prepare** — use this time wisely to optimize your email practices.


Take Action Now

Your email deliverability and business success depend on taking action now. Start with the Email Analytics dashboard and begin preparing for the new policy implementation.

10

## ESP Block Lock — AUP Update

Separate from the ESP Block Policy above, the underlying **ESP Block Lock** mechanism — the automated system that temporarily locks a sender out for damaging shared IP reputation — is also being updated. These changes tighten the confidence bar required before a lock can fire, so occasional volume spikes stop being mistaken for bad sending behavior.

Effective Date

**13th Aug 2026.** This update applies to the ESP Block Lock evaluation logic only and is independent of the 12th Feb 2026 ESP Block Policy timeline described above.

Change 1

Tiered minimum send floor: 50 → 500

**Before:** The system would evaluate ESP block rate after just 15 sends — extremely low confidence.

**After:** The minimum send count before a lock can fire is now tiered based on the ESP block rate, matching the same logic already applied to bounce.

Change 2

Minimum ESP block count: 15 → 25

**Before:** Just 15 ESP block events could contribute to a lock.

**After:** At least 25 ESP blocks must occur before the system considers locking — eliminating locks triggered by a single small send spike.

Parameter| Before| After  
---|---|---  
Minimum send floor| Flat 50 sends| Tiered up to 500 sends, based on ESP block rate  
Minimum ESP block count| 15 blocks| 25 blocks  
  
The Problem This Fixes

3 in 10 ESP block locks were triggered by bulk campaign send spikes — not bad senders. A legitimate sender blasting a large list at once could hit the threshold purely from volume, get locked, and re-trigger within the hour after unlocking.

The Result

The system now requires a larger confirmed sample before locking. Repeat offenders who genuinely damage the shared IP remain blocked. Campaign senders who spiked once are no longer caught.

11

## Frequently Asked Questions

Q: When does this new policy take effect?

The ESP Block System will be implemented on **12th Feb 2026** , giving all users 30 days to prepare and optimize their email practices.

Q: What happens to my current ESP blocks?

Your ESP block history will reset on the implementation date. However, we strongly recommend addressing any current issues before the policy goes live to ensure smooth operations.

Q: How do blocks reset?

Blocks reset after **7 consecutive days** of maintaining ESP block rates below 1%. However, if you receive 3 blocks within any 7-day period, permanent suspension will occur.

Q: Can permanent suspensions be reversed?

Permanent unblocking **cannot be done automatically**. Reach out to your agency owner in order to unblock the same.

Q: Will I receive notifications before each block?

Yes — you will receive warning emails when your ESP block rate reaches 3%, giving you time to take corrective action before the 5% threshold triggers a block.

Q: What if I'm currently above 3% ESP block rate?

Use the preparation period before 12th Feb 2026 to address these issues. The block system will not be enforced until the implementation date, giving you time to fix problems.

Q: How is this different from regular bounce management?

ESP blocks are calculated separately from regular bounces and have their own block system. Regular bounces (invalid addresses, full mailboxes) are handled differently than ESP blocks (reputation, authentication, policy issues).

Q: Is the ESP Block Lock the same thing as the ESP Block Policy?

No. The ESP Block Policy (effective 12th Feb 2026) governs the warning-and-suspension escalation described in sections 2–3 above. The ESP Block Lock is the underlying detection logic that decides how much confirmed evidence is needed before any lock fires, and it is being updated separately on **13th Aug 2026**.

Q: Will a single large campaign send still lock my account after 13th Aug 2026?

It's much less likely. With the minimum send floor tiered up to 500 and the minimum ESP block count raised to 25, a one-time volume spike from a legitimate campaign is far less likely to satisfy both thresholds on its own. Accounts with a genuine, sustained pattern of ESP blocks will still be locked.

We're Here to Help

This policy is designed to protect your sender reputation and ensure long-term email deliverability success. We're here to help you prepare and succeed with these new requirements.

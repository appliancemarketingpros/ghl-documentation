# LC Email: Email Service Provider Block Notification - Email Sending Temporarily Restricted (Action Required)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007065-lc-email-email-service-provider-block-notification-email-sending-temporarily-restricted-action-re](https://help.gohighlevel.com/support/solutions/articles/155000007065-lc-email-email-service-provider-block-notification-email-sending-temporarily-restricted-action-re)  
**Category:** Email  
**Folder:** LC Email

---

Email Deliverability

New ESP Block Policy — Action Required

A full walkthrough of the new ESP Block System, the steps to take right now, and how to keep your sub-account out of permanent suspension.

Implementation Timeline

**Effective Date: 12th Feb 2026.** This new ESP Block Policy will be implemented on 12th Feb 2026. Current users will receive advance notification and have time to review their email practices before enforcement begins.

**What you should do now:** review your current bounce classification data, implement recommended email authentication and best practices, clean your email lists and improve content quality, and monitor your ESP block rates closely.

Urgent — Action Required Within 24-48 Hours

**Your sub-account has been temporarily restricted from sending emails due to ESP (Email Service Provider) blocks.** This is part of our Anti-Spam Policy designed to protect your sender reputation and ensure high deliverability rates.

Table of Contents

1

What Are ESP Blocks?

2

New ESP Block System

3

Immediate Steps Required

4

Prepare for the New Policy

5

Why This Matters

6

Next Steps

7

Support Resources

8

Time-Sensitive Actions

9

Need Help?

10

Important Reminders

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

## New ESP Block System

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

If your email service is **blocked** due to **ESP Block Detected** , you will see the following error message displayed as a **top banner** inside the affected subaccount:

Email sending is blocked due to a high number of spam blocks from email providers.

![ESP block error banner displayed inside the subaccount](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064792608/original/5TW75eQ0t8kTt0vQOwFX3kr_-mcIEgdcDQ.png?1770907247)

This block is enforced to protect email deliverability and prevent further reputation damage with Email Service Providers (ESPs).

Related Reading

Refer to [_ESP Block Detected — Immediate Action Required to Restore Email Sending_](<https://help.gohighlevel.com/support/solutions/articles/155000007341-lc-email-email-service-provider-block-detected-immediate-action-required-to-restore-email-sending>) for the recovery walkthrough.

Setup Guide

Take Action Now

Three immediate steps, then a three-phase preparation plan.

3

## Immediate Steps Required

Step 1

Access the Bounce Classification feature

  1. Log into your sub-account.
  2. Navigate to **Sub-account Settings → Email Services → Bounce Classification**.
  3. Review your ESP block categories and error details.
  4. Identify the highest volume ESP blocks affecting your sub-account.


Step 2

Identify your primary issues

The Bounce Classification feature will show you:

  * **Specific ESP block categories** (DMARC failures, reputation issues, etc.)
  * **Error volumes** by provider (Gmail, Yahoo, Outlook)
  * **Detailed error messages** with exact reasons for blocks
  * **Recommended actions** for each block type


Step 3

Implement fixes

Based on your bounce classification results, you'll need to address:

  * Email authentication setup (SPF, DKIM, DMARC)
  * Content and template improvements
  * List hygiene and engagement issues
  * Technical configuration problems


4

## Prepare for the New Policy

Phase 1

Audit your current performance

Check Bounce Classification Dashboard

  * Navigate to Sub-account Settings → Email Services → Bounce Classification
  * Identify current ESP block rates and categories
  * Review recent email campaign performance
  * Document problem areas that need attention


Analyze Historical Data

  * Review bounce rates over the past 30 days
  * Identify patterns in ESP blocks
  * Check which email providers are blocking you most


Phase 2

Implement email best practices

Email Authentication Setup

  * Configure SPF records to include the platform's sending IPs
  * Set up DKIM signing for your domain
  * Implement DMARC policy (start with p=none for monitoring)
  * Verify all DNS records are properly configured


List Hygiene and Quality

  * Remove all bounced and invalid email addresses
  * Implement double opt-in for new subscribers
  * Segment lists based on engagement levels
  * Remove inactive subscribers (6+ months no engagement)


Content Optimization

  * Avoid spam trigger words and excessive promotional language
  * Maintain proper text-to-image ratio (60:40)
  * Include clear unsubscribe links
  * Use professional, branded email templates
  * Test content with spam checking tools


Phase 3

Monitor and test

Pre-Implementation Testing

  * Send test emails to major providers (Gmail, Yahoo, Outlook)
  * Monitor delivery rates and engagement metrics
  * Use email testing tools to check spam scores
  * Verify email authentication is working correctly


Ongoing Monitoring

  * Check bounce classification dashboard daily
  * Monitor ESP block rates closely
  * Track engagement metrics (opens, clicks, unsubscribes)
  * Set up alerts for unusual bounce patterns


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

Use the Bounce Classification feature to understand your specific ESP blocks.

Step 2 — Fix

Address the identified issues using our detailed support articles.

Step 3 — Monitor

Track your improvements through the bounce classification dashboard.

Step 4 — Verify

Ensure fixes are working before resuming normal sending.

7

## Support Resources

Bounce Classification Feature

  * Access detailed ESP block analysis
  * View error categories and volumes
  * Get specific recommendations for your sub-account
  * Monitor improvement progress


**Category-Specific Support Articles.** Each ESP block category in your bounce classification links to detailed fix guides:

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
  * Monitor bounce classification dashboard daily


Within 24 Hours of Warning

  * Review bounce classification data immediately
  * Identify top 3 ESP block categories
  * Begin implementing critical fixes (authentication, major content issues)


Within 48 Hours of Block

  * Complete all technical fixes
  * Clean email lists and remove problematic content
  * Test email delivery to major providers


Ongoing

  * Monitor bounce classification dashboard daily
  * Maintain email best practices
  * Regular list hygiene and engagement monitoring


9

## Need Help?

Self-Service Options

  * Use the Bounce Classification feature for detailed analysis
  * Follow category-specific support articles for step-by-step fixes
  * Access our email best practices documentation


Contact Support

If you need assistance interpreting your bounce classification data or implementing fixes, contact our support team with:

  * Your sub-account details
  * Screenshots from the Bounce Classification feature
  * Specific error messages you're seeing


10

## Important Reminders

  * **ESP blocks are separate from regular bounces** — they require immediate attention.
  * **Each provider has different requirements** — use bounce classification to see provider-specific issues.
  * **Prevention is better than cure** — implement proper email practices from the start.
  * **Time is critical** — delays in fixing issues can lead to permanent restrictions.
  * **You have 30 days to prepare** — use this time wisely to optimize your email practices.


Take Action Now

Your email deliverability and business success depend on taking action now. Start with the Bounce Classification feature and begin preparing for the new policy implementation.

11

## Frequently Asked Questions

Q: When does this new policy take effect?

The ESP Block System will be implemented on **12 Feb 2026** , giving all users 30 days to prepare and optimize their email practices.

Q: What happens to my current ESP blocks?

Your ESP block history will reset on the implementation date. However, we strongly recommend addressing any current issues before the policy goes live to ensure smooth operations.

Q: How do blocks reset?

Blocks reset after **7 consecutive days** of maintaining ESP block rates below 1%. However, if you receive 3 blocks within any 7-day period, permanent suspension will occur.

Q: Can permanent suspensions be reversed?

Permanent unblocking **cannot be done automatically**. A manual review by the Support team is required, and unblocking is not guaranteed — it depends on compliance with email best practices. This is why we provide multiple warnings and temporary suspensions before taking final action.

Q: Will I receive notifications before each block?

Yes — you will receive warning emails when your ESP block rate reaches 3%, giving you time to take corrective action before the 5% threshold triggers a block.

Q: What if I'm currently above 3% ESP block rate?

Use the preparation period before **12th Feb 2026** to address these issues. The block system will not be enforced until the implementation date, giving you time to fix problems.

Q: How is this different from regular bounce management?

ESP blocks are calculated separately from regular bounces and have their own block system. Regular bounces (invalid addresses, full mailboxes) are handled differently than ESP blocks (reputation, authentication, policy issues).

We're Here to Help

This policy is designed to protect your sender reputation and ensure long-term email deliverability success. We're here to help you prepare and succeed with these new requirements.

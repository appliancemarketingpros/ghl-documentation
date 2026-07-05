# Email Sending Guide:  Email Best Practices & Email Warm Up

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001021-email-sending-guide-email-best-practices-email-warm-up](https://help.gohighlevel.com/support/solutions/articles/155000001021-email-sending-guide-email-best-practices-email-warm-up)  
**Category:** Email  
**Folder:** LC Email

---

Email Deliverability

Email Best Practices & Warm-Up Guide

Everything you need to know to avoid the spam folder and land your emails in the inbox — from domain setup to warm-up schedules and troubleshooting.

Caution

Ignoring this guide can result in emails going to spam. Please read, learn, and apply these practices to your email sending before getting started.

Video Walkthrough

Table of Contents

1

Who Is This Guide For?

2

Email Best Practices

3

Email Warm-Up

4

Email Tools

5

Troubleshooting

6

Frequently Asked Questions

1

## Who Is This Guide For?

While this guide is for anyone sending emails through the platform, it is specifically designed for those using **LC Email** and **LC Email Dedicated Domain** features. Those using a Custom SMTP Provider that is not LC Email will need to consult their provider directly — support will be limited for email compliance and best practices not managed by the platform.

[Learn more about the difference between LC Email and Custom SMTP Providers here.](<https://help.gohighlevel.com/support/solutions/articles/155000001021-sending-your-first-emails-email-warm-up-best-practices#What-are-the-Differences-Between-LC-Email-and-a-Custom-SMTP-Provider?>)

Now that we know who this is for, let's hop into our guide together as we review Email Best Practices and Email Sending Recommendations below.

2

## Email Best Practices

Now that your new sending domain is set up, follow these essential practices to ensure emails land in the inbox — not the spam folder.

Best Practice 1

Set Up a Dedicated Email Sending Domain

**What is it?** Rather than sharing an IP or domain with all other users, a dedicated email domain is a single private domain you use to send and receive emails. With LC Email, you have the ability to create your own dedicated domain in-app. Custom SMTP users do not have this option.

**Why it matters:** Not having a dedicated email sending domain often results in emails going to spam despite good practices. A dedicated domain gives you full control over your reputation and email deliverability.

**How to set it up:** [Follow this step-by-step guide to set up your Dedicated Email Sending Domain.](<https://help.gohighlevel.com/en/support/solutions/articles/48001226115>)

**Already have a dedicated domain but emails still go to spam?** It is better to set up a new sub-domain than to try to repair a damaged one. See the FAQ section below for more details.

Best Practice 2

Set Up a Dedicated Sending IP Address

**What is it?** A dedicated IP address means your emails go out from a unique, exclusive IP — not shared with anyone else. Email service providers (ESPs) use IP reputation to judge deliverability, so exclusive ownership gives you full control.

**Why it matters:** With a shared LC Email dedicated domain, you still share the sending IP with all other platform users. A dedicated IP isolates your reputation — especially important when sending 200,000+ emails per week.

**How to set it up:** [See the Dedicated Sending IP Address guide here.](<https://help.gohighlevel.com/support/solutions/articles/155000001152-what-is-a-dedicated-ip-in-lc-email-#How-to-buy-a-Dedicated-IP?>)

![Dedicated IP address setup screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031452195/original/4WpKfwxRPKGnTZIl2P1zx5XU5J-t6SUJDA.jpg?1724267134)

**Cost:** $59 per month per IP, billed to the agency billing card on file. Agencies can configure rebilling to pass this cost to sub-accounts. [See pricing details here.](<https://help.gohighlevel.com/support/solutions/articles/155000001152-what-is-a-dedicated-ip-in-lc-email-#How-to-buy-a-Dedicated-IP?>)

**Additional resource:** [Reverse DNS (rDNS) Set Up — Fixing "Reverse DNS does not match SMTP Banner"](<https://help.gohighlevel.com/support/solutions/articles/155000001154>)

Best Practice 3

Enable Email Validation

**What is it?** Email Validation checks whether an email address is valid before you send to it. Sending to invalid addresses harms your domain reputation and deliverability.

**Why it matters:** Sending to invalid or non-existent addresses causes bounces, hurts your domain reputation, and can result in emails being rejected entirely or going to spam.

**How to enable it:**

  * **First-send validation:** Sub-Account View → Business Profile → scroll to "Verify Email Address when the first email is sent to a new contact" → enable the checkbox.
  * **Re-validation every 90 days:** Agency View → Sub-accounts → click on the sub-account name → scroll to "Enable Re-validation for 90 days."


[Learn how to enable and rebill LC Email Validation here.](<https://help.gohighlevel.com/en/support/solutions/articles/48001235221>)

**Cost:** $2.50 per 1,000 email validations — significantly cheaper than most major providers. [See rebilling options.](<https://help.gohighlevel.com/en/support/solutions/articles/48001235221>)

Best Practice 4

Add Your DMARC Record

**What is it?** A DMARC record provides instructions to receiving servers on how to handle incoming mail. Messages must pass DKIM and SPF alignment checks per your DMARC policy — those that fail can be rejected, reported, or sent to spam.

**Why add it?** Missing or misconfigured DMARC records negatively impact your domain reputation. Mailbox providers count it against you, resulting in emails landing in spam.

**How to add it:** Log into your DNS provider and add the following TXT record:

Field| Value  
---|---  
Type| TXT  
Name| _dmarc  
Content| v=DMARC1; p=reject  
  
Verify your DMARC record with the [DMARC Checker tool](<https://dmarcian.com/domain-checker/>). Additional resources:

  * [Email Authentication — DMARC](<https://help.gohighlevel.com/en/support/solutions/articles/48001224630>)
  * [Add Your DMARC Record (Google)](<https://support.google.com/a/answer/2466563>)
  * [DMARC Reports (Google)](<https://support.google.com/a/answer/10032472>)


Best Practice 5

Use the Proper "From Email"

**What is it?** The "From Email" is what recipients see when they receive your email. Your sending domain might be _mail.yourdomain.com_ , but your From Email can be _you@yourdomain.com_ or _you@mail.yourdomain.com_.

**Why it matters:** Using a From Email on a different organizational domain from your sending domain can result in poor deliverability and DMARC misalignment.

**Rules:** Use a From Email on the same organizational domain as your dedicated sending domain. If your sending domain is a subdomain (e.g., _mail.company.com_), you can use either _name@company.com_ or _name@mail.company.com_ — deliverability is the same when SPF, DKIM, and DMARC are set up correctly.

Sending Domain| Valid From Email| Status  
---|---|---  
replies.company.com| sender@company.com| ✓ Valid  
replies.company.com| sender@replies.company.com| ✓ Valid  
mail.company.com| user@otherbrand.com| ✗ Invalid  
  
[See more: Masking Sender Emails — From Name & Address](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>)

Best Practice 6

Add Unsubscribe Links

**What is it?** An unsubscribe link allows recipients to opt out of future emails from you.

**Why it matters:** Not including an unsubscribe link will severely harm your email deliverability rates — and can get you flagged as a spammer.

**How to set it up:** Use the "Footer" element in the email builder. You have two options:

  * [**Default Unsubscribe Link**](<https://help.gohighlevel.com/en/support/solutions/articles/48001225534>) — Quick and easy for LC Email users. Non-LC Email users should use the custom option instead.
  * [**Custom Unsubscribe Link**](<https://help.gohighlevel.com/en/support/solutions/articles/48001175857>) — Full control over the unsubscribe flow. Works for all email providers.


Best Practice 7

Use Double Opt-In

**What is it?** Double opt-in asks subscribers to confirm their intent twice — for example, filling out a form and then clicking a verification link in a confirmation email. Only after completing both steps will they receive further emails.

**Why it matters:** Double opt-ins significantly boost domain reputation and deliverability. Recipients who have confirmed twice are more likely to open, click, and engage — all positive signals for inbox providers.

**How to set it up:** [How To Build A Double Opt-In Flow](<https://help.gohighlevel.com/en/support/solutions/articles/48001162996>)

Best Practice 8

Stop Sending to Unengaged Contacts

**What is it?** Stop sending to contacts who take no action — no opens, no clicks — across multiple campaigns.

**Why it matters:** Sending to engaged recipients helps your emails land in the inbox. Low engagement signals (few opens or clicks) push emails toward spam.

**How to do it:** If someone hasn't taken action after weeks of emails, reduce your sending frequency or remove them from your list. Focus on recipients who are actively engaging.

**It is better to stop sending to an unengaged recipient than to have them unsubscribe or mark your email as spam.**

Best Practice 9

Send Regularly — But Not Too Regularly

**What is it?** Sending frequency is a major factor in domain reputation. Sending too infrequently (once a month) or too frequently (multiple times a day) can both harm your deliverability — especially if the frequency changes suddenly.

**Why it matters:** Inbox providers use engagement signals and sending consistency to assess your reputation. Erratic patterns — or sudden volume spikes — look suspicious.

**Recommended cadence:**

  * For newly opted-in contacts: send daily for a short initial window to drive conversion.
  * If no engagement after 1–2 weeks: slow down to weekly sends.
  * If no engagement after 2+ months of weekly sends: stop sending entirely.
  * For promotional blasts: keep them spaced out and concise. It is always better to undersend than to oversend.


**It is better to stop sending to an unengaged recipient than to have them unsubscribe or mark your email as spam.**

3

## Email Warm-Up

Mailbox providers will often send emails from new dedicated domains straight to spam — because anyone, including spammers, can register a new domain. Following the best practices above alongside the warm-up recommendations below will greatly improve your chances of landing in the inbox.

Email Sending Recommendations

Warm-Up Volume Schedule

Only send to opted-in contacts and stay within these daily and hourly limits at each stage.

![Email warm-up sending schedule showing stages and volume limits](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155008545111/original/G6ZM7opEZrQTEQDvqoTbQFYUdwYR_PrNFA.png?1695657495)

The schedule above shows how many emails you can send per hour and per day at each warm-up stage. Stage 1 allows up to 100 per hour and 1,000 per day. Stage 2 increases to 300 per hour and 2,500 per day. Remember: the stage is not just how long you have owned the domain — it reflects your current sending phase and the health of your domain at that moment.

[How to Send Emails in Drip Mode (Daily and Hourly Sending)](<https://help.gohighlevel.com/en/support/solutions/articles/48001167703>)

Pro Tips for Your First Warm-Up Emails

  * Follow all Email Best Practices above
  * Stay within the recommended sending volume per stage
  * Send fewer emails per day or hour than the maximum if you can
  * Only send to opted-in contacts with a high likelihood of engagement — cold emailing during warm-up tends to harm deliverability
  * Keep email content short and to the point; include an appropriate image where possible
  * Do not use public link shorteners (bit.ly, tiny.url, etc.) — these are a common spam signal


4

## Email Tools

Use these free tools to test, track, and monitor your email domain health.

Tool 1

Test the Spamminess of Your Emails

Email content itself can impact deliverability. Too much text, spam-trigger words, or URL shorteners can cause inbox providers to flag your message. Use [mail-tester.com](<https://www.mail-tester.com/>) to get a spam score before sending:

  1. Copy the test email address provided by Mail-Tester
  2. Create a new contact in the platform using that email address
  3. Send your email to that contact
  4. Return to Mail-Tester and click "Then check my score"
  5. Review the score and make adjustments based on the feedback


Tool 2

Review Your Email Health Report

Paste your sending domain into the [MX Toolbox Email Health Report](<https://mxtoolbox.com/emailhealth>) to quickly check for common issues — blacklisting, missing DMARC records, MX errors, and more. This is a great starting point for any deliverability troubleshooting.

Tool 3 — Advanced

Google Postmaster Tools

Using data from all Gmail users you send to, the [Google Postmaster Tool](<https://postmaster.google.com/>) monitors your ongoing email performance and provides detailed reporting on:

  * Spam rate
  * IP Reputation
  * Domain Reputation
  * Feedback Loop
  * Authentication
  * Encryption
  * Delivery errors


**Note:** It can take up to two days for Google to populate data in your reports. If data is missing, refresh the page, clear your cache, or use an incognito window to rule out caching issues.

5

## Troubleshooting

There are many reasons emails go to spam — URL shorteners, content issues, poor list health, and more. If emails are landing in spam, work through these steps in order:

Step 1

Check How Long You've Been Sending

A domain can take up to 4 weeks to warm up. If you are within that window, stay consistent with the Email Best Practices and Email Sending Recommendations above and use the Email Tools section to monitor progress.

Step 2

Check Your MX Records

Confirm your MX records are installed and resolving correctly. Use the [Email Health Report](<https://mxtoolbox.com/emailhealth>) from the Email Tools section above to verify.

Step 3

Ensure Your DMARC Record Is Set Up

Confirm your DMARC record is applied and valid. See the **Best Practice 4** section above for setup instructions and verification tools.

Step 4

Reach Out to Support

If you've confirmed the three steps above and are still experiencing issues, contact support for further assistance. [How to reach support.](<https://help.gohighlevel.com/en/support/solutions/articles/155000000969>)

6

## Frequently Asked Questions

Q: What about cold email outreach?

Cold emailing means contacting people who haven't opted in — and it's generally not recommended, especially for new domains. If you do use cold outreach, make sure to validate emails, enable bounce protection, and avoid using your primary sending domain. Use a separate sub-account and domain to protect your reputation.

**Cold email pro tips:**

  * Validate emails and filter out invalid addresses
  * Send small batches and drip slowly
  * Warm up your domain first
  * Never use your primary sending domain for cold outreach
  * Use purpose-built cold email tools to qualify leads before importing them


Third-party tools like instantly.ai or smartlead.ai can help manage cold outreach. Once leads engage, you can move them into the platform. (These tools are not affiliated with or endorsed by the platform.)

Q: What if I already have a dedicated sending domain but emails are still going to spam?

Some spam filtering early on is normal during warm-up. If your domain is already warmed up and emails are still going to spam, it is generally better to set up a new sub-domain than to attempt to repair the damaged one's reputation.

Q: What happens if my IP is blacklisted?

If your IP is blacklisted, reach out to support. [Click here for details on how to contact support.](<https://help.gohighlevel.com/en/support/solutions/articles/155000000969>)

Q: Should I share the same dedicated sending domain across multiple sub-accounts?

No. Do not share sending domains across sub-accounts. Each sub-account should have its own dedicated domain to maintain strong, isolated deliverability and avoid cross-account reputation issues.

Q: What is email warm-up?

Email warm-up is the process of gradually increasing your sending volume to build a good reputation with inbox providers. Starting slow and scaling up over time signals to mailbox providers that you are a legitimate sender — helping your emails avoid spam folders.

Q: What is email deliverability?

Email deliverability is your ability to land emails in the inbox rather than the spam folder. It is influenced by sender reputation, list health, content quality, authentication setup (SPF, DKIM, DMARC), and recipient engagement.

Q: What is domain reputation?

Domain reputation is how mailbox providers rate your domain's trustworthiness as a sender. A strong reputation gets your emails delivered to the inbox; a poor reputation means spam filters. Reputation is built through consistent, engaged sending over time.

Q: How long until a domain is fully warmed up?

Generally around 4 weeks. Stick to the best practices throughout the process and use the Email Tools to monitor your domain reputation and progress.

Q: What happens if I send more than the recommended volume?

Sending too much too soon can damage your domain reputation and may get your domain or IP blacklisted. Always follow the volume guidelines for your current warm-up stage to stay safe.

Q: What are the differences between LC Email and a Custom SMTP Provider?

LC Email is the built-in sending solution with native deliverability tools, validation, dedicated domain setup, and support assistance. With a Custom SMTP Provider, you are responsible for all setup and troubleshooting — support's ability to assist with compliance and deliverability issues is limited.

Q: What is a dedicated domain?

A dedicated domain gives you complete control over your email sending reputation by keeping your activity isolated from other senders. This separation improves inbox placement and lets you build a clean reputation from scratch.

Q: How do I send emails in drip mode (hourly and daily sending)?

Use Bulk Actions or Workflows to stagger your sends across time. This prevents volume spikes that can trigger spam filters and helps maintain consistent sending patterns that inbox providers trust. [How to Send Emails in Drip Mode.](<https://help.gohighlevel.com/en/support/solutions/articles/48001167703>)

Q: What is an email bounce?

A bounce occurs when your email cannot be delivered to the recipient's mailbox. There are two types:

  * **Hard Bounce** — The address is invalid or does not exist. Remove these contacts immediately.
  * **Soft Bounce** — A temporary issue such as a full inbox or server delay. The email may be retried automatically.


Related Articles

[LC Email — Overview & Setup](<https://help.gohighlevel.com/en/support/solutions/articles/48001220605>) [Dedicated Email Sending Domain — Step-by-Step Setup](<https://help.gohighlevel.com/en/support/solutions/articles/48001226115>) [What Is a Dedicated IP in LC Email?](<https://help.gohighlevel.com/support/solutions/articles/155000001152-what-is-a-dedicated-ip-in-lc-email->) [Email Authentication — DMARC](<https://help.gohighlevel.com/en/support/solutions/articles/48001224630>) [How to Enable and Rebill LC Email Validation](<https://help.gohighlevel.com/en/support/solutions/articles/48001235221>) [How to Send Emails in Drip Mode](<https://help.gohighlevel.com/en/support/solutions/articles/48001167703>)

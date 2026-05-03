# What Email Deliverability Stats Should I Look For?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001198786-what-email-deliverability-stats-should-i-look-for-](https://help.gohighlevel.com/support/solutions/articles/48001198786-what-email-deliverability-stats-should-i-look-for-)  
**Category:** Email  
**Folder:** Deliverability

---

Email Deliverability

# What Email Deliverability Stats Should I Look For?

"How do I know if my stats are good?" A definition-by-definition breakdown of the numbers that matter — with healthy, warning, and red-flag benchmarks for each.

A guest tutorial from Krystin Ruschman of [Email-2-Inbox](<https://www.facebook.com/groups/email2inboxhighlevelusers>).

Before We Start

Available stats vary between email marketing tools and SMTPs — for the sake of this article, all terminology is based on **Mailgun**. Average benchmarks pulled from multiple sources, and every situation is different. Average results are for average people doing average things — and who wants to be average?

Table of Contents

  1. 1 The 10 Stats & What They Mean
  2. 2 Delivered — The Foundation Stat
  3. 3 Opened — First Engagement Signal
  4. 4 Clicked — Action on Your CTA
  5. 5 Replied — The Deeper Response
  6. 6 Complained — The Reputation Killer
  7. 7 Bounced — Your List Hygiene Score
  8. 8 Summary & Benchmark Cheat Sheet
  9. 9 Need Some Help?
  10. 10 Frequently Asked Questions


## The 10 Stats & What They Mean

The most common email stats you'll encounter, defined in Mailgun terminology. Know what each one actually measures before you judge whether it's "good."

Processed

Total message requests received by Mailgun — both outgoing and incoming, including posts via Routes like webhooks.

Accepted

Total outgoing message requests received by Mailgun (email you tried to send).

Delivered

Total requested messages that actually got Delivered to the recipient's mail server (and presumably onto one of their account folders — no guarantee).

Opened

Total times a Delivered message triggered an Open (this does not necessarily mean a person literally opened the email…).

Clicked

Total times a Delivered message triggered a Click.

Replied

Total times a Delivered message triggered a Reply from the recipient.

Bounced (Hard)

Accepted messages that couldn't be Delivered due to bad addresses or inactive accounts. Often called "Hard Bounced" or "Permanent Failure" — though a Permanent Failure doesn't always count as a Hard Bounce.

Complained

Delivered messages that get marked as spam or junk by the recipient.

Unsubscribed

Delivered messages that trigger an Unsubscribe response by the recipient.

Suppressions

Accepted messages that were not Delivered because the address had previously Bounced, Complained, or Unsubscribed.

1

## Delivered

Healthy

At or above 98%

Warning

Around 97–98%

Red Flag

Under 97%

Where to Look

Monitor Delivered rate at the **domain level** as well as the **individual email level**.

Considerations

  * The opposite of Delivered is **Undelivered** — failed, bounced, or rejected. None of those are what we want.
  * Delivered just means it made it to the recipient's mail server — not the inbox. Delivered under 97% usually means a majority of what's delivered is landing in spam/promotions.
  * A low Delivered rate is usually indicative of **multiple** problems (reputation, authentication, list quality) — not just one.
  * 97–98% can still indicate problems, especially in conjunction with other red flags.


2

## Opened

Healthy

40–60%+

Average

16–26%

Red Flag

Under 15%

Where to Look

Monitor Open rate at the **individual email level**.

Considerations

  * Control everything a recipient sees _before_ they open — From Name, From email, domain/brand recognition, Subject Line, and the preview (first line or two of body copy).
  * The decision to open is partly about comfort. Show up in a way that feels familiar and trustworthy.
  * Note: Apple iOS 15+ Mail Privacy Protection auto-triggers Opens for many Apple Mail users — not a real person opening the email. Industry averages have recalibrated higher since this shipped, so interpret Open rate with a grain of salt.


**Heads up on iOS 15+:** Apple Mail fires Opens automatically whether the recipient reads the email or not. If Apple Mail makes up a big chunk of your list, combine Open rate with Clicks and Replies — don't evaluate it alone.

3

## Clicked

Healthy

Above 10%

Average

7–9%

Red Flag

Under 5%

Where to Look

Monitor Click rate at the **individual email level** , specifically where a "click" CTA is the focus.

Considerations

  * The psychology of a Click is very different from what encourages a Reply — don't conflate them.
  * Make your Click CTA clear and easy to act on. No guessing.
  * For short messages (3–5 lines), put a single clear CTA at the end.
  * For longer copy, place the same CTA in multiple spots throughout the email.
  * Tell recipients exactly what they'll get when they click — answer "what's in it for them?"
  * Avoid muddying the CTA with multiple competing clickable things. Keep the ONE Click you care about as the main focus.


4

## Replied

Healthy

30%+

Average

15–25%

Red Flag

Under 10%

Where to Look

Monitor Reply rate at the **individual email level** , specifically where a "reply" CTA is the focus.

Considerations

  * The psychology of a Reply is very different from what encourages a Click.
  * Make your Reply CTA clear and easy to act on.
  * For a boost, ask simple low-friction questions (yes/no) or sweeten the pot with something valuable in exchange for a reply — "what's in it for them?"
  * Avoid muddying the Reply CTA with links to click on. Keep Reply as the main focus.


5

## Complained

Healthy

As close to 0.00% as possible

AUP Threshold

0.05% (Mailgun)

Red Flag

At or above 0.04%

Mailgun's AUP ceiling of **0.05%** is roughly **1 complaint per 2,000 emails**. If you're approaching that line, your domain is already in trouble.

Where to Look

Monitor Complaint rate at the **domain level** and the **individual email level**.

Considerations

  * Following best practices should keep complaints well under 0.03%.
  * Once it approaches 0.04%, it may start affecting your domain/IP reputation.
  * High complaint rates can lead your SMTP to disable your domain and/or account — and can land you on a blacklist.
  * Give recipients an easy way to opt out (Unsubscribe or Update Preferences). Unsubscribes don't hurt reputation — they're massively preferable to a Complaint, which does.


6

## Bounced

Healthy

Well under 1%

AUP Threshold

5% (Mailgun)

Red Flag

Over 2–2.5%

Where to Look

Monitor Bounce rate at the **domain level** and the **individual email level**.

Considerations

  * Following best practices for list hygiene (initial and ongoing) should keep this well under 1%.
  * Once it approaches 2–2.5%, your domain/IP reputation starts taking damage.
  * High bounce rates can lead your SMTP to disable your domain and/or account — and can land you on a blacklist.


## Summary & Benchmark Cheat Sheet

These numbers are guidelines — not rules. The individual email or campaign, the message, the audience, and the level of segmentation all weigh into the numbers. Monitor your stats **weekly** so you can course-correct along the way.

Stat

Healthy

Watch

Red Flag

Delivered

≥ 98%

97–98%

< 97%

Opened

40–60%+

16–26%

< 15%

Clicked

> 10%

7–9%

< 5%

Replied

30%+

15–25%

< 10%

Complained

≈ 0.00%

< 0.04%

≥ 0.04%

Bounced

< 1%

1–2%

> 2–2.5%

The Real Goal

Look at your current numbers, set goals, then make **one small tweak at a time** and measure the effect. The goal isn't to hit a specific number — it's to **improve from where you started** , and ultimately improve your bottom line.

## Need Some Help?

Every Situation is Unique

This article gives a general idea of what stats to monitor and what to look for — but every situation is different.

Benchmarks Vary by Campaign

Numbers to shoot for depend on the type of campaign, the audience, and the offer/CTA you're focusing on. Not every email will perform the same.

Troubleshooting is Context-Heavy

Deliverability issues can't be meaningfully solved over a Facebook post or helpdesk ticket — they require analysis of multiple factors together.

Want a Deeper Look?

If you're struggling to get email to the inbox — or want to level up your email marketing — book a one-on-one with Krystin.

Book a Call with Krystin

Personal deliverability analysis and marketing strategy at Email-2-Inbox.

[Schedule at Email2Inbox](<https://help.email-2-inbox.com/calendar-chat>)

## Frequently Asked Questions

What's the single most important stat to watch?

**Complaint rate** , closely followed by bounce rate. Both directly and quickly damage your sender reputation, and both can trigger account-level action from your SMTP. Opens and clicks fluctuate; complaints and bounces compound.

Why does my Open rate keep jumping around since iOS 15?

Apple Mail Privacy Protection pre-fetches images — which triggers Open events automatically whether or not the recipient actually read anything. If a big chunk of your audience uses Apple Mail, your Open rate is inflated. Pair Open rate with Click and Reply rates, or focus on trend direction rather than absolute numbers.

Is a low Delivered rate always a reputation problem?

Not always — sometimes it's list quality (bad addresses, role accounts, spam traps) or authentication (missing/misconfigured SPF, DKIM, DMARC). But a chronically low Delivered rate is almost always a combination of multiple issues, and should trigger a full audit.

What's the difference between Accepted and Delivered?

**Accepted** means Mailgun received your request to send the email. **Delivered** means the recipient's mail server accepted it. The gap between Accepted and Delivered is bounces, rejections, and suppressions.

Unsubscribe or Complaint — which is worse?

**Complaints are worse — by a lot.** Unsubscribes don't damage reputation; they just remove an uninterested contact. Complaints signal to ISPs that your mail is unwanted, and they carry disproportionate reputation weight. Always give people an easy unsubscribe so they don't reach for the spam button instead.

How often should I monitor these stats?

**Weekly at minimum.** That's frequent enough to catch issues before they damage reputation, but not so often that normal variance looks like a crisis. Track trends, not single data points.

My campaign blew past the "Red Flag" thresholds — what now?

Pause additional sends to that list, scrub bounces and complaints aggressively, review what the campaign content and audience had in common, and check authentication records. If complaint or bounce rate is near the AUP ceiling, throttle volume and rebuild to your most engaged segment before ramping back up.

References

  * [SendGrid — Improve Email Deliverability with Email Validation API](<https://sendgrid.com/blog/improve-email-deliverability-with-sendgrids-newly-released-email-validation-api/>)
  * [Constant Contact — Average Industry Rates](<https://knowledgebase.constantcontact.com/articles/knowledgebase/5409-average-industry-rates>)
  * [Mailgun — Email Bounce Rates: Shifting Focus Away from Failure](<https://www.mailgun.com/blog/email-bounce-rates-shifting-focus-away-failure/>)
  * [HubSpot — Average Email Open Rate Benchmark](<https://blog.hubspot.com/sales/average-email-open-rate-benchmark>)
  * [Neil Patel — High Email Unsubscribe Rate](<https://neilpatel.com/blog/high-email-unsubscribe-rate/>)
  * [Mailgun — Email Open Rates Decoded](<https://www.mailgun.com/blog/email-open-rates-decoded>)
  * [Campaign Monitor — What is a Good Email Response Rate?](<https://www.campaignmonitor.com/resources/knowledge-base/what-is-a-good-or-average-email-response-rate-for-email-marketing/>)
  * [SendGrid — Unsubscribes: What to Do When You're Getting Too Many](<https://sendgrid.com/blog/unsubscribes-what-to-do-when-youre-getting-too-many/>)


## Related Articles

What is Email Deliverability? Email Deliverability Overview Why Are My Emails Going to Spam? Dedicated Sending Domain Setup Bot Detection for Email Stats

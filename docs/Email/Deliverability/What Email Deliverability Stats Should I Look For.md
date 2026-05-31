# What Email Deliverability Stats Should I Look For?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001198786-what-email-deliverability-stats-should-i-look-for-](https://help.gohighlevel.com/support/solutions/articles/48001198786-what-email-deliverability-stats-should-i-look-for-)  
**Category:** Email  
**Folder:** Deliverability

---

Email Deliverability

What Email Deliverability Stats Should I Look For?

"How do I know if my stats are good?" A definition-by-definition breakdown of the numbers that matter — with healthy, warning, and red-flag benchmarks for each.

Before We Start

Available stats vary between email marketing tools and sending providers. Average benchmarks pulled from multiple sources, and every situation is different. Average results are for average people doing average things — and who wants to be average?

Table of Contents

1

The 11 Stats & What They Mean

2

Delivered — The Foundation Stat

3

Opened — First Engagement Signal

4

Clicked — Action on Your CTA

5

Replied — The Deeper Response

6

Complained — The Reputation Killer

7

Bounced (Hard) — Your List Hygiene Score

8

Bounce (Soft) — Delivery in Progress

9

Summary & Benchmark Cheat Sheet

10

Need Some Help?

11

Frequently Asked Questions

1

## The 11 Stats & What They Mean

The most common email stats you'll encounter. Know what each one actually measures before you judge whether it's "good."

Processed

Total message requests received by the sending server — both outgoing and incoming, including posts via Routes like webhooks.

Accepted

Total outgoing message requests accepted for sending (email you tried to send).

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

Bounce (Soft)

A temporary delivery failure — retries happen automatically. While retrying, the email appears in **Sent** status and the email detail view shows **Delivery in Progress**. Once retries are exhausted the status resolves to **Delivered** or **Failed**.

Complained

Delivered messages that get marked as spam or junk by the recipient.

Unsubscribed

Delivered messages that trigger an Unsubscribe response by the recipient.

Suppressions

Accepted messages that were not Delivered because the address had previously Bounced, Complained, or Unsubscribed.

2

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


3

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


Heads up on iOS 15+

Apple Mail fires Opens automatically whether the recipient reads the email or not. If Apple Mail makes up a big chunk of your list, combine Open rate with Clicks and Replies — don't evaluate it alone.

4

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


5

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


6

## Complained

Healthy

As close to 0.00% as possible

AUP Threshold

0.05%

Red Flag

At or above 0.04%

The AUP ceiling of **0.05%** is roughly **1 complaint per 2,000 emails**. If you're approaching that line, your domain is already in trouble.

Where to Look

Monitor Complaint rate at the **domain level** and the **individual email level**.

Considerations

  * Following best practices should keep complaints well under 0.03%.
  * Once it approaches 0.04%, it may start affecting your domain/IP reputation.
  * High complaint rates can lead your SMTP to disable your domain and/or account — and can land you on a blacklist.
  * Give recipients an easy way to opt out (Unsubscribe or Update Preferences). Unsubscribes don't hurt reputation — they're massively preferable to a Complaint, which does.


7

## Bounced (Hard)

Healthy

Well under 1%

AUP Threshold

5%

Red Flag

Over 2–2.5%

Where to Look

Monitor Bounce rate at the **domain level** and the **individual email level**.

Considerations

  * Following best practices for list hygiene (initial and ongoing) should keep this well under 1%.
  * Once it approaches 2–2.5%, your domain/IP reputation starts taking damage.
  * High bounce rates can lead your SMTP to disable your domain and/or account — and can land you on a blacklist.


8

## Bounce (Soft)

Healthy

Under 2%

Watch

2–5%

Red Flag

Over 5%

How Soft Bounce Status Works

While Retrying

The email appears in **Sent** status and the detail view shows **Delivery in Progress** — retries are still in progress.

After Retries Exhausted

Status updates to either **Delivered** (success) or **Failed** (permanent failure after retry window).

Where to Look

Monitor Soft Bounce rate at the **domain level** and the **individual email level**. Check the email details view for "Delivery in Progress" status on in-progress retries.

Considerations

  * Unlike Hard Bounces (permanent), soft bounces are **temporary** — the receiving server rejected delivery for now but may accept it later. Common causes: recipient mailbox full, server temporarily unavailable, or message size too large.
  * Retries happen automatically within the retry window. You don't need to manually resend during this phase.
  * If you see an address soft-bouncing repeatedly across multiple campaigns, treat it like a hard bounce — remove it from your active list. Persistent soft bounces signal an abandoned or unreachable mailbox.
  * A spike in soft bounces across a send can also signal a sending volume or reputation issue — the receiving server may be throttling your domain. Monitor alongside Complaint and Delivered rates.


Don't Confuse "Delivery in Progress" with a Problem

Seeing "Delivery in Progress" in the email detail view doesn't mean something is wrong — it simply means the system is still within its retry window. Wait for the status to resolve to Delivered or Failed before drawing conclusions.

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

Bounced (Hard)

< 1%

1–2%

> 2–2.5%

Bounce (Soft)

< 2%

2–5%

> 5%

The Real Goal

Look at your current numbers, set goals, then make **one small tweak at a time** and measure the effect. The goal isn't to hit a specific number — it's to **improve from where you started** , and ultimately improve your bottom line.

## Need Some Help?

Every Situation is Unique

This article gives a general idea of what stats to monitor and what to look for — but every situation is different.

Benchmarks Vary by Campaign

Numbers to shoot for depend on the type of campaign, the audience, and the offer/CTA you're focusing on. Not every email will perform the same.

Troubleshooting is Context-Heavy

Deliverability issues can't be meaningfully solved over a Facebook post or helpdesk ticket — they require analysis of multiple factors together.

## Frequently Asked Questions

Q: What's the single most important stat to watch?

**Complaint rate** , closely followed by bounce rate. Both directly and quickly damage your sender reputation, and both can trigger account-level action from your SMTP. Opens and clicks fluctuate; complaints and bounces compound.

Q: What does "Delivery in Progress" mean in the email detail view?

It means the email hit a **soft bounce** and the system is actively retrying delivery. This is not a failure state — it's an in-progress state. The email will appear in **Sent** status during this time. Do not resend manually. Wait for the status to resolve: if delivery succeeds, the status changes to **Delivered** ; if all retry attempts are exhausted without success, it changes to **Failed**.

Q: What's the difference between a Hard Bounce and a Soft Bounce?

A **Hard Bounce** is a permanent failure — the address is bad, doesn't exist, or the account has been closed. No retry will be attempted. A **Soft Bounce** is a temporary failure — the server was unavailable, the mailbox was full, or the message was temporarily rejected. Retries happen automatically within the retry window, and the email shows in **Sent** status with a **Delivery in Progress** detail during that time. If the same address soft-bounces repeatedly across campaigns, treat it as a hard bounce and remove it from your list.

Q: Why does my Open rate keep jumping around since iOS 15?

Apple Mail Privacy Protection pre-fetches images — which triggers Open events automatically whether or not the recipient actually read anything. If a big chunk of your audience uses Apple Mail, your Open rate is inflated. Pair Open rate with Click and Reply rates, or focus on trend direction rather than absolute numbers.

Q: Is a low Delivered rate always a reputation problem?

Not always — sometimes it's list quality (bad addresses, role accounts, spam traps) or authentication (missing/misconfigured SPF, DKIM, DMARC). But a chronically low Delivered rate is almost always a combination of multiple issues, and should trigger a full audit.

Q: What's the difference between Accepted and Delivered?

**Accepted** means the system received your request to send the email. **Delivered** means the recipient's mail server accepted it. The gap between Accepted and Delivered is bounces, rejections, and suppressions.

Q: Unsubscribe or Complaint — which is worse?

**Complaints are worse — by a lot.** Unsubscribes don't damage reputation; they just remove an uninterested contact. Complaints signal to ISPs that your mail is unwanted, and they carry disproportionate reputation weight. Always give people an easy unsubscribe so they don't reach for the spam button instead.

Q: How often should I monitor these stats?

**Weekly at minimum.** That's frequent enough to catch issues before they damage reputation, but not so often that normal variance looks like a crisis. Track trends, not single data points.

Q: My campaign blew past the "Red Flag" thresholds — what now?

Pause additional sends to that list, scrub bounces and complaints aggressively, review what the campaign content and audience had in common, and check authentication records. If complaint or bounce rate is near the AUP ceiling, throttle volume and rebuild to your most engaged segment before ramping back up.

References

  * [SendGrid — Improve Email Deliverability with Email Validation API](<https://sendgrid.com/blog/improve-email-deliverability-with-sendgrids-newly-released-email-validation-api/>)
  * [Constant Contact — Average Industry Rates](<https://knowledgebase.constantcontact.com/articles/knowledgebase/5409-average-industry-rates>)
  * [Email Bounce Rates: Shifting Focus Away from Failure](<https://www.mailgun.com/blog/email-bounce-rates-shifting-focus-away-failure/>)
  * [HubSpot — Average Email Open Rate Benchmark](<https://blog.hubspot.com/sales/average-email-open-rate-benchmark>)
  * [Neil Patel — High Email Unsubscribe Rate](<https://neilpatel.com/blog/high-email-unsubscribe-rate/>)
  * [Email Open Rates Decoded](<https://www.mailgun.com/blog/email-open-rates-decoded>)
  * [Campaign Monitor — What is a Good Email Response Rate?](<https://www.campaignmonitor.com/resources/knowledge-base/what-is-a-good-or-average-email-response-rate-for-email-marketing/>)
  * [SendGrid — Unsubscribes: What to Do When You're Getting Too Many](<https://sendgrid.com/blog/unsubscribes-what-to-do-when-youre-getting-too-many/>)


Related Articles

What is Email Deliverability? Email Deliverability Overview Why Are My Emails Going to Spam? Dedicated Sending Domain Setup Bot Detection for Email Stats

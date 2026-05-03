# What is Email Deliverability? - A Guest-Tutorial From Krystin Ruschman of Email-2-Inbox

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001198783-what-is-email-deliverability-a-guest-tutorial-from-krystin-ruschman-of-email-2-inbox](https://help.gohighlevel.com/support/solutions/articles/48001198783-what-is-email-deliverability-a-guest-tutorial-from-krystin-ruschman-of-email-2-inbox)  
**Category:** Email  
**Folder:** Deliverability

---

Email Deliverability

# What is Email Deliverability?

Delivered vs. Deliverability — what's the difference, why does it matter, and what actually controls whether your email lands in the inbox?

A guest tutorial from Krystin Ruschman of [Email-2-Inbox](<https://help.email-2-inbox.com/calendar-chat>).

"I think my deliverability is ok…"

What does that actually mean? Where do you even see Deliverability? Let's start by making sure we're on the same page about two terms that get mixed up all the time — **Delivered** and **Deliverability**. They are very different.

Table of Contents

  1. 1 Delivered — What It Really Means
  2. 2 Deliverability — The Stat You Can't See
  3. 3 Factors That Influence Deliverability
  4. 4 Control What You Can Control
  5. 5 Need Some Help?
  6. 6 Frequently Asked Questions


## Delivered — What It Really Means

This is the stat you can see — in your SMTP dashboard (Mailgun, for example) and inside the HighLevel email stats view alongside opens, clicks, bounces, complaints, and replies.

![Mailgun and HighLevel dashboard delivery stats](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48146642843/original/VznCObDVAa4l0JXlCvXrzP8OgNT_RhQwlg.png?1633527869)

**"Delivered" just means the email got to the recipient's mail server** — somewhere. Could be the inbox, spam, promotions, updates… honestly, who knows where it actually landed? It's also possible for the mail server to accept the message and then never hand it off to the mailbox, though that's less common — most mail servers would rather reject outright and give the sender clear feedback.

You know… like when the postal carrier marks your package "delivered" in their system but it's nowhere to be found on your doorstep, and you end up asking every neighbor if it got dropped at their place by mistake? Yeah. Like that.

A Good Delivery Rate is 98%+

The opposite of Delivered is Undelivered — meaning it didn't make it to the recipient server at all. It failed, bounced, or got rejected. None of those are what we want.

Why HighLevel + Mailgun is Special

Most email marketing tools hide Delivered as a stat — because they'd have to answer for it. They'll show you how many people entered a campaign and then jump straight to Open Rate. HighLevel with Mailgun gives you full visibility into every stat and direct communication with your own SMTP provider, which means the power is entirely in your hands.

## Deliverability — The Stat You Can't See

Unlike Delivery, **Deliverability is a stat you don't actually see anywhere.**

Deliverability = Inbox Placement

In other words — your Inboxing Rate. How much of your mail hits the Inbox versus Spam, Junk, Promotions, Updates, or nowhere at all.

![Deliverability visualization](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48146643430/original/w38n9VFNm3fPyE8mbVChqjQW8GyMYuPOFA.png?1633527939)

Email Service Providers (Gmail, Yahoo, Outlook, etc.) don't provide inbox-placement data in their feedback loops, so there's no dashboard that tells you "42% of your email landed in spam." You only know it was delivered — not where.

There's no such thing as a perfect 100% inbox rate every time, but understanding the factors that drive deliverability lets you get as close to 100% as possible.

## Factors That Influence Deliverability

There are literally hundreds of inputs that affect inbox placement. Here are the big ones that move the needle most.

1

### IP & Domain Reputation

**Reputation is KEY.** Many, many things feed into it, but two categories carry the most weight: **Volume & Consistency** and the almighty **Engagement** (opens, clicks, replies, bounces, complaints, unsubscribes). For more on stats, see _"What Email Deliverability Stats Should I Look For?"_.

2

### ESP Filtering Preferences

Google, Yahoo, Outlook, Apple — they don't all filter the same way. There are hundreds of signals each provider evaluates, and none of them publish a whitepaper explaining their filtering logic. What works for Gmail may not work for Outlook.

3

### Authentication

Those pesky DNS records — the **SPFs, DKIMs, and DMARCs** of the world. And don't forget your MX records; if those aren't configured correctly you could land in spam or prevent delivery entirely.

4

### Domain Age

Root domain or subdomain, age factors into warm-up. Treat your new domain like a first date — the goal is a second date. A new domain has no history and no reputation, so start slow and don't rush things. A strong reputation can overcome young age.

5

### Domain Suffix (TLD)

Some TLDs come with a bad reputation from day one. The most trusted suffixes are **.com, .co, .net, .org** (plus .edu and .gov for those who qualify). Others can send you straight to spam. Check how your domain suffix rates [on Spamhaus](<https://www.spamhaus.org/statistics/tlds/>).

6

### Subject Line & Body Copy

What you say matters. I once took the word **FREE** out of a single subject line and deliverability improved by 7%. Avoid spammy triggers like "click here", "opportunity", "free", "100%", and heavy punctuation (!!!).

7

### Blacklistings

The dreaded "Black Spot." Different blacklists, different consequences — some cause huge problems, others are temporary. Check whether your domain or IP is listed on [MXToolbox Blacklists](<https://mxtoolbox.com/blacklists.aspx>).

8

### Link Types, Length, Count & Reputation

Even a simple signature tool can hurt deliverability. A single blacklisted or bad-reputation link makes your whole email "guilty by association." Only include links you trust or control.

9

### Text-to-HTML Ratio

There's a time and place for fancy templates. The general rule is **60:40, leaning text-heavy**. Audience know/like/trust and past engagement can let you get away with more HTML — and sometimes heavier HTML wins on conversions even with lower deliverability. Test.

10

### Volume & Consistency

How much you send, how fast, and how often — all of these shape reputation. Think about what a spammer does: huge volume, all at once, pushing mail out rather than nurturing relationships. Don't be a spammer. (See also: Domain Age.)

11

### Recipient Email Behavior

Believe it or not, how your recipient interacts with their own email account factors into where your message is routed. Factoring recipient behavior into your strategy puts you ahead of most marketers.

…

### And Many Others

Image-to-text ratio, attachment types, time of send, engagement recency, complaint rate trends, spam-trap exposure, unsubscribe behavior — the list keeps going. Look for more detailed articles on these individual factors coming soon.

## Control What You Can Control

We don't have control over every factor that plays into deliverability, but the play is to isolate the things we _can_ influence — even a little bit — and then commit to controlling them entirely.

The Short Version

Proper setup and authentication get you **to** the inbox. Consistent behavior — good list hygiene, relevant content, steady volume, real engagement — keeps you **in** the inbox.

## Need Some Help?

It's a Wide Topic

This article covers a handful of factors, but there are hundreds of things that play into deliverability and every situation is unique.

Setup Gets You In

Proper setup and configuration is what gets you _to_ the inbox — behavioral choices are what keep you there.

Troubleshooting is Hard

It's almost impossible to troubleshoot deliverability over a Facebook post or helpdesk ticket. Real analysis requires context.

Want a One-on-One Look?

If you're struggling to get emails to the inbox — or just want to level up your email marketing — book a call with Krystin at Email-2-Inbox.

[Book a Call with Krystin](<https://help.email-2-inbox.com/calendar-chat>)

## Frequently Asked Questions

What's the difference between Delivered and Deliverability?

Delivered means the message reached the recipient's mail server (somewhere — inbox, spam, promotions, you name it). Deliverability means inbox placement specifically — what percentage of your mail actually lands in the primary inbox versus other folders.

Where can I see my Deliverability rate?

You can't — not directly. ESPs don't report inbox placement. What you can monitor is delivery rate, open rate, spam complaint rate, and postmaster tools data (Google Postmaster, Microsoft SNDS), which together give you a strong proxy for inbox placement.

What counts as a "good" delivery rate?

**98% or higher.** Anything below that signals list hygiene problems, authentication issues, or reputation damage worth investigating.

Why should I use HighLevel with Mailgun instead of a tool that hides these stats?

Because you get full visibility. Most email marketing platforms obscure delivered, bounce, and complaint stats so you can't hold them accountable. HighLevel + Mailgun gives you every stat and lets you communicate directly with the SMTP provider — which means you own the outcome.

What's the single biggest lever I can pull to improve deliverability?

**Engagement.** Send to people who open, click, and reply — stop sending to people who don't. Clean lists and relevant content lift everything else: reputation, inbox placement, conversion rate. It's that direct.

Can I recover from a damaged sender reputation?

Yes, but it takes time. Pause your worst-performing sends, aggressively prune unengaged contacts, focus on your most engaged segment, and gradually rebuild volume. Authentication (SPF, DKIM, DMARC) must be perfect while you recover.

## Related Articles

Email Deliverability Overview Why Are My Emails Going to Spam? Dedicated Sending Domain Setup Bot Detection for Email Stats Filtering Contacts by Email Statistics

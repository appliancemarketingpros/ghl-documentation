# LC - Phone Messaging Quality Monitoring

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008745-lc-phone-messaging-quality-monitoring](https://help.gohighlevel.com/support/solutions/articles/155000008745-lc-phone-messaging-quality-monitoring)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Compliance

LC - phone messaging quality monitoring

How opt-out and delivery error monitoring protects your SMS reputation, and what happens when thresholds are exceeded.

The short version

LC - Phone tracks two things for every sub-account: how many people reply **STOP** , and how many of your messages carriers **block as spam**. If either climbs too high, you get a warning email. If it keeps climbing, bulk and automated SMS is paused for a short period while you fix the cause.

Replying to leads one-to-one in Conversations is **never** paused.

Please Note

This article covers **quality monitoring** , opt-out rates and carrier filter errors (Error 30007). For consent requirements, opt-out language, sender ID, spam handling, and daily sending limits, see the [LC - Phone Messaging Policy](<https://help.gohighlevel.com/support/solutions/articles/48001213941-lc-phone-messaging-policy>).

Table of Contents

1

Why We Monitor Messaging Quality

2

What We Measure

3

What Triggers a Warning or a Restriction

4

What Happens: First, Second, and Repeated Times

5

What Still Works During a Restriction

6

How to Get Sending Restored

7

How to Prevent Restrictions

8

Where to Check Your Restriction History

9

Emails You'll Receive

10

Frequently Asked Questions

1

## Why we monitor messaging quality

Mobile carriers , not the platform , decide whether your text messages get delivered. When too many people reply STOP to your messages, or too many of your messages get flagged as spam, carriers respond by throttling or permanently blocking your phone numbers.

Carrier blocks are hard to reverse, and they don't stay contained. Sustained poor sending erodes the reputation of the numbers your agency and your clients rely on.

What This Does For You

Monitoring gives you early notice while the problem is still fixable, briefly pauses high-risk bulk sending so the damage stops spreading, and helps you get back to healthy delivery rates, before carriers make the decision for you.

2

## What we measure

Two metrics, tracked separately for each sub-account:

Metric| What It Measures  
---|---  
Opt-out rate| The percentage of contacts who reply with a standard opt-out keyword (e.g., STOP) after receiving your SMS  
Error 30007 rate| The percentage of messages carriers flagged as filtered or blocked (Error 30007, “Message filtered”)  
  
How They're Calculated

Both rates are measured over a **rolling 7-day window** , and only once a sub-account has sent at least **500 SMS** in that window. Below 500 messages, no warnings or restrictions are triggered.

Not Counted

**RCS messages** are excluded from these calculations and from restriction enforcement entirely.

3

## What triggers a warning or a restriction

Thresholds depend on how long the sub-account has been sending SMS. Newer senders have no track record with carriers, so they are held to tighter limits.

  * **New** : fewer than 7 days of SMS sending history
  * **Established** : 7 or more days of SMS sending history


Sub-Account| Warning at| Restriction at  
---|---|---  
New — opt-out rate| ≥ 3%| ≥ 10%  
New — Error 30007 rate| ≥ 10%| ≥ 50%  
Established — opt-out rate| ≥ 4%| ≥ 6%  
Established — Error 30007 rate| ≥ 15%| ≥ 25%  
  
Good to Know

Either metric alone can trigger a warning or a restriction, they are evaluated independently. Your sub-account moves from New to Established automatically as it builds sending history; there is nothing to configure.

4

## What happens: first, second, and repeated times

Restrictions escalate. The first one is short and you can end it yourself; repeated problems get longer and eventually require a person to review the account.

Stage| Impact on Sending| How It Ends  
---|---|---  
Warning| **None.** Everything keeps sending. You get an email.| Clears on its own once your rates come back down  
First restriction| Bulk, workflow, and campaign SMS paused| **12 hours** , or sooner if you lift it yourself  
Next restriction| Bulk, workflow, and campaign SMS paused| **24 hours** , or sooner if you lift it yourself  
Repeated problems| Bulk, workflow, and campaign SMS paused| **Support review only** — no automatic expiry, no self-lift  
  
![Messaging restriction banner shown in the sub-account](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080936843/original/Eso05R7kiUGeUAe0wvdVAJFkmTtfEHrXCQ.png?1789460558)

After a Restriction Lifts

Your rates are watched more closely for a few days (72hours). If they stay healthy, nothing further happens. If they climb again in that period, the next restriction applies right away, which is why it's worth fixing the cause before resuming bulk sends.

New Sub-Accounts

A sub-account with fewer than 7 days of sending history does **not** recover automatically after its first restriction. You'll need to request a Support review before bulk and automated sending is restored.

5

## What still works during a restriction

A restriction stops outbound bulk sending. It does not cut off your ability to talk to leads who are already reaching out.

Keeps Working

  * One-to-one messages in Conversations, reply to every inbound lead as normal
  * Missed Call Text Back (if configured)
  * RCS messaging


Paused

  * Bulk Actions from the Contacts area
  * Workflow “Send SMS” actions
  * Campaigns


6

## How to get sending restored

Before anything else, fix what caused the restriction, pause the workflows or campaigns that drove the rate up, and clean the list they were sending to. Restoring sending without fixing the cause usually leads straight to the next restriction.

Option 1

Wait for it to expire

A 12-hour or 24-hour restriction lifts on its own and sending resumes automatically, no action needed, unless a Support review is open.

Option 2

Lift it yourself

An **agency owner or agency admin** can end a 12-hour or 24-hour restriction early from the sub-account's phone settings. Regular users don't have this control, and each use is recorded in the audit log.

![Self-lift restriction control in phone settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080937105/original/UMdoxvatpHXRk27PectIiMen0k8PMnCQ4w.png?1789460707)

![Self-lift confirmation dialog](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080937130/original/vkDobHEIKgedv4X84E-f6Gyuak2I5DNClw.png?1789460740)

Before You Lift It

  * Lifting restores sending but **does not reset your rates,** if the same messages keep going out, the next restriction follows quickly.
  * You can only do this once every **24 hours**.
  * It's unavailable while a Support/Manual review is open.
  * An audit log entry is created each time self-lift is used.
  * Regular users do not have access to the self-lift control.


![Audit log entry created when a restriction is lifted early](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080937499/original/VK_1Ds1vkkiUr3uTqYv6Mrkglpk-Rr7CAQ.png?1789460879)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080981759/original/QdL9MYZDtV3WXGimJ1xHTkhFEpXtiALiGw.png?1789479861)

Option 3

Request a Manual review

Required when a New sub-account doesn't recover after its first restriction, or when problems repeat on an Established sub-account. A review is also triggered automatically at very high rates, opt-out at or above **12%** , or Error 30007 at or above **45%**.

Go to **Sub-account → Settings → Phone Numbers** and submit the **Messaging Quality Review** form. This creates the Support request for you. Only one open review is allowed per sub-account at a time.

![Messaging quality review request form](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080938197/original/No4gC0Z5LiuPIy_67blv8rPjS_jWomJ-WQ.png?1789461183)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080981722/original/q-ii5Dybyn3S0bi1Db-mhcrlF6WHVKOzug.png?1789479847)

Important

Submitting a review request does not guarantee immediate restoration. Support evaluates your messaging practices, contact consent, and recent sending history first, and only Support can clear a review restriction. Bulk sending stays paused until they do.

7

## How to prevent restrictions

Nearly every restriction traces back to messaging people who didn't clearly ask to hear from you. These habits keep both rates low:

**Send only with consent** : message contacts who actively opted in, not purchased or scraped lists.

**Say who you are** : identify the business by name in the first message.

**Include opt-out language** : and honor every opt-out request immediately.

**Clean your lists** : remove invalid numbers, landlines, and prior opt-outs before a bulk send.

**Watch your message content** : heavy promotional language in cold outreach is exactly what carrier filters look for.

**Don't over-message** : repetitive outreach drives opt-outs faster than anything else.

**Act on the warning email** : pause the campaign that caused it before scaling back up.

The Payoff

A warning is your free chance to fix things, accounts that act on the first email rarely see a restriction at all. Healthy rates keep your numbers trusted by carriers, which means more of your messages reach real people.

8

## Where to check your restriction history

The **Restriction History** tab shows every restriction the sub-account has had — when it happened, why, and how it ended.

Where To Find It

**Sub-account → Settings → Phone System → Messaging → Restriction History**

Each entry shows:

  * Date and time of the event
  * Restriction type — temporary or Support review
  * The reason, and the rate or count that triggered it
  * How it ended, including whether it was lifted early
  * Date filters, so you can check a specific period


![Restriction History tab showing restriction and lift events](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080938407/original/hmFKqMqFhQNhmpwlbYlpBXPD0hEu_UiHWA.png?1789461257)

9

## Emails you'll receive

There are three emails, and they all go to the same people: the **agency account owner** and the **administrators of the affected sub-account**.

Email| What It Means  
---|---  
Messaging quality alert| A rate crossed a warning threshold. Nothing is paused — this is your chance to fix it.  
SMS temporarily paused| A restriction has been applied. Bulk and automated sending is paused.  
Support review required| The sub-account needs a Support review, or a review outcome needs your attention.  
  
Tip

Make sure the agency owner email on file is actively monitored. These emails are the earliest signal you'll get that a client's campaign is heading toward a restriction.

10

## Frequently asked questions

Q: Can I still reply to my leads during a restriction?

Yes. **One-to-one messages in Conversations always keep working** , along with Missed Call Text Back and RCS. Only Bulk Actions, Workflow SMS, and Campaigns are paused.

Q: Does a restriction on one sub-account affect my other sub-accounts?

No. Rates are measured and restrictions are applied per sub-account. That said, poor sending anywhere still erodes carrier trust in your numbers over time — which is exactly what this monitoring exists to prevent.

Q: How long does a restriction last?

The first one lasts **12 hours**. The next one lasts **24 hours**. Both can be ended early by an agency owner or admin. A Support review restriction has no set duration — it lasts until Support clears it.

Q: Do I need to send a minimum number of messages before this applies?

Yes. A sub-account must have sent at least **500 SMS** in the rolling 7-day window before any warning or restriction can trigger. Below that volume, rates aren't evaluated at all.

Q: Why is a brand-new sub-account held to tighter limits?

New numbers have no sending history with carriers, so carriers scrutinize them more heavily and block them faster. Tighter thresholds in the first 7 days catch problems before a new number gets permanently blocked.

Q: Who can lift a restriction early?

Only an **agency owner or agency admin**. Regular users don't see the control. Each lift is recorded in the audit log, and it can only be used once every 24 hours.

Q: If I lift the restriction, am I in the clear?

Not automatically. Lifting restores sending but **does not reset your rates**. If the same campaign resumes unchanged, the rate stays high and another restriction follows — a longer one. Fix the cause first.

Q: What rates do I need to get back to?

A **warning** clears when your opt-out rate is below **4%** and Error 30007 below **15%**. A **restriction** clears when opt-out is below **10%** and Error 30007 below **40%**. Aim well under these — they're the ceiling, not a healthy target.

Q: Are RCS messages affected?

No. **RCS is excluded** from the rate calculations and from restriction enforcement, and it keeps sending during a restriction.

Q: How do I request a Support review?

Submit the Messaging Quality Review form from **Sub-account → Settings → Phone Numbers**. It creates the ticket for you. Only one open review is allowed per sub-account, and only Support can clear it.

Q: Does this replace the LC - Phone Messaging Policy?

No. Quality monitoring works alongside the [LC - Phone Messaging Policy](<https://help.gohighlevel.com/support/solutions/articles/48001213941-lc-phone-messaging-policy>), which covers consent, opt-out language, sender ID, spam handling, DND, and daily sending limits. Both apply to every sub-account using LC - Phone.

Q: I just got a warning email. What should I do right now?

  1. Pause the workflows, campaigns, and bulk actions going to contacts without clear opt-in consent.
  2. Check that opt-out language and sender identification are in your messages.
  3. Review the contact list for invalid numbers, landlines, and prior opt-outs.
  4. Talk to your client before resuming any bulk outreach.


Thank You

We appreciate your partnership in maintaining healthy SMS deliverability for your agency and your clients.

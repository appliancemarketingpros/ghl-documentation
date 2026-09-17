# LC Email Sending Limits, Ramp-Up, and Trial Agency Rules

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007790-lc-email-sending-limits-ramp-up-and-trial-agency-rules](https://help.gohighlevel.com/support/solutions/articles/155000007790-lc-email-sending-limits-ramp-up-and-trial-agency-rules)  
**Category:** Email  
**Folder:** LC Email

---

Email · What's New

LC Email — Sub-account Rampup: Smart Sending Graduation & Shared Domain Reputation Protection

Sub-accounts on a shared sending domain now see exactly where they stand — daily limit, today's usage, current stage, and a complete history of every stage change — directly on the Email Services page.

Availability

Available for new agencies created on or after **27 April 2026** on GHL Shared or Agency Shared domains. Existing agencies are unaffected.

What's covered

1

The new Sending Limit panel

2

Stage and status badge

3

Contextual alerts and recommendations

4

Stage History timeline

5

Dedicated Domain nudge

6

For agencies: the Update Limit control is now automatic

7

Trial agency view: a flat 100/day cap

8

Quick FAQ

Watch the Walkthrough

Until now, sub-accounts on a shared domain had a daily sending limit but no real visibility into it — no usage counter, no context for why the limit was set the way it was, and no way to see how it would change over time. That has changed. The Email Services page now shows live limit data, the current sending stage, plain-language alerts when something needs attention, and a timeline of every stage change.

This article is a tour of what's new on the screen.

Sub-account user

Sections explain what end users will see and what the new states mean for day-to-day sending.

Agency admin

Sections explain what's changed in agency Advanced Settings and the support portal.

1

## The New Sending Limit Panel

Sub-account user

On any sub-account using a GHL Shared or Agency Shared domain, the Email Services page now shows a dedicated **Sending Limit** panel at the top. It surfaces three numbers side by side, with no extra clicks required.

  * **Daily Limit** — the maximum emails this sub-account can send today, based on its current stage.
  * **Sent Today** — a live counter of campaign and bulk emails sent so far.
  * **Remaining** — the difference between the two, updated in real time.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232730/original/dQIC_Gu-gXFNOiU68eSWtq7awVBgazdj_w.png?1777474036)

Healthy state: Sending Limit panel with live usage, current stage, and "Sending is healthy" status.

When the daily ceiling is hit, the panel switches to a red **Daily limit reached** state with a clear "Resets at midnight UTC" note, and the top of the page surfaces a blocking banner so it cannot be missed.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232829/original/wEZJ9yIs0dsSpeiZtKQDndYZDeZZaZPe1w.png?1777474082)

Daily limit reached: the page now blocks campaign sends and tells users exactly when the limit resets.

Note for users

1-to-1 emails, payment confirmations, calendar invites, and system notifications are _not_ counted against the daily limit and continue to deliver normally even when the limit is reached.

2

## Stage and Status Badge

Sub-account user

Every shared-domain sub-account is on a stage from 1 (starting) to 8 (maximum). The panel shows the current stage as a badge alongside the daily limit, so users always know which tier they're on. A small **"Why do we use stages?"** tooltip next to the badge explains, in plain language, how the system protects shared-domain reputation.

The eight stages and their daily limits are:

Stage| Daily limit  
---|---  
1 — Starting| 1,000  
2| 2,500  
3| 5,000  
4| 6,500  
5| 8,000  
6| 10,000  
7| 14,000  
8 | 15,000  
9 - Maximum| 25,000  
  
  


  
**Note:******New Stage 9 at 25,000/day (shared domain and agency owned)****  
**Before:** The shared domain ramp topped out at 15,000/day with no next step. Senders who outgrew this had only one option — upgrade to a dedicated domain.  
  
**After:** A new Stage 9 at 25,000/day gives high-volume senders room to grow before needing a dedicated domain.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070232961/original/T39g3ZbuHAWwM6yww-Wu2zdZjF8mzAYJ5Q.png?1777474179)

New account view: "Warming up" state at Stage 1 with an explanation of how the stage will grow.

Brand-new sub-accounts open at Stage 1 with the Warming up status. As sending performance stays healthy, the badge automatically rolls forward through the stages 

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233081/original/nJueVp5InZt-b46JpQr0qRaXKoSdUispLQ.png?1777474247)

Stage 8 — Maximum: 15,000/day with a CTA to create a dedicated domain for unlimited sending.

3

## Contextual Alerts and Recommendations

Sub-account user

The page now adapts to the sub-account's actual sending health. Instead of one generic screen, it renders a different banner and recommendation block for each state. Every alert is paired with concrete, step-by-step actions the user can take to recover.

State A

Bounce downgrade

A red **High bounce rate detected** banner appears when the sub-account's hard bounce rate goes above the threshold. The recommendations differ depending on whether email validation is already enabled, so the guidance is always relevant.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233166/original/JBPqeeRgEJXOp1LURrvI2GkSw-hNfpUkVA.png?1777474306)

With email validation enabled.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233209/original/83bxI4d-NAPcYGVk0lgO4Pg2bZ7bBGKL4A.png?1777474337)

Without email validation enabled.

State B

Delivery downgrade

A "Delivery rate dropped below 95%" banner appears with recommendations to pause campaigns to unengaged contacts and tighten audience targeting.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233224/original/ajp166pgsla1RXsuaLZMbchSOyUmStBjbg.png?1777474365)

Delivery rate has slipped: actionable steps to pause low-engagement campaigns and reduce volume.

State C

Spam complaint downgrade

When spam complaints exceed the threshold, recommendations focus on opt-in quality, list hygiene, and unsubscribe visibility.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233267/original/Accv3nX7ApVu4QoQD9kLOkhB7E9yY1JF5A.png?1777474403)

Spam complaints crossed the threshold: guidance focuses on opt-in quality, list hygiene, and unsubscribe visibility.

State D — Stage 1 Flagged

If a sub-account at Stage 1 also has critical health issues, the page elevates to an **Account flagged** state. The warning explains exactly which contacts to suppress and reassures the user that transactional and 1-to-1 emails will continue to deliver.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233306/original/NVc84aWw-yDWswQJWegLod3rU_Suk5Bzlg.png?1777474436)

Stage 1 flagged: targeted recovery steps plus a reminder that transactional emails are unaffected.

State E — Suspended

Usage tiles read "unavailable" and the page makes it clear sending is fully halted pending review.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233383/original/LLoS_7VqTi_rK0IQGeCNfSSWKCyrLSdjUg.png?1777474469)

Suspended: usage tiles read "unavailable" and the page makes it clear sending is fully halted pending review.

What changed under the hood

AUP enforcement emails now use clearer, state-specific subject lines so it's immediately obvious whether an account is on a first-strike 12-hour block, a second-strike 24-hour block, or a permanent lock awaiting manual review.

4

## Stage History Timeline

Sub-account user

Agency admin

The Email Services page now includes an expandable **Stage History** section that lists every upgrade and downgrade with the date and the reason. This is the first time both end users and agencies have an in-product audit trail of how a sub-account's sending capacity has evolved.

  * **Upgrade entries** are tagged "Stage improved" and include the new daily limit.
  * **Downgrade entries** are tagged "Stage declined" and surface the trigger — bounce spike, sustained delivery issue, or spam spike.
  * Brand-new accounts see a friendly empty state until enough sending activity is recorded.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233488/original/MkjYtyuzZQ30uDiD0Bj0pWGvksw7-I89-w.png?1777474545)

Stage History: each transition shown chronologically with the reason and the resulting limit.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233565/original/zhN_mf7YprnYluns5VEK0HEet9tsksFeRg.png?1777474608)

Empty state: shown for new accounts that haven't yet been evaluated.

5

## Dedicated Domain Nudge

Sub-account user

A persistent, dismissible banner now sits on the Email Services page for every shared-domain sub-account, encouraging an upgrade to a dedicated domain for higher throughput and a sender reputation tied to the user's own domain. The banner automatically disappears once the account reaches Stage 8 — at which point a similar nudge appears in the Maximum Stage card instead.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233860/original/ubP5pj8eE3PMhB_Bx74u4b3s4W3OFJHW-A.png?1777474789)

Shared-domain banner: "You're using a shared domain" with an "Add a dedicated domain" CTA.

6

## For agencies: The Update Limit control is now automatic

Agency admin

For new agencies (created on or after 27 April 2026), the manual **Update Limit** control on the agency Advanced Settings screen has been replaced with an informational banner that reads _"Limits are automatic now"_ and links directly through to the sub-account's Email Services page.

  * The Update Limit panel and footer button are hidden entirely from Agency Advanced Settings.
  * Existing agencies are completely unaffected and keep the manual control.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070233979/original/RcCzwHysXl5qcxalYoD4DvpPQt3BhpyJtA.png?1777474870)

Why this changed

Shared-domain reputation is shared across every sub-account on it. Manual overrides on a single account could pull the reputation down for everyone else. Stage-based progression replaces overrides with an automatic, transparent path to higher limits — earned through clean sending behavior.

7

## Trial Agency View: A flat 500/day cap

Agency admin

Sub-account user

  


  


  


  


Trial agency sub-accounts can send email campaigns, subject to the applicable 500 emails/day trial limit.  
  
Sub-accounts under a trial agency don't enter the rampup system at all. They run on a dedicated trial view with a 500 emails/day cap, no Update Limit control, and a streamlined panel that shows only the domain card and the trial limit.  
  
Trial agency sub-accounts can send email campaigns, subject to the applicable 500 emails/day trial limit.  
  
The moment the parent agency converts to a paid plan, the trial UI is replaced with the full Sending Limit panel and Stage History, and the rampup engine activates automatically from Stage 1.

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070234256/original/8BXH4eAo8ziGMG-VdVE3azepOcJ9NyOuwg.png?1777475007)  
  
  
**Note:******Trial sub-account cap: 100 → 500/day****  
  
**Before:** Every sub-account under a trial agency was silently capped at 100 emails/day — an emergency measure set in April to stop a spam attack. The actual fix (location creation cap) was already live, but the 100/day cap stayed on. Sub-accounts had no idea why they were hitting limits.  
  
**After:** Trial sub-accounts can now send up to 500/day. 99% of legitimate trial users never exceed this naturally.  
  


8

## Quick FAQ

Q: Will my existing sub-accounts change?

No. All agencies created before 27 April 2026 are completely unaffected same limits, same controls, same UI. A migration plan for existing agencies will be communicated separately by end of Q2 2026.

Q: Where do I see my current stage?

Open **Email Services** from the sub-account's left navigation. The Sending Limit panel shows the current stage badge alongside Daily Limit, Sent Today, and Remaining. Expand **Stage History** on the same page for the full timeline.

Q: Can I request a manual limit increase?

For new agencies on shared domains, no — limits are governed entirely by the rampup engine. The fastest path to a higher daily limit is consistent, healthy sending, which will move the sub-account up the stages automatically. Sub-accounts that need a higher limit sooner should add a dedicated domain.

Q: What happens if my limit is reached?

Campaign and bulk emails sent after the daily ceiling will fail they are not queued or retried. 1-to-1 emails, payment confirmations, calendar invites, and system notifications continue to deliver as normal. The limit resets at 00:00 UTC.

Q: Why did my account move down a stage?

The Stage History entry for the downgrade includes the trigger bounce spike, sustained delivery issue, or spam spike — alongside the date. The banner on the page will also show targeted recommendations for that specific issue.

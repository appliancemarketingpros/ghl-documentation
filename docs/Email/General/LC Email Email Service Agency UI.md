# LC Email: Email Service Agency UI

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008104-lc-email-email-service-agency-ui](https://help.gohighlevel.com/support/solutions/articles/155000008104-lc-email-email-service-agency-ui)  
**Category:** Email  
**Folder:** General

---

EMAIL DELIVERABILITY

Email Services Dashboard

Monitor domain health and sub-account email performance — all in one place.

What You'll Learn

The Email Services dashboard gives agencies full visibility into their domain sending health and sub-account performance. The interface adapts dynamically based on your domain health state.

This article covers what each health state looks like, how to read your delivery metrics, how to navigate sub-account performance, and how search and infinite scroll work across the dashboard.

Table of Contents

1

Domain Overview & Metrics

2

Domain Health States

3

Domain Health History

4

Sub-account Performance

5

Frequently Asked Questions

1

## Domain Overview & Metrics

For dedicated domains, the dashboard displays four key sending metrics. Use these benchmarks to catch deliverability issues early and track domain health over time.

Metric| What It Measures| Target Threshold  
---|---|---  
Delivery Rate| Percentage of emails successfully delivered| Keep above 95%  
Bounce Rate| Percentage of emails that could not be delivered| Keep under 2%  
Spam Complaint Rate| Percentage of delivered emails marked as spam| Keep under 0.1%  
Open Rate| Percentage of delivered emails that were opened| Keep above 20%  
  
![Domain overview metrics panel showing delivery rate, bounce rate, spam complaint rate, and open rate](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073937434/original/rT5vB7GrEkG2JRUf4boziI8woQl34zS2KA.png?1781765136)

Domain metrics panel — dedicated domain view

2

## Domain Health States

Six domain health states are possible — each with its own visual indicators and recommended actions. The state shown is determined automatically based on your domain's sending metrics over time.

How Health States Are Determined

The platform continuously evaluates three key signals from your domain's recent sending activity to assign a health state:

Signal| Upgrade threshold| Downgrade trigger  
---|---|---  
Bounce Rate| Under 2%| Exceeds 2%  
Spam Complaint Rate| Under 0.1%| Exceeds 0.1%  
Open Rate| Above 15%| Below 15% (signals low engagement)  
  
**Upgrade** happens when all three signals stay within thresholds over time. **Downgrade** happens when thresholds are breached. A domain that improves after a Critical state enters **Recovering** before it can reach Healthy. Newly provisioned domains start in the **New** state until enough sending history is built.

State 1 — Healthy

All metrics within healthy thresholds

Your domain is performing well. Continue monitoring regularly to maintain good domain health.

![Healthy state — green indicators, all metrics within threshold](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073939828/original/sDq9SKm2cRomGYqfNTHL-1Uf3XC6qBjrdQ.png?1781766774)

State 2 — At Risk

One or more metrics approaching their limit

Your domain shows early warning signs. Bounce rates or spam complaints may be creeping up. Review your sending practices and list hygiene before the state downgrades further.

![At Risk state — warning indicators and elevated metrics](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073939862/original/_axMvg4uCIVZshK6PRdztB0JzDlpMcjbVA.png?1781766793)

State 3 — Critical

Metrics have breached critical thresholds

Your domain health is severely degraded and sending capability may be restricted. Immediate action is required — address bounce rates and spam complaints before attempting recovery.

![Critical state — red indicators and sending restrictions active](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073939901/original/NzWwhDPfvNZQeW0Xjdbi5o1-3PNecYnuDw.png?1781766814)

State 4 — New

Recently provisioned — building sending history

Your domain was recently set up and is still in the warm-up phase. Sending limits may apply while domain health is established. Metrics will populate as mail volume increases.

![New state — warm-up phase indicators with limited metrics](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073939931/original/BSGpd5s_HgQMd0YnsY13uutr2QiV_p2k7w.png?1781766837)

State 5 — Recovering

Previous state: Bad → Current state: Medium

Your domain is improving after a Critical state. Keep metrics within healthy thresholds to continue the upward trend. Avoid actions that could trigger another downgrade.

![Recovering state — upward trend indicators after previous Critical state](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073940955/original/k4wM46S_Ywlv2ngfTncZr0lmmji502-6Cg.png?1781767461)

State 6 — Shared Domain

Shared sending infrastructure

This sub-account sends on a shared domain. The dashboard shows aggregate domain health rather than isolated metrics. Upgrading to a dedicated domain gives independent domain health management and full per-account metric visibility.

![Shared domain state — aggregate health view across shared sending infrastructure](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073941040/original/BPq4-u9wjH84mRXb8Yh_XgUXQIJrM7qN4w.png?1781767528)

3

## Domain Health History

The health history panel shows how your domain's health state has changed over time, giving you a clear picture of upgrades and downgrades at a glance.

**To move up:** Keep bounce rate under 2%, spam complaints under 0.1%, and open rate over 15%.

  * **Green indicators** — domain health improved (upgrade event)
  * **Orange indicators** — domain health declined (downgrade event)


Tip

Hover over any indicator on the timeline to see detailed information about what triggered the upgrade or downgrade at that point in time.

![Domain health history timeline showing green upgrade and orange downgrade indicators with hover tooltips](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073939571/original/L2TlXjydrHytlnJ_6mffNTWGrGAXxmn6OQ.png?1781766659)

Health history timeline — green = improvement, orange = decline

4

## Sub-account Performance

The **Sub-account performance** section shows how individual accounts using a shared domain are performing. Sub-accounts are grouped into three health buckets:

**Healthy** — sub-accounts with metrics within acceptable thresholds

**At Risk** — sub-accounts showing early signs of degraded sending health

**Critical** — sub-accounts with metrics that require immediate attention

![Sub-account performance section showing health bucket counts](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073938895/original/stRR01vCjVCZ6FRY67KplGHaYrOOVo6MjQ.png?1781766345)

![Sub-account performance expanded view showing location-level detail](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073939367/original/UkjB-YOhrTIiB5K3Ym0e9C57k_ya-X5lVg.png?1781766589)

Search

Finding sub-accounts by name

Click any health bucket accordion to expand it. The search field placeholder reads **Search for LC accounts**. Type to filter — matching accounts appear in real time.

If no match is found, the panel shows: **"No account found"** with the message _"Try a different name or clear your search to see all accounts using this domain."_

Location Redirect

Drilling into a specific account

Clicking any location in the list redirects you directly to that account's Email Services page, where you can view its individual sending metrics and health state.

Infinite Scroll

Loading large account lists

The first 20 accounts load immediately. As you scroll down, additional accounts load automatically — no pagination or "Load more" button required.

5

## Frequently Asked Questions

Q: What's the difference between a dedicated and a shared domain?

A dedicated domain is provisioned exclusively for your agency — its domain health is determined solely by your own sending behavior and you get full metric visibility. A shared domain pools sending across multiple accounts, meaning your domain health can be influenced by other senders on the same infrastructure.

Q: How quickly does the dashboard reflect changes in my sending metrics?

Metrics typically update within 24 hours of a sending event. Health state transitions (for example, moving from At Risk to Critical) may take a short processing window after thresholds are breached.

Q: My domain is in the Critical state. What should I do first?

Start by reviewing your bounce and spam complaint rates. Clean your contact list to remove invalid addresses, unsubscribes, and unengaged contacts. Avoid bulk campaigns until metrics improve. Once they drop back below thresholds, your domain will automatically move to the Recovering state.

Q: How long does it take to move from Recovering back to Healthy?

The timeline depends on how consistently your metrics stay within healthy thresholds. Maintain a bounce rate under 2%, spam complaints under 0.1%, and an open rate above 15%. The health history panel will show green indicators as your domain progresses.

Q: Why does my New domain show no metrics yet?

New domains are in a warm-up phase — metrics populate as mail volume accumulates. It's normal to see empty or limited data in the first few days. Ramp up sending gradually to build a positive sending history before scaling volume.

Q: Can I see health history for a sub-account on a shared domain?

The health history panel reflects the shared domain's aggregate health state, not individual sub-account behavior. For isolated health tracking per account, upgrade that sub-account to a dedicated domain. You can click any account in the sub-account list to navigate directly to its Email Services page.

Q: My open rate is below 20%. Does this affect my domain health state?

Open rate is a signal used when evaluating upgrades — the threshold for moving up is 15% (not 20%). A 20%+ open rate is a best-practice benchmark indicating strong engagement. If you're below 15%, consider reviewing subject lines, sending frequency, and list segmentation to re-engage your audience or prune inactive contacts.

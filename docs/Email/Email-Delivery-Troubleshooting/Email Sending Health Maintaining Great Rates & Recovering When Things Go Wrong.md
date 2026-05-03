# Email Sending Health: Maintaining Great Rates & Recovering When Things Go Wrong

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007768-email-sending-health-maintaining-great-rates-recovering-when-things-go-wrong](https://help.gohighlevel.com/support/solutions/articles/155000007768-email-sending-health-maintaining-great-rates-recovering-when-things-go-wrong)  
**Category:** Email  
**Folder:** Email Delivery Troubleshooting

---

Email Deliverability

Email Sending Health: Bounces, Complaints & Opens

The three metrics inbox providers use to judge your emails — what each one means, how to keep them healthy, and exactly how to recover if they slip.

Overview

Your email sending health is determined by three key metrics that inbox providers use to judge whether your emails are wanted — and whether to deliver them. Keeping these metrics within healthy ranges ensures your emails reach your contacts' inboxes instead of their spam folders.

This guide covers what each metric means, how to keep them at their best, and — if they slip — exactly how to recover.

Table of Contents

1

The Three Metrics That Matter

2

Bounce Rate — Keep It Below 2%

3

Spam Complaint Rate — Keep It Below 0.1%

4

Open Rate — Keep It Above 15%

5

Prevention Checklist — Best Practices at a Glance

6

Quick Recovery Reference

7

Frequently Asked Questions

1

## The Three Metrics That Matter

Inbox providers continuously evaluate your sending against these three benchmarks:

Metric| Target| What it means  
---|---|---  
Bounce Rate| Below 2%| Percentage of emails that could not be delivered to the recipient's inbox  
Spam Complaint Rate| Below 0.1%| Percentage of recipients who marked your email as spam  
Open Rate| Above 15%| Percentage of delivered emails that were opened by the recipient  
  
Tip

All three metrics are monitored continuously. Even a short spike can affect your sending health, so it's best to build good habits from the start rather than react after the fact.

2

## Bounce Rate — Keep It Below 2%

Causes

What causes bounces?

There are two types of bounces:

  * **Hard Bounce:** The email address does not exist, the domain is invalid, or the recipient's server permanently rejected the email.
  * **Soft Bounce:** A temporary issue — the inbox is full, the server was down, or the message was too large. These can resolve on their own but repeated soft bounces become a problem.


How to Keep Bounce Rate Low

  1. Use a verified opt-in process — only email people who confirmed their address
  2. Never import purchased or scraped lists — these almost always contain invalid addresses
  3. Regularly clean your contact list — remove addresses that have not engaged in 6+ months
  4. Use an email verification tool before importing large lists
  5. Remove hard bounces immediately after each campaign — do not retry them
  6. Avoid sending to role-based addresses like info@, admin@, noreply@ — these bounce frequently


How to Recover If Bounce Rate Is High

  1. Stop sending campaigns to your full list immediately
  2. Export all contacts who have bounced and permanently suppress them
  3. Run your remaining list through an email verification service to identify other at-risk addresses
  4. Remove or suppress any address that hasn't opened an email in the last 90 days
  5. Resume sending to your most engaged segment only — those who opened in the last 30 days
  6. Gradually expand back to your broader list only after bounce rate returns below 2%


Critical: Never Re-send to Hard Bounced Addresses

  * Hard bounced addresses should be permanently suppressed.
  * Re-sending to them signals poor list hygiene to inbox providers and will worsen your sending health.
  * The platform automatically suppresses hard bounces — do not manually re-add them.


3

## Spam Complaint Rate — Keep It Below 0.1%

Causes

What causes spam complaints?

  * Recipients do not remember signing up or did not consent to receive emails
  * Email content feels irrelevant, unexpected, or too frequent
  * The unsubscribe option is hard to find or does not work properly
  * Emails look like phishing or are overly promotional in tone
  * Sending to old lists that were not engaged for a long time


How to Keep Spam Complaint Rate Low

  1. Always get explicit consent — never assume opt-in
  2. Send a clear welcome email immediately after someone subscribes so they recognise your name
  3. Make the unsubscribe link large, visible, and working in every email
  4. Set expectations upfront — tell subscribers what kind of content they'll receive and how often
  5. Respect unsubscribe requests immediately — never delay removal
  6. Avoid subject lines that feel deceptive, overly salesy, or misleading
  7. Match the email content to what the subscriber originally signed up for
  8. Reduce frequency if engagement is dropping — over-sending is a leading cause of complaints


How to Recover If Complaint Rate Is High

  1. **Pause all bulk email campaigns immediately** — even a few more complaints will worsen the situation
  2. Identify which campaigns or segments are generating the most complaints
  3. Suppress everyone who complained — do not email them again
  4. Review your opt-in flow to ensure consent is genuine and clear
  5. Rewrite subject lines and email content to be less aggressive or misleading
  6. Add a highly visible one-click unsubscribe to every email going forward
  7. Resume sending only to your most engaged subscribers — people who opened in the last 30 days
  8. Monitor complaint rate daily until it returns below 0.1%


Gmail & Yahoo Now Enforce Strict Complaint Thresholds

  * Gmail treats a complaint rate above 0.08% as a warning and above 0.1% as critical.
  * Yahoo Mail applies similar enforcement policies.
  * Sustained high complaint rates can result in your emails being bulk-foldered or blocked entirely.


4

## Open Rate — Keep It Above 15%

Factors

What affects open rate?

  * **Subject line:** The single biggest factor — unclear or generic subject lines dramatically reduce opens
  * **Sender name:** Recipients open emails from names they recognise and trust
  * **Send time:** Emails sent at the wrong time for your audience will be buried or ignored
  * **List quality:** Disengaged contacts drag the open rate down — even if your content is great
  * **Preview text:** The short text shown next to the subject line in the inbox — often overlooked but influential


How to Keep Open Rate High

  1. Write subject lines that are specific, curiosity-driven, or clearly valuable — avoid clickbait
  2. Personalise the subject line with the recipient's first name where appropriate
  3. Keep subject lines under 50 characters so they don't get cut off on mobile
  4. Write a compelling preview text that complements the subject line
  5. Send from a consistent, recognisable sender name — not a generic address
  6. Test different send times — for most audiences Tuesday–Thursday between 9am and 11am performs well
  7. Segment your list and send content that is relevant to each group
  8. Re-engage or remove inactive subscribers regularly to keep your active list healthy


How to Recover If Open Rate Drops Below 15%

  1. **Do not send to your full list** — this will make the open rate worse, not better
  2. Identify your most engaged segment — contacts who opened at least one email in the last 60 days
  3. Send a targeted re-engagement campaign to inactive contacts with a compelling offer or question
     * Example: _"Are you still interested in hearing from us? Click here to stay subscribed."_
  4. Remove or suppress contacts who do not engage with the re-engagement campaign
  5. A/B test 2–3 different subject lines on a small segment before sending to your full list
  6. Review your email frequency — if you send too often, engagement drops
  7. Once open rate recovers above 15%, gradually expand sending to a broader audience


Tip: Apple Mail Privacy Protection

Open rate is also affected by Apple Mail Privacy Protection (MPP), which pre-loads emails and registers them as 'opened'. If a large portion of your audience uses Apple Mail, your open rate may appear higher than actual engagement. Focus on click rate as a secondary signal.

5

## Prevention Checklist — Best Practices at a Glance

| Best Practice| Why it matters  
---|---|---  
✓| Only email contacts who explicitly opted in| Reduces bounces and spam complaints  
✓| Send a welcome email immediately after sign-up| Sets expectations and builds recognition  
✓| Clean your list every 90 days| Removes dead addresses and inactive subscribers  
✓| Include a visible, working unsubscribe link in every email| Required by law and reduces complaints  
✓| Verify email addresses before importing large lists| Prevents hard bounce spikes  
✓| Never re-add suppressed or hard-bounced addresses| Avoids repeating damage to sender reputation  
✓| Use a dedicated sending domain| Builds your own sender reputation over time  
✓| Set up SPF, DKIM, and DMARC records| Proves email authenticity and improves deliverability  
✓| Segment your audience and send relevant content| Improves open rate and reduces complaints  
✓| Monitor your metrics after every campaign| Catch problems early before they escalate  
  
6

## Quick Recovery Reference

If a metric slips, use this table to take the right action fast:

Situation| Immediate Action| Next Step  
---|---|---  
Bounce rate above 2%| Pause campaigns. Export and suppress all bounced addresses.| Run list through email verification. Resume with engaged contacts only.  
Spam complaint rate above 0.1%| Pause all campaigns. Suppress all complainants immediately.| Audit opt-in flow. Rewrite content and subject lines. Add prominent unsubscribe.  
Open rate below 15%| Stop sending to the full list. Identify active segment (opened in 60 days).| Run re-engagement campaign. Remove non-responders. A/B test subject lines.  
All three metrics are poor| Stop all email sending. Audit your entire list and consent records.| Start fresh with a verified, consented list. Warm up sending volume gradually.  
  
7

## Frequently Asked Questions

Q: How often should I check my sending metrics?

Check your metrics after every campaign send. For high-volume senders, review them daily. Catching a spike early is far easier than recovering from sustained damage.

Q: Does a low open rate affect deliverability?

Yes. Inbox providers like Gmail and Outlook track engagement signals. If your emails are consistently ignored or not opened, they may begin routing future emails to the spam or promotions folder.

Q: My bounce rate spiked after importing a new list — what do I do?

Stop sending immediately. Export all bounced addresses and suppress them. Run the remaining imported addresses through an email verification tool before sending again. Consider warming up the new list with a small segment first.

Q: Is a 15% open rate realistic for all industries?

Open rate benchmarks vary by industry. B2B emails and transactional emails often see higher open rates (25–40%), while e-commerce promotional emails may see 10–20%. The 15% threshold is a general deliverability health signal — if your industry typically sees higher rates, aim for that higher standard.

Q: Can I recover a damaged sender reputation?

Yes — but it takes time. Recovery typically involves suppressing problematic contacts, re-engaging only your warmest audience, and gradually rebuilding sending volume. Significant reputation recovery can take 4–8 weeks of consistent healthy metrics.

Q: What's more important — open rate or click rate?

Both matter, but click rate is a stronger signal of genuine engagement — especially since open tracking can be inflated by privacy features like Apple Mail Privacy Protection. Use open rate as a top-of-funnel signal and click rate as the truer measure of subscriber interest.

Q: Will pausing my campaigns hurt my sender reputation?

No. Pausing temporarily during a recovery is far better than continuing to send to a list that's generating bounces or complaints. Once you've cleaned your list and addressed the underlying issue, ramp back up gradually starting with your most engaged subscribers.

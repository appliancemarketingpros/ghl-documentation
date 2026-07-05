# Low IP Reputation - Restore Sending IP Credibility

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006921-low-ip-reputation-restore-sending-ip-credibility](https://help.gohighlevel.com/support/solutions/articles/155000006921-low-ip-reputation-restore-sending-ip-credibility)  
**Category:** Email  
**Folder:** Reputation & Throttling

---

EMAIL DELIVERABILITY

Fixing Low IP Reputation Issues: Restore Sending IP Credibility

How shared and dedicated IP senders can diagnose and recover from IP-level reputation problems.

What You'll Learn

Your sending IP address has developed a poor reputation with email providers and security services, causing your emails to be blocked or rejected. Unlike domain reputation, IP reputation is tied to the specific server or infrastructure sending your emails. On the platform, this means the IP infrastructure you're using needs reputation recovery through improved sending practices and proper list management.

Table of Contents

1

What's Happening?

2

Quick Diagnosis: Identifying IP Reputation Issues

3

Understanding IP Infrastructure

4

Step-by-Step IP Reputation Recovery

5

Advanced Monitoring for Dedicated IP Users

6

When to Consider Dedicated IP

7

Best Practices for All Users

8

Recovery Timeline and Expectations

9

Working with Support

10

Still Having Issues?

11

Frequently Asked Questions

1

## What's Happening?

Your sending IP address has developed a poor reputation with email providers and security services, causing your emails to be blocked or rejected. Unlike domain reputation, IP reputation is tied to the specific server or infrastructure sending your emails. On the platform, this means the IP infrastructure you're using needs reputation recovery through improved sending practices and proper list management.

IP reputation issues are often more immediate than domain reputation problems, as they can result in complete blocking rather than just spam folder placement. The good news is that IP reputation can be restored more quickly than domain reputation with the right approach.

2

## Quick Diagnosis: Identifying IP Reputation Issues

Look for these bounce messages that indicate IP reputation problems:

Outlook/Microsoft Blocks

  * "The sending server's IP address is on a block list, causing Outlook to reject the message"
  * "The sending server's IP is blocked due to poor reputation or suspicious activity"
  * "The sending server's IP address is blocked or refused due to a history of abuse or suspicious activity"


General IP Reputation Issues

  * "The sending server's IP is blocked or blacklisted due to poor reputation or spam reports"
  * "The sending server's IP address has a poor reputation, causing the recipient to reject the message"
  * "The sending server's IP has a history of violating recipient policies, leading to mail being blocked"


Blacklist-Related IP Issues

  * "The sending server's IP is on a blocklist, causing rejection by the recipient's email provider"
  * "The sending server's IP address is listed on one or more DNS-based blacklists"
  * "The sending IP is listed on a reputation blocklist, causing the recipient server to reject the message"
  * "The sending IP or domain is listed on public blocklists due to suspected spam or abuse"
  * "The sending server's IP is blacklisted, causing email rejection"


3

## Understanding IP Infrastructure

Dedicated IP Setup

Shared IP (Default — Professionally Managed)

  * The platform maintains excellent IP reputation.
  * No manual IP reputation management required.
  * Cost-effective solution suitable for most sending volumes.
  * Benefit from collective good sending practices of the community.
  * Automatic load balancing across multiple high-quality IPs.
  * No warm-up required — ready to send immediately.
  * Professional monitoring and maintenance handled by the platform.


Dedicated IP (Available for High-Volume Senders)

  * Exclusive IP address assigned only to your account.
  * Complete control over your IP reputation.
  * Built-in SNDS monitoring available on the platform.
  * Access to advanced IP analytics and reporting.
  * Ideal for consistent high-volume sending (150,000+ emails/month).
  * Requires proper warm-up process for optimal performance.


Key Differences: IP vs. Domain Reputation

Aspect| IP Reputation| Domain Reputation  
---|---|---  
Where| Tied to the server/infrastructure sending emails| Tied to your specific sending domain  
Management| Professionally managed by the platform (shared IP)| Under your direct control  
Recovery| Can be restored relatively quickly with proper practices| Follows you regardless of ESP changes  
Impact| More immediate — affects delivery speed| Long-term factor in inbox placement  
  
4

## Step-by-Step IP Reputation Recovery

Step 1

Identify Your IP Setup

**Check your IP configuration:**

  1. **Navigate to Email Services**
     * Go to **Settings → Email Services**.
     * Check if you have access to the **Postmaster Tools** tab.
     * Look for the **Microsoft SNDS** section.
  2. **Determine your IP type**
     * **If you see SNDS data:** you have a dedicated IP.
     * **If you see "IP not found in your account":** you're on a shared IP (which is perfectly fine!).
  3. **For email header checking (if needed)**
     * Send a test email to yourself.
     * View the email source to see the sending IP in headers.
     * Look for: Authentication-Results: spf=pass (sender IP is [IP])


Step 2

IP Reputation Assessment Based on Your Setup

**For shared IP users (most users):**

Good News for Shared IP Users

The platform maintains excellent IP reputation for all shared IP users. You don't need to worry about IP reputation management — focus on your domain reputation and sending practices instead!

**For dedicated IP users:**

  * **Built-in monitoring**
    * Go to **Settings → Email Services → Postmaster Tools**.
    * View your **Microsoft SNDS** data directly on the platform.
    * Monitor complaint rates, volume patterns, and reputation metrics.
    * Track authentication success rates.
  * **External reputation checkers**
    * **Sender Score by Validity** — senderscore.org (0–100 scale)
    * **Talos Intelligence by Cisco** — talosintelligence.com/reputation_center
    * **Google Postmaster Tools** — postmaster.google.com
  * **Blacklist checkers**
    * MXToolbox Blacklist Check
    * Spamhaus Lookup
    * MultiRBL


Step 3

Recovery Actions Based on Your IP Type

**For shared IP users:**

**Your focus areas:**

  * **Domain Authentication:** Ensure SPF, DKIM, DMARC are properly configured.
  * **List Quality:** Maintain clean, engaged email lists.
  * **Content Quality:** Send relevant, valuable content to subscribers.
  * **Engagement:** Focus on improving open rates and click-through rates.
  * **Compliance:** Follow email marketing best practices.


**What the platform handles:** IP reputation monitoring, blacklist management, infrastructure optimization.

**For dedicated IP users:**

  1. **Monitor your SNDS data**
     * Check **Settings → Email Services → Postmaster Tools → Microsoft SNDS**.
     * Review complaint rates (target <0.1%).
     * Monitor volume patterns and authentication success.
     * Track any reputation warnings or alerts.
  2. **Address blacklist issues**
     * Use external tools to check for blacklist appearances.
     * Submit removal requests to relevant blacklist providers.
     * Document remediation efforts.
     * Coordinate with support if needed.
  3. **Implement IP warm-up (if needed)**
     * Start with low volume to highly engaged contacts.
     * Gradually increase volume over 4–6 weeks.
     * Monitor SNDS data for any negative trends.


Step 4

Optimize Your Sending Practices (All Users)

**Essential list management:**

  1. Go to **Contacts → Smart Lists**.
  2. Create filters to manage:
     * **Unengaged contacts** — separate contacts with no activity in 90+ days
     * **High-engagement contacts** — prioritize recent openers and clickers
  3. **Implement best practices**
     * Use double opt-in for new subscribers.
     * Regular list hygiene maintenance.
     * Segment based on engagement levels.
     * Maintain comprehensive suppression lists.


**Strengthen domain authentication:**

  1. Navigate to **Settings → Email Services → Dedicated Domain and IP**.
  2. Click **Verify Domain** for your domain.
  3. Maintain consistent "From" domain usage.
  4. Keep all authentication records up to date.


5

## Advanced Monitoring for Dedicated IP Users

Using the Platform's Built-In SNDS Monitoring

Accessing Your SNDS Data

  1. Navigate to **Settings → Email Services → Postmaster Tools**.
  2. Click on the **Microsoft SNDS** tab.
  3. Review the following metrics:
     * **Complaint Rate:** Should be <0.1%
     * **Trap Hits:** Should be 0
     * **Volume Patterns:** Monitor for consistency
     * **Authentication Success:** Should be >95%
  4. Set up a regular monitoring schedule (daily/weekly).
  5. Document trends and changes.


**Interpreting SNDS data:**

**Green status:** Excellent reputation, continue current practices.

**Yellow status:** Monitor closely, optimize sending practices.

**Red status:** Immediate action required, review all practices.

Additional Monitoring for Dedicated IP Users

Google Postmaster Tools Setup

  * Add your sending domain at postmaster.google.com.
  * Monitor spam rate trends (maintain <0.1%).
  * Track delivery error patterns.
  * Watch authentication success rates.
  * Set up alerts for performance changes.


6

## When to Consider Dedicated IP

Consider Upgrading If

  * You consistently send >150,000 emails per month.
  * You want access to detailed SNDS monitoring.
  * You need complete control over IP reputation.
  * Your business requires maximum deliverability control.
  * You can maintain consistent sending volumes.
  * You want advanced IP analytics and reporting.


Dedicated IP Advantages

  * **Built-in SNDS monitoring:** Access Microsoft reputation data directly.
  * **Complete control:** Your sending practices directly impact reputation.
  * **Advanced analytics:** Detailed reputation tracking and reporting.
  * **Isolated performance:** Your reputation isn't influenced by others.
  * **Scalability:** Better suited for high-volume sending.


7

## Best Practices for All Users

List Management Excellence

  * **Engagement-based segmentation:** Separate engaged from unengaged contacts.
  * **Regular list audits:** Monthly review of contact quality.
  * **Double opt-in implementation:** Ensure subscriber confirmation.
  * **Quality focus:** Prioritize engaged subscribers over list size.


Content and Sending Optimization

  * **Spam score testing:** Test campaigns before sending.
  * **Clear sender identification:** Use recognizable "From" names.
  * **Relevant content:** Match subscriber expectations.
  * **Easy unsubscribe:** Process opt-outs immediately.
  * **Consistent scheduling:** Maintain regular sending patterns.


Authentication and Technical Setup

  * **Perfect authentication:** Ensure SPF, DKIM, DMARC are configured.
  * **Domain consistency:** Use the same authenticated domain.
  * **Mobile optimization:** Ensure emails render well on all devices.
  * **Regular monitoring:** Check authentication status monthly.


8

## Recovery Timeline and Expectations

For Shared IP Users

  * **Immediate:** Focus on domain reputation and list quality.
  * **1–2 weeks:** See improvements in delivery rates.
  * **1 month:** Stable performance with optimized practices.
  * **Ongoing:** Maintain best practices for continued success.


For Dedicated IP Users

  * **Days 1–7:** Address blacklist issues, optimize practices.
  * **Weeks 2–6:** Monitor SNDS data, gradual improvement.
  * **Months 2–4:** Full reputation recovery and stable performance.
  * **Ongoing:** Continuous monitoring and optimization.


9

## Working with Support

When to Contact Support

  * **Shared IP users:** For general deliverability guidance and best practices.
  * **Dedicated IP users:** For SNDS data interpretation and IP-specific issues.
  * **Authentication help:** DNS configuration assistance.
  * **Dedicated IP consultation:** Discuss upgrade options and requirements.
  * **Performance optimization:** Get recommendations for your specific use case.


Information to Provide Support

  * **Your IP setup:** Shared or dedicated IP.
  * **Performance metrics:** Delivery rates, engagement data.
  * **Specific issues:** Bounce messages, delivery problems.
  * **Sending volume:** Current and planned email volumes.
  * **SNDS data:** Screenshots from your dashboard (dedicated IP users).


10

## Still Having Issues?

If you continue to experience IP reputation challenges:

  1. **Shared IP users:** Focus on domain reputation and sending practices — the platform handles IP reputation automatically.
  2. **Dedicated IP users:** Review your SNDS data and optimize accordingly.
  3. **All users:** Ensure perfect domain authentication and list quality.
  4. **Contact support:** Leverage their expertise and platform knowledge.
  5. **Consider professional consultation:** For advanced optimization strategies.


Remember

The platform's infrastructure is designed to maintain excellent IP reputation automatically for shared IP users, while dedicated IP users get advanced monitoring tools built right into the platform. Focus on what you can control — domain reputation, list quality, and content optimization.

11

## Frequently Asked Questions

Q: How do I know for sure whether I'm on a shared or dedicated IP?

Check Settings → Email Services → Postmaster Tools → Microsoft SNDS. If you see SNDS data, you have a dedicated IP. If it says "IP not found in your account," you're on a shared IP.

Q: If I'm on a shared IP, can another sender's bad behavior hurt my deliverability?

The platform actively manages shared IP reputation and monitors the pool, so this risk is minimized. It's part of why shared IP reputation management is handled centrally rather than left to individual senders.

Q: Is it worth switching to a dedicated IP if I don't send at high volume?

Generally not. Dedicated IPs need consistent volume to maintain a healthy reputation and require ongoing warm-up and monitoring. Below roughly 150,000 emails/month, a shared IP is usually the more reliable choice.

Q: How is SNDS different from Sender Score or Talos?

SNDS is Microsoft's own tool and only reflects your reputation with Outlook/Hotmail. Sender Score and Talos give broader, cross-provider reputation signals. Dedicated IP users should check all three for a complete picture.

Q: What happens to my dedicated IP's reputation if I stop sending for a while?

Reputation can decay during long gaps in sending, since providers see the IP as "cold" again. If you pause for more than a few weeks, plan to re-warm the IP with gradually increasing volume rather than resuming at full speed.

Q: Can I switch from dedicated back to shared IP if reputation issues persist?

Yes, and for senders who can't sustain the volume a dedicated IP needs, moving back to a professionally managed shared IP is often the simplest fix. Talk to support about the best path for your account.

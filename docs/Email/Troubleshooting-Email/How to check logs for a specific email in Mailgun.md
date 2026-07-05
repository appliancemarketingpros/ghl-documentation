# How to check logs for a specific email in Mailgun

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001188059-how-to-check-logs-for-a-specific-email-in-mailgun](https://help.gohighlevel.com/support/solutions/articles/48001188059-how-to-check-logs-for-a-specific-email-in-mailgun)  
**Category:** Email  
**Folder:** Troubleshooting Email

---

Email Deliverability

Mailgun Sending Logs

Look up the delivery status for any email sent through Mailgun and resolve the most common delivery errors.

Overview

This guide walks through finding a specific email's delivery status in Mailgun's Sending Logs, understanding what the results mean, and resolving the most common delivery errors — previously bounced addresses, accidental unsubscribes, and unauthenticated/DMARC failures.

Table of Contents

1

Mailgun Sending Logs

2

Analyzing the Results

3

Common Errors

→ Not delivering to a previously bounced address → Recipient unsubscribed accidentally → Unauthenticated email from a custom domain → Unauthenticated email from yahoo.com / hotmail.com / aol.com / outlook.com

4

FAQ

1

## Mailgun Sending Logs

Step 1

Log in to [app.mailgun.com/app/dashboard](<https://app.mailgun.com/app/dashboard>).

Step 2

Click **Sending**.

![Mailgun Sending menu](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48116160535/original/JVr72sqsbd8goiu1yWyP9X8LxzQIFiymnA.png?1625007552)

Step 3

Click **Logs**.

![Mailgun Logs menu item](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48116160533/original/jMWfS1lnuChsOsRrZdbYVxkKEj_FwXl5Ww.png?1625007551)

Step 4

Make sure the correct domain is selected.

![Domain selector in Mailgun logs](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48116160536/original/4gc_ywO8KMIJ2gmt_r41V-pqblZouLsulA.png?1625007552)

Step 5

Click **Add Filter**.

![Add Filter button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48188695181/original/_cN2JqLI_-4mgq52yjw5XkN8wD6j70j-fw.png?1644453931)

Step 6

Select **Recipient** from the dropdown list and paste the email address you're checking the delivery status for.

![Recipient filter dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48188695195/original/4e5JP7AlzSsBZYZOUHSn2mk7YQ0gtx0EAA.png?1644453944)

Step 7

Click **Filter**.

![Filter button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48188695270/original/5B1sUhnEpr9-WLqcHMifkVuz0WUuxtyCsQ.png?1644454025)

2

## Analyzing the Results

Step 1

Once you locate the email, click the gear (⚙) icon on the right and select **Quick view**.

Step 2

This shows a preview of the email along with its delivery status.

![Quick view of a Mailgun log entry](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48188695369/original/C19SliRpd7Pl_5q67zgT2hTAWFXDSR3jrg.png?1644454139)

Tip

If the status says **delivered** but the recipient says they never got it, check their spam folder, or reach out to Mailgun support to see if the receiving email provider is silently blocking it on their end.

3

## Common Errors

Error

Not delivering to a previously bounced address

**Solution:**

1\. Click **Sending → Suppressions**  
2\. Choose the domain at the top  
3\. Search for the recipient's email  
4\. Select the recipient and click the trash icon on the right to remove them from the **Bounces** tab

Error

Recipient unsubscribed accidentally

**Solution:** switch to the **Unsubscribes** tab and remove the email from there.

![Unsubscribes tab in Mailgun](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48188695886/original/EgH5LxHkk9DeQiKIUhWyFYFOyklyac8D7Q.png?1644454582)

Error

Unauthenticated email from a custom domain

**Solution:** set DMARC to none for the custom domain.

If you're using Gsuite email, you can [configure DMARC to none here](<https://support.google.com/a/answer/10032169?hl=en>).

Error

Unauthenticated email from yahoo.com / hotmail.com / aol.com / outlook.com

**Quick workaround:** switch the sender email from yahoo.com, aol.com, or any other free-mail domain to your own domain or gmail.com.

For example, switch `name@yahoo.com` to `name@gmail.com` or `name@your_domain.com`.

[Learn where to configure the sender's email address here](<https://gohighlevelassist.freshdesk.com/support/solutions/articles/48000979925-masking-campaign-emails-from-name-address>).

4

## FAQ

Q: I can't find the email in Mailgun logs at all — why?

Double-check that you have the correct domain selected in the logs view, and that your filter/date range covers when the email was actually sent. Logs are scoped to a single domain at a time.

Q: What's the difference between a bounce and an unsubscribe?

A bounce means the mailbox provider rejected the message (invalid address, full inbox, etc.). An unsubscribe means the recipient explicitly opted out. Both suppress future sends, but they're removed from different tabs — Bounces vs. Unsubscribes.

Q: How long does Mailgun retain sending logs?

Retention depends on your Mailgun plan. If you need to look up an older delivery, check your Mailgun plan's log retention window or reach out to Mailgun support directly.

Q: Can I search logs across all my domains at once?

No, the Logs view filters by one domain at a time. Make sure the correct domain is selected (Step 4) before adding your recipient filter.

Q: Why would DMARC cause an "unauthenticated" error?

If a domain has a strict DMARC policy (quarantine or reject) and the sending setup isn't fully aligned with SPF/DKIM, mailbox providers flag the message as unauthenticated. Setting DMARC to none relaxes enforcement while you sort out authentication.

Q: Do I need my own Mailgun login to check this?

Yes — you'll need access to the Mailgun account/dashboard tied to your sending domain to view logs and manage suppressions directly.

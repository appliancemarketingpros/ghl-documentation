# Troubleshooting Email Statistics

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001208601-troubleshooting-email-statistics](https://help.gohighlevel.com/support/solutions/articles/48001208601-troubleshooting-email-statistics)  
**Category:** Email  
**Folder:** Troubleshooting Email

---

Email Deliverability

Email Statistics Not Showing

Why open, click, delivered, and bounce stats might be missing — and how to fix it.

Overview

If email statistics aren't showing up, it's usually related to how the email was sent, which email provider is configured, or a missing CNAME record or Mailgun webhook. Work through the checks below to find the cause.

Table of Contents

1

Why Email Statistics Are Not Showing

2

Try Resetting the Mailgun API Key

3

Double-Check the CNAME Record

4

Double-Check Mailgun Webhooks

5

FAQ

1

## Why Email Statistics Are Not Showing

Check 1

How was the email sent?

Check how the email was sent — through the email builder's bulk action, or from a smartlist, workflow, or campaign. Each method has its own section for email statistics. See [Where will email statistics show for every email activity?](<https://help.gohighlevel.com/support/solutions/articles/48001215386-email-statistics#Where-will-email-statistics-show-for-every-email-activity?>)

If stats are missing after clicking into the email template:

![Missing email stats after opening the template](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48186969567/original/o7R9Zujq1hhYNwlXiBhBsGPczF6JdpTt5w.png?1644017728)

Stats only populate in the Email Builder when emails are sent through the bulk action shown below:

![Sending emails through the Email Builder bulk action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48186969568/original/8Grr4aFjwLE_qLJVsbh9xC4OHu8gAFhbYw.jpeg?1644017728)

Check 2

Which provider is sending the email?

With an SMTP provider, delivered/bounced stats can't be fetched or displayed — SMTP integrations only show opened and clicked. Only Mailgun is able to show full stats.

Pro Tip

We highly recommend setting up Mailgun or LC Email for accurate statistics.

If the sub-account previously used an SMTP provider and the workflow still contains SMTP-era statistics, those stats won't display properly. Duplicate the workflow and start sending emails again from there to see the statistics show up correctly.

2

## Try Resetting the Mailgun API Key

Go to **Agency view → Settings → Email Services → Location Settings** , edit the Mailgun API integration for the sub-account, and type **Delete**.

Then re-integrate: [Mailgun API Key — where to find it in Mailgun and add it to the platform](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>).

![Resetting the Mailgun API key](https://i.ibb.co/1TVG21t/2023-1-24-11-12-42.gif)

3

## Double-Check the CNAME Record

The CNAME record is essential for Mailgun to track opens, clicks, and unsubscribes. The fix is the same as when links don't open:

[Why are my email links changing, and how do I fix links in the email that don't open?](<https://help.gohighlevel.com/en/support/solutions/articles/48001151622>)

4

## Double-Check Mailgun Webhooks

1\. Click **Sending**  
2\. Click **Webhooks**  
3\. Make sure the right domain is selected, based on which domain/subdomain is configured for your sub-account  
4\. All webhooks should be configured, as shown in the screenshot below  
5\. If not, click **Add Webhook** for every event type

![Mailgun webhooks configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48283724301/original/XuGLhQDfmu5CAwRdHREf2Ak9-qX5s6R9gg.png?1677265427)

5

## FAQ

Q: Why don't bounced or delivered stats show up for emails sent through my SMTP provider?

SMTP integrations only expose opened and clicked events. Delivered and bounced data requires deeper access to send-time events, which is only available through Mailgun or LC Email.

Q: If I switch from SMTP to Mailgun, will old stats fill in retroactively?

No. Emails already sent through SMTP won't gain delivered/bounced data after the fact. Duplicate the workflow and resume sending from the duplicate so new sends are tracked correctly under Mailgun.

Q: Do bulk Email Builder stats and workflow email stats live in the same place?

No — each sending method (email builder bulk action, smartlist, workflow, or campaign) has its own dedicated stats section. Check the sending method first if stats seem to be missing.

Q: How do I know if my CNAME record is actually set up correctly?

Use a tool like MX Toolbox's CNAME lookup to confirm the record resolves correctly for your tracking subdomain. If it doesn't resolve, opens/clicks/unsubscribes won't be tracked even if everything else is configured correctly.

Q: What happens if only one Mailgun webhook event type is missing?

Only the data tied to that specific event (e.g., bounces) will be missing — other configured events will still report normally. Add the missing webhook for that event type to fill the gap.

Q: Is LC Email treated the same as Mailgun for tracking purposes?

Yes — LC Email is built to provide full statistics (opens, clicks, delivered, and bounced) the same way Mailgun does, without needing you to manage CNAME records or webhooks yourself.

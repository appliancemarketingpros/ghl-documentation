# Email Widgets for Dashboards and Reporting

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004328-email-widgets-for-dashboards-and-reporting](https://help.gohighlevel.com/support/solutions/articles/155000004328-email-widgets-for-dashboards-and-reporting)  
**Category:** Dashboards  
**Folder:** Dashboard Widget Types

---

**  
**

Track every email your team sends — without leaving HighLevel. Email Widgets bring dedicated email analytics directly into your Sub-Account Dashboard and Custom Reports, giving agencies and their clients a clear picture of delivery health, engagement, and exactly which campaign, workflow, or template is driving it — all without digging through Marketing → Emails → Campaigns.

  


**TABLE OF CONTENTS**

  * What Are Email Widgets?
  * Key Benefits of Email Widgets
  * Prerequisites & Access
  * Available Email Widgets
  * Widgets in Dashboard, Custom Report, Custom Metrics
  * How to Add Email Widgets
  * Configuring Email Widgets
    * Configure Tab
    * Conditions Tab
    * How AND/OR conditions work
    * Themes Tab
  * Using Email in Custom Metrics
  * Frequently Asked Questions
  * Related Articles


* * *

## What Are Email Widgets?

Email Widgets are pre-built visual reporting blocks that surface email messaging data directly inside any HighLevel Sub-Account Dashboard or Custom Report. They work exactly like SMS Widgets — no manual exports, no navigating into Marketing → Emails → Campaigns → Workflow Campaigns to check one email's numbers — just clean, real-time email analytics wherever you need them.

With 11 widgets covering delivery status, engagement, bounces, unsubscribes, and domain-level breakdowns, you can build an email health view for clients in minutes, filter it down to one specific campaign or workflow, and share it on a schedule.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075154356/original/Ygn_TmcIMNRGynvS7ckV9paTyGHhrftBpQ.png?1783084309)

## Key Benefits of Email Widgets

  * **Monitor delivery health** — See Accepted, Delivered, Opened, Clicked, Replied, Soft Bounced, Hard Bounced, Failed, and Unsubscribed counts without opening Conversations or the Campaigns tab
  * **Isolate one specific campaign or workflow** — Filter by Source (Workflow, Email Marketing Campaign, Campaign, Bulk Action, Template, Other) and then pick the exact campaign/workflow by name, so a widget shows numbers for just that one send
  * **Track unsubscribes over time** — Unsubscribed Emails Daily shows a day-by-day trend so you can catch list-health issues early
  * **See where deliverability problems concentrate** — Emails By Domain groups results by recipient domain to spot provider-specific delivery issues (e.g. all bounces landing on one domain)
  * **Hold teams accountable** — Filter any widget by Sent By to see email activity by team member
  * **Precise control with AND/OR conditions** — Stack filters across Status, Source, Sent By, Domain, Workflow, Campaign, Email Marketing Campaign, Template, and Bulk Action to segment exactly the data you need


## Prerequisites & Access

  * Dashboards & Reports access: verify the user has permission to view or edit dashboards and to create or schedule Custom Reports
  * No additional integration or connection is required — email data is already available inside HighLevel


## Available Email Widgets

11 email widgets are available, each configurable with chart type, conditions, and themes.

Widget| What Data It Shows  
---|---  
Accepted Emails| Number of emails successfully accepted by the sending system  
Delivered Emails| Number of emails delivered to recipients  
Opened Emails| Number of emails opened by recipients  
Clicked Emails| Number of emails where a link was clicked  
Replied Emails| Number of emails that received a reply  
Soft Bounced Emails| Number of emails that soft bounced (temporary delivery failure)  
Hard Bounced Emails| Number of emails that hard bounced (permanent delivery failure)  
Failed Emails| Number of emails that failed to send  
Unsubscribed Emails| Number of recipients who unsubscribed  
Unsubscribed Emails Daily| Daily trend of unsubscribes — supports Group By (Source, Status, Sent By, Workflow, Campaign, Template, Email Marketing Campaign, Bulk Action, Domain)  
Emails By Domain| Emails grouped by recipient domain — supports the same Group By options above  
  
> Most widgets above open as a single number by default but can be switched to donut, bar, line, horizontal bar, or table view. Emails By Domain and Unsubscribed Emails Daily are the two widgets with Group By enabled out of the box; every other widget can still be **filtered** (via Conditions) down to a single campaign, workflow, or template — Group By and filtering are separate controls (see Configure vs Conditions tab below).

## Widgets in Dashboard, Custom Report, Custom Metrics

In all 3 environments, you use the same 11 email widgets. Choose based on how you need to view, compute, and share the data.

  1. **Dashboard** — Best for always-on monitoring. Widgets live on a Sub-Account dashboard and update automatically. Build an email health section alongside your SMS and Calls widgets for a full messaging overview.
  2. **Custom Reports** — Best for scheduled client delivery. Add email widgets to a report layout and schedule automatic email delivery on a daily, weekly, or monthly cadence.
  3. **Custom Metric** — Build a custom metric to create your own KPI, not just an email metric — combine email data with other modules as well.


## How to Add Email Widgets

**1) Add Email Widgets to a Dashboard**

  1. In your Sub-Account, navigate to Dashboards and open the dashboard you want to edit (or create a new one)
  2. Click **Edit Dashboard** in the top right corner
  3. Click **\+ Add Widget** — the widget panel opens on the right side
  4. Scroll down to the **Emails** section — all 11 email widgets are listed here
  5. Click on the widget you want to add — it is placed on your dashboard canvas
  6. Configure the widget using the **Configure** , **Conditions** , and **Themes** tabs (see below)
  7. Click **Save Changes** to publish the widget to your dashboard


> **Tip:** To recreate the per-campaign view agencies are used to seeing under Marketing → Emails → Campaigns → Workflow Campaigns, add an Opened Emails, Clicked Emails, and Delivered Emails widget side by side, each filtered to Source = Workflow and the same specific workflow — this puts that campaign's engagement summary directly on the dashboard.

**2) Add Email Widgets to a Custom Report**

  1. In your Sub-Account, go to **Reporting → Custom Reports** and open an existing report or click **New Report**
  2. Choose to start from a **blank canvas** , use a **template** , or import an existing dashboard layout
  3. Click **Add Widget / Element** in the top left of the report builder
  4. Scroll to the **Emails** section and drag the widgets you want into your report layout
  5. Configure each widget using the **Configure, Conditions, and Themes** tabs
  6. Click **Save**
  7. Click **Send** or **Schedule** to set up automatic email delivery of the report


## Configuring Email Widgets

Each email widget has three configuration tabs in the Edit Widget panel.

### Configure Tab

The Configure tab controls how the widget looks and what data dimension it groups by.

  * **Metric** — Count of Emails
  * **Group** — Controls how widget data is broken down visually. Options: Source, Status, Sent By, Domain — and conditionally: Workflow, Campaign, Template, Email Marketing Campaign, Bulk Action (see note below)


⚠️ **How to unlock Workflow, Campaign, Template, Email Marketing Campaign, and Bulk Action in Group:**

These five options appear greyed out in the Group dropdown by default. To activate them:

  1. Go to the **Conditions** tab first
  2. Add a **Source** filter and set its value (e.g. Source = Workflow)
  3. Make sure all condition branches use the same Source value
  4. Return to the **Configure** tab — the matching Group option is now active


This lets you break down widget data by the specific workflow, campaign, template, or bulk send that triggered each email. For example: set Source = Workflow in Conditions, then Group by Workflow in Configure to see email volume broken down per workflow.

### Conditions Tab

Add filters to control exactly which email data the widget displays. Conditions support AND/OR logic — stack multiple filters to narrow or expand your dataset.

Condition| Values| Notes  
---|---|---  
Source| Workflow | Email Marketing Campaign | Campaign | Bulk Action | Template | Other| Filter by what triggered the email send. Selecting a value here unlocks the matching dependent field below.  
Status| Accepted | Delivered | Opened | Clicked | Replied | Soft Bounced | Hard Bounced | Failed | Unsubscribed| Filter by delivery/engagement outcome  
Sent By| Any team member in the sub-account| Filter emails by the sender  
Domain| Recipient sending domain| Filter by recipient email domain  
Workflow _(appears when Source = Workflow)_|  Any workflow in the sub-account| Narrows the widget to one specific workflow — this is the setting that matches the "Workflow Campaigns" view under Marketing → Emails  
Campaign _(appears when Source = Campaign)_|  Any campaign in the sub-account| Narrows the widget to one specific campaign  
Email Marketing Campaign _(appears when Source = Email Marketing Campaign)_|  Any email marketing campaign in the sub-account| Narrows the widget to one specific email marketing campaign  
Template _(appears when Source = Template)_|  Any email template in the sub-account| Narrows the widget to emails sent from one specific template  
Bulk Action _(appears when Source = Bulk Action)_|  Any bulk send in the sub-account| Narrows the widget to one specific bulk email send  
  
### How AND/OR conditions work

  * Use **\+ AND** to narrow results — all conditions in a group must be true
  * Use **OR** to add a separate condition group — either group can be true
  * Example: Source = Workflow AND Workflow = "In-Person Events Opt-ins" OR Source = Campaign — shows emails from one specific workflow or from all campaigns


### Themes Tab

Match widget colors to your dashboard or client brand. Select from available theme presets or customize colors.

## Using Email in Custom Metrics

Email is already available as a dimension in Custom Metrics. Use **Count of Emails** in the formula builder to create KPIs that combine email data with other metrics.

**How to use Count of Emails in a Custom Metric:**

  1. Go to Dashboards → Edit → Custom Metrics and click **Create Custom Metric**
  2. In the Formula builder, select **Count of Emails** as your metric (supports up to 4 metrics combined with operators)
  3. Click on **Count of Emails** in the formula to open the Configuration panel on the right
  4. Under Filters, add conditions to refine which emails are counted — Status, Source, Sent By, Domain (plus Workflow/Campaign/Template/Email Marketing Campaign/Bulk Action once the matching Source is set)
  5. Use **\+ AND** and **OR** to combine multiple filters
  6. Name your metric, set Data Type, and click **Create**


**Example KPIs you can build in Custom Metrics:**

  * **Email Open Rate** — Count of Emails (Status = Opened) ÷ Count of Emails (Status = Delivered) × 100
  * **Campaign-Specific Click Rate** — Count of Emails (Source = Workflow, Workflow = "X", Status = Clicked) ÷ Count of Emails (Source = Workflow, Workflow = "X", Status = Delivered) × 100
  * **Bounce Rate** — [Count of Emails (Status = Soft Bounced) + Count of Emails (Status = Hard Bounced)] ÷ Count of Emails (Status = Accepted) × 100


## Frequently Asked Questions

**Q: Can I show stats for just one campaign on my dashboard instead of all campaigns combined?** Yes. Add any Email widget, go to the Conditions tab, set Source to Workflow, Campaign, Email Marketing Campaign, Template, or Bulk Action (whichever matches how the email was sent), then select the specific one from the dependent field that appears. The widget will show data for that single campaign/workflow only.

**Q: What's the difference between "Campaign" and "Email Marketing Campaign" as Source options?** _[Needs SME/PM confirmation before publishing — both exist as distinct filterable Source values with their own dependent field, but the plain-language distinction between the two hasn't been confirmed for this article.]_

**Q: My agency's emails are set up as Workflow Campaigns (Marketing → Emails → Campaigns → Workflow Campaigns) — which Source do I pick?** Select Source = Workflow, then choose the specific workflow by name in the field that appears. This reproduces the same per-campaign summary (Delivered, Opened, Clicked, Bounced, Unsubscribed) you'd see by opening that campaign directly, but on your dashboard.

**Q: What are all the Status values available?** Accepted, Delivered, Opened, Clicked, Replied, Soft Bounced, Hard Bounced, Failed, and Unsubscribed.

**Q: What are the Source options?** Workflow, Email Marketing Campaign, Campaign, Bulk Action, Template, and Other.

**Q: Why is Workflow (or Campaign, Template, Email Marketing Campaign, Bulk Action) greyed out in the Group dropdown?** These only activate in Group once a matching Source filter is set in the Conditions tab. See the Configure Tab section above for the full steps.

**Q: Why is my email widget showing no data?** Common causes: the selected date range has no email activity, filters are too narrow (e.g. a Source + specific campaign combination with no sends in range), or email hasn't been used in this sub-account. Try removing conditions or widening the date range.

**Q: Can I combine Email widgets with SMS and Calls widgets on the same dashboard?** Yes. All messaging categories — Email, SMS, and Calls — can be placed on the same dashboard for a unified communication health view.

**Q: Can I schedule an email report for clients?** Yes. Add Email widgets to a Custom Report and schedule automatic email delivery on a daily, weekly, or monthly cadence.

**Q: Is Email available in Custom Metrics?** Yes. Count of Emails is already available in the Custom Metrics formula builder. Filter by Status, Source, Sent By, and Domain (plus the dependent campaign/workflow fields) to build precise KPIs like open rate or campaign-specific click rate.

**Q: How often do Email widgets update?** Widgets update automatically. No manual refresh is needed.

## Related Articles

  * [SMS Widgets for Dashboards & Reporting](<https://help.gohighlevel.com/support/solutions/articles/155000008054-sms-widgets-for-dashboards-reporting>)
  * [What Are Dashboard Widgets?](<https://help.gohighlevel.com/support/solutions/articles/155000001212-what-are-dashboard-widgets->)
  * [How To Create A Custom Dashboard](<https://help.gohighlevel.com/support/solutions/articles/155000001531-how-to-create-a-custom-dashboard>)
  * [How to Create and Schedule Reports](<https://help.gohighlevel.com/support/solutions/articles/155000001210>)
  * [Dashboards: Meta Ad Widgets and Insights](<https://help.gohighlevel.com/support/solutions/articles/155000006608-dashboards-meta-ad-widgets-and-insights>)

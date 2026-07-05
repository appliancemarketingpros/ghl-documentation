# How Sender Domains Work in LC Email Campaigns

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007249-how-sender-domains-work-in-lc-email-campaigns](https://help.gohighlevel.com/support/solutions/articles/155000007249-how-sender-domains-work-in-lc-email-campaigns)  
**Category:** Email  
**Folder:** LC Email

---

EMAIL DELIVERABILITY

Sender Domain Settings

Choose the right domain for every campaign, keep your From Email compliant, and protect your sender reputation.

Overview

Sender Domains determine which domain is used to send an email campaign and whether the From Email address is valid and compliant. Proper sender domain selection helps prevent campaign failures, protects domain reputation, and improves inbox placement.

Availability

Sender Domain behavior applies **only to LC Email** locations. SMTP-based email sending follows its existing workflow.

Table of Contents

1

What Are Sender Domain Settings?

2

Key Benefits of Sender Domain Settings

3

How Sender Domains Behave in Different Scenarios

4

How to Set Up and Configure Sender Domains for a Campaign

5

Frequently Asked Questions

1

## What Are Sender Domain Settings?

Sender Domain Settings are available when you send or schedule an email campaign under **Marketing → Emails → Campaigns**. They determine which domain is used to send a campaign and ensure that the From Email address aligns with that domain.

Email providers expect this alignment to authenticate messages correctly. When the sending domain and sender email do not match, campaigns may fail to send or be filtered as spam. With Sender Domain Settings, you can choose the appropriate sending domain for each campaign, validate the sender email in real time, and prevent campaigns from launching if domain compliance requirements are not met.

This per-campaign control helps reduce delivery issues and improves overall sending reliability. Once a campaign is sent or scheduled, the selected sender domain is locked for that campaign.

2

## Key Benefits of Sender Domain Settings

**Fewer Send Failures** — prevents campaigns from sending with mismatched or non-compliant sender domains, reducing hard errors at send time.

**Better Deliverability** — ensures proper domain alignment, helping email providers authenticate messages and improving inbox placement.

**Per-Campaign Control** — lets you choose the most appropriate sending domain for each campaign instead of relying on a single default.

**Automatic Safeguards** — automatically adjusts supported sender emails and surfaces clear warnings when manual action is required.

**Clear Visibility** — provides real-time validation and quick access to domain configuration, making issues easy to identify and resolve.

3

## How Sender Domains Behave in Different Scenarios

Scenario

Shared Domains (Agency or Platform)

When a campaign uses a shared sending domain, public email addresses such as Gmail or Yahoo are supported. The platform automatically adjusts the sender email behind the scenes to meet compliance requirements, allowing the campaign to send successfully without user intervention.

Scenario

Single Dedicated Domain

If a location has one verified dedicated domain, it is automatically selected during the send or schedule step. The sender email must match this domain, and real-time validation ensures the campaign is compliant before sending.

Scenario

Multiple Dedicated Domains

When multiple verified domains are available, you can choose a specific domain for the campaign or select **All Domains**. Choosing All Domains allows the platform to rotate sending across eligible domains based on internal rules to help manage deliverability at scale.

The table below summarizes how sender domains behave across common campaign scenarios.

Scenario| What the User Enters| What Happens  
---|---|---  
Shared domain + public email| name@gmail.com| Email is auto-refactored for compliance  
One dedicated domain| Matching domain email| Domain auto-selected and validated  
Multiple domains (single)| Selects one domain| Uses selected domain only  
Multiple domains (All Domains)| Enters marketing| Domains rotate automatically  
Dedicated domain mismatch| Domain ≠ sender email| Send is blocked  
Domain not verified| DNS incomplete| Warning shown with fix link  
  
4

## How to Set Up and Configure Sender Domains for a Campaign

Sender domain selection happens naturally as part of sending or scheduling an email campaign. There's no separate setting to turn on or configure in advance.

Step 1

Go to Campaigns

Go to **Marketing → Emails → Campaigns**.

![Navigating to Marketing, Emails, Campaigns](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062541657/original/ze0sRG7VX2OdNL3Lnn58GbebG9a5f9CBlA.png?1768304730)

Step 2

Open a Campaign

Open a new campaign or an existing draft.

![Opening a new or existing campaign draft](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062541708/original/uvGDXxJ6OmcIoJVp0Fm0hEi5H3TaIKdGhg.png?1768304758)

Step 3

Review Campaign Details

Inside the email campaign builder, click **Send** or **Schedule** to review the campaign details.

![Reviewing campaign details before sending or scheduling](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062541742/original/cVjtJTns0eY4IIlmYzVj8Nl-4ScM1SJPFg.png?1768304799)

Step 4

Confirm Sender Details

In the **Sender Details** section, take a moment to confirm the **Sender Name** and **Sender Email**.

![Sender Details section showing Sender Name and Sender Email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062542511/original/yUhh4H19Wi1FRvcYcSN93HpXGeQJx8F8Iw.png?1768305076)

Step 5

Choose a Sender Domain

Open the **Sender Domain** dropdown to see which sending options are available for your location. The options shown change based on how your email domains are configured:

  * If you're using **shared domains** , public email addresses are supported and automatically adjusted for compliance.
  * If **one dedicated domain** is available, it's pre-selected and must match the sender email.
  * If **multiple dedicated domains** are configured, you can choose a specific domain or select **All Domains** to let the platform rotate sending across eligible domains to manage deliverability.


![Sender Domain dropdown with available sending options](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062544375/original/xpDMY7KgIttDxgOURKmFGCDmFjfgTAx-uQ.png?1768305964)

Step 6

Resolve Warnings or Errors

If a warning or error appears, use the **Review Domain Configuration** hyperlink to check things like domain verification, warm-up status, or IP assignment.

![Review Domain Configuration link](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062543611/original/BSUw9vRW7fKWi1HL_x50G8SVAKLSoIprtA.png?1768305582)

Warnings vs. Errors

**Warnings** indicate a potential issue, such as a sender email and sender domain mismatch — the campaign can still be sent, but matching domains is recommended to reduce the risk of spam filtering. **Errors** indicate blocking issues where the campaign cannot be sent until the problem is fixed.

![Example of a warning and an error message on sender domain configuration](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062565977/original/7dUXgMQxCCQeFiv1rW-g-rt7g95y4W-0ZQ.png?1768316471)

You're All Set

Once everything looks good, finish sending or scheduling the campaign. The sender domain you choose is locked to the campaign when it's sent or scheduled.

5

## Frequently Asked Questions

Q: Why am I seeing a warning even though my campaign can still be sent?

Warnings appear when there's a potential deliverability issue, such as a sender email and domain mismatch. The campaign can still be sent, but matching domains is recommended to avoid spam filtering.

Q: What happens if my sender domain is not verified or warmed up?

The campaign cannot be sent until the domain is verified and meets readiness requirements. A warning or error message will guide you to complete the required setup.

Q: Can I use a different Reply-To address than the sender domain?

Yes. The Reply-To address is independent of the sender domain and can point to any valid email address.

Q: Does selecting "All Domains" affect email deliverability?

No. When selected, the platform sends emails only from verified and warmed domains, rotating them based on internal rules to help manage reputation and maintain deliverability.

Q: Does Sender Domain behavior apply to SMTP-based sending?

No. Sender Domain Settings apply only to LC Email locations. If you're sending through a custom SMTP connection, your existing SMTP workflow and domain rules still apply.

Q: Can I change the sender domain after a campaign has been scheduled?

No. The sender domain is locked to the campaign once it's sent or scheduled. To use a different domain, you'll need to edit the draft before scheduling, or duplicate the campaign and choose a new domain.

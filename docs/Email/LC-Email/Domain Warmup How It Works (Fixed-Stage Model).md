# Domain Warmup: How It Works (Fixed-Stage Model)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005242-domain-warmup-how-it-works-fixed-stage-model-](https://help.gohighlevel.com/support/solutions/articles/155000005242-domain-warmup-how-it-works-fixed-stage-model-)  
**Category:** Email  
**Folder:** LC Email

---

EMAIL DELIVERABILITY

Domain Warmup: How the Fixed-Stage Model Works

Learn how the platform's fixed-stage warmup model builds sender reputation and improves deliverability for new and existing domains.

What You'll Learn

This guide explains how the platform's domain warmup works using a fixed-stage model — helping you build sender reputation and improve email deliverability safely.

Table of Contents

1

What is Domain Warmup?

2

How the Warmup Model Works

3

When Does Warmup Start?

4

Who Can Use Email Warmup and How to Enable It

5

Google Postmaster Integration (Recommended)

6

Best Practices for a Successful Warmup

7

When Is Warmup Complete?

8

Frequently Asked Questions

9

Related Articles

1

## What is Domain Warmup?

Domain warmup is the process of gradually increasing your daily email volume to build a trusted sender reputation with inbox providers like Gmail, Outlook, and Yahoo.

Without proper warmup, new domains are more likely to:

  * Be flagged as spam
  * Experience high bounce or complaint rates
  * Face email delivery blocks or delays


The platform automates this process to help you build trust and maximize email deliverability.

2

## How the Warmup Model Works

This system uses a fixed-stage, gradual warmup model, which means:

  * Each stage has a predefined daily sending limit.
  * Progression only occurs when the full daily limit for the current stage is reached.
  * If the daily limit is not met, the domain remains in the same stage.
  * There are no hourly sending limits.
  * You must send emails through the warming domain for progress to be tracked.


Warmup Stage Breakdown

Stage| Daily Limit  
---|---  
1| 1,000  
2| 2,500  
3| 5,000  
4| 6,500  
5| 8,000  
6| 10,000  
7| 14,000  
8| 20,000  
9| 25,000  
10| 35,000  
11| 50,000  
12| 80,000  
13| 125,000  
14| 175,000  
15| 250,000  
  
Tip

Reaching the daily limit for your current stage doesn't block your sending — emails will still go out. Hitting the full limit is simply what triggers progression to the next stage.

3

## When Does Warmup Start?

  * **For newly created domains:** Warmup is automatically enabled when the domain is created and verified. No manual action is needed.
  * **For existing domains:** Warmup must be enabled manually. When you enable warmup on an existing domain, the system automatically analyzes past email activity and Google Postmaster reputation data (if integrated).


Based on this analysis, it recommends the most suitable starting stage to ensure smooth warmup progression.

4

## Who Can Use Email Warmup and How to Enable It

Email warmup is available for both agencies and sub-accounts using dedicated domains.

Agency Domain

To enable warmup for an agency domain

  1. Go to **Agency Settings**.
  2. Click **Email Services** , then select **SMTP Service**.
  3. Go to the **Dedicated Domain and IP** tab.
  4. Choose your domain and click **Start Warmup**.


![Agency Settings menu](https://jumpshare.com/v/GtgLT0vlkO7SMjOvvRYy+/Screen+Shot+2025-06-04+at+9.14.57+PM.png)

Agency Settings → Email Services

![SMTP Service tab in Email Services](https://jumpshare.com/v/xQYgGpfk242TigRljVHz+/Screen+Shot+2025-06-04+at+9.16.10+PM.png)

SMTP Service

![Dedicated Domain and IP tab](https://jumpshare.com/v/xwz98y4gphYG34N5pdkK+/Screen+Shot+2025-06-04+at+9.17.17+PM.png)

Dedicated Domain and IP tab

Sub-Account Domain

To enable warmup for a sub-account domain

  1. Go to the **Sub-Account Settings**.
  2. Click **Email Services** , then select **SMTP Service**.
  3. Go to the **Dedicated Domain and IP** tab.
  4. Choose your domain and click **Start Warmup**.


![Sub-Account Settings menu](https://jumpshare.com/v/4ZLaiss1CirfZ2DuEKX1+/Screen+Shot+2025-06-05+at+12.18.10+AM.png)

Sub-Account Settings → Email Services

![SMTP Service tab in sub-account Email Services](https://jumpshare.com/v/XGWQq0s9hK0ZqcF2vs0v+/Screen+Shot+2025-06-05+at+12.19.40+AM.png)

SMTP Service

![Dedicated Domain and IP tab for sub-account](https://jumpshare.com/v/Ugpw2Wc5L460rKeL2ZEp+/Screen+Shot+2025-06-05+at+12.21.03+AM.png)

Dedicated Domain and IP tab

5

## Google Postmaster Integration (Recommended)

Integrating your domain with Google Postmaster Tools gives you access to key deliverability data, including:

  * Domain reputation (High, Medium, Low, Bad)
  * Spam complaint rates
  * Authentication status
  * Delivery and error metrics


If Google Postmaster is not yet connected or no data is available, the domain dashboard will notify you and guide you through setup.

6

## Best Practices for a Successful Warmup

  * Send emails consistently every day.
  * Use verified, opt-in contact lists.
  * Avoid sudden spikes in volume.
  * Avoid switching sender domains mid-campaign.
  * Respect daily warmup limits to avoid future enforcement blocks.


7

## When Is Warmup Complete?

Your domain completes warmup when it reaches Stage 15 (250,000 emails/day). At that point, you'll see a "Warmup Complete" label in the domain dashboard, and full-scale sending will be supported.

8

## Frequently Asked Questions

Q: Is domain warmup required, or can I skip it?

Warmup runs automatically on newly created domains and is strongly recommended for existing ones. Skipping it and sending at full volume immediately significantly increases the risk of spam flags, blocks, and delivery delays.

Q: What happens if I don't send emails every day during warmup?

Your domain simply stays at its current stage. Since progression only happens once the full daily limit is met, missed days just pause progress — they don't reset or penalize your stage.

Q: Can I skip ahead to a higher warmup stage manually?

No. Stages progress automatically based on daily sending volume. The only exception is when enabling warmup on an existing domain, where past activity and Google Postmaster data may place you at a higher starting stage.

Q: Does warmup apply to shared domains, or only dedicated domains?

Warmup applies to dedicated domains only, for both agencies and sub-accounts. Shared sending domains already carry an established reputation and don't go through the fixed-stage model.

Q: What happens if I connect Google Postmaster after warmup has already started?

The domain dashboard will start pulling in reputation, complaint rate, authentication, and delivery data going forward. It won't retroactively change your current stage, but it gives you better visibility for the rest of the warmup.

Q: Will my contacts notice anything different while my domain is warming up?

No. Warmup only affects the daily volume threshold your domain can send before progressing to the next stage — it doesn't change how your emails look or how they're delivered to individual recipients.

Related Articles

[Dedicated Email Sending Domains Overview & Setup](<https://help.gohighlevel.com/en/support/solutions/articles/48001226115>) [What is a Dedicated IP in LC Email?](<https://help.gohighlevel.com/en/support/solutions/articles/155000001152>) [What is LC Email?](<https://help.gohighlevel.com/en/support/solutions/articles/48001220605>) [How to Add a Domain and Verify DNS Record](<https://help.gohighlevel.com/en/support/solutions/articles/155000002220>)

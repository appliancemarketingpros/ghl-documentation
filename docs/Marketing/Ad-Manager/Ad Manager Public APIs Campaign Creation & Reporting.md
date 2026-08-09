# Ad Manager Public APIs: Campaign Creation & Reporting

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008348-ad-manager-public-apis-campaign-creation-reporting](https://help.gohighlevel.com/support/solutions/articles/155000008348-ad-manager-public-apis-campaign-creation-reporting)  
**Category:** Marketing  
**Folder:** Ad Manager

---

Developer Tools

# Ad Manager Public APIs: Campaign Creation & Reporting

Automate your advertising campaigns across Facebook, Google, and LinkedIn without touching the HighLevel interface—build, manage, and measure ads directly from your own software or workflows

What You'll Learn

This article explains HighLevel's Ad Manager Public APIs in plain language—what they do, why they matter, and how your business can use them to automate advertising at scale. Even if you're not a developer, you'll understand what's possible and how to work with your technical team to implement automated ad workflows.

You'll learn what problems these APIs solve, which advertising platforms they support, and how they let you move from manual campaign setup to fully automated, code-driven advertising operations.

Table of Contents

1

What is the Ad Manager Public API?

2

Key Benefits of Ad Manager Public APIs

3

Ad Manager API Authentication & Access

4

Campaign & Ad Creation APIs

5

Integration APIs for Facebook, Google, and LinkedIn

6

Reporting APIs

7

Supported Ad Platforms & Objects

8

How to Set Up Ad Manager Public APIs

9

Related Articles

10

Frequently Asked Questions

1

## What is the Ad Manager Public API?

Ad Manager Public APIs are a set of developer tools in HighLevel that let your software talk directly to HighLevel's Ad Manager. Instead of configuring every ad manually by clicking through the interface, your development team can write code that creates campaigns, sets budgets, chooses audiences, publishes ads, and pulls performance reports across Facebook, Google, and LinkedIn—all automatically.

These APIs work like a control panel for your advertising operations. HighLevel provides a standardized way for your systems to authenticate, connect ad accounts, launch campaigns, and retrieve cross-platform performance data without human intervention.

[Screenshot: HighLevel API 2.0 documentation with "Ad Manager" highlighted in the left navigation, showing Facebook, Google, and LinkedIn sections.]

2

## Key Benefits of Ad Manager Public APIs

Using Ad Manager Public APIs transforms how you run advertising operations. Instead of being limited to what you can manually click and configure, you can build custom automation that matches exactly how your business works.

**Unified control across all platforms** — Manage Facebook, Google, and LinkedIn ads through one consistent system rather than juggling three separate advertising dashboards with different rules and interfaces.

**Automated campaign creation at scale** — Create, update, pause, resume, and duplicate campaigns, ad sets, and ads using code so you can templatize your best-performing structures and launch them across dozens or hundreds of clients instantly.

**Programmatic account setup** — Connect and manage ad accounts automatically through code, making it easy to onboard new sub-accounts or clients without manual integration steps for each one.

**Centralized reporting across networks** — Pull impressions, clicks, spend, conversions, and other metrics in a standardized format across all platforms to build your own custom dashboards, data warehouse, or client reporting tools.

**Faster time to market** — Launch complex, multi-platform campaigns in bulk via your own applications or scripts instead of spending days manually configuring every variation through the UI.

**Scalable automation and workflows** — Combine Ad Manager APIs with your internal CRM, billing system, or onboarding tools to automatically spin up campaigns for new locations, products, or verticals with zero manual work.

3

## Ad Manager API Authentication & Access

Ad Manager APIs are part of HighLevel's API 2.0, which uses secure access tokens to confirm that your software is authorized to control your advertising accounts. Think of these tokens like digital keys—your developer gets a key from HighLevel, and then every time your software wants to create a campaign or pull a report, it shows that key to prove it has permission.

Authentication Scheme

HTTP Bearer Authentication

All Ad Manager API requests use HTTP Bearer authentication with JWT tokens. These tokens can be generated as Agency tokens (for agency-level access across multiple sub-accounts) or as Sub-Account tokens (for location-level access to one specific client).

Token Scopes & Context

Choosing the Right Token Type

Use a Sub-Account access token (or private integration token) when your service only needs to manage ads for one specific client or location. Use an Agency access token when building tooling that orchestrates campaigns across multiple sub-accounts under your agency.

Where to Find the APIs

In the HighLevel API 2.0 documentation, Ad Manager has its own module with an Introduction (Ad Manager API overview) and separate sections for Facebook Integration/Ads/Reporting, Google Integration/Ads/Reporting, and LinkedIn Integration/Ads/Reporting.

[Screenshot: API 2.0 Authorization page highlighting Bearer (JWT) authentication details.]

4

## Campaign & Ad Creation APIs

Campaign and ad creation APIs let your software build complete advertising campaigns—from the top-level campaign objective and budget down to individual ads with images and headlines—all through code. This unlocks automated campaign templating, industry-specific playbooks, and bulk management that would take days to do manually.

Key capabilities by platform:

Facebook Ads

Complete Campaign Lifecycle Management

  * Search targeting options (geo-locations, interests) to build audiences
  * Create or update campaigns, ad sets, and ads programmatically
  * Manage campaign lifecycle: pause, resume, duplicate, and delete campaigns without touching the UI
  * Manage related assets: conversion pixels and custom audiences (including batch audience member updates)


Google Ads

End-to-End Google Ads Automation

  * Publish Google Ads campaigns programmatically
  * Work with conversions, creative assets, campaigns, ad groups, and ads
  * Get targeting support: geo-location search, keyword ideas, and target interests (affinity and in-market)
  * Manage audiences: offline user list jobs, audience segments, and combined audiences


LinkedIn Ads

LinkedIn Campaign Group Operations

  * Work with ad campaign groups: create or update a campaign group (with campaigns and ads) and publish it live
  * Search targeting options such as locations, industries, and job titles
  * Handle LinkedIn lead forms (get or create)
  * Update ad status (pause or resume ads, campaigns, or ad groups)


Typical Workflow

For programmatic campaign creation, follow this pattern:

  1. Use Integration APIs to ensure the platform account is connected
  2. Use platform-specific search targeting options or keyword/interest tools to build your audience definitions
  3. Create or update a campaign object with objective, budget, and status
  4. Create or update ad sets/ad groups with targeting, placements, and scheduling
  5. Create or update ads with creatives and destination URLs
  6. Publish the campaign using the dedicated publish tools


[Screenshot: Example API flow diagram showing "Integration → Targeting → Campaign → Ad Set/Ad Group → Ad → Publish".]

5

## Integration APIs for Facebook, Google, and LinkedIn

Integration APIs give you programmatic control over how ad accounts, pages, and related assets are linked to a HighLevel sub-account. This is particularly powerful if you onboard many clients and want to standardize or automate account setup—your software can connect a new client's Facebook Page, Google Ads account, or LinkedIn profile automatically instead of walking them through manual steps.

Facebook Integration

Account & Asset Management

  * Retrieve the authenticated Facebook user for a location
  * List and manage Facebook Pages, Instagram accounts linked to a page, ad accounts, lead forms, and conversation forms
  * Create and manage the Facebook ad integration at the location level: create, retrieve, or delete Facebook integrations, set default page, and remove page connections
  * Manage lead forms, including retrieving lead form details by ID


Google & LinkedIn Integration

Platform Account Connectivity

  * **Google Integration:** Retrieve and manage Google Ads conversions, assets, audiences, and campaigns for a location
  * **LinkedIn Integration:** Work with LinkedIn ad accounts via campaign groups and lead forms, and search and apply LinkedIn targeting facets


Note

Combined with HighLevel's existing UI-based integrations for Facebook, Google, and Instagram, these APIs give you both manual and programmatic setup options.

[Screenshot: Facebook Integration endpoints list (Get current Facebook user, Get pages, Get ad accounts, Create Facebook integration, etc.) in the developer docs.]

6

## Reporting APIs

Reporting APIs provide a standardized way to pull performance metrics across Facebook, Google, and LinkedIn via HighLevel's Ad Manager rather than calling each ad network directly. This helps you centralize analytics into your own business intelligence tools, client dashboards, or automated optimization routines—so you can see all your advertising performance in one place with consistent metrics.

What the Reporting APIs support:

Aggregated Performance Metrics

Core Advertising Metrics

  * Impressions
  * Clicks
  * Spend
  * Conversions and conversion-related metrics
  * Additional performance indicators depending on the platform (e.g., cost per click, cost per acquisition, conversion rate, return on investment)


Cross-Platform Reporting Structure

Consistent Schema Across Platforms

Data is exposed via Ad Manager's reporting endpoints per platform (e.g., Google Reporting "Get reporting data" and "Get reporting list"). Your application can normalize this into your own schema if you want a unified "campaign performance" model.

Example: Google Reporting Endpoints

Three Main Reporting Calls

  * **Get reporting data:** Aggregated Google Ads metrics for a location
  * **Get reporting list:** Campaigns and ad groups with summary stats
  * **Get campaign reporting:** Detailed reporting for one campaign


Note

While exact fields vary by platform, you can generally expect core performance metrics such as impressions, clicks, spend, and conversion-related metrics that align with what you see in native ad managers and Ad Manager reporting. Facebook and LinkedIn Reporting APIs follow a similar pattern to Google.

[Screenshot: Snippet of the Google Reporting section in the Ad Manager API docs, showing Get reporting data, Get reporting list, and Get campaign reporting.]

7

## Supported Ad Platforms & Objects

Ad Manager APIs are designed to abstract away some of the complexity of each ad network while still giving you access to the key building blocks you need for serious media buying.

Platform| Objects| Operations  
---|---|---  
Facebook / Instagram| 

  * Campaigns, ad sets, ads
  * Custom audiences, conversion pixels
  * Pages, lead forms, conversation forms

| 

  * Search targeting options
  * Create or update campaigns, ad sets, and ads
  * Pause, resume, duplicate, and delete
  * Manage audiences and pixels
  * Publish campaigns

  
Google Ads| 

  * Campaigns, ad groups, ads
  * Conversions & conversion goals
  * Assets (creatives), audience segments, combined audiences

| 

  * Publish ads and campaigns
  * Search geo-targets and keyword ideas
  * Manage conversions, assets, and audiences
  * Retrieve reporting metrics

  
LinkedIn Ads| 

  * Ad campaign groups (with campaigns and ads)
  * Lead forms

| 

  * Publish campaign groups
  * Search targeting facets (location, industry, job title)
  * Pause or resume ads, campaigns, or ad groups
  * Create or retrieve lead forms

  
  
Implementation Guide

Ready to automate your advertising workflows?

Follow the setup guide below to connect your development environment to Ad Manager Public APIs

8

## How to Set Up Ad Manager Public APIs

Setting up Ad Manager Public APIs involves enabling Ad Manager for the relevant sub-accounts, configuring authentication, and then wiring your own application or integration to call the endpoints you need. Treat this as a high-level implementation guide that your developers can tailor to your specific technical stack.

Step 1

Confirm Ad Manager is enabled in your account

  1. Log in to HighLevel as an Agency user.
  2. Confirm that the relevant Sub-Accounts have access to Ad Manager in the UI.
  3. If you are rolling this out across many client locations, decide which locations should be managed programmatically versus purely through the UI.


[Screenshot: Sub-Account view in HighLevel with Ad Manager module visible in the left navigation.]

Step 2

Set up API access (HighLevel API 2.0)

  1. In your Agency account, generate an API token (or private integration token) following the HighLevel API 2.0 guidelines.
  2. Decide whether your integration will use Sub-Account tokens to act on behalf of one location at a time, or use an Agency token when orchestrating across multiple sub-accounts.
  3. Store the token securely in your backend (e.g., environment variables or secret manager).
  4. Have your developers configure your API client to set the Authorization: Bearer token header on each request and use the Ad Manager endpoints documented under the Ad Manager module.


[Screenshot: API 2.0 Authorization page highlighting Bearer (JWT) authentication details.]

Step 3

Connect ad accounts using Integration APIs or the UI

For each sub-account, ensure your Facebook, Google, and LinkedIn ad accounts are connected:

  * Use the existing UI integrations for a quick one-off setup (e.g., Facebook/Instagram integration, Google Ads integration).
  * Or use Integration APIs: Facebook Integration (create, retrieve, or delete integrations; manage pages and ad accounts); Google Ads and LinkedIn Ads (ensure the platform accounts and permissions are in place for the sub-account).
  * Verify via API: Call the appropriate retrieval endpoints (e.g., Get Facebook pages, Get ad accounts, Get conversions) to confirm the integration is active.


[Screenshot: Facebook Integration setup screen in HighLevel showing connected pages and ad accounts.]

Step 4

Build and test your first API call

  1. Start with a simple retrieval endpoint (e.g., Get Facebook pages or Get Google conversions) to verify authentication is working.
  2. Use Postman, curl, or your programming language's HTTP client to make the request with your Bearer token.
  3. Review the response and confirm you're receiving expected data.
  4. Once basic calls work, move on to more complex operations like campaign creation or reporting data retrieval.


Step 5

Implement your automation workflows

With authentication and integration verified, your developers can now build the specific workflows your business needs:

  * Campaign creation automation (using the Campaign & Ad Creation APIs)
  * Scheduled reporting pulls (using the Reporting APIs)
  * Bulk campaign management (pause, resume, budget updates)
  * Custom dashboards or client portals that display aggregated ad performance


Important

Refer to the official HighLevel API 2.0 documentation for detailed endpoint specifications, request/response schemas, rate limits, and error handling guidelines. The Ad Manager module documentation provides comprehensive details for every available endpoint across Facebook, Google, and LinkedIn integrations.

9

## Related Articles

→ How to Connect Facebook Ads to HighLevel  → How to Connect Google Ads to HighLevel  → Understanding HighLevel API 2.0 Authentication  → Ad Manager: Overview and Getting Started 

10

## Frequently Asked Questions

Do I need to be a developer to use Ad Manager Public APIs?

Yes. APIs are developer tools that require writing code to interact with HighLevel's systems. However, you don't need to be a developer yourself—you can hire a developer, work with your technical team, or partner with a HighLevel-certified agency that builds custom integrations.

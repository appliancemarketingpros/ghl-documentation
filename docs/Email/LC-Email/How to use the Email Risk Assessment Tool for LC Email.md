# How to use the Email Risk Assessment Tool for LC Email

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000000577-how-to-use-the-email-risk-assessment-tool-for-lc-email](https://help.gohighlevel.com/support/solutions/articles/155000000577-how-to-use-the-email-risk-assessment-tool-for-lc-email)  
**Category:** Email  
**Folder:** LC Email

---

Email Deliverability

Risk Assessment

Analyze your imported contact list for email deliverability risks and reduce bounce rates using Bulk Verification technology.

Overview

The Risk Assessment feature is designed to optimize your email marketing campaigns. Harnessing the power of Bulk Verification, it analyzes your imported contact list and offers detailed insights into deliverability and risk levels.

Elevate your email strategy by minimizing bounce rates, reducing unnecessary sending blocks, and improving the overall deliverability of your campaigns.

Please Note

**For LC Email Users:** The bulk email verification feature is exclusively available to LC Email users.

**For the Agency:** This feature is designed for agency use and applies to locations within the LC Email system.

Table of Contents

1

What is this Feature?

2

Risk Categories

3

Usage Cases

4

How to Use This Feature

5

Risk Assessment Tab

6

FAQs

Video Walkthrough

1

## What is this Feature?

The Risk Assessment feature is an invaluable tool for email marketing. It scrutinizes your imported contact list and provides a comprehensive overview of email deliverability and potential risks.

It uses internal Bulk Verification technology to analyze the email list, dividing addresses into categories such as **deliverable** , **undeliverable** , **catch-all** , and **unknown**. It further segments these by risk level: **high** , **medium** , **low** , and **unknown** — giving you a granular picture of your contact list's deliverability prospects.

Beyond surfacing data, it enhances your email strategy by helping reduce bounce rates and unnecessary blocks on your sending capabilities. It also prompts enabling the email verification feature for those not yet using it.

In short, this feature is your strategic partner in optimizing the deliverability and effectiveness of your email marketing campaigns — helping you reach your audience more consistently and efficiently.

2

## Risk Categories

Each email address in your imported list is assigned one of the following risk categories based on its deliverability assessment:

Risk Category| Description  
---|---  
High| Email addresses in this category are highly likely to be undeliverable. This could be because the email account is non-existent, the domain has no MX records, or the recipient's mailbox is full.  
Medium| Email addresses in this category may or may not be deliverable. This could be because the server responded ambiguously, the domain was identified as a catch-all, or the address was generated randomly.  
Low| Email addresses in this category are likely to be deliverable. The server responded positively to the verification request, and the address appears properly structured and associated with a legitimate domain.  
Unknown| Email addresses in this category could not be verified due to unforeseen errors or temporary issues with the recipient's email server. Deliverability remains uncertain unless re-verified later.  
  
3

## Usage Cases

Bulk email verification is a powerful tool for businesses and organizations of all sizes. Here are the most common scenarios where it delivers value:

Use Case 1

Email Marketing Campaigns

Sending newsletters or promotions to unverified lists leads to high bounce rates and damages sender reputation. Bulk verification cleans your list so you reliably reach your intended audience.

Use Case 2

User Registration Verification

Users often make typos, use non-existent addresses, or provide fake emails during sign-up. Bulk verification validates these before they enter your database, ensuring you can communicate effectively with your users.

Use Case 3

CRM Data Cleaning

CRM records grow stale as people change jobs, email addresses, or abandon old accounts. Regularly verifying in bulk keeps your CRM data current and actionable.

Use Case 4

E-commerce Platforms

Online retailers depend on transactional emails (order confirmations, shipping updates) and marketing emails reaching customers. Verification ensures these critical communications land in inboxes.

Use Case 5

Community Updates

Non-profit organizations, clubs, and communities that send regular member updates use bulk verification to ensure information reaches all intended recipients without bouncing.

Use Case 6

Education Institutes

Universities, colleges, and schools communicating fee updates, event announcements, or educational materials must ensure these reach valid addresses — especially when communications are time-sensitive.

Use Case 7

Research and Surveys

Researchers and companies distributing surveys via email need valid addresses to collect accurate and reliable responses. Verification prevents wasted sends and skewed data.

Use Case 8

Job Portals and Recruitment Companies

Recruitment platforms sending job notifications, interview schedules, and updates to job seekers and employers rely on bulk verification to maintain effective and reliable communication.

4

## How to Use This Feature

Upon importing a CSV to the CRM, if your sub-account is on the LC Email SMTP and you have not yet enabled the individual Email Verification feature, the imported CSV will be analyzed automatically in the background.

A popup will appear and an email will be sent to sub-account team members with the risk analysis of that import's email addresses. Both the popup and the email encourage users to enable Email Verification.

Example Email

Body of the Email That Will Be Sent (Example Data)

**Subject:** Email content for list of high risk

* * *

Hi [sub-account Friendly Business Name],

We scanned your latest Contact Import and found the following with the email addresses:

**Deliverable:** 71.84%

**High Risk:** 17.81%

Activating native email verification can eliminate potential risks by ensuring that you don't send to non-valid email addresses. Once activated, the system will not attempt to send to any email address marked as invalid.

Support article link: _[support article link here]_

If you have any further questions or need assistance managing your email list, please feel free to contact our support team using the blue check mark in-app. We are here to help!

Best regards,

[Agency Admin Name]

[Agency Company Name]

Tip

Enabling native email verification as prompted will prevent the system from attempting to send to any address flagged as invalid — protecting your sender reputation proactively.

5

## Risk Assessment Tab

The Risk Assessment tab at **Settings → Email Services → Risk Assessment** keeps a historical record of all imports and their email address risk assessments.

![Risk Assessment tab in Settings showing historical import data with deliverable, undeliverable, and unknown percentages](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031509099/original/vzPwf3ZKSHgnOLALFrGJ9Brchc7OrY_Vgg.jpg?1724335549)

Settings → Email Services → Risk Assessment

Here's a breakdown of each field in the interface:

Records

Shows how many bulk email verification records or jobs are currently displayed.

Date Range

The date range at the top indicates the time frame for the verification records shown.

Import Name

Lists the name of each verification job, fetched from the Bulk Import action in Bulk Actions. Each name should be unique to help you identify and track individual jobs.

Created At

The exact date and time each job was created, formatted as "Day Month Date Year Time Zone."

No. of Emails

The total number of email addresses included in the job for verification.

Deliverable (%)

The percentage of email addresses in the job verified and found to be deliverable or valid.

Undeliverable (%)

The percentage of email addresses verified and found to be undeliverable or invalid.

Unknown (%)

The percentage of email addresses that could not be conclusively verified — their deliverability status remains unknown.

Pagination

If more records exist than fit on a single page, use the pagination controls at the bottom to navigate between pages.

6

## FAQs

Q: What does the Deliverable percentage in the Risk Assessment tab mean?

The Deliverable percentage indicates the proportion of email addresses verified and found valid and reachable. It is calculated by dividing the number of deliverable addresses by the total in the job, then multiplying by 100.

Q: How is the Undeliverable percentage calculated?

The Undeliverable percentage represents the proportion of addresses found invalid or unreachable. It is determined by dividing the number of undeliverable addresses by the total in the job, then multiplying by 100.

Q: What does the Unknown percentage signify?

The Unknown percentage shows the proportion of addresses that could not be definitively verified — their deliverability status is unclear. Calculated by dividing the number of unknown emails by the total in the job, then multiplying by 100.

Q: What is the "Import Name" in the Risk Assessment tab?

The "Import Name" is a unique identifier for each batch of email addresses submitted for verification. It lets you track and manage each verification job separately.

Q: Why might the date and time in the "Created At" column be important?

The timestamp helps you understand when each job was initiated, which is useful for tracking progress over time or determining the order in which jobs were processed.

Q: Why isn't every email verified?

Not all email addresses can be verified due to server restrictions, privacy settings, or network issues. These are categorized as "Unknown."

Q: What happens if the email server doesn't respond in time?

If the server doesn't respond in a timely manner, the verification system categorizes the address as "Unknown." Deliverability could not be determined in that instance.

Q: What should I do if I see many "Unknown" email addresses in my list?

Many "Unknown" results may indicate server issues or technical problems. Consider re-running the verification at a later time. If the issue persists, contact Support — email address formatting or CSV format issues could also be contributing.

Q: What should be the next step after getting the Risk Assessment report?

Consider removing or re-checking "Undeliverable" and "Unknown" email addresses before running any campaign. This improves your deliverability rate and overall campaign effectiveness.

Q: What does "No. of Emails" mean in the Risk Assessment tab?

It represents the total count of email addresses included in a particular batch for verification, giving you an idea of the scale of each job.

Q: Why do different jobs have different Deliverable, Undeliverable, and Unknown percentages?

Percentages vary based on the quality of addresses in each batch. A batch with older or outdated emails will typically have a higher Undeliverable percentage than one with recently collected addresses.

Q: What can I do to improve my Deliverable percentage?

Collect email addresses from reliable sources, update your lists regularly, and use double opt-in methods to ensure addresses belong to people genuinely interested in receiving your communications.

Q: Why are some emails marked Deliverable but still bounce?

Deliverable emails can still bounce due to a full recipient mailbox, a temporarily unavailable mail server, or the email being marked as spam by the recipient's email service.

Q: Can I re-run email verification for a specific batch?

Yes. Re-running is particularly helpful when a significant percentage of emails were marked Unknown, which may have been caused by temporary server issues at the time of the original run.

Q: How often should I verify my email lists?

Verification frequency depends on factors like list growth and bounce rates. As a best practice, verify your list before any significant email campaign.

Q: How does email verification impact my overall email marketing strategy?

Email verification is crucial for a healthy email marketing strategy. It helps remove invalid or undeliverable emails, improving deliverability rates, protecting sender reputation, and increasing campaign effectiveness.

Q: Does the verification process respect user privacy?

Yes. The verification process does not access the contents of any email — it only checks whether an address is valid and capable of receiving emails.

Q: Is the email verification process secure?

Yes. Data submitted for verification is processed over secure connections and handled according to the service provider's data handling and privacy policies.

More Tutorials from the Community

<https://youtu.be/PPOjAKKAuZ8> <https://youtu.be/uGPWGV8uTmc> [https://youtu.be/Lqr1UHQ_siU](<https://youtu.be/Lqr1UHQ_siU?si=s-SkA7pNrvjH8X9T>) <https://youtu.be/NdUf2_PInRU> <https://youtu.be/w_3xVNpX3-Q> <https://www.youtube.com/watch?v=FxHkDr1sJmY>

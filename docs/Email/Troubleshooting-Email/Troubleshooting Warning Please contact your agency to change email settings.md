# Troubleshooting Warning: Please contact your agency to change email settings

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001207525-troubleshooting-warning-please-contact-your-agency-to-change-email-settings](https://help.gohighlevel.com/support/solutions/articles/48001207525-troubleshooting-warning-please-contact-your-agency-to-change-email-settings)  
**Category:** Email  
**Folder:** Troubleshooting Email

---

Billing & Usage

SMTP Provider Error & Email Rebilling Settings

Understand the SMTP provider error tied to Email Reselling, and learn how to disable Email Rebilling for a sub-account.

Overview

If you see an error when adding an SMTP provider, it's usually tied to the sub-account's Email Reselling setting. This article covers that error and walks through how to disable Email Rebilling for a sub-account.

Table of Contents

1

The Error

2

How to Disable Email Rebilling

3

FAQ

1

## The Error

![SMTP provider error message](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48180856684/original/hnm15p3rph-EYFQ09-2Ix_UBaxPdERt3RQ.png?1642631121)

If you're trying to add an SMTP provider and this error message shows up, check whether **Email Reselling** is enabled for the location in the agency's SaaS configurator page.

Video Walkthrough

2

## How to Disable Email Rebilling

Step 1

Go to [app.gohighlevel.com/sub-accounts/](<https://app.gohighlevel.com/sub-accounts/>).

Step 2

Once in agency view, click **Sub-Accounts** and search for the sub-account.

![Searching for a sub-account](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48280512342/original/R86QkuQrkReIza2aG45_43Rzv42ujoCqJw.png?1675884865)

Step 3

Once you locate the sub-account, click the sub-account name **or** click the three dots at the bottom right to **Manage Client**.

![Manage Client option for a sub-account](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48280512511/original/yKwzD5ifdBAzF08vPBIyCgt0wdU7aEv3qA.png?1675884922)

Step 4

Scroll all the way down to **Email Resell Settings** and toggle the highlighted button to disable Email Rebilling.

![Email Resell Settings toggle](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48280512843/original/-QsFDNwIZh47kMExMGYCprVoBDWbaDWhjQ.png?1675885077)

3

## FAQ

Q: What is Email Reselling, and why does it block adding an SMTP provider?

Email Reselling controls whether a sub-account's email usage is billed through the agency's rebilling setup. Some SMTP integrations require this setting to be enabled first so usage and billing line up correctly.

Q: Where do I enable Email Reselling if it's currently off?

From the agency's SaaS configurator page, find the location in question and turn on the email reselling option before attempting to add the SMTP provider again.

Q: Will disabling Email Rebilling affect a sub-account that's already sending email?

Disabling it stops that sub-account's email usage from being rebilled through your agency's markup. Confirm with the client how they'll be billed going forward before turning it off.

Q: Can I re-enable Email Rebilling later if I change my mind?

Yes — the toggle in Email Resell Settings can be switched back on the same way it was turned off, from the sub-account's Manage Client screen.

Q: Does this setting apply per sub-account, or across the whole agency?

It's per sub-account. You'll need to repeat Steps 1–4 for each sub-account where you want to enable or disable Email Rebilling.

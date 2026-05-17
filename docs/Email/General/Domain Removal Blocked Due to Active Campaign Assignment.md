# Domain Removal Blocked Due to Active Campaign Assignment

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007956-domain-removal-blocked-due-to-active-campaign-assignment](https://help.gohighlevel.com/support/solutions/articles/155000007956-domain-removal-blocked-due-to-active-campaign-assignment)  
**Category:** Email  
**Folder:** General

---

Email Infrastructure

How to Unlink a Domain From Active Campaigns Before Deleting It

Step-by-step guide to safely remove a domain that’s still tied to scheduled campaigns — without breaking anything in-flight.

What You'll Learn

If you’re trying to delete a domain from your system but get an error saying it’s still linked to an active campaign, don’t worry.

This guide walks you through unlinking the domain from every campaign it’s tied to, so you can remove it cleanly — without affecting deliverability or any campaign that’s currently sending.

Table of Contents

1

Try deleting the domain

2

Go to the Domain Configurator

3

Open Manage Campaign

4

Unlink the domain from all campaigns

5

Apply the changes

6

Double-check campaign links

7

Delete the domain

Video Walkthrough

Setup Guide

Step-by-step: Unlink, then delete

Follow these seven steps in order. The whole process takes under two minutes.

1

## Try deleting the domain

Click **Delete Domain** for the domain you want to remove. If the domain is tied to a campaign, you’ll see an alert letting you know it can’t be deleted yet.

Error Message

“The domain is currently assigned to a scheduled Campaign Domain (except test campaign). Try again after the campaign has finished sending, or remove the domain from the Campaign Domain (except test campaign).”

![Delete Domain error message showing the domain is assigned to a scheduled campaign](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071399076/original/ou5GxUe-HSeYGYMsNzMxOMVN67COIpRQtg.png?1778837888)

2

## Go to the Domain Configurator

Open the **Domain Configurator** option in your menu. Find and select the domain that’s causing the deletion error.

![Domain Configurator menu with the affected domain selected](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071399074/original/ibaLnXWTTrx3yth6AheBvbS43VM9lT1bqw.png?1778837888)

3

## Open Manage Campaign

Click **Manage Campaign** for that domain to view all campaigns currently linked to it.

![Manage Campaign view listing every campaign tied to the domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071399073/original/xnbim5hW5xrmd-YxScCiXsgW7HejpBacEw.png?1778837888)

4

## Unlink the domain from all campaigns

Select all campaigns associated with the domain, then use the **Remove** option to unlink your domain from every campaign in the list.

Heads Up

Make sure to remove the domain from **every** campaign shown — missing even one will block the delete in the next step.

![Selecting all campaigns and clicking Remove to unlink the domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071399075/original/4qSVR5XKs1rLglOOsLrq9_V8ZNlYqOpLFQ.png?1778837888)

5

## Apply the changes

Click **Apply** to confirm the removal. The system will save the unlinked state across all selected campaigns.

6

## Double-check campaign links

Go back to **Manage Campaign** to confirm no campaigns are linked. The list should now be completely blank.

![Manage Campaign list now empty, confirming all campaigns are unlinked](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071399077/original/GT7mXB1R2wxijElCPVbJbcp893G6BapOBQ.png?1778837888)

7

## Delete the domain

Return to the main domain list. This time, you’ll see the option to delete the domain. Enter the required confirmation text (such as “delete”) and click **Delete**.

You're All Set

The domain is now fully removed. Unlinking before deletion prevents accidental data loss and keeps your active campaigns running smoothly.

![Final domain delete confirmation with the required confirmation text entered](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071399078/original/x2-z4yMCikeLBjVslGJxJuIFnuToThmFAg.png?1778837889)

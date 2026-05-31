# Preference Management (Email Unsubscription Management)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007291-preference-management-email-unsubscription-management-](https://help.gohighlevel.com/support/solutions/articles/155000007291-preference-management-email-unsubscription-management-)  
**Category:** Email  
**Folder:** Deliverability

---

Email Compliance

# Preference Management

Give contacts control over the types of marketing emails they want. Preference Management lets each location create subscription categories, link them to campaigns, and automatically honor opt-outs at a category level.

Currently a Labs Feature — Enable Before Use

Enable the following toggle from **Agency Settings → Labs** for all or specific sub-accounts:

**Preference Management** _(Required)_

**Important:** Preference Management is **irreversible** once enabled. Because it introduces location-level unsubscribe controls, this change **cannot be undone** after activation.

No Default Categories

For new configurations, HighLevel does **not** add a default "One-on-One" subscription type. Create the categories that fit your email program. Category names can be edited after creation and support up to **100 characters**.

Table of Contents

  1. 1What is Preference Management?
  2. 2Key Benefits of Preference Management
  3. 3Preference Types
  4. 4Associating Preferences with Campaigns
  5. 5Automatic Audience Filtering
  6. 6How to Setup Preference Management
  7. 7Managing Preferences at the Contact Level
  8. 8Frequently Asked Questions
  9. 9Related Articles


## What is Preference Management?

Preference Management helps businesses stay compliant by honoring each contact's communication choices — both whether they want to receive emails, and what types of emails they prefer to receive. This reduces unwanted outreach, minimizes the risk of being marked as spam, and supports healthier email deliverability.

With Preference Management, each location can create and manage custom communication (preference) categories that align with its marketing needs. These categories can be linked directly to campaigns, enabling the system to automatically respect every contact's stated preferences.

When a contact opts out of a specific preference type, any future campaigns assigned to that category will automatically exclude them — even if they were part of the original campaign audience. This ensures more relevant messaging, stronger compliance, and a more personalized experience for every contact.

## Key Benefits of Preference Management

Compliance-First Communication

Automatically uphold opt-out decisions at a category level so every send respects contact choices.

Healthier Email Deliverability

Reduce spam complaints and unwanted messages, protecting your sender reputation over time.

Personalized Engagement

Send more relevant content aligned with stated contact preferences — not everyone wants every email.

Location-Level Customization

Each location defines its own communication categories based on its specific marketing strategy.

## Preference Types

Preference Types are the granular categories that are the foundation of Preference Management. Create as many as you need to reflect the distinct themes of your email program (e.g., Newsletters, Promotions, Event Updates).

These categories live under **Settings → Preference Management Hub** and can be edited, disabled, or deleted at any time.

For step-by-step instructions on creating Preference Types, jump to How to Setup Preference Management.

## Associating Preferences with Campaigns

Linking a campaign to a preference category tells the system **"why"** you're emailing. This allows HighLevel to filter audiences based on contact choices before delivery.

When a contact opts out of a category, they are automatically kept out of current and future sends for that category — even if the contact is still on your static list.

For instructions on linking preferences to a campaign, see Step 2: Assign Preferences to Campaigns.

## Automatic Audience Filtering

If a contact has opted out of a specific preference type, they will be automatically excluded from any campaign assigned to that category — even if they were originally included in the campaign audience. This ensures accurate targeting and prevents unwanted emails from being sent.

Once preferences are set, the system will:

Auto-Exclude Conflicts

Automatically remove contacts from campaigns that conflict with their stated preferences.

Enforce Category Opt-Outs

Honor category-level opt-outs even if the contact appears in the original campaign audience.

## How to Setup Preference Management

Step 1

Create Preference Types

Preference Types are the subscription categories used to label your email programs — such as newsletters, promotions, or event updates.

1

### Go to the Preference Management Hub

Navigate to **Settings → Preference Management Hub** at the location level.

* * *

2

### Create a Subscription Type

Click **\+ Create Subscription Type**.

![Create Subscription Type button in Preference Management Hub](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069370539/original/PDDXKYVeUCSICwiwZsTVGef5blmdYKYbIg.jpeg?1776423230)

* * *

3

### Enter the Subscription Name & Description

Enter a **Subscription Name** and **Description** for the category you want to use.

![Subscription Name and Description fields](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069370639/original/AMUNhi9OqkkPc4J7FmVZs4_K_eeQmsf0sQ.jpeg?1776423253)

* * *

4

### Use a Clear, Descriptive Name

Pick a name that recipients will understand. Subscription category names support up to **100 characters**.

* * *

5

### Save & Confirm

Save your changes and confirm the action when prompted.

* * *

6

### Repeat for Each Category

Repeat this process for each preference category you want to use.

Step 2

Assign Preferences to Campaigns

Assign a preference category to an email campaign from within the Email Builder. This enables the system to understand why the message is being sent and who should receive it.

1

### Open the Email Campaign

Open the Email Campaign you want to assign a Subscription Type to, then click **Send or Schedule**.

![Send or Schedule button in Email Builder](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063104565/original/9l87fXiGITv6B3IjFHwWi7tcGJMHSigQVg.png?1768940148)

* * *

2

### Select the Preference Type

Choose your desired **Preference Type** using the dropdown.

![Preference Type dropdown selection](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063104691/original/hbud_C6l1m-8DaK8ssIBg_KSlZolm-tGww.png?1768940415)

## Managing Preferences at the Contact Level

From the Contact Details Page, teams can view or manually adjust each contact's preferences for full transparency and control. To view or update preference settings for a contact, follow the steps below.

**Note:** When a preference status is updated at the contact level, HighLevel logs the update in Conversations so teams can review preference changes in context.

  


1

### Open the Contact's Subscription Status

Go to **Contacts** and select a contact. From the contact page, open the **DND** tab and click **Subscription Status**.

![Subscription Status option under DND tab](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063105524/original/xze7RqTAwaecNeurxEuUu9hORwD7JlmqWQ.png?1768942404)

* * *

2

### Set Each Preference Type

In the **Manage Email Subscriptions** popup, set each Preference Type to **Subscribed** or **Unsubscribed** as appropriate.

![Manage Email Subscriptions popup](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063105550/original/pwS5GCiH_5kST2ghuW_Dxvs05UkxYlsQnw.png?1768942495)

* * *

3

### Provide a Legal Basis to Resubscribe

For any preference category marked as **Unsubscribed** , the location **must provide a legal basis** before the contact can be resubscribed.

![Legal basis required to resubscribe a contact](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063105568/original/aHL8BCQPt9iodTMcK-8CYhGLIJ0BNuqOVQ.png?1768942528)

## Frequently Asked Questions

How does category opt-out relate to global unsubscribe?

Category opt-out suppresses only the selected topics. A **global unsubscribe** opts the user out from all marketing email from the location.

Can contacts manage their own preferences?

Yes. When Preference Management is enabled, the unsubscribe link includes a **"Manage your preferences"** link where contacts can manage their own category-level choices directly.

Do emails sent from workflows honor category preferences?

Yes. Automatic filtering removes contacts whose preferences conflict with the campaign's categories — regardless of how they were added to the audience.

What happens if all preference types are archived?

When all preference types are archived, Preference Management shows a guided **zero-state message** instead of an empty view — prompting you to create or restore a category.

Can Preference Management be turned off after enabling it?

**No.** Preference Management is irreversible once enabled. Because it introduces location-level unsubscribe controls, activation cannot be undone. Enable it only when you're ready to commit.

Is there a limit on how many Preference Types I can create?

Create as many categories as your email program requires. Subscription category names support up to **100 characters** and can be edited after creation.

## Related Articles

[Email Sending Guide: Best Practices & Warm Up](<https://help.gohighlevel.com/en/support/solutions/articles/155000001021>) [Managing Default Unsubscribe Links in LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001225534>) [Creating and Managing Custom Unsubscribe Links](<https://help.gohighlevel.com/en/support/solutions/articles/155000004799>) [How to Create & Manage Smart Lists](<https://help.gohighlevel.com/en/support/solutions/articles/48001062094>)

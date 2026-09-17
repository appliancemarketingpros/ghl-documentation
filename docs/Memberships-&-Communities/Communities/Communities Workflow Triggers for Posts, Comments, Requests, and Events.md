# Communities Workflow Triggers for Posts, Comments, Requests, and Events

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008289-communities-workflow-triggers-for-posts-comments-requests-and-events](https://help.gohighlevel.com/support/solutions/articles/155000008289-communities-workflow-triggers-for-posts-comments-requests-and-events)  
**Category:** Memberships & Communities  
**Folder:** Communities

---

[](<https://help.gohighlevel.com/en/support/solutions/articles/155000008289>)Communities Workflow Triggers for Member Activity

Automate moderation, engagement, and event follow-up with four workflow triggers that respond to real-time group activity—join request rejections, posts, comments, and event registrations.

What You'll Learn

This guide explains how to use four Communities workflow triggers that fire when key actions happen inside your HighLevel Communities groups—such as join requests being rejected, posts or comments being created, or members registering for group events.

You'll learn what each trigger does, how to configure filters for smarter targeting, and how to set up complete automation flows inside Workflows to automate moderation, engagement, and event follow-up at scale.

Table of Contents

1

What is Communities Workflow Automation for Member Activity?

2

Key Benefits of Communities Workflow Triggers

3

Group Joining Request Rejected

4

Group Post Created

5

Group Comment Created

6

Member Registered for Group Event

7

How to Setup Communities Workflow Triggers

8

Related Articles

9

Frequently Asked Questions

1

## What is Communities Workflow Automation for Member Activity?

Communities Workflow Automation for member activity refers to a set of workflow triggers that fire when key actions happen inside your HighLevel Communities groups—such as join requests being rejected, posts or comments being created, or members registering for group events. These triggers let you connect everyday activity in your groups directly to workflows so you can send alerts, follow up, and track engagement automatically.

HighLevel supports a broad library of workflow triggers across CRM, payments, and communities, all managed inside the Workflow Builder. These Communities triggers provide deeper coverage so your groups can benefit from the same level of automation as the rest of your account.

2

## Key Benefits of Communities Workflow Triggers

These Communities triggers are designed to turn what members do inside groups into timely, targeted automation.

**More automation possibilities** — Automatically start workflows from key group events—rejected join requests, new posts, new comments, and event registrations—without manual checks or exports.

**Smarter targeting with filters** — Use filters like Group, Channel, Post Title, Post Content, Comment Content, and Event Title so workflows only run when the activity is actually relevant.

**Faster moderation and visibility** — Alert moderators when concerning posts or comments are created, notify account managers when VIPs engage, or route sensitive activity to a private review channel.

**Less manual effort as communities grow** — Replace manual outreach, tagging, and follow-up tasks with standardized, automated flows that scale with your member base.

**Stronger Communities + Workflows connection** — Combine these triggers with existing Communities triggers such as Group Access Granted, Group Access Revoked, and leaderboard-based triggers to build full-lifecycle journeys from first access through ongoing engagement and gamification.

3

## Group Joining Request Rejected

Group Joining Request Rejected is a Communities workflow trigger that fires when a member's request to join a specific group is rejected. It helps you keep rejected applicants on a structured follow-up path—whether that's sending a polite decline, offering alternative resources, or notifying an internal team.

When to use it:

  * You want to send an automatic, friendly "declined" message explaining next steps.
  * You need to log rejected requests in your CRM for future outreach or reporting.
  * Moderators or sales reps should be notified when high-value applicants are rejected.


Trigger behavior

**Event:** A join request for a community group is rejected.

**Required filter:** Group – You must specify which group(s) the trigger applies to.

**Typical actions downstream:**

  * Send an email or DM explaining why access was declined and how to qualify.
  * Create a task for a team member to review the application.
  * Apply tags (e.g., "Community – Join Request Rejected") for segmentation.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077055813/original/gJwNqLkmN3BPhs7S9M0rioekZjGNoH6bmQ.png?1785253202)

4

## Group Post Created

Group Post Created lets you trigger a workflow every time someone publishes a new post in a specified community group. This is ideal for automating engagement, routing important content, or moderating posts that match specific criteria.

This trigger focuses on top-level posts, not comments, and is especially powerful when combined with filters on channel and content.

Trigger behavior

**Event:** A new post is created in a community group.

**Filters:**

  * Group (required) – Target specific group(s).
  * Channel – Limit to a specific channel (e.g., Announcements, Q&A).
  * Post Title – Match posts based on the title (e.g., contains "Launch").
  * Post Content – Match posts based on body content (e.g., contains "refund", "support", or keywords you watch for).


Use case ideas

  * Auto-reply with guidance when someone posts a "Help" or "Support" question.
  * Notify your team via email/Slack when a VIP or partner publishes in a key channel.
  * Start a nurture workflow when someone posts an introduction in a "Welcome" channel.
  * Flag posts containing specific keywords for moderation review.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077055880/original/G11CSrV0Cc_zzWcwJfqY3mRCVnYmkJKFAA.png?1785253245)

5

## Group Comment Created

Group Comment Created fires when someone adds a comment to an existing group post. This trigger is perfect for deep engagement tracking—catching replies, questions, or red-flag comments that might otherwise be missed in busy threads.

It gives you the same context as Group Post Created, plus the exact comment content.

Trigger behavior

**Event:** A new comment is added to a post in a community group.

**Filters:**

  * Group (required) – Limit to one or more groups.
  * Channel – Narrow down to specific channels.
  * Post Title – Fire only on comments made under posts matching certain titles.
  * Post Content – Filter on the original post's content.
  * Comment Content – Filter based on what's written in the comment (e.g., "cancel", "refund", "issue", profanity, or other keywords).


Use case ideas

  * Auto-open a support ticket when a comment includes escalation keywords.
  * Alert an account manager when a high-value client leaves a question on a post.
  * Award gamification points or send kudos when members give helpful answers.
  * Route potentially harmful or policy-violating comments for moderator review.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077055967/original/XPkByHs-Wgx1ony27J-GB34DBpwPRZvRng.png?1785253280)

## Member Registered for Group Event

Member Registered for Group Event lets you start workflows when someone registers for an event attached to a specific community group. This gives you a clean automation hook for reminders, follow-ups, and post-event nurturing.

Trigger behavior

**Event:** A member registers for a group event.

**Filters:**

  * Group (required) – Choose the group hosting the event.
  * Event Title – Target one event or a group of events by name pattern (e.g., "Monthly Q&A").


Use case ideas

  * Send a confirmation sequence with calendar links and prep materials.
  * Add registrants to a follow-up campaign that sends replays and upsell offers.
  * Notify hosts when VIPs or certain segments register.
  * Automatically tag contacts by the type of event they registered for (e.g., "Webinar – Product Demo Attendee").


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077056117/original/ZReZnapGPG016hed2aCx80NhHCehhuasZA.png?1785253351)

dy to Automate?

Setting Up Communities Workflow Triggers

Follow these steps to configure any of the four Communities triggers and start building automated engagement flows.

7

## How to Setup Communities Workflow Triggers

Configuring these Communities triggers follows the same pattern as other workflow triggers in HighLevel—choose the trigger, add filters, then define the actions you want to run. Understanding this pattern helps you build consistent automation across your account.

Step 1

Open the Workflow Builder

  * Go to **Automation > Workflows** in your HighLevel location.
  * Click **Create Workflow** (or open an existing workflow where you want to add a Communities trigger).


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077056407/original/vVAwf63pyxNGsd8gMhSzuLUxU_2wISCvpw.png?1785253438)

Add a Communities Trigger

  * In the workflow canvas, click **Add New Trigger**.
  * In the trigger list, locate the **Communities** category.
  * Choose one of the four triggers:


  * Group Joining Request Rejected
  * Group Post Created
  * Group Comment Created
  * Member Registered for Group Event


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077056522/original/rUMIRSXeZRT1o_zN_HkBGs3d7jK0woI8MA.png?1785253496)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077056639/original/qFH6eTg5A0sgUsrW7CKXPLNJkrbjn1M34A.png?1785253543)

Step 3

Configure Required Filters

Each trigger requires at least a **Group** filter, and some include additional optional filters.

Under **Filters** , set:

  * **Group** (required): Choose the specific community group(s) to monitor.
  * **(Optional)** Add more filters depending on the trigger:


  * Channel – For post/comment triggers.
  * Post Title / Post Content – To match posts containing certain words or phrases.
  * Comment Content – To react to specific comments.
  * Event Title – For event registration triggers.


Click **Save Trigger**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077056777/original/jXpTQc1C9h9OG7M3sh9_rTFxrr8XEy93ug.png?1785253610)

Step 4

Add Actions for Your Automation Flow

Once the trigger is configured, define what should happen when it fires.

Typical actions might include:

  * Send Email / SMS / In-app notification to the member or internal team.
  * Create a Task for a moderator or account manager.
  * Add/Remove Tags to segment contacts based on their community activity.
  * Add to Another Workflow to enroll the contact in a broader nurture or onboarding sequence.
  * Update Contact Fields (e.g., last engaged group, interest category).


Step 5

Test and Publish

Use a test contact or a test member account to:

  * Submit a join request and reject it,
  * Create a post or comment,
  * Register for a group event (depending on the trigger you configured).


Confirm that:

  * The contact is added to the workflow run.
  * The correct actions (emails, tags, tasks, etc.) are executed.


When everything looks good, toggle the workflow to **Publish**.

## Related Articles

  * How to Setup, Customize, and Manage Your Communities
  * A List of Workflow Triggers
  * Getting Started with Workflows
  * Communities Workflow Triggers


9

## Frequently Asked Questions

Q: Where do I find these Communities triggers in my account?

They appear in the Add New Trigger list inside the Workflow Builder, under the Communities category—alongside existing triggers like Group Access Granted, Group Access Revoked, and leaderboard triggers.

Q: Is the Group filter really required? Can I run these triggers across all groups?

For these four triggers, Group is required. You must choose at least one group so HighLevel knows which community to listen to. If you want similar automation across multiple groups, either select multiple groups (if supported) or create separate workflows per group.

Q: Do these triggers work in both public and private groups?

Yes. The triggers are based on activity inside Communities groups (join requests, posts, comments, and event registrations), regardless of the group's visibility, as long as the group is managed through HighLevel Communities.

Q: Can I combine content filters, like Post Content and Comment Content, in the same trigger?

You can stack multiple filters in a single trigger to narrow down when it should fire—for example, require a specific group, channel, and certain words in the post or comment content. The workflow will only start when all filter conditions are met.

Q: What are some best practices for moderation workflows using these triggers?

Common patterns include:  
  
• Using Comment Content filters to detect harmful or policy-violating language and create a task for moderators.  
• Using Post Content filters to forward posts containing "support," "issue," or "bug" to your support team.  
• Sending internal notifications only (no contact-facing messages) for sensitive moderation flows.

Q: Will these triggers re-fire if a post or comment is edited later?

These triggers are designed to fire when the event occurs (join request rejection, post creation, comment creation, or registration). Edits after the fact typically do not re-trigger the workflow; you'd need a separate edit-specific trigger if it exists in the platform.

Q: Can I use these triggers together with other Communities triggers in the same workflow?

Yes. You can design multi-branch workflows where, for example, Group Access Granted starts an onboarding path, and Group Post Created or Member Registered for Group Event handle ongoing engagement. The Advanced Builder makes it easier to visualize and connect these paths.

Q: Do members need to exist as Contacts for these workflows to run?

In most Communities scenarios, members are tied to Contacts in your CRM. The workflow will act on the associated Contact record, allowing you to send communications, apply tags, and update fields like any other workflow.

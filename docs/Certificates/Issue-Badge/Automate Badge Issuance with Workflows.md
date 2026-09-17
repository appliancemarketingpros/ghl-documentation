# Automate Badge Issuance with Workflows

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008492-automate-badge-issuance-with-workflows](https://help.gohighlevel.com/support/solutions/articles/155000008492-automate-badge-issuance-with-workflows)  
**Category:** Certificates  
**Folder:** Issue Badge

---

Workflow Automation

# Automate Badge Issuance with Workflows

Issue badges automatically and trigger follow-up actions to build complete recognition journeys in your workflows.

What You'll Learn

This article explains how to use the new Workflow actions to automatically issue badges and create follow-up automations based on badge awards.

You'll learn how the Issue Badge action and Badge Issued trigger work together to streamline recognition and build automated journeys around achievements.

Table of Contents

1

What is Badge Automation in Workflows?

2

Key Benefits

3

How the Issue Badge Action Works

4

How the Badge Issued Trigger Works

5

How to Set Up Badge Automation

6

Related Articles

7

Frequently Asked Questions

1

## What is Badge Automation in Workflows?

Badge automation allows you to issue badges automatically through Workflows and trigger additional actions whenever a badge is awarded. This integration connects recognition with your broader automation strategy, making it easier to celebrate achievements and continue customer journeys based on milestones.

The feature includes two new Workflow components: the Issue Badge action, which awards a badge when workflow conditions are met, and the Badge Issued trigger, which starts follow-up automations immediately after a badge is granted.

Together, these tools let you build complete recognition flows—from automatically awarding badges based on behavior or milestones to sending congratulatory messages, updating contact records, or launching next steps in a customer journey.

2

## Key Benefits

Badge automation streamlines recognition and opens new opportunities to engage contacts based on achievements. These capabilities make it simple to acknowledge milestones and maintain momentum in customer relationships.

**Seamless recognition** — Issue badges automatically as part of existing workflows, eliminating manual tracking and ensuring timely acknowledgment.

**Follow-up automation** — Trigger additional actions after a badge is issued, such as sending congratulations, updating contact properties, or starting the next phase of a journey.

**Enhanced engagement** — Celebrate milestones automatically and maintain contact momentum by connecting recognition to further interactions.

**Workflow flexibility** — Combine badge issuance with any workflow trigger or condition, allowing recognition to fit naturally into your existing automation strategy.

3

## How the Issue Badge Action Works

The Issue Badge action adds badge issuance as a step in any workflow. When the workflow reaches this action, it automatically awards the selected badge to the contact or participant who triggered the workflow.

You can use this action in workflows triggered by events such as course completions, purchases, form submissions, or custom field updates. Once the workflow conditions are met, the badge is issued without manual intervention.

Tip

Combine the Issue Badge action with filters and conditions to ensure badges are only awarded when specific criteria are met, such as achieving a score threshold or completing multiple activities.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079016592/original/dILCkxNbAXGe83y9-voq5y9y8-h_0oGkGg.png?1787320380)

4

## How the Badge Issued Trigger Works

The Badge Issued trigger starts a workflow whenever a specified badge is awarded to a contact. This trigger activates regardless of how the badge was issued—whether manually, through the Issue Badge action, or by any other method.

Once triggered, the workflow can execute follow-up actions such as sending a congratulatory email or SMS, updating contact tags or custom fields, assigning the contact to a pipeline stage, or starting another automation sequence.

Use Case

Use the Badge Issued trigger to send a personalized message acknowledging the achievement, offer a discount or reward, or enroll the contact into an advanced course or program based on their accomplishment.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079016507/original/MDth892hmxZoMFtBYvv3z1OXeUpV6efrTw.png?1787320353)

5

## How to Set Up Badge Automation

Setting up badge automation involves configuring the Issue Badge action to award badges automatically. Follow these steps to add badge issuance to your workflows.

Step 1

Open or Create a Workflow

Navigate to the Workflows section in HighLevel and either create a new workflow or open an existing workflow where you want to add badge issuance.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079017207/original/N3lwClH59-QV_ArKnfMT8PVfM-tfMkEONw.png?1787320482)

Step 2

Add the Issue Badge Action

In the workflow builder, click to add a new action. Search for and select "Issue Badge" from the available actions list.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079017388/original/77AKgpbotR8ce2sb0qyjHxfuYYmJtToCPg.png?1787320557)

  


Step 3

Select the Badge to Issue

Use the dropdown menu to choose which badge will be issued when the workflow reaches this action. Only active badges configured in your account will appear in the list.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079017291/original/S294ffEdnbmzXiGOxRR_HlyDqu6wTmqipA.png?1787320515)

Step 4

Save and Activate the Workflow

Save your changes and activate the workflow. The badge will now be issued automatically whenever the workflow conditions are met and the action is reached.

Note

To set up follow-up actions after a badge is issued, create a separate workflow using the Badge Issued trigger. Select the badge that will start the workflow, then add actions like sending emails, updating contact fields, or starting additional automations. You can have multiple workflows using the same badge in the Badge Issued trigger for different follow-up scenarios.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079017466/original/K4rNcWBlL0zdGb299kUidFX9XBeJbD7NnA.png?1787320619)

6

## Related Articles

  * [How to Use Badges in Certificate Builder](<https://help.gohighlevel.com/support/solutions/articles/155000005539-how-to-use-badges-in-certificate-builder>)
  * [Welcome Badge for Course Enrolments](<https://help.gohighlevel.com/support/solutions/articles/155000007523-welcome-badge-for-course-enrolments>)
  * [How to Download Share Certificates & Badges](<https://help.gohighlevel.com/support/solutions/articles/155000005181-how-to-download-share-certificates-badges>)


7

## Frequently Asked Questions

Q: Can I issue multiple badges in a single workflow?

Yes. You can add multiple Issue Badge actions to the same workflow to award different badges at different stages or under different conditions within that workflow.

Q: Does the Badge Issued trigger work for manually issued badges?

Yes. The Badge Issued trigger activates whenever the selected badge is issued, whether it was awarded manually, through the Issue Badge action, or by any other method.

Q: What happens if a contact already has the badge when the workflow tries to issue it?

The workflow will continue without issuing a duplicate badge. Each badge can only be awarded once per contact, so the system prevents duplicate issuance automatically.

Q: Can I use filters or conditions with the Badge Issued trigger?

Yes. After setting the Badge Issued trigger, you can add filters and conditions to the workflow to further control when follow-up actions execute, such as checking contact tags or custom field values.

Q: Do I need to create badges separately before using them in workflows?

Yes. Badges must be created and configured in your HighLevel account before they can be selected in the Issue Badge action or Badge Issued trigger.

Q: What types of follow-up actions can I add after the Badge Issued trigger?

You can use any workflow action, including sending emails or SMS messages, updating contact fields, adding or removing tags, moving contacts through pipeline stages, creating tasks, or starting additional workflows.

Q: Can I test the badge automation before activating the workflow?

Yes. Use HighLevel's workflow testing features to verify that badges are issued correctly and follow-up actions execute as expected before activating the workflow for live contacts.

Q: Are there limits on how many badges I can issue through workflows?

There are no specific limits on badge issuance through workflows beyond the general badge and workflow limits of your HighLevel account plan.

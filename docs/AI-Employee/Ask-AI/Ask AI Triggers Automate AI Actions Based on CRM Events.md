# Ask AI Triggers: Automate AI Actions Based on CRM Events

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008715-ask-ai-triggers-automate-ai-actions-based-on-crm-events](https://help.gohighlevel.com/support/solutions/articles/155000008715-ask-ai-triggers-automate-ai-actions-based-on-crm-events)  
**Category:** AI Employee  
**Folder:** Ask AI

---

Ask AI

# Ask AI Triggers: Automate AI Actions Based on CRM Events

Configure custom Ask AI skills to run automatically when specific events occur in your CRM—no manual intervention required.

What You'll Learn

Ask AI Triggers enable you to automate AI-powered workflows by connecting custom skills to CRM events. Instead of manually initiating conversations, your skills execute automatically when contacts are created, forms are submitted, tags are applied, appointments are booked, or opportunities change status.

This article explains how to configure triggers, create skills directly from Ask AI Chat, and monitor automated runs using Trigger History.

Table of Contents

1

What Are Ask AI Triggers?

2

Key Benefits

3

Supported Trigger Events

4

How to Set Up Ask AI Triggers

5

Creating Skills and Triggers from Ask AI Chat

6

Monitoring Trigger Runs

7

Frequently Asked Questions

1

## What Are Ask AI Triggers?

Ask AI Triggers allow custom skills to execute automatically when specific CRM events occur. Instead of requiring users to manually start a conversation with Ask AI, triggers initiate skill execution in response to real-time data changes—such as a new contact being created, a form submission, or an opportunity status update.

When a trigger fires, Ask AI runs the associated skill using the relevant CRM context (contact details, form responses, opportunity data, etc.). This enables you to build intelligent automation workflows that respond instantly to customer actions and pipeline events.

Triggers complement scheduled skills, which run at specific times or intervals. Together, they provide comprehensive automation coverage for both time-based and event-based scenarios.

2

## Key Benefits

Ask AI Triggers deliver automation, responsiveness, and visibility for your CRM workflows.

**Automate Repetitive Workflows** — Eliminate manual tasks by configuring skills to run automatically when events occur, freeing your team to focus on higher-value activities.

**Respond in Real Time** — Take immediate action when contacts are created, forms are submitted, or opportunities change status, ensuring timely follow-up and engagement.

**Centralized Monitoring** — Track all automated runs in Trigger History, including execution details, run status, and resulting Ask AI sessions.

**Simplified Setup** — Create skills and triggers directly from Ask AI Chat by describing your automation goal in natural language.

**Context-Aware Execution** — Skills automatically receive relevant CRM data (contact fields, form responses, opportunity details) when triggered, enabling intelligent automation.

3

## Supported Trigger Events

Ask AI Triggers support a range of CRM events, enabling you to automate workflows across contacts, forms, surveys, tags, appointments, opportunities, and lead sources.

Event Type

Contact Created

Trigger a skill when a new contact is added to your CRM. Use this to send welcome messages, initiate onboarding sequences, or enrich contact data automatically.

Event Type

Form Submitted

Execute a skill when a specific form is submitted. Ideal for processing lead capture forms, scheduling follow-ups, or routing submissions to the appropriate team.

Event Type

Survey Submitted

Trigger a skill when a survey is completed. Use this to analyze survey responses, calculate satisfaction scores, or trigger follow-up actions based on feedback.

Event Type

Tag Added or Removed

Run a skill when a specific tag is added to or removed from a contact. Perfect for segmenting workflows based on contact attributes or lifecycle stages.

Event Type

Appointment Booked or Status Changed

Trigger a skill when an appointment is booked or its status changes (confirmed, canceled, rescheduled). Use this to send reminders, update opportunity records, or notify team members.

Event Type

Opportunity Created or Status Changed

Execute a skill when a new opportunity is created or when an opportunity's status changes (e.g., moved to a new pipeline stage). Ideal for automating sales workflows and notifications.

Event Type

Facebook Lead Received

Run a skill when a lead is received from Facebook Lead Ads. Use this to enrich lead data, send immediate follow-up messages, or route leads to the appropriate team member.

Event Type

Scheduled Execution

Skills can also run on a schedule (specific date/time, interval, or cron expression), enabling time-based automation alongside event-based triggers.

4

## How to Set Up Ask AI Triggers

Follow these steps to configure a trigger for a custom Ask AI skill. This allows the skill to run automatically when the specified CRM event occurs.

Step 1

Navigate to Ask AI Customize

In your HighLevel account, go to **Ask AI** → **Customize** → **Skills**. This displays all custom skills configured for your account.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080725637/original/iAmcunXejrzzaEWlObvU7dXnMNRx_K-uzg.png?1789135558)

Step 2

Select the Skill to Automate

Click on the custom skill you want to trigger automatically. If you don't have a skill yet, create one by clicking **\+ Add Skill** and defining its purpose, instructions, and behavior.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080725710/original/_qByjNLE4Wyxjs1Q-oTKvJDmnEtmrgiZqQ.png?1789135601)

Step 3

Add a Trigger

Within the skill settings, locate the **Triggers** section and click **\+ Add Trigger**. Select the event type that should initiate the skill (e.g., Contact Created, Form Submitted, Tag Added).  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080694873/original/idPd3dR00Wzv6FhBU00EAQApvNOKveuCKw.png?1789122469)

Step 4

Configure Trigger Conditions

Depending on the event type, configure additional conditions. For example, if you selected "Form Submitted," specify which form should trigger the skill. If you selected "Tag Added," specify the tag name.

Step 5

Enable the Trigger

Toggle the trigger to **Enabled**. Once enabled, the skill will execute automatically whenever the configured event occurs.

Success

Your trigger is now active. Ask AI will run the skill using the relevant CRM context each time the event fires.

5

## Creating Skills and Triggers from Ask AI Chat

You can now create both a skill and its trigger configuration directly from Ask AI Chat—without navigating to the Customize section. This streamlines the automation setup process.

Step 1

Start a Conversation with Ask AI

Open Ask AI Chat and describe the automation you want to create in natural language. For example: "Create a skill that sends a welcome email when a new contact is added."

Step 2

Ask AI Creates the Skill and Trigger

Ask AI interprets your request and generates the skill along with its trigger configuration. It will suggest the appropriate event type, trigger conditions, and skill instructions.

Step 3

Review and Confirm

Review the proposed skill and trigger setup. You can refine the instructions, adjust trigger conditions, or modify the skill's behavior before finalizing.

Step 4

Enable the Skill

Once you're satisfied with the configuration, confirm the setup. Ask AI will save the skill and activate the trigger, making it immediately operational.

Tip

This conversational approach is ideal for users who prefer a guided setup experience. You can always refine skills and triggers in the Customize section later.

6

## Monitoring Trigger Runs

Trigger History provides visibility into all automated skill executions. You can review which events fired triggers, whether they succeeded, and view the resulting Ask AI sessions.

To access Trigger History, navigate to **Ask AI** → **Trigger History**. Each entry displays the following information:

**Trigger Event** — The CRM event that initiated the skill run (e.g., Contact Created, Form Submitted).

**Run Status** — Whether the skill execution succeeded, failed, or is in progress.

**Execution Details** — Information about the skill that ran, the context provided, and any actions taken.

**Resulting Ask AI Session** — A link to the Ask AI conversation log generated by the skill execution.

Tip

Use Trigger History to troubleshoot failed runs, verify that triggers are firing as expected, and gain insights into automated workflow performance.

7

## Frequently Asked Questions

Q: Can I add multiple triggers to a single skill?

Yes. You can configure multiple triggers for a single skill. For example, a skill could run when either a contact is created or a specific tag is added. Each trigger operates independently.

Q: What CRM data does the skill receive when triggered?

When a trigger fires, Ask AI provides the skill with relevant context from the triggering event. For example, a "Contact Created" trigger includes contact fields, while a "Form Submitted" trigger includes form responses. This enables the skill to act on specific data.

Q: Can I disable a trigger temporarily without deleting it?

Yes. You can toggle a trigger off in the skill settings to pause automated execution. The trigger configuration remains saved and can be re-enabled at any time.

Q: How do I know if a trigger failed to execute?

Check Trigger History to view the run status for each execution. Failed runs are logged with details about the error, allowing you to troubleshoot and adjust the trigger or skill configuration as needed.

Q: Can triggers be used with both custom skills and default Ask AI skills?

Triggers are currently available for custom skills only. Default Ask AI skills do not support trigger-based automation.

Q: Do triggers work across all sub-accounts in an agency account?

Triggers are configured at the sub-account level. Each sub-account's skills and triggers operate independently. If you want consistent automation across multiple sub-accounts, you'll need to configure triggers in each one.

Q: Can I test a trigger before enabling it in production?

Yes. You can create a test contact, submit a test form, or perform the triggering event in your account to verify that the skill runs as expected. Review the execution in Trigger History to confirm success before enabling the trigger for all events.

Q: Are there any limits on how many triggers I can create?

There are no strict limits on the number of triggers you can configure. However, monitor Trigger History to ensure your automations remain performant and aligned with your workflow requirements.

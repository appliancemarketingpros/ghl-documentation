# Appointment Triggers in Managed Agents

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008310-appointment-triggers-in-managed-agents](https://help.gohighlevel.com/support/solutions/articles/155000008310-appointment-triggers-in-managed-agents)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

AI Agent Studio

# Managed Agents Appointment Triggers

Automate AI agent responses when customers book, confirm, cancel, or miss appointments using event-based triggers in Agent Studio.

What You'll Learn

This article explains how to configure appointment-based start triggers for Managed Agents (formerly Super Agents) in HighLevel, so your AI agents can respond instantly to key scheduling moments like bookings, confirmations, cancellations, and no-shows.

You'll learn how to set up both trigger types, apply calendar and status filters, and use the visual builder or Builder Chat to create automation that delivers timely, personalized outreach without manual work.

Table of Contents

1

What is Managed Agents Appointment Triggers?

2

Key Benefits

3

Appointment Trigger Types

4

Advanced Trigger Filters

5

Configuring Triggers in the Visual Builder

6

Configuring Triggers with Builder Chat

7

Appointment Events in the Activity Feed

8

How to Set Up Appointment Triggers

9

Related Articles

10

Frequently Asked Questions

Video Walkthrough

1

## What is Managed Agents Appointment Triggers?

Managed Agents (formerly Super Agents) Appointment Triggers are event-based start conditions that launch a Managed Agent whenever specific appointment events occur on your HighLevel calendars. Instead of only reacting to chats, form submissions, or tag changes, your agents can start running the moment a booking is created or its status updates, ensuring that high-intent contacts get timely, relevant outreach.

These triggers are configured on the Managed Agent's start trigger using the same real-time, event-driven infrastructure already available in Agent Studio. When you attach an appointment trigger to a Managed Agent's start node, the agent receives appointment context—such as the calendar and status—as part of the event payload, allowing your prompts and flow logic to reference those details for personalized responses.

Two appointment events are available as trigger sources for Managed Agents:

**Customer Booked Appointment** — Fires whenever a new appointment is successfully booked on one of your selected calendars.

**Appointment Status Changed** — Fires whenever an existing appointment's status changes, such as Confirmed, Cancelled, Showed, No Show, or Rescheduled.

Each trigger can be scoped to specific calendars and appointment statuses, giving you precise control over when the agent should start.

2

## Key Benefits

Adding appointment-based triggers unlocks automation opportunities around your scheduling workflows, helping you respond faster, stay organized, and scale personalized experiences without adding manual tasks.

**Real-time appointment engagement** — Launch agents automatically when a customer books, confirms, cancels, or misses an appointment, instead of relying on delayed workflows or manual follow-ups.

**High-intent timing** — Focus AI conversations around moments when contacts are most engaged—right after scheduling, changing, or missing an appointment—dramatically increasing response and show-up rates.

**Precise targeting by calendar and status** — Restrict triggers to specific calendars (such as sales calls, consultations, or service appointments) and optionally filter by status to avoid unnecessary executions.

**Consistent, reusable logic** — Centralize your appointment logic inside Managed Agents so you can reuse the same flow for confirmations, reminders, and win-back campaigns across multiple calendars.

**Lower manual workload** — Replace manual outreach and ad-hoc reminders with automated agents that handle confirmations, FAQs, rescheduling instructions, and follow-up offers.

**Leverages existing Agent Studio infrastructure** — Appointment triggers use the same start-trigger architecture as form, tag, and chat events, so you can rely on familiar testing, validation, and publish flows.

3

## Appointment Trigger Types

Appointment triggers define when a Managed Agent should start based purely on calendar activity. Understanding the two trigger types helps you align each with the outcomes you want—such as instant confirmations, pre-call nurturing, or post-no-show recovery.

Trigger Type 1

Customer Booked Appointment (appointment_booked)

Fires whenever a new appointment is successfully booked on one of the calendars you select.

Ideal for sending confirmation details, pre-appointment instructions, or pre-qualifying questions.

Can be limited to specific calendars (e.g., "Sales Strategy Call," "Onboarding Call," "Dental Cleaning").

Trigger Type 2

Appointment Status Changed (appointment_status)

Fires whenever an existing appointment's status changes (e.g., Confirmed, Cancelled, Showed, No Show, Rescheduled).

Useful for outcomes-based flows, such as:

  * Send a "thanks for attending" message when status becomes Showed.
  * Trigger a win-back or reschedule campaign when status becomes No Show or Cancelled.
  * Provide reminders or directions when status moves to Confirmed.


![Managed Agent canvas with Start trigger configured for Customer Booked Appointment, showing calendar and status filter options](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077215438/original/PlduRTJ4nzFd-0LTguiIIjX5Ahhe6Wr23w.png?1785403529)

4

## Advanced Trigger Filters

Advanced filters ensure Managed Agents only run when appointment events truly matter to your workflow. This reduces noise, saves AI usage, and keeps your automation focused on high-value scenarios.

Filter 1

Calendars (Required)

You must choose one or more calendars before saving the trigger.

The Managed Agent runs only when events occur on the selected calendars.

Common patterns:

  * Trigger only on "Sales" or "Consultation" calendars, not internal or admin calendars.
  * Separate flows per service line (e.g., Coaching, Dental Cleaning, HVAC Service).


Filter 2

Appointment Statuses (Optional)

For appointment_status triggers, you can narrow execution to specific statuses such as Confirmed, Cancelled, Showed, No Show, or Rescheduled.

If you leave the status filter empty, the Managed Agent will run on every status change for appointments on the selected calendars.

Example Use Cases

  * Run the agent only when a prospect confirms a sales call to send prep emails or collect more information.
  * Run the agent when a service appointment is cancelled or marked No Show to trigger re-booking offers.
  * Run the agent whenever any status changes on an internal calendar for internal notifications or reporting updates.


![Trigger configuration panel highlighting multi-select calendar and optional status filters](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077215448/original/9t8LC_jZv3llElLKlEfWYOBeqIsM_UIX9g.png?1785403550)

5

## Configuring Triggers in the Visual Builder

The Managed Agents visual builder lets you set up appointment triggers with a few clicks using a familiar, canvas-based experience. This approach is ideal if you prefer visual control over when and how your agents start, and it mirrors the existing Agent Studio trigger configuration for forms, tags, and chat.

When you use the visual builder:

  * You explicitly attach the appointment trigger to the Managed Agent's Start node.
  * You configure calendars and statuses directly inside the trigger panel.
  * Built-in validation checks for required fields (like at least one calendar) before you can save.


High-level configuration flow:

  1. Open the Managed Agent in the visual builder.
  2. Locate or add the Start trigger node on your canvas.
  3. Choose Customer Booked Appointment or Appointment Status Changed as the trigger type.
  4. Select at least one calendar from the calendar dropdown.
  5. (Optional) Select one or more statuses for appointment_status triggers, or leave blank to trigger on all status changes.
  6. Save, test, and publish the agent so real appointment events start the flow.


![Managed Agent Start trigger node with Appointment Status Changed selected and multiple statuses highlighted](https://files.slack.com/files-pri/T098GV8SRC2-F0BFDRE6SHY/download/screenshot_2026-07-06_at_5.46.51___pm.png)

6

## Configuring Triggers with Builder Chat

Builder Chat allows you to describe your desired automation in natural language so the system can generate the corresponding trigger configuration for you. This is helpful if you know what you want the agent to do but don't want to manually click through every setting.

By using Builder Chat, you can:

  * Explain scenarios like: "Start this agent whenever someone books a consultation on my Sales Calendar."
  * Or: "Run this agent when a dental cleaning appointment is marked as No Show."


The builder automatically:

  * Chooses the appropriate appointment trigger type (appointment_booked or appointment_status).
  * Attaches the trigger to the correct Managed Agent.
  * Sets calendar and status filters based on your description.


You can still open the visual builder afterward to:

  * Verify the calendars and statuses the chat builder configured.
  * Adjust filters, prompts, and downstream nodes.
  * Run tests using the standard Agent Studio testing tools before going live.


7

## Appointment Events in the Activity Feed

Appointment-triggered runs of a Managed Agent are surfaced clearly in the activity feed, making it easier to understand why an agent started and what appointment it responded to. This visibility is especially useful when combined with Agent Logs and other analytics tools in HighLevel.

Appointment executions include:

**Dedicated calendar icon** — Quickly distinguish appointment-triggered runs from other event types.

**"Appointment" event tag** — See at a glance that the agent was started by an appointment event rather than a chat, form, or tag change.

**Metadata about the event** — View which calendar the appointment belongs to and the status at the time the agent started (e.g., Confirmed, Cancelled, No Show).

With this context, you can:

  * Troubleshoot why a particular contact received a message.
  * Confirm that your calendar and status filters are working as expected.
  * Review patterns—such as how often no-show recovery flows are running—using Agent Logs and other reporting features.


![Activity feed entry with calendar icon, Appointment tag, and status metadata](https://files.slack.com/files-pri/T098GV8SRC2-F0BFBRH3GMU/download/screenshot_2026-07-06_at_5.49.01___pm.png)

8

## How to Set Up Appointment Triggers

Proper setup ensures your Managed Agents start reliably on the right appointment events while remaining safe to test before impacting live customers. These steps outline a practical path from initial configuration to production rollout using HighLevel's existing Agent Studio trigger framework.

Step 1

Prepare Your Calendars and Appointment Types

  * Confirm that the calendars you want to use are created and active in your sub-account.
  * Verify that appointment types, time zones, and availability are correct, since your agents will rely on these settings.
  * If needed, create separate calendars for different use cases (e.g., "Sales Demo," "Onboarding Call," "VIP Consult") so your triggers can target them precisely.


Step 2

Open or Create Your Managed Agent

  * Navigate to your AI agents > Agent Studio and open the Managed Agent you want to enhance.  
  

  * If you're building a new agent, design at least the core flow: a greeting or confirmation message, any questions you want to ask (e.g., qualification or pre-appointment checklist), and follow-up actions such as notes, tags, or internal notifications.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077214758/original/-WPvdzWbLujPTlUduzGd3QRwblQIZRCMiw.png?1785403184)


Step 3

Add an Appointment Start Trigger

On the canvas, locate the Start node (or add a Start trigger node if one is not present).

Choose Customer Booked Appointment or Appointment Status Changed as the trigger type based on your use case:  
  


  * Use Customer Booked Appointment for post-booking confirmations and nurture.
  * Use Appointment Status Changed for post-event or status-specific flows (e.g., No Show recovery).  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077214927/original/NYiLdhIOWFYhvclT-EJm6rwAnxepu6PesA.png?1785403311)


Step 4

Configure Calendars and Statuses

  * In the trigger settings, select one or more calendars that should fire this Managed Agent.  
  

  * If you chose Appointment Status Changed: Select only the statuses that should start the agent (e.g., No Show, Cancelled), or leave the status list empty to run the agent on all status changes for the selected calendars.  
  

  * Save your trigger configuration and confirm that validation passes (for example, at least one calendar must be selected).  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077215065/original/MyQ9Qbx8770lzmVFyomGNol8rULs94jbcQ.png?1785403380)


Step 5

Design Appointment-Aware Logic Inside the Agent

Update your prompts and messages to reference appointment context, such as date and time of the booking, type of appointment or service, and status (Confirmed, Cancelled, No Show, etc.).

Add any necessary nodes:

  * Tag the contact (e.g., "Booked Consult," "No-Show Recovery Sent").
  * Send SMS or email reminders.
  * Notify internal team members.


Step 6

Test Before Going Live

Use Agent Studio's test tools to simulate appointment events and verify that the correct trigger fires, that the agent receives the expected appointment data, and that messages and actions behave as intended.

Optionally, create a test calendar and test contact to avoid triggering real customers.

Review the activity feed and Agent Logs to ensure the appointment icon, event tag, and metadata look correct.

Step 7

Publish and Monitor

Once tests pass, publish the Managed Agent so the appointment triggers become active for your sub-account.  
  


Monitor initial runs:  
  


  * Confirm that only the intended calendars and statuses are starting the agent.  
  

  * Watch performance metrics such as show rates, response rates, and recovery rates using your existing reporting tools.  
  

  * Iterate on prompts, filters, and logic as you learn from real-world behavior.


Success Tip

Start with one high-value calendar (such as sales demos or new client consultations) to validate your trigger logic, then expand to additional calendars and statuses once you confirm the agent behaves as expected.

9

## Related Articles

  * How to Use the AI Agent Studio in HighLevel
  * Agent Studio Overview & Beginner Guide
  * How to Set Up a Booking Calendar in HighLevel
  * Agent Logs in HighLevel: Overview, Benefits, and Setup


10

## Frequently Asked Questions

Q: Do appointment triggers replace form, tag, or chat triggers for Managed Agents?

No. Appointment triggers are additive. You can continue using form, tag, and chat triggers alongside appointment-based triggers, or even configure multiple trigger types for the same Managed Agent if it makes sense for your workflow.

Q: What happens if I don't select any appointment statuses for an appointment_status trigger?

If you leave the status filter empty, the Managed Agent will run on all appointment status changes for the calendars you selected—such as Confirmed, Cancelled, Showed, and No Show. Use this only when you want the agent to respond to every status transition.

Q: Can a Managed Agent have more than one appointment trigger?

Yes. You can configure multiple appointment triggers on the same agent—for example, one trigger for "Customer Booked Appointment" on your Sales calendar and another for "Appointment Status Changed = No Show" on your Service calendar—to handle different flows in a single agent.

Q: How do appointment triggers behave with recurring or rescheduled appointments?

A newly booked occurrence fires the Customer Booked Appointment trigger (if the calendar is selected). When an appointment is rescheduled or updated, the Appointment Status Changed trigger can fire depending on how your account records the change and which statuses you selected.

Q: Can I test appointment triggers without affecting real customers?

Yes. You can create a test calendar and test contact, configure the trigger to listen only to that calendar, then book and update test appointments while using the Agent Studio test tools and logs to validate your flow before rolling it out to production.

Q: How do I see which appointment caused a specific Managed Agent run?

Open the execution in your activity feed or Agent Logs. Appointment-triggered runs include a calendar icon, an "Appointment" event tag, and metadata such as the calendar and status so you can quickly identify the source event.

Q: Are appointment triggers available for all calendars in my account?

Appointment triggers listen to calendars and appointments managed by your HighLevel sub-account. If you do not see a particular calendar in the trigger configuration, confirm that it exists in the same location and that you have permission to view it.

Q: Will appointment triggers impact my existing workflows that already automate reminders?

Appointment triggers do not automatically disable or modify existing workflows. If you already use workflows or campaigns for reminders, you may want to review and adjust them so customers don't receive duplicate messages when both the workflow and the Managed Agent respond to the same event.

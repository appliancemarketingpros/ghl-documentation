# How to Use Workflow AI Assistant Performance Analytics

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008386-how-to-use-workflow-ai-assistant-performance-analytics](https://help.gohighlevel.com/support/solutions/articles/155000008386-how-to-use-workflow-ai-assistant-performance-analytics)  
**Category:** AI Employee  
**Folder:** AI Employee

---

Workflow Automation

# Workflow AI Assistant Performance Analytics

Ask the AI Assistant how your workflows perform and get structured answers from live data in your account — no digging through logs required.

What You'll Learn

The Workflow AI Assistant answers performance questions in plain language. You can ask how a workflow is performing, track individual contacts through steps, diagnose trigger issues, and search every workflow in your account.

This article explains what insights you can request, how to interpret the data, and how to use the Assistant to troubleshoot and optimize your workflows.

Table of Contents

1

What is Workflow AI Assistant Performance Analytics?

2

Key Benefits

3

How to Access the AI Assistant

4

Performance Insights

5

Email and SMS Results

6

Branch and Path Insights

7

Contact Tracking

8

Trigger Diagnostics

9

Find Workflows Across Your Account

10

Version History

11

Frequently Asked Questions

1

## What is Workflow AI Assistant Performance Analytics?

The Workflow AI Assistant answers questions about how your workflows are performing by analyzing live data from your account. You ask in plain language, and it returns structured insights — entries, completion rates, trigger diagnostics, contact-level tracking, and email or SMS engagement — without requiring you to search through execution logs.

The Assistant reads your workflow data but never modifies your workflows. All date ranges respect your account timezone, and when data is missing, the Assistant tells you what to check rather than inventing numbers.

2

## Key Benefits

Performance analytics in the AI Assistant help you troubleshoot and optimize workflows faster. You spend less time guessing and more time fixing.

**Plain-language queries** — Ask how a workflow is doing, which contacts failed, or why a trigger isn't firing, and get back structured answers in seconds.

**Live data** — All insights come from real-time workflow execution data in your account, not cached or delayed reports.

**Period comparisons** — See whether entries, completion rates, or goal conversions are trending up or down compared to the previous period.

**Contact-level visibility** — Track individual contacts through the workflow, see where they are now, and identify who failed or is waiting at a particular step.

**Trigger diagnostics** — Discover silent rejections by checking whether the trigger is firing, what percentage of fires qualified, and the top reasons contacts were rejected.

**Account-wide search** — Find workflows by name, status, tags, the triggers or actions they use, or who last edited them.

3

## How to Access the AI Assistant

The AI Assistant is available in every workflow. Follow these steps to access performance analytics:

Step 1

Navigate to Automations

  


From your HighLevel dashboard, go to **Automations** and then select **Workflows**.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077889353/original/-sQMlPml9rU3kQDyuxDqGU_R38XY7iVkrg.png?1786105800)

Step 2

Select or Create a Workflow

  


Choose an existing workflow you want to analyze, or create a new workflow from scratch.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077889607/original/ZKDq_NOvgBknNXV_RCwt6fedFfOgGY9wrg.png?1786105864)

Step 3

Open the AI Assistant

  


Once you're inside the workflow builder, locate the AI Assistant icon in the left sidebar and click it to open the Assistant panel.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077890607/original/6XcdjTYoJ_UnjeOL7as-VR7lus_NTNZdlw.png?1786106196)

Step 4

Switch to Chat Mode

  


At the top of the AI Assistant panel, click the **Chat** button to switch to Chat mode. This enables performance analytics and displays Quick Starters to help you get started.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077890871/original/aI-qIAkyQg4Bs5PlRw8KS4hj129EWdZS6Q.png?1786106286)

Step 5

Ask Your Question

Type your question in the input field or select one of the Quick Starters, such as "Key metrics at a glance" or "Opens, clicks, and delivery rates," to instantly retrieve performance insights.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077891593/original/n7gw8KCWSC21Y2cybHZWT2xOdOdtwAhyDw.png?1786106553)

Tip

Use the Quick Starters to see example queries you can ask. You can also type custom questions in plain language, such as "How is this workflow performing?" or "Why aren't contacts entering?"

4

## Performance Insights

Ask the Assistant how a workflow is performing to see entries over any period, a status breakdown, completion rate, goal conversions, and where contacts drop off. You can view trends by week, day, or hour, and see how many contacts sit at each step right now.

Example queries:

  * "How is [workflow name] performing?"
  * "Show me entries for the last 30 days"
  * "What's the completion rate this week vs. last week?"
  * "Where are contacts dropping off?"


Tip

The Assistant compares the current period against the equivalent period before it. For example, "last 7 days" compares against the 7 days prior to that window.

The response includes total entries, percentage change from the previous period, a status breakdown (completed, failed, waiting, skipped), goal conversion counts if applicable, and a step-by-step view showing where contacts are currently positioned in the workflow.

5

## Email and SMS Results

Ask for delivery and engagement metrics for any email or SMS step in your workflow. The Assistant reports delivered, opened, clicked, replied, bounced, unsubscribed, opted out, and other engagement events.

Example queries:

  * "Show me email results for [step name]"
  * "How many SMS messages were delivered?"
  * "What's the open rate for the welcome email?"


Use these metrics to measure engagement, identify deliverability issues, and refine messaging based on real performance data.

Quick Insight

Put Names to the Numbers

Ask "who entered last week?" or "which contacts failed at the SMS step?" and get back names and emails from your workflow executions.

6

## Branch and Path Insights

For if/else and split steps, the Assistant shows what percentage of contacts took each branch. This reveals whether your conditional logic is working as expected and which paths contacts prefer.

Example query:

  * "What percentage of contacts took the yes branch?"


7

## Contact Tracking

Check whether an individual contact completed, failed, or is still active in the workflow. The Assistant returns when they entered, how long they've been in the workflow, and where they are right now.

You can also ask for lists of contacts who meet specific conditions — who entered during a period, who failed at a particular step, or who is waiting at a given action.

Example queries:

  * "Did [contact name] complete this workflow?"
  * "Who entered last week?"
  * "Which contacts failed at the SMS step?"
  * "Show me everyone waiting at step 3"


8

## Trigger Diagnostics

Trigger diagnostics help you understand why a workflow isn't enrolling as many contacts as expected. The Assistant tells you whether the trigger is firing, what percentage of fires qualified, and the top reasons contacts are rejected.

You can inspect a single fire event to compare the value checked against the value expected. This surfaces silent rejections that were previously invisible in execution logs.

Example queries:

  * "Is the trigger firing?"
  * "What percentage of trigger fires qualified?"
  * "Why are contacts being rejected?"
  * "Show me the last trigger fire"


Note

Trigger diagnostics reveal rejections that don't appear in standard execution logs. If contacts aren't entering as expected, ask the Assistant to check trigger qualification.

9

## Find Workflows Across Your Account

Search every workflow in your account by name, status, tags, the triggers or actions it contains, or who last edited it. This is useful when you need to audit workflows, find workflows using a specific step type, or locate workflows edited by a particular team member.

Example queries:

  * "Which workflows use a Wait step?"
  * "Which workflows have the Invoice Paid tag?"
  * "Show me all active workflows"
  * "Which workflows did [team member name] last edit?"


10

## Version History

Ask who last edited a workflow and how many versions exist. This helps you track changes and understand the workflow's editing history.

Example queries:

  * "Who last edited this workflow?"
  * "How many versions exist?"


11

## Frequently Asked Questions

Q: Does the AI Assistant modify my workflows?

No. The AI Assistant only reads your workflow data. It never changes workflow structure, settings, or execution.

Q: What does "last 7 days" mean?

All date ranges use your account timezone. "Last 7 days" means the 7 days ending at the current moment in your configured timezone.

Q: What happens if there's no data for my query?

The Assistant tells you that no data is available and suggests what to check — for example, confirming the workflow is active or verifying that the time period includes executions.

Q: Can I ask about workflows in other accounts or subaccounts?

The Assistant only accesses data in the account where you're currently working. It does not read data from other accounts or subaccounts.

Q: How does trigger diagnostics differ from the execution log?

Trigger diagnostics show silent rejections — events where the trigger fired but the contact did not qualify. The execution log only shows contacts who entered the workflow. Diagnostics reveal why contacts were rejected before entering.

Q: Can I export the data the Assistant provides?

The Assistant provides structured text answers. You can copy and paste the response, but there is no built-in export to CSV or other formats.

Q: Is there a limit to how many questions I can ask?

There is no stated limit. You can ask as many questions as needed to understand workflow performance.

Q: What kind of questions can I ask?

You can ask about performance (entries, completion rates), trigger behavior (is it firing, why rejections), contact tracking (who entered, who failed, where they are), email/SMS results, branch percentages, workflow searches, and version history.

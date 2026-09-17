# Managed Agent Activity Feed: Monitor & Debug AI Agents

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008415-managed-agent-activity-feed-monitor-debug-ai-agents](https://help.gohighlevel.com/support/solutions/articles/155000008415-managed-agent-activity-feed-monitor-debug-ai-agents)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

Managed Agents

# Managed Agent Activity Feed

Monitor every action your Managed Agents (formerly Super Agents) take — live chat sessions and automated trigger runs — with execution logs, full step visibility, and inline debugging in one unified timeline.

What You'll Learn

The Activity Feed for Managed Agents provides a single timeline of everything your agent has done — both live chat conversations and automated trigger runs (form submissions, tag changes, and more). Click any run to open its execution log — the completed steps, skills and tools used, and final result — making it easy to monitor and debug your agents in one place.

This article explains what the Activity Feed is, how to use it to monitor and debug your Managed Agents, and why visibility into agent execution matters for trust and performance.

Table of Contents

1

What is the Managed Agent Activity Feed?

2

Key Benefits

3

How to Use the Activity Feed

4

Understanding Activity Feed Data

5

Viewing Execution Logs

6

Frequently Asked Questions

1

## What is the Managed Agent Activity Feed?

The Activity Feed is a unified timeline inside every Managed Agent that displays recent Managed Agent runs and activity, sorted in reverse chronological order (newest first). It combines live chat conversations and automated trigger executions — form submissions, tag changes, and other automations — into one view.

Each row in the feed shows an icon (lightning bolt for trigger runs, chat bubble for conversations), run status (such as "Completed"), timestamp, trigger type label (such as "Trigger" or "Chat"), and the context that fired the agent (such as "Form: Real Estate Consulting Lead" or "Tag added: new-lead"). Click any run to open its execution log, revealing the completed steps, which skills and tools were used, their inputs and outputs, and the final response delivered.

The Activity Feed is accessible inside Agent Studio under the Activity tab (which displays a badge count of recent runs) and is available on Managed Agents that support this feature.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077994388/original/zBpudjiUap0DKoXbY7__DQg-Q2tA7kmNaw.png?1786351169)

2

## Key Benefits

The Activity Feed centralizes every action your Managed Agent takes, giving you visibility and control over both live and automated interactions.

**Full Visibility:** See what your agent did across chat and automated runs in a single chronological view.

**Faster Debugging:** Review execution steps and tool calls inline to identify issues quickly.

**Trust and Transparency:** Verify what happened during automated trigger runs with detailed execution logs.

**Simplified Monitoring:** Chat and automation activity appear in a single feed with no context switching.

**Performance Tracking:** Review timing and token usage metrics to help identify slow steps or high-usage runs.

3

## How to Use the Activity Feed

Follow these steps to monitor and debug your Managed Agents using the Activity Feed.

Step 1

Navigate to Agent Studio

Go to the AI Agents section in HighLevel and open Agent Studio. Select the Managed Agent you want to monitor.

Step 2

Open the Activity Tab

Click the Activity tab at the top of the agent's page. The tab displays a badge showing the number of recent runs. The feed displays runs in reverse chronological order, with each row showing an icon, status, timestamp, trigger type label, and context description.

Step 3

Browse the Activity Feed

Scroll through the feed to view every run — both live chat sessions and automated trigger executions. Each row shows the run's status, timestamp, trigger type, and context. Click any row to open the full execution log.

Step 4

View Execution Logs

Click any run in the feed to open its execution log. The log displays the conversation title, action buttons (refresh, timing metrics, token usage, "Copy ID", and "View in Agent Logs"), the agent conversation view on the left (showing the run summary and completed steps), and the execution timeline on the right (showing each step with timing and token data).

Pro Tip

Use the Activity Feed during testing to verify that your agent's skills and triggers work as expected. During troubleshooting, review the execution timeline to identify which step caused an issue. Timing and token metrics help you optimize performance and identify bottlenecks.

4

## Understanding Activity Feed Data

Each row in the Activity Feed provides key information about a single agent run. Understanding these data points helps you quickly assess performance and identify issues.

Run Icon

Visual Run Type Indicator

Each run displays an icon: a lightning bolt for automated trigger runs or a chat bubble for live chat conversations. This helps you instantly distinguish between user-driven chat sessions and automated executions.

Run Status

Completion Indicator

The status indicator shows whether the run completed successfully (such as "Completed"), failed, or is still in progress. Use this to quickly spot errors or incomplete executions without opening the full log.

Timestamp

When the Run Occurred

Each run displays the date and time it started, making it easy to correlate agent activity with external events, user actions, or specific automation triggers.

Trigger Type Label

What Fired the Agent

The trigger type badge shows whether the run was initiated by a "Trigger" (automation) or "Chat" (live conversation). This label appears next to the context description, helping you distinguish between user-driven and automated interactions.

Context Description

Details About the Run

For automated trigger runs, the context field displays the name of the form, tag event, or other automation that fired the agent. For chat runs, it displays a preview of the user's message. This allows you to trace runs back to their source without opening the full log.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077994838/original/U3jVirAqF6aovKrejrjEM9Fff8vVzk7Umg.png?1786351361)

5

## Viewing Execution Logs

Clicking any run in the Activity Feed opens the execution log, which provides visibility into the agent's completed steps, tool usage, timing, and results. The execution log is divided into two main sections displayed side by side.

Agent Conversation View

Run Summary and Response

The left side of the execution log displays the agent conversation view, which shows the run summary and final response. This section displays the agent's avatar icon, thinking status (such as "Thought for 2s"), and the completion message.

Below the thinking status, you'll see a structured execution summary with a title, trigger details, timestamp, and detailed step breakdowns. Each step includes tables showing fields and values, making it easy to verify the agent's data lookups, eligibility checks, and action results.

Execution Timeline

Step-by-Step Tool and Skill Usage

The right side of the execution log displays the execution timeline, which shows every step the agent took during the run in sequential order. Each step includes an icon, step label (such as "Message" or "Llm"), description, timing metrics, and token usage.

Each step can be expanded to reveal detailed execution data, including inputs, outputs, structured data, and nested sub-steps for complex tool or skill invocations. The timeline provides transparency into the agent's execution process, making it easy to debug failures, verify correct behavior, and optimize performance.

Top Action Bar

Execution Controls and Metadata

The top of the execution log displays the conversation title along with action buttons: a refresh icon to reload the log, total execution time, total token usage, a "Copy ID" button to copy the conversation ID for reference or support tickets, and a "View in Agent Logs" button that opens the full log in a separate view. Use these controls to monitor performance, share run details with your team, or escalate issues to support.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077994990/original/NRBNU2G8pHt13KOIQxNQEKXzzYXqHt8JjA.png?1786351492)

6

## Frequently Asked Questions

Q: Where can I find the Activity Feed?

The Activity Feed is located inside Agent Studio under the Activity tab on Managed Agents that support this feature. The tab displays a badge showing the number of recent runs.

Q: What types of runs appear in the Activity Feed?

The Activity Feed displays both live chat conversations (marked with a chat bubble icon and "Chat" label) and automated trigger executions (marked with a lightning bolt icon and "Trigger" label), including runs initiated by form submissions, tag changes, and other automation events.

Q: How do I know if a run was successful or failed?

Each run displays a status indicator next to the status text. Use labels such as "Completed" or any visible error state to understand whether a run finished successfully or needs review.

Q: What information is included in the execution log?

The execution log includes the agent conversation view (showing the run summary, thinking time, and structured execution summary with numbered steps and data tables) and the execution timeline (showing every step the agent took, including LLM invocations, plugin usage, message steps, with timing and token usage for each step). Expand any step to view detailed inputs, outputs, and structured data.

Q: How do I debug a failed agent run?

Click the failed run in the Activity Feed to open its execution log. Review the run summary in the conversation view (left side) and each step in the execution timeline (right side) to identify where the failure occurred. Common issues include missing or incorrect inputs, unavailable tools or skills, unexpected data formats, or API errors. Use the timing and token metrics to identify performance bottlenecks, and expand individual steps to view detailed error messages or outputs.

Q: Can I filter or search the Activity Feed?

The Activity Feed currently displays runs in reverse chronological order (newest first). Check your interface for any available filtering or search options, as these capabilities may vary.

Q: What does the "View in Agent Logs" button do?

The "View in Agent Logs" button (located in the top right corner of an execution log) opens the full log in a separate view with additional screen space to review detailed execution data, timing metrics, token usage, and structured outputs.

Q: Can I export or download activity data?

Export availability may vary. Use "Copy ID" when available to reference a specific run in internal notes or support conversations.

Q: How long are activity logs retained?

Activity log retention may vary based on your HighLevel account settings. Check your account settings or contact HighLevel support for specific retention information for your plan.

Q: Can I see activity for multiple Managed Agents in one view?

The Activity Feed is specific to each individual Managed Agent. To view activity for multiple agents, navigate to each agent's Activity tab separately. The "View in Agent Logs" feature may provide broader logging capabilities across agents.

Q: What do the timing and token metrics mean?

Timing metrics show how long each step or the entire run took to execute. Token usage shows how many tokens (units of text processed by the AI model) were consumed during each step or the entire run. Use these metrics to identify slow steps, optimize agent performance, monitor AI usage, and ensure efficient execution.

### Related Articles

[Agent Studio Overview & Beginner Guide](<https://help.gohighlevel.com/support/solutions/articles/155000007393>) [How to Build Managed Agents with Natural Language](<https://help.gohighlevel.com/support/solutions/articles/155000007931>) [Agent Logs in HighLevel: Overview, Benefits, and Setup](<https://help.gohighlevel.com/support/solutions/articles/155000007657>) [How to Test and Debug AI Conversations in Agent Studio](<https://help.gohighlevel.com/support/solutions/articles/155000007425>) [Skills Platform for AI Agents](<https://help.gohighlevel.com/support/solutions/articles/155000008315>) [Agent Studio: Multi-Agent System Builder](<https://help.gohighlevel.com/support/solutions/articles/155000007609>)

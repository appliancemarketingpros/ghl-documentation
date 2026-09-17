# Todoist: Workflow actions & triggers

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008221-todoist-workflow-actions-triggers](https://help.gohighlevel.com/support/solutions/articles/155000008221-todoist-workflow-actions-triggers)  
**Category:** Workflows  
**Folder:** Getting Started w/ Workflows

---

**TABLE OF CONTENTS**

  * Overview
  * About the Integration
  * How to Set Up Todoist
    * Connect via the Workflow Builder (recommended)
    * Connect via Settings (alternative path)
  * List of Triggers
  * List of Actions
  * Example: Setting Up a Trigger (New incomplete task)
    * Step 1: Add the trigger
    * Step 2: Configure the trigger
    * Step 3: Test the trigger
  * Example: Setting Up an Action (Create task)
    * Step 1: Add the action
    * Step 2: Configure the action
    * Step 3: Test the action
  * How to Test Triggers and Actions
    * Test a trigger
    * Test an action
  * Common Use Cases
    * Use Case 1: Form submission → Todoist task in the right project
    * Use Case 2: Task completed → close the loop in the platform
    * Use Case 3: Team task with due date and label
  * Frequently Asked Questions


  


## Overview

Todoist is a task-management platform used by teams and individuals to organize work into projects, sections, and tasks, with support for labels, priorities, due dates, deadlines, comments, and collaboration. The Todoist integration brings these primitives into the Workflow Builder so task-lifecycle activity fires customer-facing automations, and any workflow can manage Todoist tasks and projects without leaving the builder.

  


## About the Integration

The integration ships with two halves:

  * Triggers (Todoist → Workflows): Three polling triggers — New incomplete task, New completed task, New project — all polling every 5 minutes.

  * Actions (Workflows → Todoist): Twelve actions covering task lifecycle (create, update, mark complete), task and project comments, project creation and section moves, discovery (find tasks, find projects, find user), and collaborator management (get collaborators, invite user).


All triggers and actions are flagged as premium workflow components — premium action credits apply at the standard automation rate. Todoist plan usage (projects, tasks, collaborators, integrations) is billed by Todoist directly on your Todoist account.

##   


## How to Set Up Todoist

Before any Todoist trigger or action can run, the integration has to be connected via OAuth.

### Connect via the Workflow Builder (recommended)

  * Open Automation → Workflows and pick (or create) a workflow.

  * Add a Todoist trigger or action — search for Todoist in the Apps tab.

  * Select any Todoist trigger or action.

  * On the panel, click Connect your account.

  * You will be redirected to Todoist’s OAuth authorization screen. Approve the requested scopes.

  * You will be returned to the Workflow Builder; the panel will update to show Connected.


### Connect via Settings (alternative path)

  * Go to Settings → Integrations.

  * Locate Todoist and click Connect.

  * Complete the OAuth flow.


  


  


  


## List of Triggers

All triggers poll Todoist every 5 minutes and surface matching records since the last poll, in order.

Trigger| What it does  
---|---  
New incomplete task| Fires when a new task is added to a project. Filterable by Project — only trigger for tasks in a specific project. Returns the task payload (title, note, due date, deadline, priority, labels, project, section).  
New completed task| Fires when an existing task is marked complete. Ideal for close-the-loop notifications and completion-driven downstream flows.  
New project| Fires when a new project is created in the connected account. Useful for automated project-kickoff bundles.  
  
  


##   


## ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075694732/original/MS5D_uPOTjNBpeiYgiyPcno7zdDlC8Gulg.png?1783677085)  


##   


## List of Actions

Actions are grouped by what they manage.

  


Task lifecycle

Action| Purpose  
---|---  
Create task| Creates a new task in Todoist with optional project, section, labels, priority, and due date. Required: Title. Defaults project to Inbox if not specified.  
Update task| Updates fields on an existing task by ID — title, note, due date, deadline, priority, labels.  
Mark task as completed| Marks an existing task as complete. Fires the New completed task trigger downstream for anyone listening on the same account.  
Move task to section| Moves an existing task into a specific section within its project.  
  
  


Comments

Action| Purpose  
---|---  
Add comment to task| Adds a comment to an existing task. Useful for annotating progress or attaching context from external systems.  
Add comment to project| Adds a comment at the project level rather than on a specific task.  
  
  


Projects

Action| Purpose  
---|---  
Create project| Creates a new Todoist project. Useful for automated onboarding — a new customer, a new engagement, a new sprint gets its own project scaffolded from a workflow.  
  
  


Discovery

Action| Purpose  
---|---  
Find tasks| Searches Todoist tasks by name, project, label, or filter. Returns matching tasks for downstream branching.  
Find projects| Lists projects in the connected account or filters by name. Returns project IDs — required upstream of Create task if the project isn’t Inbox.  
Find user| Looks up a Todoist user by name or email.  
  
  


Collaboration

Action| Purpose  
---|---  
Get project collaborators| Lists the users collaborating on a specific Todoist project.  
Invite user to project| Invites a user (by email) to collaborate on a project.  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075694768/original/I026zReVMox69rNesS9rWvtHpNRjngxxIQ.png?1783677118)  


  


## Example: Setting Up a Trigger (New incomplete task)

This walkthrough wires up a workflow that fires every time a new task is created in a specific Todoist project. The same configuration shape applies to New completed task and New project — only the trigger selection and applicable filters change.

### Step 1: Add the trigger

  * Open the workflow and click Add trigger.

  * Switch to the Apps tab and search for Todoist.

  * Select New incomplete task.


### Step 2: Configure the trigger

  * Connected Account — pick the Todoist account this trigger should watch.

  * Workflow Trigger Name — a meaningful label, e.g. ‘New Support Task’.

  * Filters → Project — pick a project to scope to (helper text reads ‘Only trigger for tasks in this project’). Leave empty to fire on tasks in any project.

  * Add filters (optional) — layer on additional conditions (label, priority, due-date range).


### Step 3: Test the trigger

  * Click Find new records inside the Test your trigger panel.

  * If no matching records appear, add a task to the target Todoist project and wait one polling cycle (5 minutes), then re-fetch.

  * Select the returned record as the mapping reference.

  * Click Save trigger.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075694779/original/uy7Ptn3KkAdPJF_8YlWCwsVNxR7elZ9OXA.png?1783677134)  


  


## Example: Setting Up an Action (Create task)

This walkthrough creates a Todoist task from a workflow event — the most common outbound-to-Todoist pattern.

### Step 1: Add the action

  * Inside the workflow, click Add to insert a new step.

  * Open the Apps tab and select Todoist.

  * Choose Create task from the action list.


### Step 2: Configure the action

  * Connected Account — pick the Todoist account where the task should be created.

  * Action Name — e.g. ‘Create Task from Form Submission’.

  * Project — pick from the dropdown. Defaults to Inbox if not specified. Use Find projects upstream to resolve the project ID from a project name if it isn’t known at build time.

  * Title (required) — the task title. Keep it concise for clean rendering in Todoist’s task lists.

  * Note — a detailed description for the task, if the title alone doesn’t carry enough context.

  * Due Date (Human Formatted) OR Due Date (Raw Formatted) — pick one, not both. See ‘Working with Due Dates and Deadlines’ above.

  * Deadline Date (optional) — hard deadline in YYYY-MM-DD. Todoist deadlines don’t support a time component.

  * Priority — P1 (red, highest) to P4 (grey, lowest, default).

  * Labels — one or more labels. Labels must exist in the Todoist account first.


### Step 3: Test the action

  * Click Test action.

  * Confirm — this creates a real task in Todoist. Use a clearly-marked title (‘TEST — DELETE’) if testing against a production project.

  * Save the action and run a full Test workflow before publishing.


  


## How to Test Triggers and Actions

Always test before publishing. Testing locks the payload schema and gives downstream steps a real record to map against.

### Test a trigger

  * Inside the trigger panel, click Find new records.

  * If no matching records appear, create or complete a task in Todoist (or create a project) and wait one polling cycle (5 minutes), then re-fetch.

  * Select the returned record as the mapping reference.


### Test an action

  * Inside the action panel, click Test action.

  * The action runs against the live Todoist account — real tasks, comments, or projects are created.

  * Verify in Todoist and clean up test records afterwards.


##   


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075694804/original/XthgUGHj0h0kMhDc6aaCB_XgRx--ldwT4g.png?1783677150)

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075694814/original/R0KN7bNHdSnfea-KrV0u4s66yGt23Dwp4g.png?1783677159)

##   


## Common Use Cases

### Use Case 1: Form submission → Todoist task in the right project

Goal: Route inbound requests into Todoist as tasks with the right project, labels, and priority.

Workflow Setup:

  * Trigger: Form submission

  * Optional: Branch on form input to determine the right project or priority

  * Action: Find projects (resolve the target project ID by name)

  * Action: Create task (title from form, note with the full submission body, priority based on urgency signal, labels for team routing)


Example: A customer submits a support request marked ‘urgent’. The workflow finds the ‘Support Backlog’ project and creates a P1 task with the full request as the note, labeled ‘external-report’ — the support lead sees it in Todoist within seconds without leaving their task list.

### Use Case 2: Task completed → close the loop in the platform

Goal: Take action when a Todoist task is marked complete.

Workflow Setup:

  * Trigger: New completed task (filter by project)

  * Action: Match the task back to the originating CRM contact (via a stored task ID or a label carrying the contact reference)

  * Action: Update contact / send notification / advance a stage


Example: A ‘Follow up with Acme’ task is marked complete in the AE’s Todoist. Within 5 minutes, the CRM contact’s custom field is updated (‘last touched: today’) and the deal stage is bumped — Todoist stays the AE’s working list, and the CRM records get updated for free.

### Use Case 3: Team task with due date and label

Goal: Create a task on a shared project with proper metadata for routing and reporting.

Workflow Setup:

  * Trigger: Any operational event needing follow-up

  * Action: Create task (Project = shared team project, Priority = P2, Labels = ‘needs-review’)

  * Action: Add comment to task (context / links / instructions)


Example: A signup-abandonment automation creates a task in the CS team’s Todoist project with a note linking to the abandoned session, priority P2, and label ‘needs-review’ — a CS agent picks it up within their normal workflow.

  


  


## Frequently Asked Questions

Q: What is Todoist?

Todoist is a task-management platform used by individuals and teams to organize work into projects, sections, and tasks — with support for labels, priorities, due dates, deadlines, comments, and collaborators. Free and paid tiers are available; paid plans unlock features like reminders, larger attachments, more collaborators, and advanced filters.

Q: Are Todoist triggers and actions premium workflow components?

Yes. All three triggers and all twelve actions are flagged as premium and consume premium action credits at the standard automation rate. Todoist plan usage (projects, tasks, collaborators, integrations) is billed by Todoist directly on your Todoist account.

Q: Are the triggers instant or polled?

Polled. All three triggers poll Todoist every 5 minutes and return matching records since the last poll, in order.

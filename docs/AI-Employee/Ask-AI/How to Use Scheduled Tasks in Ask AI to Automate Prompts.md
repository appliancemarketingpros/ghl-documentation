# How to Use Scheduled Tasks in Ask AI to Automate Prompts

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007966-how-to-use-scheduled-tasks-in-ask-ai-to-automate-prompts](https://help.gohighlevel.com/support/solutions/articles/155000007966-how-to-use-scheduled-tasks-in-ask-ai-to-automate-prompts)  
**Category:** AI Employee  
**Folder:** Ask AI

---

Ask AI - Task Scheduler makes your AI work for you around the clock. Instead of opening Ask AI and asking the same questions every day, you can schedule prompts to run automatically and review the results when it fits your schedule.

* * *

**TABLE OF CONTENTS**

  * What is Ask AI - Task Scheduler?
  * Key Benefits of Ask AI - Task Scheduler
  * Scheduled Tasks Workspace
  * Task Frequencies, Timezones, and Cron Schedules
  * Run History and Result Indicators
  * Task Lifecycle: Active, Paused, and Cancelled
  * Manual Runs with “Run now”
  * Creating Scheduled Tasks from Chat and Voice
  * How To Setup Ask AI - Task Scheduler
  * Frequently Asked Questions
    * Related Articles


* * *

# **What is Ask AI - Task Scheduler?**

Ask AI - Task Scheduler (also called **Scheduled Tasks**) is a feature inside the Ask AI workspace that lets you tell Ask AI what to do and _when_ to do it—hourly, daily, weekly, on weekdays only, or at any custom cron time. Once a task is scheduled, Ask AI runs the prompt automatically in the background and saves the results to a run history, so you can come back and review them without keeping a chat session open.

Ask AI itself is a built‑in AI workspace in HighLevel that helps you create content, answer questions, and take supported actions directly inside the platform through natural language prompts or voice. Task Scheduler extends this workspace with time‑based automation so your favorite Ask AI prompts become always‑on assistants.

* * *

## **Key Benefits of Ask AI - Task Scheduler**

Ask AI - Task Scheduler turns recurring questions and check‑ins into automated, reliable routines. These benefits help agencies and businesses stay informed without adding manual work to their day.

  * **Recover hours every week:** Automate daily summaries, weekly pipeline reports, follow‑up reminders, and recurring health checks that you’d otherwise trigger manually in Ask AI.


  


  * **Always get insights at the right moment:** Schedule prompts like “Summarize yesterday’s new contacts” for early morning, “Send me a weekly pipeline report” for Monday before your team sync, or “Recap today’s appointments” for the end of day.


  


  * **Hands‑free productivity (including voice):** Turn spoken instructions into scheduled tasks while commuting, between meetings, or away from your keyboard—Ask AI already supports voice input for hands‑free commands.


  


  * **Better visibility across multiple sub‑accounts:** Agencies can set up per‑location daily or weekly check‑ins to spot missed appointments, drop‑offs, or stalled opportunities without manually pulling each report.


  


  * **Faster onboarding for new team members:** New staff can rely on scheduled AI recaps and reports from day one, gaining the same insights experienced team members use—without needing to learn every report and screen.


  


  * **More value from your existing AI:** The same Ask AI subscription now powers scheduled insights 24/7, increasing the business outcomes you get from the AI you’re already paying for.


* * *

## **Scheduled Tasks Workspace**

The Scheduled Tasks workspace is where you create, review, and manage every Ask AI task that runs on a schedule. It provides a high‑level overview of what will run next and which tasks have fresh results waiting for you.

In the Ask AI workspace (Agency or sub‑account, depending on your access), you’ll find a **Scheduled Tasks** area that typically includes:

  * **Task list**
    * Each row represents one scheduled task.
    * Common columns include:
      * **Name** – e.g., “Daily new‑contacts summary”
      * **Frequency** – e.g., Hourly, Daily, Weekdays, Weekly, Cron, or One‑time
      * **Next run** – date/time of the next execution, shown in your local timezone
      * **Status** – Active, Paused, or Cancelled
      * **New result indicator** – a badge or marker when a new run has completed and hasn’t been opened yet.


  


  * **Task actions**
    * Quick actions on each task such as:
      * **Run now**
      * **Pause / Resume**
      * **Edit**
      * **Delete**


* * *

## **Task Frequencies**

Choosing the right schedule ensures your AI delivers insights exactly when they’re most useful before morning stand ups, ahead of client calls, or right after business hours.

When you create or edit a scheduled task, you’ll choose from these options:

  * **Hourly**
    * Runs the prompt every hour.
    * Helpful for near‑real‑time monitoring (e.g., “Check failed appointments in the last hour.”).


  


  * **Daily**
    * Runs once per day at a specific time and timezone you choose.
    * Great for daily dashboards like new contacts, appointments, or tasks created “yesterday.”


  


  * **Weekdays**
    * Runs Monday through Friday at your chosen time.
    * Ideal for workday‑only summaries, such as weekday pipeline or lead reports.


  


  * **Weekly**
    * Runs on a chosen day of the week and time (e.g., every Monday at 10:00 AM).
    * Perfect for weekly performance reviews, campaign summaries, or account health reports.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071494345/original/nPZvpJWBtuZB-zwS8MFhJONq22-WOrGQ9Q.png?1778990956)

* * *

## **Run History and Result Indicators**

Run history turns each scheduled task into a transparent log of everything Ask AI has done—successful runs, failures, skips, and manual executions.

Each task stores a chronological **run history** , where you can:

  * **See every “fire” of the task**


  


  * **Successful:** the prompt executed and returned results.


  


  * **Failed:** Ask AI could not complete the run (for example, due to missing permissions or transient errors).


  


  * **Skipped:** a scheduled run was intentionally bypassed (e.g., while the task was paused at its scheduled time).


  


  * **Open completed runs**


  


  * Click any completed entry to open the full Ask AI session tied to that run.


  


  * Review summaries, reports, or downstream actions (e.g., emails sent, opportunities updated) just like any other Ask AI chat.


  


  * **Track new results**


**  
**

  * A**“new result”** indicator appears when a run has finished but hasn’t been opened.


  


  * Opening the run automatically marks it as read and removes the badge, helping you stay on top of what’s new.


This history makes it easy to answer questions like “Did yesterday’s pipeline report run?” or “What exactly did Ask AI do during the last weekly check‑in?”

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071494302/original/_y-8kV7eGqnRPxefZpEdxWbRPlVfBrOLEg.png?1778990788)

* * *

## **Task Lifecycle: Active, Paused, and Cancelled**

Task statuses reflect where each scheduled task is in its lifecycle so you can safely stop or retire tasks without losing important history.

  


  * **Active**
    * The task runs according to its schedule (Hourly, Daily, etc.).
    * New runs are added to history and may show a “new result” badge until opened.


  


  * **Paused**
    * The task temporarily stops running at its scheduled times.
    * Any fires that would have occurred while paused are **skipped** , and these skip events are still visible in run history.
    * You can **Resume** when you want to restart the schedule.


  


  * **Cancelled / Deleted**
    * Cancelling or deleting a task removes it from the active list and stops all future runs.
    * The historical runs remain available where supported, so you can still review past results even after you’ve retired the task.


This lifecycle makes it safe to experiment—create tasks for seasonal campaigns, temporarily disable them when not needed, and clean up old tasks without losing past insights.

* * *

## **Manual Runs with “Run now”**

Sometimes you don’t want to wait for the next scheduled time. The **Run now** option lets you trigger an on‑demand execution while preserving the existing schedule.

  


Key behaviors:

  * **Run any time**
    * Click **Run now** on any task whether it’s **Active** or **Paused**.


  


  * **Fresh Ask AI session**
    * Manual runs use a fresh Ask AI session, so the results are independent of previous scheduled runs.
    * In history, manual runs are clearly labeled, so you can distinguish them from scheduled executions.


  


  * **Schedule remains unchanged**
    * The recurring schedule is **not** shifted or reset.
    * The next scheduled fire still occurs at the originally defined time.


This is ideal when you’ve just updated a report prompt and want to see the new output immediately or when leadership needs the latest data before the scheduled report time.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071494294/original/1Vsf8_G-qnPhYeNtnt-9BK8yiKjFVeTISA.png?1778990687)

* * *

## **Creating Scheduled Tasks from Chat and Voice**

Ask AI - Task Scheduler doesn’t require you to leave your conversation. You can turn natural language prompts—typed or spoken directly into scheduled tasks.

Ask AI already supports typed and voice prompts in the Ask AI workspace, making it simple to create and manage work through natural language.

**From Ask AI chat**

While chatting with Ask AI, you can “promote” a one‑off question into a recurring task just by asking:

  * Example prompts:
    * “Run a summary of new contacts every weekday at 9 AM.”
    * “Send me a pipeline report every Monday at 10 AM.”
    * “Email Sarah a check‑in reminder on June 1st at 9 AM.”


Ask AI interprets the instruction, builds the corresponding schedule, and saves it to **Scheduled Tasks** automatically.

**From voice mode**

If voice mode is enabled in your account:

  1. Start a **voice conversation** with Ask AI.
  2. Speak a schedule request, such as:
     * “Every weekday at 9 AM, give me a summary of new contacts.”
  3. Ask AI confirms the schedule out loud, including the **next run time** , and saves it to Scheduled Tasks.


This natural scheduling flow is especially helpful when you’re mobile or multitasking and don’t want to manually configure forms.

* * *

## **How To Setup Ask AI - Task Scheduler**

Proper setup ensures your scheduled tasks run reliably, use clear prompts, and respect the right timezone. The steps below cover creating tasks through the Scheduled Tasks form, from chat, and using voice.

  


### **1\. Create a task from the Scheduled Tasks tab**

Use the tab when you want full control over the schedule and prompt details from the start.

  1. Open **Ask AI** from the top navigation or left sidebar.
  2. Go to **Scheduled Tasks**.
  3. Click **+** **New task**.
  4. Fill in the form:
     * **Name**
       * A descriptive label such as **“Daily new‑contacts summary”** or **“Monday pipeline review”**.
     * **Prompt**
       * The exact instruction Ask AI should run, for example:
         * “Summarize all new contacts added yesterday, highlighting source, status, and next steps.”
         * “List opportunities in the pipeline that haven’t moved in 7 days and suggest next actions.”
     * **Frequency**
       * Choose **Manually,****Hourly** , **Daily** , **Weekdays** , **Weekly**.
  5. Click **Save**.
     * The task appears in the list with its **Next run** time shown in your local timezone.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071486978/original/ns_ZZIxFKvbgMI9PdOOKtWkyCw_ZId7atQ.png?1778950181)

  


### **2\. Create a task from Ask AI chat**

When a one‑off question proves useful, turn it into a scheduled task without leaving the conversation.

  1. Open **Ask AI** and start a chat.
  2. Type your request combining what you want and how often you want it, for example:
     * “Run a summary of new contacts every weekday at 9 AM.”
     * “Send me a pipeline report every Monday at 10 AM.”
  3. Ask AI interprets the schedule, confirms details, and saves it into **Scheduled Tasks**.
  4. Open **Scheduled Tasks** to see the new entry, adjust the name or prompt if needed, and confirm the **Next run** time looks correct.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071487174/original/mHxj3OpSdnnDzZz_LIsshHMqVdkgdErIWw.gif?1778950669)

###   


### **3\. Create a task using voice**

If voice input is available in your account, you can set up tasks hands‑free.

  1. Start a voice conversation with **Ask AI**.
  2. Speak your schedule in natural language, such as:
     * “Every weekday at 9 AM, give me a summary of new contacts.”
  3. Ask AI repeats back the schedule and next run time for confirmation.
  4. Visit **Scheduled Tasks** later to fine‑tune the prompt or schedule if needed.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071487667/original/fWqhVMnVI_AtCU_W8lqBeE0RHC449cOpEQ.gif?1778951950)

  


### **4\. Manage existing tasks**

Once tasks exist, keep them tuned to your workflow:

  * **Pause / Resume**
    * Pause when a report isn’t needed (e.g., during holidays or between campaigns).
    * Resume to restart the schedule—upcoming fires run as usual.


  


  * **Edit**
    * Update **Name** , **Prompt** , **Frequency** at any time.
    * The next scheduled fire automatically uses the new values.
    * Any pre‑update background jobs that might conflict are gracefully skipped, preventing duplicate runs during the changeover.


  


  * **Run now**
    * Use **Run now** for an immediate, one‑off execution without altering the underlying schedule.


  


  * **View run history**
    * Open past runs for auditing, troubleshooting, or comparing results over time.


  


  * **Delete**
    * Remove tasks you no longer need.
    * Future runs are cancelled, and the task is removed from the active list.


  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071494432/original/yUd71wTpzpXCKh5uR8Vg1ovqD1Du3UJucg.gif?1778991668)

* * *

## **Frequently Asked Questions**

**Q: Do I need a specific plan or add‑on to use Ask AI - Task Scheduler?**

Ask AI is available to Agency Admins/Users and to Sub‑account Admins/Users on the Unlimited AI Employee plan. Scheduled Tasks follows the same underlying Ask AI availability—if you can open Ask AI in a given account and see the Scheduled Tasks area, you can use Task Scheduler there.

**Q: Where do I see the results of a scheduled task?**

All results are stored under the task’s **Run history** in **Ask AI > Scheduled Tasks**. Click any completed run to open the associated Ask AI session and review the full output.

**Q: Does Task Scheduler automatically email or notify me when a task runs?**

By default, Task Scheduler focuses on running the prompt and saving the result. Notifications or emails only occur when your prompt explicitly instructs Ask AI to send them (and your account has the necessary messaging capabilities configured).

**Q: Do scheduled runs count toward Ask AI usage and billing?**

Yes. Each scheduled execution is effectively an Ask AI session under the hood and contributes to your AI usage just like a manually triggered Ask AI request. For examples of how sessions are counted and costed, refer to the Ask AI Sessions Pricing overview.

**Q: What happens if a scheduled run fails or is skipped?**

The run will appear in **Run history** as **Failed** or **Skipped**. You can open the entry (when details are available) to understand what happened and then use **Run now** after fixing the underlying issue or adjusting the prompt.

**Q: Can multiple team members manage the same scheduled tasks?**

Visibility and control follow your normal Ask AI and sub‑account permissions. Team members who have access to Ask AI and the relevant account will typically be able to see and manage scheduled tasks, subject to their role and permission settings in HighLevel.

**Q: Can I change the timezone or schedule without recreating the task?**

Yes. Use **Edit** to update the frequency, time, or timezone. The next scheduled run will automatically use the new configuration, and background tasks are handled to prevent double‑runs at the moment of editing.

**Q: Do I have to use Cron, or can I stick to simple schedules?**

Cron is optional and intended for advanced timing patterns. Most users can rely on the built‑in **Hourly** , **Daily** , **Weekdays** , **Weekly** , and **One‑time** options for common business schedules.

* * *

###  **Related Articles**

  


  * [Introduction to Ask AI Assistant](<https://help.gohighlevel.com/a/solutions/articles/155000005327?portalId=48000045315>)


  


  * [Contact Summary Agent in Ask AI](<https://help.gohighlevel.com/a/solutions/articles/155000005484?portalId=48000045315>)


  


  * [How to Generate and Edit Images Using Ask AI](<https://help.gohighlevel.com/a/solutions/articles/155000005764?portalId=48000045315>)


  


  * [Conversational Editing of Content with Ask AI](<https://help.gohighlevel.com/a/solutions/articles/155000005765?portalId=48000045315>)


  


  * [Ask AI + Agent Studio Integration](<https://help.gohighlevel.com/a/solutions/articles/155000006677?portalId=48000045315>)


  


  * [Ask AI Sessions Pricing Overview](<https://help.gohighlevel.com/a/solutions/articles/155000007818?portalId=48000045315>)

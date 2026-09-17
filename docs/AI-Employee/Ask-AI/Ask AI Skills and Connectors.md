# Ask AI Skills and Connectors

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008434-ask-ai-skills-and-connectors](https://help.gohighlevel.com/support/solutions/articles/155000008434-ask-ai-skills-and-connectors)  
**Category:** AI Employee  
**Folder:** Ask AI

---

Ask AI

# Ask AI Skills and Connectors

Connect Ask AI to your favorite apps and teach it your workflows—with complete control over every tool and instruction.

What You'll Learn

Ask AI Connectors let you link your Notion, Canva, GitHub, HubSpot, or any Model Context Protocol (MCP) app directly to Ask AI. You authenticate once, grant per-app or per-tool permissions, and Ask AI acts inside your accounts—securely, without exposing credentials.

Ask AI Skills let you codify how you want work done. Write a custom instruction set, upload an existing playbook or SOP, and Ask AI will apply it automatically when your request matches—or on demand via the **/** command in any text or voice chat.

Table of Contents

1

What Are Connectors?

2

What Are Skills?

3

How to Connect an App

4

How to Create or Upload a Skill

5

Security and Reliability

6

Frequently Asked Questions

1

## What Are Connectors?

Connectors let Ask AI act inside the apps you already use—Notion, Canva, GitHub, HubSpot, or any app in the Model Context Protocol (MCP) marketplace. You authenticate under your own login (not a sub-account's), and Ask AI can read, create, update, or search within the connected service on your behalf.

Every connector is linked to your user account within a company, so your credentials and tool selections never leak across agency or sub-account boundaries.

**Marketplace browser in Ask AI** — Open **Customize → Connectors → Manage Connectors** to browse and connect any MCP app without leaving Ask AI.

**Per-app and per-tool control** — Toggle an entire connector on or off, or pick exactly which tools (e.g., "create page", "search database") the AI may invoke.

**Two-way sync with the marketplace** — Connect an app anywhere in HighLevel and it appears in Ask AI ready to use. Renames and new icons follow automatically; your enable/tool choices are preserved.

**Browser Control connector** — Enable the Browser Control connector to let Ask AI open pages, click, fill forms, and complete multi-step tasks in Chrome, Edge, Brave, or Arc (requires the Ask AI Chrome extension).

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078134050/original/2zJmC3T6KiF9fhBcEnBAqd6Y4_8J9cbTxg.gif?1786453754)

2

## What Are Skills?

Skills teach Ask AI how you want work done. A Skill is a named instruction set that Ask AI applies whenever your request matches—or that you invoke on demand by typing **/skill-name** in the composer. Skills work in both text and voice chats.

You can write a Skill from scratch, upload an existing markdown playbook, or ask Ask AI to create one during a conversation. Once saved, a Skill becomes part of your personal library and is matched automatically when relevant.

**Write a Skill** — In **Customize → Skills** , provide a name, a one-line "use when…" trigger, and a markdown body that describes the process Ask AI should follow.

**Upload a Skill** — Drop a .md file and Ask AI reads it, names it, and summarizes it for you. Uploading the same file twice creates a versioned copy (e.g., "PDF Processing 2") instead of overwriting.

**Invoke on demand** — Type **/** in the composer to see your Skills library and pin a specific Skill to that message, bypassing automatic matching.

**Enable, disable, or remove** — A disabled Skill stays in your library but is invisible to Ask AI until re-enabled. You can also delete a Skill permanently.

**Self-maintaining Skills** — When you say "save this as a skill," Ask AI writes one. If a Skill turns out to be wrong mid-conversation, Ask AI can correct it iteratively, creating a self-learning workflow.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078134848/original/mrXn_a9G2sj22MNNiAXDOLxo-aITnquJyg.png?1786454006)

Security First

No credentials are stored or shown to the AI

Ask AI stores only a reference to your connected account. Access tokens are minted per call, never persisted, and never logged.

3

## How to Connect an App

Follow these steps to link a new connector to Ask AI and configure which tools it may use.

Step 1

Open the Connectors panel

Click the **plus** icon in the Ask AI sidebar, then select **Connectors**.

Step 2

Browse the marketplace

Click **Manage Connectors** to open the MCP app browser. Search or scroll to find the app you want—Notion, GitHub, Canva, HubSpot, Cal.com, and more.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078135225/original/uoppXEf_H2yu9SZRU6NEiNtT2TvUV5T30g.png?1786454111)

Step 3

Connect your account

Select the app and click **Connect**. You'll be redirected to authenticate with the service. Once authorized, the app appears in your **Connected apps** list.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078135464/original/WZA1XBtJp0VYHaI2S68yrWpxrbZa1qn8NA.png?1786454187)

Step 4

Configure tools (optional)

Click the app name in **Connected apps** to see the full list of tools it offers. Toggle **All tools** off to individually enable only the actions you want Ask AI to use (e.g., **notion-search** , **notion-create-page**).

Step 5

Enable the connector

Flip the toggle next to the app name to **Enabled**. Ask AI will now use that connector when fulfilling your requests.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078135619/original/jZg98NjxdE8oXFmlYxn7DY4vTlDWhoAUgA.png?1786454246)

Quick Tip

You can also access the connector toggle from the composer **+** menu at the bottom of any Ask AI chat.

4

## How to Create or Upload a Skill

You can create a Skill in three ways: let Ask AI write it for you, upload an existing document, or write it manually. Once created, you can enable, disable, or delete Skills at any time.

Option 1: Create with Ask AI

Step 1

Start a chat and describe your workflow

In any Ask AI conversation, say something like "Save this as a skill: When I ask you to generate a PDF report, use the following steps…" Ask AI will draft the Skill for you.

Step 2

Review and confirm

Ask AI shows you the generated Skill. Confirm to add it to your library, or refine it by providing more detail.

Option 2: Upload a Skill file

Step 1

Navigate to Skills

Click **Customize → Skills** in the Ask AI sidebar.

Step 2

Upload your .md file

Click **Upload a skill** and select a markdown file. Ask AI reads it, proposes a name and one-line summary, and adds it to your library. Uploading the same file twice creates a versioned copy (e.g., "Report Generation 2").

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078135891/original/of7La46H-Ro1D3Itya7x3xA14-4sJaVaiw.png?1786454353)

Option 3: Write a Skill manually

Step 1

Click Write skill instructions

In **Customize → Skills** , click **Write skill instructions**.

Step 2

Fill in the form

Provide a **Name** , a **Use when…** trigger description (one line), and a **Markdown body** with the full process Ask AI should follow.

Step 3

Save

Click **Save**. Your new Skill appears in the library and is enabled by default.

Managing Skills

Invoke on demand

Type / to pick a Skill

In the Ask AI composer, type **/** and select a Skill from the dropdown. That Skill will be pinned to your message, bypassing automatic matching.

Disable or remove

Toggle or delete from the library

In **Customize → Skills** , toggle a Skill off to hide it from Ask AI without deleting it. Click the trash icon to remove it permanently.

Iterative Correction

If a Skill produces the wrong output mid-conversation, Ask AI can correct it on the fly. Provide feedback ("That didn't work; update the Skill to…"), and Ask AI will revise the Skill instructions iteratively.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078135971/original/Euz__p9EYFw5K8T4VTeD4Yc0ZD44P8tqJQ.png?1786454401)

5

## Security and Reliability

Ask AI Connectors and Skills are designed to be secure by default and resilient to common failure modes. Your credentials, tools, and instructions are scoped to your user account and never shared across organizational boundaries.

Your library is yours

User-scoped storage

Skills and connector settings are keyed to your user within a company. Agency and sub-account scopes never leak into each other.

No credentials in Ask AI

Token-less architecture

Ask AI stores only a reference to your connected account. Access tokens are minted per call, never persisted, never shown to the AI, and never logged.

Isolated connector execution

A broken connector can't break your chat

Each app is isolated, so one failing integration is dropped for that turn while everything else keeps working.

Self-healing connections

Automatic account repair

If a connected account is rotated or reconnected elsewhere in HighLevel, Ask AI finds the healthy reference and repairs the saved setting on its own.

Privacy by Design

No connector or Skill data is shared across users, sub-accounts, or agencies. Your connections and instructions remain private to you.

6

## Frequently Asked Questions

Q: Are Connectors and Skills available on all HighLevel plans?

Connectors and Skills are part of Ask AI, which is available to all HighLevel users. Specific MCP apps in the marketplace may have their own authentication or subscription requirements.

Q: Can I connect the same app to multiple HighLevel accounts?

Yes. Connectors are user-scoped, so you can connect different app accounts in different HighLevel sub-accounts or agencies. Each connection is independent and isolated.

Q: How do I revoke access to a connector?

Toggle the connector off in **Customize → Connectors** , or disconnect it via **Manage Connectors**. You can also revoke access from the third-party app's settings (e.g., Notion's integrations page).

Q: What happens if I upload a Skill file twice?

Ask AI creates a versioned copy with a number suffix (e.g., "Report Generation 2") instead of overwriting the original. You can then enable, disable, or delete any version.

Q: Can I share a Skill with my team?

Skills are currently user-scoped. To share, export your Skill as a .md file (copy the markdown body) and have your teammate upload it to their own Ask AI library.

Q: Does Ask AI use my connector credentials for training?

No. Connector credentials and access tokens are never logged, never shown to the AI model, and never used for training. Ask AI sees only the data returned by the tool call, which it uses to fulfill your request.

Q: What is the Browser Control connector?

Browser Control lets Ask AI open pages, click, fill forms, and complete multi-step tasks in a supported Chromium-based browser (Chrome, Edge, Brave, Arc). You must install the Ask AI Chrome extension to enable this connector.

Q: How does Ask AI decide which Skill to use?

Ask AI matches your request against the "use when…" triggers of all enabled Skills. If multiple Skills match, it picks the best fit. You can override automatic matching by invoking a Skill with **/skill-name**.

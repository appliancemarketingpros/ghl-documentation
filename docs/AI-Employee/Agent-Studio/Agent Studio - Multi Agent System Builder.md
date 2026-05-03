# Agent Studio - Multi Agent System Builder

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007609-agent-studio-multi-agent-system-builder](https://help.gohighlevel.com/support/solutions/articles/155000007609-agent-studio-multi-agent-system-builder)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

Agent Studio is HighLevel’s visual, no-code/low-code builder for AI-driven multi-agent systems. With drag-and-drop nodes, conditional routing, and built-in testing, you can launch sophisticated workflows that blend autonomous AI reasoning with deterministic logic without writing a single line of code. 

* * *

**TABLE OF CONTENTS**

  * What is Agent Studio?
  * Key Benefits of Agent Studio
  * Visual Agent Builder
  * Node Types
  * Conditional Routing
  * Knowledge Base for RAG
  * Global Variables & Runtime Inputs
  * Version Control
  * Testing & Deployment
  * Pricing
  * How to Set Up Agent Studio
  * Frequently Asked Questions
    * Related Articles


* * *

# **What is Agent Studio?**

  


Agent Studio is a canvas-style builder that lets you orchestrate multiple AI agents and rule-based steps inside one workflow. Each agent can access LLMs, knowledge bases, web search, third-party APIs, and more, while sequential nodes handle predictable tasks such as validation or form capture. The result is a single, unified automation that can think, decide, and act on your behalf.

* * *

## **Key Benefits of Agent Studio**

Designing in Agent Studio unlocks:

  


  * Visual drag-and-drop creation—no code required.


  


  * Hybrid automation that mixes AI reasoning with deterministic logic.


  


  * Conditional edges that branch intelligently based on variables or AI intent.


  


  * Version control with one-click publish and rollback for safe iteration.


  


  * Built-in testing so you can validate logic before going live.


  


  * Free tier for unlimited agents; pay only for LLM tokens.


* * *

## **Visual Agent Builder**

The canvas provides an intuitive way to map out entire workflows: drag nodes onto the grid, connect them with edges, and rename or reorder anything via right-click context menus. Cleaner node layouts and updated connection lines make even large systems easy to follow at a glance.

* * *

## **Node Types**

Agent Studio ships with two core nodes that you can combine freely:

  


  * **AI Agent Node:** Connect LLM prompts to tools like Web Search, Knowledge Base Search, GenAI, or external APIs for dynamic reasoning, content generation, and data look-ups.


  


  * **Sequential Node:** Perform rule-based actions such as API calls, form validation, or webhook triggers when you need absolute control and repeatability.


* * *

## **Conditional Routing**

Instead of separate “router” blocks, edges themselves hold the logic. Write simple expressions (e.g., `orderTotal > 500`) or use AI intent matching to decide which downstream node should fire. This keeps flows compact while enabling highly granular branching.

* * *

## **Knowledge Base for RAG**

Attach multiple knowledge sources like PDFs, CSVs, FAQs, or full websites to any AI Agent Node. Retrieval-augmented generation (RAG) ensures answers are grounded in your content while still benefiting from LLM creativity. You can even set source-level filters for surgical precision.

* * *

## **Global Variables & Runtime Inputs**

Store API keys, environment constants, or branding guidelines once, then reference them anywhere in the workflow. Pass runtime variables (e.g., `locationId`, `userId`) from the calling app or chat session so every execution feels personal.

* * *

## **Version Control**

Every save creates a draft. When you’re ready, publish to Production with one click or instantly roll back to any prior version if something breaks, no separate Git flow required.

* * *

## **Testing & Deployment**

The Test panel lets you run the entire agent, including LLM calls and tool invocations before a single end-user ever sees it. Once verified, deploy to Ask AI immediately; additional channels (web widgets, API endpoints, etc.) are coming soon.

* * *

## **Pricing**

Free Tier: nlimited agents, free Knowledge Base & non-AI executions.

Paid Usage: pay only for LLM tokens at published API rates.

* * *

## **How to Set Up Agent Studio**

Building your first multi-agent workflow is straightforward:

### **Step 1: Navigate to Agent Studio**

  * From your HighLevel dashboard, click **AI Agents** in the left sidebar

  * Select the **Agent Studio** tab


  


You will land on the Agent Studio dashboard where all your agents are listed.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155068691956/original/oM306XL0CLGv43shlHNkdwRI8W9yP5nnWA.png?1775648710)

  


  


### **Step 2: Create a New Agent**

  * Click **\+ Create Agent** in the top-right corner


  


This opens the **canvas** , which is your workspace for building workflows.

  


**What you’re seeing:**

  * Left panel → Available nodes (building blocks)

  * Center → Canvas (where you build your workflow)

  * Right panel → Settings (where you configure each step)


  


Click Create Agent to open the blank canvas.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155068692017/original/8yryGHr1gcrGUVwlxlaKSkmXNoZHxKDsFA.png?1775648766)

  


  


### **Step 3: Add an AI Agent Node**

  


AI Agent Nodes are the core of your workflow. They allow your agent to think, generate responses, and use tools like Knowledge Base or Web Search.

  


  * From the left panel, drag **AI Agent** onto the canvas


  


This node will handle conversations and decision-making.

  


### **Step 4: Configure the AI Agent**

  


Click on the AI Agent node to open its settings panel.

  


Fill in the following:

  


  * **Model** : Select the recommended model (e.g., GPT-4.1)

  * **Prompt** : Define how the agent should behave


  


**Example Prompt :**

  


You are a helpful assistant for a business. Answer user questions clearly and politely. If you don’t know the answer, ask for more details.

  


The prompt acts as the “instructions” for your AI agent. It directly controls how the agent responds.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155068695833/original/WdcKZtDBJdclP99zJGfyc2KoPxK1Kpdyag.png?1775650445)

  


  


### **Step 6: Connect the Flow**

  


Workflows run from one step to another using connections.

  


  * Click and drag from the small connector dot on the node

  * Connect it to the next step (or leave it as a single-node flow for now)


  


If no condition is added, the flow simply continues to the next step automatically.

  


### **Sequential Nodes**

  


Sequential Nodes are used for structured, rule-based actions like API calls or validations.

  * Drag a **Sequential Node** from the left panel if needed


  


  


### **Step 8: Add Variables (Optional but Powerful)**

  


Variables allow you to reuse values like names, IDs, or API keys across your workflow.

  * Click **Variables** at the top of the screen

  * Add a new variable under the **Global** tab


  


Example use cases:

  * Store API keys

  * Pass user-specific data

  * Personalize responses


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155068780592/original/1EqRgv45V7WIqYy6nHiVxlARwFeIfSKLkw.png?1775731777)

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155068780696/original/fYooQZNYO0pXaMWPQksXYxh5B9OisBsRtA.png?1775731814)

  


  


### **Step 9: Test Your Agent**

  


Testing ensures your agent behaves correctly before going live.

  * Click the **Test** button at the top

  * Enter a sample question (e.g., “What services do you offer?”)


  


Review:

  


  * Response quality

  * Tool usage (if added)

  * Flow behavior


###   


### **Step 10: Publish Your Agent**

  


Once you’re satisfied with the results:

  


  * Click **Publish → Production**


* * *

## **Frequently Asked Questions**

  


**Q: Who can access Agent Studio in my account?**

Agency Admins/Users and Subaccount Admins/Users with the proper role permissions can build and manage agents.

  


**Q: Does every edge need a condition?**

No. If you omit a condition, the edge behaves like a default “next” step.

  


**Q: Can one agent call another agent?**

Yes, simply place the second agent inside an AI Agent Node as a sub-workflow or trigger it via API from a Sequential Node.

  


**Q: How do I track LLM token usage?**

Usage appears under Settings → Billing → AI Usage once the agent runs in Production.

  


**Q: Is data from Knowledge Bases sent to the LLM?**

Only the retrieved snippets (not entire documents) are passed, keeping context tight and costs low.

  


**Q: What happens if an external API fails inside a Sequential Node?**

The error is surfaced in the run log, and you can branch to a fallback node using conditional edges (e.g., on error codes).

  


**Q: Can I export an agent to another sub-account?**

Export/import functionality is on the roadmap; for now, rebuild or duplicate manually within the same account.

  


**Q: Are multiple versions of one agent billable separately?**

No. Only Production runs consume tokens; drafts and tests use your sandbox quota.

* * *

### **Related Articles**

  


  * [How to Use the AI Agent Studio in HighLevel](<https://help.gohighlevel.com/a/solutions/articles/155000006058?portalId=48000045315>)

  * [Ask AI Agent Studio Integration ](<https://help.gohighlevel.com/a/solutions/articles/155000006677?portalId=48000045315>)

  * [AI Employee Overview](<https://help.gohighlevel.com/a/solutions/articles/155000003906?portalId=48000045315>)

  * [Setting Up Conversation AI ](<https://help.gohighlevel.com/a/solutions/articles/155000004401?portalId=48000045315>)

  * [Knowledge Base Integration for Voice-AI Agents](<https://help.gohighlevel.com/a/solutions/articles/155000005266?portalId=48000045315>)

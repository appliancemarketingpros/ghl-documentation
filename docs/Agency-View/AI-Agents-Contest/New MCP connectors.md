# New MCP connectors

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008709-new-mcp-connectors](https://help.gohighlevel.com/support/solutions/articles/155000008709-new-mcp-connectors)  
**Category:** Agency View  
**Folder:** AI Agents Contest

---

AI • Managed Agents • Ask AI

New MCP Connectors

Connect Clay, Lemlist, Airtable, Composio, and Reap to HighLevel AI experiences so agents can securely use third-party tools to enrich data, automate outreach, manage records, access connected apps, and repurpose video.

What You'll Learn

HighLevel's MCP connector catalog now includes five additional apps: **Clay** , **Lemlist** , **Airtable** , **Composio** , and **Reap**. These connectors extend Managed Agents and Ask AI beyond native CRM actions by giving them controlled access to tools available in connected third-party accounts.

This guide explains what each new connector is designed for, how MCP apps work with Managed Agents and Ask AI, how to select the tools an agent can use, and how to test a connector before using it in live automation.

Available Now

Clay, Lemlist, Airtable, Composio, and Reap are now available in the MCP connector catalog. They join the existing and growing collection of third-party integrations available to supported HighLevel AI experiences.

Table of Contents

1\. What are the New MCP Connectors? 2\. Key Benefits 3\. Five New MCP Connectors 4\. How MCP Connectors Work with Managed Agents 5\. Managed Agents vs. Ask AI 6\. How To Setup and Use MCP Connectors 7\. Security and Access Best Practices 8\. Troubleshooting 9\. Frequently Asked Questions 10\. Related Articles

# **What are the New MCP Connectors?**  
  


MCP, or **Model Context Protocol** , provides a standardized way for AI agents to connect to external applications and use the tools those applications expose. In HighLevel, MCP app connectors allow Managed Agents and Ask AI to work with authenticated third-party services without requiring you to manually build every integration.

Once an MCP app is connected, you control which available tools the AI can use. A Managed Agent can then call those tools when its trigger and instructions require them, while Ask AI can use enabled connector tools while responding to your requests.

The latest catalog expansion adds **Clay** , **Lemlist** , **Airtable** , **Composio** , and **Reap**.

## **Key Benefits of MCP Connectors**  
  


MCP connectors extend AI automation beyond HighLevel by letting agents securely access selected capabilities from third-party applications. This makes it possible to build richer automations without creating a separate custom integration for every use case.

  * **More External Actions:** Let AI agents work with supported tools in connected third-party apps.
  * **Controlled Tool Access:** Choose which tools each connected app makes available to the agent.
  * **Secure Connections:** Authenticate through the connector's supported OAuth or secure sign-in flow instead of placing credentials in agent instructions.
  * **Multi-App Agents:** Connect multiple MCP apps to a Managed Agent when one workflow needs to work across several systems.
  * **Faster Automation:** Add prebuilt app capabilities without manually configuring individual API calls for every operation.
  * **Broader AI Workflows:** Combine CRM events, AI reasoning, and external applications in one agent workflow.


## **Five New MCP Connectors**  
  


Each connector expands the types of work an AI agent can perform. Choose the app that matches the external data, outreach, record management, multi-app automation, or content-production task you want the agent to handle.

Connector| What It Enables| Example Use  
---|---|---  
**Clay**|  Build and enrich lead lists using company and contact data from 100+ sources, enrichment waterfalls, and outbound preparation tools.| Enrich a newly created lead before routing it to sales.  
**Lemlist**|  Work with cold-outreach activities such as lead discovery, multichannel email and LinkedIn sequences, and campaign management.| Add qualified prospects to the appropriate outbound campaign.  
**Airtable**|  Read, create, and update records across connected Airtable tables and views using the tools made available by the connector.| Create a project record after a customer completes onboarding.  
**Composio**|  Reach 1,000+ tools through one managed gateway that handles supported authentication and gives agents access to connected application actions.| Build an agent that needs to take actions across several external systems.  
**Reap**|  Repurpose long-form video into shorter clips with supported captioning, dubbing, and translation capabilities.| Turn a long recording into short-form assets ready for a content workflow.  
  
**Important:** Available tools can vary by connector, connected account, third-party permissions, and future connector updates. Review the tool list shown during setup before publishing an agent.

## **How MCP Connectors Work with Managed Agents**  
  


A connector gives the agent access to external tools, but it does not decide when the agent should run or what the agent should do. Managed Agents combine triggers, instructions, apps, capabilities, and optional Knowledge Bases so each part of the configuration has a clear role.

### **Triggers Determine When the Agent Runs**

Triggers start a Managed Agent when the configured event occurs. For example, an agent might run when a contact is created, an opportunity is created, or a lead-generation form is submitted.

### **Apps Define Which External Systems the Agent Can Use**

The **Apps** area contains the MCP connectors assigned to the Managed Agent. A single agent can use more than one connector when its instructions require actions across different external applications.

### **Instructions Tell the Agent What to Do**

Clear instructions define when an external tool should be used, what information should be passed to it, and what outcome the agent should produce. Giving an agent access to a connector does not mean every available tool will be called on every run.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080665834/original/cHjstd7zZKESrYYXP1AKrsCTnOj7w9Ftow.png?1789107309)

**Note:** Screenshots may show existing connectors such as Notion or HubSpot as examples. The same Apps workflow is used to add supported connectors from the current catalog. Tool counts can change as connectors are updated.

## **Using MCP Connectors in Managed Agents vs. Ask AI**  
  


Managed Agents and Ask AI can both use MCP connectors, but they serve different automation patterns. Managed Agents are designed for triggered, autonomous work, while Ask AI uses connected tools in response to a user's request.

Area| Managed Agents| Ask AI  
---|---|---  
**How work starts**|  Configured trigger or supported agent event| User asks Ask AI to perform a task  
**Where connectors are configured**|  Apps area inside the Managed Agent| Customize → Connectors → Manage Connectors  
**Typical use**|  Repeatable or event-driven automation| Interactive, user-initiated work  
**Tool control**|  Select connector tools available to the agent| Enable the connector and control available tools  
  
## **How To Setup and Use New MCP Connectors**  
  


Proper setup ensures the AI has access only to the external account and tools required for its task. Connect the app, review its permissions, select the appropriate tools, and test the behavior before relying on the connector in production.

### **Option 1: Connect an MCP App to a Managed Agent**

Managed Agents use MCP apps as part of event-driven automation. The app should be attached to the specific agent that needs its tools so access remains aligned with the agent's purpose.

### **Step 1: Open Managed Agents**

Managed Agents are configured from Agent Studio, where you can define the agent's instructions, triggers, apps, capabilities, Knowledge Bases, testing, and publishing state.

  1. Go to **AI Agents → Agent Studio**.
  2. Open **Managed Agents**.
  3. Create a new Managed Agent or open an existing agent.


### **Step 2: Add an MCP App**

The Apps area determines which external connectors are available to the agent. Only add connectors that are relevant to the automation the agent is expected to perform.

  1. Locate the **Apps** area.
  2. Click **Add app**.
  3. Browse or search the MCP catalog.
  4. Select **Clay** , **Lemlist** , **Airtable** , **Composio** , **Reap** , or another supported connector.


### **Step 3: Connect the External Account**

Authentication allows the connector to act within the permissions granted by the external service. Use the supported OAuth or secure sign-in flow presented by the connector.

  1. Select the MCP app.
  2. Click the option to connect or add an account.
  3. Sign in to the applicable third-party account.
  4. Review and authorize the requested access.


### **Step 4: Choose the Tools the Agent Can Use**

Tool selection controls the specific actions exposed to the agent. Limiting access to the tools required for the use case makes the agent's capabilities easier to understand, test, and govern.

  1. Review the available tools for the connector.
  2. Select the tools the agent needs.
  3. Leave unrelated tools disabled when they are not required.
  4. Click **Save**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080665931/original/9wjn7Ig_Odkx_N-vCllS9FJeNsCO2sNPqg.png?1789107339)

### **Step 5: Update the Agent Instructions**

The agent needs clear guidance about when and why to use the connector. Good instructions reduce unnecessary tool calls and make the expected outcome easier to test.

Include details such as:

  * Which situations require the external app.
  * What data the agent should read or send.
  * Which actions it is allowed to perform.
  * When the agent should ask for clarification.
  * What the agent should do when the connector returns an error or no result.


### **Step 6: Configure the Trigger**

Triggers determine when a Managed Agent begins its work. Choose an event that provides the right context for the connected app action.

For example, a lead-enrichment agent could run when a contact is created, while a follow-up agent could run after a form submission or another supported CRM event.

### **Step 7: Test the Agent**

Testing confirms that the correct connector and tool are selected, the external account returns the expected information, and the agent follows the restrictions in its instructions.

  1. Click **Test Agent**.
  2. Use representative test data.
  3. Confirm the correct MCP tool is invoked.
  4. Verify the expected result appears in the external app.
  5. Refine the instructions or tool permissions if the result is not correct.


### **Step 8: Publish the Managed Agent**

Publishing makes the tested configuration available for live execution. Publish only after confirming the trigger, external account, tool permissions, and agent instructions behave as intended.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080665965/original/qRmPY3BS7TJ83n0fVMVrngKs2qHdqTmW1Q.png?1789107359)

### **Option 2: Connect an MCP App in Ask AI**

Ask AI connectors are designed for user-initiated tasks. Connect the app once, control which tools are enabled, and then ask Ask AI to perform supported work using that connected account.

  1. Open **Ask AI**.
  2. Go to **Customize → Connectors**.
  3. Select **Manage Connectors**.
  4. Find the MCP app you want to use.
  5. Connect and authenticate the applicable third-party account.
  6. Review and enable the tools Ask AI should be allowed to use.
  7. Enable the connector.
  8. Start a chat and give Ask AI a clear request that requires the connected app.


## **Security and Access Best Practices**  
  


MCP connectors can allow AI to take real actions in external systems, so connector access should match the agent's exact responsibility. Limiting accounts, tools, and instructions reduces unnecessary access and makes production behavior easier to audit.

  * **Grant only required access:** Authorize the minimum third-party permissions necessary for the agent's job.
  * **Select only required tools:** Avoid enabling every available tool when the agent needs only a small subset.
  * **Keep credentials out of prompts:** Use the connector authentication experience rather than placing passwords, API keys, or login details in agent instructions.
  * **Write explicit guardrails:** Tell the agent which actions it may perform and which situations require confirmation or escalation.
  * **Test with realistic inputs:** Verify read and write actions before exposing the agent to live triggers.
  * **Review third-party requirements:** Some apps may require their own account, plan, permissions, or feature access.
  * **Recheck tools after connector updates:** Available tool lists can evolve as MCP integrations add or change capabilities.


## **Troubleshooting MCP Connectors**  
  


Most MCP connector issues come from authentication, third-party permissions, tool selection, or unclear agent instructions. Check each layer separately to identify whether the connection, tool, or agent behavior needs to be adjusted.

Issue| What to Check  
---|---  
**The app is connected but the agent cannot use it**|  Confirm the connector is attached to the correct agent and the required individual tools are enabled.  
**Authentication fails**|  Reconnect the app, verify the third-party account credentials, and confirm the account is allowed to authorize the requested access.  
**A required tool does not appear**|  Review the connector's current tool list and the permissions or plan available in the connected third-party account.  
**The agent uses the wrong external action**|  Reduce unnecessary tool access and make the agent instructions more explicit about when each tool should be used.  
**The Managed Agent does not run**|  Verify that the intended trigger is configured, the agent is published, and your test event matches the trigger conditions.  
**The connector previously worked but now fails**|  Check whether authorization was revoked or expired, then reconnect the third-party account and retest the tool.  
**Ask AI does not use the connector**|  Confirm the connector is enabled, the required tool is allowed, and your request clearly asks for an action that requires the connected app.  
  
## **Frequently Asked Questions**  
  


Q: Are Clay, Lemlist, Airtable, Composio, and Reap replacing existing MCP connectors?

No. These apps expand the existing MCP connector catalog rather than replacing current connectors.

Q: Can one Managed Agent use more than one MCP connector?

Yes. Multiple MCP apps can be attached when the agent needs to work across several external systems. Keep its instructions clear about when each connector should be used.

Q: Does adding an MCP connector automatically cause the Managed Agent to run?

No. The connector provides external tools. The Managed Agent still needs the appropriate trigger and instructions to determine when it runs and what action it should perform.

Q: Can I control which tools an MCP app exposes to an agent?

Yes. Review the available tool list after connecting the app and enable only the tools required for the agent's use case.

Q: Do I need an account with the third-party app?

Generally, you must authenticate an eligible account with the third-party service. Required plans, permissions, or features can vary by app.

Q: Can Ask AI use these MCP connectors too?

Yes. This release applies to Managed Agents and Ask AI. Ask AI connectors are managed from Customize → Connectors → Manage Connectors.

Q: Are catalog MCP connectors the same as custom MCP connectors?

No. Catalog connectors are prebuilt integrations available from the MCP app catalog. Custom MCP connections are a separate configuration path for connecting other compatible MCP servers.

Q: Why does my connector show a different number of tools than a screenshot?

Tool counts can change as connectors evolve. Use the current tool list displayed in your account as the source of truth for the actions available to your agent.

### **Related Articles**  
  


[ MCP Connectors for Managed Agents ](<https://help.gohighlevel.com/support/solutions/articles/155000008304-mcp-connectors>) [ Setup and Use Managed Agents in Agent Studio ](<https://help.gohighlevel.com/support/solutions/articles/155000007931-important-update-agent-studio-is-evolving>) [ Ask AI Skills and Connectors ](<https://help.gohighlevel.com/support/solutions/articles/155000008434-ask-ai-skills-and-connectors>) [ Custom MCP Connectors for Managed Agents ](<https://help.gohighlevel.com/support/solutions/articles/155000008353-custom-mcp-connectors-for-superagents-agent-studio>) [ Managed Agents, Conversation AI & Ask AI: What's the Difference? ](<https://help.gohighlevel.com/support/solutions/articles/155000008362-super-agents-conversation-ai-ask-ai-what-s-the-difference->) [ Skills Platform for AI Agents ](<https://help.gohighlevel.com/support/solutions/articles/155000008315>)

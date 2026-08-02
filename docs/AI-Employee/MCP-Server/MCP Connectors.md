# MCP Connectors

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008304-mcp-connectors](https://help.gohighlevel.com/support/solutions/articles/155000008304-mcp-connectors)  
**Category:** AI Employee  
**Folder:** MCP Server

---

AI Automation

# MCP App Connectors

Extend your Superagents with powerful third-party integrations through Model Context Protocol (MCP) connectors.

What You'll Learn

MCP connectors allow your Superagents to interact with external applications like HubSpot, Notion, Make, Calendly, and more. Agents can authenticate, access tools, and perform actions in connected apps based on workflow triggers.

This article covers what MCP connectors are, which apps are supported, how to set them up in Agent Studio, and answers common questions about using these integrations.

Table of Contents

1

What are MCP App Connectors?

2

Key Benefits

3

Supported MCP Apps

4

How to Connect an MCP App to Your Superagent

5

Frequently Asked Questions

1

## What are MCP App Connectors?

MCP (Model Context Protocol) app connectors enable your HighLevel Superagents to securely authenticate and interact with third-party applications. Once connected, agents can access tools and perform actions within these apps as part of automated workflows.

For example, a Superagent with Notion MCP connected can create pages, search content, or update databases in your Notion workspace. With HubSpot MCP, agents can create contacts, update deals, or log activities directly in HubSpot.

MCP connectors use secure OAuth authentication or direct login to give agents the permissions they need without exposing credentials. You control which tools each agent can access within the connected app.

2

## Key Benefits

MCP app connectors expand what your Superagents can do by bridging HighLevel workflows with external platforms. Here are the primary advantages:

**Browse and Connect Apps in Agent Studio** — Add MCP apps directly from the Agent Studio interface. No need to leave the platform to set up integrations.

**Secure Authentication** — Connect using OAuth or secure login flows. Credentials are handled safely and agents receive only the permissions you authorize.

**Granular Tool Selection** — Choose which specific tools each agent can use within a connected app, ensuring agents have access only to the functions they need.

**Trigger-Based Actions** — Agents execute actions in connected apps based on workflow triggers, automating tasks like creating records, updating statuses, or retrieving information.

**Growing Ecosystem** — New MCP connectors are added regularly, expanding the range of third-party services your agents can integrate with.

3

## Supported MCP Apps

HighLevel supports a growing list of MCP app connectors. Each connector provides a set of tools that agents can use to interact with the connected application.

MCP App| Description  
---|---  
HubSpot| Manage contacts, deals, and CRM activities in HubSpot.  
Notion| Create pages, search content, and organize knowledge in Notion workspaces.  
Apify| Run web scraping and automation tasks using Apify actors.  
Make| Trigger Make scenarios and automate multi-app workflows.  
Fathom| Access analytics and visitor data from Fathom.  
Calendly| Schedule meetings and manage calendar availability via Calendly.  
Canva| Generate and manage design assets using Canva's tools.  
OpenArt| Create AI-generated artwork and visual content through OpenArt.  
Monday.com| Manage work in boards, create and update items, and move tasks through statuses.  
Cal.com| Book, reschedule, and manage meetings on connected calendars automatically.  
Higgsfield| Generate cinematic AI videos and images from text or reference inputs.  
  
More Connectors Coming Soon

Additional MCP connectors are in development. Custom MCP support is also planned, allowing you to connect proprietary or niche applications to your Superagents.

4

## How to Connect an MCP App to Your Superagent

Follow these steps to add an MCP app connector to a Superagent in HighLevel Agent Studio:

Step 1

Open Agent Studio

Navigate to Agent Studio in your HighLevel account.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077351998/original/PmwPnqyDU8s4O4H14iDIzc29dFr7HAHI9A.png?1785506605)

Step 2

Create or Select a Superagent

Create a new Superagent or open an existing one. You can also instruct the agent builder to add an MCP app during agent creation.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077155106/original/RzrdxHjOhb_7Cf_6Gbr0bHUOhab_AZ6Jkw.png?1785335821)

Step 3

Add an MCP App

In the Apps section of the agent configuration, click "+ Add app" and select the MCP connector you want to integrate (e.g., Notion, HubSpot, Make).

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077352212/original/X7W8p_kjwiN3ItIJ_9IFHcJuZAI-1BuIVg.png?1785506759)

Step 4

Authenticate Your Account

Click "+ Connect" next to the MCP app. You will be prompted to sign in using OAuth or a secure login flow. Grant the necessary permissions for the agent to access the app.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077156026/original/_sia11EHfqV04YB9T-asTfn86VNZpPqdMA.png?1785336258)

Step 5

Select Tools

Once authenticated, a list of available tools for the MCP app appears. Check the boxes next to the tools you want the agent to use (e.g., "notion-create-pages", "notion-search", "get_board_items_page" for Monday.com).

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077352359/original/ESa-D6ymUTPpEB4uFLN4kNXKi8G75ovBEA.png?1785506878)

Step 6

Save the Configuration

Click "Save" to apply the MCP app connection and selected tools to your Superagent.

Step 7

Trigger the Agent

Activate the agent using the configured trigger (e.g., "Lead Gen Form Submitted"). The agent will execute actions in the connected MCP app as part of its workflow.

Tip

You can connect multiple MCP apps to a single Superagent. Agents will use the appropriate tools based on the context and instructions you provide.

5

## Frequently Asked Questions

Q: What is the Model Context Protocol (MCP)?

MCP is a standard protocol that allows AI agents to securely connect to and interact with external applications. It defines how agents authenticate, access tools, and execute actions across different platforms.

Q: Can I connect multiple MCP apps to one Superagent?

Yes. A single Superagent can be connected to multiple MCP apps simultaneously. The agent will use the appropriate tools from each app based on its workflow instructions.

Q: Are my credentials secure when connecting MCP apps?

Yes. MCP connectors use OAuth or secure login flows. Your credentials are not stored by HighLevel, and agents receive only the permissions you explicitly grant during authentication.

Q: Which HighLevel products support MCP connectors?

MCP connectors are currently available in Agent Studio for Superagents. Support for Voice AI and Conversations AI is planned for a future release.

Q: Can I create custom MCP connectors?

Custom MCP connector support is in development. Once released, you will be able to connect proprietary or specialized applications to your Superagents.

Q: How do I choose which tools an agent can access?

After connecting an MCP app, you will see a list of available tools. Check the boxes next to the tools you want the agent to use. You can modify these selections at any time by editing the agent configuration.

Q: What happens if an MCP app connection fails?

If authentication fails or permissions are revoked, the agent will not be able to execute actions in that app. You can reconnect the MCP app by re-authenticating the account in the Apps section of Agent Studio.

Q: Will more MCP apps be added in the future?

Yes. HighLevel is actively adding new MCP connectors. You can track upcoming integrations and request new connectors through the MCP app tracker in the HighLevel community.

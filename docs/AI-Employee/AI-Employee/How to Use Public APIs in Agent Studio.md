# How to Use Public APIs in Agent Studio

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007515-how-to-use-public-apis-in-agent-studio](https://help.gohighlevel.com/support/solutions/articles/155000007515-how-to-use-public-apis-in-agent-studio)  
**Category:** AI Employee  
**Folder:** AI Employee

---

Public APIs for AI Agent Studio let you call, manage, and run any HighLevel agent from your own software—without logging in to HighLevel. This article explains what the APIs are, why they matter, and how to use them securely with OAuth.

* * *

**TABLE OF CONTENTS**

  * What is Agent Studio Public API?
  * Key Benefits of Agent Studio Public API
  * List Agents API
  * Get Agent API
  * Execute Agent API
  * OAuth Authentication
  * PIT Integrations
  * How To Set Up Agent Studio Public API
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Agent Studio Public API?**

  


A Public API (Application Programming Interface) is a secure way for external applications to communicate with HighLevel. In Agent Studio, the Public API allows your software to list, retrieve, and execute production-ready AI agents programmatically without logging into the HighLevel dashboard.

  


Your application sends secure HTTP requests to HighLevel’s servers, which run the selected agent and return a structured JSON response. Each request is tied to a specific sub-account (location) and must include proper authentication using OAuth 2.0 bearer tokens or a Private Integration Token (PIT). Only agents that are Active in the Production lifecycle stage can be accessed through the Public API.

* * *

## **Key Benefits of Agent Studio Public API**

  


  * Embed AI agents inside mobile apps, SaaS platforms, voice assistants, or internal tools.


  


  * Trigger complex agent workflows from external automations (Zapier, Make, Airflow, etc.).


  


  * Centralize security with OAuth 2.0 and scoped access tokens.


  


  * Leverage PIT Integrations to run agents inside your own environment while respecting data-privacy rules.


  


  * Return rich, structured JSON so downstream systems can parse results without extra NLP.


* * *

## **Manage Agents with Public APIs**

  


Agent Studio Public APIs now support full agent management, making it possible to create, retrieve, update, publish, execute, and delete agents programmatically. This gives API-first users a more complete way to manage agents without relying only on the Agent Studio UI.

  


Public API support now covers the core agent lifecycle, helping teams automate agent operations inside their existing platforms and workflows.

* * *

  


## **Supported Agent Management Actions**

  


You can now use public APIs for these Agent Studio actions:

  


  * Create Agent
  * List Agents
  * Get Agent
  * Update Agent
  * Update Agent Metadata
  * Delete Agent
  * Promote to Production and Publish
  * Execute Agent


  


Depending on the endpoint, requirements may vary for scopes, location context, and request parameters. In general, read actions use read-only access while create, update, publish, execute, and delete actions require write access.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074047814/original/BoUhA7VwsjtVQ-lXiW60JsoXvwXO3M4b1g.png?1781862173)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074048015/original/1R19rn90VcmyS-nfDrnL3Wsp022Wv4ZZFQ.png?1781862296)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074048322/original/_GRGuvHnBfnFx72p3q_6Lr-BXmW7reFPhg.png?1781862414)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074048472/original/ellrdXSweWuUqH3uW4lcWIvd1S4EwqtnuQ.png?1781862499)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074048606/original/-6YeVYxErIydrc3KWuDahc3Hv5LJUZh0dA.png?1781862566)

* * *

## **Deprecated Endpoints and Migration Guidance**

  


Some legacy Agent Studio public endpoints remain available and are marked as **deprecated** for backward compatibility.

  


For new development, use the current public endpoints instead of deprecated ones. Deprecated endpoints may be replaced or removed in future API versions, so newer integrations should be built against the active Agent Studio API routes.

  


If you currently rely on deprecated endpoints, review the latest Agent Studio API documentation and migrate to the updated endpoints where available.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074048700/original/PDmT5kGCEJOLXnrGDOQWsdwZxeD0zsPJEg.png?1781862630)

* * *

## **List Agents API**

This endpoint returns every active agent for a given location.

  


  * **Method:** GET /agent-studio/public-api/agents


  


  * Required query param: locationId


  


  * Optional pagination: limit, offset


  


  * **Typical use:** show a dropdown of available agents in your app.


* * *

## **Get Agent API**

Retrieve full metadata about a single agent.

  


  * **Method:** GET /agent-studio/public-api/agents/{agentId}


  


  * Required query param: locationId


  


  * **Returns:** name, status, tool-nodes, variables, lifecycle stage, and more.


  


  * **Typical use:** display agent details before execution or inspect variables.


* * *

## **Execute Agent API**

Run an agent and get the complete output in one JSON payload.

  


  * **Method:** POST /agent-studio/public-api/agents/{agentId}/execute


  


  * **Body:**{ locationId, input, executionId? }


  


  * First call omits executionId; response returns executionId so you can continue the same conversation thread in subsequent calls.


  


  * **Typical use:** deliver instant results (e.g., “Summarize this PDF” or “Generate ad copy”).


* * *

## **OAuth Authentication**

Public APIs use OAuth 2.0 bearer tokens. Create a private integration in HighLevel or use the standard OAuth flow to obtain an access token. Tokens are JWTs that must be included in the Authorization header:

Authorization: Bearer {access_token}

* * *

## **PIT Integrations**

  


Private Integration Tokens (PIT) offer a simplified alternative to full OAuth when you need server-to-server calls. Generate a PIT in the HighLevel Developer Settings, scope it to the required sub-account, and include it in the Authorization header just like an OAuth access token.

* * *

## **How To Set Up Agent Studio Public API**

Follow these steps to connect your external app:

  * Enable AI Agents → Agent Studio in your sub-account (must have agents in “Production”).


  


  * Go to Settings → Developer and create a Private Integration or OAuth App.


  


  * Copy the Client ID and Client Secret (OAuth) or PIT value (Private Integration).


  


For OAuth:

Call POST /oauth/token with grant_type=authorization_code to exchange the code for an access token.

  


  * b. Store the access token securely; refresh it as needed.


  


  * Test the connection with List Agents:


  


  * curl -H "Authorization: Bearer {token}" "<https://services.leadconnectorhq.com/agent-studio/public-api/agents?locationId={locationId}>"


  


  * Parse the response and save the agentId(s) you intend to run.


  


Execute the agent:

  


curl -X POST \

-H "Authorization: Bearer {token}" \

-H "Content-Type: application/json" \

-d '{ "locationId":"abc123", "input":{ "prompt":"Write a Facebook ad for plumbers"} }' \

  


<https://services.leadconnectorhq.com/agent-studio/public-api/agents/{agentId}/execute>

  


Store the returned executionId if you need multi-turn conversations.

* * *

## **Frequently Asked Questions**

  


**Q: Is there a rate limit?**

Yes. Each sub-account is limited to 300 API requests per minute across all Agent Studio endpoints.

  


**Q: Can I stream partial responses?**

Not yet. The Execute Agent endpoint currently returns a single JSON object after completion.

  


**Q: Do agents need to be in Production?**

Yes. Only agents with status = “Active” in the Production lifecycle stage are accessible via the public API.

  


**Q: What happens if I omit locationId?**

The API returns HTTP 400 (“locationId is required”).

  


**Q: Can I call the API from client-side JavaScript?**

It’s not recommended; always proxy the request from your backend to protect the bearer token.

  


**Q: How long is an executionId valid?**

Execution IDs expire after 30 minutes of inactivity. Start a new session if needed.

  


**Q: Does OAuth support refresh tokens?**

Yes follow the standard OAuth 2.0 refresh_token grant to renew access tokens without user interaction.

  


**Q: Are PIT tokens limited to a single location?** Yes. PIT tokens are scoped to the sub-account you selected when generating the token.

* * *

### **Related Articles**

  * [How to Use the AI Agent Studio in HighLevel ](<https://help.gohighlevel.com/a/solutions/articles/155000006058?portalId=48000045315>)

  * [Ask AI + Agent Studio Integration ](<https://help.gohighlevel.com/a/solutions/articles/155000006677?portalId=48000045315>)

  * [Private Integrations: Everything you need to know](<https://help.gohighlevel.com/a/solutions/articles/155000003054?portalId=48000045315>)

  * [Agent Studio Overview](<https://help.gohighlevel.com/a/solutions/articles/155000007393?portalId=48000045315>)

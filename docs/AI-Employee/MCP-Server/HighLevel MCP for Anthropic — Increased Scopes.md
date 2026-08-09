# HighLevel MCP for Anthropic — Increased Scopes

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008391-highlevel-mcp-for-anthropic-increased-scopes](https://help.gohighlevel.com/support/solutions/articles/155000008391-highlevel-mcp-for-anthropic-increased-scopes)  
**Category:** AI Employee  
**Folder:** MCP Server

---

API Integration

# HighLevel MCP for Anthropic — Increased Scopes

Connect Claude to HighLevel with OAuth-based authentication and access to the full operation catalog across 40 domains.

What You'll Learn

The HighLevel MCP for Anthropic endpoint provides Claude clients with OAuth-based access to 625 operations across 40 domains. This represents a significant expansion beyond the limited-scope surface available through the original universal MCP endpoint.

This article explains the key capabilities, setup process, and technical architecture of the Anthropic MCP endpoint, including user-controlled scope selection, the 5-tool facade pattern, and per-client OAuth isolation.

  


For more, visit the **Support Doc:**<https://marketplace.gohighlevel.com/docs/other/mcp/>

Table of Contents

1

What is the HighLevel MCP for Anthropic?

2

Key Features and Capabilities

3

Supported Claude Clients

4

Operation Coverage and Scopes

5

How to Set Up the HighLevel MCP for Anthropic

6

Technical Architecture

7

Video Walkthrough

8

Related Articles

9

Frequently Asked Questions

1

## What is the HighLevel MCP for Anthropic?

The HighLevel MCP for Anthropic is an OAuth-based Model Context Protocol endpoint specifically designed for Claude clients. MCP (Model Context Protocol) enables AI assistants like Claude to connect to external data sources and tools through a standardized interface.

This endpoint provides access to the complete HighLevel operation catalog — 625 operations across 40 domains — representing a substantial expansion beyond the limited-scope surface of the original universal MCP endpoint. The Anthropic endpoint uses a dedicated OAuth application that grants the widest scope set available, while maintaining complete user control over which permissions are granted.

The endpoint follows a per-client MCP pattern, with the URL structure:

https://services.leadconnectorhq.com/mcp/anthropic/v2

This approach allows different AI clients to maintain isolated OAuth grants, ensuring that scopes granted to Claude remain separate from scopes granted to other clients like ChatGPT or future integrations.

2

## Key Features and Capabilities

The HighLevel MCP for Anthropic introduces several advanced capabilities designed to provide comprehensive API access while maintaining security and efficiency:

**Increased Scopes** — Access to the widest scope set available, spanning the full operation catalog across 40 domains, compared to the limited-scope surface of the original endpoint

**User-Controlled Scope Selection** — Users approve exactly which scopes the integration can access through the OAuth consent screen, maintaining complete control over permissions

**5-Tool Facade Pattern** — Instead of hundreds of individual tools, a compact interface of five core tools (search, fetch, search_operations, describe_operation, execute_operation) keeps model context small while enabling full catalog access

**Per-Client OAuth Isolation** — Scopes granted to Claude remain isolated from scopes granted to other AI clients, with dedicated OAuth apps per official client

**Latest v3 API Documentation** — All operations are based on the latest HighLevel v3 API with full RBAC (Role-Based Access Control) enforcement

**Sub-Account Level Connections** — Every connection operates at the location level; one connection equals one location, never agency-wide

How the 5-Tool Facade Works

Agents discover and execute operations using the pattern: `search_operations → describe_operation → execute_operation`. This architecture keeps the model's context window efficient while still providing access to the complete operation catalog.

3

## Supported Claude Clients

The HighLevel MCP for Anthropic endpoint supports the following Claude clients:

**Claude.ai** — The web-based Claude interface from Anthropic

**Claude Code** — Claude's code-focused development environment

**Claude Cowork** — Claude's collaborative workspace environment

Upcoming Clients

Support for additional AI clients is in development, including OpenAI, Cursor, Windsurf, and VS Code. These clients will follow the same per-client pattern with isolated OAuth grants.

Original Universal Endpoint

The original universal endpoint at `https://services.leadconnectorhq.com/mcp/` remains fully supported and continues to work with any MCP client over OAuth or Private Integration Token, though with the existing limited-scope surface.

4

## Operation Coverage and Scopes

The HighLevel MCP for Anthropic provides comprehensive access to HighLevel operations. The following table summarizes the complete operation catalog:

Metric| Value  
---|---  
Total Operations in Catalog| 625  
Active Operations| 571  
Read Operations| 243  
Write Operations| 244  
Delete Operations| 84  
Domains Covered| 40  
  
Key characteristics of the operation coverage:

**Automatic Filtering** — Operations are automatically filtered based on the user's OAuth grant, ensuring users only access permitted resources

**Widest Scope Set** — The Anthropic OAuth app exposes the complete scope set across the full catalog

**Location-Level Connections** — Every connection operates at the sub-account/location level; one connection equals one location, never agency-wide

**User-Controlled Selection** — Users choose which scopes to grant through OAuth consent or Private Integration Token creation

Legacy Endpoint Comparison

The legacy `/mcp/` endpoint provides a limited subset of operations through the Private Integration Token flow. For full catalog access with Claude clients, use the Anthropic-specific endpoint.

5

## How to Set Up the HighLevel MCP for Anthropic

Setting up the HighLevel MCP for Anthropic involves configuring your Claude client to connect to the Anthropic-specific endpoint and completing the OAuth authorization flow.

Step 1

Access Your Claude Client

Open one of the supported Claude clients: Claude.ai, Claude Code, or Claude Cowork. Navigate to the MCP or integrations settings within the client interface.

Step 2

Add the HighLevel MCP Endpoint

Configure the MCP connection using the Anthropic-specific endpoint URL:

https://services.leadconnectorhq.com/mcp/anthropic/v2

Step 3

Initiate OAuth Authorization

Click the connect or authorize button to begin the OAuth flow. You will be redirected to the HighLevel authorization page.

Step 4

Select Your Scopes

On the OAuth consent screen, review the requested scopes. Select exactly which permissions you want to grant to the Claude integration. You control which operations the AI can access.

Step 5

Choose Your Location

Select the HighLevel sub-account (location) you want to connect. Remember that each connection operates at the location level, not agency-wide.

Step 6

Authorize the Connection

Click "Authorize" or "Allow" to complete the OAuth flow. The system uses Authorization Code with PKCE (Proof Key for Code Exchange) for secure authentication with refresh token support.

Step 7

Verify the Connection

You will be redirected back to your Claude client. Confirm that the HighLevel MCP connection appears in your active integrations list. You can now use Claude to interact with your HighLevel data.

Connection Confirmed

After successful authorization, Claude can discover and execute operations using the 5-tool facade pattern. The locationId is automatically injected from your OAuth grant for all API calls.

6

## Technical Architecture

The HighLevel MCP for Anthropic implements several advanced architectural patterns to deliver secure, scalable, and efficient AI integration:

Component 1

Hosted Operation Registry

A generated registry containing every hosted CRM operation provides faster operation discovery, better operation ranking, consistent execution routing, and improved AI tool selection accuracy.

Component 2

Per-Client OAuth App Registry

An upstream OAuth app registry resolves a dedicated OAuth application for each official client behind the `/mcp/{client}/v2` pattern. Client identity is detected from origin and redirect signals, with scoped-path mismatches rejected and per-client OAuth discovery metadata served.

Component 3

Security Enhancements

The architecture enforces redirect URI allowlists, performs MCP origin validation to prevent DNS rebinding attacks, applies sensitive token and secret redaction, and isolates internal admin/debug surfaces from public runtime endpoints.

Component 4

Infrastructure and Reliability

The system utilizes dedicated Redis infrastructure for MCP services, manages OAuth secrets through AWS Secrets Manager, and automatically injects locationId from OAuth grants into API calls.

Component 5

RBAC Enforcement

All operations are based on the latest v3 API documentation with full Role-Based Access Control enforcement. Operations that fail RBAC checks are blocked, ensuring users only access resources permitted by their role and OAuth grant.

Note

Authentication uses Authorization Code with PKCE (Proof Key for Code Exchange) to prevent interception attacks and supports refresh tokens for long-lived connections without re-authorization.

7

## Video Walkthrough

Watch these video demonstrations to see the HighLevel MCP for Anthropic in action:  
  
*HighLevel MCP for Anthropic* `/mcp/anthropic/v2`  
<https://www.loom.com/share/b23bfe32e8be42838bd6eab12a0b932f>  
  
*Claude Code setup*  
<https://www.loom.com/share/6e944d0b4038430da6d829a74c944b88>  
  
*Old endpoint* `/mcp/`  
<https://www.loom.com/share/d6b2228911514b5a9bbf88fd74a84759>  
  
*Docs*  
<https://marketplace.gohighlevel.com/docs/other/mcp/>

Maximize Your AI Integration

Ready to Connect Claude to HighLevel?

Access the full operation catalog with 625 operations across 40 domains using the new Anthropic MCP endpoint.

8

## Related Articles

  * [HighLevel MCP Documentation](<https://marketplace.gohighlevel.com/docs/other/mcp/>)
  * Understanding OAuth Scopes in HighLevel
  * HighLevel API v3 Reference


9

## Frequently Asked Questions

Q: What is the difference between the Anthropic endpoint and the original universal endpoint?

The Anthropic endpoint (`/mcp/anthropic/v2`) provides access to the complete operation catalog with 625 operations across 40 domains using dedicated OAuth apps. The original universal endpoint (`/mcp/`) offers a limited-scope surface designed for general MCP client compatibility. For Claude integrations requiring full API access, use the Anthropic endpoint.

Q: Can I connect multiple HighLevel locations to Claude?

Yes, but each connection operates at the sub-account (location) level. One OAuth connection equals one location, never agency-wide. To work with multiple locations, you need to establish separate OAuth connections for each location. The locationId is automatically injected from your OAuth grant for all API calls.

Q: How does the 5-tool facade keep the model context small?

Instead of exposing hundreds of individual tools that would consume the model's context window, the MCP surface presents only five core tools: `search`, `fetch`, `search_operations`, `describe_operation`, and `execute_operation`. Claude discovers available operations dynamically using the pattern `search_operations → describe_operation → execute_operation`, maintaining efficiency while enabling full catalog access.

Q: What does per-client OAuth isolation mean?

Per-client OAuth isolation means that scopes granted to one AI client (such as Claude) remain completely separate from scopes granted to another client (such as ChatGPT or future integrations). Each client receives its own dedicated OAuth app through the registry, preventing cross-client permission leakage and allowing you to control exactly what each AI can access.

Q: Will the original universal endpoint be deprecated?

No, the original universal endpoint at `https://services.leadconnectorhq.com/mcp/` remains fully supported and continues to work with any MCP client over OAuth or Private Integration Token. It serves as a backward-compatible option for general MCP client connectivity, though with the limited-scope surface.

Q: How are operations filtered based on my OAuth grant?

Operations are automatically filtered based on the scopes you selected during the OAuth consent process. The system enforces Role-Based Access Control (RBAC) for all operations based on the latest v3 API documentation. Operations that fail RBAC checks are blocked, ensuring you only access resources permitted by your role and granted scopes.

Q: Which Claude clients are currently supported?

The HighLevel MCP for Anthropic endpoint currently supports Claude.ai, Claude Code, and Claude Cowork. Support for additional AI clients including OpenAI, Cursor, Windsurf, and VS Code is in development and will follow the same per-client pattern with isolated OAuth grants.

Q: What security measures protect my OAuth tokens and credentials?

The system implements multiple security layers: redirect URI allowlists are enforced, MCP origin validation prevents DNS rebinding attacks, sensitive tokens and secrets are redacted in logs, internal admin surfaces are isolated from public endpoints, OAuth secrets are managed through AWS Secrets Manager, and authentication uses Authorization Code with PKCE to prevent interception attacks.

# HighLevel MCP Server: Connect AI Agents to HighLevel Tools

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007981-highlevel-mcp-server-connect-ai-agents-to-highlevel-tools](https://help.gohighlevel.com/support/solutions/articles/155000007981-highlevel-mcp-server-connect-ai-agents-to-highlevel-tools)  
**Category:** AI Employee  
**Folder:** MCP Server

---

The HighLevel MCP Server lets AI agents and MCP-compatible clients connect securely to HighLevel tools and services. With MCP, AI assistants can retrieve records, update data, send messages, search opportunities, access calendar information, and automate tasks through a standardized HTTP connection.

* * *

**TABLE OF CONTENTS**

  * What is HighLevel MCP Server?
  * Key Benefits of HighLevel MCP Server
  * Supported MCP Clients
  * Prerequisites
  * How To Connect to the HighLevel MCP Server
  * Recommended Scopes
  * Available MCP Tools
  * Example MCP Workflows
  * Using MCP in AI Clients
  * Security and Authentication
  * Best Practices
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is HighLevel MCP Server?**

  
The HighLevel MCP Server uses the Model Context Protocol, or MCP, to let AI agents securely interact with HighLevel services. MCP acts as a bridge between an AI client and HighLevel, allowing the AI client to discover available tools, query data, and perform approved actions.  
  


The MCP Server can be used with supported AI clients and developer tools to interact with HighLevel services such as Contacts, Conversations, Calendars, Opportunities, Payments, Locations, and Custom Fields.  
  


**Production MCP Endpoint**
    
    
    https://services.leadconnectorhq.com/mcp/

* * *

  


## **Key Benefits of HighLevel MCP Server**  
  


The MCP Server helps AI builders connect intelligent assistants to HighLevel data and actions without building a custom integration from scratch.  
  


  * **Centralized AI Access:** Connect AI agents to multiple HighLevel services through one MCP endpoint.  
  

  * **Secure Authentication:** Use Private Integration Tokens and scoped permissions to control access.  
  

  * **Natural Language Automation:** Let AI assistants perform supported actions from plain-language prompts.  
  

  * **Multi-Service Connectivity:** Work with contacts, conversations, calendars, opportunities, payments, locations, and more.  
  

  * **MCP-Compatible Flexibility:** Connect supported clients such as Cursor, Windsurf, OpenAI Playground, Claude-compatible clients, and custom MCP applications.  
  

  * **No SDK Required:** Use a standardized HTTP-based MCP connection instead of building a full custom integration.


* * *

  


## **Supported MCP Clients**  
  


MCP-compatible clients allow AI agents to discover and run HighLevel tools through a connected server. Support depends on whether the client can connect to HTTP-based MCP servers and pass the required authentication headers.  
  


Supported client examples include:  
  


  * Cursor  
  

  * Windsurf  
  

  * OpenAI Playground  
  

  * Claude-compatible MCP clients  
  

  * Custom MCP-compatible applications  
  

  * Other HTTP-based MCP clients  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074666168/original/ZPl2PdjICCrOIYRWbXUGdCSqYuEaVcUD9w.png?1782625638)**

* * *

## **Prerequisites**

  
A correct setup helps ensure the AI client can access only the HighLevel data and actions it needs.

Before connecting to the HighLevel MCP Server, make sure you have:  
  


  * Access to the desired HighLevel sub-account/location  
  

  * A Private Integration Token  
  

  * Required scopes enabled for the token  
  

  * The sub-account/location ID  
  

  * An MCP-compatible client


* * *

  


## **How To Connect to the HighLevel MCP Server**  
  


Connecting an MCP client requires a Private Integration Token, the HighLevel MCP endpoint, and the location ID. Once connected, the AI client can discover available tools based on the scopes granted to the token.  
  


### **Step 1:**_Create a Private Integration Token_

Private Integration Tokens allow your MCP client to authenticate securely with HighLevel.  
  


  1. Log in to HighLevel.  
  

  2. Open the desired sub-account/location.  
  

  3. Go to **Settings**.  
  

  4. Select **Private Integrations**.  
  

  5. Click **Create New Integration**.  
  

  6. Choose the required scopes.  
  

  7. Click **Create Integration**.  
  

  8. Copy and securely store the generated token.  
  


### **Step 2:**_Add the MCP Server to Your Client_  
  


Add the MCP endpoint and authentication headers to your MCP-compatible client.  
  

    
    
    {  "mcpServers": {    "prod-ghl-mcp": {      "url": "https://services.leadconnectorhq.com/mcp/",      "headers": {        "Authorization": "Bearer <your-token>",        "locationId": "<your-location-id>"      }    }  } }

  
Replace:  
  


  * `<your-token>` with your Private Integration Token  
  

  * `<your-location-id>` with the HighLevel sub-account/location ID  
  


### **Step 3:**_Select the Required Tools_  
  


After the client connects, available tools appear based on the scopes assigned to the Private Integration Token. Select only the tools your AI agent needs for the workflow.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074666241/original/Le5L74qHHBhJnDdLhrvb88MjkZmvN8Rlew.png?1782626047)**

* * *

## **Recommended Scopes**  
  


Scopes control which HighLevel resources the MCP client can read or modify. Grant only the permissions required for your workflow.  
  


Recommended scopes may include:  
  


  * **Contacts:** View Contacts, Edit Contacts  
  

  * **Conversations:** View Conversations, Edit Conversations  
  

  * **Conversation Messages:** View Conversation Messages, Edit Conversation Messages  
  

  * **Opportunities:** View Opportunities, Edit Opportunities  
  

  * **Calendars:** View Calendars, Edit Calendars  
  

  * **Calendar Events:** View Calendar Events, Edit Calendar Events  
  

  * **Payments:** View Payment Orders, View Payment Transactions  
  

  * **Other:** View Custom Fields, View Forms, View Locations


##   
**Available MCP Tools**  
  


The HighLevel MCP Server includes tools across core HighLevel services. The tools available to your client depend on the permissions granted through the Private Integration Token.  
  


### **Calendar Tools**  
  


Calendar tools help AI agents retrieve scheduling information and appointment details.  
  
  


  * `calendars_get-calendar-events`  
  

  * `calendars_get-appointment-notes`


###   
**Contact Tools**  
  


Contact tools allow AI agents to find, create, update, and manage contact records.  
  
  


  * `contacts_get-all-tasks`  
  

  * `contacts_add-tags`  
  

  * `contacts_remove-tags`
  *   

  * `contacts_get-contact`  
  

  * `contacts_update-contact`  
  

  * `contacts_upsert-contact`  
  

  * `contacts_create-contact`  
  

  * `contacts_get-contacts`  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074666188/original/ho3sEKy2qIzUvXOux5z_vsgsMOD01qdZAA.png?1782625774)**

###   
**Conversation Tools**  
  


Conversation tools allow AI agents to search conversations, review message history, and send supported messages.  
  


  * `conversations_search-conversation`  
  

  * `conversations_get-messages`  
  

  * `conversations_send-a-new-message`  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074666229/original/R4S_QOX4AKG3CbpIyuQkU4MXJMjnmCjmmA.png?1782626002)**

###   
**Location Tools**  
  


Location tools allow AI agents to retrieve location details and custom field information.  
  


  * `locations_get-location`  
  

  * `locations_get-custom-fields`  
  


### **Opportunity Tools**

  
Opportunity tools allow AI agents to search, retrieve, and update pipeline opportunities.  
  


  * `opportunities_search-opportunity`  
  

  * `opportunities_get-pipelines`  
  

  * `opportunities_get-opportunity`  
  

  * `opportunities_update-opportunity`  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074666227/original/3FwqFMZ9rdYkj6-JAJ2DcRF8cXQNSquFmw.png?1782625987)**

###   
**Payment Tools**  
  


Payment tools allow AI agents to retrieve order and transaction data.  
  


  * `payments_get-order-by-id`  
  

  * `payments_list-transactions`


* * *

## **Example MCP Workflows**  
  


MCP allows AI agents to interact with HighLevel using natural language while executing approved tools in the background.  
  


Common workflows include:  
  


  * Searching for a contact by name, email, or phone number  
  

  * Creating or updating a contact  
  

  * Adding or removing contact tags  
  

  * Searching conversation history  
  

  * Sending a message to a contact  
  

  * Retrieving calendar events  
  

  * Searching opportunities  
  

  * Updating opportunity details  
  

  * Reviewing payment order or transaction data


* * *

  


## **Using MCP in AI Clients**

  
AI clients can use the HighLevel MCP Server to discover tools and complete actions inside HighLevel. After the MCP server is connected, the client can call available tools based on the user’s prompt and the token’s scopes.  
  


For example, a user could ask:  
  


Check if I have a contact named Bruce Wayne.  
  


The AI client can use contact tools to search HighLevel and return matching records.  
  


Another example:  
  


Search for available opportunities in my account.  
  


The AI client can call opportunity tools and summarize the results.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074666214/original/j9eaNrvwsy5Qk0G0iWxFwq7L6LOzRcWQGw.png?1782625923)**

* * *

## **Security and Authentication**  
  


The MCP Server uses token-based authentication to protect access to HighLevel data. Each request must include a valid Private Integration Token and location ID.  
  


Required authentication details:  
  


  * Private Integration Token  
  

  * `locationId`  
  

  * Required scopes for the requested tools  
  


Keep tokens private and never expose them in public repositories, screenshots, shared prompts, or client-side code.

* * *

## **Best Practices**  
  


Following MCP best practices helps keep AI workflows secure, reliable, and easier to manage.  
  


  * **Use least-privilege access:** Enable only the scopes required for the AI workflow.  
  

  * **Store tokens securely:** Keep Private Integration Tokens in secure storage and avoid sharing them publicly.  
  

  * **Review write permissions carefully:** Grant edit permissions only when the AI agent needs to create or update data.  
  

  * **Test before production use:** Confirm the AI client calls the correct tools and returns expected results.  
  

  * **Monitor AI activity:** Review AI-driven actions when enabling write access.  
  

  * **Rotate tokens periodically:** Replace tokens regularly or when access should be revoked.  
  

  * **Use clear prompts:** Give the AI agent specific instructions about when it should read data, update records, or ask for confirmation.


##   
**Frequently Asked Questions**  
  


**Q: What does MCP stand for?**  
MCP stands for Model Context Protocol. It is a standardized protocol that allows AI agents and copilots to connect with external tools and services.  
  


**Q: What does the HighLevel MCP Server do?**  
It allows MCP-compatible AI clients to securely access supported HighLevel tools, retrieve data, and perform approved actions.  
  


**Q: Which HighLevel services are supported?**  
The MCP Server supports tools for contacts, conversations, calendars, opportunities, payments, locations, and custom fields.  
  


**Q: How do I authenticate with the MCP Server?**  
Authentication requires a Private Integration Token and a valid location ID added to the MCP client configuration headers.  
  


**Q: Can AI agents update HighLevel data through MCP?**  
Yes. AI agents can update data when the connected token includes the required edit scopes.  
  


**Q: Can I limit what an AI client can access?**  
Yes. Access is controlled through the scopes assigned to the Private Integration Token.  
  


**Q: Can I use MCP with Cursor or Windsurf?**  
Yes. MCP-compatible clients such as Cursor and Windsurf can connect when they support the required HTTP MCP configuration.  
  


**Q: Can I use MCP with OpenAI Playground?**  
Yes. OpenAI Playground can connect to remote MCP servers when configured with the endpoint and required headers.  
  


**Q: Is OAuth supported?**  
OAuth support is planned for a future release. Use Private Integration Tokens for the current setup.  
  


**Q: Can I connect custom AI agents to the HighLevel MCP Server?**  
Yes. Custom applications can connect if they support MCP over HTTP and can send the required authentication headers.

* * *

  


## **Related Articles**  
  


  * [HighLevel API Documentation](<https://help.gohighlevel.com/en/support/solutions/articles/48001060529>)  
  

  * [Documents & Contracts: Public APIs](<https://help.gohighlevel.com/en/support/solutions/articles/155000006323>)  
  

  * [Private Integrations](<https://help.gohighlevel.com/en/support/solutions/articles/155000003054>)


##

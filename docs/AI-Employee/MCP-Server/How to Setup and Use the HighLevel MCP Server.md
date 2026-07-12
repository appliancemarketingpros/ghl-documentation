# How to Setup and Use the HighLevel MCP Server

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005741-how-to-setup-and-use-the-highlevel-mcp-server](https://help.gohighlevel.com/support/solutions/articles/155000005741-how-to-setup-and-use-the-highlevel-mcp-server)  
**Category:** AI Employee  
**Folder:** MCP Server

---

The HighLevel MCP Server lets AI agents and MCP-compatible clients connect securely to HighLevel tools and services. With MCP, AI assistants can retrieve records, update data, send messages, search opportunities, access calendar information, and automate tasks through a standardized HTTP connection.

  


* * *

**TABLE OF CONTENTS**

  * What is HighLevel MCP Server?
  * Key Benefits of HighLevel MCP Server
  * Example of Supported MCP Clients
  * Prerequisites
  * How To Setup the HighLevel MCP Server
  * Recommended Scopes
  * Example of Some Available MCP Tools 
  * Example Tool Call
  * Example MCP Workflows
  * How Users can Use the MCP Tool
  * Security and Authentication
  * Best Practices
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is HighLevel MCP Server?**

  
The HighLevel MCP Server uses the Model Context Protocol, or MCP, to let AI agents securely interact with HighLevel services. MCP acts as a bridge between an AI client and HighLevel, allowing the AI client to discover available tools, query data, and perform approved actions.  
  


The MCP Server can be used with supported AI clients and developer tools to interact with HighLevel services such as Contacts, Conversations, Calendars, Opportunities, Payments, Locations, and Custom Fields.  
  

    
    
    **HighLevel MCP Endpoint:**  
      
    <https://services.leadconnectorhq.com/mcp/>

* * *

## **Key Benefits of HighLevel MCP Server**

  


  * **Centralized AI Access:** Connect AI agents to multiple HighLevel services through one MCP endpoint.  
  

  * **Secure Authentication:** Use Private Integration Tokens and scoped permissions to control access.  
  

  * **Natural Language Automation:** Let AI assistants perform supported actions from plain-language prompts.  
  

  * **Multi-Service Connectivity:** Work with contacts, conversations, calendars, opportunities, payments, locations, and more.  
  

  * **MCP-Compatible Flexibility:** Connect supported clients such as Cursor, Windsurf, OpenAI Playground, Claude-compatible clients, and custom MCP applications.  
  

  * **No SDK Required:** Use a standardized HTTP-based MCP connection instead of building a full custom integration.


* * *

## **Example of Supported MCP Clients**

  


MCP-compatible clients allow AI agents to discover and run HighLevel tools through a connected server. Support depends on whether the client can connect to HTTP-based MCP servers and pass the required authentication headers.  
  


Supported client examples include:  
  


  * Cursor  
  

  * Windsurf  
  

  * OpenAI Playground  
  

  * Claude-compatible MCP clients  
  

  * Custom MCP-compatible applications  
  

  * Other HTTP-based MCP clients


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

## **How To Setup the HighLevel MCP Server**

  


Connecting an MCP client requires a Private Integration Token, the HighLevel MCP endpoint, and the location ID. Once connected, the AI client can discover available tools based on the scopes granted to the token.  
  


### **_Step 1:_**_Create a Private Integration Token_

  


Private Integration Tokens allow your MCP client to authenticate securely with HighLevel.  
  


  1. Log in to HighLevel.  
  

  2. Open the desired sub-account/location.  
  

  3. Go to **Settings**.  
  

  4. Select **Private Integrations**.  
  

  5. Click **Create New Integration**.  
  

  6. **Choose** the **required** **scopes**.  
  

  7. Click **Create Integration**.  
  
![](https://jumpshare.com/share/7gA8UGKPR4X2jWsBJUWv+/GIF+Recording+2026-07-09+at+21.22.25.gif)  
  

  8. **Copy** the generated **token**.  
  
![](https://jumpshare.com/share/rcYMQpvMn05fORecK54M+/Screen+Shot+2026-07-09+at+21.23.11.png)  
  


### **_Step 2:_**_Add the MCP Server to Your Client_

  


Add the MCP endpoint and authentication headers to your MCP-compatible client.

  

    
    
    {  "mcpServers": {    "prod-ghl-mcp": {      "url": "https://services.leadconnectorhq.com/mcp/",      "headers": {        "Authorization": "Bearer <your-token>",        "locationId": "<your-location-id>"      }    }  } }

  


Replace:  
  


  * `<your-token>` with your Private Integration Token  
  

  * `<your-location-id>` with the HighLevel sub-account/location ID  
  


### ** _Step 3:_**_Select the Required Tools_

  


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


* * *

## **Example of Some Available MCP Tools**

  


The HighLevel MCP Server includes tools across core HighLevel services. The tools available to your client depend on the permissions granted through the Private Integration Token.

  


#| Tool| Endpoint| Description  
---|---|---|---  
1| Get Calendar Events| calendars_get-calendar-events| Get calendar events using userId, groupId, or calendarId.  
2| Get Appointment Notes| calendars_get-appointment-notes| Retrieve notes for a specific appointment.  
3| Get All Tasks| contacts_get-all-tasks| Retrieve all tasks for a contact.  
4| Add Tags| contacts_add-tags| Add tags to a contact.  
5| Remove Tags| contacts_remove-tags| Remove tags from a contact.  
6| Get Contact| contacts_get-contact| Fetch contact details.  
7| Update Contact| contacts_update-contact| Update a contact.  
8| Upsert Contact| contacts_upsert-contact| Update or create a contact.  
9| Create Contact| contacts_create-contact| Create a new contact.  
10| Get Contacts| contacts_get-contacts| Fetch all contacts.  
11| Search Conversation| conversations_search-conversation| Search/filter/sort conversations.  
12| Get Messages| conversations_get-messages| Retrieve messages by conversation ID.  
13| Send a New Message| conversations_send-a-new-message| Send a message to a conversation thread.  
14| Get Location| locations_get-location| Get location details by ID.  
15| Get Custom Fields| locations_get-custom-fields| Retrieve custom field definitions for a location.  
16| Search Opportunity| opportunities_search-opportunity| Search for opportunities by criteria.  
17| Get Pipelines| opportunities_get-pipelines| Fetch all opportunity pipelines.  
18| Get Opportunity| opportunities_get-opportunity| Fetch opportunity details by ID.  
19| Update Opportunity| opportunities_update-opportunity| Update opportunity details.  
20| Get Order by ID| payments_get-order-by-id| Retrieve payment order details.  
21| List Transactions| payments_list-transactions| Fetch paginated list of transactions.  
22| Check Blog URL Slug| blogs_check-url-slug-exists| Check the blog slug which is needed before publishing any blog post.  
23| Update Blog Post| blogs_update-blog-post| Update blog post for any given blog site  
24| Create Blog Post| blogs_create-blog-post| create blog post for any given blog site  
25| Get Blog Authors| blogs_get-all-blog-authors-by-location| get blog authors for a given location ID  
26| Get Blog Categories| blogs_get-all-categories-by-location| get blog categories for a given location ID  
27| Get Blog Posts by Blog ID| blogs_get-blog-post| get blog posts for any given blog site using blog ID  
28| Get Blogs by Location| blogs_get-blogs| get blogs using Location ID  
29| Create Email Template| emails_create-template| Create a new template  
30| Get Email Templates| emails_fetch-template| Fetch email templates by location id  
31| Get Social Media Accounts| socialmediaposting_get-account| Get list of accounts and groups  
32| Get Social Media Statistics| socialmediaposting_get-social-media-statistics| Retrieve analytics data for multiple social media accounts  
33| Create Social Media Post| socialmediaposting_create-post| Create posts for all supported platforms  
34| Get Social Media Post| socialmediaposting_get-post| Get social media post  
35| Get Social Media Posts| socialmediaposting_get-posts| Get social media posts  
36| Update Social Media Post| socialmediaposting_edit-post| Edit social media post  
  
  


### **Calendar Tools**

  


Calendar tools help AI agents retrieve scheduling information and appointment details.  
  


  * `calendars_get-calendar-events`  
  

  * `calendars_get-appointment-notes`


`  
`

### **Contact Tools**

  


Contact tools allow AI agents to find, create, update, and manage contact records.  
  


  * `contacts_get-all-tasks`  
  

  * `contacts_add-tags`  
  

  * `contacts_remove-tags`  
  

  * `contacts_get-contact`  
  

  * `contacts_update-contact`  
  

  * `contacts_upsert-contact`  
  

  * `contacts_create-contact`  
  

  * `contacts_get-contacts`  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074666188/original/ho3sEKy2qIzUvXOux5z_vsgsMOD01qdZAA.png?1782625774)**

  


  
**Conversation Tools**

  


Conversation tools allow AI agents to search conversations, review message history, and send supported messages.  
  


  * `conversations_search-conversation`  
  

  * `conversations_get-messages`  
  

  * `conversations_send-a-new-message`  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074666229/original/R4S_QOX4AKG3CbpIyuQkU4MXJMjnmCjmmA.png?1782626002)**

  


  


### **Location Tools**

  


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

  


  


### **Payment Tools**

  


Payment tools allow AI agents to retrieve order and transaction data.  
  


  * `payments_get-order-by-id`  
  

  * `payments_list-transactions`


* * *

## **Example Tool Call**

  


Python example:

  


import requests

  


headers = {

"Authorization": "Bearer YOUR_PIT_TOKEN",

"locationId": "YOUR_LOCATION_ID"

}

  


data = {

"tool": "contacts_get-contact",

"input": {

"contactId": "abc123"

}

}

  


response = requests.post(

"https://services.leadconnectorhq.com/mcp/",

headers=headers,

json=data

)

  


print(response.json())

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

## **How Users can****Use the MCP Tool**

  
Users can use the HighLevel MCP Server to complete actions inside HighLevel. After the MCP server is connected, the user can call available tools based on the user’s prompt and the token’s scopes.  
  


**For example, a user could ask:**

**  
**

Check if I have a contact named Bruce Wayne.  
  


The AI client can use contact tools to search HighLevel and return matching records.  
  


**Another example:**

**  
**

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


* * *

## **Frequently Asked Questions**

  


**Q: What does MCP stand for?**  
MCP stands for Model Context Protocol. It is a standardized protocol that allows AI agents and copilots to connect with external tools and services.

  


**Q: What does the HighLevel MCP Server do?**  
It allows MCP-compatible AI clients to securely access supported HighLevel tools, retrieve data, and perform approved actions.  
  


**Q: Can I use this with OpenAI Playground or Claude?**

Yes! Any client supporting HTTP requests can integrate with MCP.

  


**Q: Do I need to install an SDK?**

No SDK is required — MCP uses a standard HTTP protocol.

  


**Q: Is my data secure?**

Yes. Data access is fully scoped via Private Integration Tokens and secured through HTTPS.

  


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

  


  * [How to Use the MCP Server within Ask AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000005855>)  
  

  * [Automate Workflows with GHL MCP and N8N](<https://help.gohighlevel.com/en/support/solutions/articles/155000007777>)  
  

  * [Connect External MCP Servers to AI Agents in Workflows](<https://help.gohighlevel.com/en/support/solutions/articles/155000008197>)

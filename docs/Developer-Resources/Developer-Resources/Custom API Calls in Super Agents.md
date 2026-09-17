# Custom API Calls in Super Agents

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008645-custom-api-calls-in-super-agents](https://help.gohighlevel.com/support/solutions/articles/155000008645-custom-api-calls-in-super-agents)  
**Category:** Developer Resources  
**Folder:** Developer Resources

---

AI Automation

# Custom API Calls in Super Agents

Connect Super Agents to external APIs and enable them to make authenticated requests, process responses, and use the data in conversations.

What You'll Learn

This article explains how to configure custom API calls in Super Agents, allowing your AI agent to connect to external services and use live data during conversations.

You'll learn how to set up API endpoints using the Super Agent Builder, configure authentication and parameters, test requests, select response fields, and enable Super Agents to execute API calls automatically when needed.

Table of Contents

1

What Are Custom API Calls in Super Agents?

2

Key Benefits

3

How Custom API Calls Work

4

Setting Up Custom API Calls Using the Builder

5

Configuring API Calls Manually

6

Testing and Selecting Response Fields

7

How Super Agents Use APIs in Conversations

8

Managing Custom API Calls

9

Frequently Asked Questions

1

## What Are Custom API Calls in Super Agents?

Custom API calls enable Super Agents to connect to external APIs and retrieve or send data during live conversations. The Super Agent can determine when an API call is relevant, gather required information from the contact, execute the request securely, and use selected response fields in its answers.

This capability transforms Super Agents from conversational assistants into intelligent automation tools that can interact with third-party systems, databases, and services in real time.

Custom API calls work seamlessly within the conversation flow. The Super Agent recognizes when external data is needed, collects any missing parameters through natural conversation, executes the API request, and incorporates the response into its reply—all without breaking the conversational experience.

  


  


2

## Key Benefits

Custom API calls unlock powerful automation and data integration capabilities for Super Agents.

**Real-Time Data Access** — Super Agents can retrieve live information from CRMs, inventory systems, booking platforms, and other external services during conversations.

**Automated Data Updates** — Send information to external systems using POST, PUT, PATCH, or DELETE methods to create records, update statuses, or trigger workflows.

**Conversational Parameter Collection** — The Super Agent can ask for missing information naturally and place responses into the correct API fields automatically.

**Builder-Assisted Configuration** — Describe the API and its purpose in conversation with the Super Agent Builder, which can configure endpoints, methods, parameters, and authentication automatically.

**Response Field Selection** — Choose which response fields the Super Agent should use, keeping results focused and preventing information overload.

**Secure Authentication** — Support for API key, Bearer token, Basic authentication, or no authentication ensures secure connections to protected endpoints.

**Testing and Preview Tools** — Test each API call before use with full request, cURL, status code, and response previews to verify configuration.

3

## How Custom API Calls Work

Custom API calls follow a four-stage execution process that integrates seamlessly with the conversation flow.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080299805/original/iyTnJoQ_IFEAW04Cz5TgmMjELIJ5SGU9pQ.gif?1788796207)

Stage 1

Relevance Detection

The Super Agent evaluates the conversation context and determines whether an API call is relevant based on the instructions you provide. For example, if a contact asks about order status, the Super Agent recognizes that it needs to query an order tracking API.

Stage 2

Parameter Collection

The Super Agent checks whether it has all required information to execute the API call. If any parameters are missing (such as an order number or customer ID), the Super Agent asks the contact for the information naturally during the conversation.

Stage 3

Request Execution

Once all required parameters are collected, the Super Agent places them into the correct request fields (path parameters, query parameters, headers, or request body) and executes the API call securely using the configured authentication method.

Stage 4

Response Interpretation

The Super Agent receives the API response, extracts the selected response fields you configured, interprets the data, and continues the conversation using the result. The response is presented naturally as part of the Super Agent's reply.

Pro Tip

Use the Super Agent Builder for Faster Setup

Describe the API you want to connect in plain language. The Builder can configure the endpoint, method, parameters, authentication, and usage instructions automatically—saving you time on manual configuration.

4

## Setting Up Custom API Calls Using the Builder

The Super Agent Builder can configure API calls for you through a conversational interface. This method is ideal when you want to quickly set up an API connection without manually configuring each field.

Step 1

Open Your Super Agent

Navigate to the Super Agents section in HighLevel and open the saved Super Agent you want to enhance with API capabilities.

Step 2

Access the Super Agent Builder

Open the Builder interface for your Super Agent. This is the conversational configuration tool that understands natural language instructions.

Step 3

Describe the API Connection

Tell the Builder which API you want to connect and what the Super Agent should do with it. For example: "I want to connect to the Order Status API at https://api.example.com/orders/{orderId} to check order statuses when customers ask about their orders.

Step 4

Review the Configuration

The Builder configures the API call including the endpoint URL, request method (GET, POST, etc.), required parameters, request body structure, authentication method, and usage instructions. Review the configuration to ensure it matches your requirements.  
  


Step 5

Test and Enable

Test the API call to verify it works correctly, select which response fields the Super Agent should use, and enable the API call. The Super Agent can now use this API connection during conversations.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080298247/original/Ey1CcJp5qtfkmYfnBPge8DjHuHwTePzK7A.png?1788795614)

Success

The API call is configured and ready to use. The Super Agent will determine when to execute the call based on the instructions provided by the Builder.

5

## Configuring API Calls Manually

You can configure custom API calls manually by enabling the Custom API option in your Super Agent configuration panel. This method gives you complete control over every aspect of the API request.

Configuration Element

Request Method

Select the HTTP method for your API call: GET (retrieve data), POST (create data), PUT (replace data), PATCH (update data), or DELETE (remove data).

Configuration Element

Endpoint URL

Enter the full API endpoint URL. Include path parameter placeholders using curly braces, such as https://api.example.com/orders/{orderId}.

Configuration Element

Path and Query Parameters

Define path parameters (values inserted into the URL path) and query parameters (values appended to the URL after a question mark). Specify parameter names and provide descriptions to help the Super Agent understand what information to collect.

Configuration Element

Headers

Add custom headers required by the API, such as Content-Type or Accept headers. Headers are sent with every request.

Configuration Element

Request Body

For POST, PUT, and PATCH requests, configure the JSON request body structure. Define the fields the Super Agent should populate based on information collected from the contact.

Configuration Element

Authentication

Select the authentication method: API Key (header or query parameter), Bearer Token (OAuth), Basic Authentication (username and password), or No Authentication for public endpoints.

Configuration Element

Usage Instructions

Provide clear instructions defining when the Super Agent should use this API call. Describe the conversation scenarios, triggers, or contact requests that should cause the Super Agent to execute this API call.

Tip

Write detailed usage instructions. The clearer your instructions, the more accurately the Super Agent will determine when to use the API call.

6

## Testing and Selecting Response Fields

Before enabling a custom API call, you can test it to verify the configuration and select which response fields the Super Agent should use.

Testing Step 1

Provide Test Values

Enter test values for all required parameters (path parameters, query parameters, and request body fields). Use realistic values that will return a valid response from the API.

Testing Step 2

Execute the Test Request

Click the test button to execute the API call. The system sends the request to the API endpoint using your test values and authentication credentials.

Testing Step 3

Review the Preview

The test interface displays four preview sections: the complete request details, the cURL command equivalent, the HTTP status code, and the full JSON response from the API.

Testing Step 4

Select Response Fields

Review the API response and select which fields the Super Agent should receive and use in conversations. Selecting specific fields keeps the result focused and helps the Super Agent understand the data structure.

Important

Only select response fields that are relevant to the Super Agent's task. Including too many fields or unnecessary data can confuse the Super Agent and reduce response quality.

7

## How Super Agents Use APIs in Conversations

Once a custom API call is configured and enabled, the Super Agent can use it naturally during conversations without requiring manual intervention.

**Automatic Relevance Detection:** The Super Agent evaluates the conversation context against the usage instructions you provided. When it determines an API call is relevant, it initiates the execution process automatically.

**Natural Information Gathering:** If any required parameters are missing, the Super Agent asks the contact for the information using natural conversation. For example, if the API requires an order ID, the Super Agent might say "I'd be happy to check your order status. Could you provide your order number?"

**Automatic Field Mapping:** The Super Agent places collected information into the correct request fields. If the contact provides an order number, the Super Agent automatically inserts it into the path parameter, query parameter, or request body field you configured.

**Secure Execution:** The API call executes using the authentication credentials you configured. The Super Agent sends the request to the external API, receives the response, and extracts the selected response fields.

**Conversational Response:** The Super Agent interprets the API response data and incorporates it into its reply naturally. For example, "I checked your order #12345. It shipped yesterday and is expected to arrive on Friday."

8

## Frequently Asked Questions

Q: Can I use both the Super Agent Builder and manual configuration for different API calls?

Yes. You can use the Builder for some API calls and configure others manually. Choose the method that works best for each specific API connection.

Q: How many custom API calls can I add to a single Super Agent?

A Super Agent can have multiple custom API calls. There is no specified limit mentioned in the documentation. Add as many API connections as needed to support your Super Agent's capabilities.

Q: What happens if an API call fails during a conversation?

When an API call fails, the Super Agent can recognize the error and respond appropriately. The exact behavior depends on the error type and your Super Agent's configuration. Test API calls thoroughly before enabling them to minimize failure risks.

Q: Can the Super Agent use data from one API call as input for another API call?

Yes. The Super Agent can chain API calls by using response data from one call as parameters for subsequent calls. This enables complex multi-step workflows within a single conversation.

Q: How does the Super Agent know which API call to use when multiple calls are configured?

The Super Agent uses the usage instructions you provide for each API call to determine relevance. Write clear, specific instructions that distinguish when each API call should be used based on conversation context and contact requests.

Q: Can I test an API call with different parameters without re-configuring it?

Yes. The testing interface allows you to provide different test values each time you test the API call. You can verify the configuration works correctly with various parameter combinations without modifying the base configuration.

Q: What authentication methods are supported for custom API calls?

Custom API calls support API Key authentication (in headers or query parameters), Bearer Token authentication (OAuth), Basic Authentication (username and password), or no authentication for public endpoints.

Q: Do I need to know how to write cURL commands to use custom API calls?

No. The cURL preview is provided for reference and debugging purposes, but you don't need to write or understand cURL commands. Configure API calls using the visual interface or the Super Agent Builder's conversational setup.

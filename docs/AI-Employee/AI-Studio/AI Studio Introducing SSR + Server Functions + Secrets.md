# AI Studio: Introducing SSR + Server Functions + Secrets

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008701-ai-studio-introducing-ssr-server-functions-secrets](https://help.gohighlevel.com/support/solutions/articles/155000008701-ai-studio-introducing-ssr-server-functions-secrets)  
**Category:** AI Employee  
**Folder:** AI Studio

---

AI Studio

AI Studio: SSR + Server Functions + Secrets

Build full-stack AI Studio applications with server-side rendering, private server logic, REST APIs, secure Secrets, and an integrated publishing workflow.

What You'll Learn

AI Studio now supports full-stack web applications with **server-side rendering (SSR), Server Functions, REST APIs, and secure Secrets**. New AI Studio projects use **TanStack Start** , combining frontend pages and server functionality in the same project.

This guide explains how each capability works, when to use Server Functions instead of REST APIs, how to protect credentials, how existing projects are affected, and how to publish a full-stack application.

Existing AI Studio Projects

Existing Vite/React AI Studio projects continue using their current architecture and are not automatically migrated to TanStack Start. The new full-stack architecture applies to new projects unless an existing project is migrated separately.

Table of Contents

1\. What is AI Studio SSR, Server Functions, and Secrets? 2\. Key Benefits 3\. How the Full-Stack Architecture Works 4\. Choosing Between Server Functions and REST APIs 5\. New Projects vs. Existing Projects 6\. How To Setup and Use the Full-Stack Features 7\. SEO Considerations 8\. Troubleshooting 9\. Frequently Asked Questions 10\. Related Articles

# **What is AI Studio SSR, Server Functions, and Secrets?**  
  


AI Studio's full-stack architecture extends the builder beyond frontend-only applications. New projects can render pages on the server, execute private application logic, expose HTTP endpoints, and store sensitive credentials outside browser code.

These capabilities are built around four parts:

  * **Server-Side Rendering (SSR):** Generates page HTML on the server before it is delivered to the browser.
  * **Server Functions:** Run private application logic on the server while allowing the application's frontend to call it.
  * **REST APIs:** Create HTTP endpoints such as `/api/...` for integrations, webhooks, and external applications.
  * **Secrets:** Store API keys, tokens, webhook secrets, and other sensitive values outside client-side code.


## **Key Benefits of AI Studio Full-Stack Projects**  
  


Full-stack support lets AI Studio combine the customer-facing interface with the server functionality needed to power it. This reduces the need to maintain separate frontend and backend projects for supported use cases.

  * **Server-Rendered Content:** Deliver meaningful HTML to visitors, search engines, and services that generate social previews.
  * **Private Backend Logic:** Keep sensitive application logic away from browser code.
  * **Secure Credentials:** Store API keys and tokens as Secrets rather than exposing them in the client bundle.
  * **External Integrations:** Create REST endpoints for webhooks, third-party services, and external applications.
  * **Unified Development:** Build frontend and supported backend functionality within the same AI Studio project.
  * **Integrated Publishing:** Publish the application and its supported server functionality from the same workflow.
  * **Backward Compatibility:** Existing Vite/React projects continue operating without being automatically converted.


## **How the AI Studio Full-Stack Architecture Works**

Each capability handles a different part of the application. Separating page rendering, private backend logic, public HTTP endpoints, and protected configuration helps keep the project easier to understand and maintain.

Capability| Primary Purpose| Typical Use  
---|---|---  
**SSR**|  Render pages on the server.| SEO, public pages, and social previews.  
**Server Functions**|  Run private application logic.| Internal backend operations and protected integrations.  
**REST APIs**|  Expose HTTP endpoints.| Webhooks, integrations, and external applications.  
**Secrets**|  Protect sensitive configuration.| API keys, tokens, and credentials.  
  
### **Server-Side Rendering (SSR)**

Server-Side Rendering generates page HTML on the server before returning it to the visitor. Search engines, social platforms, and browsers can therefore receive page content without depending entirely on client-side JavaScript to construct the page.

SSR is especially useful for:

  * Marketing websites and landing pages
  * Multi-page websites
  * Public application pages
  * Pages with unique URLs and metadata
  * Search-focused content
  * Pages shared through services that generate link previews


### **Server Functions**

Server Functions let the application's frontend request server-side operations without placing the implementation itself in the browser bundle. They are useful for work that belongs to the application but should remain private.

  * Calling external services with private credentials
  * Loading protected data
  * Validating submitted information
  * Performing server-side calculations
  * Transforming data before returning it to the frontend
  * Keeping sensitive application logic off the client


**Security Tip:** Server Functions can keep implementation details on the server, but sensitive credentials should still be stored as Secrets. Return only the information the browser actually needs.

### **REST APIs**

REST API routes create HTTP endpoints that services outside the AI Studio application can call. Routes can use paths such as `/api/...` and can support methods such as GET or POST depending on the application.

  * Receiving webhooks
  * Connecting third-party applications
  * Building public or authenticated APIs
  * Accepting information from another service
  * Returning structured data such as JSON


### **Secrets**

Secrets provide server-side storage for information that should not be included in frontend code. This allows server-side application functionality to use sensitive values without deliberately exposing them in the client bundle.

  * API keys
  * Authentication tokens
  * Webhook signing secrets
  * Integration credentials
  * Private service configuration


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080660269/original/5rcCxcCqpmXu39z7BxQHxxaMZGld2ERYaw.png?1789100021)

## **Choosing Between Server Functions and REST APIs**

Selecting the correct server interface keeps the application simpler and reduces unnecessary public endpoints. Use Server Functions for private logic called by the application's own frontend, and REST APIs when an outside system needs a callable HTTP endpoint.

Need| Recommended Approach  
---|---  
Frontend securely calls its own backend logic| **Server Function**  
External service sends data into the application| **REST API**  
Third-party system needs an HTTP endpoint| **REST API**  
Internal operation requires a private API key| **Server Function + Secret**  
Webhook provider needs a callback URL| **REST API**  
Sensitive value must stay outside browser code| **Secret**  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080660275/original/erpRqacDGDKsWNrDuvb7e1X2erMVJt73Ig.png?1789100058)

## **New Projects vs. Existing Vite/React Projects**

AI Studio preserves existing projects rather than automatically changing their underlying framework. Knowing which architecture the project uses helps determine which backend, SEO, and migration guidance applies.

Project Type| Behavior  
---|---  
**New AI Studio Project**|  Uses the current TanStack Start full-stack architecture.  
**Existing Vite/React Project**|  Continues using its existing architecture.  
**Existing Project Needing the New Stack**|  Requires a separate migration process instead of being automatically converted.  
  
**Recommendation:** Do not recreate an existing project solely because the new architecture is available. First determine whether the application actually needs SSR, private server logic, REST endpoints, or Secrets.

## **How To Setup and Use SSR, Server Functions, REST APIs, and Secrets**

Start with the application's functional requirements before deciding how each capability should be implemented. Clearly identifying private operations, external integrations, and sensitive credentials helps AI Studio place functionality in the appropriate part of the application.

### **Step 1: Create a New AI Studio Project**

New AI Studio projects use the current full-stack architecture and can combine frontend pages with supported server-side functionality.

  1. Open the applicable HighLevel sub-account.
  2. Enable **AI Studio** from Labs if it is not already enabled.
  3. Open **AI Studio** from the left navigation.
  4. Create a new project.
  5. Describe the website or application you want AI Studio to build.


### **Step 2: Describe the Full Application Behavior**

Describe what the application needs to do, not only how it should look. Mention external services, private credentials, incoming webhooks, protected processing, and public API requirements when applicable.

Example Prompt

Build an order-status portal with a public landing page, a private account lookup that runs on the server, and an API endpoint for receiving order-status webhooks.

### **Step 3: Add Secrets for Protected Credentials**

Configure Secrets whenever server functionality needs a value that should not be exposed in browser code.

  1. Identify the private credential required by the integration.
  2. Add it through the Secrets workflow when prompted.
  3. Give the Secret a clear and recognizable name.
  4. Reference the Secret only from the server-side functionality that needs it.
  5. Test the integration without returning the private credential to the browser.


### **Step 4: Build and Review Server Functions**

Use Server Functions when the application's own frontend requires backend functionality that should remain private.

  1. Verify that sensitive processing runs on the server.
  2. Confirm private credentials are retrieved from Secrets.
  3. Return only the information required by the frontend.
  4. Test successful and unsuccessful requests.
  5. Review the generated code when additional validation or customization is required.


### **Step 5: Create REST APIs for External Requests**

Use a REST API route when another service or application needs to communicate with the AI Studio project through HTTP.

  1. Define the endpoint path.
  2. Define the supported HTTP method.
  3. Define the expected request payload.
  4. Add authentication or signature validation when required.
  5. Process the request on the server.
  6. Return the appropriate response.


**Webhook Security:** Validate webhook authentication or signatures when the provider supports them before processing protected operations.

### **Step 6: Preview and Test the Application**

Testing both frontend and backend behavior before publishing helps identify problems that may not be visible from the page design alone.

  * Confirm public pages load correctly.
  * Test Server Functions with expected and unexpected inputs.
  * Test REST endpoints with the intended requests.
  * Confirm Secrets are not exposed in browser-visible output.
  * Verify important error states are handled safely.
  * Review page titles, headings, and metadata.


### **Step 7: Publish the Application**

Publishing makes the application available through its live AI Studio URL and deploys the supported application runtime.

  1. Click **Publish**.
  2. Review or update the generated website address.
  3. Confirm publication.
  4. Open the published URL and test the live application.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080660298/original/sBAV36e4SOlTJmYOOAZMWveDqPTmeZlfOA.jpeg?1789100104)

### **Step 8: Connect a Custom Domain**

A custom domain can be connected after publishing when you want visitors to access the application through your own domain instead of the generated project URL.

  1. Open **Publish**.
  2. Select **Add Custom Domain**.
  3. Enter the domain you want to use.
  4. Add the DNS records provided by AI Studio at your domain provider when required.
  5. Click **Verify DNS**.
  6. Allow certificate provisioning to complete.
  7. Test the application through the connected domain.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080660313/original/b_NQ-jU2huRL8l7XCuxWaoYiTiR9DFH4Ww.png?1789100124)

## **SEO Considerations for AI Studio Projects**  
  


SEO behavior depends on the architecture used by the project. New full-stack projects use server-side rendering, while existing Vite/React projects continue using their current architecture and the SEO tools applicable to that project type.

Review the following before publishing important public pages:

  * Page titles
  * Meta descriptions
  * Heading structure
  * Canonical URLs when applicable
  * Social preview information
  * Sitemap behavior when applicable
  * Rendered content on the live published page


## **Troubleshooting AI Studio Full-Stack Projects**  
  


Full-stack application issues can originate from frontend code, server logic, endpoint configuration, Secrets, publishing, or DNS. Identifying which layer is failing makes troubleshooting faster and helps avoid unnecessary project changes.

Issue| What to Check  
---|---  
**Server Function fails**|  Review function inputs, required Secrets, server-side errors, and the data returned to the frontend.  
**REST endpoint cannot be called**|  Confirm the endpoint path, HTTP method, published application state, request format, and authentication requirements.  
**External API authentication fails**|  Confirm the correct Secret exists and that server-side code references the intended value.  
**Webhook requests fail verification**|  Verify the signing Secret, request headers, signature-validation logic, and callback URL.  
**Custom domain does not load**|  Confirm the DNS records exactly match the values provided by AI Studio and complete Verify DNS after propagation.  
**Existing project does not show new architecture behavior**|  Confirm whether the project was created using the earlier Vite/React architecture. Existing projects are not automatically migrated.  
  
## **Frequently Asked Questions**  
  


Q: Do existing AI Studio projects automatically move to TanStack Start?

No. Existing Vite/React projects continue using their existing architecture and are not automatically migrated.

Q: What is the difference between a Server Function and a REST API?

Server Functions are primarily used when the application's own frontend needs private backend logic. REST APIs expose HTTP endpoints that external systems or applications can call.

Q: Can a Server Function use a Secret?

Yes. This is a common approach when server-side application logic requires a private API key, authentication token, or other protected credential.

Q: Can I create webhook endpoints in AI Studio?

Yes. REST API routes can provide HTTP endpoints that supported webhook providers can call.

Q: Should I put a Secret directly in frontend code?

No. Sensitive credentials should remain in Secrets and be referenced only by server-side functionality that requires them.

Q: Does SSR replace the Advanced SEO workflow for older AI Studio projects?

No. Existing projects retain their existing architecture, so the SEO tools applicable to those projects remain relevant.

Q: Can I manually edit generated backend code?

Yes. The AI Studio Code Editor provides direct access to project code for supported manual changes and validation.

Q: Can I download my AI Studio project code?

Yes. AI Studio supports downloading the project codebase as a ZIP, including supported versions available through Version History.

### **Related Articles**  
  


[ AI Studio in HighLevel ](<https://help.gohighlevel.com/support/solutions/articles/155000007587-ai-studio-in-highlevel>) [ Code Editor in AI Studio ](<https://help.gohighlevel.com/support/solutions/articles/155000007652>) [ Advanced SEO Support in AI Studio ](<https://help.gohighlevel.com/support/solutions/articles/155000007691>) [ Visual Edits in AI Studio ](<https://help.gohighlevel.com/support/solutions/articles/155000007914>) [ Connect Forms and Calendars in AI Studio ](<https://help.gohighlevel.com/support/solutions/articles/155000007599-connect-forms-and-calendars-in-ai-studio>) [ Download AI Studio Codebase as ZIP ](<https://help.gohighlevel.com/support/solutions/articles/155000008639-download-ai-studio-codebase-as-zip>)

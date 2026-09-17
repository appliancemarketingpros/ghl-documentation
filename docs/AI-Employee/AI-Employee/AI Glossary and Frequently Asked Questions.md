# AI Glossary and Frequently Asked Questions

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008598-ai-glossary-and-frequently-asked-questions](https://help.gohighlevel.com/support/solutions/articles/155000008598-ai-glossary-and-frequently-asked-questions)  
**Category:** AI Employee  
**Folder:** AI Employee

---

This article explains common AI terminology and answers frequently asked questions about AI usage across HighLevel. Use it to better understand AI activity, usage, and the different ways AI products may measure or charge for usage.

  


For current product-specific pricing, included usage, and billing details, see [AI Product Pricing.](<https://help.gohighlevel.com/en/support/solutions/articles/155000006652>)

* * *

**TABLE OF CONTENTS**

  * AI Glossary
    * Tokens
    * Usage
    * 3x Usage
    * Request
    * Prompt
    * Session
  * Frequently Asked Questions
    * Why can't I bring my own AI API keys?
    * Are AI Studio and Ask AI included in the AI Employee plans?
    * How is token cost accumulated?
    * Why did one request use more tokens than another?
    * Why can AI Studio usage increase as I continue working on a project?
    * Why does AI Studio and Ask AI use a 5-hour usage window?
    * When will other current free AI products turn to PPU?
    * Is the Managed Agents feature included in the AI Employee Plans?
  * Related Articles


* * *

## **AI Glossary**

  


Understanding common AI terminology can help you make sense of how HighLevel AI products work, how usage is measured, and why different interactions may require different amounts of AI processing.

  


### **Tokens**

  


AI tokens are the s**mall pieces of text an AI reads and writes** when processing a request.

  


Think of tokens like puzzle pieces. When you type a prompt, AI breaks your words into smaller pieces called tokens. It processes those tokens to understand what you’re asking, then uses more tokens to create its response.

For example, **“Write a follow-up email for this lead”** gets broken into tokens. Both your prompt and the AI-generated email count toward token usage.

The key takeaway is simple: **the more information AI processes or generates, the more tokens it uses.** Tokens are often how AI usage and costs are measured.

  


  


### **Usage**

  


Usage reflects how much computing power your AI requests require. Not every request uses the same amount. A simple Ask AI request may use less usage, while building a more complex project in AI Studio may use more.

  


Want a better idea of what that looks like? Use our [Usage plan calculator ](<https://ai-plan-calculator.vibepreview.com/>)to see examples of the AI Studio projects you can build and the types of Ask AI requests you can make with your usage. It can also help you compare usage levels and find the plan that best fits how you work.  
  
Already an active client using AI tools? Use your AI Suite, tab Usage Dashboard located in Agency View to review your personalized charges and usage. For more info, see: [AI Usage Dashboard](<https://help.gohighlevel.com/support/solutions/articles/155000007742-ai-usage-dashboard>)[](<https://help.gohighlevel.com/support/solutions/articles/155000007742-ai-usage-dashboard>)

  


  


### **3x Usage**

  


3x usage means you get three times the usage capacity within the same rolling 5-hour window.

  


For example, if standard usage gives you a certain amount of AI activity during a five-hour period, 3x usage lets you do roughly three times as much before reaching that window’s usage threshold.

  


Actual usage will still vary depending on the complexity of your requests.

  


  


### **Request**

  


A request is an instruction or task submitted to an AI experience such as Ask AI, AI Studio or Managed Agents.

  


A request does not represent a fixed amount of AI usage or a fixed charge. A simple request may require relatively little processing, while another may require the AI to reason through multiple steps, retrieve or analyze information, generate content or images, or perform actions.

  


For example, asking AI Studio to create a website is one request. Sending another prompt asking it to change the headline creates another request, but the amount of AI processing required for each request may be different.

  


  


### **Prompt**

  


A prompt is the message, question, instruction, or information you provide to an AI tool. Prompts can range from simple questions to detailed instructions containing background information, requirements, uploaded files, images, or other context. For Ask AI and AI Studio, submitting a prompt counts as a request.

Example: _"Create a three-page website for a dental practice with a homepage, services page, and contact page."_

  


Prompt length alone does not determine total AI usage. Task complexity, context, the model used, and the generated output can also affect how much AI processing is required.

  


  


### **Session**

  


A session is a group of interactions used to complete work within supported AI products such as Ask AI.

  


A session may contain multiple prompts or requests. For example, an Ask AI session may involve retrieving information, generating content, processing follow-up instructions, and requesting approval before completing an action.

  


Note that not every HighLevel AI product uses sessions as a usage or billing measurement.

* * *

## **Frequently Asked Questions**

  


### **Why can't I bring my own AI API keys?**

HighLevel uses multiple AI providers and models across its AI products. Requiring customers to maintain their own accounts, API keys, and billing relationships with every supported AI provider would make setup and ongoing management significantly more complicated.

  


HighLevel often adds providers, introduces newer models, or changes which models are used for particular AI tasks. Managing these integrations within HighLevel allows those changes to happen without requiring customers to replace or reconfigure their own API keys.

  


  


### **Are AI Studio and Ask AI included in the AI Employee plans?**

Yes. Both AI Studio and Ask AI are included with AI Employee plans.  
  


  * **AI Employee Growth** includes standard usage within a rolling 5-hour window.  
  

  * **AI Employee Unlimited** includes 3x usage within the same rolling 5-hour window, giving you more capacity to build and ask before reaching your usage threshold.


  


Not sure how much usage you need? Use our [AI plan calculator](<https://ai-plan-calculator.vibepreview.com/>) to see examples of what you can build with AI Studio and the types of requests you can make with Ask AI to find the plan that fits you best.

  


  


### **How is token cost accumulated?**

Token cost is based on the amount of information the AI processes and the amount of content it generates.

  


When you send a request, the AI uses **input tokens** to read things like your prompt, instructions, conversation history, knowledge base content, and other context. It then uses **output tokens** to generate its response.

  


The total cost depends on how many tokens are processed and the pricing of the AI model being used. Different models have different token rates, so two requests using the same number of tokens may not have the same cost. HighLevel calculates these costs automatically based on the models and actions used.

  


For current model rates and product-specific pricing, see [AI Product Pricing Guide.](<https://help.gohighlevel.com/en/support/solutions/articles/155000006652>)

  


  


### **Why did one request use more tokens than another?**

Not every request requires the same amount of AI processing. Usage can vary based on the amount of context involved, task complexity, requested output, information retrieval or analysis, generated assets, and the AI models used.

  


As a result, two prompts that appear similar may still use different numbers of tokens.

  


  


### **Why can AI Studio usage increase as I continue working on a project?**

AI Studio maintains project context so that it can understand previous instructions and changes. For example, if you have already established a site's design, structure, style, and other requirements, later requests may use that existing context when determining how to make your next change.

  


This makes iterative development easier because you do not have to restate every previous requirement. However, maintaining and processing additional context can increase the amount of AI processing required for later requests. For more information, see [AI Studio - Pricing](<https://help.gohighlevel.com/en/support/solutions/articles/155000008322>)

  


  


### **Why does AI Studio and Ask AI use a 5-hour usage window?**

AI Studio and Ask AI use a rolling 5-hour usage window to help keep AI fast and reliable for everyone. Because AI tasks require significant computing power, the window helps balance demand and prevent periods of heavy usage from slowing down the experience.

  


Your usage is measured continuously over the previous five hours. As older activity falls outside that window, usage becomes available again, so you don’t have to wait for a fixed daily reset.

  


  


### **When will other current free AI products turn to PPU? (AI Blog Builder, certificate builder, funnel builder, email builder)**

These will all stay free.

  


  


### **Is the Managed Agents feature included in the AI Employee Plans?**

Yes Managed agents are included: 100 agent runs on Growth, 1000 agent runs on Unlimited. For more information, see: [AI Product Pricing](<https://help.gohighlevel.com/en/support/solutions/articles/155000006652>)

* * *

## **Related Articles**

  


  * **[](<https://help.gohighlevel.com/en/support/solutions/articles/155000006652>)**[](<https://help.gohighlevel.com/en/support/solutions/articles/155000006652>)[](<https://help.gohighlevel.com/en/support/solutions/articles/155000006652>)[AI Product Pricing](<https://help.gohighlevel.com/en/support/solutions/articles/155000006652>)  
  

  * [AI Usage Dashboard](<https://help.gohighlevel.com/en/support/solutions/articles/155000007742>)  
  

  * [AI Studio – Pricing](<https://help.gohighlevel.com/en/support/solutions/articles/155000008322>)  
  

  * [Ask AI Session Examples & Usage Costs](<https://help.gohighlevel.com/en/support/solutions/articles/155000007818>)  
  

  * [AI Usage Limits](<https://help.gohighlevel.com/en/support/solutions/articles/155000007813>)


##

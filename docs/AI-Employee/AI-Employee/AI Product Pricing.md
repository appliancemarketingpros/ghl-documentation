# AI Product Pricing

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006652-ai-product-pricing](https://help.gohighlevel.com/support/solutions/articles/155000006652-ai-product-pricing)  
**Category:** AI Employee  
**Folder:** AI Employee

---

Some HighLevel AI features have free access and no longer use AI credits. To keep performance stable for all users, fair-usage protections may apply. If a user reaches the daily limit, access resets in 24 hours.

  
This article lists pricing by product. Always use the product-specific section below before you quote pricing or rebilling details.

* * *

**TABLE OF CONTENTS**

  * AI Employee Unlimited Plan
    * Ask AI Pricing (Pay-Per-Use)
    * Conversation AI Pricing (Pay-Per-Use)
    * Voice AI Pricing (Pay-Per-Use)
      * External Voice AI Models
      * Voice AI Prompt Optimizer
    * Agent Studio Pricing
      * Agent Response Generation
      * External APIs
      * Multimodal and Specialized Models
    * Workflow AI Pricing
    * Funnel & Website AI
    * Content AI Pricing
    * Reviews AI Pricing
    * AI Studio Pricing


* * *

# ** _AI Employee Unlimited Plan_**

  


On the Unlimited subscription, users will enjoy unmetered usage of the AI Employee features for only $97/month!

  


**Fair Use Policy:** Your use of Employee AI is subject to HighLevel's Terms of Service, including Excessive Use Restrictions. If HighLevel determines in its sole discretion that your usage is excessive, abusive, or negatively impacts our platform, we reserve the right to throttle, limit, require service upgrades, or terminate your access with or without notice.

  


**AI Employee** includes:

  


  * **Voice AI (Inbound)**  
  

  * **Conversation AI**  
  

  * **Reviews AI**  
  

  * **Content AI**  
  

  * **Ask AI**


  


**AI Employee Plus** includes:

  

    
    
    **Note:** The AI Employee Plus features are not included in the Unlimited subscription and will continue to be pay-per-use.

  


  * **Agent Studio**  
  

  * **Voice AI Widget**  
  

  * **Voice AI Outbound**  
  

  * **Prompt Optimizer**  


  


So AI Employee Unlimited covers use of Voice AI ( via inbound phone calls), Conversation AI, Reviews AI, Content AI, and Ask AI. It **does not cover use of Agent Studio, Voice AI Prompt Optimizer, or use of Voice AI through the website voice chat widget, or via outbound phone calls**. Unlimited coverage is subject to the Fair Use Policy.

  

    
    
    **Note:** Phone System charges still apply to all phone calls, they are still pay-per-use even when using Voice AI (Inbound) under the AI Employee Unlimited subscription. 

  


  

    
    
    **Note:** We are coming up with cheaper subscription places for AI Employee, New cheaper plan rates are coming soon.

  


* * *

## **_Ask AI Pricing (Pay-Per-Use)_**

  


Ask AI uses multiple models behind the scenes to handle requests. The model selected depends on the complexity of the query. For pay-per-use usage, we charge at cost.

  


Agency users can choose to rebill this usage to their sub-accounts with a markup based on their plan.

  


Here is an article that shows how ASK AI Usage will be priced accross few example sessions:  
<https://help.gohighlevel.com/support/solutions/articles/155000007818-ask-ai-sessions-pricing-overview>

  


  


## **_Conversation AI Pricing (_****_Pay-Per-Use)_**

  


Conversation AI pricing is transitioning to token-based, with model token usage at API pricing. This change ensures you pay exactly for the tokens you use.

  


Provider| Model| Input Price / 1M Tokens| Output Price / 1M Tokens  
---|---|---|---  
OpenAI| Chat GPT-5| $1.25| $10.00  
OpenAI| Chat GPT-5 Mini| $0.25| $2.00  
OpenAI| Chat GPT-4.1| $2.00| $8.00  
OpenAI| Chat GPT-4.1 Mini| $0.40| $1.60  
  
* * *

## ** _Voice AI Pricing** _(_****_Pay-Per-Use)_**_**

  


Voice AI pricing includes: 

  


  1. A per-minute Voice Engine charge.
  2. A per-minute text-to-speech (TTS) charge based on your selected provider/model. 
  3. LLM token usage based on your selected model.


  


Per-Minute Voice Engine Charge

  


May 20 onward: Voice Engine: $0.045/min

  


If you are reviewing historical usage before May 20, you may see older bundled Voice AI pricing.

  


TTS Provider Rates (Per Minute)

  


TTS Provider| Model| TTS Rate| Effective Date  
---|---|---|---  
OpenAI| (TTS)| $0.015/min| April 20  
Cartesia| (TTS)| $0.015/min| April 20  
ElevenLabs| V3| $0.17/min| April 20  
ElevenLabs| V2.5| $0.035/min| May 20  
  
  


**Invoice Line Items (May 20 onward)**

  


Starting **May 20** , Voice AI charges are shown as separate line items for:

  


  * Voice Engine (**$0.045/min**)  
  

  * TTS (based on your selected provider/model)


  


**Total Voice AI Cost (Pay-Per-Use)**

  


**Total Voice AI cost per call =**

(call duration in minutes × (Voice Engine rate + selected TTS rate))

\+ (total call tokens ÷ 1,000,000 × selected model price)

  


Phone calls are usually framed as cost per minute, so you can model Voice AI like this:

  


**Average cost per minute =**

(Voice Engine rate + selected TTS rate)

\+ (average tokens per minute ÷ 1,000,000 × selected model price)

  


**Examples (per-minute, excluding LLM tokens):**

  


**OpenAI or Cartesia TTS:** $0.045 + $0.015 = $0.06/min  
  


**ElevenLabs V2.5 (May 20 onward):** $0.045 + $0.035 = $0.08/min

  


Two calls with the same duration can cost different amounts. 

  


The Voice Engine and TTS portions are driven by time, while the LLM portion is driven by token usage and the model you choose. 

  


**What usually increases the price:**

  


  * Longer call duration
  * Larger prompts or more retrieved context
  * More turns in the conversation
  * Faster or denser speech, which can increase tokens per minute
  * Higher-cost models


  

    
    
    **Want to keep your costs at $0.06/min?** 
    Switch to one of our new TTS providers — OpenAI, Cartesia— at $0.015/min for TTS, bringing your total to $0.06/min (voice engine $0.045 + TTS $0.015), the same rate you pay today.

  


### **External Voice AI Models**

  


If you choose to use an external AI model such as Google's Genimi, OpenAI's ChatGPT, or Anthropic's Claude, to power your HighLevel Voice AI, the pricing of the models are as follow:

  


Provider| Model| Price of LLM Model/1M Tokens  
---|---|---  
Google| Gemini 2.0 Flash | $0.10  
Google| Gemini 2.0 Flash Lite| $0.075  
Google| Gemini 2.5 Flash | $0.30  
Google| Gemini 2.5 Flash Lite| $0.10  
OpenAI| GPT 4o Mini| $0.15  
OpenAI| GPT 4o| $2.50  
OpenAI| GPT 4.1 Nano| $0.10  
OpenAI| GPT 4.1 Mini| $0.40  
OpenAI| GPT 4.1| $2.00  
OpenAI| GPT 5 Nano| $0.05  
OpenAI| GPT 5 Mini| $0.25  
OpenAI| GPT 5| $1.25  
Anthropic| Claude 4.5 Sonnet| $3  
Anthropic| Claude 4.0 Sonnet| $3  
Anthropic| Claude 3.7 Sonnet| $3  
Anthropic| Claude 3.5 Haiku| $0.80  
  
###   


###  _**Voice AI Prompt Optimizer**_

  


Prompt Optimizer includes **20 minutes per day for each location**. After the included 20 minutes are used, any additional usage is billed at your applicable **Voice AI rate**.

* * *

## **_Agent Studio Pricing_**

  


Agent Studio, which include multimodal and specialized AI capabilities, will be charged at model token usage at API Pricing.

  


### **Agent Response Generation**

  


Provider| Model| Input Price / M Tokens| Output Price / M Tokens  
---|---|---|---  
OpenAI| GPT-5| $1.25| $10.00  
OpenAI| GPT-5 Mini| $0.25| $2.00  
OpenAI| GPT-5 Nano| $0.05| $0.40  
OpenAI| GPT-4.1| $2.00| $8.00  
OpenAI| GPT-4.1 Mini| $0.40| $1.60  
OpenAI| GPT-4.1 Nano| $0.10| $0.40  
  
  


  


### **External APIs**

  


Feature| Provider| Price  
---|---|---  
Web Search| Tavily| $0.01/search  
  
  


  


### **Multimodal and Specialized Models**

  


 _** All prices are in USD. Prices for third-party models are subject to change by the respective provider (Google, Anthropic, OpenAI)_

  


Content Type| Provider| Model| Quality| Size| Price/Unit| Unit  
---|---|---|---|---|---|---  
Video| Gemini| Veo3 Fast|   
| -| $0.15| Second of Video  
  
| Gemini| Veo3|   
|   
| $0.40| Second of Video  
Image| OpenAI| DALL-E 3| Standard| 1024 x 1024| $0.04| Image Output  
1024 x 1536 / 1536 x 1024 | $0.08  
  
|   
|   
| HD| 1024 x 1024| $0.08| Image Output  
1024 x 1536 / 1536 x 1024| $0.12  
Text| OpenAI| gpt4.1|   
| -| $2.00| 1M Tokens Input  
  
|   
|   
|   
| -| $8.00| 1M Tokens Output  
Text| OpenAI| gpt5 mini|   
| -| $0.25| 1M Tokens Input  
  
|   
|   
|   
| -| $2.00| 1M Tokens Output  
Speech| OpenAI LLM| gpt-4o-mini |   
| -| $0.15| 1M Token (Text)  
LLM+TTS|   
| -| $0.60 | 1M Token (Text Output)  
OpenAI  
TTS| gpt-4o-mini-tts|   
| -| $12.00| 1M Token (Audio Output)  
  
* * *

## **_Workflow AI Pricing_**

  
 _**Refer to[Workflow Pro Plans](<https://help.gohighlevel.com/en/support/solutions/articles/155000003971>) for bulk purchase of premium actions at a cheaper price_

  
Workflow AI| Tools/Actions| Pricing  
---|---|---  
Actions| Decision Maker| $0.01/execution  
  
| Intent Detection| $0.01/execution  
  
| Summarize Text| $0.01/execution  
  
| Translate| $0.01/execution  
Builder| Let Workflow AI create Workflows for you(Multi-language Support) with a simple prompt.| FREE (limit resets within 24hrs)  
**Generate**|  Generate with AI (SMS, email, code, etc)| FREE (limit resets within 24hrs)  
External Models| Use OpenAI inside of a workflow using the GPT workflow action.| Refer to OpenAI for API Price  
  
* * *

## ** _Funnel & Website AI_**

  


Funnel & Website AI allows building and editing funnels/websites with the help of prompts.

  
Funnel AI| Rate Limit| Pricing  
---|---|---  
Build Funnels & Websites with AI| 1000 prompts per day _(per sub-account)_|  FREE  
  
* * *

## ** _Content AI Pricing_**

  


**Content Type**| **Pricing**  
---|---  
Image| $0.063/Image  
Text| $0.0945/1000 Words  
  
* * *

## ** _Reviews AI Pricing_**

  


  
| Pricing  
---|---  
Reviews AI| $0.01 / review   
  
  

    
    
    Workflow AI Builder and Generate with AI do not use AI credits. These features are free to use, subject to fair-usage protections. If a user reaches the daily limit, access resets in 24 hour

* * *

## ** _AI Studio Pricing_**

  


AI Studio is currently free and pricing is expected to evolve over time.

  


We want as many people as possible to experience the power of AI Studio so we don't have immediate plans to charge for its use. In the future, we may have a cap on usage wherein overages would be charged at a reasonable token price.

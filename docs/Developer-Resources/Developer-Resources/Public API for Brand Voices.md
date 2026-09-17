# Public API for Brand Voices

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007943-public-api-for-brand-voices](https://help.gohighlevel.com/support/solutions/articles/155000007943-public-api-for-brand-voices)  
**Category:** Developer Resources  
**Folder:** Developer Resources

---

Brand Voice APIs in HighLevel allow you to programmatically create, manage, and update brand voices across locations. This enables seamless integration with external systems, automated onboarding workflows, and dynamic content personalization. With flexible creation modes and full CRUD capabilities, developers and agencies can scale brand management efficiently.

  

    
    
    **IMPORTANT** : For a complete list of available APIs and detailed documentation, please refer to the official API reference here: [Brand Voices](<https://marketplace.gohighlevel.com/docs/ghl/brand-boards/brand-voices/>)

* * *

**TABLE OF CONTENTS**

  * What is Brand Voice API?
  * Key Benefits of Brand Voice API
  * Brand Voice API Endpoints
  * Brand Voice Creation Modes
  * Validation Rules and Requirements
  * Frequently Asked Questions


* * *

## **What is Brand Voice API?**

  


Brand Voice APIs provide a programmatic way to create, retrieve, update, delete, and manage brand voices within HighLevel. This allows external applications, integrations, and automation systems to control how brand identity is defined and used across AI-powered features like Content AI and Agent Studio.

  


Instead of manually configuring brand voices in the UI, you can automate the process, ensuring consistency across multiple accounts, clients, or systems. This is especially valuable for agencies, SaaS platforms, and developers managing large-scale operations.

* * *

## **Key Benefits of Brand Voice API**

  


Brand Voice APIs unlock powerful automation and scalability capabilities, making it easier to maintain consistent branding across all client interactions and AI-generated content.

  


  * **Automation at Scale** : Automatically create and manage brand voices across multiple locations without manual input.  
  

  * **Flexible Creation Methods** : Generate brand voices using manual input, website URLs, or descriptive text.  
  

  * **Seamless Integrations** : Connect HighLevel with external platforms, CRMs, or onboarding systems.  
  

  * **Centralized Brand Management** : Maintain consistent tone, messaging, and audience targeting across tools.  
  

  * **Dynamic Updates** : Instantly update brand voices as businesses evolve.


* * *

## **Brand Voice API Endpoints**

  


Understanding available API endpoints helps you manage brand voices efficiently and integrate them into your workflows with precision and control.

  


  * **GET /locations/:locationId/voices**  
Retrieve a list of brand voices with support for pagination, search, and filtering (including deleted records)  
  

  * **GET /locations/:locationId/voices/:brandVoiceId**  
Retrieve full details of a specific brand voice  
  

  * **POST /locations/:locationId/voices**  
Create a new brand voice using one of the supported creation modes  
  

  * **PATCH /locations/:locationId/voices/:brandVoiceId**  
Update an existing brand voice (all fields optional during update)  
  

  * **DELETE /locations/:locationId/voices/:brandVoiceId**  
Delete a brand voice  
  

  * **POST /locations/:locationId/voices/:brandVoiceId/default**  
Set a brand voice as the default for the location


* * *

## **Brand Voice Creation Modes**

  


Different creation modes allow you to tailor how brand voices are generated, depending on available data and desired level of automation.

  


  * **Manual Mode (`manual`)**
    * Directly provide brand voice inputs such as:  
  

      * Brand name
      * Tone of voice
      * Target audience
      * Customer pain points  
  

    * Best for precise control and customization  
  

  * **URL Mode (`url`)**  

    * Provide a website URL  
  

    * HighLevel AI analyzes the site and generates brand voice content  
  

    * Ideal for quick onboarding using an existing web presence  
  

  * **Description Mode (`description`)**  

    * Provide a text-based description of the business  
  

    * AI generates brand voice details based on the description  
  

    * Useful when a website is not available


* * *

## **Validation Rules and Requirements**

  


Understanding validation rules ensures successful API requests and prevents common errors when creating or updating brand voices.  
  


  * **Required Fields for Manual Creation**  

    * `brandName`
    * `toneOfVoice`
    * `targetAudience`
    * `customerPainPoints`
  * **Required Field on Create**  

    * `type` (must be one of: `manual`, `url`, `description`)  
  

  * **Field Restrictions**  

    * Manual fields cannot be sent with `url` or `description` types  
  

    * URL field cannot be used with `manual` type  
  

    * AI-generated modes should not include manual answer fields  
  

  * **Update Behavior**  

    * All fields are optional during updates  
  

    * Only provided fields will be modified


* * *

## **Frequently Asked Questions**

  


**Q: When should I use manual vs AI-generated creation modes?**  
Manual mode is best for precise control, while URL and description modes are ideal for quick, automated setup.

  


  


**Q: Can I update only one field in a brand voice?**  
Yes, PATCH requests allow partial updates, so only the fields you send will be modified.

  


  


**Q: What happens if I send incorrect fields for a creation mode?**  
The API will return a validation error if fields do not match the selected type.

  


  


**Q: Can I have multiple brand voices per location?**  
Yes, you can create and manage multiple brand voices and set one as the default.

  


  


**Q: Is it possible to recover a deleted brand voice?**  
Deleted brand voices may be retrievable depending on system behavior, but you should confirm before deletion.

  


  


**Q: Do API-created brand voices work with Content AI and Agent Studio?**  
Yes, all brand voices created via API are fully compatible with HighLevel AI features.

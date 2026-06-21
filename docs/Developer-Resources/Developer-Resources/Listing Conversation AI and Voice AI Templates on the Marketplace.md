# Listing Conversation AI and Voice AI Templates on the Marketplace

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005412-listing-conversation-ai-and-voice-ai-templates-on-the-marketplace](https://help.gohighlevel.com/support/solutions/articles/155000005412-listing-conversation-ai-and-voice-ai-templates-on-the-marketplace)  
**Category:** Developer Resources  
**Folder:** Developer Resources

---

1. **Generate a Marketplace Link**  
  


     * On HighLevel, in the **Conversation AI** or **Voice AI** page, select the agent and click **Sell this Template/Agent on Marketplace** (This option is **visible only to Agency Owners and Admins**. Sub-account admins and users cannot view this option). Define exactly what ships with your agent so buyers know what installs automatically and what they’ll configure later.  
  


       * **Knowledge Base (optional):** Choose to **Include** or **Exclude** the agent’s Knowledge Base during publishing.  
  


       * If **Included** , the Knowledge Base is **bundled** and installs automatically with the agent for the buyer.  
  


     * The template will not only include the prompts, but also the actions such as triggering a workflow, creating an appointment, along with the underlying assets - workflows, calendar, custom field/value, etc. So you're selling the whole package.  
  


       * Please ensure that the assets you're packaging are not imported as part of an IP protected snapshot. Restricted/IP protected assets cannot be included in the AI agents.  
  


     * You’ll be redirected to the Developer Portal with a special link that carries your bot’s package.  
  


     * If you wish to update your existing template listed on the marketplace, you can make the necessary changes in the Conversation AI or Voice AI page, click on **Copy Link for Marketplace** from the menu, and update the link in the **[Developer portal](<https://marketplace.gohighlevel.com/apps>)** (refer to #2 below)  
  


  2. **Complete Your App Details**  
  


     * In the [**Developer Portal**](<https://marketplace.gohighlevel.com/apps>) under **Modules → ConversationAI or Voice AI** , paste your link and click **Submit** to fetch.  
  


     * **Editable fields** : Use-cases (e.g. lead qualification, appointment booking), Agent Description and available actions (workflows, appointments, SMS blasts, call transfers)  
  


     * You can also configure the list of **suggested questions** that buyers can ask the agent while they are testing your agent on the Marketplace before purchasing your agent.  
  


     * **Review non-editable fields** : supported channels (SMS, email, Instagram, calls)  
  


  3. **Finalise & Submit**  
  


     * Fill out your **app's Basic Info, App Profile** , **[Pricing](<https://help.gohighlevel.com/support/solutions/articles/155000001217-set-up-your-app-pricing>)** , and **Support** sections.  
  


     * Submit your listing for review—once approved, it goes live in the Marketplace for all agency users and sub-accounts.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048513172/original/VgMMbsAj4VTfo5m_lo-P4jadH08_7heP3A.png?1750309262)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063751576/original/vL0-fSzhDqj8fJxat8-feeF30OyZR-auiA.png?1769681448)

* * *

## **AI Agent Templates Now Follow App Versioning**

  


Conversation AI and Voice AI templates now follow the Marketplace app-versioning workflow. This means AI Agent template changes are tied to app versions and are no longer edited directly on a Live app version.

  


This creates a clearer release history for AI Agent module updates and helps developers ship template changes more intentionally.

  


**Update AI Agent Templates Through a Draft Version**

  


AI Agent templates on a Live app version are no longer directly editable. To make changes:

  


1\. Go to **Manage** > **Versions**.  
  


2\. Clone the **Live** version as a **Draft**.  
  


3\. Make your Conversation AI or Voice AI template changes in the Draft version.  
  


4\. Publish the Draft using the appropriate version bump.

  


This ensures template updates are released through the same controlled app-versioning flow as other Marketplace app changes.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074065071/original/nfF4YuIO2hBET562IpkXciYFFv5-5Zhw8A.png?1781871451)

* * *

## **Major vs Minor Version Updates for AI Agent Templates**

  


Changes to an existing AI Agent template are treated as a **Minor** update by default. This includes updates such as:

  


  * Agent name  
  

  * Agent description  
  

  * Use case  
  

  * Supported channels  
  

  * Actions  
  

  * Template configuration  
  

  * Template link changes  
  

  * Disabling or re-enabling an existing template link


  


A **Major** version is required when a Conversation AI template or Voice AI template is added for the first time to an existing Live app.

  


For example, if a Live app does not currently include a Conversation AI or Voice AI template and a developer adds one in a Draft version, that update should be published as a Major version because it introduces new module capabilities.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074065310/original/-j2GvPQ5XDgfJXeE1DXXCN0_NSK39jlRUQ.jpeg?1781871630)

* * *

## **Frequently Asked Questions**

  


**Q: What assets are included in a template?  
****A:** Templates may include **workflows, calendars, custom fields, custom values, and an optional Knowledge Base** (if the Agent Builder selects **Include** during publish).  
  


**Q: Can I exclude the Knowledge Base when listing my agent?  
****A:** Yes. On the **Publish** screen, set **Knowledge Base** to **Exclude** to publish without a bundled KB.

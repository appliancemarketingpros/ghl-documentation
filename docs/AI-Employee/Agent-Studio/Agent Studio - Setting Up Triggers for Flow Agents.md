# Agent Studio - Setting Up Triggers for Flow Agents

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007310-agent-studio-setting-up-triggers-for-flow-agents](https://help.gohighlevel.com/support/solutions/articles/155000007310-agent-studio-setting-up-triggers-for-flow-agents)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

Use Agent Studio Triggers to start an AI agent automatically when a contact action or system event happens in HighLevel. Real-time starts help you respond faster, reduce manual work, and launch the right automation at the moment a trigger occurs. This article explains how to configure real-time Start triggers for existing Flow Agents in HighLevel.

  

    
    
    **Important:** Agent Studio now includes **Super Agents** and **Flow Agents**. New agent creation should be done using **Super Agents**. Existing **Flow Agents** continue to run normally and can still be opened, edited, and managed from the **Flow Agents** page.

  


* * *

# **What are Triggers for Flow Agents?**

  


Flow Agent Triggers are event listeners attached to an agent’s Start node that automatically launch the agent when a supported platform event occurs. By reacting to real user actions like submitting a form or sending a chat, agents can engage contacts immediately without external API calls or manual steps.

  


Flow Agent Triggers provide three entry events today: **Form submitted** , **Lead tag** (added or removed), and **Chat message**. When one of these events fires, the agent starts from its **Start trigger** and continues through your designed flow.

* * *

## **Key Benefits of Flow Agent Triggers**

  


  * **Real‑time engagement** : Respond to leads the moment they act—submit a form, message your business, or get tagged.


  


  * **Hands‑free scalability** : Remove polling scripts and custom web-hooks and configure an in‑product trigger and publish.


  


  * **Consistent entry point** : Standardize how agents start so testing and troubleshooting are easier.


  


  * **Non‑breaking adoption** : Triggers are optional and additive; existing API‑based agents continue to work.


  


  * **Foundation for growth** : Event‑driven design sets the stage for additional event types over time.


* * *

## **How to Set Up Flow Agent Triggers**

  


Follow these steps to create a reliable, testable, and production‑ready trigger configuration from start to finish.

  

    
    
    **Prerequisites & Access: **
    
    Confirm access and environment so your trigger setup goes smoothly and matches your deployment process.
    
    Access **AI Agents → Agent Studio** inside the correct sub‑account/location.
    
    See **[](<https://help.gohighlevel.com/a/solutions/articles/155000006058?portalId=48000045315>)[How to Setup Flow Agents in Agent Studio](<https://help.gohighlevel.com/en/support/solutions/articles/155000007393>)** for canvas navigation, testing, and publish lifecycle.
    

  


  1. From the left sidebar, click **AI Agents** , then select the **Agent Studio** tab at the top.  
  

  2. Click on the **Flow Agents** button.  
  
![](https://jumpshare.com/share/GHcBJsQLzhbMZnJ8U7Nd+/Screen+Shot+2026-07-08+at+18.27.14.png)  
  

  3. **Click** an **existing** **agent's** **name** to edit it.  
  

  4. Inside the agent, you’ll see the builder canvas with nodes and a plus control. Use **Add New Node** to begin building or locate the starting area of your existing flow.  
  

  5. From the node picker, choose **Start trigger** under **Flow Control**. This places a trigger tile that listens for events to start your agent.  
  

  6. In the **Select trigger** panel, pick **Form submitted** , **Lead tag** , **Chat message** or **Workflows** to define what starts the agent. Your choice determines which configuration options appear next.  
  

     1. **Form Submitted Trigger:** Use this when you want an agent to engage immediately after a contact completes a HighLevel‑tracked form, ideal for instant nurture, qualification, or routing. It:  
  

        * Starts the agent when any selected form is submitted.
        * Exposes submitted form fields as variables your agent can reference in later steps.  
  

     2. **Lead Tag Trigger (Added / Removed):** Fire targeted automations when a tag is applied to or removed from a contact. Common uses include VIP onboarding, re‑engagement, or churn‑prevention.  
  

        * Starts the agent when a selected tag is **added** or **removed** from a contact.
        * Provides the contact context (including existing tags and custom fields) to your flow.  
  

     3. **Chat Message Trigger:** Start your agent the instant a new inbound message arrives through supported chat widgets/providers, this trigger is ideal for instant replies, smart routing, or FAQ deflection.  
  

        * Requires no additional configuration, add the trigger and publish.
        * Provides message text, sender details, and conversation context for your flow logic.  
  

     4. **Workflows Trigger:** Checkout this article for better understanding - [Workflow Action - Invoke Agent Studio Agent](<https://help.gohighlevel.com/en/support/solutions/articles/155000007402>)  
  
![](https://jumpshare.com/share/VOcHRyGZDNtg9Rs7gUEg+/GIF+Recording+2026-07-08+at+18.48.55.gif)  
**  
**
  7. **Setup the Triggers:  
**  
**Select Forms**  
  
For **Form submitted** trigger, use the dropdown to choose one or more forms, or click **Add new** if the form isn’t created yet. The agent will start whenever any selected form is submitted.  
  
**Choose Tag Action**  
  
For **Lead tag** , set **Tag action** to **Tag added** or **Tag removed**. This decides whether the agent starts when a tag is applied to a contact or when it’s removed.  
  
**Select** the **specific** **tag****** from the list, or create one with **Add new**. The agent listens only for changes to the tags you select here.  
  
When bulk‑adding tags for testing, consider using a small test segment first to avoid triggering many agent runs at once.  
  
**Enable Chat Trigger**  
  
For **Chat message** , no additional configuration is required. The agent will start automatically whenever a new inbound message arrives through connected chat channels.  
  
![](https://jumpshare.com/share/uDIC7Gt97CHnFzAx8Odr+/GIF+Recording+2026-07-08+at+19.25.55.gif)  
  

  8. **Validate & Go Live**


  


  * **Test:** Run a safe simulation of the selected trigger to see exactly which variables and payload the agent receives, no live contacts are affected. Use this to iterate quickly on prompts/nodes and verify the flow before publishing.


  


  * **Save:** Store your current changes as a Staging version so you don’t lose work and can return later; nothing goes live yet. Saving is ideal after each configuration step (e.g., choosing forms or tags) to keep a clean working version.


  


  * **Publish:** Push the current agent and its Start trigger live for this sub-account so real events immediately start the agent. Publish after successful Tests, ensuring the Start trigger is connected to the first node; if the agent is mapped to other features (e.g., Ask AI), it typically must be in Production to be selectable.  
  
![](https://jumpshare.com/share/wId879x6RlnN0bG3qxtc+/Screen+Shot+2026-07-08+at+19.29.51.png)


* * *

## **Frequently Asked Questions**

  


**Q: Can I create a new Flow Agent for real-time Start triggers?**  
No. New agent creation should now be done using Super Agents. Existing Flow Agents can still be opened, edited, and managed from the Flow Agents page.

  


**Q: Will my existing Flow Agent triggers continue to work?**  
Yes. Existing Flow Agents and their configured triggers continue to run normally.

  


**Q: Do triggers change how my existing API‑invoked agents run?**

No. Triggers are additive. Your existing API flows continue to work; triggers only run for agents where you’ve added a Start trigger.

  


**Q: Can I test before going live?**

Yes. Use the canvas **Test** option to simulate the event and validate variables and responses before publishing.

  


**Q: Which chat sources are supported?**

Triggers work with HighLevel’s existing chat widgets/providers connected to your sub‑account. No extra configuration is required to start.

  


**Q: What data is available to my agent when a trigger fires?**

Form submissions include mapped form fields; Lead tag events include contact context; Chat message events include message text and conversation metadata.

  


**Q: What if I don’t see my form or tag in the dropdown?**

Confirm you’re in the correct sub‑account/location and that the asset exists there. Refresh the builder after creating new forms/tags.

* * *

### **Related Articles**

  


  * [How to Setup Flow Agents in Agent Studio](<https://help.gohighlevel.com/en/support/solutions/articles/155000007393>)  
  

  * [Ask AI + Agent Studio Integration ](<https://help.gohighlevel.com/en/support/solutions/articles/155000006677>)  
  

  * [Agent Studio - Router Tool (AI & Conditional Router)](<https://help.gohighlevel.com/en/support/solutions/articles/155000007404>)  
  

  * [Workflow Action - Invoke Agent Studio Agent](<https://help.gohighlevel.com/en/support/solutions/articles/155000007402>)

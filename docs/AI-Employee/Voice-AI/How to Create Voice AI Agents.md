# How to Create Voice AI Agents

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004107-how-to-create-voice-ai-agents](https://help.gohighlevel.com/support/solutions/articles/155000004107-how-to-create-voice-ai-agents)  
**Category:** AI Employee  
**Folder:** Voice AI

---

Voice AI Agents can answer calls, respond to common questions, collect caller information, and complete actions such as booking appointments or transferring calls. HighLevel provides prebuilt Marketplace agents, a Custom Agent builder, and a visual Flow Based Builder. Follow this guide to create, test, and deploy an agent for live calls.

* * *

**TABLE OF CONTENTS**

  * What Is a Voice AI Agent?
  * Key Benefits of Voice AI Agents
  * Before You Begin
  * Choose a Voice AI Agent Creation Method
  * How To Create and Configure a Voice AI Agent
  * How To Test a Voice AI Agent
  * How To Deploy a Voice AI Agent
  * Final Voice AI Launch Checklist
  * Frequently Asked Questions
  * Related Articles


* * *

# **What Is a Voice AI Agent?**  
  


A Voice AI Agent is an automated voice assistant that communicates with callers using the instructions, business information, and actions you configure. It can answer questions, collect information, update contact records, book appointments, trigger automations, and route callers when human assistance is needed.

* * *

## **Key Benefits of Voice AI Agents**  
  


Voice AI Agents help businesses handle routine calls consistently while allowing team members to focus on conversations that require personal attention.  
  


  * **Immediate call handling:** Respond to callers without requiring a team member to answer every call.  
  

  * **Consistent conversations:** Follow the same approved instructions and escalation rules.  
  

  * **Automated actions:** Book appointments, send messages, update contacts, or trigger workflows.  
  

  * **Business knowledge access:** Answer questions using a connected Knowledge Base.  
  

  * **Flexible routing:** Transfer callers to a person or another Voice AI Agent when needed.  
  

  * **Scalable coverage:** Support more calls without creating a separate manual process for every caller.


##   


* * *

## **Before You Begin**  
  


Preparing the agent's purpose, supporting information, and required account resources before opening the builder makes setup faster and testing more reliable.  
  


Confirm that you have:  
  


  * Access to the correct HighLevel sub-account.  
  

  * The **View & Manage Voice AI Agents** permission.  
  

  * A defined use case, such as lead qualification, customer support, appointment booking, or call routing.  
  

  * Approved business information for the prompt or Knowledge Base.  
  

  * Any calendar, workflow, transfer number, or integration required by your planned actions.  
  

  * An eligible LC Phone number, Twilio number, or Number Pool when the agent will handle live calls.  
  


**Permissions:** If Voice AI is missing, ask a sub-account administrator to review your user permissions. Agent management, goal configuration, and dashboard access may be controlled separately.

**Outbound calling:** Outbound Voice AI requires the applicable approval and compliance setup. The Outbound testing option may remain unavailable until those requirements are completed.

* * *

## **Choose a Voice AI Agent Creation Method**  
  


HighLevel provides three starting points so you can balance setup speed with the level of control required for the conversation.  
  


  * **Browse Marketplace:** Install a prebuilt agent designed for a specific use case. Review all included prompts, actions, workflows, calendars, fields, and Knowledge Base content before deployment.  
  

  * **Create Custom Agent:** Configure an agent through the full-screen builder using a prompt, Knowledge Base, actions, and call settings.  
  

  * **Flow Based Builder:** Design a visual, node-based flow for structured or multi-step conversations.


* * *

## **How To Create and Configure a Voice AI Agent**  
  


A complete setup begins with the agent's purpose and conversation instructions, then adds only the knowledge, actions, and settings required for that use case.  
  


### **Step 1:__**_Open Voice AI_  
  


The Voice AI Agent List provides access to existing agents, call logs, and the agent-creation workflow.  
  


  1. Log in to the appropriate sub-account.  
  

  2. Go to **AI Agents → Voice AI**.  
  

  3. Open the **Agent List** tab.  
  


![Voice AI selected under AI Agents with the Agent List displayed.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074837601/original/hsT98POgEm7Jh58oQRuGyuZ4aJ5Q3KlJvQ.png?1782821661=)  
  


### **Step 2:**_Start a New Agent_  
  


Creating a separate agent for each primary call-handling use case makes prompts, actions, routing, and reporting easier to manage.  
  


  1. Click **\+ Create Agent**.


![Voice AI Agent List with the Create Agent button highlighted.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074837671/original/Lk4nHQrVy9H4uOjxWGCtR8A9fsouhbojZQ.png?1782821701=)  
  


  2. Select **Browse Marketplace** , **Create Custom Agent** , or **Flow Based Builder**.  
  

  3. Click **Continue**.


![Create Voice AI Agent window showing Marketplace, Custom Agent, and Flow Based Builder.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074837719/original/larfbyqSnOdZioKh3imuhe6KCczqP5mLcg.png?1782821744=)

  
The remaining steps focus on **Create Custom Agent**. Marketplace agents should be reviewed and customized after installation. Flow Based Builder agents are configured through connected nodes.

###   
**Optional: Start With Flow Based Builder**  
  


Flow Based Builder is useful when the conversation requires defined paths, routing conditions, or multiple AI steps. A new blank flow begins with a Start Call node connected to an AI Agent node.

![Flow Based Builder showing Start Call connected to an AI Agent node.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078115672/original/an3JyyuhBYx9B1XTWkFZvaqvHWcGXZ09Ig.png?1786445202=)

**Important:** The starter flow is not retained until you save the agent.

###   
**Step 3:**_Configure the Core Agent_  
  


The full-screen builder keeps the prompt, settings, and test console together so you can configure and test the agent without leaving the page.  
  


  1. Enter a clear **Agent Name**.  
  

  2. Select the agent's **Voice**.  
  

  3. Select the appropriate **Model** and **Language**.  
  

  4. Write or review the agent prompt.  
  

  5. Configure the **Welcome Message** for inbound and outbound calls.  
  

  6. Choose whether the agent or caller speaks first, when available.  
  

  7. Set the pause before the agent begins speaking.  
  

  8. Click **Save**.


![Full-screen Voice AI builder showing the prompt editor, configuration sections, and Test Audio panel.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074838562/original/8ZalWN_lgrjgUgVq0Nwx3dXETndOYV_NUg.gif?1782822183=)

  
A reliable prompt should define:  
  


  * The agent's role and primary objective  
  

  * The information it should collect  
  

  * The topics it may answer  
  

  * The claims or topics it must avoid  
  

  * When each action should run  
  

  * When the caller should be transferred or escalated  
  

  * How the conversation should end


**Tip:** Prompt Optimizer can help improve an initial prompt, but you should review and test the final instructions. Tell the agent not to guess when required information is unavailable.

###   
**Step 4:**_Connect a Knowledge Base_  
  


A Knowledge Base helps the agent answer business-specific questions using approved information instead of relying only on the prompt.  
  


  1. Open **Knowledge Base** in the configuration panel.  
  

  2. Select the Knowledge Base the agent should use.  
  

  3. Add or update the relevant sources.  
  

  4. Describe when the agent should search the Knowledge Base.  
  

  5. Test common questions and edge cases.  
  


Useful sources may include business hours, services, pricing, policies, locations, and frequently asked questions.

###   


### **Step 5:**_Add Voice AI Actions_  
  


Actions allow the agent to complete tasks during the conversation or after the call ends. Add only the actions required for the agent's objective.  
  


  1. Open **Actions**.  
  

  2. Click **\+ New Action**.  
  

  3. Select the action type.  
  

  4. Enter a clear action name.  
  

  5. Define the condition that should trigger the action.  
  

  6. Complete the required destination, workflow, field, calendar, or integration settings.  
  

  7. Save the action.


![Voice AI Actions menu showing available action types.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074838877/original/1NNC169G50aavt22xDHtYMTtKqN4bmtmuA.png?1782822386=)  
  


Common actions include:  
  


  * **Call Transfer:** Send the caller to a human phone number.  
  

  * **Trigger a Workflow:** Start a selected HighLevel workflow.  
  

  * **Send SMS:** Send a message during the conversation.  
  

  * **Update Contact Field:** Save information collected from the caller.  
  

  * **Appointment Booking:** Offer availability and schedule an appointment.  
  

  * **Custom Action:** Send a real-time webhook request to an external system.  
  

  * **Agent Transfer:** Hand the conversation to another Voice AI Agent when available.  
  


After-call actions can apply updates or trigger follow-up processes after the conversation without interrupting the caller.

![Call Transfer action configuration showing transfer conditions and the message used before the transfer.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074840100/original/_3J9-fBFUNs14AliWjU9aMct55U2XMf6pQ.png?1782822995=)

**Call Transfer versus Agent Transfer:** Call Transfer sends the caller to a person or external number. Agent Transfer hands the conversation to another Voice AI Agent.

###   
**Step 6:** _Review Call and Post-Call Settings_  
  


These settings control how the agent speaks, responds to silence, handles interruptions, and processes information after the call.  
  


Review the areas that apply to your use case:  
  


  * **Call Settings:** Call duration, idle reminders, and silence handling  
  

  * **Agent Behavior:** Response speed, interruption sensitivity, and response style  
  

  * **Transcription & Speech:** Speech recognition, pronunciation, and keywords  
  

  * **Translation:** Translated transcripts or summaries  
  

  * **Voice Settings:** Voice speed, volume, and supported audio options  
  

  * **Post-Call:** Notifications, workflows, summaries, and follow-up behavior  
  


Keep the default settings when they already match the intended experience. Change one setting at a time and retest so you can identify which adjustment affected the call.

* * *

  


## **How To Test a Voice AI Agent**  
  


Testing before deployment helps identify prompt gaps, inaccurate answers, action failures, and unnatural call behavior before customers reach the agent.  
  


  1. Save the current agent configuration.  
  

  2. Open the **Test** or **Test Audio** panel.  
  

  3. Choose a test method:  
  

     * **Web Call:** Test the conversation in your browser without assigning a phone number.  
  

     * **Phone Call:** Test the complete telephony experience through an actual phone connection.  
  

  4. Select the available inbound or outbound scenario.  
  

  5. Start the call and interact with the agent as a real caller would.  
  

  6. Adjust the prompt, Knowledge Base, actions, or settings.  
  

  7. Repeat the test until the expected behavior is consistent.  
  

  8. Review the call history, transcript, recording, summary, and action results.  
  


**Testing limitation:** Call Transfer does not run during a Web Call test. Use Phone Call testing or call the deployed number to validate a transfer.

Test the agent with:  
  


  * A common caller request  
  

  * A question answered by the Knowledge Base  
  

  * A question the agent should not answer  
  

  * An incomplete or unclear request  
  

  * Each configured action  
  

  * A transfer or escalation request  
  

  * A period of silence  
  

  * An interruption while the agent is speaking  
  

  * The intended call-closing sequence


* * *

  


## **How To Deploy a Voice AI Agent**

  


Deployment connects the completed agent to live Phone and Chat channels and controls how the agent handles incoming interactions.

  


  1. Open the agent's **Deploy** tab.  
  


  2. In the **Phone** section, select an eligible phone number or configured Number Pool.

     * Available phone numbers appear directly on the Deploy screen.

     * To add a new number, purchase it without leaving the Deploy screen.

     * After purchasing a number, choose whether to assign it to the agent.  
  


  3. Under **Call Routing** , select how the agent handles incoming calls:

     * **Answer Calls Directly:** The Voice AI Agent answers incoming calls directly.

     * **Use as Backup:** The Voice AI Agent acts as a backup when the primary call path does not answer.  
  


  4. Under **Working Hours** , choose the agent's availability:

     * Select **All Hours** for unrestricted availability.

     * Select **Custom Schedule** to choose active days and time ranges.

     * Custom schedules can extend through midnight.  
  


  5. In the **Chat** section, configure a Chat Widget when the agent will also handle website conversations.

     * Connect an existing Chat Widget.

     * Create and automatically connect a new Chat Widget.

     * Disconnect a linked Chat Widget when needed.

     * Click a linked widget to open its editor in a new browser tab.  
  


  6. Review the inbound call flow, forwarding, timeout, voicemail, and fallback behavior associated with the assigned number.  
  


  7. Save the deployment settings.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079236730/original/8VllPp0XX1GQ-5tONHcmDlD49uVV2_rOVw.png?1787650211)


  


**Routing matters:** Assigning a number does not guarantee that the agent will answer every call. Working Hours, Call Routing mode, forwarding, timeout, voicemail, and the phone number's call-flow configuration can affect routing.

* * *

## **Final Voice AI Launch Checklist**  
  


A final live-call review confirms that the agent's conversation behavior, actions, availability, and phone routing work together as intended.  
  


  * ☐ The agent name, voice, model, and language are correct.
  * ☐ The inbound and outbound greetings sound natural.
  * ☐ The prompt clearly defines the agent's role, limits, and objective.
  * ☐ Knowledge Base answers are accurate and relevant.
  * ☐ The agent does not invent answers when information is unavailable.
  * ☐ Each action runs only under its intended conditions.
  * ☐ Phone Call testing confirms that transfers reach the correct destination.
  * ☐ The correct phone number or Number Pool is assigned.
  * ☐ Working hours and after-hours behavior are correct.
  * ☐ The inbound call flow routes callers to the agent as intended.
  * ☐ A live external call reaches the deployed agent.
  * ☐ The call log contains the expected transcript, summary, and action results.


* * *

## **Frequently Asked Questions**  
  


**Q: Why can't I see Voice AI under AI Agents?**  
Your role may not include **View & Manage Voice AI Agents**. Ask a sub-account administrator to review your permissions.  
  


**Q: Which creation method should I choose?**  
Use **Create Custom Agent** for standard call-handling use cases. Use **Browse Marketplace** when a suitable prebuilt agent is available. Use **Flow Based Builder** for structured, multi-path conversations.  
  


**Q: Can I test an agent without assigning a phone number?**  
Yes. Use **Web Call** to test prompts, Knowledge Base responses, and most actions directly in your browser.  
  


**Q: Why did Call Transfer not work during my Web Call test?**  
Call Transfer is not supported during Web Call testing. Use a Phone Call test or call the deployed number.  
  


**Q: Why does the agent not answer the assigned number?**

Confirm that the phone number or Number Pool is assigned to the correct agent. Then review Working Hours, the selected Call Routing mode, inbound routing, forwarding, timeout, voicemail, and the phone number's call-flow configuration.

  
  


**Q: Can one Voice AI Agent handle calls from multiple numbers?**  
Yes. Assign a configured Number Pool when multiple numbers should route to the same agent.  
  


**Q: Can a Marketplace agent include a Knowledge Base?**  
Yes. Marketplace agents may include a Knowledge Base and other supporting assets. Review and replace any business-specific information before deployment.  
  


**Q: Can Voice AI book appointments during a call?**  
Yes. Add the Appointment Booking action and connect an appropriate HighLevel calendar. Test availability selection and booking confirmation before deployment.

* * *

### **Related Articles**

  * [](<https://help.gohighlevel.com/support/solutions/articles/155000003911-overview-of-voice-ai-agents>)[Overview of Voice AI Agents](<https://help.gohighlevel.com/en/support/solutions/articles/155000003911>)  
  

  * [](<https://help.gohighlevel.com/support/solutions/articles/155000004108-how-to-test-voice-ai-agents>)[How to Test Voice AI Agents](<https://help.gohighlevel.com/en/support/solutions/articles/155000004108>)  
  

  * [](<https://help.gohighlevel.com/support/solutions/articles/155000005680-managing-granular-permissions-for-voice-ai-agents>)[Managing Granular Permissions for Voice AI Agents](<https://help.gohighlevel.com/en/support/solutions/articles/155000005680>)

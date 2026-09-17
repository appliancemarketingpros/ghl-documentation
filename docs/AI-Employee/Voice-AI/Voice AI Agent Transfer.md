# Voice AI: Agent Transfer

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007796-voice-ai-agent-transfer](https://help.gohighlevel.com/support/solutions/articles/155000007796-voice-ai-agent-transfer)  
**Category:** AI Employee  
**Folder:** Voice AI

---

Agent Transfer lets one Voice AI Agent hand off an active conversation to another Voice AI Agent during the same live call. Use this feature to route callers to specialized agents based on intent, such as sales, support, billing, booking, or language-specific needs. This keeps each agent focused while helping callers continue the conversation without starting over.

* * *

**TABLE OF CONTENTS**

  * What is Voice AI: Agent Transfer?
  * Key Benefits of Agent Transfer
  * Agent Transfer vs Call Transfer
  * Transfer Conditions and Handoff Messages
  * Audit Agent Transfers in Call Logs
    * Call Summaries
    * Transcripts and Transfer Markers
  * How To Set Up Voice AI: Agent Transfer
      * Step 1: Open the root Voice AI agent
      * Step 2: Add the Agent Transfer action
      * Step 3: Connect the destination agent
      * Step 4: Add the transfer condition
      * Step 5: Configure the optional handoff message
      * Step 6: Review incoming transfers
      * Step 7: Review root agent settings
      * Step 8: Save and test the transfer
  * Frequently Asked Questions 
  * Related Articles


* * *

## **What is Voice AI: Agent Transfer?**

  


Agent Transfer is a Voice AI action that lets one Voice AI agent hand off a live call to another Voice AI agent without leaving the original call. Instead of dialing a new number or starting a new conversation, the caller remains in one continuous live call while the agent changes behind the scenes.

  


Agent Transfer uses a root-and-destination model. The **root agent** is the agent the call starts with, and **destination agents** are the agents that can receive the transferred conversation.

  


During the call, the root Voice AI agent listens for the transfer conditions you define. For example, when a caller asks about pricing, the root agent can transfer the conversation to a pricing-focused destination agent. The destination agent then continues the conversation based on its own configuration, prompt, and purpose.

  


Agent Transfer is different from Call Transfer because it hands the call to another Voice AI agent instead of sending it to a person.

  


Key terms to know:

  


  * **Root agent:** The Voice AI Agent that starts the call and evaluates whether the caller should be transferred.  
  

  * **Destination agent:** The Voice AI Agent that receives the transferred conversation and continues the interaction.  
  

  * **Transfer condition:** The caller intent or situation that tells the root agent when to transfer.  
  

  * **Handoff message:** An optional spoken message used to explain the transfer to the caller.


* * *

## **Key Benefits of Agent Transfer**

  


Agent Transfer helps teams design cleaner, more specialized Voice AI call flows. Instead of building one large prompt to handle every possible caller need, teams can route callers between focused agents that are each configured for a specific purpose.

  


  * **Seamless caller experience:** The caller stays in the same live call while the conversation moves to another Voice AI agent.  
  

  * **Sharper, more accurate responses:** A focused agent is less likely to drift or mix up instructions from unrelated flows.  
  

  * **Lower token usage:** Each specialist carries only its own context, which can reduce the cost compared to using one large agent.  
  

  * **Reuse specialists across agents:** The same "pricing expert" agent can be the handoff destination for any number of parent agents.  
  

  * **Unified post-call experience:** Data extraction, workflows, and notifications from every agent involved in the call are merged automatically so downstream automations can use the combined post-call output.


* * *

## **Agent Transfer vs Call Transfer**

  


These are easy to mix up as both features move a live conversation forward but they are designed for different outcomes. 

  


**Call Transfer** transfers the call to a human using a phone number. **Agent Transfer** hands the call off to another Voice AI agent with no phone number involved.

  


Transfer Type| Destination| Requires Phone Number| Best Used When  
---|---|---|---  
Agent Transfer| Another Voice AI Agent| No| A different AI agent should continue the conversation  
Call Transfer| Human Representative| Yes| A person needs to speak with the caller  
  
  


  


Use **Agent Transfer** when:  
  


  * A caller asks about pricing and should speak with a pricing-focused AI agent.  
  


  * A caller wants to schedule an appointment and should move to a booking-focused AI agent.  
  


  * A caller has a support question and should move to a support-focused AI agent.  
  


  * A caller requests another language and should move to a language-specific AI agent.


  


  


Use **Call Transfer** when:  
  


  * A caller needs a live team member.  
  


  * A high-value lead should speak with a sales representative.  
  


  * A sensitive issue requires human judgment.


* * *

## **Transfer Conditions and Handoff Messages**

  


Transfer conditions tell the root agent when to move the caller to a destination agent. When configuring a destination agent, enter a natural-language condition in the **When to transfer to this agent** field. The condition should describe the caller intent that should trigger the handoff.

  


Each Agent Transfer configuration can include **up to three destination Voice AI agents**. Each destination agent needs its own transfer condition so the root agent knows when to send the caller there.

  


**Examples:**

  


  * “When the caller asks about pricing.”  
  


  * “When the caller wants to schedule an appointment.”  
  


  * “When the caller needs help in Spanish.”  
  


  * “When the caller asks for technical support.”


  

    
    
    **Important:** Avoid transfer loops. Agents should not transfer to each other in a circular pattern, as this can cause the call to fail.

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070328054/original/oWfcv-4zgVOe4xHt_A2QN4gvS0YyCcJpkA.png?1777558835)

  


  


You can also enable **Speak During Execution** to have the agent say a short handoff message. This can make the transition clearer for the caller, especially when the conversation is moving to a different department, topic, or language.

  


**Example handoff messages:**

  


  * “Let me connect you to our pricing specialist.”  
  


  * “I’ll transfer you to an agent who can help with scheduling.”  
  


  * “One moment while I connect you with the right specialist.”


  


If you leave **Speak During Execution** turned off for a destination, the transfer happens invisibly. The caller simply experiences a natural pause and continuation of the conversation, now powered by a different agent.

  

    
    
    **Note:** Only the root agent greeting plays when the call starts. Destination agents do not play their standard greeting when they receive a transferred call.

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070328143/original/p9E4fSPH0iz1OMWa-AQ29NhIKZDBJDg6bQ.png?1777558876)

* * *

## **Audit Agent Transfers in Call Logs**

  


After a call ends, you can use Call Logs to confirm whether an Agent Transfer took place and review how the conversation moved between agents. Call summaries, transcripts, data extraction, recap emails and workflow triggers include activity from all of the agents that participated in the call.

  


To view the call logs, go to **AI Agents > Voice AI**, then review the call log table for the completed call.

  


If Agent Transfer occurred, the **Actions Triggered** column displays **Agent Transfer**. If multiple transfers occurred during the same call, the column can show the transfer count, such as **Agent Transfer (2)**.

**  
**
    
    
    **Note:** Post-call workflows can be triggered for the root agent and any agent involved in the transfer chain.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070339178/original/yGNIgJYi8OHmIZDBRf4cZxjiBCLjHcFL3Q.png?1777564483)

  


  


### **Call Summaries**

  


From the call log table, click **Summary** on the call row to open the call summary.

  


The summary shows the call flow the agent followed during the conversation. When Agent Transfer occurs, the summary can show the transfer chain so you can see which Voice AI agents participated and how the caller moved through the flow.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070339373/original/JEFBZD4Kukjxaot-bxgan4conkAw7U2S1Q.jpeg?1777564649)

  


  


Use the call summary and call-flow view to review:  
  


  * Which agent started the call.  
  


  * Which destination agent received the transfer.  
  


  * The sequence of agents involved in the conversation.  
  


  * Whether the caller moved through the intended transfer path.  
  


You can hover over an agent in the call-flow diagram to review its details. If you need to inspect the agent configuration, click the agent from the diagram to open the agent details in a new tab.

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070338304/original/4sXSO0vWA9rJiq20cYAUjJIJctCNT1ivNA.png?1777563914)**

  


  


### **Transcripts and Transfer Markers**

  


From the call log table, click the transcript icon on the call row to open the **T****ranscript**.

  


The transcript shows how the transfer happened during the conversation. When Agent Transfer occurs, the transcript clearly marks the transfer point and updates the active agent name so you can see which agent handled each part of the call. This means that the transcript reflects the entire conversation, including every agent that handled part of the call.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070339859/original/mRm5SV9JFMnrWDyd0CJsShSv2TWGFqy5rw.png?1777564823)

  


  


Use the transcript to review:  
  


  * The caller’s exact wording before the transfer.  
  


  * Whether the transfer condition matched the caller’s intent.  
  


  * Where the transfer occurred in the conversation.  
  


  * Which agent was active before and after the transfer.  
  


  * How the destination agent continued the conversation.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070339948/original/ploJGspV9g-6wLsp5C9yxJ56qpuJS44gzg.png?1777564856)

* * *

## **How To Set Up Voice AI: Agent Transfer**

  


####  _**Step 1:** Open the root Voice AI agent_

  


Navigate to **AI Agents** > **Voice AI** > **Agent List** and select the Voice AI agent that should begin the call. This is the root agent.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070333232/original/vf83-6QUWLGKo2XKS1z9Xo7gA24i3AGeNw.png?1777561611)

  


  


#### _**Step 2:** Add the Agent Transfer action_

  


Click **\+ New****Action** and select **Agent Transfer** from the dropdown.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070333567/original/fGbP1JbI52mRhTT1mhYgztxmKCnRXJN5Rw.png?1777561763)

  


  


#### _**Step 3:** Connect the destination agent_

  


In the Agent Transfer modal, click **Connect Agent**. Select the destination Voice AI agent that should receive the transferred call.

  


Repeat this process for additional destination agents, up to the supported limit of three destination agents.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070333767/original/-GmWvr2n7Jiu1SPEI_gTAq5_hgP-oqltMA.png?1777561868)

  


  


#### _**Step 4:** Add the transfer condition_

  


Enter the transfer condition in the **When to transfer to this agent** field. Use clear, natural language that describes when the root agent should transfer the caller.

  


Repeat this step for each connected destination agent.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070334132/original/SVr5IeH12AzQKUCkUjYMRbIGjPYqnXnnUg.jpeg?1777562049)  
  


#### _**Step 5:** Configure the optional handoff message_

  


Enable **Speak During Execution** if you want the agent to say a handoff message during the transfer then enter the message the caller should hear during the handoff.

  


Leave **Speak During Execution** disabled if you want the transfer to happen without a spoken transition.

  


Repeat this step for each connected destination agent.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070334191/original/QQ_Z3zQY0CrkfAJM485UkiMDr5w7EBnngQ.jpeg?1777562062)

  


  


#### _**Step 6:** Review incoming transfers_

  


Use **View Incoming Transfers** to review which agents are configured to transfer calls into the selected agent. This is helpful when multiple root agents use the same destination agent or when you are auditing a more complex transfer setup.

  


Hide this view when you want to return to the main transfer configuration.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070334750/original/uEtkaNHo_pkhd9husbpmtHiOS9I0JEHuuA.png?1777562252)  
  


#### **_Step 7:_**_Review root agent settings_

  


Review the root agent’s **Maximum Call Time** , **Working Hours** , and **AI Agent as a Backup** settings before saving.

  


These root agent settings control the transfer chain once the call is connected. Destination agent settings for call time, working hours, and backup behavior are ignored during the transfer chain.

####   


####   


#### _**Step 8:** Save and test the transfer_

  


Click **Save Changes**. Test the agent by calling or testing the Voice AI flow. Review the call log, summary, and transcript to confirm the transfer triggered as expected.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070334955/original/Fc4UVcOm95BVFgi-tihjy1ISSb2CqyYxjg.png?1777562298)

* * *

## **Frequently Asked Questions**

  


**Q: How many destination agents can I connect?**  
Each Agent Transfer configuration can include up to three destination Voice AI Agents.

  


  


**Q: Does Agent Transfer send the caller to a human?**  
No. Agent Transfer sends the caller from one Voice AI Agent to another Voice AI Agent. Use Call Transfer when the caller should be sent to a human representative or phone number.

  


  


**Q: Does the destination agent greeting play after transfer?**  
No. Destination agent greetings do not play during transferred calls. Use a handoff message if the caller needs an explanation before the transfer.

  


  


**Q: Which agent controls working hours and maximum call time?**  
The root agent controls connected-call settings such as Working Hours, Maximum Call Time, and AI Agent as a Backup.

  


  


**Q: Can a destination agent transfer the caller again?**  
A destination agent may be configured with its own transfer behavior, but transfer paths should be carefully tested to avoid loops or repeated transfers.

  


  


**Q: How do I prevent transfer loops?**  
Avoid configuring agents to transfer callers back and forth. Keep transfer conditions specific and review the full transfer chain during testing.

  


  


**Q: Will transfers appear in call logs?**  
Yes. Transfers can be reviewed in call logs, summaries, transcripts, and transfer markers when available.

  


  


**Q: Can Agent Transfer trigger post-call workflows?**  
Post-call workflows may trigger for the root agent and agents involved in the transfer chain, depending on workflow configuration.

  


  


**Q: Is Agent Transfer the same as inbound call routing?**  
No. Inbound call routing determines how the call reaches the root Voice AI Agent. Agent Transfer determines whether the active Voice AI conversation is handed to another Voice AI Agent.

  


  


**Q: Should I test Agent Transfer before going live?**  
Yes. Test each transfer condition separately and review logs, summaries, and transcripts before using Agent Transfer with live callers.

* * *

## **Related Articles**

  


  * [How to Create Voice AI Agents](<https://help.gohighlevel.com/en/support/solutions/articles/155000004107>)  
  

  * [Voice AI - Agent Logs](<https://help.gohighlevel.com/en/support/solutions/articles/155000007687>)  
  

  * [How to Edit a Voice AI Agents Voice](<https://help.gohighlevel.com/en/support/solutions/articles/155000005874>)  
  

  * [Voice AI: Translation Service for Call Transcript & Summary](<https://help.gohighlevel.com/en/support/solutions/articles/155000005797>)  
  

  * [AI Voice Agents Overview](<https://help.gohighlevel.com/en/support/solutions/articles/155000003911>)  
  

  * [Appointment Booking in Voice AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000005293>)

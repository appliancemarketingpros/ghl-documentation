# How to Create Voice AI Agents

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004107-how-to-create-voice-ai-agents](https://help.gohighlevel.com/support/solutions/articles/155000004107-how-to-create-voice-ai-agents)  
**Category:** AI Employee  
**Folder:** Voice AI

---

Creating a Voice AI Agent is fast and easy, and it will help your business field phone calls so your office staff can focus on more pressing tasks like following up with warm leads and closing deals! Follow the steps below to set up your first Voice AI Agent!

  

    
    
    **Permissions note:** Access to Voice AI is controlled by role-based permissions. If you don’t see Voice AI under **AI Agents** , your user role may not include Voice AI permissions. Ask an admin to grant Voice AI access. 

* * *

**TABLE OF CONTENTS**

  * How to Create a Voice AI Agent
  * How to Configure Voice AI Agent Details
  * Agent Details Tab
  * Settings Tab
  * How to Transfer Calls Based on Keywords or Phrases
  * Trigger Workflows
  * Email Notifications
  * Phone and Availability Tab
  * Test your Voice AI Agent during creation:
  * Make Your Inbound Voice AI Agent Reachable (Widget or URL)
  * Publish a Phone Number (Shareable “URL” via tel: links)
  * Edit and/or Delete AI Agents


* * *

# **How to Create a Voice AI Agent**

  


  1. Login to your sub-account.  
  

  2. Click on **AI Agents** tab > **Voice AI**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074837601/original/hsT98POgEm7Jh58oQRuGyuZ4aJ5Q3KlJvQ.png?1782821661)  
  

  3. Click on the **\+ Create Agent** button.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074837671/original/Lk4nHQrVy9H4uOjxWGCtR8A9fsouhbojZQ.png?1782821701)  
  

  4. You can either **Create an Agent from scratch** or choose **prebuilt** **agents** from the **Marketplace**.  
  

  5. Choose your preferred method and click **Continue**.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074837719/original/larfbyqSnOdZioKh3imuhe6KCczqP5mLcg.png?1782821744)


* * *

# **How to Configure Voice AI Agent Details**

  


When configuring your Voice AI Agent, you will need to follow a multi-step process including configuring the AI Agent, assigning actions that will happen after the phone call, and connecting the AI Agent to a phone number in your sub-account.

  


## **Agent Details Tab**

  


  1. **Agent Name:** Enter a name for your agent (e.g., “Customer Support Bot”).  
  

  2. **Business Name:** Confirm or update your business name.  
  

  3. **Voice:** Choose from a list of available voices for your AI Agent. You can preview each voice by clicking the play button.  
  

  4. **Timezone:** Select your business's timezone.  
  

  5. **LLM:** Choose your preferred LLM model.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074838226/original/etM-vLGzMkklyAhM9-PsWjooiK3SdJieeg.png?1782822007)  
  

  6. **Advanced Settings:** Configure **Call Settings** , **Agent Behavior** , **Transcription** and**Speech Settings** & **Voice Settings**.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074838124/original/C3WfFb2veJDoYpzpfvueMlLAZo80br4Owg.png?1782821969)

  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074838562/original/8ZalWN_lgrjgUgVq0Nwx3dXETndOYV_NUg.gif?1782822183)**  
**  

  7. **Greeting Message Configuration:** Customize the first message your agent says (e.g., “Hello, you’ve reached [Business Name]. How can I assist you today?”) for both Inbound and Outbound calls. Also choose **Wait Time Before Speaking**.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074838647/original/-Hvk9cQeAq00OuvdEBxnFfB5tNuoJxwCMw.png?1782822250)  
  

  8. Click **Save**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074838737/original/bpQ_Q1jhyoLLLYcUjl0zGyq9gVuELXBE0w.png?1782822305)  
  


## **Settings Tab**

  


Settings Tab simplifies the Voice AI Agent setup process by giving you few options to instruct the Voice AI Agent while in the call. No prompting required!

  


  * Choose **Knowledge Base**.  
  

  * Select the information you want the agent to collect from callers, such as: **Name** , **Email** , **Address** , **Contact's** **issue**.  
  

  * Choose if and which **Workflow you want to t****rigger post call completion**.  
  

  * If and who should receive **Email** **Notification** post call completion.


  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074839322/original/aeRp9Q7o-XAY8Ke99wZCcEDu2XAddGEzeg.png?1782822581)

###   


  * When you edit the prompt, the prompt editor includes a toolbar with quick actions:  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074839751/original/7XkDNh9bc4PMRVROndkDQGiq-5wCE5Gxlg.gif?1782822785)  
  

  * **Setup your Actions:**  
  

    * **Call Transfer:** Transfer the call to a human agent under certain conditions.  
  

    * **Trigger a Workflow:** Automatically initiate workflows based on call interactions.  
  

    * **Send SMS:** Configure the agent to send SMS messages during or after the call.  
  

    * **Update Contact Fields:** Specify how information collected should update contact records.  
  

    * Appointment Booking.  
  

    * **Custom** **Action**.  
  

    * Add **MCP** (Beta)  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074838877/original/1NNC169G50aavt22xDHtYMTtKqN4bmtmuA.png?1782822386)  
  

  * Click **Save**.


* * *

## **How to Transfer Calls Based on Keywords or Phrases**

  


Keyword-based transfers help your Voice AI Agent send callers to the right person when they mention specific words, phrases, or request types during a call. Use **Call Transfer** when the caller should be transferred to a person or phone number.

  


To set this up:

  


1\. Go to AI Agents > Voice AI.

  
2\. Create a new Voice AI Agent or edit an existing one.

  
3\. In Setup your Actions, add the Call Transfer action.

  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074839821/original/3sHir6hoYEthXbppnpgj4GNQWtTvNCGmQw.png?1782822835)

  


  
6\. Enter the phone number or destination where the call should be transferred.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074839869/original/qchTI_CsJjxGIt8iLYPNLk_XT0jI6qLZUA.png?1782822885)

  
7\. Update the agent prompt with clear instructions for when the transfer should happen.

  


**Example Prompt Instruction:**

  


If the caller asks about billing, refunds, payment issues, canceling their subscription, or speaking to a representative, transfer the call using the Call Transfer action. Before transferring, say: "I can connect you with someone who can help with that. Please hold while I transfer your call.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074840100/original/_3J9-fBFUNs14AliWjU9aMct55U2XMf6pQ.png?1782822995)

* * *

### **Trigger Workflows**

  
With Voice AI Agents, you have the option to trigger a single workflow or multiple workflows after the call ends. This keeps workflow triggering simple and allows you to control all workflow entry for Voice AI Agents based on the AI Agent that is involved in the call.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074840311/original/hHjZhyyHJBNVSwkqtFGp-usQQT_L9lPEFw.gif?1782823105)

  
  

    
    
    **Translation note (post-call outputs):** If Voice AI Translation is enabled, post-call outputs can include a translated summary and transcript. Workflows triggered after the call can consume the translated fields, and post-call notifications may display the translated artifacts. 

  


### **Email Notifications**

  
Send emails to individuals, or multiple people after a call has ended that involved that particular AI Agent.

  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074841005/original/Ismbf4zldqVMgoW21b_vNWXB9qUsRVRWHQ.png?1782823388)

  


  


**The following data is included in the email notifications:**  
  


  * **Call Summary:** Overview of the call duration, date, and time.  
  

  * **Contact Information:** Details collected during the call.  
  

  * **Call Transcript:** A written record of the conversation.  
  

  * **Actions Taken:** Any workflows triggered or contact fields updated.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035815444/original/YE-vVHh1Ypl8da9fNfHRwVpAW2WMDayhvA.jpeg?1730406227)

  


* * *

## **Phone and Availability Tab**

  


When you create a Voice AI Agent you will need to assign that AI Agent to a single phone number or multiple numbers inside your sub-account. This means that when that particular number, or group of numbers, is called, the AI Agent will step in and field the call.

  


You also have the option to configure working hours for the AI Agent, which sets specific day and time intervals that the agent should handle calls.

  


[Click here to learn more about setting up and configuring working hours for Voice AI Agents.](<https://help.gohighlevel.com/en/support/solutions/articles/155000004139-working-hours-for-ai-employee>)

  


### **Test your Voice AI Agent during creation:**

  


You can run a quick test call without leaving the **Create Agent** flow.  
  


  1. In the Test Audio, there is a **Test Your Agent panel** on the right side. Choose Call type (**Phone Call or Web Call)** and Scenario **(Inbound or Outbound).**   
  

  2. Enter the phone number you want to test with.  
  

  3. Click **Call Me** to receive a test call from your Voice AI Agent. Interact with your agent to evaluate its responses. During **Web Call** tests, you can follow the conversation in real time using **Live Transcript** in the call window.   
  

  4. After the call, review:  
  


  * Call History for past test calls.  
  

  * Transcripts & Recordings to analyze the conversation.  
  

  * Summaries & Feedback to refine your agent’s behavior.


  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074841229/original/BsPwFQVSozVKS1Q51nvJaWPUqUrxEeOleg.png?1782823454)**

* * *

## **Make Your Inbound Voice AI Agent Reachable (Widget or URL)**

  


After creating an inbound Voice AI agent, choose how people will reach it. Use a **phone number** for traditional inbound calls or embed the **Voice AI Chat Widget** on a webpage to let visitors talk to your agent directly in the browser.  
  


### **Publish a Phone Number (Shareable “URL” via`tel:` links)**

  


Give callers a dedicated number that routes to your inbound agent. You can post the number anywhere and create click-to-call links for mobile users.

  


  1. Go to **Edit** your agent.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074841395/original/SNzgZ1apOAclPKZ61TBCRaLAQVr6COSeCg.png?1782823538)  
  


  2. Open the **Settings** and **assign** a HighLevel (LC Phone or Twilio) number to this agent. **Save.**  
  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074841502/original/Vyubrb-MuyeWyCz5ZME1sYVAVeP6rAlcQQ.png?1782823606)**  
  


  3. Configure your**Inbound Call Flow** and **Incoming Call Settings** so the agent answers immediately or after time-out/voicemail rules, as desired.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074841592/original/rHul6SDSg9d4LxTP_IDUnz8hMSCn0l6j7w.png?1782823658)


* * *

# **Edit and/or Delete AI Agents**

  


In order to edit or delete any of your Voice AI Agents, you would first need to click on the actions tab for that specific AI Agent and then select either **"Edit"** , or **"Delete"**.

  

    
    
    **IMPORTANT:** **Deleting a Voice AI Agent is permanent.**  
      
     If you want to keep any custom prompt information, and just render the AI Agent in a dormant state, simple remove the phone number from any give AI Agent and they will no longer participate in phone calls.

  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074841851/original/QPQEM5_8xk2Dy-FozGcLP_zUjE-oW7pR6A.png?1782823752)

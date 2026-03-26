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
  * Agent Goals Tab
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
  
![](https://jumpshare.com/share/qIIM5HWhxZuKX47ECUmy+/Screen+Shot+2026-03-17+at+19.09.16.png)  
  

  3. Click on the **\+ Create Agent** button.  
  
![](https://jumpshare.com/share/Nt7lPIZin7ewgWjsA3QU+/Screen+Shot+2026-03-17+at+19.11.08.png)  
  

  4. You can either **Create an Agent from scratch** or choose **prebuilt** **agents** from the **Marketplace**.  
  

  5. Choose your preferred method and click **Continue**.  
  
![](https://jumpshare.com/share/ZSYD0YVF1skQFqkXwHCk+/Screen+Shot+2026-03-17+at+19.12.29.png)


* * *

# **How to Configure Voice AI Agent Details**

  


When configuring your Voice AI Agent, you will need to follow a multi-step process including configuring the AI Agent, assigning actions that will happen after the phone call, and connecting the AI Agent to a phone number in your sub-account.

  


## **Agent Details Tab**

  


  1. **Agent Name:** Enter a name for your agent (e.g., “Customer Support Bot”).  
  

  2. **Business Name:** Confirm or update your business name.  
  

  3. **Voice:** Choose from a list of available voices for your AI Agent. You can preview each voice by clicking the play button.  
  

  4. **Timezone:** Select your business's timezone.  
  

  5. **LLM:** Choose your preferred LLM model.  
  
![](https://jumpshare.com/share/vjEtB31jnSglGwdrHafg+/Screen+Shot+2026-03-17+at+19.22.47.png)  
  

  6. **Advanced Settings:** Configure **Call Settings** , **Agent Behavior** , **Transcription** and**Speech Settings** & **Voice Settings**.  
  
![](https://jumpshare.com/share/TooYjdkpNYTuynk7gYS0+/GIF+Recording+2026-03-17+at+19.27.49.gif)**  
**  

  7. **Greeting Message Configuration:** Customize the first message your agent says (e.g., “Hello, you’ve reached [Business Name]. How can I assist you today?”) for both Inbound and Outbound calls. Also choose **Wait Time Before Speaking**.  
  

  8. Click **Next**.  
  
![](https://jumpshare.com/share/izpLKakCPkb2JA4VtiqQ+/GIF+Recording+2026-03-17+at+19.32.52.gif)  
  


## **Agent Goals Tab**

  


You have two options for setting up your agent’s goals: **Basic Mode** or **Advanced Mode**.

  


**Access control (View vs Manage):** If your role does not include **View & Manage Voice AI Agent Goals**, the Agent Goals area may be view-only and editing may be disabled. In this case, you may also be blocked from upgrading to the newest Voice AI experience. 

  


### **Basic Mode**

  


Basic mode simplifies the Voice AI Agent setup process by giving you few options to instruct the Voice AI Agent while in the call. No prompting required!

  


  * Choose **Knowledge Base**.  
  

  * Select the information you want the agent to collect from callers, such as: **Name** , **Email** , **Address** , **Contact's** **issue**.  
  

  * Choose if and which **Workflow you want to t****rigger post call completion**.  
  

  * If and who should receive **Email** **Notification** post call completion.


  


![](https://jumpshare.com/share/0j8vEw9zE1gNrhXr3yLY+/Screen+Shot+2026-03-17+at+19.39.49.png)

  
  


### **Advanced Mode**

  
When using the advanced mode, you are given more options to control the AI Agent such as prompts and different actions.

  

    
    
    **To Learn more about prompting, checkout these articles:******
    [AI Prompting 101](<https://help.gohighlevel.com/en/support/solutions/articles/155000002254>)
    [How to Use the Prompt Evaluator in Voice AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000006074>)
    [Voice AI - Exposed System Prompts for Agents](<https://help.gohighlevel.com/en/support/solutions/articles/155000007215>)
    [Voice AI Custom Variable Support in Prompt](<https://help.gohighlevel.com/en/support/solutions/articles/155000004690>) 

  


  * Click on the Switch to **Advanced** **Mode** button.  
  
![](https://jumpshare.com/share/zDmlLH2hWoWZvfLnueW4+/Screen+Shot+2026-03-17+at+19.47.31.png)  
  

  * Select **Knowledge Base**.  
**  
**
  * **Prompt:** Write detailed instructions and personality traits for your agent.   
  
**Prompt editor toolbar and shortcuts**  
  
When you edit the prompt in Advanced Mode, the prompt editor includes a toolbar with quick actions:  
  

    * **Undo and Redo:** Revert or re-apply recent prompt changes.
    * **Custom Value:** Insert supported values into your prompt.
    * **Evaluate:** Run a prompt evaluation to get feedback before you publish changes.  
  

    * **Keyboard shortcuts:**  
  
**Undo:** Cmd + Z (Mac) / Ctrl + Z (Windows)  
**Redo:** Cmd + Shift + Z (Mac) / Ctrl + Y (Windows)  
  
![](https://jumpshare.com/share/44MXmOe7WLVipYwIdvBl+/Screen+Shot+2026-03-06+at+19.49.21.png)  
  

  * **Setup your Actions:**  

    * **Call Transfer:** Transfer the call to a human agent under certain conditions.  
  

    * **Trigger a Workflow:** Automatically initiate workflows based on call interactions.  
  

    * **Send SMS:** Configure the agent to send SMS messages during or after the call.  
  

    * **Update Contact Fields:** Specify how information collected should update contact records.  
  

    * Appointment Booking.  
  

    * **Custom** **Action**.  
  

    * Add **MCP** (Beta)  
  
![](https://jumpshare.com/share/OdPRE5LnSGo9HnJfOHAZ+/Screen+Shot+2026-03-17+at+19.58.29.png)  
  

  * Click **Next**.


* * *

### **Trigger Workflows**

  
With Voice AI Agents, you have the option to trigger a single workflow or multiple workflows after the call ends. This keeps workflow triggering simple and allows you to control all workflow entry for Voice AI Agents based on the AI Agent that is involved in the call.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035814793/original/AaVhDvNIim1ZcaBQHFZpYDcULGB_61biyg.gif?1730404561)

  
  

    
    
    **Translation note (post-call outputs):** If Voice AI Translation is enabled, post-call outputs can include a translated summary and transcript. Workflows triggered after the call can consume the translated fields, and post-call notifications may display the translated artifacts. 

  


### **Email Notifications**

  
Send emails to individuals, or multiple people after a call has ended that involved that particular AI Agent.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155035814808/original/I7KXFj9nJ2NSpmBGENIFdVXg7jxx-VXHtw.gif?1730404590)

  


  


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
  


  1. In the Phone & Availability step, there is a **Test Your Agent panel** on the right side. Choose Call type (**Phone Call or Web Call)** and Scenario **(Inbound or Outbound).**   
  

  2. Enter the phone number you want to test with.  
  

  3. Click **Call Me** to receive a test call from your Voice AI Agent. Interact with your agent to evaluate its responses. During **Web Call** tests, you can follow the conversation in real time using **Live Transcript** in the call window.   
  

  4. After the call, review:  
  


  * Call History for past test calls.  
  

  * Transcripts & Recordings to analyze the conversation.  
  

  * Summaries & Feedback to refine your agent’s behavior.


  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155061015213/original/V-aP0HSVDV43--n10yzBrA_K8dDTMuguGg.png?1766152841)**

* * *

## **Make Your Inbound Voice AI Agent Reachable (Widget or URL)**

  


After creating an inbound Voice AI agent, choose how people will reach it. Use a **phone number** for traditional inbound calls or embed the **Voice AI Chat Widget** on a webpage to let visitors talk to your agent directly in the browser.  
  


### **Publish a Phone Number (Shareable “URL” via`tel:` links)**

  


Give callers a dedicated number that routes to your inbound agent. You can post the number anywhere and create click-to-call links for mobile users.

  


  1. Go to **Edit** your agent.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064889358/original/Qrx4asnzq9gD_mskkd1PdM43_RnU7kB_cA.png?1770997372)  
  


  2. Open **Phone & Availability** and **assign** a HighLevel (LC Phone or Twilio) number to this agent. **Save.**  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064889450/original/b0jOgOreEhegRahv2qhijy29Fk73CA_w0g.png?1770997432)**  


  3. Configure your**Inbound Call Flow** and **Incoming Call Settings** so the agent answers immediately or after time-out/voicemail rules, as desired.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064889570/original/iE4qfoDL6oAs8V7vBB23dXl0R2QeQYVvrQ.png?1770997503)  


  4. Share the number publicly (website, Google Business Profile, social, email signature).  
  


  5. To make a clickable link, use `tel:` — for example:  
  


     * **Button/link:** `tel:+15551234567`  
  


     * **HTML example:** `<a href="tel:+15551234567">Call Our AI Assistant</a>`


* * *

# **Edit and/or Delete AI Agents**

  


In order to edit or delete any of your Voice AI Agents, you would first need to click on the actions tab for that specific AI Agent and then select either **"Edit"** , or **"Delete"**.

  

    
    
    **IMPORTANT:** **Deleting a Voice AI Agent is permanent.**  
      
     If you want to keep any custom prompt information, and just render the AI Agent in a dormant state, simple remove the phone number from any give AI Agent and they will no longer participate in phone calls.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155036927896/original/yZ9a9RXstPDOVH4SRiwJpJlHXpm3WtU1bA.gif?1732137586)

# Conversation AI - Advanced Settings Overview

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004415-conversation-ai-advanced-settings-overview](https://help.gohighlevel.com/support/solutions/articles/155000004415-conversation-ai-advanced-settings-overview)  
**Category:** AI Employee  
**Folder:** Getting Started w/ Conversation AI

---

This article explains the Advanced Settings available in Conversation AI and how to configure them to control bot behavior, response timing, conversation limits, sleep and reactivation settings, and response styles.

* * *

**TABLE OF CONTENTS**

  * What are Advanced Settings in Conversation AI?
  * Key Benefits of Advanced Settings
  * How to Access Advanced Settings
  * Autopilot Mode Settings
    * Wait Time Before Responding
    * Maximum Messages a Bot Can Send in a Conversation
    * Allow the Bot to Respond to Images and Voice Notes
    * Bot Sleep and Reactivation Settings
  * Response Settings
  * Frequently Asked Questions
  * Related Articles


* * *

# **What are Advanced Settings in Conversation AI?**

  


Advanced Settings help you fine-tune how your Conversation AI bot behaves during customer interactions. These settings provide additional controls that allow you to customize how the bot responds to contacts, creating a more personalized and efficient conversational experience.

  


With Advanced Settings, you can:

  


  * Control how long the bot waits before responding.
  * Limit the number of messages the bot can send in a conversation.
  * Enable the bot to respond to images and voice notes in Autopilot Mode.
  * Automatically pause bot responses when manual or workflow messages are sent.
  * Configure when the bot should reactivate after being put to sleep.
  * Adjust the level of detail used in bot responses through Response Style Settings.


  


Properly configuring these settings can help improve engagement, streamline human handoffs, prevent unwanted automated interactions, and ensure your bot responds in a way that aligns with your business goals. By tailoring these options to your workflows, you can optimize the bot's performance for sales, support, lead qualification, and customer engagement scenarios.

* * *

## **Key Benefits of Advanced Settings**

  


  * **Improved Response Timing:** Control how long the bot waits before responding to collect multiple messages and provide more contextual replies.  
  

  * **Better Conversation Management:** Set message limits to prevent excessive automated interactions.  
  

  * **Enhanced Customer Experience:** Enable support for image and voice note inputs in Autopilot Mode.  
  

  * **Seamless Human Handoffs:** Automatically pause bot responses when team members or workflows send messages.  
  

  * **Customizable Communication Style:** Adjust response detail levels to match your business needs and audience expectations.  
  

  * **Flexible Reactivation Controls:** Automatically resume bot activity after a specified period or keep it disabled until manually reactivated.


* * *

## **How to Access Advanced Settings**

  


Advanced Settings can be configured when creating a new Conversation AI bot or when editing an existing bot. This flexibility allows you to adjust bot behavior at any stage of your implementation.

  


### **While Creating a New Bot**

  

    
    
    **Note:** Checkout our detailed article on [Setting Up Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004401>)

  


  1. Navigate to **AI Agents** > **Conversation AI**.  
  

  2. Click **\+ Create Bot**.  
  

  3. Select your **preferred setup method** :  
  

     * Guided Form Setup
     * Prompt Based Bot
     * Flow Based Builder  
  

  4. Complete the initial bot configuration.  
  

  5. Scroll to **Bot Settings** and locate **Advanced Settings**.


  


**![](https://jumpshare.com/share/IqYCzXpWcXimKXdNU25d+/GIF+Recording+2026-05-29+at+19.20.32.gif)**  


  


### **While Editing an Existing Bot**

  


  1. Navigate to **AI Agents** > **Conversation AI**.  
  

  2. Locate the bot in the Agent List.  
  

  3. Click the **three-dot menu** and select **Edit**.  
  


OR  
  


  4. **Click** directly on the **bot name**.  
  

  5. Scroll to **Bot Settings** and locate **Advanced Settings**. 


  


![](https://jumpshare.com/share/pALRit5uJSXpV34YAb2f+/GIF+Recording+2026-05-29+at+19.23.20.gif)

* * *

## **Autopilot Mode Settings**

  


Autopilot Mode Settings determine how your bot automatically interacts with contacts. These controls help balance responsiveness, conversation quality, and operational efficiency.

  


### **1\. Wait Time Before Responding**

  


The Wait Time Before Responding setting determines how long the bot waits before sending a reply. This delay allows the bot to collect multiple incoming messages and respond more naturally with a single, contextual answer.

  


**You can configure the delay using:**

  


  * Minutes 
  * Seconds


  


**Example:** If a contact sends three messages within a few seconds, the bot can wait, process all messages together, and provide one complete response instead of sending multiple replies.

  


![](https://jumpshare.com/share/MWmNh9JUq2UwPmQbHMgA+/Screenshot+2026-05-29+at+19.51.38.png)  


  


### **2\. Maximum Messages a Bot Can Send in a Conversation**

  


This setting limits the total number of automated messages the bot can send within a conversation before it automatically goes to sleep for that contact.

  


**Configuration range:**

  


  * **Minimum:** 1 message  

  * **Maximum:** 100 messages


  


**When the limit is reached:**

  


  * The bot stops responding to that contact.  

  * The conversation must be reactivated before automated responses resume.


  


**To reactivate the bot:**

  


  * Mark the conversation as **Read**.  

  * Or use another configured reactivation method.


  


![](https://jumpshare.com/share/pfBqlUwj5bukAv1mykjK+/Screen+Shot+2026-05-29+at+20.03.54.png)  


  


### **3\. Allow the Bot to Respond to Images and Voice Notes**

  


This setting enables the bot to process and respond to image and voice note inputs from contacts.

  


**Supported input types:**

  


  * Images  

  * Voice Notes


  

    
    
    **Important:** This feature is only supported when the bot is operating in **Autopilot Mode**.
    If the bot is configured in **Suggestive Mode** , enabling this setting will not activate image or voice note processing. 
    
    Response times for image and voice note analysis may be slightly longer than standard text responses.

  


![](https://jumpshare.com/share/DVdjjrzWUSGUgm5mJuZ5+/Screen+Shot+2026-05-29+at+20.08.39.png)  


  


### **4\. Bot Sleep and Reactivation Settings**

  


Bot Sleep and Reactivation Settings help manage transitions between AI-driven and human-driven conversations. These controls are particularly useful when team members need to take over customer interactions.

  


#### **Send Bot to Sleep When I Send a Manual Message or Workflow Message**

  


This setting pauses bot responses whenever selected outbound message types are sent.

  


**Available options include:**

  


  * Manual Messages
  * Workflow Messages


  


**When enabled:**

  


  * The bot automatically stops responding to the contact after the selected message type is sent.
  * Human agents can continue the conversation without interference from the AI bot.


  


**Common use cases:**

  


  * Sales representatives taking over conversations
  * Escalated support interactions
  * Personalized outreach campaigns


  


#### **Reactivate Bot After**

  


This setting determines when the bot should automatically resume responding after being put to sleep.

  


**You can configure:**

  


  * Hours
  * Minutes
  * Seconds


  


**When enabled:**

  


  * The bot automatically becomes active again after the selected duration.


  


**When disabled:**

  


  * The bot remains inactive indefinitely.  
  

  * A user must manually reactivate the bot before automated responses can resume.


  


**![](https://jumpshare.com/share/eg7We8NSbcL9SvhIJAfu+/GIF+Recording+2026-05-29+at+20.19.38.gif)**

* * *

## **Response Settings  
**

  


Response Settings help control how detailed the AI bot's replies are. This allows businesses to tailor conversations based on customer expectations and communication preferences.

  


Enabling Response Style Settings allows you to choose the level of detail the bot uses when generating responses.

  


**Available styles include:**

  


  * Concise
  * Balanced
  * Detailed


  


![](https://jumpshare.com/share/3g0RRRExjUfTgZfJecjA+/Screen+Shot+2026-05-29+at+20.23.39.png)

* * *

## **Frequently Asked Questions**

  


**Q: What happens when the maximum message limit is reached?**

The bot automatically goes to sleep for that contact and stops sending responses until it is reactivated.

  


**Q: Can the bot respond to images and voice notes in Suggestive Mode?**

No. Image and voice note processing is currently supported only in Autopilot Mode.

  


**Q: Does enabling Response Style Settings affect bot training?**

No. Response Style Settings control how the bot responds, while training controls what information the bot uses.

  


**Q: Can I disable automatic bot reactivation?**

Yes. If automatic reactivation is disabled, the bot remains inactive until manually reactivated.

  


**Q: What is the best response style for most businesses?**

Balanced is generally recommended because it provides a good mix of detail and efficiency.

  


**Q: Why would I increase the wait time before responding?**

Longer wait times allow the bot to collect multiple messages and provide more contextual responses.

  


**Q: Will workflow messages always put the bot to sleep?**

Only if the workflow message option is enabled within the Bot Sleep Settings.

  


**Q: Can I update Advanced Settings after the bot is live?**

Yes. Advanced Settings can be modified at any time by editing the bot configuration.

* * *

### **Related Articles**

  


  * [Setting Up Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004401>)  
  


  * [Training the Conversation AI Bot](<https://help.gohighlevel.com/en/support/solutions/articles/155000000996>)  
  


  * [Workflow X Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000001358>)  
  


  * [Workflow Action - Appointment Booking Conversation AI Booking Bot](<https://help.gohighlevel.com/en/support/solutions/articles/155000003363>)

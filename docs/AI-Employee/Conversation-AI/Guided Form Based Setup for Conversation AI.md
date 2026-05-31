# Guided Form Based Setup for Conversation AI

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005382-guided-form-based-setup-for-conversation-ai](https://help.gohighlevel.com/support/solutions/articles/155000005382-guided-form-based-setup-for-conversation-ai)  
**Category:** AI Employee  
**Folder:** Conversation AI

---

This article provides a step-by-step guide to setting up Conversation AI V3 using the Guided Form approach in HighLevel. With the Guided Form method, you can create bots without writing prompts—just fill out a simple form, define your objectives, and let the system handle the logic. It’s perfect for quickly building effective, on-brand AI conversations.

* * *

**TABLE OF CONTENTS**

  * What is the Guided Form Bot?
    * Key Benefits of the Guided Form Bot
    * How to Set Up the Guided Form Bot
    * Additional Instructions
    * Frequently Asked Questions
    * Related Articles


* * *

  


# **What is the Guided Form Bot?**

  


The Guided Form Bot is a user-friendly setup option within Conversation AI that removes the need for manual prompt engineering. Instead, it walks you through creating a bot using a structured form. You define key goals—like collecting contact details or answering FAQs—and the system builds a logic-driven, objective-based conversation flow behind the scenes.

* * *

## **Key Benefits of the Guided Form Bot**

  


  * **Simpler setup:** Build a Conversation AI bot by completing guided fields instead of writing detailed prompts from scratch.  
  


  * **Structured conversations:** Define objectives and questions so the bot knows what information to collect and what goal to complete.  
  


  * **Better consistency:** Keep bot behavior aligned across conversations by using clear setup fields, fallback messages, and additional instructions.  
  


  * **Improved lead qualification:** Ask targeted questions that help identify contact needs, urgency, budget, service interest, or appointment readiness.  
  


  * **Action-based automation:** Configure actions such as collecting contact details, triggering workflows, or helping contacts move toward booking.  
  


  * **Easier bot updates:** Edit objectives, instructions, questions, or actions as your business process changes.  
  


  * **Reduced prompt complexity:** Give the bot clear direction without needing to understand advanced AI prompting techniques.


* * *

## **How to Set Up the Guided Form Bot**

  


Proper setup ensures the bot collects the right information, follows the intended conversation path, and takes the correct action after each objective is completed.

  


#### _**Step 1:** Open Conversation AI_

  


Navigate to **AI Agents** in the left menu, then select the **Conversation AI** tab. Click **\+ Create Bot** in the upper-right corner to start creating a new Conversation AI agent.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072409045/original/TbqdYZFH58Tba9kb8L5NKAp5kBpETn8lLg.png?1779984082)

  


  


#### _**Step 2:** Select Guided Form Based Setup_

  


Choose **Guided Form Based Setup** as the setup method.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072409078/original/nYjEBwGYO0w8LcSJAB5SOceEmqRE7kXd7A.png?1779984119)  
  


#### _**Step 3:** Select Type of Bot_

  


Select the type of bot you would like to create (_General Q &A_ or _Appointment Booking_) then click **Continue**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072409134/original/4Mjr8pZKYYdpZMQ5rGgpxzP_AzJy6x-APw.png?1779984169)  
  


#### _**Step 4: Select Brand Voice**_

  


Choose a **Brand Voice** from the dropdown or create a new Brand Voice before continuing. After selecting a Brand Voice, you can optionally click **Edit** to adjust the voice settings.  
  
For more info on creating a brand voice, see: [Create Your Brand Voice](<https://help.gohighlevel.com/en/support/solutions/articles/155000007263>)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072409282/original/gqhyuCNLQplYU26LrvtvCrlZ8CPtJN47zQ.png?1779984267)  
  


####  _**Step 5:** Bot Settings_

  


Configure Your Bot's Communication Preferences and Language Settings.

  


  * **Bot Name:** Give your bot a friendly identifier.  
  

  * **Preferred Channels:** Select the channels where the bot should respond, such as Instagram, Facebook, SMS, and any other available connected channels.****  
  

  * **Bot Initial Message:** This is the first message the bot will send to users. If left empty, the bot will use a generic greeting.  
  

  * **Make this as Primary Bot:** Enable this option if this bot should reply to inbound messages as the Primary Bot. Make sure the preferred channels are assigned to this bot.  
  

  * **Wait Time Before Responding:** Set how long the bot should wait before replying, such as 2 seconds.


  


Click **Next** after the Bot Settings are complete.

**  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072409617/original/_nnWEVTqmw6HeVYirKkMV-qomkT2HIz9zw.png?1779984603)

  


  


#### _**Step 6:** Information Collection_**  
**

  


Choose the contact details the bot should collect. Available options shown in the setup include Name, Email, Phone, Street Address, and City.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072418618/original/FZs1_81_xSlSo6fzqs1DK9OqFtMV6VniSw.png?1779996844)

  


  


#### _**Step 7:** Custom Question / Objectives_

  


Add all the objectives you’d like the bot to complete. Enable **Skip if Already Filled** to prevent asking for existing contact data.

  


Common use cases include:

  


  * Ask for name, email, phone  
  

  * Qualify lead with Yes/No questions  
  

  * Offer scheduling link


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072419146/original/xIWyrjSnVtGqrP-OLMl2yE6HL07i6_P9Iw.png?1779997566)

  
  


####  _**Step 8:** Appointment Details_

  


Enable **Appointment Booking** to allow the bot to book an appointment, then select the calendar the bot should use. 

  


You can also select workflows under **Trigger Workflows After Appointment Booking** if an automation should run after the appointment is booked.

  


Use the secondary appointment toggles to decide whether the bot can manage existing appointments.  
  


  * Enable **Allow bot to cancel the appointment** if the bot should be able to cancel appointments.  
  

  * Enable **Allow bot to reschedule the appointment** if the bot should be able to reschedule appointments.


  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072418930/original/_KzipL4mnZTYBP-5J0s-Q411thpiAd9BeA.png?1779997366)**  
  


#### _**Step 9:** Email Notification Settings_

  


Use Email Notification Settings to receive an email when the bot does not know the answer. Enable **Receive Email Notification if The Bot Doesn’t Know the Answer** , then choose who should receive the notification.

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072418938/original/UFjBV2F9DqT1nikEwiaRNIG3qGgUhIvynw.png?1779997390)**

**  
**

**  
**

#### _**Step 10:** Enable Conversation Summary_

  


Enable **Conversation Summary** when the system should generate a summary after a conversation becomes inactive. Configure the **Set Inactivity Time** value and the **Minimum Messages required to generate Summary** value.

  


You can also choose whether to trigger a workflow when the summary or transcript is generated, save the summary to a custom field, or receive an email notification for the conversation summary.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072418961/original/fk5FHlR_Ki4pTkgK9bFiOiZz_KIL0gLN3Q.png?1779997430)

  


  


#### _**Step 11:** Save the Bot_

  


After Bot Goals are configured, click **Save**. 

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072419766/original/maEWvd491TY0rruiGQRG7r4z2KKrtR1tbA.png?1779998884)

  


  


####  _**Step 12:**__Set the Status_

  


After the bot is created, the **Bot Created Successfully** modal appears. The bot’s initial status is set to **Off** , which means it is not actively responding in conversations yet.  
  


Choose one of the available status options:  
  


  * **Off:** Turns off Conversation AI so the bot does not actively respond.  
  


  * **Suggestive:** Suggests prompts within the chat window for a team member to review and send.  
  


  * **Auto Pilot:** Allows the bot to reply automatically based on trained data.


  


From this modal, you can also click **Test Your Bot** , open **Go To Advanced Settings** , or click **Save and Close** to finish setup.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072419833/original/9dyC8NK5VALmZvNhjdHQNlDPoR3zR_t87w.png?1779999055)

* * *

## **Additional Instructions**

  


Use Additional Instructions to give your bot extra context and guardrails so it follows your processes consistently and handles edge cases confidently. Character limit: Up to 2,000 characters (previously 1,200).

  
Best practices  
  


  * Define the bot’s role and boundaries.  
  

  * Use clear do/don’t rules for tricky scenarios.  
  

  * Keep bullets concise; put critical steps first.


  
Where to find it  
  


  1. Go to Conversation AI and select Edit on the bot you would like to add instructions to.  
  

  2. Locate Additional Instructions.  
  

  3. Enter your guidance and Save.


* * *

## **Frequently Asked Questions**

  


**Q: Can I switch between Guided Form and prompt-based bots?**

Yes! From the bot creation screen, click the dropdown arrow next to “Create Bot” to choose your setup method.

  


**Q: Can I edit the bot after it’s created?**

Absolutely. Just open the bot from the Bot Manager and click “Edit.”

  


**Q: What happens if the user doesn’t answer a question?**

The bot will either retry, move on, or end the conversation—based on how you’ve configured each objective.

  


**Q: Can I duplicate a bot?**

Yes. Use the Duplicate option in the bot menu to reuse a configuration.

  


**Q: Can I use Guided Form bots across channels like Instagram or WhatsApp?**

Yes, as long as those channels are integrated into your HighLevel setup.

  


**Q: When does the Guided Form flow start if I set an Initial Message?**

If you configure an Initial Message, the bot sends that welcome message first and waits for the contact’s next reply before starting the objectives/questions flow. If you leave Initial Message blank, the flow starts immediately on the first message.

* * *

## **Related Articles**

  


  * [Setting Up Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004401>)  
  

  * [Conversation AI - Transfer Bot Action](<https://help.gohighlevel.com/en/support/solutions/articles/155000005371>)  
  

  * [Auto-Pilot Mode in Conversation AI for Efficient Communication](<https://help.gohighlevel.com/en/support/solutions/articles/155000001022>)  
  

  * [Conversations AI - Suggestive Mode](<https://help.gohighlevel.com/en/support/solutions/articles/155000007994>)

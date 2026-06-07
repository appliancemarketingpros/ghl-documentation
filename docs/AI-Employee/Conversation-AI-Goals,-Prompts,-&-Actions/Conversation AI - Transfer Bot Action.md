# Conversation AI - Transfer Bot Action

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005371-conversation-ai-transfer-bot-action](https://help.gohighlevel.com/support/solutions/articles/155000005371-conversation-ai-transfer-bot-action)  
**Category:** AI Employee  
**Folder:** Conversation AI - Goals, Prompts, & Actions

---

The **Transfer Bot Action** in HighLevel’s Conversation AI allows one AI bot to seamlessly transfer a conversation to another bot based on user intent or trigger conditions. This helps businesses create modular bot experiences, reduce complex workflows, and route contacts to the right bot for the right service without losing conversation flow.

* * *

**TABLE OF CONTENTS**

  * What is the Transfer Bot Action?
  * Key Benefits of Transfer Bot Action
  * How to Configure the Transfer Bot Action
  * Transfer Bot Action Requirements
  * Transfer to Another Bot
  * Using Trigger Conditions and Example Phrases
  * Important Workflow Note
  * Best Practices for Transfer Bot Action
  * Frequently Asked Questions
  * Related Articles


* * *

## **What is the Transfer Bot Action?**  
  


The Transfer Bot Action allows a Conversation AI bot to hand off a conversation to another AI bot when a specific intent, phrase, or condition is detected. Instead of building one large bot to handle every possible scenario, you can create specialized bots for different services, departments, languages, or customer needs.

For example, if a contact starts with a general service bot but mentions “My AC is not working,” the conversation can automatically transfer to an AC repair bot configured to handle that specific service.

* * *

## **Key Benefits of Transfer Bot Action**  
  


The Transfer Bot Action improves bot routing, simplifies automation setup, and helps contacts reach the right AI agent faster.  
  


  * **Improves user experience:** Routes contacts to the most relevant bot based on what they need.  
  

  * **Reduces complex workflows:** Allows bot-to-bot handoffs without building unnecessary workflow branches.  
  

  * **Supports modular bot setups:** Lets businesses create separate bots for different services, teams, departments, or languages.  
  

  * **Improves automation accuracy:** Keeps each bot focused on a specific topic or use case.  
  

  * **Preserves conversation flow:** Helps the destination bot continue the conversation naturally after the transfer.  
  

  * **Simplifies bot maintenance:** Makes it easier to update individual bots instead of managing one large bot.  
  


* * *

## **How to Configure the Transfer Bot Action**  
  


Proper setup ensures the source bot can identify when a transfer is needed and route the conversation to the correct destination bot. Both bots should be active, compatible, and configured before enabling the transfer.  
  


  1. From your sub-account, navigate to **AI Agents**.  
  

  2. Select **Conversation AI** from the top navigation.  
  

  3. Open the **Agents List** tab.  
  

  4. Click the three-dot menu next to the bot you want to edit.  
  

  5. Select **Edit**.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072660209/original/XDJHljwzVjx-WlXhCn32pa5GCra41T4-wQ.png?1780377865)**  


  6. Open the**Bot Goals** tab.  
  

  7. Under **Setup your Actions** , click **Transfer Bot**.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072660313/original/VVMaW8SY1OU9lOM5RmmTsnpM5JqlwbZZtA.png?1780377955)**  
  


  8. In the**Bot Transfer** window, enter an **Action name**. Use a clear name that explains where the conversation will be transferred, such as “Transfer to AC Repairing Bot.”  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072660372/original/lK2kq4vNYRyfy5ayx_MezQBxY1_b5fQdUg.png?1780378010)**  


  9. Select the destination bot from the**Select Bot to Transfer to** dropdown.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072660464/original/2emfeweEMaZNgs_0gznzCWYIrCr4rtupVw.png?1780378094)**  


  10. Confirm that the current bot and selected bot are compatible. The bots should be active on the same channel and both should be in**Auto Pilot** mode.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072660510/original/PeMEFZl2Ohysc7PSXnIuFoOGQmdB0Nqhhg.png?1780378117)**  


  11. Add a**Trigger Condition** to define when the transfer should happen. For example: “The customer says AC repairing or needs AC repairing services.”  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072660527/original/Q3AtGLKvB-Sk7DzhPP5viycgozcsLvL_hg.png?1780378146)**  


  12. Add**Example Phrases** that contacts may use to trigger the transfer action. For example: “AC repairing,” “My AC is not working,” or “I need AC repair.”  
  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072660530/original/3xP_mJSmrdeUfr1rccI_dG5VAAY8yGRXsg.png?1780378168)**

  13. Click**Save** to apply your changes.


* * *

  


## **Transfer Bot Action Requirements**  
  


Transfer Bot Action depends on compatibility between the source bot and destination bot. If these requirements are not met, the transfer may not work as expected.  
  


  * The source bot and destination bot must be active on the same channel.  
  

  * For example, if the source bot is active on Live Chat, the destination bot must also be active on Live Chat.  
  

  * Both bots must be in **Auto Pilot** mode.  
  

  * The destination bot should be published and tested before using it in a live transfer.  
  

  * Trigger conditions and example phrases should be specific enough to avoid accidental transfers.  
  


* * *

## **Transfer to Another Bot**  
  


Transferring to another bot is useful when your business has multiple services, departments, or conversation paths that are better handled by separate AI agents. This allows each bot to stay focused while still creating a connected experience for the contact.  
  


Common examples include:  
  


  * A general intake bot transferring to a sales bot.  
  

  * A support bot transferring to a billing bot.  
  

  * A home services bot transferring to an HVAC, plumbing, electrical, or roofing bot.  
  

  * A multilingual bot transferring to a language-specific bot.  
  

  * A general appointment bot transferring to a service-specific booking bot.  
  


Example: A contact asks, “Do you repair AC units?” The general services bot detects the intent and transfers the conversation to the AC repair bot.

* * *

## **Using Trigger Conditions and Example Phrases**  
  


Trigger conditions tell Conversation AI when the transfer should happen. Example phrases help the bot understand the types of contact messages that should match the transfer scenario.  
  


Use clear, realistic phrases that contacts are likely to send, such as:  
  


  * “My AC is not working.”  
  

  * “I need help with billing.”  
  

  * “Can I book a dental cleaning?”  
  

  * “I want to speak with someone about roofing.”  
  

  * “Do you offer emergency plumbing?”  
  


Avoid vague trigger conditions that could match too many conversations. Specific examples help improve transfer accuracy.

* * *

## **Important Workflow Note**  
  


If you are using the **Update Conversation AI Bot and Status** workflow action, add a **Wait** step before or after the update action as needed. Without a Wait step, the original bot may continue reassigning the conversation, which can break the transfer logic.  
  


Use this note when combining Transfer Bot Action with workflow automation:  
  


Add a Wait step when using the Update Conversation AI Bot and Status workflow action to prevent the original bot from reassigning the conversation and interrupting the transfer.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072660830/original/rzrC0LtdqopjE57rsbnqCtFltrEOxM-9Eg.png?1780378485)**

* * *

## **Best Practices for Transfer Bot Action**

  


A well-configured transfer creates a smoother handoff and helps prevent contacts from reaching the wrong bot or experiencing a dead end.  
  


  * Use clear action names that describe the destination bot.  
  

  * Keep each bot focused on a specific topic, service, department, or language.  
  

  * Make sure all destination bots are published before selecting them.  
  

  * Confirm that both bots are active on the same communication channel.  
  

  * Keep both bots in **Auto Pilot** mode.  
  

  * Test each transfer scenario before using it with live contacts.  
  

  * Add enough example phrases to help Conversation AI understand user intent.  
  

  * Avoid overlapping trigger conditions across multiple transfer scenarios.  
  


* * *

## **Frequently Asked Questions**  
  


**Q: What does the Transfer Bot Action do?**  
The Transfer Bot Action transfers a conversation from one Conversation AI bot to another bot based on user intent, trigger conditions, or example phrases.  
  


**Q: Can I transfer a conversation to any bot?**  
You can transfer to a compatible destination bot. The source and destination bots must be active on the same channel, and both bots must be in Auto Pilot mode.  
  


**Q: Will the conversation history be preserved after transfer?**  
Yes. The conversation context is preserved so the destination bot can continue the conversation more naturally.  
  


**Q: Why is my transfer not working?**  
The most common causes are channel mismatch, one of the bots not being in Auto Pilot mode, the destination bot not being published, or trigger conditions that are too vague.  
  


**Q: Can I use Transfer Bot Action instead of building complex workflows?**  
Yes. Transfer Bot Action can reduce the need for complex workflow routing by allowing one bot to hand off the conversation directly to another bot.  
  


**Q: What happens if I use the Update Conversation AI Bot and Status workflow action?**  
Add a Wait step when using this workflow action. Without it, the original bot may keep reassigning the conversation and break the transfer logic.  
  


**Q: Can I use Transfer Bot Action for different departments or services?**  
Yes. You can create separate bots for sales, support, billing, service booking, or other departments and transfer contacts based on their needs.  
  


**Q: Should the destination bot be tested before using it?**  
Yes. Always publish and test the destination bot before enabling it in a live transfer scenario.

* * *

## **Related Articles**  
  


  * [Conversation AI Bot - Explained](<https://help.gohighlevel.com/en/support/solutions/articles/155000001335>)  
  

  * [Setting Up Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004401>)  
  

  * [Conversation AI Flow Builder](<https://help.gohighlevel.com/en/support/solutions/articles/155000006515>)

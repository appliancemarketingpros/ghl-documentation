# How to Manage Conversation AI Bot Channels and Routing

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008266-how-to-manage-conversation-ai-bot-channels-and-routing](https://help.gohighlevel.com/support/solutions/articles/155000008266-how-to-manage-conversation-ai-bot-channels-and-routing)  
**Category:** AI Employee  
**Folder:** Conversation AI

---

Conversation AI Channel Management lets you decide which bot responds, where it responds, and which contacts it serves. Each bot can be assigned directly to supported channels without requiring a workflow simply to make the bot active. You can also route messages by connected page, number, widget, and contact tags for more precise multi-bot setups.

* * *

**TABLE OF CONTENTS**

  * What Is Conversation AI Channel Management?
  * Key Benefits of Conversation AI Channel Management
  * Supported Conversation AI Channels
  * The Updated Conversation AI Agents List
  * How Bot Routing Works
  * Direct Bot Assignment Priority
  * Channel-Level Deployment Settings
  * Tag-Based Routing
  * Preventing Conflicting Bot Assignments
  * Automatic Migration from the Primary Bot Model
  * How To Enable Conversation AI Channel Management
  * How To Configure a Bot’s Deploy Settings
  * How To Route Regular and Premium Customers to Different Bots
  * Configure the Regular Customers Bot
  * Configure the Premium Customers Bot
  * How To Verify Which Bot Responded
  * Verify the Regular Customer Route
  * Verify the Premium Customer Route
  * Frequently Asked Questions
  * Related Articles


* * *

# **What Is Conversation AI Channel Management?**

  


Conversation AI Channel Management is a bot-level deployment system that controls where each Conversation AI bot can respond. Instead of relying on one Primary Bot, each bot can be configured independently through its **Deploy** tab.

  


Channel assignments can combine:

  * A supported messaging channel  
  


  * A connected page, phone number, account, or widget  
  


  * Tags the contact must have  
  


  * Tags the contact must not have


  


This makes it possible to use several bots in the same subaccount while giving each bot a clear group of conversations to handle.

* * *

## **Key Benefits of Conversation AI Channel Management**

  


Bot-level deployment makes it easier to build predictable multi-bot setups without creating unnecessary workflows.

  


  * **Simpler bot deployment:** Assign a bot directly to its channels from the Deploy tab.  
  


  * **More precise routing:** Combine the channel, connected destination, and contact tags to control which bot responds.  
  


  * **Better customer segmentation:** Route premium customers, new leads, support requests, or other groups to different bots.  
  


  * **Flexible multi-bot setups:** Use separate bots for sales, support, locations, pages, widgets, or customer groups.  
  


  * **Fewer routing conflicts:** HighLevel prevents two bots from using the same channel, destination, and tag setup.  
  


  * **Automatic migration:** Existing Primary Bot channel assignments are moved into the new deployment experience.


  


* * *

## **Supported Conversation AI Channels**

  


Each channel represents a place where customers can send messages to your business. Channel settings are managed separately so a bot can respond only through the destinations you choose.

  


Conversation AI Channel Management supports:

  * SMS

  * Email

  * Facebook

  * Instagram

  * WhatsApp

  * Live Chat

  * Chat Widget


  


The options available inside each channel depend on the type of connection. For example, one channel may allow you to select a phone number, while another may allow you to select a page or widget.

* * *

## **The Updated Conversation AI Agents List**

  


The updated Agents List focuses on the bot’s name, status, most recent update, and available actions. Channel assignments are no longer managed from the main list because each bot now has its own deployment settings.

  


Open **AI Agents > Conversation AI > Agents List** to view and manage your bots.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076564174/original/_PhptkbTlBETBTgZbDgO0wtWpDM1XjQtQw.png?1784711242)**

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076564252/original/9WYZnBVBPxkwcim8vwv0DuvGD0iQJ0PVSA.png?1784711284)**

* * *

## **How Bot Routing Works**

  


Bot routing determines which Conversation AI bot is allowed to answer an incoming message. HighLevel reviews direct contact assignments first, then uses the bot’s channel and tag settings to find the matching deployment.

  


A deployment rule may include:

  * The messaging channel  
  


  * The connected destination, such as a page, number, or widget  
  


  * Tags the contact has  
  


  * Tags the contact does not have


  


For example, two bots can use the same Chat Widget when one bot is assigned to contacts with a `regular-customer` tag and the other is assigned to contacts with a `premium-customer` tag.

* * *

## **Direct Bot Assignment Priority**

  


A direct bot assignment keeps a specific contact with the selected bot, even when another bot would normally match the contact’s channel and tags. This priority helps preserve intentional handoffs and workflow-based assignments.

  


Direct assignments include:

  * Assigning a bot directly to a contact  
  


  * Using the **Update Conversation AI Bot and Status** workflow action  
  


  * Using **Transfer Bot** to hand the conversation to another bot


  


A directly assigned bot takes priority across supported channels. The contact remains with that bot until the assignment or bot status changes.

* * *

## **Channel-Level Deployment Settings**

  


The Deploy tab controls the channels where a bot can respond. Each channel has its own switch and, where available, an edit control for selecting the destination and adding contact conditions.

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076564620/original/mlIOF7-0fqKHqjuC72cR7UjzpK8iitd2Mg.png?1784711417)**

  


  


A channel card may show:

  * Whether the channel is enabled  
  


  * The selected phone numbers, pages, accounts, or widgets  
  


  * An edit icon for more detailed routing  
  


  * A summary such as **All phone numbers** , **All pages** , or **All widgets**


  


* * *

## **Tag-Based Routing**

  


Tag-based routing lets different bots serve different contact groups through the same channel. This is useful when customers need different responses based on their plan, location, lead type, service level, or stage in the customer journey.

  


The Edit Channel window includes two tag controls:

  * **Has tags:** The contact must match the selected tag condition.  
  


  * **Doesn’t have tags:** The contact must not match the selected tag condition.


  


Tag fields also include:

  * **AND:** The contact must meet all selected tag conditions.  
  


  * **OR:** The contact must meet at least one selected tag condition.


  


Avoid creating routing rules that can match the same contact unless the intended priority has been confirmed.

* * *

## **Preventing Conflicting Bot Assignments**

  


Clear deployment rules ensure that one eligible bot handles each incoming message. HighLevel prevents identical routing setups so two bots cannot share the same channel, connected destination, and tag configuration.

  


A conflict may occur when two bots use the exact same combination of:

  * Channel

  * Connected page, number, account, or widget

  * **Has tags** conditions

  * **Doesn’t have tags** conditions


  


Adjust the destination or tag conditions when HighLevel prevents a duplicate assignment.

* * *

## **Automatic Migration from the Primary Bot Model**

  


Automatic migration preserves existing bot behavior when Channel Management is enabled. The previous Primary Bot is assigned to the channels it already supported, allowing it to continue responding while you review the new deployment settings.

  


When the feature is enabled through Labs:

  1. HighLevel begins migrating the existing channel setup.  
  


  2. Allow approximately five minutes for the migration to complete.  
  


  3. Open the previous Primary Bot.  
  


  4. Review its **Deploy** tab.  
  


  5. Confirm that the expected channels are enabled.  
  


  6. Split channels or customer groups across other bots as needed.


  


Use the Primary Bot term only when referring to the earlier setup. New deployments should be managed through each bot’s Deploy tab.

* * *

## **How To Enable Conversation AI Channel Management**

  


Enabling the feature prepares the subaccount for bot-level channel assignments and migrates the existing Primary Bot settings. Complete this step before changing channel ownership so the current setup has time to move into the new deployment model.

  


  1. Open the required subaccount.  
  


  2. Go to **Settings**.  
  


  3. Open **Labs**.  
  


  4. Find **Conversations AI Channel Management**.  
  


  5. Enable the feature.  
  


  6. Allow approximately five minutes for the existing setup to migrate.  
  


  7. Open **AI Agents > Conversation AI > Agents List**.  
  


  8. Review the Deploy settings for the existing bots.


  

    
    
    **Important:** The Labs step applies while the feature remains available as an optional Labs feature. Remove this step when Channel Management becomes available by default.

  


* * *

## **How To Configure a Bot’s Deploy Settings**

  


Proper deployment settings help the bot receive only the messages it is meant to handle. Configure one channel at a time, then test the result with contacts who match and do not match the routing conditions.

  


  1. Go to **AI Agents > Conversation AI**.  
  


  2. Open the **Agents List** tab.  
  


  3. Select the bot you want to configure.  
  


  4. Click **Deploy**.  
  


  5. Turn on the required channel.  
  


  6. Click the channel’s edit icon when additional settings are available.  
  


  7. Turn on **Assign channel**.  
  


  8. Select the required page, phone number, account, or widget.  
  


  9. Add the required **Has tags** conditions.  
  


  10. Add any **Doesn’t have tags** conditions.  
  


  11. Choose **AND** or **OR** where needed.  
  


  12. Click **Update**.  
  


  13. Click **Save** to save the bot’s deployment settings.  
  


  14. Repeat the process for other channels as needed.


* * *

## **How To Connect a Conversation AI Bot to a Website Chat Widget**

  


The website Chat Widget controls how chat appears on your site, while the bot assignment is managed from the Conversation AI bot’s **Deploy** tab. The bot is no longer selected from an Agent tab inside the Chat Widget builder.

  


  1. Go to **Sites > Chat Widgets**.  
  

  2. Create a new widget or open an existing widget.  
  

  3. Configure and save the widget.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076614471/original/8UPanb_14bh8kcSw94wWgjc3OphsPCnJdg.png?1784733533)
  4. Go to **AI Agents > Conversation AI**.  
  

  5. Open the bot you want to use.  
  

  6. Select the **Deploy** tab.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076614595/original/EuLEhiXBEFusP6CUe-ljqHxg_aK_ELRMkw.png?1784733599)
  7. Enable **Chat Widget**.  
  

  8. Click the edit icon for the Chat Widget channel.  
  

  9. Turn on **Assign channel**.  
  

  10. Select the required widget.  
  

  11. Add tag conditions when needed.  
  

  12. Click **Update**.  
  

  13. Save the bot.  
  

  14. Test the widget on your website.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076614741/original/KRrh-0eEZxT_6E_m1j79lyh9YrvFcu6Q5Q.png?1784733697)**

* * *

## **How To Route Regular and Premium Customers to Different Bots**

  


A shared channel can support several bots when each bot has a different tag rule. This example routes contacts from one Chat Widget to either a Regular Customers Bot or a Premium Customers Bot.

###   


### **Configure the Regular Customers Bot**

  1. Open the **Regular Customers Bot**.  
  


  2. Click **Deploy**.  
  


  3. Enable **Chat Widget**.  
  


  4. Open the channel settings.  
  


  5. Turn on **Assign channel**.  
  


  6. Select **Chat Widget 1**.  
  


  7. Under **Has tags** , select `regular-customer`.  
  


  8. Click **Update**.  
  


  9. Save the bot.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076565589/original/bTZG4WLnwR9btyXst7nnpByywQcydMrctw.png?1784711921)**

  


###   


### **Configure the Premium Customers Bot**

  1. Open the **Premium Customers Bot**.  
  


  2. Click **Deploy**.  
  


  3. Enable **Chat Widget**.  
  


  4. Open the channel settings.  
  


  5. Turn on **Assign channel**.  
  


  6. Select **Chat Widget 1**.  
  


  7. Under **Has tags** , select `premium-customer`.  
  


  8. Click **Update**.  
  


  9. Save the bot.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076565719/original/MK10mwr7VWzhhzWHuk-IS0gP8APQev8zDQ.png?1784711973)**

These two bots can share the same widget because their tag conditions are different.

* * *

## **How To Verify Which Bot Responded**

  


Checking the bot assignment and AI Response Info confirms that the routing rules worked as expected. Test each route with a contact whose tags match the intended bot.

###   


### **Verify the Regular Customer Route**

  1. Open a contact with the `regular-customer` tag.  
  


  2. Send a message through the configured channel.  
  


  3. Review the **Conversation AI Bot** panel.  
  


  4. Confirm that **Regular Customers Bot** is assigned.  
  


  5. Open **AI Response Info** for the generated response.  
  


  6. Confirm the bot name and response mode.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076565972/original/1W0n2ybH1mc3eBn2ohRWNl-VRJYw0GBXPQ.png?1784712124)**

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076566038/original/G4Me_lqgRG84sg2t13U93Fqssh_LiEvC1Q.png?1784712178)**

###   


### **Verify the Premium Customer Route**

  1. Open a contact with the `premium-customer` tag.  
  


  2. Send a message through the configured channel.  
  


  3. Review the **Conversation AI Bot** panel.  
  


  4. Confirm that **Premium Customers Bot** is assigned.  
  


  5. Open **AI Response Info**.  
  


  6. Confirm that the Premium Customers Bot generated the response.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076566203/original/GPKmF0qw8jhaiqNeaxNQB6-iTzEUVU8qTw.png?1784712324)**

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076566263/original/0n_VDdnnPRaQRS3GFqvPZBWIv055xreC4g.png?1784712370)**

* * *

## **Frequently Asked Questions**

  


**Q: The Agent tab is missing from my Chat Widget. How do I select a Conversation AI bot?**  
A: Conversation AI bots are no longer selected from the website Chat Widget builder. Create and install the widget under **Sites > Chat Widgets**, then open the required bot under **AI Agents > Conversation AI > Deploy** and assign it to the Chat Widget channel.

  


**Q: Do I still need a workflow to make a second Conversation AI bot respond?**  
A: No. A bot can now be assigned directly to channels through its Deploy settings. Workflows remain useful when you need to assign a bot directly to a particular contact.

  


**Q: Can two bots use the same channel?**  
A: Yes. They must use different destinations or tag conditions so HighLevel can determine which bot should respond.

  


**Q: Can two bots use the same Chat Widget?**  
A: Yes. For example, one bot can serve contacts with a `regular-customer` tag while another serves contacts with a `premium-customer` tag.

  


**Q: What happens when a bot is assigned directly to a contact?**  
A: The directly assigned bot takes priority over normal channel and tag routing.

  


**Q: Does Transfer Bot override the Deploy settings?**  
A: A transferred bot is directly assigned to the contact and takes priority over the standard routing rules.

  


**Q: What happens to the existing Primary Bot when I enable Channel Management?**  
A: HighLevel automatically assigns it to the channels it previously supported. Review its Deploy tab after migration to confirm the settings.

  


**Q: Why can’t I save a channel configuration?**  
A: Another bot may already use the same channel, destination, and tag conditions. Change one or more routing settings to create a distinct rule.

  


**Q: What happens when no bot matches the contact’s tags?**  
A: The bot will not qualify under that tag-based deployment. Review your broader channel assignments and fallback plan before enabling the setup.

  


**Q: Does disabling a channel stop the bot from responding there?**  
A: Disabling the channel removes that bot’s normal deployment eligibility for the channel. A direct contact assignment may still affect which bot is attached to the conversation.

  


**Q: How can I confirm which bot generated a response?**  
A: Open the conversation’s **AI Response Info** panel and review the bot name shown with the AI response.

* * *

### **Related Articles**

  * [How to Create and Set Up a Conversation AI Bot in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000004401-how-to-set-up-a-conversation-ai-bot>)  
  


  * [Workflow Action — Update Conversation AI Bot and Status](<https://help.gohighlevel.com/support/solutions/articles/155000003821-workflow-action-update-conversation-ai-bot-and-status>)  
  


  * [Transfer Bot Action in Conversation AI](<https://help.gohighlevel.com/support/solutions/articles/155000005371-conversation-ai-transfer-bot-action>)  
  


  * [Bot Status for Individual Contacts](<https://help.gohighlevel.com/support/solutions/articles/155000004096-bot-status-for-individual-contacts>)  
  


  * [Conversation AI Flow Builder](<https://help.gohighlevel.com/support/solutions/articles/155000006515-conversation-ai-flow-builder>)  
  


  * [Conversation AI Agents Dashboard](<https://help.gohighlevel.com/support/solutions/articles/155000005427-conversation-ai-agents-dashboard>)

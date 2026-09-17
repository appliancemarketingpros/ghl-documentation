# How to Use Custom Conversation Providers with Conversation AI

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008559-how-to-use-custom-conversation-providers-with-conversation-ai](https://help.gohighlevel.com/support/solutions/articles/155000008559-how-to-use-custom-conversation-providers-with-conversation-ai)  
**Category:** AI Employee  
**Folder:** Conversation AI

---

Conversation AI can reply to messages that come through supported apps installed from the HighLevel App Marketplace. You can choose which of these apps each bot can use, so your bot only responds through the channels you want. This gives you more control when your business uses messaging apps outside HighLevel’s built-in channels.

  

    
    
    **Labs feature** : To use custom Marketplace channels with Conversation AI, turn on **Conversations AI Channel Management** in **Settings > Labs**. If this Labs feature is turned off, the custom channel options may not appear.

  


* * *

**TABLE OF CONTENTS**

  * What are Custom Conversation Providers for Conversation AI?
  * Key Benefits of Custom Conversation Providers
  * Turn On Conversations AI Channel Management in Labs
  * What You Need Before You Start
  * Where Custom Messaging Apps Appear
  * How Contact Tags Can Control Replies
  * What Changed?
  * How Conversation AI Replies Through a Marketplace App
  * How To Set Up a Custom Conversation Provider for Conversation AI
  * Step 1: Turn On Conversations AI Channel Management in Labs
  * Step 2: Install a Supported Marketplace App
  * Step 3: Open Your Conversation AI Bot
  * Step 4: Add the Marketplace Messaging App
  * Step 5: Check the Channel and Save
  * Troubleshooting Custom Conversation Providers
  * Frequently Asked Questions
  * Related Articles


* * *

# **What are Custom Conversation Providers for Conversation AI?**

  


Custom Conversation Providers let a Conversation AI bot reply through supported messaging apps from the HighLevel App Marketplace. This is useful when your business talks to customers through messaging services that are not already built into HighLevel.

  


A **Custom Conversation Provider** is simply a Marketplace app that adds another messaging channel to HighLevel.

  


HighLevel already includes channels such as:

  * SMS

  * Email

  * Facebook

  * Instagram

  * WhatsApp

  * TikTok

  * Live Chat

  * Chat Widget


  


A supported Marketplace app can add another messaging channel that your Conversation AI bot can use.

Once the app is installed and added to your bot, the bot can reply to customer messages that come through that app.

* * *

## **Key Benefits of Custom Conversation Providers**

  


Custom Conversation Providers make it easier to decide where your Conversation AI bot can respond. This gives you more control when your business uses several messaging apps.

  


  * **More messaging options:** Use Conversation AI with supported Marketplace messaging apps.  
  


  * **Choose apps for each bot:** Decide which messaging apps each bot can use.  
  


  * **Simple setup:** Add supported apps from the bot's **Deploy** tab.  
  


  * **Separate controls:** Each added messaging app can be turned on or off by itself.  
  


  * **Contact filters:** Use contact tags to control which contacts the bot can reply to.  
  


  * **Existing setups keep working:** Messaging apps that were already connected continue working after this update.


* * *

## **Turn On Conversations AI Channel Management in Labs**

  


The **Conversations AI Channel Management** Labs feature must be turned on before you can add custom Marketplace messaging apps to a Conversation AI bot. If this feature is off, the options shown in this article may not appear in your account.

  


Before doing anything else:

  1. Go to **Settings**.  
  


  2. Open **Labs**.  
  


  3. Find **Conversations AI Channel Management**.  
  


  4. Turn the feature on.  
  


  5. Return to your Conversation AI bot.


  

    
    
    **Important:** This Labs setting is required for the custom channel setup described in this article.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079715983/original/fohLJmbdU5FHxhULPQhBtmwu-m6_lV3ccA.png?1788186166)

* * *

## **What You Need Before You Start**

  


A few things need to be ready before you can connect a Marketplace messaging app to your bot. Checking these items first can help prevent missing options later.

  


Make sure you have:

  * **Conversations AI Channel Management** turned on in Labs.  
  


  * A Conversation AI bot already created.  
  


  * A Marketplace app that supports **Conversation Provider**.  
  


  * The Marketplace app installed for the correct subaccount.  
  


  * The app connected and active.


  


Not every app in the Marketplace can be used for Conversation AI messages.

  


The app must specifically support **Conversation Provider**. Only supported apps that are already installed will appear in the list when you add a new channel.

* * *

## **Where Custom Messaging Apps Appear**

  


The **Deploy** tab shows the messaging channels your bot can use. This is where you can add supported Marketplace apps and control whether the bot can respond through them.

  


On the Deploy tab, you may already see HighLevel channels such as:

  * SMS

  * WhatsApp

  * Instagram

  * Facebook

  * TikTok

  * Live Chat

  * Chat Widget

  * Email


  


You will also see **Add channels from marketplace**.

  


Use this option to add a supported Marketplace messaging app to your bot.

Once an app is added, it appears as its own card on the Deploy screen.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079716164/original/UOtbZHEd3KUPnEcieIgixcy9RgsMoGCv7w.png?1788186257)

* * *

## **How Contact Tags Can Control Replies**

  


Contact tags can help you decide which contacts the bot should or should not reply to through a specific messaging app. These rules are optional.

  


When adding a Marketplace messaging app, you may see:

  * **Has tags**

  * **Doesn't have tags**

  * **AND**

  * **OR**


  


Here is what they mean:

  * **Has tags:** The bot can use this channel only for contacts that have the selected tag.  
  


  * **Doesn't have tags:** The bot will not use this channel for contacts that have the selected tag.  
  


  * **AND:** All selected tag rules must match.  
  


  * **OR:** At least one selected tag rule must match.


  


For example, you could allow the bot to respond to contacts with the **normal** tag but not contacts with the **premium** tag.

  


You may also see an **Assign channel** switch when adding the app. Use the settings shown in your account when connecting the messaging app.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079716313/original/30dmxe0I8Ykf17d7O0ucjzfbgfUCZjDuzw.png?1788186346)

* * *

## **What Changed?**

  


Custom Marketplace messaging apps are now easier to control because each one appears separately on the Deploy tab. This makes it easier to choose exactly where your bot can respond.

  


Before this update, custom messaging apps depended on the SMS or Email settings.

  


That meant:

  * Turning on SMS or Email could also allow replies through connected custom apps.

  * You could not easily choose each custom app separately.


Now:

  * Each custom messaging app appears on the **Deploy** tab.  
  


  * You can choose which apps each bot can use.  
  


  * Each app has its own settings.  
  


  * Each app can be turned on or off separately.  
  


  * Existing custom app setups continue working.  
  


  * Apps that were already active appear automatically on the Deploy tab.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079716466/original/SltjHAdrIDGt7qNl6_m0OoepmNLxCZLRSA.png?1788186434)

* * *

## **How Conversation AI Replies Through a Marketplace App**

  


Once a supported Marketplace app is added and turned on, Conversation AI can reply to messages that come through that app. The reply goes back through the same messaging app the customer used.

  


For example:

  1. A customer sends a message through the connected Marketplace app.  
  


  2. HighLevel receives the message.  
  


  3. The Conversation AI bot reads the message.  
  


  4. The bot creates a reply.  
  


  5. The reply is sent back through the same Marketplace app.


  


The bot will only reply if:

  * the app is added to the bot,  
  


  * the app is turned on,  
  


  * the bot is saved,  
  


  * and any contact tag rules are met.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079716604/original/lWl0g8Grm46qWD7PIvKaM3k0Da8jbc1H1A.png?1788186509)

* * *

## **How To Set Up a Custom Conversation Provider for Conversation AI**

  


Setting up the feature in the correct order helps make sure the messaging app appears and the bot can reply through it. Start by turning on the required Labs feature, then install the app and connect it to your bot.

###   


### **Step 1: Turn On Conversations AI Channel Management in Labs**

  


This step is required.

  1. Go to **Settings**.  
  


  2. Open **Labs**.  
  


  3. Find **Conversations AI Channel Management**.  
  


  4. Turn it on.


  


If this setting is not enabled, you may not see the custom channel options on the Deploy tab.

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079716697/original/k_op4gjEmfDpnBtCs8oA2vBe4jZ46T2tiw.jpeg?1788186536)**

###   


### **Step 2: Install a Supported Marketplace App**

  


The app must be installed before it can be added to your bot.

  1. Open the **App Marketplace**.  
  


  2. Find the messaging app you want to use.  
  


  3. Make sure it supports **Conversation Provider**.  
  


  4. Install the app for the correct subaccount.  
  


  5. Complete the app's setup.  
  


  6. Make sure the app is active.


  


If the app does not support Conversation Provider, it will not appear in the list later.

###   


### **Step 3: Open Your Conversation AI Bot**

  


The Deploy tab is where you choose which messaging channels the bot can use.

  1. Go to **AI Agents > Conversation AI**.  
  


  2. Open the bot you want to update.  
  


  3. Click **Deploy**.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079716778/original/gxm0IBIZBcJm0ocnyoanPmWmwJtg4tysAA.jpeg?1788186573)**

###   


### **Step 4: Add the Marketplace Messaging App**

  


Now you can connect the installed app to your bot.

  1. Click **Add channels from marketplace**.  
  


  2. Open the **Installed providers** dropdown.  
  


  3. Select the app you want to use.  
  


  4. Add contact tag rules if needed.  
  


  5. Choose **AND** or **OR** if you are using more than one tag rule.  
  


  6. Click **Add channel**.


  


If the app is missing from the list, check that:

  * it is installed,

  * it is active,

  * it is installed for the correct subaccount,

  * and it supports Conversation Provider.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079716864/original/bSCE89aKxiVWErZLGFuGBO5w6v_MH56q0w.png?1788186608)**

###   


### **Step 5: Check the Channel and Save**

  


Review the setup before saving to make sure the bot is using the correct messaging app.

  1. Confirm that the new app appears on the **Deploy** screen.  
  


  2. Make sure the app is turned on.  
  


  3. Review any contact tag rules.  
  


  4. Check the bot's other active channels.  
  


  5. Click **Save**.


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079716928/original/PL0jPWCZF6IlTAF0cDnNGECTST3kzUFfEQ.jpeg?1788186650)**

* * *

## **Troubleshooting Custom Conversation Providers**

  


Most setup problems happen because the Labs feature is off, the Marketplace app is not supported, or the channel was not saved. Checking these items can quickly identify why the bot is not responding.

  


**The Marketplace app does not appear**

Check that:

  * **Conversations AI Channel Management** is turned on in Labs.  
  


  * The app is installed.  
  


  * The app is installed for the correct subaccount.  
  


  * The app supports Conversation Provider.  
  


  * The app is active.


**The bot is not replying**

  


Check that:

  * The custom messaging app was added to the bot.  
  


  * The app is turned on.  
  


  * The bot was saved after the change.  
  


  * The contact matches any tag rules you added.  
  


  * The Marketplace app itself is connected correctly.


  


**The bot replies to some contacts but not others**

Review the **Has tags** and **Doesn't have tags** rules. A contact may not meet the rules you set for that messaging app.

* * *

## **Frequently Asked Questions**

  


**Q: Do I have to turn on a Labs feature first?**  
A: Yes. **Conversations AI Channel Management** must be turned on in Labs before you can use the custom channel setup described in this article.

  


**Q: Why don't I see my Marketplace app in the list?**  
A: Only installed apps that support Conversation Provider appear. Make sure the app is installed, active, and supports this feature.

  


**Q: Can every Marketplace app be used with Conversation AI?**  
A: No. The app must support Conversation Provider.

  


**Q: Will my existing custom messaging setup stop working?**  
A: No. Existing setups continue working. Apps that were already active should appear automatically on the Deploy tab.

  


**Q: Do custom messaging apps still depend on SMS or Email settings?**  
A: With the new Channel Management experience, supported custom apps can be managed directly from the Deploy tab.

  


**Q: Why is the bot not replying through my custom app?**  
A: Make sure the app is added, turned on, saved, and connected correctly. Also check whether contact tag rules are blocking the reply.

  


**Q: Can I control which contacts the bot replies to?**  
A: Yes. You can use **Has tags** and **Doesn't have tags** rules when setting up the channel.

  


**Q: Can different bots use different Marketplace messaging apps?**  
A: Yes. You choose the channels separately from each bot's Deploy tab.

* * *

### **Related Articles**

  * [How to Set Up a Conversation AI Bot ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004401>)  
  


  * [Conversation AI Bot Explained ](<https://help.gohighlevel.com/en/support/solutions/articles/155000001335>)  
  


  * [Custom Conversation Providers in Mobile App ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004167>)

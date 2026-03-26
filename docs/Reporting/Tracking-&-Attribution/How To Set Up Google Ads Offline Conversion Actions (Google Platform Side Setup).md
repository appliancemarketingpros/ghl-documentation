# How To Set Up Google Ads Offline Conversion Actions (Google Platform Side Setup)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001220947-how-to-set-up-google-ads-offline-conversion-actions-google-platform-side-setup-](https://help.gohighlevel.com/support/solutions/articles/48001220947-how-to-set-up-google-ads-offline-conversion-actions-google-platform-side-setup-)  
**Category:** Reporting  
**Folder:** Tracking & Attribution

---

This guide explains how to configure **Google Ads offline conversion actions** directly in the Google Ads interface. It is a **standalone platform-side setup** and does not include HighLevel configuration steps. After completing this setup, use the links in **Next Steps** to connect conversions from HighLevel via Ad Manager or Workflows. 

* * *

**TABLE OF CONTENTS**

  * What is Google Ads Conversion Actions?
    * Key Benefits of Google Ads Conversion Actions
    * Prerequisites on the Google Side
    * How To Set Up Google Ads Offline Conversion Actions (Google Platform-Side)
    * Frequently Asked Questions
    * Related Articles


* * *

# **What is Google Ads Conversion Actions?**

  
Google Ads conversion actions define the events you want to track and optimize for—such as leads, calls, form submissions, or offline sales. Creating a clear, well-scoped conversion action ensures Google Ads can attribute performance correctly and helps your campaigns bid toward meaningful outcomes.

  
A **conversion action** is a rule in Google Ads that records when a desired action occurs. For offline conversions (e.g., a deal marked won in your CRM), Google Ads matches identifiers like **GCLID/GBRAID/WBRAID** to attribute results back to ads and keywords.

* * *

## **Key Benefits of Google Ads Conversion Actions**

  
Benefits focus on data quality, optimization, and reporting. Establishing the right conversion actions improves bidding signals, clarifies measurement, and prevents noisy or duplicated data.  
  


  * **Accurate Optimization** : Feeds Google Ads with clean signals for Smart Bidding.  
  


  * **Clear Reporting** : Separates primary outcomes (e.g., qualified leads) from secondary events.  
  


  * **Control Over Counting** : Decide whether to count **Every** or **One** conversion per ad interaction.  
  


  * **Flexible Attribution** : Choose a model that fits your funnel and data volume.  
  


  * **Offline Compatibility** : Supports uploading server-side/CRM events using IDs like GCLID/GBRAID/WBRAID.


* * *

## **Prerequisites on the Google Side**

  
Preparing your Google Ads account prevents rework later. Confirm access, account structure, and goal taxonomy before creating actions.  
  


  * Admin or standard access to the correct **Google Ads** account.  
  


  * Agreement on goal taxonomy (e.g., **Lead** vs **Submit lead form** vs **Qualified lead**).  
  


  * Decision on whether this action should be marked as a **Primary** action used for bidding.  
  


  * Clarity on identifiers you’ll send later (e.g., **GCLID/GBRAID/WBRAID**) when posting offline conversions from HighLevel.


* * *

## **How To Set Up Google Ads Offline Conversion Actions (Google Platform-Side)**

  
Follow these steps in **Google Ads** to create the conversion action you’ll later send data to from HighLevel. Proper setup ensures clean attribution and reliable bidding signals.

  

    
    
    **Note:** This is a **Google platform-side** guide only. To **setup offline conversions in HighLevel Ad Manager** , checkout our article on [HighLevel Ad Manager - Create & Manage Google Ads Offline Conversions.](<https://help.gohighlevel.com/en/support/solutions/articles/155000005431>)
    [](<https://help.gohighlevel.com/en/support/solutions/articles/155000005431>)
    **T****o setup and track Google Ads Conversion Actions like form submissions, number pool calling, chat widget replies etc, directly inside HighLevel Workflows** , checkout our article on [Workflow Action - Add To Google Ads.
    ](<https://help.gohighlevel.com/en/support/solutions/articles/155000003368>)

##   


  1. Head into your Google Adwords account or open [ads.google.com](<https://ads.google.com/intl/en_in/start/lc/?subid=in-en-ha-awa-bk-c-c00!o3~CjwKCAjwyYPOBhBxEiwAgpT8PxzugBXx8nv7PGe8R-bVM6pT1TSQUkUBsSH7fq-9uWlPPKDs9bWKqxoCiVUQAvD_BwE~140706620052~kwd-94527731~16862088904~592470418766&gclsrc=aw.ds&gad_source=1&gad_campaignid=16862088904&gclid=CjwKCAjwyYPOBhBxEiwAgpT8PxzugBXx8nv7PGe8R-bVM6pT1TSQUkUBsSH7fq-9uWlPPKDs9bWKqxoCiVUQAvD_BwE>).  
  


  2. Click on **"Sign In"** to sign into your google ads account or click on "Start Now" to start creating a new google ads account.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064512308/original/C8Aw37elwsskF22cfBXP7IxnyZg-vd6WuA.png?1770651246)  


  3. Click the "**+"** and Navigate to**Conversion Action** from the dropdown**.**  
  
_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067502302/original/9qUf3GbbUGIRqj0l1iAlLO-HcyOURbtFdQ.gif?1774272837)_  


  4. Choose data sources to measure conversions depending on your current Google Ads UI prompt.  
  
_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067579637/original/1wvU2iIuwl1vgDCU4q672wPZXEmaxnNILg.png?1774345111)_  


  5. To start tracking conversions, we need to choose the**Conversions offline** option.  
  
**Please Note:** HighLevel supports **Offline Conversions only.** Website, app, phone call, and other conversion sources are **not supported.**  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067579648/original/-PwtOolBiOv6IZ2uBtJZzD_-GhUtvdE7Pw.png?1774345121)  
  


  6. Click on **Edit D****ata Sources** to add an offline data source and select 'Skip this step and set up a data source later.'   
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067579723/original/VsiSQvjZtX8P0cXhZbudRHW9m_XWoawx1w.png?1774345176)  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067579852/original/j74nCVGHCYk6FtNsTFSCiGXRAtF9qKwHPA.png?1774345222)  


  7. Click **"Save and Continue".**  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067579906/original/Lc38gm87HysxZ7IKAiwmYlGfJ6gMn7wYMA.png?1774345249)  
Select the **Conversion Category.** This step is to define, "**What do you want to measure?** ". Click **"See all"** to access the entire list of conversion categories.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067506158/original/8tXXliQSYFav771REY1QnV9yBwa06VkBHw.png?1774274441)  

  8. Post selection of the conversion category, you need to add data source to the category.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067580048/original/U4gxlhKu0mq9IJ2RGZx4--KiYeZ5-CrH8Q.png?1774345321)  


  9. Click on **Edit****settings** to define the details.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067580713/original/-Kp98QJlnSnH0Od2wiV0YYMqhjt-C42fKg.png?1774345593)  


  10. This section shows the action optimisation which shows the 'Conversion Goal' selected in the earlier steps. Let the radio button be **'****Primary action used for bidding optimisation'** as the selected choice.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067580773/original/f53u6AuJzI4SU2_7b9jsWXCmby7r6dAnwQ.png?1774345640)  


  11. **Give this Conversion a name.** Please type in the name of your conversion. In this example, we are calling it "**Conversion Test** ".  
  
**__Note:__**__Once you have completed this step, please**copy and paste** your **conversion name** somewhere close.__  
_  
_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067580849/original/TCZ-Nua_u5JdjdMQXgA7sxrjV91S4dGzwg.png?1774345674)  
  


  12. Select the value for your conversion. Select from: same, different, or don't use a value... **[More info](<https://support.google.com/google-ads/answer/3419241?hl=en>)**  
  
** _![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067512334/original/OVD2rhwjEiMpi-bLkZL6FRJy95oudTnFWQ.png?1774276716)_  
**

  13. Select the count, we recommend always choosing option "**Every** ".   
  
 _![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067512364/original/Ok2YxrgbOjCqKyH3GwIb2PP9oG6xJggbiA.png?1774276744)_  


  14. Setup the conversion window and attribution model.  
  
1\. Set the _click-through conversion window_ to "**90 days"**  
  
2\. Select engaged view conversion window from the dropdown.  
  
3\. Next, set the _Attribution model_ as "**Last Click** " or "**Data Driven** " (recommended).  
  
_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067512556/original/zAV1TcL39odzlku9ZwfwwGtSwrwxZ6qFHg.png?1774276791)_  


  15. Click on**"Done"** and the conversion settings are defined and saved.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067512857/original/IuaqENbu2fX7uCCFX1IZ4KdRsdD8wKrMzw.png?1774276957)  


  16. Click on **Save and continue** to proceed with the changes. Choose**"Create Conversion"** to create a new conversion**.** Click on**"Add Another Category"** to add more conversion categories.  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067580436/original/H8j4q657JuhY9VGvEq6vj7gb4_PE-MOR0A.png?1774345508)**  


  17. Click on**Finish** to conclude the conversion creation process.|  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067580981/original/sHqe_AHeotyPhYjnrCfR12jhkrnN57S8Zg.png?1774345723)


* * *

## **Frequently Asked Questions**

  
**Q: What should I set for Count—Every or One?**  
Use **One** for lead generation to avoid inflating conversions when a contact repeats the same event. Use **Every** for revenue events like purchases.

  
**Q: How long until I see conversions in Google Ads?  
** Processing can take from a few hours up to 24–48 hours depending on volume and method. Reporting latency is normal; use absolute dates when checking reports.

  
**Q: Do I need GCLID, GBRAID, or WBRAID to upload offline conversions?**

Yes—at least one identifier is needed for reliable matching. Capture and store whichever is available on first touch, then include it when sending the conversion from HighLevel.

  
**Q: Where do I verify that conversions are being recorded?  
** In Google Ads: Tools & Settings > Conversions and in campaign reports using Conversion columns. In HighLevel, use Ad Manager reporting for visibility once HL-side sending is configured (see Related Articles).

  
**Q: Should I use HighLevel Ad Manager or Workflows to send conversions?  
** Use Ad Manager if you prefer a centralized ads workspace and built-in mapping. Use Workflows if you need granular automation or custom logic. Both can send to the same Google conversion action.

  
**Q: Why don’t my uploads match or show results?  
** Common issues include missing identifiers, incorrect timezones, currency/value mismatches, or sending to the wrong conversion action. Confirm the conversion ID/name, identifier presence, and event timestamps.

* * *

## **Related Articles**

  


  * **[](<https://help.gohighlevel.com/en/support/solutions/articles/155000003051>)[](<https://help.gohighlevel.com/en/support/solutions/articles/155000005431>)**[](<https://help.gohighlevel.com/en/support/solutions/articles/155000005431>)[Ad Manager - Create& Manage Google Ads Offline Conversions](<https://help.gohighlevel.com/en/support/solutions/articles/155000005431>)  
  


  * [Workflow Action – Add to Google AdWords.](<https://help.gohighlevel.com/en/support/solutions/articles/155000003368>)  
  


  * [Overview of Ad Manager Settings ](<https://help.gohighlevel.com/en/support/solutions/articles/155000003051>)  
  


  * [Overview of Ad Manager ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002433>)  
  


  * [How to Set Up Google Ad Reporting ](<https://help.gohighlevel.com/en/support/solutions/articles/48001219312>)  
  


  * [Understanding Attribution Source](<https://help.gohighlevel.com/en/support/solutions/articles/48001219997>)

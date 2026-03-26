# Understanding Attribution Source

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001219997-understanding-attribution-source](https://help.gohighlevel.com/support/solutions/articles/48001219997-understanding-attribution-source)  
**Category:** Reporting  
**Folder:** Tracking & Attribution

---

# **What is Attribution?**

Attribution provides a breakdown of which channels or sources a contact came from. With this information, we will be able to identify growth opportunities and determine which channels offer the most potential. For example, if we are running Facebook and Google Ads, we would like to know which is more effective at generating leads into HighLevel. Attribution can make this happen.

  


In the article below, we will walk through attribution in HighLevel and even where to go to set up your ad reporting. Let's hop in!

  


  


* * *

**TABLE OF CONTENTS**

  * What is Attribution?
  * What is "First" or "Latest" Attribution?
  * Where to Locate Contact Attribution Data?
  * Types of Attribution Sources
    * Paid Search (Google Ads)
    * Paid Social (Facebook & Instagram Ads)
    * Direct Traffic
    * Organic Search
    * Social Media
    * Referrals
    * Others
    * CRM UI
    * Third-Party
  * What Events Record Attribution?
  * How is Attribution Source Determined?
  * Ad Reporting Setup
    * Facebook and Instagram Ads Reporting Setup
    * Google Ads Reporting Setup
  * Troubleshooting Ad Reporting Issues


* * *

# **What is "First" or "Latest" Attribution?**

When attributing a contact to a specific source it is common to consider the first and lastest attribution. Both are always stored on every single contact.

  


**First Attribution** \- is the first time a contact interacts with our system, when this happens we record attribution data for that session. For example: Someone fills out a Contact Us Form.

  


**Latest Attribution** \- is the most recent recorded interaction with us, when this happens we record attribution data for this most recent session as well. For example: After filling out a Contact Us form they then decide to purchase our product via a HighLevel Two-Step Order Form. When this happens, the latest attribution data will be recorded.

_*The latest attribution will always change based on the last recorded interaction. However, the first attribution will not._

  


Now that we know what First and Latest Attribution is, we need to know where it is stored.

  


* * *

# **Where to Locate Contact Attribution Data?**

Rather it is the first or latest attribution data, you can locate this information in the bottom right of all contacts from the contact record.

  


Within the Sub-Account, go to Contacts > select a **contact record** > then locate the attribution data at the bottom right column under the **activity** tab.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48247964170/original/VSgXZHb-pBWW3cGC7emsU4xKKLFyaKQJ3g.gif?1661800754)

###   


**For contact creation, the first and latest attribution is defined as:**

  

    
    
    **- First attribution:** The contact's first interaction is recorded in the system. This is usually their first visit to your website or an interaction with any of the sources listed above.  
      
    **- Latest attribution:** The contact's last interaction before they were converted to a contact in the system

  


* * *

  


#### 

# **Types of Attribution Sources**

Below we will walk through each of the Attribution Sources you will see on the contact’s **_First_** _**Attribution** _or _**Latest Attribution** _value will be one of the following:

  * Paid Search
  * Paid Social
  * Direct Traffic
  * Organic Search
  * Social Media
  * Referrals
  * Others
  * CRM UI
  * Third-Party


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155015178854/original/LaAFs5bfFxyo0Su56GWkBEkyyD7o2l6oQA.png?1702496706)

  


## **Paid Search (Google Ads)**

Traffic categorized under __Paid search__ comes from paid search campaigns (e.g., Google AdWords). This will help in analyzing the Google Ad Reporting.

  


**It needs to have the UTM parameters matching (It is case-sensitive)**

{YourLandingPageUrl.com}?utm_source=adwords&utm_medium={adname}&utm_campaign={campaignname}&utm_content={adgroupname}&utm_keyword={keyword}&utm_matchtype={matchtype}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}

  


Google Ads UTM Parameters

**Name**| **Key**| **Value**| **Type**| **Example**  
---|---|---|---|---  
UTM Source| utm_source| adwords|   
|   
  
UTM Medium| utm_medium| {adname}|   
|   
  
UTM Campaign| utm_campaign| {campaignname}| manual, changeable| summer_sale  
UTM Content| utm_content| {adgroupname}|   
|   
  
Match Type| utm_matchtype| {matchtype}|   
|   
  
Campaign ID| campaign_id| {adgroupid}| set by Google Ads, constant| 123456789  
Ad Group ID| ad_group_id| {adgroupid}|   
|   
  
Ad ID| ad_id| {creative}|   
|   
  
  
  


For more information, see [How to Set Up Google Ad Reporting](<https://help.gohighlevel.com/support/solutions/articles/48001219312-how-to-set-up-google-ad-reporting>).

  


  


## **Paid Social**

Traffic categorized under __Paid social__ comes from a paid social campaign. This will help in analyzing the Facebook Ad Reporting if the leads are coming from Facebook

  


**It needs to have the UTM parameters matching (It is case-sensitive)**

{YourLandingPageUrl.com}?utm_source=fb_ad&utm_medium={{adset.name}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&campaign_id={{campaign.id}}

  


Facebook and Instagram Ads UTM Parameters

**Name**| **Key**| **Value**| **Type**| **Example**  
---|---|---|---|---  
UTM Source| utm_source| fb_ad|   
|   
  
UTM Medium| utm_medium| {{adset.name}}|   
|   
  
UTM Campaign| utm_campaign| {{campaign.name}}| manual, changeable  
| summer_sale  
  
UTM Content| utm_content| {{ad.name}}|   
|   
  
Campaign ID| campaign_id| {{campaign.id}}| set by Facebook Ads, constant  
| 123456789  
  
  


For more information see, [](<https://help.gohighlevel.com/a/solutions/articles/48001219997/edit?portalId=48000045315#Facebook-\(and-Instagram\)-Ads-Attribution-Setup>)[How to Setup Facebook Ad Reporting](<https://help.gohighlevel.com/support/solutions/articles/48001204042-how-to-set-up-facebook-ad-reporting>).

  


## **Direct Traffic**

Traffic categorized under __Direct traffic__ does not have an indication of its source (_See row 8 above_). Typically, these people typed the URL directly in their browser or removed all query parameters before entering a site. 

  


To view the source URLs for these visitors, click the Direct traffic source.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48247964541/original/eIy9MeT34UCvxRzk02GYCS7qwWMvBizWbQ.gif?1661800923)

  


  


## **Organic Search**

Traffic categorized under __Organic Search__ comes from non-paid search results in known search engines, such as Google, Bing, Yahoo, and Duckduckgo. 

  


To view the keywords used in the search engine, click the Organic search source in the Sources table. 

When there are Unknown keywords (SSL), it is likely due to the search engine encrypting user data. For example, Google encrypts all the search terms entered by their users.

  


  


## **Social Media**

Traffic categorized under Organic social comes from social media websites or apps. An example is when a visitor shares your content or website on their social media account, and their followers visit your content or visit the links inside your messages on social media.

  


  


## **Referrals**

Traffic categorized under Referrals comes from external sites that link to your website. It should not be a search engine or social media site. A referring domain may have multiple pages that link to your site.

  


  


## **Others**

When a lead is generated through various channels such as incoming calls, SMS, emails, WhatsApp messages, or Facebook messages, it is important to display all the information in one place. This helps keep track of all the leads and ensures that none fall through the cracks. By having a centralized system to manage all the leads, businesses can ensure they are not missing out on potential customers.

  


  


## **CRM UI**

When a lead is created manually through the HighLevel App CRM, its source is defined as this. This categorization helps in identifying leads that were created manually within the HighLevel App CRM only.

  


  


## **Third-Party**

When a lead is created by a third-party tool like Zap, its source is defined as this. This categorization helps identify leads created through third-party integration.

  


* * *

# **What Events Record Attribution?**

Within the same session, a contact must do one or more of the following actions:

  1. Form/Survey Submission
  2. Calendar Booking Submission
  3. Chat Widget (After Submitting Contact Info)
  4. Order Form Submission (One or Two-Step)


  

    
    
    **This action must be a****HighLevel Form, Survey, Calendar, Chat Widget and Order Form in order for all attribution data to be captured**. Non-HighLevel events will not capture attribution data -- this includes UTM Parameter data.

  


* * *

# **How is Attribution Source Determined?**

When you want to understand why a contact attribution source was added by HighLevel to the contact, you need to understand what we look for when determining attribution data.

  


All attribution events follow a set of rules to categorize traffic into a specific source, and we check the full page URL and the referring domain, if available, against these rules.

They are applied in this order:

  


Order| Rule| Source  
---|---|---  
1| The "utm_source" parameter contains the word “adwords” for Google Ad. | Paid Search  
2| The "gclid", "wbraid" or "gbraid" parameter is present, as they are Google click IDs.The "msclkid" parameter is present, it is the Microsoft click ID for Bing/Yahoo| Paid Search  
3| The "utm_source", "utm_medium", or "utm_campaign" parameter is present and the referring domain is google.com.| Paid Search  
4| The "utm_source" parameter contains the word “fb_ad” for Facebook Ad.We have deprecated utm_source=facebook, **please use "fb_ad". The "utm_source" parameter contains the word “linkedin_ad” for Linkedin Ads, "twitter_ad" for Twitter Ads and "reddit_ad" for Reddit. **  
**The "ctwa_clid" is present for whatsapp conversations**|  Paid Social  
5| The referring domain is a social media site. | Social Media  
6| Referring domain is a search engine. (Google, Yahoo, Bing, Duckduckgo)| Organic Search  
7| Referring domain is not a social media site or search engine.| Referral  
8| No referring domain or tracking URL.| Direct Traffic  
9| This shows up if the lead came from an Incoming Call/SMS/Email/WhatsApp/Facebook message or any other source not covered above.| Others  
10| Lead is manually created within the CRM system | CRM UI  
  
11| Lead is generated from a third-party integration tool like Zap | Third-Party  
  
  
  


Now that we can see how HighLevel chooses to apply a specific attribution source, let's walk through each attribution source together.

  


* * *

# **Ad Reporting Setup**

When you need to set up your Paid Ads attribution tracking, please see the following documentation for Facebook, Instagram, and Google Ads Set Up.

  


## Facebook and Instagram Ads Reporting Setup

To set up Facebook and Instagram ads attribution, please visit [](<https://help.gohighlevel.com/support/solutions/articles/48001204042-how-to-set-up-facebook-ad-reporting>)[Facebook Ad Reporting Setup](<https://help.gohighlevel.com/support/solutions/articles/48001204042-how-to-set-up-facebook-ad-reporting>).

  


_Additional Facebook Ads Resources_

[How to set up a Funnel Event Pixel for Facebook Conversion API ](<https://help.gohighlevel.com/support/solutions/articles/48001236281-how-to-set-up-a-funnel-event-pixel-for-facebook-conversion-api->)

[How to set up and install a Meta Pixel ](<https://www.facebook.com/business/help/952192354843755?id=1205376682832142>)

[Facebook Conversion Leads Walkthrough ](<https://help.gohighlevel.com/support/solutions/articles/48001233833-facebook-conversion-leads-walkthrough>)

[Facebook Conversions API Trigger in Workflows](<https://help.gohighlevel.com/support/solutions/articles/48001185099-facebook-conversions-api-trigger-in-workflows>)

[](<https://www.facebook.com/business/help/2360940870872492>)

  


  


## Google Ads Reporting Setup

To set up Google Ads Attribution, please visit [Google Ad Reporting Setup](<https://help.gohighlevel.com/support/solutions/articles/48001219312-how-to-set-up-google-ad-reporting>).[](<https://support.google.com/google-ads/answer/6305348?hl=en-GB&sjid=16240213768626225606-NC#zippy=%2Cfinal-url-tracking-template-or-custom-parameter>)

  


_Additional Google Ads Resources_

[Google Analytics 4 Tracking ](<https://help.gohighlevel.com/support/solutions/articles/48001234199-google-analytics-4-tracking>)

[Understanding Google Ad Reporting Terminology ](<https://help.gohighlevel.com/support/solutions/articles/48001219241-understanding-google-ad-reporting-terminology>)

[Troubleshoot Guide For Google Ad Reporting](<https://help.gohighlevel.com/support/solutions/articles/48001219996-troubleshoot-guide-for-google-ad-reporting>)

  


For any additional assistance, you can contact us 24/7. In addition, please note you may need to consult an ad specialist for more advanced reporting and attribution setup for external reporting and attribution tracking.

  


* * *

# **Troubleshooting Ad Reporting Issues**

If your attribution data is not being recorded in HighLevel after you have set up your [Facebook or Instagram Ad Reporting](<https://help.gohighlevel.com/support/solutions/articles/48001204042-how-to-set-up-facebook-ad-reporting>) or your [Google Ad Reporting](<https://help.gohighlevel.com/support/solutions/articles/48001219312-how-to-set-up-google-ad-reporting>), we can try the following troubleshooting steps to fix this...

  


  1. **Check for Spaces or Misspellings in the Final URL**

When creating your UTM parameters, be sure to check for any misspellings, extra spaces from copying, or case sensitivity. The examples provided should be used, it is best to copy and paste them. Take a moment to confirm it was done correctly. Also, the examples are case sensitive, meaning an upper case or lower case being present where it shouldn't be will cause errors in attribution.  
  


Final URL = The URL a contact clicks on from their ad, which takes them to where they take the next action on your site or form.  
  


  2. **Confirm that Submissions Happen on the Final URL  
** For the UTM parameters to be recorded, when a user lands from an ad they cannot move from this page. For example, if someone lands on a page and then clicks a button that moves them to another page to submit a form, no attribution data from URMs can be added. So we need to keep them on this page when they fill out the form.  
  
A workaround would be to add a pop-up or a section with the submission form to ensure the data is captured.  
  


  3. **Do NOT add any custom UTM parameters to Facebook, Instagram, or Google Ads. Please be sure to use our HighLevel UTM templates as instructed in the setup directions.**  
Please do not add custom UTM parameters to the templated examples provided in the setup guides. This could cause issues and may result in missing data or failure to record any data.

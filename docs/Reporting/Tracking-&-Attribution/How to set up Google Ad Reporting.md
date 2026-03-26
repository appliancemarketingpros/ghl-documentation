# How to set up Google Ad Reporting

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001219312-how-to-set-up-google-ad-reporting](https://help.gohighlevel.com/support/solutions/articles/48001219312-how-to-set-up-google-ad-reporting)  
**Category:** Reporting  
**Folder:** Tracking & Attribution

---

Google Ad reporting provides live reporting and analysis for your client's digital ad campaigns. Here are a few must-have setup guidelines for Google Ad Reporting.

  


**Covered in this article:**

**Step 1 -** Choose the correct Google Ad Account in Integrations

**Step 2 -** Select the correct MCC Account Id and Client Account ID

**Step 3 -** Add the UTM Template to the Google Ad Account 

  * Example


**Step 4:** Adding Script for Precautionary Measures (See Help Doc)

  
**Here are some important things to keep in mind:**

  


* * *

## **Step 1 - Choose the correct Google Ad Account in Integrations**

The user who has the connected google account should have the maximum permissions as a user [(administrator)](<https://support.google.com/admanager/answer/177403>) or [google ad account manager access](<https://support.google.com/google-ads/answer/6139186#MCC_invite>).

  
  
  


## **Step 2 - Select the correct MCC Account Id and Client Account ID**

MCC account stands for My Client Centre, it is also commonly known as Google Ads Manager Account, managing multiple clients' Google Ad accounts.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48241723515/original/cpKfLamkhGxOwB2benWY2aBbeModkz311w.png?1659031538)

###   


### **MCC id is present in the top right corner.**

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48248202783/original/2kB4rlhnXyUOvhwIOf5AADT7gZ7J91IbsQ.png?1661885519)

  


  


  


### **Client Account id is present on clicking the help section**

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48241724794/original/41FtCevRGsKvW2aJupKjPEfYRnjb_h9fcA.png?1659031996)

  


  


* * *

## **Step 3 - Add the UTM Template to the Google Ad Account**

The UTM tracking template can be added to three places. It can be added at Account Settings, Campaign Settings, or ad group level. We would recommend adding the UTM Template at Account level Settings. 

###   
**UTM Tracking Template _(Copy this)_**

{lpurl}?utm_source=adwords&utm_medium={adname}&utm_campaign={campaignname}&utm_content={adgroupname}&utm_keyword={keyword}&utm_matchtype={matchtype}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}

  


###   
**How it works**

Tracking templates must include a [ValueTrack parameter](<https://support.google.com/google-ads/answer/6305348?hl=en#urlinsertion>) that inserts your final URL, like {lpurl}. 

  


Once your ad is clicked, these parameters will insert your final URL. If you don’t include a URL insertion parameter in your tracking template, **_your landing page URL will break_**.

  


If you want to add more than one [ValueTrack parameter](<https://support.google.com/google-ads/answer/6305348?hl=en#urlinsertion>) to a single URL, simply append them together in your URL using an _ampersand ( &)_, like this: **{lpurl}****?matchtype={matchtype} &device={device}.**

  


Set up or edit a tracking template with ValueTrack parameters at the campaign, Ad group, and or Ads and Extension level - [Follow this article](<https://support.google.com/google-ads/answer/6305348?hl=en#zippy=%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-ad-group-level%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-ads-extensions-level%2Cfinal-url-tracking-template-or-custom-parameter%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-sitelink-level>)[](<https://support.google.com/google-ads/answer/6305348?hl=en#zippy=%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-ad-group-level%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-ads-extensions-level%2Cfinal-url-tracking-template-or-custom-parameter%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-sitelink-level>)

##   
**Example**

### **Final URL:** <http://example.com>

  


** _Tracking template:_** {lpurl}?utm_source=adwords&utm_medium={adname}&utm_campaign={campaignname}&utm_content={adgroupname}&utm_keyword={keyword}&utm_matchtype={matchtype}&campaign_id={campaignid}&ad_group_id={adgroupid}&ad_id={creative}

  


  


**_Landing page URL after clicking ads:_**

{lpurl}?utm_source=adwords&utm_medium=black_friday&utm_campaign=blackday10&utm_content=marketingbanner&utm_keyword=getdiscounteddeal&utm_matchtype=e&campaign_id=12345&ad_group_id=2394984903&ad_id=93844980940&gclid=84843ewhfb834nedhj4u49

### [ ](<http://example.com?utm_source=adwords&utm_medium={AgencyBlackFriday}>)

### [](<https://support.google.com/google-ads/answer/6305348?hl=en#zippy=%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-ad-group-level%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-ads-extensions-level%2Cfinal-url-tracking-template-or-custom-parameter%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-sitelink-level>)**[](<https://support.google.com/google-ads/answer/6305348?hl=en#zippy=%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-ad-group-level%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-ads-extensions-level%2Cfinal-url-tracking-template-or-custom-parameter%2Cset-up-or-edit-a-tracking-template-with-valuetrack-parameters-at-the-sitelink-level>)**

### Go to Your**Google Ads Account** > **Account Settings** > **Tracking** (See image below)

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48241751601/original/EXs2wVlSlNDgpnZygMVfKqT4A5Kzxz5wAw.png?1659042898)

  


###   
Paste the Tracking Template URL from above in the "**Tracking template** " field below.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48241751703/original/FzN2NCdQqsIInlAJVnvV2WbbdMb1WoWbRA.png?1659042970)

  
**Please Note:**
    
    
    - After adding the tracking template,  _**please run a test**_ and you will see that the majority of the campaigns should show that the landing page is found. If there are any errors, please rectify them if they are active campaigns.  
      
    - Earlier, UTM Source was used as Google (utm_source=google). Although it has been depreciated it is the ad blocker used to identify the URL and stripped of the UTM parameters.

  


  


* * *

## **Step 4: Adding Script for Precautionary Measures[(See Help Doc)](<https://help.gohighlevel.com/en/support/solutions/articles/48001219356>)**

The script is a simple example of how you would set up the Google AdPrecautionary tracking code. The script acts as a fail-safe if the UTM template fails in capturing the attribution data. 

  


It will track all clicks on a particular link and send it to Google Analytics. The only thing that needs to be changed in this script is the URL for the tracking page, which should match the one used by your website.

  


[**How to set up Google Ad Precautionary Tracking Script**](<https://help.gohighlevel.com/en/support/solutions/articles/48001219356>)

  


  


  


* * *

## **Here are some important things to keep in mind:**

  

    
    
    **1.** Campaign names, Ads, and Ad-set need to be **_unique_**.  
      
    **2.** The name parameters **_can’t be changed during the lifetime of the campaign_** / Ad-set / Ad. If the name has to be changed, then create a new campaign / Ad-set / Ad to avoid any issues.  
      
    **3.** If you decide to change the name of the campaign / Ad-set / Ad and choose**_NOT to_** create a new campaign, then _data in the CRM will keep referring to the original/ first campaign_. [Google Ad provides the old name in the parameter and skews your campaign reporting]
    
    **4.** You will find an Objectives dropdown on the top left , Its purpose is to help define what objective the company had for this Ad campaign when creating it. 
    
    **![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48249248484/original/BVS_7NnRNEQp3b4qJgSWEcs3kymdNOhDkw.png?1662394187)**

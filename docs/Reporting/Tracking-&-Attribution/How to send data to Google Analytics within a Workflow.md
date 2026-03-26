# How to send data to Google Analytics within a Workflow

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001223243-how-to-send-data-to-google-analytics-within-a-workflow](https://help.gohighlevel.com/support/solutions/articles/48001223243-how-to-send-data-to-google-analytics-within-a-workflow)  
**Category:** Reporting  
**Folder:** Tracking & Attribution

---

It is easy to set up the workflow with Google Analytics triggers. The "Google Analytics" event trigger will require you to add the following parameters in a workflow. This technique is used when you want to track more than the page view/visit of the user, you would like to track specific events like submission of the form, user optin or support calls, etc.

  


  
[Difference between GA4 and UA property](<https://support.google.com/analytics/answer/11986666?hl=en#zippy=%2Cin-this-article>)

  


  


* * *

## How to Find Tracking ID in Google Analytics

  


**For UA Property -**

  1. Open Google Analytics
  2. Click the ‘**Admin** ’ tab
  3. In the left-hand column, click '**Tracking Info** '
  4. Click ‘**Tracking Code** ’
  5. Your code will be available here. For Universal Analytics users, the codes start with “**UA.** ”


  


**For GA4 Property -**

  1. Open Google Analytics
  2. Click the ‘**Admin** ’ tab
  3. In the left-hand column, click '**Property Settings** '
  4. Click '**Property ID** '
  5. Your code will be available here. For Google Analytics 4 users, the codes will be a number.


  


##   


* * *

## How does it work?

  
When a user selects the option in trigger or action as add to google analytics. Here's the new set of fields that will visible. 

  * Tracking id/property id
  * Event Category 
  * Event Action
  * Event label
  * Event value


  


For example - Event Category is Form Submission, Action is Exit Form Opt in and Label is Back Friday form submission. These things can be set with dynamic values with small icon tags.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48255298205/original/JWpX4aSQucOUmvCdoyaTbe1uTLj9BAn9vw.jpeg?1665087756)

  *   


We follow a set of rules to categorize traffic into a specific source, and check the full page URL and the referring domain, if available, against these rules. The details about rules and sources for tracking are given in the table below. 

  


  
**Please Note:**
    
    
    If you have set both utm_medium and utm_source, we will use them and if any one of them is not available, we will categorize them according to the below-given table.
    
    We pass gclid (Google Click Identifier) to recognize each unique click.

  


  


**Attribute**| **Rules**| **utm_medium**| **utm_source**  
---|---|---|---  
Google Organic| Referring domain is the Google search engine.| organic  
  
| Google  
Paid Search  
| If the utm_source is google and the referring domain is google.com.| CPC  
  
| Google  
Facebook| facebook.com| referral| Facebook  
Paid Social| The "utm_medium" parameter contains "cpc" where utm_source is facebook.com| CPC| Facebook  
Direct Traffic or Bookmarked| When there are no referring domains or tracking URLs.| none  
  
| direct  
Referral| example.com| referral| example.com  
Social Media| Referring domain is a social media site like   
Facebook, Instagram, Youtube, credit, Twitter, Naver, Pinterest| social  
  
| Social Referring Site  
Display Traffic| example.com| cmp, banner, display| example.com  
  
  


  


  


  


  


  


  


* * *

# **FAQ**

  


  1. #### **What is the difference between Universal Analytics and Google Analytics 4?**


Please see this article for more info -[ https://support.google.com/analytics/answer/9964640?hl=en#zippy=%2Cin-this-article](<%20https%3A//support.google.com/analytics/answer/9964640?hl=en#zippy=,in-this-article>)

  


####   
**How to find the Category, action, and label in GA4?**

A Universal Analytics event has a Category, Action, and Label and is its own hit type. In Google Analytics 4 properties, every "hit" is an event; there is no distinction between hit types. For example, when someone views one of your website pages, a page_view event is triggered. 

  
Google Analytics 4 events have no notion of Category, Action, and Label and, unlike Universal Analytics reports, Google Analytics 4 reports do not display Category, Action, and Label. Therefore, it’s better to rethink your data collection in terms of the Google Analytics 4 model rather than port your existing event structure to Google Analytics 4.

####   
  
**How to find in GA4 if the setup is working or not?**

Please go to Google Analytics, and visit the GA4 property. In the navigation, please go to Reporting > Acquisition Reports. If the setup is done correctly, it will show up here and we would say add filters of source and medium (marked in red).

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48255298206/original/x2CxeoFrIDUpxT_My_liS1jTU-k_yj5hnQ.jpeg?1665087756)

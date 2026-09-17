# RSS Blocks In Email Builder

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001201780-rss-blocks-in-email-builder](https://help.gohighlevel.com/support/solutions/articles/48001201780-rss-blocks-in-email-builder)  
**Category:** Marketing  
**Folder:** RSS Guide

---

**TABLE OF CONTENTS**

  * Overview
  * Usage
    * RSS Header
      * Basic Vs Custom in RSS Header 
    * RSS Items
      * Basic Vs Custom in RSS Items 
    * HTML Based RSS Feed
    * Scheduling:
      * Sending Options:
    * Testing RSS Emails
    * View and Edit RSS Campaign


#   
**Overview**

The RSS Elements in the HighLevel Email Builder allow you to automatically send emails containing dynamically inserted content when a new RSS (Real Simple Syndication) item is published. 

# **Usage**

## RSS Header

  


## ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855351/original/vkt1WTZi4swPcywq_8ebw7FWUejefs3UTQ.png?1636131879)

**RSS Header Block**

  


This will dynamically populate <channel> tags from your RSS Feed ([learn more about the <channel> tag here](<http://www.landofcode.com/rss-tutorials/rss-channels.php>)). The RSS Header Element supports the following RSS channel tags - use their respective Custom Value to populate the email with the corresponding tag value:

  


**RSS Tags**| **Custom Value For HL**  
---|---  
<title>| {{rss_feed.title}}  
<description>| {{rss_feed.description}}  
<link>| {{rss_feed.url}}  
<lastBuildDate>| {{rss_feed.date}}  
  
### Basic Vs Custom in RSS Header 

  


When using the RSS Header block, you'll see two options in the "RSS Editing Options" dropdown selector: Basic and Custom.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855348/original/TXhqhCn_ybN6lz8F_4U1No7-vaLkA_Sj1w.png?1636131878)

  


  


  * **Basic** : adds the following non-editable text in Text Editor


    
    
        <h1 class="h1">{{rss_feed.title}}</h1>    {{rss_feed.description}}<br />    <br />

  *   

    * **Custom:** adds the following editable text in Text Editor


    
    
        Updates from {{rss_feed.url}}    <h1>{{rss_feed.title}}</h1>    <strong>{{rss_feed.description}}</strong><br />    <br />    <strong>In the {{rss_feed.date}} edition:</strong><br />

NOTE: The four custom RSS <channel> variables can also be used in the subject field like this: ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855344/original/c2Vi4rUtLOvx56OiuS-hfAmtJXBuLF2hng.png?1636131877)

## RSS Items

  


**RSS Items Block**

  


The RSS Items block accepts the following Custom Values and will dynamically insert their corresponding RSS Tags:

  


**RSS Tags**| **Custom Values**| **Description**  
---|---|---  
<title/>| {{rss_item.title}}| The title of the RSS item, usually a blog post.title  
<description/>| {{rss_item.content}}| A summary of the RSS item in HTML format, which includes information inside the <description> tag. If there is no <description> tag in your feed, it will display the information in the <content:encoded> tag  
<link/>| {{rss_item.url}}| The text link to the RSS item online, which can be displayed as text or used in a hyperlink.content:encoded  
<content:encoded/>| {{rss_item.content_full}| The full content of the information inside the <content:encoded> tag for an RSS item, in HTML format. If there is no <content:encoded> tag, it will display the information in the <description> tag.  
pubDate| {{rss_item.date}}| The date the RSS item was published, in format `MMM DD, YYYY hh:mm A`. We will provide support for custom formatting in the future.  
<dc:creator>| {{rss_item.author}}| The author of the RSS itemmedia:content  
<media:content>| {{rss_item.imageUrl }}| This will provide the src URL of image as text in order to render it as image, use {{rss_img}} {{rss_img alt="alt_text" src=rss_item.imageUrl height="200" width="200"}}  
<item>| {{#rss_items rss_items}}| This tag doesn't display anything. It's used to open the customized formatting for individual RSS items.  
</item>| {{/rss_items}}| This tag doesn't display anything. It's used to close the customized formatting for individual RSS items.  
  
### Basic Vs Custom in RSS Items 

  


When using the RSS Items block, you'll see two options in the "RSS Editing Options" dropdown selector: Basic and Custom.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855347/original/L0LyUj9IorHU0sZYjFppVorh01rAx3ll6A.png?1636131878)

  *   

    * **Basic** : adds the following non editable formatted text in Text Editor


    
    
              {{#rss_items rss_items}}      <h2 class="mc-toc-title"><a href="{{rss_item.url}}" target="_blank">   {{rss_item.title}}      </a> </h2>      {{rss_item.content}}      <br />      <a href="{{rss_item.url}}" target="_blank">Read on &raquo;</a><br />      <br />     {{/rss_items}}

  *   

    * **Custom:** adds the following formatted text and Text editor will become editable 


    
    
        {{#rss_items rss_items}}    <h2 class="mc-toc-title"><a href="{{rss_item.url}}" target="_blank">{{rss_item.title}}</a></h2>    <em>By {{rss_item.author}} on {{rss_item.date}}</em><br />    {{rss_item.content_full}}<br />    <a href="{{rss_item.url}}" target="_blank">Read in browser &raquo;</a><br />    <br />    {{/rss_items}}<br />    <br />    <br />    <h3 class="h3">Recent Articles:</h3>   {{#rss_items rss_items}}

## HTML Based RSS Feed

The values returned by the RSS-based custom variable `{{rss_item.title}}` are HTML-escaped. For example, if the expression contains `&`, then the returned HTML-escaped output is generated as `&amp;` or if your RSS Feed has HTML-based text instead of plain text then it will be rendered as plain text.

If you don't want it to escape a value, use the "triple-stash", `{{{`:

Eg: if your RSS feed source is something like this

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855360/original/uPxMn189zEmr7WCh_6qYv6DAQ_WrxdccDA.png?1636131880)

without "triple-stash" it will render like this

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855357/original/78KNj092LUO9cZRouzUlv84qXhEsZtHv3g.png?1636131879)

once you will use "triple-stash" `{{{rss_item.content}}}` it will render like this

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855364/original/BojThSBQRv2EsNKXzmCAgxdVL1HDID98HA.png?1636131880)

## 

## Scheduling:

  


To schedule RSS Feed based emails:

  * navigate to the "Send or Schedule" tab
  * select the "RSS Email Campaign" sending option
  * give your campaign a name in the "Campaign Name" field
  * paste your RSS feed url in the "RSS Feed URL" field. 


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855359/original/SpMiwm3Uo4icKGEWl86NUztsGxQIVOojtg.png?1636131880)

### Sending Options:

  


  * **"When we should send":** Here you can determine whether RSS Emails should go out Daily, Weekly, or Monthly as well as at what time the emails should go out.
  * **Send on:** Here you can choose the Day(s) of the week on which you want to send the campaign


Once all inputs fields filled along with the recipient, in Review and Send side panel You will see following new information

  *   

    * Email type
    * RSS Feed URL
    * Repeat After
    *     * ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855354/original/MU4iPH7O-wwTKti8UnJOm1i-OjBLL0oviw.png?1636131879)


## Testing RSS Emails

  


When using the "Send Test Email" functionality with an email that has RSS Elements, you will see a new "**RSS Feed URL"** field where you'll need to provide the RSS Feed URL from where you want to pull the content. Without this, all RSS tag based custom variables will replace by empty text.

  * ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855353/original/ngePuhb-X4mSVnHZA5POqiWBBo9VYF65NQ.png?1636131879)


NOTE: If you try to Schedule RSS Element based email template through normal scheduling options (send now, schedule for later, send in drip mode), all RSS tags based custom variable will replace by empty text.

## View and Edit RSS Campaign:

  


You can see your scheduled RSS Campaigns in the Scheduled Tab, where you'll see the type listed as RSS. For other scheduled emails (send now, schedule for later, send in drip mode), the type will be Normal.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855356/original/8LsOBEXvUvsrD9m6DAUbFnIGnga6WRbVDQ.png?1636131879)

The example above is an RSS email set to send Daily and we can see the Next Execution time will be at 2 pm. Once the 2 pm email has been sent, it will be marked as complete and a new scheduling/execution will be scheduled with the same configuration (RSS Feed URL, send Daily) with the following day's date.

### 

### Actions:

  


With RSS type scheduling you can perform the following actions:

  * **Edit:** If you click the pencil icon to edit, you will see a confirmation modal asking you to confirm that you would like to cancel the currently scheduled email and re-schedule a new one.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855352/original/o--HIRT2KbBv-OrhGrqfaPrTLEZw1T2Wsw.png?1636131879)


  


  * Once you click Confirm, it will cancel the current scheduling and open up a Email Builder with RSS Scheduling options pre-filled with the current cancelled scheduling information![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48155855361/original/-VqGcwC_5HX3QI-gngmW-H9NmIDY_i7yWg.png?1636131880)


  


  * **Pause/Resume:** You can also pause and resume the execution through the Pause/Resume actions
  * **Delete:** You can also delete the RSS scheduling. Deleting will first cancel the scheduling then delete it permanently from the system

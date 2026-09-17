# A basic guide of RSS Campaign

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004928-a-basic-guide-of-rss-campaign](https://help.gohighlevel.com/support/solutions/articles/155000004928-a-basic-guide-of-rss-campaign)  
**Category:** Marketing  
**Folder:** RSS Guide

---

In HighLevel, you can include an RSS feed (Item and Header) in your direct and automated campaigns using the RSS content block. This allows your subscribers to automatically receive and read updates from online content sources, like blog posts and news articles

##   
**How does an RSS Campaign work?**

  


You can insert an RSS item or header element and add your RSS feed URL in the send or schedule section. All feed updates published between the time you schedule the campaign and when the email is sent will be included. You can customise the feed layout by selecting the tags you want to display from the feed.  
  
**Usual RSS Items**  
When you add an RSS Element, depending on what all details are present in your feed, you can use the respective custom values in the builder and it would automatically get the relevant data.  
For Example, if you wish to add blog title and content only,  
  
Step 1: Add a RSS header to your template

Step 2: Ensure we have {{rss_item.title}} and {{rss_item.content}}. Depending on what field is needed, add the respective custom values  
Step 3: In your send or schedule section add your RSS URL

Step 4: Schedule your campaign  
  
**Behaviour:** When the campaign is sent, in the template the contact can see all blog titles and content from the day it was scheduled

  


##   
  
**Details about the RSS header and item block**  
  
**What is RSS header?**

This will dynamically populate <channel> tags from your RSS Feed . The RSS Header Element supports the following RSS channel tags - use their respective Custom Value to populate the email with the corresponding tag value:

**RSS Tags**| **Custom Value For HL**  
---|---  
<title>| {{rss_feed.title}}  
<description>| {{rss_feed.description}}  
<link>| {{rss_feed.url}}  
<lastBuildDate>| {{rss_feed.date}}  
  


  
**What is RSS Items Block?**

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
  
##   
**How to send a RSS Campaign?**  
  
**1.****Find Your RSS Feed URL**

  * Look for the RSS icon in the site’s footer or sidebar.

  * View the page source and search for `rss` or `xml`.

  * Try common endings like `/feed`, `/rss`, or `/rss.xml`.

  * Use a browser extension or tools like Feedbucket or CtrlQ to detect the feed.


  


### **2.****Enter the RSS URL**

Go to **Send or Schedule → RSS Campaign** and paste your feed URL.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044064262/original/ZNtVQGvrlt2DDSMYM4nOzSPPEODXe1wULg.png?1743061150)

### **3.****Add RSS Content**

In the email builder, insert an **RSS header** or **RSS item** element.

### ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044064296/original/X-oJsYjlONXwwYwFFetlJ5SWeFMk97eHeA.png?1743061209)**4\. Set Custom Values**

Add the necessary custom fields for your RSS tags.

### ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044064334/original/jZdjc8KmvvvMg9RV-Xh1BQNg-qv4NKx1oA.png?1743061238)**5\. Configure Schedule**

  * In **Send or Schedule → RSS Schedule** , set the send time and number of items to include.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044064446/original/CrG6AVKZHoYeLkyUHPKZoFR9UeeM_I6sJw.png?1743061302)

### **6.****Schedule Your Campaign**

  * Review and schedule your RSS campaign.


  
  
**FAQs**  
**1\. How to handle a scenario where description is an HTML content?**

The values returned by the RSS-based custom variable `{{rss_item.title}}` are HTML-escaped. For example, if the expression contains `&`, then the returned HTML-escaped output is generated as `&amp;` or if your RSS Feed has HTML-based text instead of plain text then it will be rendered as plain text.

If you don't want it to escape a value, use the "triple-stash", `{{{`:

Eg: if your RSS feed source is something like this

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044064498/original/053-vudl3uozwzP1Jenv_6x0A937_zBr-g.png?1743061362)

without "triple-stash" it will render like this

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044064499/original/0lJbkcnhpyV1FeCYL-L8f1VWUhGX7TQ5TA.png?1743061362)

once you will use "triple-stash" `{{{rss_item.content}}}` it will render like this

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044064500/original/pgFuMeYnJqPkP0UFa3vHK8k63GH3YNiQjA.png?1743061362)  
  


  


**2\. What content can I expect in the next month RSS Campaign?**  
  
If you have created the campaign on March 10th and scheduled it for March 25th, all blog posts after March 10 would be part of the campaign on March 25th.   
If you want to limit the number of posts, in the send or schedule give the maximum number of feeds. If a user specifies "5", we will show most recent 5 blogs in the campaign.   
  
**3\. What will happen if I have no blogs after the RSS campaign was scheduled.**  
In the next cycle, no campaign would be sent. You can review the same from audit log where you can find an entry of unsuccessful schedule due to no new feeds.

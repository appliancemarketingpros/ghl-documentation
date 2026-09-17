# URL Parameters in Websites and Funnels

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005722-url-parameters-in-websites-and-funnels](https://help.gohighlevel.com/support/solutions/articles/155000005722-url-parameters-in-websites-and-funnels)  
**Category:** Sites  
**Folder:** Funnels and Websites

---

Funnels, Websites, Stores & Webinars

URL Parameters in Funnels, Websites, Stores & Webinars

Personalize page content with values passed through a page URL. HighLevel now provides a native URL Parameter option in the Custom Value Picker with default values, text transformations, separator normalization, and visual tokens in the builder.

What You'll Learn

Learn how to insert URL Parameters through the Custom Value Picker, add fallback text, format incoming values, reuse parameters across supported elements, and pass dynamic values through links. The native workflow removes the need to manually type URL-parameter syntax when creating new dynamic page content.

Table of Contents

  1. What are URL Parameters?
  2. Key Benefits of URL Parameters
  3. Supported Builders and Elements
  4. How to Set Up URL Parameters
  5. Set a Default Value
  6. Format URL Parameter Text
  7. URL Parameter Behavior
  8. URL Parameters in Links
  9. Frequently Asked Questions
  10. Related Articles


# What are URL Parameters?  
  


URL Parameters are key-value pairs added to a page URL that can pass information into the page. HighLevel can use these values to dynamically personalize supported page content for each visitor.

For example, if a page is opened with:

`https://example.com/offer?city=Austin`

A URL Parameter configured with the name `city` can display **Austin** directly in the page content. The native Custom Value Picker lets you configure this without manually entering template syntax.

## Key Benefits of URL Parameters  
  


The native URL Parameter workflow makes dynamic text easier to configure and provides more control over what visitors see when URL data is incomplete or inconsistently formatted.

  * **No-Code Setup:** Insert and configure URL Parameters directly from the Custom Value Picker.
  * **Default Values:** Display fallback content when a parameter is missing or empty.
  * **Text Formatting:** Apply UPPERCASE, lowercase, Title Case, or Sentence case to incoming values.
  * **Cleaner Display:** Hyphens and underscores in incoming values are automatically converted to spaces.
  * **Broader Coverage:** Use URL Parameters across supported text areas, including button text and sub-text.
  * **Safe Rendering:** Incoming parameter values are sanitized before they are displayed on the page.


## Supported Builders and Elements  
  


URL Parameters can be inserted into supported text areas throughout HighLevel's page-building experiences, allowing the same personalization workflow to be used across different types of customer-facing pages.

Supported Builders| Supported Text Areas  
---|---  
  
  * Funnels
  * Websites
  * Stores
  * Webinars

| 

  * Button text
  * Button sub-text
  * Headings
  * Paragraphs
  * Rich text
  * Bullet lists
  * FAQs
  * Popups

  
  
## How to Set Up URL Parameters  
  


Configuring URL Parameters through the Custom Value Picker keeps the parameter name, fallback content, and formatting rules attached to the token itself. This makes dynamic content easier to build and edit without manually managing URL-parameter syntax.

Step 1

Open the Page Builder

Open the Funnel, Website, Store, or Webinar page you want to personalize, then edit a supported text element or button.

Step 2

Select URL Parameter

Open the **Custom Value Picker** , then select **URL Parameter**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080759323/original/3uZbFKa-tDeY1ho2rzxX2_9-h18tPkPzSA.png?1789170429)

Step 3

Configure the Parameter

Enter the **parameter name** , configure a **default value** if needed, and optionally select a **text transformation**.

Step 4

Insert and Edit the Token

Insert the URL Parameter into the element. The parameter appears as a visual token in the editor instead of raw template syntax. Select the token whenever you need to update its settings.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080759248/original/RI1dElWE3eLWjixNkFS4vXRiqWVDIpmd8Q.png?1789170233)

Step 5

Save, Publish, and Test

Save and publish the page, then open it with the matching parameter in the URL.

For example, opening `?city=Austin` causes a token configured for `city` to display **Austin**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080759250/original/5SN33iyr6pgtjikSectG7Iy6bvK2JLqbnw.png?1789170252)

## Set a Default Value  
  


A default value controls what visitors see when the expected URL Parameter is missing or contains no value. This prevents dynamic areas from appearing blank.

For example, if a token is configured for `city`, its default is displayed when either of these conditions occurs:

  * The URL does not contain a `city` parameter.
  * The URL contains an empty parameter such as `?city=`.


**Good to know:** Default values are configured per token. You can enter fallback text or use an existing Custom Value as the default.

## Format URL Parameter Text  
  


Text transformations let you control the capitalization of incoming URL values without changing the parameter itself. Separator normalization also makes common UTM-style values easier to read.

Transformation| Example  
---|---  
**UPPERCASE**|  DALLAS NOW  
**lowercase**|  dallas now  
**Title Case**|  Dallas Now  
**Sentence case**|  Dallas now  
  
**Separator normalization:** Hyphens and underscores in incoming values are automatically converted to spaces. For example, `emergency-plumber` becomes `emergency plumber`. Applying **Title Case** would display it as **Emergency Plumber**.

## URL Parameter Behavior  
  


Understanding how URL Parameters are matched and rendered helps you build predictable personalization across pages and campaigns.

**Case-insensitive matching:** Parameter names are matched without regard to capitalization. For example, `?City=` and `?city=` can match the same configured parameter.

**Independent token settings:** The same parameter can be used in multiple elements, with a different text transformation configured for each token.

**Missing or empty values:** When a configured parameter is absent or empty, the token displays its configured default value.

**Safe rendering:** Incoming URL Parameter values are sanitized before rendering so visitor-supplied markup is not rendered as page markup.

## URL Parameters in Links  
  


Passing a URL Parameter through a link and displaying that parameter on the destination page are two parts of the same personalization flow. The link supplies the value; the URL Parameter token determines where and how the value appears.

A URL can pass a fixed value:

`https://example.com/page?city=Austin`

You can also use a merge field in a link so the value changes for each contact:

`https://example.com/page?first_name={{contact.first_name}}`

On the destination page, configure a URL Parameter token named `first_name` wherever you want that incoming value to appear.

## Frequently Asked Questions  
  


Q: What happens when a URL Parameter is missing?

The configured default value is displayed. The same behavior applies when the parameter exists in the URL but its value is empty.

Q: Are URL Parameter names case-sensitive?

No. Parameter matching is case-insensitive, so `?City=Austin` and `?city=Austin` can match the same configured parameter.

Q: Can I use the same URL Parameter more than once?

Yes. The same parameter can appear in multiple supported elements, and each token can have its own text transformation.

Q: Can I use a Custom Value as the default?

Yes. A URL Parameter token can use fallback text or an existing Custom Value as its configured default.

Q: What happens to hyphens and underscores in URL values?

Hyphens and underscores are automatically converted to spaces when the parameter value is displayed. You can also apply a capitalization transformation separately.

Q: Can URL Parameters be used in button text?

Yes. The native URL Parameter workflow supports button text and button sub-text in addition to other supported text areas.

### Related Articles

  * [List of Merge Fields](<https://help.gohighlevel.com/support/solutions/articles/48001078171>)
  * [Websites Overview](<https://help.gohighlevel.com/support/solutions/articles/155000001633>)
  * [Complete Guide to Creating Webinars in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000006062-complete-guide-to-creating-webinars-in-highlevel>)
  * [Setting Up an E-Commerce Online Store](<https://help.gohighlevel.com/support/solutions/articles/155000001157-how-to-set-up-an-e-commerce-online-store-websites->)
  * [Save, Draft and Publish Funnels and Websites](<https://help.gohighlevel.com/support/solutions/articles/155000001913>)

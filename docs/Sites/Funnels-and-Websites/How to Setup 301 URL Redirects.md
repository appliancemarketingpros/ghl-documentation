# How to Setup 301 URL Redirects

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001202713-how-to-setup-301-url-redirects](https://help.gohighlevel.com/support/solutions/articles/48001202713-how-to-setup-301-url-redirects)  
**Category:** Sites  
**Folder:** Funnels and Websites

---

A 301 redirect permanently sends visitors and search engines from an old URL to a new destination. In HighLevel, you can create redirects for an entire domain or a specific URL path and send visitors to a custom URL, funnel step, or website page. 

  


This guide explains how to create and manage 301 redirects, when to use them, and how to troubleshoot common redirect issues.

* * *

**TABLE OF CONTENTS**

  * What is a 301 URL Redirect?
  * Key Benefits of 301 URL Redirects
  * When Should You Use a 301 Redirect?
  * How to Set Up 301 Redirects in HighLevel
    * Step 1: Navigate to URL Redirects
    * Step 2: Add a New Redirect
    * Step 3: Select the Source Domain
    * Step 4: Choose What You Want to Redirect
    * Step 5: Select the Redirect Target
  * 301 Redirect vs Canonical URL
  * Best Practices for 301 Redirects
  * Common Issues & Troubleshooting
  * Frequently Asked Questions
  * Related Articles


* * *

## **What is a 301 URL Redirect?**

  


A 301 URL redirect is a permanent redirect from one URL to another. It tells browsers and search engines that the original URL has moved permanently, helping visitors reach the correct page even if they click an old link. In HighLevel, 301 redirects can send traffic from a selected domain or path to a custom URL, funnel step, or website page.

  


A 301 redirect is commonly used when you rename a page, change a funnel or website path, move content to a different destination, or want an old URL to continue working after updates are made.

* * *

## **Key Benefits of 301 URL Redirects**

  


  * **Improved visitor experience:** Sends visitors from old URLs to the correct destination automatically.  
  

  * **Reduced broken links:** Helps prevent 404 errors when pages are renamed, deleted, or moved.  
  

  * **SEO continuity:** Signals to search engines that a URL has permanently moved and helps preserve continuity when URLs are changed.  
  

  * **Domain consolidation:** Redirects traffic from one domain version to another, such as a `www` version to a root domain.  
  

  * **Flexible destination options:** Allows redirects to custom URLs, funnel steps, or website pages in HighLevel. 


* * *

## **When Should You Use a 301 Redirect?**

  


Use a 301 redirect when a URL has permanently changed and visitors should automatically be sent to a new destination.

  


Common scenarios include:

  


  * Renaming a funnel step or website page path  
  

  * Moving content to a different URL  
  

  * Replacing or deleting a page while preserving traffic from existing links  
  

  * Migrating content to another domain  
  

  * Redirecting an old campaign or landing-page URL to a current page  
  

  * Consolidating domain versions when one URL should permanently point to another


  


> **Note:** If multiple URLs should remain accessible but you only want search engines to recognize one as the preferred version, consider using a canonical URL instead of a 301 redirect.

* * *

## **How to Set Up 301 Redirects in HighLevel**

  


Follow these steps to configure 301 redirects for your domains:

  


### **_Step 1:_**_Navigate to URL Redirects_

  


  1. Go to **Settings** > **Domains & URL Redirects**.  
  

  2. At the top of the page, select the **URL Redirects** tab. This opens the redirect management view where you can create, search, edit, or delete redirects.  
  


![](https://jumpshare.com/share/fjz9BYWVCmnfkIqeeTxq+/GIF+Recording+2026-06-18+at+17.19.48.gif)

  


  


### _**Step 2:** Add a New Redirect_

  


  1. Click **\+ Add Redirect** in the top-right corner.  
  


If there are no existing redirects, you may also see an option to add your first redirect from the main redirect screen.  
  


  2. The **Add Redirect** setup window will open.


  


![](https://jumpshare.com/share/BypLYCyFq3lrw5qXbNhi+/GIF+Recording+2026-06-18+at+18.10.26.gif)

  


  


### **_Step 3:_**_Select the Source Domain_

  

    
    
    **Note:** Source domain must already be added to your HighLevel sub-account.

  


  1. Under the **Source** section, click the **Redirect From** dropdown.  
  

  2. Select the domain you want to redirect from.  
  


The dropdown will show the domains currently available in your account.  
  


![](https://jumpshare.com/share/O1tsuhiz8XnXJQShOVwP+/Screenshot+2026-06-18+at+18.11.54.png)  


  


### **_Step 4:_**_Choose What You Want to Redirect_

  


After selecting the source domain, choose whether you want to redirect the entire domain or only a specific path.

  


You can choose one of the following options:

  


**_Option 1:_**_Redirect a Specific Path_

  


Select this option if you only want to redirect one page or path from the domain.

  


For example, if you want to redirect: `yourdomain.com/contact `you would enter the specific path, such as:

`/contact`

  


Use this option for pages like a home page, contact page, thank-you page, or any other individual page.

  

    
    
    **Important : Avoid Special Characters in Redirect Paths**
    
    When creating a redirect for a specific path, do not include special characters such as **?**, **%**, **&**, **=**, or **#** in the redirect path. These characters can prevent the redirect from working as expected.
    
    For the most reliable redirect paths, use clean URL slugs containing **lowercase letters, numbers, hyphens (****-****), and forward slashes (****/****) for supported nested paths**.
    
    
    **Nested paths:** HighLevel supports nested URL paths. When creating redirects for nested pages, enter the complete supported path, such as /resources/guides/getting-started.
    
    
    **Recommended:** /special-offer
    
    **Avoid:** /special?offer=summer&utm_source=email
    
    If your original URL contains query parameters, enter the clean URL **path** rather than including the query string when configuring the redirect.
    

  


**_Option 2:_**_Redirect the Entire Domain_

  


Select this option if you want the whole domain to redirect to another destination.

  


For example, all traffic from: `yourdomain.com `would be redirected to the target you select.

  


![](https://jumpshare.com/share/Ua1jVlxEuUOqaZ5if6BL+/Screen+Shot+2026-06-18+at+18.19.01.png)

  


  


### **_Step 5:_**_Select the Redirect Target_

  


Under the **Target** section, choose where you want visitors to be redirected.

  


You can redirect users to one of the following destination types:

  


_**Option 1:** Custom URL_

  


Use this option if you want to redirect visitors to any external or custom URL.  
  


  1. Select **Custom URL**.  
  

  2. Enter the full destination URL.  
  

  3. Click **Add Redirect**.


  


For example, you can redirect users to a thank-you page, external website, or any other URL.

  


![](https://jumpshare.com/share/DWSZTFL7e5eXxvd35cJR+/GIF+Recording+2026-06-18+at+18.29.10.gif)  


  


**_Option 2:_**_Funnel_

  


Use this option if you want to redirect visitors to a funnel connected to the selected domain.  
  


  1. Select **Funnel**.  
  

  2. Choose the funnel from the dropdown.  
  


Only funnels linked to the selected domain will appear.  
  


  3. Select the funnel step where you want visitors to land.  
  


You can select only one funnel step at a time.  
  


  4. Click **Add Redirect**.  
  


![](https://jumpshare.com/share/3tD1Jh3Xe2dEVvJPDuIP+/GIF+Recording+2026-06-18+at+18.31.06.gif)

  


  


**_Option 3:_**_Website_

  


Use this option if you want to redirect visitors to a website page connected to the selected domain.  
  


  1. Select **Website**.  
  

  2. Choose the website from the dropdown.  
  


Only websites linked to the selected domain will appear.  
  


  3. Select the website page where you want visitors to land.  
  

  4. Click **Add Redirect**.


  


![](https://jumpshare.com/share/ZoRHwjsNLXcQXTCpWTJd+/GIF+Recording+2026-06-18+at+18.33.36.gif)

* * *

## **301 Redirect vs Canonical URL**

  


Use a 301 redirect when the old URL should no longer be used and visitors should automatically reach the new destination. Use a canonical URL when multiple URLs remain accessible but search engines should treat one as the preferred version.

  


Use| 301 Redirect| Canonical URL  
---|---|---  
Visitors should automatically go somewhere else| **Yes**|  No  
Old URL should permanently move to a new URL| **Yes**|  No  
Multiple URLs should remain accessible| No| **Yes**  
Tell search engines which accessible URL is preferred| Indirectly through the move| **Yes**  
Browser URL changes| **Yes**|  No  
  
* * *

## **Best Practices for 301 Redirects**

  


  * **Use absolute URLs** (e.g., https://newsite.com/page) to prevent errors.  
  

  * ****Avoid redirect chains:** **Redirect the original URL directly to the final destination whenever possible. For example, avoid `Page A → Page B → Page C`. Instead, configure `Page A → Page C`.   
  

  * Check for broken redirects regularly to ensure they work properly.   


* * *

## **Common Issues & Troubleshooting**

  


Issue| What to Check  
---|---  
**Redirect isn't working**|  Confirm the source domain is connected and the source path exactly matches the URL being accessed.  
**Redirect loop**|  Make sure the destination does not redirect back to the source URL.  
**404 after changing a page path**|  Confirm a redirect exists from the old path to the new page and that the destination page is published.  
**Funnel isn't available as a target**|  Confirm the funnel is linked to the selected source domain.  
**Website isn't available as a target**|  Confirm the website is linked to the selected source domain.  
**Specific path redirect fails**|  Remove query parameters or unsupported special characters and use the clean URL path.  
**Unexpected redirect behavior**|  Check for other redirects that may affect the same source or destination.  
**Google still shows the old URL**|  Search engines may need time to recrawl the page. Use Google Search Console to inspect/request indexing where appropriate.  
  
* * *

## **Frequently Asked Questions**

  


**Q: What is a 301 redirect?**

A 301 redirect is a permanent redirect from one URL to another. It helps send visitors and search engines to the correct webpage when a URL has changed.

  


  


**Q: Can I edit or delete a redirect after creating it?  
** Yes. Return to **Settings** > **Domains & URL Redirects** > **URL Redirects** to manage existing redirects.

  


  


**Q: Why should I use 301 redirects?**

301 redirects help preserve SEO rankings, prevent broken links, improve the visitor experience, consolidate domain versions, and ensure outdated links still lead to relevant pages.

  


  


**Q: Does the source domain need to be added to HighLevel first?**

Yes. The domain you are redirecting from must already be added to your HighLevel sub-account before you can create a redirect for it.

  


  


**Q: Can I redirect an entire domain?**

Yes. When creating a redirect, you can choose to redirect the entire domain so all traffic from that domain is sent to the selected target destination.

  


  


**Q: Can I redirect only one specific page or path?**

Yes. You can choose to redirect a specific path if you only want one page or URL path to redirect. For example, you can redirect yourdomain.com/test-one by entering the specific path, such as test-one.

  


  


**Q: What target options are available for redirects?**

You can redirect visitors to a Custom URL, a Funnel step, or a Website page. Funnel and website options only show items linked to the selected domain.

  


  


**Q. Should I use a 301 redirect or canonical URL?**

Use a 301 redirect when visitors should permanently move from an old URL to a new destination. Use a canonical URL when multiple URLs remain accessible but one should be treated as the preferred version by search engines. 

  


  


**Q. Should I create a redirect after changing a funnel or website page path?**

Yes, if the previous URL was already being used. A redirect helps visitors using old links reach the new page and avoids sending them to an unavailable URL. HighLevel's nested-path documentation specifically recommends adding a 301 redirect after changing a live URL.

  


  


**Q: Why is my funnel or website not showing in the redirect target dropdown?**

Funnels and Websites that are linked with a domain are only listed.

  


  


**Q: What can cause redirect issues?**

Common issues include redirect loops, 404 errors, and slow load times. To avoid these, make sure you are not redirecting a URL to itself, confirm the target page exists, and avoid using too many redirects.

  


  


**Q: What are some best practices for setting up 301 redirects?**

Use absolute URLs, avoid redirect chains, check for broken redirects regularly, and use REGEX redirects carefully to prevent incorrect redirects.

* * *

### **Related Articles**

  


  * [Troubleshooting URL Indexing Issues in Funnels](<https://help.gohighlevel.com/en/support/solutions/articles/155000004789>)  
  

  * [Nested URL Paths Support for Websites, Funnels, Ecomm & Webinars](<https://help.gohighlevel.com/en/support/solutions/articles/155000005779>)  
  

  * [How to Add a Domain and Verify DNS Record](<https://help.gohighlevel.com/en/support/solutions/articles/155000002220>)

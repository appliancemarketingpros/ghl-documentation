# How do I find my Client's Location ID?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001204848-how-do-i-find-my-client-s-location-id-](https://help.gohighlevel.com/support/solutions/articles/48001204848-how-do-i-find-my-client-s-location-id-)  
**Category:** Settings  
**Folder:** Sub-Account Settings

---

When you interact with our support teams, they may request you to provide a Location ID for the sub-account where you are experiencing a problem.

  


A **Location ID** is a unique ID assigned to every sub-account in your agency account. It helps our support teams identify the correct client account and narrow down troubleshooting efforts.  
  


## 
    
    
    **Important:** Please do not share the Location ID outside of your organization.
    

* * *

## **Option 1: From Business Profile**

  


To locate the Location ID:  
  


  1. From the **Sub-Account Dashboard** , go to **Settings** in the lower-right corner.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078226830/original/vFmhdAGTs8c3mtvtowfppcHwAkE67MrIcw.png?1786532580)  
  


  2. Select **Business Profile** from the left-side navigation menu.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078226892/original/2VDcANkAXnqU7VoLZ4W0bVwv-S1ouzutrQ.png?1786532632)  
  


  3. Locate the **Location ID** displayed on the Business Profile page.  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078226914/original/HntdJSGsxOwT6tn-aBPli1pFGs2mjIi11Q.png?1786532661)  


  


This is the most reliable method for finding and verifying the Location ID for a specific sub-account.

* * *

## **Option 2: From the URL**

  


If you are already inside the client's sub-account, you may be able to quickly find the Location ID in your browser's address bar.  
  


  1. Open the client's sub-account.  
  


  2. Look at the URL in your browser.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078227077/original/agdRKaeJD21eSFvVhb4AHYwtx48XEOrqkg.png?1786532750)  
  


  3. Find the value that appears after `/location/` or in the `locationId=` parameter.  
  


  4. That value is the **Location ID**.


  


**Example:**

  


`https://app.../v2/location/abc123XYZ/dashboard`

  


In this example, `abc123XYZ` is the Location ID.  
  


> **Tip:** Finding the Location ID from the URL can be the fastest method when the URL contains `/location/` or a `locationId=` parameter.

* * *

## **What if the Location ID isn't visible in the URL?**

  


Some HighLevel pages may not display the Location ID in the browser URL. For example, you may be viewing an agency-level page or another page whose URL does not contain the sub-account's Location ID.

  


If you don't see `/location/` or `locationId=` in the URL:  
  


  1. Make sure you have opened the correct **sub-account**.  
  


  2. Go to **Settings → Business Profile**.  
  


  3. Find the **Location ID** displayed on the Business Profile page.


  


Use the Location ID shown under **Business Profile** to verify that you have the correct identifier.

* * *

## **Location ID vs. Other dentifiers**

  


The Location ID identifies a specific sub-account in your agency account. Do not confuse the Location ID with other identifiers you may encounter in HighLevel, such as an Agency ID, User ID, or other account-related IDs.

  


If you're unsure which ID to provide, navigate to the relevant sub-account and use the Location ID displayed under Settings → Business Profile.

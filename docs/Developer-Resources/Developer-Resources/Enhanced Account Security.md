# Enhanced Account Security

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002545-enhanced-account-security](https://help.gohighlevel.com/support/solutions/articles/155000002545-enhanced-account-security)  
**Category:** Developer Resources  
**Folder:** Developer Resources

---

We’ve rolled out a new security update to keep your data safer than ever!

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155034345888/original/4BHSSG3Nx3UB57D_SZGBk9bU54xXrf8SRA.jpeg?1728418263)

  

    
    
    The enhanced security option does not restore API key generation for locations where it was previously revoked. It only applies to locations that still have an active API key.

  


**  
**

### **Enabling Enhanced Account Security will:**

  


  1. Disable Auto-generation of Location API keys: To enhance account security, API keys will not be automatically generated when you create a new location via API or our user interface (UI). Instead, you will need to generate them manually through the UI. 


  


  2. Exclude API Keys in Location CRUD APIs: Previously, you could access API keys via the Location CRUD APIs responses. Going forward, you’ll need to log in and retrieve the keys directly from the UI.  
  


  3. **Disable Users APIs on API v1:** User APIs on API v1 (legacy API version) for creating, updating and deleting users will be disabled. These APIs can be used to hack into your account easily if a hacker gets hold of your API key, hence these legacy APIs pose a security risk to your account.


* * *

### **User Management permissions and API access**

  


When Enhanced Security is enabled, API-based changes to user-management permissions remain restricted.

  


To allow API-based updates for User Management permissions, go to Settings > Company > Advanced Settings and disable Enhanced Security. Only disable Enhanced Security if your agency requires API-based user-management workflows. Disabling this setting may increase security risk.

  


This allows API-based updates for the following User Management permissions:

  


**View & Manage Users: **Allows API-based user creation and user edits.

**View Users:** Allows API-based user viewing.

  

    
    
    Please note that the Enhanced Account Security setting is default for all accounts, unless you have opted-out in advance.

  


  


You’ll have the ability to opt-out in [Settings](<https://app.gohighlevel.com/settings/company>); however, we strongly advise against it as it will put your account and data at risk.

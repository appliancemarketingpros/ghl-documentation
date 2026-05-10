# Admin Vs. User Roles and Permission Scopes

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001078296-admin-vs-user-roles-and-permission-scopes](https://help.gohighlevel.com/support/solutions/articles/48001078296-admin-vs-user-roles-and-permission-scopes)  
**Category:** Settings  
**Folder:** User Settings

---

**_  
_**

The following is a table outlining permissions of sub-account level roles.

  


  


  


### **Sub-Account Level User Roles**

** _![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155018238155/original/mcE4xdl46E3pyAgBhVD9qRWDvOg8gfscqg.png?1705709137)_**

* * *

## **Quick-Reference Permission Matrix.  
**

  


  


**Agency-Only**  
| **Sub-Account-Only**  
| **Available in Both**  
  
---|---|---  
Create / Edit / Delete Sub-Accounts  
| Pipelines & Opportunities  
| User Management (Admins can add/edit users within their level)  
  
Manage SaaS Mode & Reselling  
| Workflows / Campaigns  
| Dashboard Reporting  
  
Global Integrations (Mailgun, Twilio Rebilling, Google API, etc.)  
| Calendars & Appointment Settings  
| Media Library  
  
Snapshot Management  
| Conversations (SMS, Email, Chat)  
| Audit Logs  
  
Agency-Level Billing & Branding  
| Contact Management & Smart Lists  
|   
  
Agency Settings (Company Info, Rebilling Settings)  
| Reputation Management  
|   
  
White-Label Settings (Custom Domains, Logos, Colors)  
| Funnel & Website Builder  
|   
  
  
  


  

    
    
    **Note:** If a permission is not listed, assume it inherits the broader role’s default capabilities at its respective level.

  


  


Admins can change the role of a particular user by going to **Settings > My Staff > Edit (pencil icon) > Scroll to and expand "User Roles"****  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155018238329/original/SO6U66a5eqB-L00Pot42Kknck7OO6w0K8Q.png?1705709967)**

  


* * *

## **Frequently Asked Questions**

  


**Q. If a permission is available at both Agency and Sub-Account levels, does the Agency Admin override Sub-Account Admins?**

Yes. Agency Admins hold global authority. For permissions like user management, reporting, or media library, Agency Admin actions apply across all sub-accounts, while Sub-Account Admins manage only within their assigned sub-account.

  


**Q. What happens if a user is added at the Agency level and then also given access to a Sub-Account?**

The user will have **two role scopes** : agency-wide access from their Agency role, plus sub-account-specific access from their Sub-Account role. Permissions don’t cancel out—they stack, with the broader Agency permissions always taking precedence.

  


**Q. Do all Agency Admins have “Login As”?****  
****No**. “Login As” is controlled by the Enable Login As **permission at the agency level**. If it’s disabled for an admin, the Login As option is hidden for that user.

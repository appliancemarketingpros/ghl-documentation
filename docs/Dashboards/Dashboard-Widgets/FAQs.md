# FAQs

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001230-faqs](https://help.gohighlevel.com/support/solutions/articles/155000001230-faqs)  
**Category:** Dashboards  
**Folder:** Dashboard Widgets

---

**TABLE OF CONTENTS**

  * General Questions
    * Which plans offer access to custom dashboard widgets?
    * Why does the widget data show a different time/date format compared to other sections of the platform?
    * Which roles have access to the Custom widgets?
    * How do permissions work for the dashboard?
    * How can I configure widgets to display data specific to the team member viewing the dashboard?
    * Why is there a mismatch in opportunities on the new dashboard?


  


* * *

# General Questions

## Which plans offer access to custom dashboard widgets?

Multiple custom dashboards, widgets and custom reports are available for the $297 and $497+ plans.

  


* * *

## Why does the widget data show a different time/date format compared to other sections of the platform?

Currently, our dashboard widgets use a system timezone and date format for consistency. We understand this may not be ideal for all users, and we're actively working to provide you with the flexibility to switch time and date formats within the dashboard widgets for a more tailored experience. Stay tuned for this upcoming feature!

* * *

  


## Which roles have access to the Custom widgets?

The dashboard can be modified using these custom widgets by the Agency Admins and Agency users on the $497 plan or higher. For accounts on the $497 plan or above, dashboard access varies based on roles:

  * Agency Admin ➝ Complete Edit and View Access 
  * Agency User ➝ Complete Edit and View Access
  * Account Admin ➝ View Access
  * Account User ➝ View Access, based on user permissions 


  


* * *

## How do permissions work for the dashboard?

To modify user permissions for the dashboard, follow these steps:

  1. Navigate to "My Staff" in the Settings.
  2. Click on "Edit" next to the user for whom you want to adjust permissions.
  3. In the "User Permissions" section, make the necessary changes. The following dashboard permissions are available:  
  


Dashboard Stats| Grants access to the entire Dashboard. This is view only for Account Admin and Account users  
---|---  
Contacts| Provides access to all contacts and contact-related widgets.  
Opportunity| Provides access to all Opportunities and opportunity-related widgets.  
Appointment| Provides access to all Appointments and appointment-related widgets.  
Lead value| Provides access to value (monetary) related widgets on the dashboard.  
Only Assigned data| No date will be visible on the custom widgets if enabled  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155010424997/original/_Zs22irMphOpjSYobA124EmRNCPjSH5G0w.png?1697628144)

  


* * *

## How can I configure widgets to display data specific to the team member viewing the dashboard?

To enable team members to view their own data exclusively on the dashboard widgets, ensure you set a condition for each widgets using USER -> LOGGED IN USER under the conditions tab. This configuration will ensure that each team member sees only their data on the widgets.

* * *

## Why is there a mismatch in opportunities on the new dashboard?

We've shifted to considering the "Last Status Change" date for opportunities, departing from the previous "Created" date. The mismatch in opportunity counts on the new dashboard is due to updates in older opportunities, contributing to the overall chart count.

  


To address this, you can customize the date property used on the widgets:

  


  * **For General Widgets:** Click on the filter icon on the widget and switch the date property. Changing it on one filter will automatically update it for the remaining general filters.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155013893411/original/hGP9vr-CceskSunU0YQHHwivCCiKtNYf0w.png?1701245396)  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155013893429/original/hlFooSebrvx_XMUh3A4UCbS_Ptu5ABFgBg.png?1701245419)
  * **For Users on the $497 and Higher Plans:** Custom widgets can be added, allowing users to specify the date property in the widget settings for a more tailored experience. This is an exclusive feature for users on plans $497 and higher.


* * *

## Why can’t I select Session Source or Medium in the “Group By” or “View By” options?

This happens when multiple filter groups are used in the widget settings. If you're trying to use Session Source or Session Medium as a grouping option, only one filter group is allowed. That group must include the Attribution Type filter (either First Touch or Last Touch). Adding more than one filter group will disable attribution-based groupings for accuracy and consistency.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048128269/original/_tZSrZ3xijwoL6i9pVvRqzvW3aOlIa0_Gg.png?1749715177)

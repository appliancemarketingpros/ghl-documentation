# LC Phone - Inbound Call Routing by Working Hours

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008268-lc-phone-inbound-call-routing-by-working-hours](https://help.gohighlevel.com/support/solutions/articles/155000008268-lc-phone-inbound-call-routing-by-working-hours)  
**Category:** Phone System  
**Folder:** LC Phone System

---

Inbound Call Routing by Working Hours helps prevent work calls from ringing outside a user’s scheduled availability. This article explains how the feature works, how to configure it for yourself or a team member, and how HighLevel handles calls received after hours.

* * *

**TABLE OF CONTENTS**

  * What Is Inbound Call Routing by Working Hours?
  * Key Benefits of Inbound Call Routing by Working Hours
  * Who Can Configure Inbound Call Routing
  * How Calls Are Routed Outside Working Hours
  * How to Set Up Inbound Call Routing by Working Hours
    * Configure the Setting for Your Profile
    * Configure the Setting for a Team Member
  * How Forwarding Numbers Are Handled
  * Important Limitations
  * Frequently Asked Questions
  * Related Articles


* * *

## **What Is Inbound Call Routing by Working Hours?**

  

    
    
    **Note:** The setting is **off by default**. Nothing changes until you turn it on.
    

  


Inbound Call Routing by Working Hours uses a selected availability schedule to determine whether an inbound call should ring a user. This helps prevent work calls from reaching users after hours, on weekends, during holidays, or while they are away without requiring them to change device settings or uninstall the mobile app.

  


When **Only ring during working hours** is enabled, any inbound call that reaches you outside the selected schedule skips you and follows the phone number’s existing backup handling. During your working hours, calls ring exactly as they do today.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076517184/original/6hyNBeH53XiPEUxB3yiiJB5Q_rFEvmgHdA.png?1784648284)

* * *

## **Key Benefits of Inbound Call Routing by Working Hours**

  


  * **Prevent after-hours interruptions:** Stop work calls from ringing users outside their selected availability.  
  

  * **Use existing availability schedules:** Control inbound ringing with a selected schedule instead of manually changing call settings.  
  

  * **Support team-based routing:** Unavailable users can be skipped while other eligible users continue receiving calls in supported routing scenarios.  
  

  * **Handle holidays and time off:** Date-specific schedule entries can prevent calls from ringing users on holidays or other unavailable dates.  
  

  * **Preserve existing backup routing:** When a user is unavailable, supported calls continue through the phone number’s existing routing or backup configuration.


* * *

## **Who Can Configure Inbound Call Routing**

  


Access depends on whether a user is managing their own availability or an administrator is managing availability for another team member. 

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076517747/original/ZZ19tu14AMZgUZHimlt76b0PmUOrI0tuag.png?1784648574)

* * *

## **How Calls Are Routed Outside Working Hours**

  


HighLevel checks the selected schedule before ringing the user. The result depends on how the inbound call is routed.

  


Routing scenario| During working hours| Outside working hours  
---|---|---  
**Assigned user or contact**|  The user rings normally| User is skipped, and call follows existing backup (**Voice mail or Voice AI**)  
**Ring All**|  All eligible users ring normally| Users outside working hours are skipped; available users continue to ring  
**Call Menu or IVR**|  Configured recipients ring normally| The unavailable user is skipped; other recipients continue to ring  
**Only recipient in an IVR connect step**|  The user rings normally| No recipient is connected, and the call flow continues  
**Transferred call**|  Existing transfer behavior applies| Working-hours filtering is not currently supported  
  
* * *

## **How to Set Up Inbound Call Routing by Working Hours**

  


Selecting the correct schedule ensures HighLevel can accurately determine when you should receive inbound calls. Confirm the schedule’s weekly hours, date-specific entries, and timezone before relying on it for after-hours routing.

  


### **_Configure the Setting for Your Profile_**

  


  1. Click on **Settings.**  
  
![](https://jumpshare.com/share/Ku3XuD0iLcmYNkviMPjq+/Screen+Shot+2026-07-22+at+15.29.14.png)  
  

  2. Click on**My Profile.**  
  

  3. Scroll to the **Inbound call routing** card.  
  

  4. Enable **Only ring during working hours**.  
  

  5. Open the **Call routing schedule** dropdown.  
  

  6. **Select** the **schedule** that defines your working hours. The selected schedule is the schedule HighLevel checks before ringing you. Your choice saves automatically.  
  
![](https://jumpshare.com/share/Sk5lEAcUmRHBZ1UPMwP6+/GIF+Recording+2026-07-22+at+15.32.47.gif)  
  


### **_Configure the Setting for a Team Member_**

  

    
    
    **Note:** The administrator or manager completing these steps must have the **Manage calendars** permission.
    

  


  1. Click on **Settings.**  
  
**![](https://jumpshare.com/share/Ku3XuD0iLcmYNkviMPjq+/Screen+Shot+2026-07-22+at+15.29.14.png)**  
  

  2. Go to**My Staff**.  
  

  3. Click on the **edit icon** of the team member you want to update.  
  
![](https://jumpshare.com/share/izl1zumovbJJ6KFVXVCc+/Screen+Shot+2026-07-22+at+15.41.57.png)  
  

  4. Select **User Availability**.  
  

  5. Locate the **Inbound call routing** card.  
  

  6. Enable **Only ring during working hours**.  
  

  7. **Select** the **schedule** that defines the team member’s working hours.  
  

  8. **Save** the team member’s settings when prompted.  
  
![](https://jumpshare.com/share/lHc2znfTkdwxxK2OzegU+/GIF+Recording+2026-07-22+at+15.43.43.gif)


* * *

## **How Forwarding Numbers Are Handled**

  
When a user's personal number matches a configured forwarding or business phone number, HighLevel also skips that matching number outside the user's working hours. This prevents the user from being reached indirectly and ensures the selected schedule is respected.

  


![](https://jumpshare.com/share/r8qmylw8JqFaUD8hu4h7+/4SWAcLuwcT4fvhC2Hb7xoEeJjtRaW7Qnkg.png)

* * *

## **Important Limitations**

  


Keep the following limitations in mind when using working-hours routing:

  


  * **Transferred calls are not currently filtered by working hours.** Existing transfer behavior applies when a call is transferred to a user.  
  

  * **Working-hours routing does not create a separate after-hours destination.** Calls received outside a user's selected schedule continue through the phone number's existing routing or backup configuration.  
  

  * **The setting is user-specific.** Each user who should be excluded from calls outside their availability must have the appropriate schedule selected and the setting enabled.  
  

  * **Schedule configuration matters.** Weekly hours, date-specific availability, and the schedule timezone determine whether HighLevel considers a user available.


* * *

## **Frequently Asked Questions**

  


**Q: Will anything change when the setting is left off?**  
No. The setting is off by default, and call routing remains unchanged until it is enabled.

  


  


**Q: Which schedule does HighLevel use?**  
HighLevel uses the schedule selected from the **Call routing schedule** dropdown. You can change the selected schedule at any time.

  


  


**Q: How can I stop calls from ringing on a holiday?**  
Add a date-specific entry with no available hours for that date to the selected schedule. The date-specific entry overrides the normal weekly hours for that day.

  


  


**Q: Does working-hours routing apply to transferred calls?**  
Not yet. This release applies to inbound calls routed to assigned users, **Ring All** , and call menu or IVR steps. Transferred calls are not currently supported.

  


  


**Q: Can I route after-hours calls to a specific teammate or my personal voicemail?**  
Not in this version. Calls received outside your working hours follow the phone number’s existing backup.

  


  


**Q: Why do calls still reach me after hours after I enabled the setting?**  
Confirm that the correct schedule is selected, the current time falls outside that schedule, and the schedule’s timezone is correct. Also verify that the toggle is enabled for the correct user profile. When testing a holiday or day off, confirm that the date-specific entry has no available hours.

  


  


**Q: Does this setting change my phone number's normal routing during working hours?**  
No. During the selected working hours, supported inbound calls continue through the existing routing configuration.

  


  


**Q: What happens in Ring All if some team members are outside their working hours?**  
Users outside their selected working hours are skipped. Other eligible users can continue receiving the call.

* * *

### **Related Articles**

  


  * [Inbound Calls: IVR, AI, Routing & Call Flow Explained](<https://help.gohighlevel.com/support/solutions/articles/155000007498-inbound-calls-ivr-ai-routing-call-flow-explained>)  
  

  * [Overview of Phone Number Configuration Options](<https://help.gohighlevel.com/support/solutions/articles/48001229976-overview-of-phone-number-configuration-options>)  
  

  * [Ring Incoming Calls to Multiple Users](<https://help.gohighlevel.com/support/solutions/articles/155000002850>)  
  

  * [Voicemail for Company and Users](<https://help.gohighlevel.com/support/solutions/articles/48001146671-voicemail-for-company-and-for-users>)  
  

  * [Workflow Action – IVR Connect Call](<https://help.gohighlevel.com/support/solutions/articles/155000003371-workflow-action-ivr-connect-call>)  
  

  * [How to Forward Inbound Calls to Mobile App](<https://help.gohighlevel.com/support/solutions/articles/48001224659-how-to-forward-inbound-calls-to-mobile-app>)

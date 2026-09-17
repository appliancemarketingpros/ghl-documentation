# Workflow Action - Event Start Date

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003357-workflow-action-event-start-date](https://help.gohighlevel.com/support/solutions/articles/155000003357-workflow-action-event-start-date)  
**Category:** Workflows  
**Folder:** Data Management

---

**TABLE OF CONTENTS**

  * Overview
  * Action Name
  * Action Description
  * Action Details
  * Example


##   


## Overview

The **Event Start Date** action in the workflow allows you to set a specific date and time to trigger Wait events or other future actions. It ensures that subsequent events are based on a specific time or day, enhancing control over the timing of follow-up actions.

  


## Action Name

**Event Start Date**

  


## Action Description

The **Event Start Date** action sets a specific date, time, or a custom field value as the reference point for subsequent workflow actions, particularly **Wait** events. This action ensures that actions are paused or triggered based on the set event time, making it useful for automating follow-ups, reminders, or other scheduled tasks.

  


## Action Details

### Specific Day

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032445509/original/iwafksQDf_H0H5RLys6FTyLMe12XPHXRmg.png?1725713040)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032445558/original/NF4KiMa2-WOZCmfGmjoWXszo7CKkD3JY5w.png?1725713140)

  


### Custom Field![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032445534/original/Jv63PBvwYkS7K6_OMyoB6eLJW8nSljqA6Q.png?1725713083)

###   


### Specific Date and Time

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032445569/original/lnBfAlpPR6O72bkGrAG9ycyxviTT5JWDTg.png?1725713232)

  


### **How to Configure** :

  1. **Action Name** : Enter a name that describes this action, e.g., "Event Start Time for Webinar".
  2. **Type** : Choose from the following options:
     * **Specific Day** : Select if you want to set a specific recurring day (e.g., day of the month or day of the week).
     * **Specific Date/Time** : Use this when you want to set an exact date and time (e.g., Sept 14, 2024, 10:30 AM).
     * **Custom Field** : This pulls the date from a custom field (e.g., a field capturing "Event Registration Date").
  3. **Select Custom Field** (only visible for **Custom Field** type): Choose the relevant custom field that stores the date.
  4. **Select Date** (only visible for **Specific Date/Time** type): Pick a date and time from the calendar picker.
  5. **Current Day of Month/Week** (only visible for **Specific Day** type): Select whether the event starts based on the current day of the month or the current day of the week.


  


### **Field Details:**

Field Name| Description| Mandatory  
---|---|---  
Action Name| The label or title for the action in your workflow.| Yes  
Type| Choose between Specific Day, Specific Date/Time, or Custom Field.| Yes  
Select Custom Field| This field appears if Custom Field type is selected. It picks a custom date field.| No  
Select Date| This field appears if Specific Date/Time type is selected. Select the date from a calendar picker.| No  
Current Day of Month/Week| This appears if Specific Day type is selected, allowing you to choose day or week-based triggers.| Yes  
  
##   


## Example

  * **Type: Specific Date/Time**

    * Use Case: If you want to trigger a follow-up email one week after an event that was scheduled on a particular date.
    * Example Setup: Select the date `September 14, 2024` to mark the event start. The workflow will use this as the reference point for all subsequent timed actions.
  * **Type: Custom Field**

    * Use Case: You want to set a follow-up action based on a custom date field like "Event Registration Date".
    * Example Setup: The workflow pulls the date from the custom field `Event Registration Date` to trigger subsequent actions like reminder emails or task assignments based on that date.
  * **Type: Specific Day**

    * Use Case: For recurring events or tasks, you want to automate actions based on the current day of the week or month.
    * Example Setup: Select "Current Day of Month" to set recurring reminders every first of the month.


  


## Additional Notes

  * **Date Format** : Ensure the date and time are in the correct format (e.g., MM-DD-YYYY HH). This prevents errors in workflow timing.
  * **Use Cases** : Perfect for automating reminders, follow-ups, or any action that is contingent on a specific date.
  * **Triggering** : Combine this action with **Wait** events to hold contacts until a specific date or time before proceeding to the next action.

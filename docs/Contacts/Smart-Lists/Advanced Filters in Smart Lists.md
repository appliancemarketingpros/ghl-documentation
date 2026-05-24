# Advanced Filters in Smart Lists

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007530-advanced-filters-in-smart-lists](https://help.gohighlevel.com/support/solutions/articles/155000007530-advanced-filters-in-smart-lists)  
**Category:** Contacts  
**Folder:** Smart Lists

---

Use Advanced Filters in Smart Lists to segment contacts with more precision in HighLevel. This article explains what Advanced Filters are, how they are used, and how the different filter options work so you can build more accurate contact lists. For a broader overview of Smart Lists, see [How to Create & Manage Smart Lists.](<https://help.gohighlevel.com/en/support/solutions/articles/48001062094>)

* * *

**TABLE OF CONTENTS**

  * What are Advanced Filters in Smart Lists?
  * Key Benefits of Advanced Filters
  * How To Setup Advanced Filters in Smart Lists
  * Understanding the Different Types of Advanced Filters
  * Date Filters
  * DND Filters
  * String Filters
  * Numeric Filters
  * Frequently Asked Questions 
  * Related Articles


* * *

# **What are Advanced Filters in Smart Lists?**

  


Advanced Filters allow you to narrow Smart List results using specific rules tied to contact fields and related data. This makes it easier to build targeted lists based on contact details, engagement, communication settings, opportunity data, and more.  
  


Each filter is built using three main parts: a field, an operator and a value. The available operators depend on the field you select. For example, a date field will support date-based operators, while a number field will support comparison operators.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067238877/original/2MAhrzna8g6y0aqLrdchTLh9wgPWGgieiw.png?1773848221)

* * *

## **Key Benefits of Advanced Filters**

  


  * **Precise Segmentation:** Narrow contact lists using specific field values, operators, and conditions.  
  


  * **Better List Accuracy:** Match contacts more reliably by choosing operators that fit the selected field type.  
  


  * **Faster List Building:** Use searchable filters to quickly find the fields you need.  
  


  * **Flexible Filtering:** Work with date, string, number, status, opportunity, and DND-related data.  
  


  * **Cleaner Contact Management:** Find missing values, invalid statuses, and other records that need review.  
  


  * **Safe Outreach Targeting:** Use DND and status-based filters to build more compliant communication lists.


* * *

## **How To Setup Advanced Filters in Smart Lists**

  


Applying Advanced Filters correctly helps return more relevant contacts and makes Smart Lists easier to manage. Choosing the right field, operator, and value is the key to getting reliable results.

  


  1. Go to **Contacts** then click **\+ Add smart list or** open existing smart list.  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155071633839/original/Clp4-CCdWz2BunkzxrRaKU7jmXGTz4CyUw.png?1779174768)**  
  


  2. Click**Advanced Filters**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067252423/original/oAnRy_lp0f5vbb0euwFqrKkCjtjhZyJK1A.png?1773855045)  
  


  3. Search for and select the field you want to use.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067252494/original/EEEl4VdL2r-4GLQRASjwamcyL-Klf61B8w.png?1773855089)  
  


  4. Choose the operator that matches the type of segmentation you are looking for.  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067252536/original/F5dFqWTMIr7py7AkXc9mc6wSkouElO4_ww.png?1773855152)**  
  


  5. Enter or select the value.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067252566/original/R3et-b6Kotvl9PZJd20cz8C7cA2gAqr5jw.png?1773855196)  
  


  6. Click **\+ Add Nested Filter** to add another condition that must also be true for the contact to stay in the Smart List. Use this when you want to apply **AND** logic

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067252789/original/yqDPCcGJgG1FdLWyBH6gmqqIc7zJLJq63A.png?1773855412)  
  


  7. Click **\+ Add Filter** to add another possible condition the contact can match to be included in the Smart List. Use this when you want to apply **OR** logic.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067253135/original/ijwpGiCnf_zydnxJEIR_LHFBx9DHLI3E6g.png?1773855635)  
  


  8. Click **Apply**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067253339/original/YYqQ5F1dZ6DxzVb5g7xrujEjb7T16VctUw.png?1773855719)


* * *

## **Date Filters**

  


Date filters help you segment contacts using exact dates, relative timeframes, and rolling date conditions. These filters are useful for finding recent activity, upcoming events, and recurring date-based milestones. Date-based filters can be applied to fields that store a date or date-and-time value.

  


Examples of date fields you may be able to filter by include:

  


  * Last Appointment At
  * Date of Birth
  * Created On
  * Last Activity On
  * Last Updated On
  * Last Email Clicked Date
  * Last Email Opened Date


  


Date operators can vary based on the kind of date logic you need to apply. The sections below organize them into groups so you can quickly understand what each operator is used for before reviewing the matching options in the tables.

  


  


### **Relative Date Filters**

  
Shows contacts based on action timing relative to today's date.

  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Is → Today| Contacts whose last appointment occurred today| Today = 11 Mar 2026| Appointment on 11 Mar 2026  
Is → Tomorrow| Appointment is scheduled tomorrow| Today = 11 Mar 2026| Appointment on 12 Mar 2026  
Is → Yesterday| Appointment occurred yesterday| Today = 11 Mar 2026| Appointment on 10 Mar 2026  
Is → This Week| Appointments in the current calendar week| Week: 9–15 Mar 2026| Appointment between 9 Mar – 15 Mar 2026  
Is → This Month| Appointments in the current month| Month: March 2026| Appointment between 1 Mar – 31 Mar 2026  
Is → This Quarter| Appointments within the current quarter| Q1 = Jan–Mar 2026| Appointment between 1 Jan – 31 Mar 2026  
Is → This Year| Appointments within the current year| Year = 2026| Appointment between 1 Jan –  
31 Dec 2026  
  
  


  


### **Exact Date Filters**

  
Filter contacts by pinpointing a specific date or date range.

  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Is → On| Matches appointments on a specific date| 5 Mar 2026| Appointment exactly on 5 Mar 2026  
Is → Between| Matches appointments within a date range| 1 Mar – 7 Mar 2026| Appointment between 1 Mar & 7 Mar 2026  
  
  


  


### **Time Difference Filters (Relative Duration)**

  
Filter contacts based on elapsed or upcoming time from today.

  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Is → More Than| Appointment happened longer than the specified time ago| More than 7 days ago| Appointment before 4 Mar  
Is → Less Than| Appointment happened within the specified time ago| Less than 7 days ago| Appointment between 4 Mar –11 Mar 2026  
Is → In the Next| Appointment scheduled within upcoming time range| Next 3 days| Appointment between 11 Mar – 14 Mar 2026  
Is → In the Last| Appointment happened within past time range| Last 3 days| Appointment between 8 Mar – 11 Mar 2026  
  
  


  


### **Date Comparison Filters**

  
Compare action dates against a fixed reference date.

  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Is → After Date| Appointment occurs after the selected date| After 5 Mar 2026| Appointment 6 Mar 2026 onward  
Is → Before Date| Appointment occurs before the selected date| Before 5 Mar 2026| Appointment 4 Mar 2026 or earlier  
  
  


  


### **Negative Filters (Is Not)**

**  
**Exclude contacts based on date conditions — the inverse of each positive filter.

  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Is Not → Today| Excludes appointments happening today| Today = 11 Mar 2026| Any appointment except 11 Mar 2026  
Is Not → Yesterday| Excludes appointments from yesterday| Yesterday = 10 Mar 2026| Any appointment except 10 Mar 2026  
Is Not → This Week| Excludes appointments in the current week| Week: 9–15 Mar 2026| Any appointment outside this range  
Is Not → On| Excludes a specific date| Not on 5 Mar 2026| All dates except 5 Mar 2026  
Is Not → Between| Excludes a date range| Not between 1–7 Mar 2026| Dates before 1 Mar or after 7 Mar 2026  
Is Not → Tomorrow| Any date except tomorrow| Mar 12, 2026| All contacts whose last appointment is not scheduled for tomorrow  
Is Not → This Month| Any month other than March 2026| Before Mar 1 or after Mar 31| Contacts whose last appointment was in any other month  
Is Not → This Quarter| Outside current quarter (Q1 2026)| Before Jan 1 or after Mar 31| Contacts whose last appointment falls outside Q1 2026  
Is Not → This Year| Not in 2026| Before Jan 1 or after Dec 31| Contacts whose last appointment was not in 2026  
Is Not → More Than ... Ago| Appointment NOT more than 30 days ago| On or after Feb 9, 2026| Appointment was within the last 30 days  
Is Not → After Date| On or before selected date| On or before Mar 1, 2026| Inverse of 'After Date'  
Is Not → Less Than ... Ago| NOT within the last 7 days| On or before Mar 4, 2026| Last appointment was 7+ days ago  
Is Not → Before Date| On or after selected date| On or after Jan 1, 2026| Inverse of 'Before Date'  
Is Not → In the Next ...| Not within the next 7 days| Not within Mar 11–18, 2026| Past appointments and future ones beyond 7-day window  
Is Not → In the Last ...| NOT within the last 14 days| Before Feb 25 or after Mar 11, 2026| Contacts who haven't had a recent appointment  
  
  


  


### **Empty / Not Empty Filters**

  
Identify contacts with or without any appointment record.

  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Is Empty| Contact has never had an appointment recorded|  -| Contacts with no appointment history  
Is Not Empty| Contact has at least one appointment| -| Contacts with any appointment on record  
  
  


  


### **Best Practices for Using Date Filters**

  


  * Use 'In the Last' to identify recent engagement  
  

  * Use 'More Than' to identify inactive contacts  
  

  * Use 'Between' for historical reports  
  

  * Use 'Is Empty' to find leads without appointments


* * *

## **DND Filters**

  


DND (Do Not Disturb) filters help you identify whether communication restrictions are enabled for a contact. These filters are especially useful for building compliant outreach lists and excluding contacts who should not receive messages on specific channels. DND filters can be applied to fields that store yes-or-no values related to contact communication preferences.

  


Examples of DND and boolean fields you may be able to filter by include:  
  


  * DND all
  * SMS DND
  * Email DND
  * Calls & Voicemails DND
  * WhatsApp DND
  * Inbound DND
  * FB Messenger DND
  * GMB Messenger DND


  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Enabled| Contact has DND enabled|  -| Contacts who opted out of the selected channel  
Disabled| Contact has not have DND enabled|  -| Contacts who have not opted out of the selected channel  
  
  


* * *

## **String Filters**

  


String filters help you match contacts based on names, labels, IDs, attribution values, communication details, and other text-based information. These filters are useful when you need to find exact values, partial matches, selected values from a dropdown, comma-separated lists, or blank fields.

  


The main difference between different types of string fields is how the value is entered. Some string filters use a free-text input where you type the value yourself. Others use a dropdown or selected-value field where you choose from available options. Some fields may also allow comma-separated values, while others only support a single selected value. If an operator is not shown for the selected field, that operator is not available for that field.  
  


Examples of string fields you may be able to filter by include:

  


  * First name
  * Last name
  * Email
  * Address
  * Timezone
  * Last Updated By
  * Opportunity Pipeline
  * Email Status
  * Tags


  

    
    
    **Note:** Any new custom field created with:
    1. Single line, Multi line text will follow contact score parameters
    2. Text Box list will follow Time Zone parameters
    3. Drop Down Single, Drop Down Multiple, Radio Button, Checkbox will follow Tags parameters

  


  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Is| Matches one selected value| Chicago| Contacts located in Chicago  
Is Not| Excludes one selected value| Chicago| Contacts not located in Chicago  
Contains| Matches text that appears anywhere in the field value| New York| Contacts with city that includes "New York" (ex. New York City)  
Does Not Contain| Excludes text that appears anywhere in the field value| New York| Contacts with city that doesn't include "New York" (ex. New York City)  
Is any of (comma separated)| Matches one or more listed values| Chicago, London, New York City  
| Contacts located in Chicago, London or NYC  
Is None of (comma separated)| Excludes any value from a comma-separated list| Chicago, London, New York City  
| Contacts not located in Chicago, London or NYC  
Is Empty| Finds contacts where the field has no stored value| -| Contacts with no city listed  
Is Not Empty| Finds contacts where the field contains a value| -| Contacts with any city listed  
  
* * *

## **Numeric Filters**

  


Numeric filters help you segment contacts based on measurable values such as scores, counts, and other number-based data. These filters are useful when comparing values, ranges, thresholds, and whether a field contains a numeric value. Numeric filters can be applied to fields that store measurable numeric values.

  


Examples of numeric fields you may be able to filter by include:

  


  * Engagement Score
  * Score from a Quiz (Custom Field)


  

    
    
    **Note:** Any new custom field created with 
    1. Number - will follow engagement score parameters
    2. Phone - will follow Phone Number parameters
    3. Monetary - will follow engagement score parameters

  


Filter Setting| Meaning| Example Input| Contacts That Will Match  
---|---|---|---  
Equal To| Matches one selected number  
| 100| Contacts who scored a 100  
Does Not Equal| Excludes one selected number| 100| Contacts who did not score 100  
Between| Matches a numeric range| 90 - 100| Contacts who scored between 90 and 100  
Greater Than| Matches values above a threshold| 90| Contacts who scored over a 90  
Greater Than or Equal To| Matches values at or above a threshold| 90| Contacts who score a 90 or above  
Less Than| Matches values below a threshold| 90| Contacts who scored under a 90  
Less Than or Equal To| Matches values at or below a threshold| 90| Contacts who scored a 90 or below  
Is Empty| Finds contacts where the field does not contains a value| -| Contacts who did not complete the quiz  
Is Not Empty| Finds contacts where the field contains a value| -| Contacts who completed the quiz  
  
* * *

## **Frequently Asked Questions**

  


**Q: Do all fields support the same operators?**

No. The operators available depend on the field you select.

  


**Q: Can I use more than one filter at a time?**

Yes. You can apply multiple filters to narrow your Smart List results further.

  


**Q: Can I filter contacts by opportunity information?**

Yes. Opportunity-related filters can be used to segment contacts by pipeline, stage, and status.

  


**Q: Where can I learn more about Smart Lists?**

See [How to Create & Manage Smart Lists](<https://help.gohighlevel.com/en/support/solutions/articles/48001062094>) for a broader overview of Smart Lists and how they work.

* * *

## **Related Articles**

  


  * [How to Create & Manage Smart Lists](<https://help.gohighlevel.com/en/support/solutions/articles/48001062094>)  
  


  * [AND/OR Filters](<https://help.gohighlevel.com/en/support/solutions/articles/155000001247>)  
  


  * [How to Filter Opportunities](<https://help.gohighlevel.com/en/support/solutions/articles/155000001241>)  
  


  * [Contacts – Revamped List View & SmartLists](<https://help.gohighlevel.com/en/support/solutions/articles/155000006504>)

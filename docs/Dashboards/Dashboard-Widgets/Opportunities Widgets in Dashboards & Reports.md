# Opportunities Widgets in Dashboards & Reports

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008109-opportunities-widgets-in-dashboards-reports](https://help.gohighlevel.com/support/solutions/articles/155000008109-opportunities-widgets-in-dashboards-reports)  
**Category:** Dashboards  
**Folder:** Dashboard Widgets

---

**TABLE OF CONTENTS**

  * Overview
  * Available Opportunities Widgets
    * Supported Chart Types
  * Group By Options
  * Date Properties
  * Filtering Opportunities Widgets (Conditions)
    * Standard Filters
    * Attribution Filters
  * Where to Use Opportunities Widgets
  * Frequently Asked Questions (FAQs)


## Overview

Opportunities Widgets let you track and analyze your pipeline directly inside your dashboards and custom reports. From total opportunity counts and revenue trends to lost reason breakdowns and this-month win rates, these widgets give you a full picture of your pipeline health — without leaving HighLevel.

All Opportunities Widgets support multiple chart types and can be filtered using conditions to scope results to a specific pipeline, stage, status, assignee, or attribution source.

* * *

## Available Opportunities Widgets

There are **17 Opportunities Widgets** available. Each widget opens with a default chart type but can be switched to any supported chart type from within the widget settings.

#| Widget Name| Default Chart| Metric| What It Shows| Default Filter| Date Scope  
---|---|---|---|---|---|---  
1| **Opportunity Count**|  Number| Count| Total number of all opportunities| None| Dashboard Date Range  
2| **Opened Opportunities**|  Number| Count| Number of opportunities currently open| Status = Open| Dashboard Date Range  
3| **Opened Opportunity Value**|  Number| Sum of Monetary Value| Combined monetary value of all open opportunities| Status = Open| Dashboard Date Range  
4| **Won Opportunities**|  Number| Count| Number of won opportunities| Status = Won| Dashboard Date Range  
5| **Won Opportunity Value**|  Number| Sum of Monetary Value| Combined monetary value of won opportunities| Status = Won| Dashboard Date Range  
6| **Lost Opportunities**|  Number| Count| Number of lost opportunities| Status = Lost| Dashboard Date Range  
7| **Lost Opportunity Value**|  Number| Sum of Monetary Value| Combined monetary value of lost opportunities| Status = Lost| Dashboard Date Range  
8| **Lost Opportunities By Reason**|  Donut| Count| Breakdown of lost opportunities split by loss reason| Status = Lost| Dashboard Date Range  
9| **Abandoned Opportunities**|  Number| Count| Number of abandoned opportunities| Status = Abandoned| Dashboard Date Range  
10| **Abandoned Opportunity Value**|  Number| Sum of Monetary Value| Combined monetary value of abandoned opportunities| Status = Abandoned| Dashboard Date Range  
11| **Total Opportunity Value**|  Number| Sum of Monetary Value| Combined monetary value of all opportunities regardless of status| None| Dashboard Date Range  
12| **Opportunity Counts by Status**|  Donut| Count| Distribution of opportunities across all statuses| None| Dashboard Date Range  
13| **Opportunity Counts Over Time**|  Line| Count| How opportunity creation trends over a time period| None| Dashboard Date Range  
14| **Opportunity Revenue Over Time**|  Line| Sum of Monetary Value| How opportunity revenue trends over a time period| None| Dashboard Date Range  
15| **Won Opportunities This Month (For You)**|  Number| Count| Won opportunities this month assigned to the logged-in user| Status = Won + Assigned User = logged-in user| This Month (fixed)  
16| **Won Opportunities Value This Month**|  Number| Sum of Monetary Value| Total won revenue this month across all team members| Status = Won| This Month (fixed)  
17| **Won Opportunities Value This Month (For You)**|  Number| Sum of Monetary Value| Total won revenue this month for the logged-in user| Status = Won + Assigned User = logged-in user| This Month (fixed)  
  
> **Note:** Widgets #15, #16, and #17 use a **fixed date scope (This Month)**. They do not follow the dashboard's global date range selector unless modified in Configure.

> **Note:** Widgets #15 and #17 are **"For You" widgets** — they are scoped to the currently logged-in user via a built-in Assigned User filter. When included in a scheduled report, they reflect the data of the report owner, not the recipient.

* * *

### Supported Chart Types

All 17 Opportunities Widgets can be switched to any of these (supported) chart types from within widget settings:

Chart Type| Best For  
---|---  
**Number**|  Single KPI / quick count or value  
**Donut**|  Distribution / breakdown by category (e.g. by status, by lost reason)  
**Bar**|  Comparing values across categories  
**Line**|  Trends over time  
**Horizontal Bar**|  Comparing many categories with long labels  
**Table**|  Detailed row-level breakdown  
  
* * *

## Group By Options

Widgets that support a breakdown dimension can be grouped by the following fields. Grouping is available on widgets #8, #12, #13, and #14.

Group By Option| What It Groups By  
---|---  
**Status**|  Open / Won / Lost / Abandoned  
**Assignee**|  The user assigned to each opportunity  
**Followers**|  Users following the opportunity  
**Source**|  The source field on the opportunity record  
**Pipeline**|  The pipeline the opportunity belongs to  
**Stage**|  The stage within the pipeline  
**Lost Reason**|  The reason recorded when the opportunity was marked Lost  
**Session Source**|  Session-level traffic channel (e.g. Organic Search, Paid Social)  
**Medium**|  Attribution medium (e.g. Form, Facebook, Calendar)  
  
> **Tip:** Combine Group By with a Status condition to go deep — for example, set Status = Lost as a filter, then Group By Lost Reason to see exactly where deals fall off.

* * *

## Date Properties

Opportunities Widgets can be measured against the following date fields. The date property determines which timestamp is used when the dashboard date range is applied.

Date Property| Description  
---|---  
**Created On**|  When the opportunity was created (default for most widgets)  
**Updated On**|  When the opportunity record was last modified  
**Status Change**|  When the opportunity's status last changed (e.g. when it was marked Won or Lost)  
  
> **Important — Status Change date caveat:** The Status Change date reflects the _most recent_ status change, not when the opportunity originally entered a given status. If an opportunity is re-opened after being marked Lost, the Status Change date resets. This means historical dashboard figures based on Status Change can drift over time. For stable historical reporting, consider using Created On and filtering by Status instead.

* * *

## Filtering Opportunities Widgets (Conditions)

Every Opportunities Widget supports filtering via **Conditions** in the widget settings panel. Conditions let you scope a widget to a specific subset of opportunities — for example, only opportunities in a specific pipeline, or only those lost with a particular reason.

There are **24 condition fields** available, split into standard fields and attribution fields.

* * *

### Standard Filters

Condition Field| Data Type| Available Operators| Value Input| Notes  
---|---|---|---|---  
**Status**|  Enum| Is / Is not / Is one of / Is none of| Open / Won / Lost / Abandoned| Setting Status = Lost unlocks the **Lost Reason** child field  
**Assigned User**|  Enum| Is / Is not / Is one of / Is none of / Is empty / Is not empty| User/Reference lookup|   
**Followers**|  Enum| Is / Is not / Is one of / Is none of / Is empty / Is not empty| User/Reference lookup|   
**Business Name**|  String| Is / Is not / Is empty / Is not empty| Text input|   
**Tags**|  Enum| Is / Is not / Is one of / Is none of / Is empty / Is not empty / Is all of| User/Reference lookup|   
**Primary Contact Name**|  Enum| Is / Is not / Is one of / Is none of / Is empty / Is not empty| User/Reference lookup|   
**Pipeline**|  Enum| Is / Is not / Is one of / Is none of| User/Reference lookup| Setting a Pipeline value unlocks the **Stage** child field  
**Lead Value**|  Number| Is / Is not / Is more than / Is more than equal to / Is less than / Is less than equal to / Is empty / Is not empty| Number input|   
**Lost Reason**|  Enum (dependent)| Is / Is not / Is one of / Is none of / Is empty / Is not empty| User/Reference lookup| Requires **Status = Lost** to be set first  
**Stage**|  Enum (dependent)| Is / Is not / Is one of / Is none of| User/Reference lookup| Requires a **Pipeline** to be selected first  
**Source**|  Enum| Is / Is not| Text input|   
**Custom Fields**|  Custom (per field type)| Varies by custom field type| User/Reference lookup|   
  
* * *

### Attribution Filters

Attribution filters unlock additional sub-filters once the parent **Attribution** field is set. Select either **First Attribution** or **Latest Attribution** first — the child fields below then become available.

Condition Field| Parent Required| Available Operators| Value Input  
---|---|---|---  
**Attribution**|  —| Is| First Attribution / Latest Attribution  
**Medium**|  Attribution| Is / Is not / Is one of / Is none of| Form / Survey / Calendar / Chat Widget / CSV Import / Manual / API / Order Form / Two Step Order Form / Facebook / TikTok / Membership / Conversation / Zapier / Other  
**Session Source**|  Attribution| Is one of / Is none of| Direct Traffic / Organic Search / Paid Search / Social Media / Paid Social / Referral / Third Party / CRM UI / Email Marketing / Trigger Links / Other  
**UTM Medium**|  Attribution| Contains| Text input  
**UTM Source**|  Attribution| Contains| Text input  
**UTM Campaign**|  Attribution| Contains| Text input  
**UTM Campaign ID**|  Attribution| Is / Is not| Text input  
**UTM Keyword**|  Attribution| Contains| Text input  
**UTM Content**|  Attribution| Contains| Text input  
**UTM Matchtype**|  Attribution| Contains| Text input  
**UTM Ad ID**|  Attribution| Is / Is not| Text input  
**UTM Ad Group ID**|  Attribution| Is / Is not| Text input  
  
> **How Attribution filtering works:**
> 
>   1. In the Conditions panel, set **Attribution** to either **First Attribution** or **Latest Attribution**.
>   2. Once set, Medium, Session Source, and all UTM fields become available.
>   3. All child fields apply against the touchpoint you selected (first or latest).
>   4. If you use Session Source or Medium in the **Group By** or **View By** dropdown, only one compound filter group is allowed, and it must include the Attribution Type. Adding multiple filter groups disables attribution-based fields in the dropdown.
> 


* * *

## Where to Use Opportunities Widgets

All 17 Opportunities Widgets are available in both surfaces:

  * ✅ **Dashboards** — for always-on pipeline monitoring and daily check-ins
  * ✅ **Custom Reports** — for scheduled delivery and client-ready exports


* * *

## Frequently Asked Questions (FAQs)

**Q: What is the difference between "Won Opportunity Value" and "Won Opportunities Value This Month"?**

"Won Opportunity Value" follows the dashboard's global date range — it shows won revenue for whatever period you've selected. "Won Opportunities Value This Month" always shows the current calendar month, regardless of the dashboard date range selector.

**Q: Why do my Won/Lost numbers change when I look back at last month?**

If you're using **Status Change** as the date property, this is expected behaviour. Status Change reflects the _most recent_ status change on the record, so reopened or re-lost opportunities update the date retroactively. Use **Created On** as the date property and filter by Status for stable historical counts.

**Q: Can I see opportunities broken down by pipeline stage?**

Yes. Use **Opportunity Counts by Status** or **Opportunity Counts Over Time** , then set **Group By → Stage**. To scope to a specific pipeline first, add a Pipeline condition filter.

**Q: What is "Lost Opportunities By Reason" showing if no Lost Reason was recorded?**

Opportunities marked Lost without a reason recorded will appear as a blank or "None" segment in the donut. To ensure clean data in this widget, make Lost Reason a required field in your pipeline settings.

**Q: How do the "For You" widgets behave for team members with different pipelines?**

"For You" widgets filter by the logged-in user's Assigned User value. They aggregate across all pipelines by default. Add a Pipeline condition to scope further.

**Q: Can I filter Opportunities Widgets by a specific pipeline stage without selecting the pipeline first?**

No. **Stage** is a dependent field — it requires a **Pipeline** to be selected first in the Conditions panel. Once a pipeline is selected, the stages within that pipeline become available.

**Q: Do Opportunities Widgets work with Quick Filters on the dashboard?**

Yes. Dashboard-level Quick Filters apply on top of any widget-level Conditions. If a widget has Status = Won set as a condition, a Quick Filter for Assignee will further narrow to won opportunities for that assignee.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073961599/original/GSBW2LnMxYtbuNu7S2w7uyA8lZyeHkvS_w.png?1781778184)

* * *

_For related articles, see:_

  * _What Are Dashboard Widgets?_ — <https://help.gohighlevel.com/support/solutions/articles/155000001212-what-are-dashboard-widgets->
  * _Customizing Dashboard Widgets_ — <https://help.gohighlevel.com/support/solutions/articles/155000001207-customizing-dashboard-widgets>
  * _How to Create & Add Dashboard Widgets_ — <https://help.gohighlevel.com/support/solutions/articles/155000001206-how-to-create-add-dashboard-widgets>
  * _Using Custom Fields in Sub-Account Dashboard Table Widgets_ — <https://help.gohighlevel.com/support/solutions/articles/155000006144-using-custom-fields-in-sub-account-dashboard-table-widgets>
  * _Contacts Widgets in Dashboards & Reports_ — <https://help.gohighlevel.com/support/solutions/articles/155000008108>

# Use Custom Fields as Metrics in Dashboards, Reports & Custom Metrics

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008495-use-custom-fields-as-metrics-in-dashboards-reports-custom-metrics](https://help.gohighlevel.com/support/solutions/articles/155000008495-use-custom-fields-as-metrics-in-dashboards-reports-custom-metrics)  
**Category:** Dashboards  
**Folder:** Configuring Dashboards

---

Numeric and monetary custom fields can be more than filters or grouping options in HighLevel reporting. Contact and Opportunity custom fields that store business-specific numbers—such as treatment cost, property value, or projected deal size can now be aggregated directly in dashboards and Custom Reports. This gives you more flexibility to measure the data that matters to your business without forcing it into a standard field.

* * *

**TABLE OF CONTENTS**

  * What Are Custom Field Metrics?
  * Key Benefits of Custom Field Metrics
  * Supported Fields and Aggregations
  * Where Custom Field Metrics Are Available
  * How To Setup Custom Fields as Metrics
    * Use a Custom Field in a Dashboard Widget or Custom Report
    * Use a Custom Field in a Custom Metric
  * Example: Reporting on Property Value
  * Frequently Asked Questions
  * Related Articles


* * *

# **What Are Custom Field Metrics?**

  


Custom field metrics turn eligible numeric and monetary values stored on Contacts or Opportunities into measurable reporting data. Instead of only filtering or grouping records by a custom field, you can calculate the Sum, Minimum, Maximum, or Average of its values and display the result in supported reporting tools.

For example, if your Opportunities contain a Monetary custom field named **Property Value** , you can calculate the total property value across won opportunities or identify the highest-value property in a selected period.

* * *

## **Key Benefits of Custom Field Metrics**

  


  * **Measure business-specific data:** Aggregate values such as property value, treatment cost, estimated project value, or other numeric information unique to your business.  
  


  * **Choose the calculation that fits your goal:** Apply Sum, Min, Max, or Average to the same custom field depending on the insight you need.  
  


  * **Report across multiple tools:** Use eligible custom fields in Dashboard widgets, Custom Reports, and the Custom Metric module.  
  


  * **Reduce manual reporting:** Analyze custom-field values directly in HighLevel instead of exporting the data for separate calculations.  
  


  * **Use new fields automatically:** Eligible custom fields become available as metrics when they are created without requiring a separate admin toggle or enablement step.


* * *

## **Supported Fields and Aggregations**

  


Custom field metrics are available for supported Contact and Opportunity fields that store numeric or monetary values. HighLevel separates the field you want to measure from the calculation applied to it, so the same custom field can be used to answer different reporting questions.

  


Supported custom field metrics include:  
  


  * **Objects:** Contacts and Opportunities

  * **Field types:** Number and Monetary custom fields

  * **Aggregations:**

    * **Sum:** Adds all applicable values together.

    * **Min:** Displays the lowest applicable value.

    * **Max:** Displays the highest applicable value.

    * **Average:** Calculates the average of all applicable values.  
  


When configuring a metric, use the two separate dropdowns in the metric picker:  
  


  1. **Field:** Select the custom field you want to measure, such as **Property Value**.

  2. **Aggregation:** Select how HighLevel should calculate that field, such as **Sum** , **Min** , **Max** , or **Average**.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079393116/original/VbeOjw6UXnlQS9FAHBapomzJYsR2Bsu6Ig.png?1787788359)

  
  


For example, to calculate the total property value across a set of Opportunities, select **Property Value** as the Field and **Sum** as the Aggregation. You will not see a combined option such as **Sum of Property Value** in the Field dropdown.  
  


If you need to create a supported custom field first, see **[Creating and Managing Custom Fields for Better Data Organization.](<https://help.gohighlevel.com/support/solutions/articles/155000008466-creating-and-managing-custom-fields-for-better-data-organization>)**

  

    
    
    **Note:** Eligible custom fields are added to the metric picker automatically, so no additional setup or enablement is required after the field is created.

* * *

## **Where Custom Field Metrics Are Available**

  


Custom field metrics can be used across HighLevel's primary reporting experiences, allowing the same business-specific data to support quick dashboard monitoring, shareable reports, and more advanced calculated KPIs.

  


Eligible Contact and Opportunity custom fields are available as metrics in:  
  


  * **Dashboard widgets:** Add the aggregated value to a dashboard for ongoing KPI monitoring.  
  


  * **Custom Reports:** Use custom-field metrics inside report widgets alongside other reporting data.  
  


  * **Custom Metric module:** Include eligible custom-field metrics when building supported calculated KPIs.


[](<https://help.gohighlevel.com/support/solutions/articles/155000001212?utm_source=chatgpt.com>)

* * *

## **How To Setup Custom Fields as Metrics**

  


Proper setup starts with an eligible custom field and then depends on where you want to use that metric. Dashboard widgets and Custom Reports use metric configuration controls, while the Custom Metric module uses a formula builder for combining metrics and calculations.

  


### **Use a Custom Field in a Dashboard Widget or Custom Report**

  


Dashboard widgets and Custom Reports let you measure the values stored in an eligible custom field by pairing the field with a supported aggregation.

  


  1. **Confirm that the custom field is eligible.**  
Verify that the field belongs to either Contacts or Opportunities and uses a Number or Monetary field type.  
If the field does not exist yet, create it under **Settings > Custom Fields**. Choose the correct object when creating the field because a Contact custom field cannot later be converted into an Opportunity custom field, or vice versa.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079393542/original/aPFft1ih86s0pI6SMjmb6Y4KDDw9N2V0lA.png?1787790602)  
  

  2. **Open the reporting destination and Edit.**  
Open the Dashboard widget or Custom Report where you want to use the custom field.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079393576/original/Sjvckdd8k2rhLJ_HrJc52EIwR3rJJ8EuVg.png?1787790676)  
  

  3. **Add or configure the metric and Select the custom field.**  
Open the metric configuration for the widget. Choose the Number or Monetary custom field you want to measure, such as **Property Value**.  
  

  4. **Choose the aggregation.**  
Select the calculation you want HighLevel to apply: Sum, Min, Max or Average  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079393600/original/bSqoI6UpWgB2G4wlRJ2IW84jRfEu-tvuNA.png?1787790737)  
  

  5. **Add filters or a View By when needed.**  
Refine the metric to answer a more specific reporting question. For example, filter Opportunities to won records or group the results by another supported field.  
  

  6. **Save the widget or report configuration.**  
  


### **Use a Custom Field in a Custom Metric**

  


Custom Metrics let you combine individual metrics into formulas for more advanced KPI calculations. The formula builder provides separate options for adding metrics, mathematical operators, and fixed numbers.  
  


  1. **Open the Custom Metric module and create a new Custom Metric.**  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079393628/original/_7dlEiHDoXXXRbYVulqrlre96ckNooRO_A.png?1787790820)**  

  2. **Enter the Metric name and select the Display format.**
  3. **Add a metric to the Formula builder.**  
Select the metric you want to use. Custom-field metrics can be included when available.  
  

  4. **Click the + button to add another formula component.**
  5. **Choose what you want to add:**
     * **Metrics**
     * **Operator**
     * **Number**
  6. **If you select Operator, choose the mathematical operation you want to use:**
     * +
     * −
     * *
     * /
     * (
     * )  
  

  7. **Continue building the formula as needed.**  
Custom Metrics support formulas containing multiple metrics.  
  

  8. **Configure the comparison value behavior.**  
Select whether an increase or decrease should be considered positive for the metric.  
  

  9. **Click Create/Update to save the Custom Metric.**  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079393651/original/q0HESvoeXJy9qh7oO_NLxyBJVbEZ8JrVcA.png?1787790919)**


* * *

## **Example: Reporting on Property Value**

  


A practical example shows how the same custom field can answer different business questions simply by changing the aggregation, filters, or reporting dimension. This allows one field to support several KPIs without creating duplicate fields for each calculation.

  


Suppose a real estate agency stores **Property Value** as a Monetary custom field on each Opportunity.  
  


  * **Total value of won properties:** Select **Property Value** as the Field and **Sum** as the Aggregation, then filter the results to won opportunities. When the applicable reporting period is set to the current month, the metric can show the total property value represented by won opportunities for that period.  
  


  * **Largest property value:** Select **Property Value** as the Field and **Max** as the Aggregation to identify the highest applicable property value.  
  


  * **Property value by property type:** Use **Property Value** as the metric and add **Property Type** as the View By/dimension to compare values across categories.  
  


The custom Monetary field in this example is separate from HighLevel's built-in Opportunity Monetary Value. A custom field stores a value defined for your specific business process, while standard Opportunity value metrics use HighLevel's built-in opportunity data.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079393146/original/0fvm6xOjwSAK0dRqM482AfbLPnqdQKlASw.png?1787788543)

* * *

## **Frequently Asked Questions**

  


**Q: Why is my custom field not appearing in the Field dropdown?**

Confirm that the custom field belongs to either Contacts or Opportunities and uses a supported numeric/Number or Monetary field type. Custom-field availability can depend on the object, field type, and reporting component being configured.  
  


**Q: Can I change a Contact custom field into an Opportunity custom field if I created it under the wrong object?**

No. The object associated with a custom field cannot be changed after the field is created. Create a new field under the correct object instead.  
  


**Q: Is a Monetary Opportunity custom field the same as Opportunity Monetary Value?**

No. Opportunity Monetary Value is a standard HighLevel opportunity value used by built-in Opportunity reporting. A Monetary custom field is a separate field created for business-specific information, such as Property Value or Estimated Project Cost.  
  


**Q: Can I use filters or grouping with a custom field metric?**

Yes. Supported reporting configurations can combine a custom-field metric with filters or a View By/dimension. For example, Property Value can be summed for won opportunities and then analyzed by Property Type.  
  


**Q: Do Dashboard widgets, Custom Reports, and Custom Metrics have the same plan availability?**

Not necessarily. HighLevel's reporting features can have different plan requirements. Review the dedicated Custom Metrics documentation for the current availability of that module rather than assuming access to one reporting feature automatically includes every reporting feature.  
  


**Q: What should I do if I need the same custom field calculated in different ways?**

Select the same custom field as the Field and choose the aggregation appropriate to each reporting use case. For example, **Sum** can measure the combined value while **Max** can identify the highest value.

* * *

## **Related Articles**

  


  * [How to Create and Use Custom Metrics for Dashboard Reports](<https://help.gohighlevel.com/support/solutions/articles/155000005903-how-to-create-and-use-custom-metrics?utm_source=chatgpt.com>)  
  


  * [Creating and Managing Custom Fields for Better Data Organization](<https://help.gohighlevel.com/support/solutions/articles/155000008030-creating-and-managing-custom-fields-for-better-data-organization?utm_source=chatgpt.com>)  
  


  * [How to Use Custom Fields for Opportunities in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000000521-how-to-use-custom-fields-for-opportunities?utm_source=chatgpt.com>)  
  


  * [Opportunities Widgets in Dashboards & Reports](<https://help.gohighlevel.com/support/solutions/articles/155000008109-opportunities-widgets-in-dashboards-reports?utm_source=chatgpt.com>)  
  


  * [How to Create a Custom Report, Schedule and Export Report as PDF](<https://help.gohighlevel.com/support/solutions/articles/155000003965-how-to-create-and-schedule-reports?utm_source=chatgpt.com>)  
  


  * [What Are Dashboard Widgets?](<https://help.gohighlevel.com/support/solutions/articles/155000001212?utm_source=chatgpt.com>)

# Workflow Trigger - Opportunity Created

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003499-workflow-trigger-opportunity-created](https://help.gohighlevel.com/support/solutions/articles/155000003499-workflow-trigger-opportunity-created)  
**Category:** Workflows  
**Folder:** Opportunity Workflow Triggers

---

The **Opportunity Created trigger** allows users to automate workflows when a new opportunity is created in the system. This trigger is valuable for automating actions like notifications, follow-ups, and task assignments based on the creation of a new sales opportunity in your pipeline.

* * *

**TABLE OF CONTENTS**

  * Trigger Name: Opportunity Created Trigger
  * Trigger Description
  * Trigger Details
  * How to Configure
  * Example


* * *

## **Trigger Name:****Opportunity Created Trigger**

  


### **Trigger Description**

  
The Opportunity Created trigger is activated when a new opportunity is created in the system. This allows you to automate processes such as assigning tasks, notifying team members, or updating the status based on opportunity characteristics such as pipeline stage, lead value, or the assigned user.

  


### **Trigger Details**

  


Field Name| Description| Mandatory  
---|---|---  
Assigned To| The user assigned to the opportunity| No  
Has Tag| Filter opportunities based on specific tags| No  
In Pipeline| Select the pipeline to track the opportunity| No  
Lead Value| The monetary value associated with the lead| No  
Lost Reason| The reason provided for marking an opportunity as lost| No  
Status| The current status of the opportunity (New, Open, etc.)| No  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033069568/original/_veN8lgt5BolbVsdYDxR3sw3dRYxUnbLWg.png?1726650717)

  


Operator| Description  
---|---  
Equals to| Matches the exact value  
Greater than| Value should be greater than the input  
Less than| Value should be less than the input  
Contains| Value contains the given string  
Is Empty| The field is empty  
Is Not Empty| The field is not empty  
  
* * *

## **How to Configure**  
**  
**

  * **Select Trigger** : In the workflow builder, choose _Opportunity Created_ as your trigger.  
  


  * **Assign a Trigger Name** : Give the trigger a meaningful name, such as “High Value Lead Opportunity Created.”  
  


  * **Filters** :  
  


    * **Assigned To** : Filter opportunities based on which user it’s assigned to.  
  

    * **Pipeline** : Filter opportunities in specific pipelines.  
  

    * **Lead Value** : Set criteria based on the opportunity’s monetary value.  
  

  * **Tag:** Use Tag filters to include/exclude opportunities by tags. Tag supports multi-select operators (Equals to / Not equals to / Any of / None of) and you can add multiple Tag filters for advanced rules.  
**  
**

  * **Add Multiple Filters** : If necessary, apply additional filters by clicking **Add filters** and selecting the desired fields and conditions.


* * *

## **Example**

  
**Scenario** : You want to notify the sales manager when a new opportunity with a lead value greater than $10,000 is created in the pipeline.  
  


  * **Trigger** : Opportunity Created  
  

  * **Filter** : Lead Value greater than $10,000  
  

  * **Action** : Notify the sales manager


  
This setup ensures that significant opportunities are flagged and acted upon promptly by notifying key stakeholders.

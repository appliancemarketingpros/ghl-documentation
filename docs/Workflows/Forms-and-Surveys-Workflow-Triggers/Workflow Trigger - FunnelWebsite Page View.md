# Workflow Trigger - Funnel/Website Page View

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003498-workflow-trigger-funnel-website-page-view](https://help.gohighlevel.com/support/solutions/articles/155000003498-workflow-trigger-funnel-website-page-view)  
**Category:** Workflows  
**Folder:** Forms and Surveys Workflow Triggers

---

**TABLE OF CONTENTS**

  * Overview
  * Trigger Name
  * Trigger Description
  * How to Configure
  * Example


##   


## Overview

The **Funnel/Website PageView** trigger allows users to automate actions when a contact views a specific page on a funnel or website. By tracking these page views, you can trigger various automations based on page-specific behavior, such as sending a follow-up email or tagging a contact based on their interaction with your content.

  


## Trigger Name

**Funnel/Website PageView**

  


## Trigger Description

This trigger activates when a contact visits a specified funnel or website page. It helps to automate actions based on which pages your leads or customers are visiting, allowing for personalized follow-up or specific actions to be executed.

  


## Trigger Details

  


Field Name| Description| Mandatory  
---|---|---  
Funnel/Website| Specifies which funnel or website to monitor| Yes  
Page| Defines the specific page to monitor within the funnel/website| No  
UTM Campaign| Tracks visits associated with a specific UTM campaign| No  
UTM Source| Tracks visits associated with a specific UTM source| No  
UTM Medium| Tracks visits associated with a specific UTM medium| No  
UTM Content| Tracks visits associated with a specific UTM content| No  
Page Path| Specifies a specific page path for more refined tracking| No  
  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033068980/original/nRQNQfh7_KzYG6muqLyfvI2cQK3yLIXCrw.png?1726650432)

##   


Operator| Description  
---|---  
Is| The value must exactly match the given input  
Is any of| The value can be one of the listed options  
Is none of| The value should not be one of the listed options  
Is empty| The field must be empty  
Is not empty| The field should not be empty  
  
##   


## How to Configure

  * **Select Trigger** : Start by choosing the _Funnel/Website PageView_ trigger from the list of available triggers in the workflow builder.

  * **Assign a Name** : Set a meaningful name for the trigger such as "Funnel Page Visit - Checkout."

  * **Filters** :

    * **Funnel/Website** : Select the specific funnel or website you want to monitor.
    * **Page** : Optionally, specify the exact page you want to track.
    * **UTM Parameters** : Set filters like UTM Campaign, Source, or Medium to refine the page view conditions.
  * **Add Multiple Filters** : You can add additional filters to monitor specific pages, paths, or UTM campaigns as needed by clicking on **Add filters**.


  


## Example

**Scenario** : You want to track when visitors reach the “Checkout” page of your funnel and then send them a follow-up email if they abandon their cart.

  * **Trigger** : Funnel/Website PageView
  * **Funnel/Website** : Funnel Name (e.g., Bookkeeper Funnel)
  * **Page** : Is equal to “Checkout”
  * **Action** : Send a follow-up email offering assistance after a specific amount of time if no purchase is completed.


This setup allows you to re-engage customers who might have dropped off at the final stage of purchasing.

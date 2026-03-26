# Workflow Action - Review Request

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003291-workflow-action-review-request](https://help.gohighlevel.com/support/solutions/articles/155000003291-workflow-action-review-request)  
**Category:** Workflows  
**Folder:** Communication Workflow Actions

---

**TABLE OF CONTENTS**

  * Overview
  * Action Name
  * Action Description
  * Action Details
  * Example


##   


## Overview

The **Review Request** action allows you to send a request to your contacts asking them to provide feedback or reviews. This action can be customized to send requests via different communication channels such as email or SMS.

  


## Action Name

**Review Request**

  


## Action Description

This action sends a review request to a contact. You can specify the type of review request (e.g., via email) and configure the content of the message through the Reputation Settings.

#### 

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032221015/original/vbIkWRX96_oJbKXra9qskIpF1P5hdNdk3A.png?1725443273)

  


Field| Description| Mandatory  
---|---|---  
Action Name| The name of the action. Default is "Send Review Request".| Yes  
  
Review Type| Select the type of review request. Options include "E-mail" and potentially other channels (e.g., SMS).| Yes  
  
  


### How to Configure

  1. ### **Action Name** : Set a name for the action. By default, it's "Send Review Request".

  2. **Review Type** : Choose the type of review request from the dropdown menu. For example, select "E-mail" to send the review request via email.
  3. **Message Configuration** : Configure the actual message content that will be sent out in the review request by clicking on the "Reputation Settings" link. This will allow you to customize the message template, ensuring that the request aligns with your branding and communication style.


##   


## Example

To set up a review request action effectively, consider the following workflow configuration:

  1. **Trigger** : Select a trigger such as "Appointment Completed".
  2. **Action** : Configure the action as follows:
     * **Action Name** : "Send Review Request".
     * **Review Type** : "E-mail".
     * Configure the message template in the Reputation Settings to include details like:
       * A thank you note for the appointment.
       * A request for feedback.
       * A link to the review platform.


  


By configuring the action in this manner, you ensure that contacts receive timely and relevant requests for feedback, helping you to gather valuable customer insights and enhance your business reputation.

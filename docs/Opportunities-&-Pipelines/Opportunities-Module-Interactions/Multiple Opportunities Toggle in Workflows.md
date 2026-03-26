# Multiple Opportunities Toggle in Workflows

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003440-multiple-opportunities-toggle-in-workflows](https://help.gohighlevel.com/support/solutions/articles/155000003440-multiple-opportunities-toggle-in-workflows)  
**Category:** Opportunities & Pipelines  
**Folder:** Opportunities Module Interactions

---

TABLE OF CONTENTS

  * Overview
  * Setting Name
  * Setting Description
  * How to Configure
  * Example


##   


## Overview

Currently, only the most recent opportunity associated with a contact enters the workflow. However, with the introduction of the "Allow Multiple Opportunity" feature, users can enable workflows to handle multiple opportunities for the same contact. Each contact-opportunity pair will have its own distinct workflow execution, allowing more precise and effective management of opportunities.

  


## Setting Name

Allow Multiple Opportunity

  


## Setting Description

  


Once the "Allow Multiple Opportunity" toggle is enabled:

  


Each opportunity associated with a contact will enter the workflow as a separate execution.
    
    
    Any updates made to the opportunity will not restart the workflow. Instead, the workflow will continue from the stage it is at, and the updated opportunity values will be used going forward.

* * *

## How to Configure

To enable this feature, follow these steps:

  1. Navigate to Settings > Objects > Opportunities  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067256405/original/E55qlGbBoXq24bbpZ6yiHBRHxM0qcjGvjQ.png?1773859304)  

  2. Locate the "Allow Multiple Opportunity" Toggle:
     * Find the new toggle at the top of the settings, similar to the "Allow Re-entry" option.  
  

  3. Enable the Toggle:
     * Toggle the Allow Multiple Opportunity switch to "ON" to activate the feature.  
  

  4. Save Changes: Make sure to save the settings.


* * *

## Example

Let's say you are a Real Estate agent who is connecting with a client for two different properties. Hence, you have a contact "John Doe" with two opportunities "1 Madison Avenue" and "2 Nice Street"

  
You have a workflow which is triggered whenever an opportunity is updated and sends a reminder SMS to the contact for 2 days

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032844678/original/rV7XzET3MI-S_nCYXzPuWQ5hMetF-kpbeA.jpeg?1726238737)

  
  


**If "Allow Multiple Opportunity" is "OFF" :**

  


1 Madison Avenue is updated on 1/1/2024 8 AM and an SMS is sent to John Doe 

2 Nice Street is updated on 1/1/2024 12 PM and the rest of the actions will be skipped.

  


**Whereas, if " Allow Multiple Opportunity" is "ON" :**

  


1 Madison Avenue is updated on 1/1/2024 8 AM and an SMS is sent to John Doe 

2 Nice Street is updated on 1/1/2024 12 PM and another SMS will be sent to John Doe

Hence, both the opportunities will co-exist in the system.

  


##

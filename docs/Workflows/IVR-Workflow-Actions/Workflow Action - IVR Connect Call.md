# Workflow Action - IVR Connect Call

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003371-workflow-action-ivr-connect-call](https://help.gohighlevel.com/support/solutions/articles/155000003371-workflow-action-ivr-connect-call)  
**Category:** Workflows  
**Folder:** IVR Workflow Actions

---

**TABLE OF CONTENTS**

  * Overview
  * Action Name
  * Action Description
  * Action Details
  * Example


##   


## Overview

The **Connect Call (IVR)** action allows you to transfer an ongoing call to another phone number, user, or agent. This can be useful for routing calls to specific departments, agents, or external phone numbers in a call center or IVR system. Additionally, the action allows advanced settings like voicemail detection, call recording, timeout, and time limits for connected calls.

  


## Action Name

**Connect Call (IVR)**

  


## Action Description

The **Connect Call (IVR)** action provides functionality to transfer an ongoing call from the IVR system to another phone number or user. You can choose multiple users to call in parallel and set custom numbers. This action also supports advanced features such as detecting voicemail, recording calls, and setting timeout and time limits for the connected call.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032467994/original/yEZzn_vVkBxvrg-S8UQGevn5_pVJTB-qqg.png?1725822997)

  


### **How to Configure:**

  1. **Action Name** : Provide a name for the action, such as "Transfer to Agent" or "Connect to Sales Department".

  2. **Connect Call To** : Specify the user or custom phone numbers where the call should be transferred. You can select up to 10 users to call simultaneously.

  3. **Advanced Settings** :

     * **Detect Voicemail** : Enable this feature if you want to detect if the call goes to voicemail. Enabling this option may introduce a small delay.
     * **Record Call** : Toggle this setting to record the transferred call for later review.
     * **Timeout (Seconds)** : Set the number of seconds to wait for the called party to answer the call (e.g., 30 seconds).
     * **Time Limit (Seconds)** : Set the maximum duration of the connected call. For example, if you want the call to automatically disconnect after 1 hour, you would set this to 3600 seconds.
     *   


Field Name| Description| Mandatory  
---|---|---  
Action Name| Provide a name for the action.| Yes  
Connect Call To| Specify the phone numbers or users to connect the call to.| Yes  
Select Users| Choose from existing users or add custom numbers to transfer the call to.| Yes  
Detect Voicemail| Toggle to enable voicemail detection for the call.| No  
Record Call| Enable to record the transferred call for quality or compliance purposes.| No  
Timeout (Seconds)| Set the maximum time in seconds to wait for the called party to answer.| Yes  
Time Limit (Seconds)| Set the maximum duration for the connected call in seconds (up to 24 hours).| No  
  
##   


## Example

**Scenario** : A customer calls the sales department through the IVR system, and the system automatically transfers the call to an available sales agent.

  * **Action Name** : "Transfer call to Sales Agent"
  * **Connect Call To** : Select the sales agent’s phone number or custom numbers.
  * **Advanced Settings** : Enable call recording, set timeout to 30 seconds, and set a time limit of 1 hour for the call duration.

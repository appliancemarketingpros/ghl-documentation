# Workflow Action - IVR Gather Input On Call

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003370-workflow-action-ivr-gather-input-on-call](https://help.gohighlevel.com/support/solutions/articles/155000003370-workflow-action-ivr-gather-input-on-call)  
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

The **Gather Input On Call** action enables users to gather inputs via keypad from the caller. This can be used in IVR systems where the caller is prompted to press certain keys to make a selection (e.g., "Press 1 to speak to support, Press 2 to leave a message"). This action helps automate responses and proceed based on the inputs from the user.

  


## Action Name

**Gather Input On Call**

  


## Action Description

The **Gather Input On Call (IVR)** action collects information from the caller through DTMF (Dual Tone Multi-Frequency) inputs. It is typically used in IVR flows, where the user interacts with the system by pressing keys on their phone. Based on the keypress, different branches can be defined, allowing for customized flows depending on the input.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032467893/original/UcwBIizZxLaiHIF6_C7pXEdsTOKADGR4dg.png?1725822507)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032467902/original/GGJsEM9GZ_TeC1H01k3e01ossdpOH4BbWA.png?1725822537)

##   


### **How to Configure:**

  1. **Action Name** : Set a relevant name for this IVR input gathering action.

  2. **Say or Play Message** : Choose between "Say a message" (text-to-speech) or uploading a pre-recorded audio file.

  3. **Text to Say** : If "Say a message" is chosen, provide the message that will be played (e.g., "Press 1 for support").

  4. **Language** : Select the language for the text-to-speech.

  5. **Message Voice** : Select whether you want a "Man" or "Woman" voice for the text-to-speech message.

  6. **Number of Loops** : Define how many times the message will be repeated before proceeding.

  7. **Advanced Settings** : Set a timeout (in seconds) after which input gathering stops and optionally stop the input gathering when the user presses a key.

  8. **Match Conditions** : Use this feature to create branches based on the caller’s input. For example:

     * Branch 1: Press "1" for Support
     * Branch 2: Press "2" for Sales


  


Field Name| Description| Mandatory  
---|---|---  
Action Name| Provide the name of the action.| Yes  
Say or Play Message| Choose whether to say a message or play a pre-recorded audio file.| Yes  
Text to Say| If "Say a message" is selected, input the text to be said to the caller.| Yes  
Language| Select the language in which the message should be spoken.| Yes  
Message Voice| Choose between male or female voice.| Yes  
Number of Loops| Select the number of times the message should be played or repeated.| Yes  
Stop Gathering After (Seconds)| Set the duration (in seconds) after which the gathering stops.| Yes  
Stop Gathering After (Digits)| Specify how many digits to collect before stopping input collection.| No  
Stop Gathering on Key Press| Enable this to stop gathering input once a key is pressed.| No  
Match Conditions| Option to define branches based on key press values.| Yes  
  
  


## Example

**Scenario** : Collecting input from a caller for a bank's IVR system.

**Message** : "Press 1 to hear your bank statement, Press 2 to connect with an agent, or Press 3 to exit."

**Key Presses** :

  * Pressing "1" directs the user to a branch that reads their bank statement.
  * Pressing "2" directs the caller to a customer support agent.
  * Pressing "3" terminates the call after thanking the customer.

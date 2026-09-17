# Workflow Action - IVR End Call

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003372-workflow-action-ivr-end-call](https://help.gohighlevel.com/support/solutions/articles/155000003372-workflow-action-ivr-end-call)  
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

The **End Call (IVR)** action allows the IVR system to immediately disconnect a call. Alternatively, you can choose to play a final message or custom audio before ending the call. This is useful when you want to wrap up an IVR interaction or provide an informational message before disconnecting.

  


## Action Name

**End Call**

  


## Action Description

The **End Call (IVR)** action disconnects a call immediately. Optionally, users can configure a custom message or audio to be played before ending the call. This feature is useful for delivering a final message or confirmation to the caller before disconnection.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032468051/original/hx11NzrEWZfe8i3H0wvJPK-ZU8cUKqRhNw.png?1725823415)

  


### How to Configure

  1. **Action Name** : Set a name for this action to identify it within your workflow.
  2. **Add Voice Instructions** : Enable this toggle if you want to provide a final message before the call ends. Otherwise, the call will disconnect immediately.
  3. **Say or Play Message** : Select whether to use a text-to-speech message ("Say a message") or an uploaded audio file ("Play audio file").
  4. **Text to Say** : If "Say a message" is selected, enter the text to be spoken to the caller.
  5. **Language** : Choose the language for the text-to-speech message.
  6. **Message Voice** : Select the voice type (Man or Woman) for the text-to-speech message.
  7. **Number of Loops** : Specify how many times the message should be repeated (default is 1).


  


Field Name| Description| Mandatory  
---|---|---  
Action Name| Name for this action in the workflow| Yes  
Add Voice Instructions| Toggle to enable or disable adding a final message before ending the call| No  
Say or Play Message| Choose between "Say a message" or "Play audio file" to deliver the final message| No  
Text to Say| Input the text that will be converted to speech and played to the caller| No  
Language| Select the language of the text-to-speech voice| No  
Message Voice| Choose between "Man" or "Woman" for the text-to-speech voice| No  
Number of Loops| Number of times to loop the final message (Default is 1)| No  
  
  


##   


## Example

**Scenario** : At the end of a customer service call, you want to confirm that the system is going to disconnect and thank the customer for their call.

  * **Action Name** : End IVR Call
  * **Add Voice Instructions** : Enabled
  * **Say or Play Message** : Say a message
  * **Text to Say** : "Thank you for calling ABC Services. Your call will now end."
  * **Language** : English (US)
  * **Message Voice** : Woman
  * **Number of Loops** : 1


When configured, the system will play the message and then disconnect the call automatically.

###   


## Additional Notes:

  * If **Add Voice Instructions** is disabled, the call will end immediately without any final message.
  * Using text-to-speech can be effective for providing dynamic, real-time information before ending a call.

# Workflow Action - Record Voicemail

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003373-workflow-action-record-voicemail](https://help.gohighlevel.com/support/solutions/articles/155000003373-workflow-action-record-voicemail)  
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

The **Record Voicemail (IVR)** action allows users to record audio messages from callers. This feature enables callers to leave voice messages during the call flow. You can also configure the message to end automatically after a period of silence, on keypress, or when the maximum time length is reached. The recorded voicemail can be accessed within the conversation section.

  


## Action Name

**Record Voicemail (IVR)**

  


## Action Description

This action allows the IVR to collect audio recordings from callers as voicemail. The action supports additional configurations such as when to stop recording based on silence, keypress, or time limit. You can also provide instructions to the caller before they start recording.

  


## Action Details

[![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032468108/original/GV9HD1jqFuQsW1h8MADN-2tzB9-6iTJGGw.png?1725823639)](<https://help.gohighlevel.com/en/support/solutions/articles/155000003372-workflow-action-ivr-end-call>)

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032468111/original/lTXQBsegzr59AJicaT9O7cKiK50k0i07pA.png?1725823666)

### How to Configure:

  1. **Action Name:** Choose a unique name for this voicemail action (e.g., "Record voicemail").
  2. **Play Beep:** Optionally play a beep to indicate the recording has started.
  3. **Stop Recording After (Seconds of Silence):** Define the period of silence after which recording will stop. This is set in seconds.
  4. **Stop Recording on Keypress:** The caller can stop the recording by pressing a designated key on the keypad (e.g., #).
  5. **Max Recording Length:** Set the maximum duration of the voicemail recording in seconds.
  6. **Add Voice Instructions (Optional):** Enable this to add pre-recorded voice instructions for the caller.


  


Field Name| Description| Mandatory  
---|---|---  
Action Name| Name of the voicemail action| Yes  
Play Beep| Plays a beep sound indicating the recording has started| No  
Stop Recording After| Number of seconds of silence before the recording automatically stops| Yes  
Stop Recording on Keypress| Specific key the caller can press to stop the recording (e.g., 1-9, #, *)| No  
Max Recording Length| The maximum length of the voicemail in seconds| Yes  
Add Voice Instructions| Say a message or upload a recorded message to instruct the caller| No  
  
  


## Example

Suppose you want to record a voicemail when the customer doesn’t respond to the menu. Here’s how you can configure it:

  * **Action Name:** “Record Customer Voicemail”
  * **Play Beep:** Yes (Enable it to play a beep)
  * **Stop Recording After (Seconds of Silence):** 5 (Wait for 5 seconds of silence before stopping)
  * **Stop Recording on Keypress:** # (Allow the customer to stop the recording by pressing the hash key)
  * **Max Recording Length:** 360 (Record for a maximum of 6 minutes)
  * **Add Voice Instructions:** "Please record your message after the beep." (Enable to give the caller this instruction)


  


## Additional Notes

  * **Stop Recording on Silence:** This setting is useful to automatically stop the recording if the caller does not respond for a certain time.
  * **Recording Keypress:** Useful for providing the caller a quick method to stop recording when they are done.
  * **Max Recording Length:** Ensure that this is set according to your system requirements to avoid exceeding maximum storage limits.

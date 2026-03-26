# Workflow Action - Voicemail

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003275-workflow-action-voicemail](https://help.gohighlevel.com/support/solutions/articles/155000003275-workflow-action-voicemail)  
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

The Voicemail action allows you to send a pre-recorded voicemail directly to a contact. This can be useful for follow-ups, notifications, or delivering specific messages without engaging in a live call.

  


## Action Name

**Voicemail**

  


## Action Description

Sends a pre-recorded voicemail file to the selected contact.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032066704/original/S5yOIgMvdxybPNVPONEqVuXi7sUy1IQMiw.png?1725274416)

  


Field| Description| Mandatory  
---|---|---  
Action Name| The name of the action, which is set as "Voicemail".| Yes  
Drop Your File| Upload the pre-recorded voicemail file you wish to send. The file format should be compatible with voicemail playback.| Yes  
  
  


**How to Configure:**

  1. **Name the Action:** Under "Action Name," ensure it reads "Voicemail" to identify the action being taken.
  2. **Upload the File:** Click on the "Upload file" button to choose a pre-recorded voicemail message from your local system. Once uploaded, you can play the message to ensure it's the correct one.
  3. **Save:** After configuring, ensure to save the workflow to apply these changes.


  


**Some Triggers (But not limited to)**

To use the Voicemail action effectively, consider combining it with the following triggers:

  1. **Appointment No-Show:** If a contact misses a scheduled appointment, automatically send them a voicemail to reschedule.
  2. **Follow-Up Reminder:** Trigger a voicemail if a contact hasn’t responded to previous communications within a set time frame.


##   


## Example

  * **Trigger:** "Appointment Status Changes" changed to "No-Show"
  * **Action:** "Voicemail"
  * **Uploaded File:** "Reschedule.mp3" (a pre-recorded message encouraging the contact to reschedule their missed appointment)


In this example, the workflow will detect if a contact does not show up for an appointment and automatically send a voicemail to encourage them to reschedule, improving engagement without the need for manual follow-up.

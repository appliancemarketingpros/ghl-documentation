# Workflow Action - IVR Say/Play

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003369-workflow-action-ivr-say-play](https://help.gohighlevel.com/support/solutions/articles/155000003369-workflow-action-ivr-say-play)  
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

The **Say/Play** action allows you to provide instructions or information to callers via either text-to-speech or pre-recorded audio. This action is part of an IVR (Interactive Voice Response) system, which helps guide callers through options or deliver important messages.

  


## Action Name

**Say/Play**

  


## Action Description

This action lets you configure whether to play a text-to-speech message or a pre-recorded audio message to the caller. It can be used for greetings, instructions, or any other information to be conveyed in a phone call.

  


## Action Details

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032467835/original/NB9MGkUup5hqPvn782YDAT8EHar4UBS8-A.png?1725822187)

  


### How to Configure

  1. **Say or Play Message** : Choose whether you want to say a message (text-to-speech) or play a message (pre-recorded audio).

     * **Say a message** : Input the text you want to convert to speech.
     * **Play a message** : Upload an audio file to be played to the caller.
  2. **Text to Say** : If you selected "Say a message," type the text that the system will read aloud.

  3. **Language** : Select the language in which the message should be spoken. Only English is supported for this

  4. **Message Voice** : Choose whether the voice will be male or female.

  5. **Number of Loops** : Set the number of times you want the message to be played. Default is 1.


  


  


## Field Name| Description| Mandatory  
---|---|---  
Say or Play Message| Choose between text-to-speech or playing a pre-recorded audio message| Yes  
Text to Say| The text that will be converted to speech (if text-to-speech is selected)| No (only for text-to-speech option)  
Language| The language in which the text will be spoken| Yes  
Message Voice| Select the type of voice (e.g., male or female) for the text-to-speech| Yes  
Number of Loops| Number of times the message should be repeated| No  
  
  


## Example

If you're setting up a welcome message for a customer service IVR, you might configure it like this:

  * **Action Name** : Welcome Message to the Caller
  * **Say or Play Message** : Say a message
  * **Text to Say** : "Hello, welcome to ABC Services. Please press 1 for Sales, 2 for Support."
  * **Language** : English (US)
  * **Message Voice** : Woman
  * **Number of Loops** : 1


  


## Additional Notes

  * For pre-recorded audio, ensure the file is in a compatible format (e.g., MP3).
  * Adjust the number of loops depending on the type of message and its importance.

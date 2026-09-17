# Workflow Action - Appointment Booking Conversation AI Booking Bot

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003363-workflow-action-appointment-booking-conversation-ai-booking-bot](https://help.gohighlevel.com/support/solutions/articles/155000003363-workflow-action-appointment-booking-conversation-ai-booking-bot)  
**Category:** Workflows  
**Folder:** Appointments Workflow Actions

---

**TABLE OF CONTENTS**

  * Overview
  * Action Name
  * Action Description
  * Action Details
  * Example


##   


## Overview

The "**Appointment Booking Conversation AI Bot** " is designed to automate appointment bookings by engaging in a conversation with the contact. It aims to guide the user towards booking an appointment, and it adjusts its flow depending on the user's responses.

##   


## Action Name

**Appointment Booking Conversation AI Bot**

  


## Action Description

This action uses AI to assist the contact in booking an appointment through a conversational interface. The bot can be customized with specific instructions, personality traits, and timeouts for improved interaction.

  


## Action Details

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032467476/original/G_Zs1ZabHgVz4i9LzKzuQ0E_H6-OGXuCXg.png?1725820371)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032467481/original/YzdtxNSpkSohH4c9NZIETdRMeLVl14G47Q.png?1725820404)

##   


### How to Configure

  1. **Calendar:** Select the calendar where appointments are managed.
  2. **Personality:** Define how the bot will interact with the contact. For example, you can set it to be friendly, professional, etc.
  3. **Additional Instructions:** Provide guidelines like conversational tips or specific reminders for the bot.
  4. **Message Limit:** Set a limit for how many back-and-forth messages can be exchanged before the bot stops trying to book an appointment.
  5. **Timeout:** Set how long the bot will wait for the user’s reply.
  6. **Channel:** Choose the communication medium (e.g., SMS, chat) through which the conversation will take place.
  7. **Disable Confirmation Message:** Check this box if you do not want the bot to send a confirmation after the appointment is booked.


  


Field Name| Description| Mandatory  
---|---|---  
Calendar| The calendar where appointments are booked.| Yes  
Personality| Instructions about the tone or style of the conversation the bot should follow.| Yes  
Additional Instructions| Additional notes or guidelines the bot should follow during the conversation.| No  
Maximum Messages Limit| The maximum number of messages the bot will send before marking the appointment as not booked.| Yes  
Timeout (Value)| The time for which the bot will wait for the contact's reply before it times out.| Yes  
Timeout (Unit)| The time unit for the timeout (minutes, hours, or days).| Yes  
Channel| The communication channel through which the bot sends messages (e.g., SMS, email).| Yes  
Don't let the bot send confirmation message| Option to disable the confirmation message sent by the bot after an appointment is booked.| No  
  
  


## Example

Imagine a scenario where you want to book a consultation appointment using the bot. You set the bot to act friendly and persuasive, guiding the contact towards scheduling their consultation. If the user does not respond within 24 hours (as per the timeout), the bot stops the conversation and marks the appointment as "not booked."

###   


## Additional Notes

  * Ensure that the bot’s personality is aligned with your business's tone and audience.
  * Setting a higher message limit allows for longer conversations, but it can also result in slower resolution.
  * If the contact does not respond in the allotted time, the appointment will be considered "not booked," and the workflow will proceed accordingly.

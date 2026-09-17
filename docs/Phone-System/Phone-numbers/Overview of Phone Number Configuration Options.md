# Overview of Phone Number Configuration Options

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001229976-overview-of-phone-number-configuration-options](https://help.gohighlevel.com/support/solutions/articles/48001229976-overview-of-phone-number-configuration-options)  
**Category:** Phone System  
**Folder:** Phone numbers

---

This article walks you through how to configure a specific phone number inside your HighLevel sub-account, including settings like call forwarding, timeout behavior, whisper messages, call recording, and more. Proper setup ensures optimal call routing, lead handling, and automation accuracy across your account.

  


  


* * *

**TABLE OF CONTENTS**

  * What is Phone Number Configuration?
  * Phone Number Configuration Options – At a Glance
  * How to Edit Your Phone Configuration
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Phone Number Configuration?**

  


Phone number configuration in HighLevel enables you to**control how each phone number behaves for****both inbound and outbound calls**.

  


These configurations are crucial for teams that rely on efficient phone communications, whether they show a custom caller ID, route calls to users, or enable voicemail.

* * *

## **Phone Number Configuration Options – At a Glance**

  


Option| Purpose| Common Use Case/Example  
---|---|---  
**Name Your Number**|  Label numbers for internal use| “Main Sales Line” or “Support Desk”  
**Forwarding Calls To**|  Route calls to external or mobile numbers| Send calls to team members' personal phones  
**Use Verified Number as Caller ID**|  Show verified number for outbound calls| Enhances professionalism in outbound calls  
**Call Connect**|  Adds prompt before call connects to ensure a human answers| Ideal for triggering missed-call automation  
**Whisper Message**|  Custom message before call connects| “Call from XYZ Agency - press 1 to connect”  
**Call Recording**|  Automatically records calls for compliance or training| Quality assurance and team monitoring  
**Play Call Recording Message**|  Announces recording to comply with legal standards| “This call may be recorded...”  
**Incoming Call Timeout**|  Determines how long phone rings before voicemail| Route to CRM voicemail or personal voicemail  
**Outgoing Call Timeout**|  Sets outbound ring time limit| Avoids hitting recipient voicemails  
**Ring Incoming Calls to Users**|  Ring multiple users simultaneously| Ensures calls are answered promptly  
  
* * *

## **How to Edit Your Phone Configuration**

  


####  _**Step 1:** Navigate to Phone Numbers_  


  


From you sub-account, navigate to **Settings >** **Phone System > Phone Numbers.**

  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078175121/original/2_7746jY1JbETbwa_AKn4M6xLxQDzuZ-ZQ.png?1786482930)**

  


  


#### _**Step 2:** Navigate to Edit Configuration Option_

  


Click on the **Three Dots** beside the number you want to configure then click the **Edit Configuration** option from the pop-up.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078265714/original/QYLwBsJHVBI2OpYubnD1DdRVraz-CMfTFA.png?1786550188)

  


  


#### _**Step 3:** Name Your Number_

  


This option lets you label your number for internal reference. 

  
 _Example:_ Main Sales Line, Support Line, or Agent John's Number.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261222/original/AjIPxtxxoxpVuihRi9zd2WlFUR0WQczFKg.png?1786547987)

  


  


#### _**Step 4:** Calls Go To_

  


This lets you define the number where incoming calls will be routed to. Useful for forwarding to mobile phones, external lines, or different departments.

  


When a caller dials Number A (the configured number), the call is immediately forwarded to Number B (the destination number).

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078262129/original/hNzHFsPcHsWKye8yCG06lKl8ij68XzmYpw.png?1786548521)

  


####   


#### _**Step 5:** Call Recording_

  


The Call Recording option enables automatic call recordings for training, quality assurance, or compliance purposes. 

  


The Play Call Recording Message setting lets you add a pre-recording whisper message, such as “This call will be recorded for quality purposes,” to inform the receiver before recording begins.

  

    
    
    **Important:** Call Recording costs **$0.0025/min**. Storing it costs **$0.0005/min/month**.  
    

  


  

    
    
    **Note:** In many U.S. states, playing a **recording disclaimer is legally required** to ensure compliance.  
    

  


_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261663/original/xwZ-KU27fVakXHruyFmplSVNIXh-s5uF1A.png?1786548244)_

  


  


#### _**Step 6:** Set Call Forwarding_

  


For more detailed call forwarding, click on the **Call Forwarding** tab. This includes the option to:  
  


  * **External Phone Number:** Route calls to an External Phone Number  
  


  * **Business Phone Number:** Route calls to the Business phone number setup in your Business profile  
  

  * **Voice AI:** Route calls to an AI Agent that can take calls 24x7, answer queries, transfer calls and more  
  

  * **Ring Multiple Team members:** Route incoming calls to multiple users (team members) within your sub-account. When a call comes in, the phones of all selected users will ring simultaneously until someone answers or the call times out. You can assign maximum 6 users to receive these calls.  
  
For more details, checkout our article: [Ring Incoming Calls to Multiple Users ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002850>)


**  
**

**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078261752/original/kBo7JmWCtgvGRm5qpviD2K3n5jdnG2F1uw.png?1786548326)**

  


  


####  _**Step 7:** Set Timeout and Backup_

  * **Incoming Call Timeout:** The amount of time (in seconds) the system lets the inbound call ring before being dropped or forwarded to a voicemail (personal voicemail or pre-recorded voicemail within the CRM).  
  
Make sure you’ve uploaded a voicemail recording (MP3 or WAV format) either in the Business Info tab or in the assigned user’s profile settings.  
  

    * _Scenario 1 - Route to Personal Voicemail:_ If you want missed calls to go to your cellphone's voicemail, simply leave the Inbound Call Timeout field blank or set it to 60 seconds. This gives the call enough time to reach your personal voicemail system.  
  

    * _Scenario 2 - Route to CRM Voicemail After Ringing:_ If you'd like the call to ring briefly before directing the lead to a pre-recorded voicemail within the CRM, set the Inbound Call Timeout to around 20 seconds. This avoids the call reaching your personal voicemail and ensures it gets handled by your CRM setup.  
  

    * _Scenario 3 - Direct to CRM Voicemail Immediately:_ To send calls directly to a pre-recorded CRM voicemail without ringing your phone, set the Inbound Call Timeout to 1–4 seconds.  
  

  * **Outgoing Call Timeout:** The amount of time (in seconds) the system lets the outbound call ring before dropping the call. Use a shorter timeout like 30 seconds to avoid hitting customer voicemails, ideal for voicemail-drop or lead-churn reduction campaigns  
**  
**
  * **Set the Backup:** Choose between Voicemail and Voice AI for you backup. This is what customers will here when you are unable to answer an incoming call. 


####   
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078263338/original/tfDNVEgdD7Rf27FWX41R0W9Xt2QKRRZ1OA.png?1786549051)**

  


 _  
_

#### **_Step 8:_**_Advanced Settings_

  


Navigate to the **Advanced** **Settings** tab. This area includes the options for:

  


  * **Call Connect:** When enabled, the recipient will hear a whisper message prompting them to press a key to accept the call, ensuring that only calls answered by a human are marked as connected.  
  
Ideal for enabling Missed-Call Text-Back automations and preventing voicemails from being falsely marked as successful calls.  
  

  * **Whisper Message:** This option allows you to set the message that plays before connecting the call when Call Connect is enabled. The Call Recording and Whisper messages uses Text-to-Speech (TTS). TTS is billed at $0.00084 per 100 characters.  
  
_Example:_ “Call from HighLevel - press a key to connect.” or "Call from XYZ Agency - press a key to connect."  
  

  * **Bring Your Own Number:** This feature allows you to show your verified phone number in the callerID of the recipient when you are making outbound phone calls. This option is only applicable to Verified Phone Numbers.  
**  
**To learn more, see:[How to Set Up Verified Caller ID (Use your number for Voice Calls)](<https://help.gohighlevel.com/en/support/solutions/articles/155000003232>)  
  
[](<https://help.gohighlevel.com/en/support/solutions/articles/155000003232>)[](<https://help.gohighlevel.com/en/support/solutions/articles/155000003232>)**[](<https://help.gohighlevel.com/en/support/solutions/articles/155000003232>)**
  * **Phone number I see when receiving the call:** By default, the system transmits the number of the caller for caller ID. However, if you prefer your caller ID to show the number that the caller dialed instead, you can activate this feature. This is most relevant if the caller dialed number A and was forwarded to number B (your number).  
  

  * **Prefer forwarding calls to:** When receiving an inbound call on a phone number, it can either be sent to the contact owner or the phone number owner.  
  

  * **Connect me to the contact (Outbound calls):** Choose Between the options  
  

    *  _Immediately after they answer_ : Connects you to the contact as soon as they answer. Helps you hear the real ringing/connecting/busy tone when calling the contact (instead of a simulated one). You hear the call recording message too (if enabled).  
_  
_
    * _After the call recording message finishes:_ Avoids conversation overlap with call recording message. But you hear a simulated ring tone when calling them.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078265404/original/TY1cV14WgGJoF3wWNPSeoHU7ikLw2XNmVg.png?1786550051)

* * *

## **Frequently Asked Questions**

**  
**

****Q: What happens if I leave inbound or outbound timeout fields blank?  
**** The system defaults to 60 seconds for both inbound and outbound timeouts.  
**  
**

****Q: What URL should I provide when verifying a toll-free number?  
**** Use your official business website URL, one that customers can find and verify.

Checkout this article for more information - [Toll-Free Verification Guide for LC - Phone (US/Canada) ](<https://help.gohighlevel.com/en/support/solutions/articles/48001222300>)  
**  
**

****Q: Can I assign the same number to multiple users?  
**** Yes, under "Ring Incoming Calls to Selected Users," you can assign up to 7 users to a single number.  
**  
**

****Q: How do I stop forwarded calls from going to my personal voicemail?  
**** Use a short inbound timeout (~20 secs) so calls hit a CRM voicemail before reaching your personal voicemail.  
**  
**

****Q: Why aren’t my outbound calls displaying the right caller ID?  
**** Ensure that your number is verified and approved for outbound calling and you’ve selected “Use Verified Number as Caller ID.”  
**  
**

****Q: Can I use toll-free numbers for both SMS and voice?  
**** Yes, but they must be registered and verified for SMS compliance and typically have limitations for outbound voice caller ID depending on carrier support.

**  
**

**Q:**Why isn’t my whisper message playing when calls are routed through my IVR workflow?****

Whisper messages will only play for calls forwarded to external phone numbers.  
If the call is answered through the HighLevel web app, mobile app, or desktop app, the whisper message will not play , this is expected behavior.

* * *

## **Related Articles**

  


  * [ Inbound Call Routing - Explained ](<https://help.gohighlevel.com/en/support/solutions/articles/48000981432>)  
  

  * [How To Setup Automatic Calls and Voicemail Drops](<https://help.gohighlevel.com/en/support/solutions/articles/48000981430>)  
  

  * [Outbound Calls / Softphone - How It Works ](<https://help.gohighlevel.com/en/support/solutions/articles/48000981431>)  
  

  * [Moving Numbers tool across sub-accounts ](<https://help.gohighlevel.com/en/support/solutions/articles/48001203968>)  
  

  * [How to Purchase a Phone Number in a Sub-Account](<https://help.gohighlevel.com/en/support/solutions/articles/155000003226>)  
  

  * [Porting your telephone number (non-Twilio number) to a location ](<https://help.gohighlevel.com/en/support/solutions/articles/48001211919>)[](<https://help.gohighlevel.com/en/support/solutions/articles/48001211919>)**[](<https://help.gohighlevel.com/en/support/solutions/articles/48001211919>)[](<https://help.gohighlevel.com/support/solutions/articles/155000002850>)[](<https://help.gohighlevel.com/support/solutions/articles/155000002850>)[](<https://help.gohighlevel.com/support/solutions/articles/155000002850>)  
**

# Outbound Calls with Dialer in Web App (Softphone)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981431-outbound-calls-with-dialer-in-web-app-softphone-](https://help.gohighlevel.com/support/solutions/articles/48000981431-outbound-calls-with-dialer-in-web-app-softphone-)  
**Category:** Phone System  
**Folder:** Calling

---

Browser-Based Calling

Outbound Calls with the HighLevel Web Dialer (Softphone)

Make outbound calls directly from your browser, choose the correct Calling From number, manage live calls, transfer callers, and troubleshoot common Web Dialer issues.

Overview

The HighLevel Web Dialer, sometimes called the Softphone, lets users place and manage calls directly from a supported browser. Users can manually enter a phone number, search for a contact, select a recent call, choose an available Calling From number, and use in-call controls without leaving HighLevel.

A reliable calling experience depends on the user’s number assignment, permissions, microphone and audio-device access, browser configuration, network connection, and outbound call timeout.

This guide explains how the Web Dialer differs from the Power Dialer and mobile calling, how to make and transfer calls, how Calling From behavior works, and how to resolve common audio, caller ID, and connection issues.

Important

Your browser must be allowed to use the microphone before the Web Dialer can transmit your voice. Headsets, speakers, VPNs, browser extensions, firewall rules, and security applications can also affect call audio or connection behavior.

When recording calls, review the consent and disclosure requirements that apply to the caller, recipient, and jurisdictions involved before changing or removing the recording announcement.

Table of Contents

What is the Web Dialer (Softphone)? Key Benefits of the Web Dialer Web Dialer vs. Power Dialer vs. Mobile Calling What You Need Before Making Outbound Calls Choosing the Calling From Number How to Make Outbound Calls with the Web Dialer Managing an Active Call How to Set Up the Web Dialer for Outbound Calls Understanding Connecting and Ringback Tones Caller ID, Call Recording, and Number Reputation Troubleshooting Outbound Calls Frequently Asked Questions Related Articles

# **What is the Web Dialer (Softphone)?**  
  


The Web Dialer is HighLevel’s browser-based calling interface. It allows users to make and manage outbound calls without using a separate deskphone or the HighLevel mobile app.

The dialer is available from the green phone icon in the top navigation on most pages. Once opened, users can enter a number manually, search for an existing contact, review recent calls, use the dialpad during a live call, access configured call scripts, transfer calls, and record follow-up information.

The Web Dialer can be used from a desktop browser or supported mobile browser. For a dedicated mobile experience, use the HighLevel mobile app.

## **Key Benefits of the Web Dialer**  
  


The Web Dialer keeps calling tools close to the contact record so users can spend less time switching applications and more time managing customer conversations.

  * **Browser-Based Calling:** Place calls without a separate physical phone or mobile application.
  * **Fast Contact Access:** Search contacts, enter numbers manually, or return calls from the Recents view.
  * **Flexible Caller ID:** Use the assigned number or select another permitted Calling From number when access allows.
  * **Live Call Controls:** Mute, hold, use the keypad, and transfer connected calls.
  * **Consistent Call Handling:** Access configured call scripts, notes, tags, and contact information during or after calls.
  * **Centralized Call Activity:** Keep outbound call history and related contact activity inside HighLevel.


## **Web Dialer vs. Power Dialer vs. Mobile Calling**  
  


These calling options can use the same underlying phone system but serve different workflows. Choosing the correct option helps users understand where calls are started and how contacts enter the calling queue.

Calling Option| How It Works| Best Used For  
---|---|---  
**Web Dialer / Softphone**|  A user opens the dialer in a browser and manually selects a contact or enters a phone number.| Individual calls, callbacks, and contact-specific outreach.  
**Manual Actions / Power Dialer**|  A workflow creates manual call tasks that appear under **Conversations → Manual Actions**. The user works through the assigned queue using the dialer.| Structured sales, support, or follow-up calling queues.  
**HighLevel Mobile App**|  A user places calls from the dedicated mobile application.| Calling while away from a desktop or browser workspace.  
  
## **What You Need Before Making Outbound Calls**  
  


A short pre-call review helps prevent missing audio, incorrect caller ID, and calls ending before the recipient has enough time to answer.

  * **Available outbound number:** Confirm the user has an assigned number or access to an eligible Calling From number.
  * **Correct user access:** Review the user’s role, data visibility, contact access, and phone-number assignments.
  * **Microphone permission:** Allow the browser to use the microphone.
  * **Audio devices:** Select the intended microphone, speaker, or headset and test them before calling.
  * **Stable network:** Use a reliable internet connection and avoid unnecessary VPN or security-routing interference.
  * **Outbound timeout:** Set the phone number’s Outgoing Call Timeout to at least 20 seconds.
  * **Recording compliance:** Confirm that call-recording and announcement settings meet applicable legal and business requirements.


## **Choosing the Calling From Number**  
  


The Calling From number determines which eligible HighLevel number is used as the outbound caller ID. User role, data visibility, number assignment, and account access determine whether the number is selected automatically or can be changed from the dialer.

User Configuration| Calling From Behavior  
---|---  
**User role with Only Assigned Data**|  Outbound calls automatically use the user’s assigned phone number when the applicable assignment is available.  
**User with All Records access**|  The user can open the **Calling From** dropdown and select from the phone numbers available to their account and permissions.  
  
### **Review User Role and Data Visibility**  
  


Data visibility affects whether a user is limited to assigned data or can access all records. Review this setting when a user cannot choose a different Calling From number or calls are using an assigned number automatically.

![HighLevel user Roles and Permissions showing User role and Only Assigned Data](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045947128/original/OPsybV0rDD4Ru3ln9VuYh1fn1O8j9RFLWg.png?1746053604=)

A user with the User role and Only Assigned Data is generally limited to the phone number assigned to that user.

### **Select a Number from the Calling From Dropdown**  
  


When the user has the appropriate access, open the Calling From dropdown and select the eligible number that should appear as the outbound caller ID.

![HighLevel Web Dialer showing the Calling From dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045947177/original/5ljIoO6AWgEYanhVAj8Dk62VdyeWA3SsWg.png?1746053805=)

Select the appropriate outbound number from Calling From before placing the call.

## **How to Make Outbound Calls with the Web Dialer**  
  


The dialer can start a call from a manually entered number, an existing contact, or a recently used number. Confirm the Calling From selection before dialing so the intended business number is used.

  1. From the top navigation, click the **green phone icon**.
  2. Review the **Calling From** number and change it when your access permits.
  3. Choose one of the following:
     * **Keypad:** Enter a phone number manually.
     * **Contacts:** Search for and select an existing contact.
     * **Recents:** Select a previously called or received number.
  4. Enter or select the destination phone number.
  5. Click the **call button** to begin dialing.
  6. After the call connects, use the dialpad when you need to send keypad input to an IVR or automated phone menu.


![HighLevel Web Dialer opened from the green phone icon](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045946208/original/dIIfwMvTRPPPEuL6Zl10oKECU0mPgfgDtg.png?1746050609=)

Open the Web Dialer from the green phone icon, select the Calling From number, and choose Keypad, Contacts, or Recents.

**Dialer workspace:** The Web Dialer can auto-minimize when you click elsewhere. Pin it when you want it to remain visible, or drag it to a different part of the screen while working in HighLevel.

## **Managing an Active Call**

  
Once a call connects, the dialer provides controls for audio privacy, call handling, automated-menu navigation, and transferring the conversation to another user or phone number.

Control| What It Does  
---|---  
**Mute**|  Turns off your microphone so the other party cannot hear you.  
**Hold**|  Places the call on hold so neither party can hear the other until the call is resumed.  
**Keypad**|  Sends DTMF keypad tones for IVRs, extensions, conference codes, and automated menus.  
**Call Scripts**|  Displays a configured call script during the conversation when scripts are available.  
**Transfer**|  Moves the active caller to another user or phone number using a warm or blind transfer.  
  
### **Warm Transfer**  
  


A warm transfer lets you speak with the transfer recipient before connecting the original caller. This is useful when the next person needs context before taking over the conversation.

  1. From the connected call, open the transfer controls.
  2. Search for another user or manually enter a phone number.
  3. Select **Call & Hold** to place the original caller on hold and call the transfer recipient.
  4. Speak with the recipient and provide the necessary context.
  5. Select the final patch or transfer option shown in your dialer to connect both parties and leave the call.


![HighLevel Web Dialer warm transfer screen showing Call and Hold](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045946585/original/9r03TLzUsFl7kYcgLvlhCpcmuTxkK2EyDA.png?1746051274=)

Call & Hold keeps the original caller on hold while you speak with the transfer recipient.

### **Blind Transfer**  
  


A blind transfer immediately sends the caller to another user or phone number without first speaking with the recipient. Your participation ends when the transfer is completed.

  1. Open the transfer controls during the connected call.
  2. Search for a user or enter the destination number.
  3. Click **Transfer & End** to send the caller to the destination and disconnect yourself.


![HighLevel Web Dialer blind transfer screen showing Transfer and End](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155010495830/original/kkJck-tqalFEHANzgUMyCBsUrUBUwUAoXA.png?1697670632=)

Transfer & End sends the caller to the selected destination without a consultation call.

## **How to Set Up the Web Dialer for Outbound Calls**  
  


Proper browser and phone-number configuration prevents the most common dialer problems. Complete the steps below before relying on the Web Dialer for live customer calls.

### **Step 1: Allow Microphone Access in the Browser**

The microphone must be allowed for the HighLevel site. In Chrome, click the site-information icon to the left of the address bar and confirm that **Microphone** is enabled.

![Chrome site information menu showing microphone permission enabled for HighLevel](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045947374/original/GHKokaA_r5Jo-VnwcM6lqShTa_14auVT9g.png?1746054454=)

Allow microphone access from the browser’s site-information menu.

If the permission is not available from the address bar, open the browser’s site-permission settings and change Microphone from **Block** or **Ask** to **Allow**.

![Chrome site settings showing the microphone permission option](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045947375/original/bY1_yjTWeOXmY7Li13V3_734_AUG90V5uw.jpeg?1746054454=)

Browser site settings can be used to reset or allow microphone access.

### **Step 2: Select and Test Audio Devices**

  


Open the Web Dialer’s audio-device settings and select the microphone and main speaker you want to use. When available, use the test controls and microphone-level indicator before placing a live call.

[ Learn more about Audio Device Settings in the Web Dialer → ](<https://help.gohighlevel.com/support/solutions/articles/155000008366-audio-device-settings-in-the-web-dialer>)

### **Step 3: Test Without VPNs or Browser Extensions**  
  


VPNs, privacy extensions, ad blockers, security tools, and traffic-routing applications can interfere with Web Dialer audio or connection requests. Temporarily test in an incognito or guest browser session where extensions are disabled.

![Chrome browser showing VPN and security extensions that can interfere with the HighLevel Web Dialer](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045947381/original/inaZmrkekmNgr6ZCyjHL6j4u6WHJe01wHw.png?1746054592=)

Temporarily disable VPN or security extensions for testing, or use an incognito or guest session.

### **Step 4: Set the Outgoing Call Timeout**  
  


Set the phone number’s **Outgoing Call Timeout** to at least 20 seconds. A timeout that is too short can end the call before the recipient’s carrier and device have enough time to ring.

  1. Go to **Settings → Phone System → Phone Numbers**.
  2. Open **Edit Configuration** for the applicable number.
  3. Enable **Outgoing Call Timeout**.
  4. Enter a value of at least **20 seconds** and save the configuration.


![HighLevel phone number configuration showing incoming and outgoing call timeout settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045947501/original/YAtV96DxqG5nYp8mx3fvRcSrRiaNm6GflQ.png?1746054859=)

The screenshot shows where the call-timeout fields are configured. Choose a value appropriate for your calling workflow and keep the outgoing timeout at 20 seconds or more.

### **Step 5: Place a Controlled Test Call**  
  


Call a phone you can monitor. Confirm that the recipient’s device rings, the expected caller ID is used, both parties can hear each other, the keypad works, and the call can be placed on hold or transferred when needed.

## **Understanding Connecting and Ringback Tones**  
  


The sound heard immediately after starting a call reflects different stages of carrier connection. Understanding the difference can help distinguish normal setup time from a call that never reached the destination network.

  1. **Connecting tone:** HighLevel plays a brief connecting tone while attempting to reach the recipient’s carrier.
  2. **Ringback tone:** Ringback starts after the destination carrier confirms that the recipient’s device is ringing.
  3. **Localized ringback:** For supported countries, the tone can match the country associated with the phone number involved in the call.
  4. **Carrier not reached:** If the destination carrier cannot be reached, the call can end after the connecting tone instead of playing a ringback tone for a device that is not actually ringing.


## **Caller ID, Call Recording, and Number Reputation**  
  


The Calling From number identifies the outbound line, while CNAM, SHAKEN/STIR, and Voice Integrity help carriers and recipients interpret the identity and reputation of that number. These features serve different purposes and should not be treated as interchangeable.

Feature| Purpose| Important Limitation  
---|---|---  
**Calling From**|  Selects the HighLevel phone number used for the outbound call.| Available choices depend on number assignment, user permissions, and account configuration.  
**CNAM**|  Associates a business or personal name with a US phone number.| Display is not guaranteed and CNAM does not remove spam labels.  
**SHAKEN/STIR**|  Authenticates caller ID information and helps carriers evaluate whether a call is legitimate.| Authentication does not guarantee that a nuisance or spam label will be removed.  
**Voice Integrity**|  Registers eligible US numbers with major caller-ID analytics providers to improve number reputation and address spam labeling.| Provider reviews occur separately, and label changes can take time to appear across networks.  
  
### **Call Recording Announcement**  
  


The message “This call will be recorded for quality purposes” is controlled by the applicable phone number’s recording settings. To review it, go to **Settings → Phone System → Phone Numbers → Edit Configuration**.

The announcement can be edited or disabled when the interface allows, but removing it is not recommended unless you have confirmed that your recording process satisfies all applicable consent and disclosure requirements.

[ Learn more about Phone Number Configuration Options → ](<https://help.gohighlevel.com/support/solutions/articles/48001229976-overview-of-phone-number-configuration-options>)

### **Voice Integrity Prompt After an Unanswered Call**  
  


After an outbound Web Dialer call is not answered, HighLevel may show a Voice Integrity recommendation. The prompt provides a shortcut to registration tools intended to improve the reputation and answer rates of eligible US phone numbers.

## **Troubleshooting Outbound Calls**  
  


Start troubleshooting with the user’s number access, browser permissions, audio devices, network path, and timeout configuration. Testing one layer at a time helps isolate whether the issue is caused by account configuration, the browser, or the destination carrier.

The Dialer Does Not Open or the Call Button Is Unavailable

Refresh the page, confirm the user has access to the sub-account, and verify that an eligible phone number is assigned or available for outbound calling. Also review the user’s role and data visibility.

The Other Person Cannot Hear Me

Confirm the browser is allowed to use the microphone, the correct microphone is selected in Audio Device Settings, the microphone is not muted, and another application is not exclusively controlling the device.

I Cannot Hear the Other Person

Confirm the correct main speaker or headset is selected, verify the device volume, and test another output device. Reconnect Bluetooth devices when the browser is using an older or disconnected audio route.

The Call Ends Before the Recipient Rings

Confirm the destination number is valid, set the Outgoing Call Timeout to at least 20 seconds, and test without a VPN, privacy extension, or security application. If the call stops after the connecting tone, the destination carrier may not have been reached.

The Wrong Calling From Number Is Used

Review the user’s assigned number, role, Data Visibility Scope, and Calling From dropdown. Users limited to Only Assigned Data can be routed through their assigned number automatically.

Call Audio Is Delayed, Choppy, or Unstable

Use a stable network, reduce competing bandwidth usage, test without a VPN, and use a reliable headset or wired connection when possible. Compare the result in another supported browser or device.

The Recipient Sees “Spam Likely” or Does Not See the Business Name

Review SHAKEN/STIR, CNAM, and Voice Integrity in the Trust Center. CNAM can associate a business name with the number but does not guarantee display or remove nuisance labels. Voice Integrity is the appropriate reputation-registration path for eligible US numbers.

A Call Transfer Does Not Complete

Confirm the destination user or phone number is valid. For a warm transfer, wait for the consultation call to connect before patching the parties together. For a blind transfer, use Transfer & End only after confirming the intended destination.

## **Frequently Asked Questions**  
  


Q: Can I use the Web Dialer from a mobile browser?

Yes. The browser dialer can work from supported desktop and mobile browsers. For a dedicated mobile calling experience, use the HighLevel mobile app.

Q: Why can’t I select another Calling From number?

The available Calling From options depend on the user’s role, Data Visibility Scope, number assignment, and account permissions. A User limited to Only Assigned Data generally calls from the assigned number automatically.

Q: Is the Web Dialer the same as the Power Dialer?

No. The Web Dialer is the browser calling interface. The Power Dialer experience uses workflow-created Manual Call tasks under Conversations → Manual Actions and opens the dialer as users work through the queue.

Q: Why do I hear a connecting tone before the normal ringing sound?

The connecting tone plays while HighLevel reaches the recipient’s carrier. Ringback begins after the carrier confirms that the destination device is ringing.

Q: Why do I see a Voice Integrity prompt after an unanswered call?

HighLevel can recommend Voice Integrity after an unanswered Web Dialer call. The prompt is a shortcut to reputation tools that can help eligible US numbers address spam labeling and improve future answer rates.

Q: Can I remove or change the call-recording announcement?

The recording announcement can be reviewed from the phone number’s Edit Configuration screen. Do not disable or change it until you have confirmed that your recording process meets all applicable consent and disclosure requirements.

Q: Can I use the dialpad to navigate an automated phone menu?

Yes. Open the keypad during a connected call to send DTMF tones for menu selections, extension numbers, or conference codes.

Q: Does minimizing the Web Dialer end the call?

No. Minimizing or auto-minimizing changes only how the dialer appears on the screen. The call remains active until it is ended or disconnected.

### **Related Articles**  
  


[ The Phone Dialer Overview ](<https://help.gohighlevel.com/support/solutions/articles/155000005807-the-phone-dialer-overview>) [ Audio Device Settings in the Web Dialer ](<https://help.gohighlevel.com/support/solutions/articles/155000008366-audio-device-settings-in-the-web-dialer>) [ How to Create and Use Call Scripts in Web & App Dialers ](<https://help.gohighlevel.com/support/solutions/articles/155000004935-how-to-create-and-use-call-scripts-in-web-app-dialers>) [ How to Add a Manual Call Action to a Workflow ](<https://help.gohighlevel.com/support/solutions/articles/48000979920-manual-call-how-to-add-a-manual-call-action-power-dialer->) [ Improve Your Phone Number’s Reputation with Voice Integrity ](<https://help.gohighlevel.com/support/solutions/articles/155000005566-improve-your-phone-number-s-reputation-with-voice-integrity>) [ What is CNAM? ](<https://help.gohighlevel.com/support/solutions/articles/155000006430-what-is-cnam->)

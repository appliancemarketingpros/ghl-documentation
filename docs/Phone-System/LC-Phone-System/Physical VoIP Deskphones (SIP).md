# Physical VoIP Deskphones (SIP)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005487-physical-voip-deskphones-sip-](https://help.gohighlevel.com/support/solutions/articles/155000005487-physical-voip-deskphones-sip-)  
**Category:** Phone System  
**Folder:** LC Phone System

---

SIP Deskphone Calling

Physical VoIP Deskphones (SIP)

Connect a compatible physical SIP deskphone to HighLevel, configure inbound and outbound calling, assign users, test registration, manage devices, transfer calls, and troubleshoot one-way calling or audio issues.

Overview

HighLevel can connect compatible physical VoIP deskphones using SIP so users can make and receive business calls from a traditional handset while keeping call activity connected to the CRM.

A successful setup requires more than entering SIP credentials. The deskphone must register correctly, the assigned HighLevel user must be configured to receive calls on the deskphone, inbound routing must point to that user when appropriate, and the network must permit the required SIP and RTP traffic.

This guide covers provisioning, supported network requirements, user routing, testing, extension dialing, blind transfers, device management, and dedicated troubleshooting for both inbound-only and outbound-only calling failures.

Having a One-Way Calling Issue?

If **inbound calls work but outbound calls fail** , jump to Inbound Works but Outbound Fails. If **outbound calls work but inbound calls do not ring the deskphone** , jump to Outbound Works but Inbound Fails.

Table of Contents

What is the Physical VoIP Deskphone (SIP) Integration? Key Benefits of Physical VoIP Deskphones Permissions for VoIP Deskphones Technical Requirements & Recommended Deskphones SIP Settings and Network Requirements How to Set Up a Physical VoIP Deskphone Manage SIP Devices Deskphone-to-Deskphone Calling & Transfers Troubleshooting One-Way Calling Additional Troubleshooting Frequently Asked Questions Related Articles

# **What is the Physical VoIP Deskphone (SIP) Integration?**  
  


The Physical VoIP Deskphone integration lets a compatible open-SIP handset register with HighLevel so users can make and receive calls from physical phone hardware while maintaining HighLevel call routing and CRM activity.

Each deskphone is provisioned with a SIP domain, SIP username or extension, password, and assigned HighLevel user. Once the phone registers successfully, HighLevel can route supported calls to the deskphone based on the user and phone-number configuration.

HighLevel features such as call recording and transcription can remain part of the call workflow when those features are enabled. Call transcription requires call recording and is a separately billed Voice Intelligence feature.

## **Key Benefits of Physical VoIP Deskphones**  
  


Physical SIP deskphones give teams a traditional handset experience without separating their voice activity from HighLevel. This is especially useful for office-based teams that prefer dedicated phone hardware while still relying on CRM-based routing and reporting.

  * **Physical Handset Calling:** Make and receive supported HighLevel calls from a compatible SIP deskphone.
  * **CRM-Connected Calling:** Keep call activity connected to the HighLevel phone system and contact records.
  * **User-Based Routing:** Assign each SIP device to a HighLevel user and control which channel receives inbound, Ring All, and IVR-routed calls.
  * **Extension Dialing:** Call another configured deskphone directly using its extension.
  * **Deskphone Transfers:** Blind-transfer supported calls to another configured deskphone extension.
  * **Built-In Testing:** Use HighLevel's Test Calls area to verify both outbound calling and inbound ringing before putting the device into production.


## **Permissions for VoIP Deskphones**  
  


Deskphone provisioning changes phone-system credentials and user routing, so setup access is limited according to the user's administrative role.  
  


Role| Access  
---|---  
**Agency Admin**|  Can provision supported deskphones across agency locations.  
**Sub-Account Admin**|  Can provision devices inside the sub-account they administer.  
**Other Users**|  Read-only access; users may be prompted to ask an administrator to configure the device.  
  
## **Technical Requirements & Recommended Deskphones**  
  


Choosing open-SIP hardware and preparing the network correctly reduces registration, audio, and one-way calling problems. Confirm these requirements before provisioning production devices.

### **Network and Protocol Requirements**  
  


Requirement| HighLevel Guidance  
---|---  
**SIP Transport**|  SIP over UDP, TCP, or TLS.  
**SIP Signaling**|  Allow outbound ports **5060/5061**.  
**RTP Audio**|  Allow UDP **10000–20000**.  
**SIP ALG**|  Disable SIP ALG when it interferes with registration, audio, answering, or inbound calling.  
**Power**|  Use a PoE-capable network connection or the appropriate external power adapter for the phone.  
  
**Do not confuse the documented outbound SIP requirement with public port forwarding.** HighLevel's published deskphone requirements specify outbound SIP ports 5060/5061 and UDP 10000–20000 for RTP. Do not expose SIP ports to the public internet or add arbitrary inbound port-forwarding rules solely because a call is failing. First verify registration, HighLevel routing, Keep Alive, SIP ALG, and the device configuration.

###   
**What to Look for When Choosing a Deskphone**  
  


  * Standard open-SIP support.
  * PoE support when the office network uses Power over Ethernet.
  * At least two programmable line keys when your workflow benefits from them.
  * Avoid carrier-locked or proprietary-provisioning hardware that prevents manual SIP account configuration.


###   
**Commonly Used Models**  
  


  * Yealink T54W / T58W
  * Poly VVX 450
  * Grandstream GXP 2170
  * Snom D785
  * Cisco 7841


**Compatibility note:** Model menus, labels, firmware behavior, and SIP-account fields vary by manufacturer. Most open-SIP devices can work when standard SIP registration is supported, but the list above should not be interpreted as an exhaustive certification list.

## **SIP Settings and Network Requirements**  
  


The terminology used by physical phones varies, but every device needs the HighLevel-generated SIP server information and credentials. Matching these values exactly is essential for registration and outbound calling.

Deskphone Setting| What to Enter or Verify  
---|---  
**Registrar / SIP Server / Server**|  Use the SIP Domain / SIP Endpoint generated in HighLevel.  
**Username / Extension / User ID**|  Use the exact SIP user or extension created in HighLevel. Credentials are case-sensitive where applicable.  
**Password**|  Use the SIP-user password created in HighLevel. Store it securely because HighLevel cannot display the saved password later.  
**Transport**|  HighLevel supports SIP over UDP, TCP, or TLS. The phone and network must permit the transport being used.  
**Keep Alive**|  When available on the handset, enable Keep Alive and set the type to **Options** , especially when outbound calls work but inbound calls do not.  
  
**Vendor menus vary.** Some deskphones use labels such as Registrar, Server, Proxy, SIP URI, User ID, or Authentication ID. Use the HighLevel-generated values for the device's SIP account and refer to the handset manufacturer's documentation when the device separates these fields.

## **How to Set Up a Physical VoIP Deskphone (SIP)**  
  


Complete the setup in order so the SIP credentials, user assignment, inbound routing, and physical handset all point to the same configuration. Test the device before relying on it for production calls.  
  


### **Step 1: Open the VoIP Deskphone Setup**

  1. Open the applicable HighLevel sub-account.
  2. Go to **Settings → Phone Numbers**.
  3. Open **Advanced Settings**.
  4. Select **VoIP deskphone (SIP)**.
  5. Click **Get Started**.


![HighLevel Phone System Advanced Settings showing VoIP deskphone SIP and Get Started](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155050093926/original/YS4668PA9CkKqvVzZi-iCSDpL4zwgmAVHw.png?1752866528)

Open Settings → Phone Numbers → Advanced Settings → VoIP deskphone (SIP), then select Get Started.

### **Step 2: Configure the SIP Domain**  
  


Under **Setup SIP** , review the suggested SIP Domain / SIP Endpoint and choose the organization-specific prefix before saving.

**Important:** The SIP domain can be set only once. Review it carefully before saving the server configuration.

![HighLevel Setup SIP screen showing SIP Server Configuration and SIP Domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048947940/original/T_RoByQReSUzOcLWvCk_S-OlnygySLa2mg.png?1750964313)

The SIP Server Configuration creates the SIP Domain / SIP Endpoint used when registering physical deskphones.

### **Step 3: Create the SIP User**  
  


Create the credentials the physical phone will use to register with HighLevel.

  * **Extension/User Name:** Create the SIP username or extension for the device.
  * **Recommended extension format:** Use 3–5 digits when creating a numeric extension.
  * **Extension guidance:** Avoid starting with 0, 1, or 9, and consider matching the final digits of the assigned user's direct-dial number.
  * **Password:** Create a strong SIP password and save it securely.


**Save the SIP password now.** HighLevel does not display the saved password later. If the password is lost, reset it from Manage Devices and update the physical handset with the new password.

![HighLevel Create New SIP User fields for extension username and password](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048947928/original/MgsSV8OV1wJbZoUkMb7urN7BZExwWyiLVQ.png?1750964269)

Create the SIP extension or username and a secure password that will be entered into the physical phone.

### **Step 4: Assign the SIP Device to a HighLevel User**  
  


Use **Assign to User** to connect the SIP device with the HighLevel team member who will use the deskphone.

![HighLevel SIP setup showing Assign to User dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048947966/original/L3fI9Oggy2nZ9JE1bPLRwQdMYOycNEvsUw.png?1750964402)

Assign the SIP device to the HighLevel user who should place and receive calls on the handset.

### **Step 5: Configure the User's Inbound Deskphone Routing**  
  


Creating the SIP user registers the device, but inbound calls still depend on the assigned user's call-routing settings.

  1. Go to **Settings → My Staff**.
  2. Edit the assigned user.
  3. Open **Call & Voicemail Settings**.
  4. Under **Forward Calls to** , enable **Deskphone (SIP)** when direct calls should ring the deskphone.
  5. For shared Ring All routing, select **Deskphone (SIP)** as the user's Default Channel for Ring All when appropriate.
  6. For IVR-routed calls, select **Deskphone (SIP)** as the user's Default Channel for IVR when the deskphone should receive the routed call.


![HighLevel user Call and Voicemail Settings showing Deskphone SIP forwarding and default channels](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155050752109/original/s6wUPXQfAjDIUvnnGnpzS6V7a2bKE_GdjA.png?1753979052)

Enable Deskphone (SIP) for the inbound routes the user should receive, including direct forwarding, Ring All, or IVR.

### **Step 6: Configure the Physical Phone**  
  


Open the SIP account configuration on the physical handset and enter the SIP Domain, Username/Extension, and Password generated in HighLevel. Depending on the manufacturer, the server field may be labeled Registrar, SIP Server, Server, Proxy, or something similar.

After saving the phone's SIP account, confirm that the handset reports the account as **Registered** or shows an equivalent successful-registration indicator before testing calls.

### **Step 7: Run the Built-In Test Calls**  
  


Use the built-in tests to separate SIP registration or network problems from phone-number routing problems.

  1. Go to **VoIP deskphone (SIP) → Test Calls**.
  2. Select the SIP user you want to test.
  3. **Outbound test:** Use the physical deskphone to dial the displayed test number. A successful test plays the confirmation message.
  4. **Inbound test:** Use the inbound test / Test Ring control and confirm that the physical deskphone rings.


![HighLevel VoIP deskphone Test Calls screen for outbound and inbound SIP testing](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155050094240/original/q3Ukfp7AIe5rXyIjZpLnTQqSp7uBWzIUUw.png?1752867440)

The Test Calls screen helps verify the SIP user's outbound calling and whether the deskphone can receive a test ring.

## **Manage SIP Devices**  
  


Manage Devices lets administrators update a SIP user's password or assignment and remove devices that are no longer authorized to register with the sub-account.

### **Reset a SIP User Password**  
  


Go to **Settings → Phone Numbers → Advanced Settings → VoIP deskphone (SIP) → Manage Devices** and click the **pencil icon** for the applicable SIP user. Enter a new password, save the change, and then update the physical handset with the same password.

**Password changes affect registration.** The physical phone must be updated with the new SIP password after a reset or it will fail authentication.

![HighLevel Edit SIP User modal for resetting the SIP password or assigned user](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155050094265/original/uKVc1XmL5W74kkBCOiueVF7_8Up0fC8H8A.png?1752867520)

Use Edit SIP User to set a new password or review the HighLevel user assigned to the SIP device.

### **Delete a SIP Device**  
  


From **Manage Devices** , click the **trash can icon** next to the SIP user you want to remove.

**Warning:** Deleting the SIP device immediately removes its registration credentials. The handset will no longer be able to register using that SIP user.

![HighLevel Manage SIP Devices screen showing edit and delete actions](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155050094286/original/HLX6OxRIGnOvDhywfsLHaB5kEnAXQWo7Qw.png?1752867571)

Manage Devices provides edit and delete controls for provisioned SIP users.

## **Deskphone-to-Deskphone Calling & Transfers**  
  


Configured SIP deskphones can communicate internally by extension and can use supported blind-transfer behavior to move calls between deskphones without dialing an external business number.

### **Direct Extension Dialing**

To call another configured deskphone, dial that deskphone's SIP extension. For example, if the teammate's extension is **201** , dial 201 from your physical deskphone.

  * No external destination number is required for the internal extension call.
  * Both deskphones must be configured and registered.
  * Direct extension dialing is a deskphone feature.


### **Blind Transfer Between Deskphones**  
  


During a supported call, initiate the deskphone's transfer function, enter the destination user's extension, and complete the transfer according to the handset interface.

  1. Start the transfer from the active call.
  2. Dial the teammate's SIP extension.
  3. Complete the transfer on the handset.


![SIP deskphone software showing an extension entered for a deskphone transfer](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155065084807/original/hAOdaYjFSw10_XmuBQrArbP9dGoGJGH0Eg.png?1771329355)

Enter the destination deskphone extension when initiating the transfer.

![SIP phone interface showing the Transfer control during an active call](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155065084806/original/XqWn-AXejIHACYzbx0ChB_iERS33xnIURw.png?1771329355)

Complete the transfer using the physical phone or SIP client's Transfer control.

**Transfer limitation:** Physical SIP deskphones currently support blind transfers between extensions. Warm transfers from the deskphone are not currently supported.

## **Troubleshooting One-Way Calling**  
  


When only one call direction works, the successful direction provides an important diagnostic clue. Use the workflow that matches your issue instead of changing multiple SIP or firewall settings at once.

### **Inbound Calls Work but Outbound Calls Fail**  
  


If the deskphone receives calls but cannot place them, start with the SIP account, outbound network access, and HighLevel's built-in outbound test.

  1. **Confirm the SIP account is registered.**  
The phone should show Registered or an equivalent status. If it is not registered, verify the SIP Domain, Username/Extension, and Password before troubleshooting call routing.
  2. **Verify the server and credentials exactly.**  
Use the HighLevel-generated SIP Domain as the device's Registrar / SIP Server and the exact SIP username and password created under Setup SIP.
  3. **Check the documented outbound SIP ports.**  
The network must allow outbound SIP signaling on **5060/5061**.
  4. **Check the RTP audio range.**  
Allow UDP **10000–20000** for RTP audio. If the call establishes but has missing or one-way audio, this range and SIP ALG should be reviewed.
  5. **Review SIP ALG.**  
Disable SIP ALG on the router or firewall when it is modifying SIP traffic or causing registration, answering, or audio problems.
  6. **Run the built-in outbound test.**  
Go to **VoIP deskphone (SIP) → Test Calls** , select the SIP user, and use the physical phone to dial the displayed outbound test number.
  7. **If you receive 401 or 403 errors, recheck authentication.**  
These responses commonly indicate that the SIP username or password does not match the credentials configured in HighLevel.
  8. **If the built-in outbound test still fails, collect the diagnostic details listed below and contact Support.**


### **Outbound Calls Work but Inbound Calls Do Not Ring**  
  


Successful outbound calling usually confirms that the phone can register and reach the SIP service. For inbound failures, test the device first, then verify user routing, call-flow priority, Keep Alive, and network behavior.

  1. **Run the HighLevel inbound test.**  
Open **VoIP deskphone (SIP) → Test Calls** , select the SIP user, and use the inbound Test Ring option.
  2. **If the test ring fails, confirm SIP registration.**  
Check that the handset is still registered and that the SIP Domain, Username, and Password are correct.
  3. **Confirm the SIP user is assigned to the correct HighLevel user.**  
Go to **VoIP deskphone (SIP) → Setup SIP** or Manage Devices and verify the assigned user.
  4. **Verify the user's Call & Voicemail Settings.**  
Go to **Settings → My Staff → Edit User → Call & Voicemail Settings**. Enable **Deskphone (SIP)** under Forward Calls to when the deskphone should receive direct calls.
  5. **Check Ring All and IVR channels.**  
If the call reaches the user through Ring All, choose Deskphone (SIP) as the Default Channel for Ring All. If an IVR routes the call to the user, choose Deskphone (SIP) as the Default Channel for IVR.
  6. **Review the called phone number's inbound routing.**  
Confirm that the intended user is part of the number's call flow and that another configured route such as IVR or Voice AI is not handling the call before the team-member ring stage.
  7. **Enable SIP Keep Alive.**  
If the handset exposes a Keep Alive setting, enable it and set **Keep Alive Type = Options**. On some devices this appears under **Account → Advanced** ; the exact menu varies by manufacturer and firmware.
  8. **Disable SIP ALG if the issue continues.**  
SIP ALG can interfere with SIP registration and inbound call signaling even when some outbound behavior still works.
  9. **Retest both the built-in Test Ring and a real inbound call.**  
If the built-in inbound test rings successfully but the public phone number still does not reach the deskphone, focus the next troubleshooting step on HighLevel inbound routing rather than changing the handset credentials.


What to Collect Before Contacting Support  
  


  * SIP Domain / SIP Endpoint
  * SIP extension or username — **do not send the password**
  * Assigned HighLevel user
  * Deskphone manufacturer, model, and firmware version
  * Registration status shown by the handset
  * Result of the built-in outbound test
  * Result of the built-in inbound Test Ring
  * Date, time, and time zone of a failed call
  * Calling number and called HighLevel number
  * Any displayed SIP or test-call error code
  * Screenshots of the relevant HighLevel routing settings
  * Whether SIP ALG is enabled or disabled on the network


## **Additional Troubleshooting**  
  


Start with the symptom instead of changing every SIP field at once. The table below maps common deskphone problems to the first configuration or network area to review.

Symptom| Likely Area| What to Check  
---|---|---  
**401 / 403 Unauthorized**|  Authentication| Re-enter the exact SIP username and password. Check for case or copy/paste errors.  
**Phone does not register**|  SIP server, credentials, or network| Verify the SIP Domain, credentials, transport, outbound 5060/5061 access, and SIP ALG.  
**Inbound works; outbound fails**|  Outbound SIP signaling or authentication| Run the outbound test, verify 5060/5061 outbound access, credentials, transport, and SIP ALG.  
**Outbound works; inbound does not ring**|  User routing, Keep Alive, or SIP ALG| Run Test Ring, verify the assigned user, Deskphone routing, Ring All/IVR channel, Keep Alive = Options, and SIP ALG.  
**No audio or one-way audio**|  RTP / firewall| Verify UDP 10000–20000 and disable SIP ALG if it interferes with media.  
**Phone rings but the call cannot be answered correctly**|  NAT / SIP ALG / media| Disable SIP ALG and verify the network permits the documented SIP and RTP traffic.  
**Built-in Test Ring works but real inbound calls do not**|  HighLevel inbound routing| Review phone-number routing, assigned users, IVR/Voice AI, Ring All, and the user's Deskphone channel.  
**Cannot save SIP domain**|  Domain configuration| Use the suggested available domain or another valid available name before completing the one-time setup.  
**Phone stopped registering after password reset**|  Stored handset password| Update the physical handset with the newly saved SIP password.  
  
## **Frequently Asked Questions**

Q: What ports are required when outbound calls are failing?

HighLevel's documented deskphone requirements specify outbound SIP signaling on ports **5060/5061** and UDP **10000–20000** for RTP audio. Also review the SIP Domain, username/password, registration status, and SIP ALG before changing additional network rules.

Q: Inbound calls work, but I cannot make outbound calls. What should I check first?

Confirm the phone is registered, verify the HighLevel SIP Domain and credentials, confirm outbound 5060/5061 access, verify UDP 10000–20000 for media, disable SIP ALG if it interferes, and run HighLevel's built-in outbound SIP test.

Q: Outbound calls work, but inbound calls do not ring the deskphone. What should I check?

Run the built-in inbound Test Ring, confirm the SIP user is assigned correctly, enable Deskphone (SIP) in the user's Call & Voicemail Settings, review Ring All or IVR channel selection, verify the phone-number call flow, and enable Keep Alive with the type set to Options when the handset supports it.

Q: Which VoIP deskphones are compatible?

Most compatible open-SIP phones can work when they support standard SIP registration. Current HighLevel guidance lists examples including Yealink T54W/T58W, Poly VVX 450, Grandstream GXP 2170, Snom D785, and Cisco 7841.

Q: Does HighLevel support SIP trunking to an existing PBX?

No. The physical deskphone feature provisions individual SIP endpoints and does not currently provide SIP trunking for connecting an existing PBX such as Asterisk.

Q: Are deskphone calls automatically recorded and transcribed?

Recording and transcription depend on your HighLevel voice configuration. Transcription requires call recording to be enabled and is a paid Voice Intelligence feature. Review applicable recording-consent requirements before enabling recording.

Q: Is using a physical deskphone free?

Calls placed or received through the Phone System are billed according to the applicable voice rates. Optional services such as call recording, recording storage, and transcription can have additional usage charges. Review the current Phone System Pricing & Billing Guide for current rates.

Q: Can I perform a warm transfer from the physical deskphone?

Not currently. Physical SIP deskphones support blind transfers to another configured deskphone extension. Warm transfers are available through supported web-dialer workflows instead.

Q: Can the deskphone's native voicemail button open HighLevel voicemail?

No. A handset's native voicemail feature is separate from HighLevel voicemail. HighLevel voicemail and associated call activity are reviewed through the applicable HighLevel Conversations, voicemail, and reporting areas.

### **Related Articles**

[ Inbound Calls: IVR, AI, Routing & Call Flow Explained ](<https://help.gohighlevel.com/support/solutions/articles/155000007498-inbound-call-handling-ivr-ai-routing-call-flow-explained>) [ Phone Number Edit Configuration: Incoming Call Settings ](<https://help.gohighlevel.com/support/solutions/articles/155000006881-phone-number-edit-configuration-incoming-calls-settings->) [ How to Assign LC Phone Numbers to Users ](<https://help.gohighlevel.com/support/solutions/articles/48001152124-how-to-assign-twilio-phone-numbers-to-users>) [ How to Fix Bad VoIP Call Quality ](<https://help.gohighlevel.com/support/solutions/articles/48000981694-how-to-fix-bad-call-quality>) [ How to Enable Call Transcriptions for Recorded Calls ](<https://help.gohighlevel.com/support/solutions/articles/155000002841>) [ Voicemail for Company and Users ](<https://help.gohighlevel.com/support/solutions/articles/48001146671-voicemail-for-company-and-for-users>)

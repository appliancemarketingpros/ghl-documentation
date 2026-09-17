# Setting up webhooks to receive incoming calls, messages and status updates for calls (for Twilio users)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002824-setting-up-webhooks-to-receive-incoming-calls-messages-and-status-updates-for-calls-for-twilio-user](https://help.gohighlevel.com/support/solutions/articles/155000002824-setting-up-webhooks-to-receive-incoming-calls-messages-and-status-updates-for-calls-for-twilio-user)  
**Category:** Phone System  
**Folder:** General

---

Twilio Webhook Configuration

Setting Up Webhooks for Incoming Calls, Messages & Call Status Updates

Configure Twilio to send inbound calls, incoming SMS/MMS messages, and call status updates to the correct HighLevel endpoints.

Overview

Locations connected to their own Twilio account need the correct webhooks so Twilio can pass inbound calls, incoming messages, and call status updates to HighLevel.

Voice webhooks are configured on the individual Twilio phone number. Messaging can be configured directly on the number or through a linked Twilio Messaging Service, depending on the number's current configuration.

This guide provides the exact webhook endpoints, explains which messaging path to use, and includes troubleshooting steps for calls, messages, or status updates that do not appear correctly in HighLevel.

Important

These instructions apply to locations using **their own Twilio account**. They do not apply to phone numbers managed through HighLevel's native LC Phone system.

If another application intentionally controls the phone number's existing webhooks, replacing those values can change how inbound traffic is routed. Confirm that the number should route calls and messages into HighLevel before replacing a custom webhook.

Table of Contents

What is Twilio Webhook Configuration? Key Benefits of Correct Webhook Configuration Before You Begin Webhook Endpoints at a Glance Direct Number vs. Messaging Service How to Set Up Twilio Webhooks for HighLevel Troubleshooting Twilio Webhooks Frequently Asked Questions Related Articles

# **What is Twilio Webhook Configuration?**

Twilio webhooks tell Twilio where to send events when someone calls or messages one of your Twilio phone numbers. Correct webhook configuration allows HighLevel to receive those events and display or process them inside the connected sub-account.

Voice configuration controls **incoming calls** and **call status updates**. Messaging configuration controls **incoming SMS/MMS messages**.

These settings are especially important after connecting an existing Twilio account, moving a number, changing a Messaging Service, or troubleshooting calls or texts that no longer appear correctly in HighLevel.

## **Key Benefits of Correct Webhook Configuration**

Webhooks create the connection between Twilio and HighLevel for inbound communication. Correct configuration helps prevent missing calls, missing messages, and incomplete call-status information.

  * **Inbound Call Routing:** Send incoming Twilio calls to HighLevel's voice endpoint.
  * **Incoming Message Delivery:** Route inbound SMS/MMS activity into HighLevel.
  * **Call Status Synchronization:** Send call-status events back to HighLevel using the dedicated call-status webhook.
  * **Messaging Service Support:** Configure inbound messaging correctly when multiple numbers use a Twilio Messaging Service.
  * **Faster Troubleshooting:** Separate voice, direct-number messaging, and Messaging Service configuration so the correct failure point can be identified quickly.


## **Before You Begin**

Confirming the correct Twilio account, phone number, and messaging path before editing webhooks prevents configuration changes from being applied to the wrong client or number.

  * Confirm the affected HighLevel location uses a **connected Twilio account** , not LC Phone.
  * Log in to the Twilio account or subaccount that owns the phone number.
  * Identify the exact phone number experiencing the issue.
  * Confirm whether the phone number is attached to a **Messaging Service**.
  * Do not replace webhook values belonging to another intentional integration unless the number should now route into HighLevel.


**A2P 10DLC is separate from webhook configuration.** Twilio may display A2P registration notices on the same screens. Completing webhook setup does not replace applicable A2P registration requirements.

## **Webhook Endpoints at a Glance**

Each event type must point to the appropriate HighLevel endpoint. Copy these values exactly and use **HTTP POST** where specified.

Event| Twilio Field| HighLevel Endpoint| Method  
---|---|---|---  
**Incoming Call**|  A call comes in| `https://services.leadconnectorhq.com/phone-system/voice-call/inbound`| **HTTP POST**  
**Call Status Update**|  Call status changes| `https://services.leadconnectorhq.com/appengine/twilio/incoming_call_status`| **HTTP POST**  
**Incoming SMS/MMS**|  A message comes in / Messaging Service Request URL| `https://services.leadconnectorhq.com/appengine/twilio/incoming_message`| **HTTP POST**  
**Messaging Service Fallback**|  Fallback URL| `https://services.leadconnectorhq.com/appengine/twilio/incoming_message`| **HTTP POST**  
  
**Do not mix the endpoints.** The incoming-call URL, call-status URL, and incoming-message URL perform different functions.

## **Direct Number vs. Messaging Service**

Incoming-message configuration depends on whether the Twilio number is using its own messaging webhook or belongs to a Messaging Service. Check the number's Active Configuration before changing messaging settings.

Configuration| Where to Configure Incoming Messages  
---|---  
**No Messaging Service linked**|  Configure the phone number's Messaging section directly.  
**Messaging Service linked**|  Open the linked Messaging Service and configure its Integration settings.  
  
**Voice configuration is still managed on the individual phone number.** A linked Messaging Service changes the messaging setup path, not the Voice Configuration steps below.

## **How to Set Up Twilio Webhooks for HighLevel**

Configure voice first, then configure messaging using the path that applies to the phone number. Save each configuration before testing so Twilio uses the updated webhook values.

### **Step 1: Open the Twilio Phone Number**

  1. Log in to the Twilio account or subaccount that owns the affected number.
  2. Go to **Phone Numbers → Manage → Active Numbers**.
  3. Select the phone number you want to configure.


[Open Twilio Active Numbers →](<https://console.twilio.com/us1/develop/phone-numbers/manage/incoming>)

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080149836/original/bQdShEuBKREN9VYnYFrWSTpj806csZkc0g.jpeg?1788548209)

### **Step 2: Open the Number's Configure Tab**

After selecting the phone number, open **Configure**. This page contains the routing, Voice Configuration, and Messaging configuration used for the number.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080149838/original/bP7eC5GCwGBE8YwcoKHoEfOIHZooJ-x3UQ.jpeg?1788548218)

### **Step 3: Confirm US1 Voice Routing**

Under **Voice Configuration** , confirm the Routing area shows **United States (US1) Region call routing is: Active**. If US1 is not active, use Twilio's routing controls to update the configuration before continuing.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080149845/original/8Z-XLh_cbAv7x5v9uAmn4VZ-GCFy-Rr9Mg.jpeg?1788548230)

### **Step 4: Configure Incoming Calls and Call Status Updates**

Voice Configuration needs two HighLevel endpoints: one for new inbound calls and one for subsequent call-status changes.

**Configure with**|  Webhook, TwiML Bin, Function, Studio Flow, Proxy Service  
---|---  
**A call comes in**|  Webhook  
**Incoming Call URL**| `https://services.leadconnectorhq.com/phone-system/voice-call/inbound`  
**HTTP**|  HTTP POST  
**Primary handler fails**|  No change required for this setup.  
**Call status changes URL**| `https://services.leadconnectorhq.com/appengine/twilio/incoming_call_status`  
**Call Status HTTP**|  HTTP POST  
**Caller Name Lookup**|  Optional. Leave at your preferred setting.  
  
Save the phone-number configuration after entering the values.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080149853/original/IlcEg0CgJmsfxVU2KtAK92q_EzbK0G8aPw.jpeg?1788548240)

### **Step 5: Confirm US1 Messaging Routing**

In the phone number's Messaging configuration, confirm **United States (US1) Region message routing is: Active**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080149860/original/8YeyN1X4W-58yewvde58E7oKhTaS6C2EQQ.jpeg?1788548252)

### **Step 6: Configure Incoming Messages**

Use the path that matches the phone number's current Twilio configuration.

Path A — Number Is Not Connected to a Messaging Service

  1. Remain on the individual phone number's **Configure** page.
  2. Under Messaging, set **Configure with** to **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
  3. Set **A message comes in** to **Webhook**.
  4. Enter:  
`https://services.leadconnectorhq.com/appengine/twilio/incoming_message`
  5. Set the method to **HTTP POST**.
  6. Save the configuration.


Path B — Number Is Connected to a Messaging Service

If **Active Configuration** displays a linked Messaging Service, configure inbound messaging from that service instead of relying only on the number-level messaging field.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080149861/original/lCBD9SDZoHAkHMxhiniHtFMts3-l7JPeCA.png?1788548266)

  1. From **Active Numbers** , click the linked Messaging Service.
  2. Open **Integration**.
  3. Under **Incoming Messages** , select **Send a webhook**.
  4. Enter the following **Request URL** :  
`https://services.leadconnectorhq.com/appengine/twilio/incoming_message`
  5. Set the Request URL method to **HTTP POST**.
  6. Enter the same URL as the **Fallback URL** :  
`https://services.leadconnectorhq.com/appengine/twilio/incoming_message`
  7. Set the Fallback URL method to **HTTP POST**.
  8. Click **Save**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080149864/original/AkMZJ6tAZXJO-GjSEuA8nrmbdNSyaWPjpA.png?1788548280)

The call-status callback configured earlier belongs to the phone number's **Voice Configuration**. Do not copy the call-status URL into the Messaging Service's Delivery Status Callback field.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080149881/original/_BzNdLZvI5inEWeJVlZfa9apefXYYnKn7A.png?1788548290)

### **Step 7: Test the Configuration**

After saving the Twilio configuration, test each communication path separately so you can identify exactly which webhook is working or failing.

  1. Call the Twilio number from an external phone and confirm the incoming call reaches HighLevel.
  2. Send an SMS to the Twilio number and confirm the message appears in **Conversations**.
  3. Review the associated call activity in HighLevel to confirm call-status information is updating.


## **Troubleshooting Twilio Webhooks**

Troubleshoot the event that is failing instead of changing every webhook at once. Voice, call status, and messaging use separate configuration fields, so one can fail while the others continue working.

Incoming Calls Do Not Reach HighLevel

Confirm the correct Twilio number is selected, US1 voice routing is active, **A call comes in** is set to Webhook, the incoming-call URL is exact, the method is HTTP POST, and the configuration has been saved.

Calls Work but Call Status Does Not Update Correctly

Re-check the **Call status changes** URL and confirm it uses **HTTP POST**. The call-status endpoint is different from the inbound-call endpoint.

Incoming SMS Does Not Appear in Conversations

First determine whether the number is attached to a Messaging Service. If it is, check the service's **Integration** settings. If it is not, check the number-level messaging webhook. Also confirm the number supports SMS.

The Webhook Looks Correct but Messages Still Do Not Appear

Review Twilio's Messaging Logs for the affected message. Confirm the message reached Twilio, note its status and Message SID, and use those details when escalating the issue.

The Wrong Twilio Subaccount Was Configured

If your Twilio account contains multiple subaccounts, confirm the affected phone number belongs to the same Twilio subaccount connected to the HighLevel location before changing webhooks.

Webhook Values Keep Changing

Review whether another connected application or integration is managing the Twilio number. Repeatedly replacing webhooks without identifying the integration that owns them can cause routing conflicts.

## **Frequently Asked Questions**

Q: Do I need to configure these webhooks if I use LC Phone?

No. These steps are for locations connected to their own Twilio account. LC Phone webhook configuration is managed by the platform.

Q: I have several Twilio subaccounts. How do I know which one to configure?

Confirm the Twilio subaccount connected to the affected HighLevel location and make sure that subaccount owns the phone number you are troubleshooting. Configuring the same phone number or webhook in another Twilio account will not correct the connected location.

Q: Do I need to configure every Twilio phone number?

Voice Configuration is stored on the individual Twilio phone number, so verify each affected number. Numbers that share a Messaging Service can use that service's shared inbound-message integration settings.

Q: Why can calls work even when incoming SMS is missing?

Voice and messaging use separate webhook settings. A correct Voice Configuration does not confirm that the number-level messaging webhook or linked Messaging Service is configured correctly.

Q: Should the Messaging Service Request URL and Fallback URL be the same?

Yes. For the HighLevel Twilio setup documented here, both use `https://services.leadconnectorhq.com/appengine/twilio/incoming_message` with HTTP POST.

Q: Does the call-status webhook belong in the Messaging Service Delivery Status Callback field?

No. The `incoming_call_status` endpoint belongs in the phone number's Voice Configuration under **Call status changes**. It should not be reused as a Messaging Service delivery-status callback.

Q: Does configuring these webhooks complete A2P 10DLC registration?

No. Webhook configuration and A2P 10DLC registration are separate. A US local number used for application-to-person messaging may still require an approved A2P registration and proper Messaging Service association.

Q: What should I collect before escalating a webhook issue?

Collect the affected HighLevel location, Twilio subaccount, phone number, exact timestamp of the failed event, screenshots of the current webhook configuration, and the relevant Twilio Call SID or Message SID when available.

### **Related Articles**

[ Troubleshooting: Inbound SMS Showing as Calls or Not Appearing at All ](<https://help.gohighlevel.com/support/solutions/articles/48001181601-troubleshooting-inbound-sms-showing-as-calls-or-not-appearing-at-all->) [ How to Check Logs for a Specific Text Message in Twilio ](<https://help.gohighlevel.com/support/solutions/articles/48001222601-how-to-check-logs-for-a-specific-text-message-if-you-are-connected-to-your-own-twilio-account>) [ US Phone Number Registrations — A2P 10DLC ](<https://help.gohighlevel.com/support/solutions/articles/155000002380-what-is-a2p-10-dlc-brand-and-campaign-registration-faqs-and-summary>) [ Overview of Phone Number Configuration Options ](<https://help.gohighlevel.com/support/solutions/articles/48001229976-overview-of-phone-number-configuration-options>) [ What is the Native Phone System? ](<https://help.gohighlevel.com/support/solutions/articles/48001223546>) [ How Do I Migrate My Agency and Sub-Account Over to LC Phone? ](<https://help.gohighlevel.com/support/solutions/articles/48001204027>)

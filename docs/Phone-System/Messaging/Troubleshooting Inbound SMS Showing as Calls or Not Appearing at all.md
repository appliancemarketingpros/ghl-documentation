# Troubleshooting: Inbound SMS Showing as Calls or Not Appearing at all.

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001181601-troubleshooting-inbound-sms-showing-as-calls-or-not-appearing-at-all-](https://help.gohighlevel.com/support/solutions/articles/48001181601-troubleshooting-inbound-sms-showing-as-calls-or-not-appearing-at-all-)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Troubleshooting

Incoming SMS Not Showing Up (or Appearing as Calls)

How to troubleshoot and resolve missing or miscategorized inbound texts, for both Twilio and LC Phone.

Overview

If you're not seeing incoming SMS messages in the platform — or they're showing up as calls instead — this guide walks you through how to troubleshoot and resolve the issue based on whether you're using Twilio or LC Phone.

Table of Contents

1

How to Fix This (At a Glance)

2

Step-by-Step Fix (for Twilio Users)

3

Check SMS Capability

4

Review Message Logs

5

Frequently Asked Questions

1

## How to Fix This (At a Glance)

✅ For LC Phone Users

Contact [Support](<https://help.gohighlevel.com/support/tickets/new>) for resolution.

✅ For Twilio Users (Non-LC Phone)

  * Check Twilio Number Configuration
    * Number is SMS/MMS-capable.
    * Webhook URL is correctly set for messaging.
  * **Check whether the phone number is linked to a Twilio Messaging Service.** If it is, verify incoming-message routing in the Messaging Service's **Integration** settings. If it is not, verify the phone number's own Messaging webhook.
  * Review Message Logs.
  * If the issue still persists, contact [Twilio Support](<https://support.twilio.com>).


2

## Step-by-Step Fix (for Twilio Users)

Step 1

Log in to Twilio

  * Go to [twilio.com/login](<https://www.twilio.com/login>) and sign in.
  * In the top-left drop-down, click **Account Name > View Subaccounts**.


![Twilio account dropdown showing View Subaccounts](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048323954/original/vSEfQvPJiGA_zCYQVSYDBuW57Nd8YiVNrw.png?1750080048)

Note

If you have multiple subaccounts and can't find the right one, go to your **Agency View > Settings > Phone Integration > Sub-Account Settings**. Search for the account you're troubleshooting and copy the Account SID as shown in Screenshot 2.0 below.

![Copying the Account SID from Sub-Account Settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048325672/original/qGhVCcYLVbwLO1VN4X0Xpn3w8q35BA32yA.png?1750081121)

Screenshot 2.0

Step 2

Find the Correct Twilio Number

  * In Subaccounts, paste the Account SID into the search bar to find the matching subaccount.
  * Click on the sub-account you were looking for.
  * Go to **Phone Numbers > Manage > Active Numbers**.
  * Click the phone number in question.


![Searching subaccounts by Account SID](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048326658/original/wfGuy2jN0edS5KwbyvRVA0mOpKVvm0t0sg.png?1750081679)

Screenshot 3.0

![Active Numbers list under Phone Numbers > Manage](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048327877/original/_D4Wur5uDAlf_h1E3_d7NGARNhx25WrDYA.png?1750082372)

Screenshot 3.1

Step 3 

### **Confirm the Incoming Message Webhook**

  


First, check whether the Twilio number is connected to a **Messaging Service**.

**If the number is not connected to a Messaging Service:**

  1. Open the Twilio phone number.
  2. Scroll to **Messaging**.
  3. Set **A message comes in** to **Webhook**.
  4. Enter:  
`https://services.leadconnectorhq.com/appengine/twilio/incoming_message`
  5. Set the method to **HTTP POST**.
  6. Click **Save**.


  


**If the number is connected to a Messaging Service:**

  1. Open the linked Messaging Service.
  2. Go to **Integration**.
  3. Under **Incoming Messages** , select **Send a webhook**.
  4. Enter:  
`https://services.leadconnectorhq.com/appengine/twilio/incoming_message`
  5. Set the Request URL method to **HTTP POST**.
  6. Enter the same URL as the **Fallback URL**.
  7. Set the Fallback URL method to **HTTP POST**.
  8. Click **Save**.


![Messaging webhook configuration field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048362616/original/2ntLPpZIJdr7VF4u9xmzO-7KppYrsCYUyQ.png?1750139542)

Screenshot 3.2

![Messaging webhook saved correctly](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048362676/original/1DQr6QHWJDF3N6X0Dg1dY6R8xfOOb_ydtg.png?1750139698)

Screenshot 3.3

### Test the Configuration

  1. Send a new SMS to the Twilio number from an external phone.
  2. Confirm that the message appears in **Conversations** in HighLevel.
  3. If it does not appear, review the corresponding message in Twilio **Messaging Logs**.
  4. Record the **Message SID** and exact timestamp if further troubleshooting is required.


3

## Check SMS Capability

Confirm that the Twilio phone number supports **SMS**. If the inbound message contains media, also confirm that the number supports **MMS**.

  


A dagger icon (†), when shown in Twilio, indicates that SMS capability may be limited to domestic messaging for that number.

![Dagger icon indicating domestic-only SMS capability](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048330328/original/NZze8-m4RTxheJoX6VOiTVKmwDY7auuZLA.png?1750083890)

Screenshot 3.4

4

## Review Message Logs

  * In the left sidebar, click **Monitor > Logs > Messaging**.
  * Enter the **contact's phone number in the From field** when troubleshooting an inbound SMS.

Use the **To** field when troubleshooting an outbound SMS sent to the contact.

  * Review the message status.
  * Click the Date to view message details.


![Twilio Messaging logs filtered by phone number](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048331030/original/ViTgBcW-gKaOnr8ozV98rbF4K16o2ZsVYQ.png?1750084349)

Screenshot 4.0

Note

**Note:** If Twilio shows the inbound message in **Messaging Logs** but the message does not appear in HighLevel, copy the **Message SID** , exact timestamp, sender number, recipient number, and message status.

Then verify the incoming-message webhook or Messaging Service configuration. If the configuration is correct and the issue continues, include these details when escalating the issue.

5

## Frequently Asked Questions

Q: How do I know if I'm using Twilio or LC Phone?

Check your number under Settings → Phone Numbers. Numbers provisioned through the platform's built-in phone system are LC Phone; numbers connected through your own Twilio account are Twilio numbers.

Q: I have several Twilio subaccounts and can't tell which one is mine — what do I do?

Grab the Account SID from Agency View → Settings → Phone Integration → Sub-Account Settings, then paste it into the subaccount search bar in Twilio to jump straight to the right one.

Q: Why would an incoming text show up as a call instead of a message?

This can happen when Twilio's incoming-message routing is not configured correctly.

First determine whether the number is connected to a **Messaging Service** :

  * If it is not, verify the number-level **A message comes in** webhook.
  * If it is, verify the Messaging Service's **Integration** settings.


Also confirm that the HighLevel incoming-message endpoint is configured with **HTTP POST**.

  


Q: What does the dagger icon next to a number mean?

It flags a number that can only send and receive SMS within its own country. If you're messaging internationally from that number, this is likely why messages aren't arriving.

Q: The Twilio log shows "Delivered" but I still don't see the message — who's responsible?

At that point the message reached Twilio successfully, so the gap is on the delivery/webhook side. Copy the Message SID and open a ticket with Twilio Support so they can trace where the payload stopped.

Q: I'm on LC Phone and having the same issue — can I fix the webhook myself?

No. LC Phone numbers are managed on the platform's side, so you won't have direct access to webhook settings. Contact Support and they'll investigate and resolve it for you.

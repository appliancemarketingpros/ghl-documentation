# Error: The "From" number is not SMS-capable.

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001180919-error-the-from-number-is-not-sms-capable-](https://help.gohighlevel.com/support/solutions/articles/48001180919-error-the-from-number-is-not-sms-capable-)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Troubleshooting

# Error: The "From" Number Is Not SMS-Capable

Resolve sender validation errors and configure SMS-capable phone numbers in HighLevel

What You'll Learn

This article explains the "From number is not SMS-capable" error and provides step-by-step solutions for verifying number capabilities, ownership, A2P registration status, and proper formatting in HighLevel.

This error indicates that the selected sender cannot be used for the attempted message. If the message was accepted for sending but failed later with a carrier or delivery error, use the general SMS delivery troubleshooting guidance instead.

Table of Contents

1

What Is the Error?

2

Quick Fix Checklist

3

Common Causes & How to Resolve

4

Special Cases and Number Types

5

Related Articles

6

Frequently Asked Questions

1

## What Is the Error?

The "From number is not SMS-capable" error occurs when HighLevel or the connected phone provider rejects an outbound SMS because the sender number cannot be used for text messaging. This validation happens before the message is sent to the carrier network.

The error can appear in Conversations, workflow send actions, campaign message logs, or API responses. It indicates a configuration or capability issue with the From number itself, not a delivery or carrier rejection after the message was accepted.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079971452/original/0VwsyZ28FnI-EuizCVmk69mKcrCRGqcp1g.png?1788419464)

This error is distinct from carrier delivery failures that occur after a message is accepted. If you see error codes related to carrier filtering, spam detection, or destination unreachable, refer to the general SMS delivery troubleshooting resources.

2

## Quick Fix Checklist

These checks address the most common reasons HighLevel or the connected phone provider rejects a sender number before an SMS is sent. Start here before changing phone-system settings or purchasing another number.

**Verify the number supports SMS:** Confirm the sender number is provisioned with messaging capability (not voice-only). A number can support voice but not SMS, so successful calling does not confirm that the number can send text messages.

**Confirm ownership and assignment:** Ensure the number belongs to your HighLevel location or connected phone account and is properly assigned in the messaging configuration.

**For US 10DLC numbers:** Confirm A2P registration and Campaign association. **LC Phone:** Confirm the number is associated with the approved Brand/Campaign in HighLevel. **Twilio/BYOT:** Confirm the number is attached to the appropriate Messaging Service associated with the approved Campaign.

**Check number format:** If the sender number is entered manually or referenced in an integration or API request, use E.164 format, including + and the country code (e.g., +15551234567).

**Verify sender/destination compatibility:** Confirm the sender type (local number, toll-free, short code, or alphanumeric ID) is valid for the destination country.

3

## Common Causes & How to Resolve

The following scenarios are the most frequent causes of the "From number is not SMS-capable" error. Review each to identify and resolve the configuration issue.

Cause 1

The Number Is Not SMS-Capable

Some phone numbers are provisioned for voice only and cannot send or receive text messages. This is common with older numbers, certain porting scenarios, or numbers purchased without messaging capability.

**How to check:**

  * **LC Phone:** Navigate to **Settings → Phone Numbers** , open the number details, and confirm that **Messaging** is enabled.
  * **Twilio / BYOT:** Log in to your Twilio console, locate the number, and verify that **Capabilities** includes **SMS**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079971441/original/EGwEG9AhihK13aLGVhV3vC446hJO1NQiLQ.png?1788419439)

**Solution:** If the number does not support SMS, enable messaging capability (if available) or select a different SMS-capable number. If the number was recently purchased or ported, allow 24–48 hours for carrier provisioning to complete.

Cause 2

The Number Isn't Valid for Your Account or Destination

The sender must be provisioned or hosted for messaging in the current HighLevel location or connected phone account and must be valid for the destination being messaged. Using a number that belongs to a different location, a disconnected Twilio account, or an incompatible sender type for the destination will trigger this error.

**Common scenarios:**

  * The number was hosted to a different HighLevel location and is no longer available in the current location.
  * The Twilio account or API credentials associated with the number have been disconnected or changed.
  * The sender type is not supported for the destination country (e.g., using a US local number to message an international recipient that requires an alphanumeric sender ID).
  * A short code is being used to message a destination in a different country. Short codes are country-specific and generally cannot be used for cross-country messaging.


**Solution:** Verify the number is provisioned in the current location's phone system or connected Twilio account. For hosted numbers, confirm the number is correctly assigned to the active location. For international messaging, confirm the destination country's supported sender requirements before selecting the From value.

Cause 3

A2P Registration or Number Assignment May Be Incomplete (US 10DLC)

In the United States, local 10-digit numbers used for application-to-person (A2P) messaging must be registered with an approved Brand and Campaign. If the number is not properly associated with an active A2P Campaign, messaging may fail or be restricted.

**How to check:**

  * **LC Phone:** Navigate to **Settings → Phone Numbers** , select the number, and confirm it is linked to an approved Brand and Campaign. If the Campaign status is pending or rejected, the number cannot be used for A2P messaging.
  * **Twilio / BYOT:** Log in to your Twilio console, verify the number is attached to a Messaging Service, and confirm the Messaging Service is associated with an approved A2P Campaign. Check the Campaign approval status in the Twilio Trust Hub.


**Solution:** If A2P registration is incomplete, complete the Brand and Campaign registration process. If the Campaign is approved but the number is not assigned, attach the number to the appropriate Messaging Service (Twilio) or assign it to the Campaign in HighLevel (LC Phone). Note that A2P registration issues may produce different error messages depending on carrier validation. If this check passes but the error persists, review the exact messaging error code.

Cause 4

The Number Was Recently Moved or Re-Hosted

If a number was recently ported, hosted to a new location, or moved between phone accounts, HighLevel may still reference the old configuration. This can cause sender validation to fail even though the number is active in the new account.

**Solution:** Re-select the active number in Conversations sender settings, Campaigns and Workflows sender configuration, default messaging settings, user-assigned numbers, and any external integration that stores the sender number. After updating the sender reference, test an outbound message to confirm the new number is recognized.

Cause 5

The From Value Is Formatted Incorrectly

When a From number is entered manually in a workflow, API request, or integration, it must use E.164 international format, which includes a + symbol, the country code, and the full phone number with no spaces or special characters (e.g., +15551234567).

**Solution:** If the sender is manually entered or dynamically referenced, verify the format matches E.164. For standard Conversations and campaign messages, the From dropdown automatically formats the number correctly, so manual formatting is not required.

4

## Special Cases and Number Types

Certain sender types have additional requirements or restrictions that can contribute to the "From number is not SMS-capable" error. Review the following if you are using toll-free numbers, short codes, or messaging internationally.

Toll-Free Numbers (US/Canada)

Verification Required for Reliable Delivery

An SMS-capable toll-free number may still experience delivery restrictions if Toll-Free Verification is incomplete. While toll-free numbers can technically send messages without verification, carriers increasingly filter or block unverified toll-free traffic. If the sender passes capability checks but messages still fail, review Toll-Free Verification status and the returned messaging error code.

Short Codes

Country-Specific Sender Type

Short codes are country-specific and generally cannot be used for cross-country messaging. Use a sender type supported for the destination country. If you attempt to send from a US short code to a Canadian or international recipient, the message will fail with a sender validation error.

International Messaging

Sender Requirements Vary by Country

Messaging sender requirements vary by destination country. Some countries require registered sender IDs, approved number types, or Alphanumeric Sender IDs. For example, certain countries do not accept long-code A2P messaging and require an approved alphanumeric sender or short code. Confirm the destination country's supported sender requirements before changing the From value. If the sender type is not supported for the destination, you will need to provision an approved sender for that country.

5

## Related Articles

  * [LC Phone System – Error Code and Warning Dictionary](<https://help.gohighlevel.com/en/support/solutions/articles/155000005526>)
  * [Understanding Common SMS Delivery Errors](<https://help.gohighlevel.com/en/support/solutions/articles/48001208912>)
  * [Number Hosting Guidelines for LC Phone Locations](<https://help.gohighlevel.com/en/support/solutions/articles/48001230556>)
  * [Troubleshooting SMS Delivery](<https://help.gohighlevel.com/en/support/solutions/articles/48000981696>)


6

## Frequently Asked Questions

Q: Does this error mean the number is suspended or inactive?

Not necessarily. The error indicates a configuration or capability issue, not a suspension. A number can be active for voice calls but not enabled for SMS, or it may be assigned to the wrong location or phone account. Check the number's messaging capability and assignment before assuming it is suspended.

Q: What if I don't see my number in the From dropdown?

If the number does not appear in the sender dropdown, it is not provisioned or assigned to the current HighLevel location. Verify the number exists in **Settings → Phone Numbers** (LC Phone) or confirm the connected Twilio account includes the number. If the number was recently added or hosted, refresh the location settings or reconnect the phone integration.

Q: Does this error affect MMS as well as SMS?

Yes. If the From number is not SMS-capable, it also cannot send MMS. MMS requires the same messaging capability as SMS, plus additional media support. Resolve the SMS capability issue first, then verify MMS is enabled for the number.

Q: Why does a recently ported or added number still show the error?

Newly ported or provisioned numbers can take 24–48 hours to complete carrier activation and messaging capability setup. During this period, the number may appear in your account but not yet support SMS. Wait for the provisioning window to complete, then verify messaging is enabled in the number settings.

Q: Can I use a landline number as the From number?

No. Landline numbers cannot send or receive SMS. Only mobile-capable, toll-free, short code, or VoIP numbers provisioned with messaging capability can be used as SMS senders. If you need to message from a business phone number, port it to a VoIP or SMS-capable service, or use a dedicated SMS number.

Q: My number is SMS-capable, but I still get this error. What should I check next?

Confirm that the number belongs to the current location, is properly assigned to the messaging configuration, and is valid for the destination country. For US local numbers, also confirm A2P registration and Campaign association. If those checks pass, review the exact messaging error code in the delivery logs or error dictionary. The error may indicate a related but distinct issue, such as a Messaging Service misconfiguration or carrier-level restriction.

Q: Can I use an alphanumeric sender ID instead of a phone number?

Alphanumeric sender IDs are supported for international messaging in certain countries, but they are not universally accepted. In the United States and Canada, alphanumeric IDs are not supported for standard SMS. If you are messaging internationally and the destination country supports alphanumeric sender IDs, you can configure one in HighLevel. However, recipients cannot reply to messages sent from an alphanumeric ID.

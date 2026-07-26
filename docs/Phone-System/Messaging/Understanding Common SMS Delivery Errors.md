# Understanding Common SMS Delivery Errors

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001208912-understanding-common-sms-delivery-errors](https://help.gohighlevel.com/support/solutions/articles/48001208912-understanding-common-sms-delivery-errors)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Troubleshooting

Understanding Common SMS Delivery Errors

How to identify, interpret, and resolve the most common SMS/MMS delivery error codes.

Overview

This article provides a comprehensive guide to understanding and resolving common SMS delivery errors in the platform. By identifying typical failure points and offering practical solutions, you can enhance your messaging success rate and ensure effective communication with your contacts.

Table of Contents

1

What Are Common Unsuccessful SMS Errors?

2

How to Identify and Interpret Common SMS Errors

3

Common Error Codes and What They Mean

4

Additional Troubleshooting Tips

5

Frequently Asked Questions

6

Related Articles

1

## What Are Common Unsuccessful SMS Errors?

SMS delivery errors occur when a message cannot be delivered to the intended recipient due to issues like invalid numbers, carrier filtering, user opt-outs, or technical restrictions. Understanding these errors helps businesses maintain high message deliverability and comply with industry regulations.

Most of these errors originate from carriers, Twilio, or LC Messaging, and are represented by specific error codes. Identifying and interpreting these codes enables users to take corrective action quickly and confidently.

### Key Benefits of Understanding SMS Errors

Recognizing and addressing SMS errors promptly can significantly improve your communication strategy.

  * **Enhanced Deliverability:** By identifying common errors, you can take proactive steps to prevent message failures.
  * **Efficient Troubleshooting:** Understanding error codes allows for quicker resolution of issues.
  * **Improved Compliance:** Awareness of carrier and platform restrictions helps maintain compliance and avoid penalties.
  * **Optimized Messaging Strategies:** Insights into errors can inform better messaging practices and content.


2

## How to Identify and Interpret Common SMS Errors

Accurate diagnosis of SMS errors requires checking delivery logs, identifying the error code, and using the information to adjust your messaging or recipient data.

Step 1

Go to the Conversation Logs

  * Click on the **Conversations** tab from your account.
  * Search for the **SMS log** that was unsuccessful.
  * Click on the unsuccessful **Conversation**.
  * Hover over the **Red Triangle Error Box**.


![Locating the unsuccessful SMS log in Conversations](https://jumpshare.com/v/3y1TTEGBoYVOYYkLuXR0+/Screen+Shot+2025-05-29+at+6.59.38+PM.png)

![Hovering over the red triangle error box in a conversation](https://jumpshare.com/v/GQuCGpZiPfibXmvZGEOw+/Screen+Shot+2025-05-29+at+7.06.05+PM.png)

Step 2

Locate and Identify the SMS Error Code

The dialogue box will display the **numerical error code** and a **short description of the error** for that conversation (e.g., Error 30034, Error 21610).

![Error code dialogue box shown for a failed conversation](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155047435739/original/VVBlPxy5MAQEGjqIOqDzF7oY6ERGFRh_qg.png?1748526440)

3

## Common Error Codes and What They Mean

The following are the most frequently encountered SMS errors within the platform:

Error 11751

Media Message Size Limit Exceeded

**Description:** The total size of the media message exceeds the maximum limit allowed by the messaging provider.

**Resolution:**

  * Compress or resize the media file.
  * Ensure the file stays within Twilio's supported MMS size limits.
  * **MMS (US/Canada):** Maximum size is 5MB per message.


Error 21610

DND Enabled or user has unsubscribed by replying STOP

**Description:** The recipient has opted out of receiving messages by replying with STOP.

**Resolution:**

  * Do not message this number again unless the user sends START to opt back in.
  * Ensure proper opt-in mechanisms are in place.


Error 21612

Messaging to {{destination_country}} is not allowed with {{source_country}} phone numbers. Please use a local number.

**Description:** The recipient number can't be reached using the current 'From' number (e.g., due to carrier restrictions or unsupported international routes).

**Resolution:**

  * Use a local or internationally enabled number.
  * Confirm routing compatibility between 'To' and 'From' numbers.


Error 30002

Message failed: your Twilio account is currently suspended.

**Description:** Your Twilio account was suspended between the time of message send and delivery.

**Resolution:**

  * Contact Twilio Support to resolve account status.
  * Ensure your account remains active for message queues.


Error 30003

Number unreachable or out of service.

**Description:** The recipient's phone is turned off, out of range, or temporarily unavailable.

**Resolution:**

  * Retry the message later.
  * Verify the number is active.


Error 30004

Recipient has opted out or has DND enabled.

**Description:** The destination number is blocked from receiving this message.

**Resolution:**

  * Confirm the number is valid and not carrier-blocked.
  * Avoid messaging numbers with prior failed delivery history.


Error 30005

The recipient's number is inactive or does not exist.

**Description:** The destination device is unreachable (e.g., turned off or out of range for an extended period).

**Resolution:**

  * Retry after some time.
  * Clean your list to remove unreachable or inactive numbers.


Error 30006

Landline or non-mobile number. Cannot receive SMS.

**Description:** The number cannot receive SMS — usually because it's a landline or incompatible with SMS.

**Resolution:**

  * Remove landlines from your list using number validation tools.
  * Confirm numbers support SMS before messaging.


Error 30007

Message blocked due to carrier policies. This often happens if content violates carrier rules.

**Description:** The message was blocked by the carrier for violating content policies or appearing as spam.

**Resolution:**

  * Avoid spam-like content and shortened URLs.
  * Use personalized, compliant messaging.
  * Register your number with A2P 10DLC or Toll-Free verification.


Refer to for more context: [How to Prevent SMS Filtering by Carriers: Error 30007](<https://help.gohighlevel.com/support/solutions/articles/48001237726-how-to-prevent-sms-filtering-by-carriers-error-30007>)

Error 30034

Number not A2P compliant. Please register for A2P.

**Description:** You attempted to send a message to a U.S. number from a 10DLC number that is not associated with a registered A2P campaign.

**Resolution:**

  * Register your number through Twilio's Trust Hub.
  * Link the number to an approved Messaging Service.
  * Confirm proper campaign association.


Error 30008

Message failed due to unknown error. Retry or check Twilio logs.

**Description:** An unspecified error occurred during message delivery.

**Resolution:**

  * Check the message body for formatting or content issues.
  * Test with a different number or content structure.


Error 11200

HTTP Retrieval Failure

**Description:** This error often occurs when images fail to load or send in conversations.

**Resolution:**

  * Check the domain's DNS configuration using MXToolbox. If the DNS records aren't found or not pointing to `brand.ludicrous.cloud`, this can cause the image retrieval to fail.
  * Ensure a CNAME record is set up correctly, pointing your branded domain to `brand.ludicrous.cloud`.
  * If this is missing or misconfigured, images will appear broken in conversations. Check out [Branding System-Generated Links (API Domain)](<https://help.gohighlevel.com/en/support/solutions/articles/48001143244>).


![DNS configuration check for the branded domain](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155048038110/original/DSMUXHzu7zkN9Fk7fHyrtnbxHsMZ_Py14g.png?1749592564)

Error 30024

Numeric Sender ID Not Provisioned on Carrier

**Description:** You attempted to send a message to a mobile number in a country that requires pre-registration and provisioning of a Numeric Sender ID. However, the Numeric Sender ID has not yet been provisioned with the carrier.

**Resolution:** If you believe your Numeric Sender ID is already registered, please gather at least three Message IDs that show an "undelivered" status with error code 30024. Once you have these, contact our Support team, and we'll review the registration status to help resolve the issue.

Note

To explore additional error codes beyond those most commonly encountered in the platform, view the [Full Catalog of Error Codes](<https://www.twilio.com/docs/api/errors>).

4

## Additional Troubleshooting Tips

Understanding the technical side is helpful, but these best practices can proactively reduce errors:

Use Verified Sending Numbers

A2P 10DLC and Toll-Free numbers go through a vetting process that improves delivery rates and reduces filtering.

Format SMS Content Properly

Avoid all caps, spammy phrases, or including long URLs without a proper link shortener.

Use a conversational tone to avoid content blocks.

Maintain Clean Lists

Ensure numbers are valid, formatted correctly, and that users have opted in.

Monitor Error Trends

Use the platform's reporting tools to spot patterns in delivery issues and make proactive adjustments.

5

## Frequently Asked Questions

Q: How can I get a user to resubscribe after opting out?

The user must send a message with the word START to the same number they unsubscribed from.

Q: Can I resend messages that failed due to a 30007 error?

Yes, but first revise the content to comply with carrier filtering guidelines before retrying.

Q: Why do some messages fail even if the number is valid?

Carriers may still block messages due to content filtering or recipient settings.

Q: How can I tell if a number is a landline?

Use number validation tools or scrub lists before uploading to the platform.

Q: Will the platform alert me of frequent SMS errors?

You can review delivery reports, but setting up notifications via workflows is recommended for real-time alerts.

Related Articles

[Best Practices for SMS Deliverability and Avoiding SMS Restrictions](<https://help.gohighlevel.com/en/support/solutions/articles/155000000079>) [What Is A2P 10DLC, Brand and Campaign Registration — Summary and FAQs](<https://help.gohighlevel.com/en/support/solutions/articles/155000002380>) [Getting Started — Launch an SMS Campaign](<https://help.gohighlevel.com/en/support/solutions/articles/155000005065>) [A2P Standard Brand Registration for 10DLC](<https://help.gohighlevel.com/en/support/solutions/articles/48001225526>) [A2P Sole Proprietor Brand Registration for 10DLC](<https://help.gohighlevel.com/en/support/solutions/articles/155000000340>) [Toll-Free Number Verification Guide for LC-Phone (US/Canada)](<https://help.gohighlevel.com/en/support/solutions/articles/48001222300>)

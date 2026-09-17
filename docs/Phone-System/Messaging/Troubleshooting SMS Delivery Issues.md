# Troubleshooting SMS Delivery Issues

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981696-troubleshooting-sms-delivery-issues](https://help.gohighlevel.com/support/solutions/articles/48000981696-troubleshooting-sms-delivery-issues)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Troubleshooting

# Troubleshooting SMS Delivery Issues

A comprehensive guide to diagnosing and resolving SMS delivery failures in HighLevel, from error codes to carrier filtering and registration requirements.

What You'll Learn

This article provides a structured troubleshooting framework for SMS delivery issues in HighLevel. You will learn how message delivery works across three layers, where to find error details, and how to resolve the most common failure scenarios.

Use this guide as your entry point for SMS troubleshooting, then reference the current error code dictionary and specialized articles for specific resolution steps.

Table of Contents

1

How SMS Delivery Works

2

Where to Find Error Messages

3

Troubleshooting Checklist

4

Common SMS Delivery Failures

5

Related Articles

6

Frequently Asked Questions

1

## How SMS Delivery Works

When you send an SMS through HighLevel, the message passes through three distinct layers before reaching the recipient. Understanding this flow helps you identify where a failure occurs and how to resolve it.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080046090/original/W62xcyzPKTTwQBt90fgpNNghaweLfRwqgQ.png?1788455942)  


Layer 1

HighLevel Platform

HighLevel validates the message format, checks contact opt-out status, enforces workflow rules, and applies account-level restrictions such as daily send caps or ramp-up limits.

Layer 2

Phone Provider

LC Phone or Twilio (for BYOT accounts) validates the sender number, checks A2P or Toll-Free registration status, enforces geo-permissions, and may filter messages based on content or policy.

Layer 3

Mobile Carrier

The recipient's mobile carrier delivers the message to the device. Carriers may apply their own filtering, block messages to invalid or inactive numbers, or reject messages due to handset issues.

Most delivery failures generate an error code that indicates the layer and reason for the failure. Use the error code to determine the correct resolution path.

2

## Where to Find Error Messages

HighLevel surfaces SMS delivery errors in multiple locations depending on your workflow and account configuration.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080046133/original/ho_a7lVajWIIPQw5NKJZ-LBX8HR3LcwUZg.png?1788456007)

**Conversations Tab** — Open the failed message thread in the Conversations area. Failed messages display a red status indicator and an error code or description.

**Contact Timeline** — View the contact record and check the Activity or Communication timeline. Failed SMS events appear with error details.

**Workflow Logs** — If the message was sent from an automated workflow, check the workflow execution log for send failures and associated error codes.

**Phone Provider Logs** — LC Phone users can reference error codes in the LC Phone System - Error Code and Warning Dictionary. Accounts using their own Twilio integration (BYOT) can also review Twilio message logs for additional context.

Tip

Always note the exact error code when troubleshooting. The code determines the root cause and the correct resolution steps.

3

## Troubleshooting Checklist

Follow this structured checklist to diagnose and resolve SMS delivery failures efficiently.

Step 1

Identify the Scope

Determine whether the failure affects one contact, one sending number, or all outbound messages. This helps you narrow the troubleshooting path.

Step 2

Check the Failed Message in Conversations

Open the failed message in Conversations and note the status (e.g., failed, undelivered) and the exact error code displayed.

Step 3

Check the Recipient

Verify the recipient's phone number is a valid mobile number, formatted correctly, SMS-capable, and not on the opt-out or Do Not Disturb list.

Step 4

Check the Sender

Confirm the sending number is SMS-capable, active, correctly configured for your location, and has valid A2P or Toll-Free registration status if required.

Step 5

Check Account Restrictions

Review whether your account or sending number has hit daily send caps, is in a ramp-up period, is suspended, or lacks geo-permissions for the destination country.

Step 6

Check Message Content

Verify the message length is within carrier limits, MMS attachments are under 5 MB, URLs are valid, and content complies with messaging policy to avoid filtering.

Step 7

Use the Current Error Dictionary

Look up the displayed error code in the LC Phone System - Error Code and Warning Dictionary for the exact cause and recommended resolution.

Step 8

Retest Once After Correction

After applying the fix, send a test message to confirm delivery. Avoid retrying repeatedly without addressing the root cause.

Step 9

Escalate with Examples if the Failure Persists

If the issue continues after troubleshooting, contact HighLevel Support with specific examples: the sending number, recipient number, timestamp, and error code.

4

## Common SMS Delivery Failures

The following failure categories cover the majority of SMS delivery issues. Use the error code displayed in Conversations to identify the specific problem, then apply the recommended resolution.

Failure Category

Recipient Previously Opted Out

If the recipient opted out by sending STOP or another supported keyword, outbound messaging remains blocked until they opt back in using a supported resubscribe keyword such as START, where applicable.

**Resolution:** The contact must send the resubscribe keyword to the same number. Review your consent practices to prevent future opt-outs.

Failure Category

Invalid or Non-SMS-Capable Number

Messages fail when the recipient number is a landline, invalid, disconnected, or formatted incorrectly.

**Resolution:** Confirm the destination is SMS-capable and use a valid mobile or message-capable number.

Failure Category

A2P or Toll-Free Registration Is Incomplete

US local and toll-free numbers may require appropriate registration or verification before messaging. Common error codes include 30032 (Toll-Free number not verified), 30033 (A2P Campaign suspended), and 30034 (Number not fully registered or associated for A2P messaging).

**Resolution:** Confirm that the sender is properly registered and associated with the correct approved Campaign or verification record. Review the relevant A2P or Toll-Free registration articles in the Related Articles section.

Failure Category

Message Filtered by HighLevel or the Carrier

Messages may be blocked when content appears spam-like, violates messaging policy, uses prohibited content, or triggers carrier filtering. Error code 30007 is a common indicator of filtering.

**Resolution:** Review the exact error code, your consent practices, message content, and current messaging-policy guidance before resending. Refer to the article How to Prevent SMS Filtering by Carriers: Error 30007 for detailed mitigation steps.

Failure Category

Messaging Limits or Account Suspension

HighLevel enforces daily send caps, ramp-up periods, and account-level restrictions. New numbers or campaigns may be limited to lower volumes initially.

**Resolution:** Check your account's current daily cap and ramp-up status. If your account is suspended, contact HighLevel Support to resolve the underlying issue.

Failure Category

International Geo Permissions

Sending messages to international destinations requires geo-permissions to be enabled for the destination country.

**Resolution:** Enable geo-permissions for the destination country in your account settings or contact HighLevel Support to request access.

Failure Category

MMS or File Size Issues

MMS messages fail when attachments exceed carrier limits (typically 5 MB) or when the recipient's carrier does not support MMS.

**Resolution:** Reduce the attachment size below 5 MB or send the attachment as a link. Confirm the recipient's carrier supports MMS delivery.

Failure Category

Sender Number Is Not SMS-Capable

The sending number may not be provisioned for SMS or may be inactive, suspended, or incorrectly configured.

**Resolution:** Verify the number is active, SMS-enabled, and correctly associated with your account. If the number is new, confirm it has completed provisioning.

Note

This list covers broad failure categories. Always reference the LC Phone System - Error Code and Warning Dictionary for the exact cause and resolution steps associated with a specific error code.

5

## Related Articles

For additional guidance on SMS delivery, error codes, and messaging best practices, review the following articles:

  * [LC Phone System - Error Code and Warning Dictionary](<https://help.gohighlevel.com/en/support/solutions/articles/155000005526>)
  * [Understanding Common SMS Delivery Errors](<https://help.gohighlevel.com/en/support/solutions/articles/48001208912>)
  * [Error: The "From" Number Is Not SMS-Capable](<https://help.gohighlevel.com/en/support/solutions/articles/48001180919>)
  * [Best Practices for SMS Deliverability and Avoiding SMS Restrictions](<https://help.gohighlevel.com/en/support/solutions/articles/155000000079>)
  * [How to Prevent SMS Filtering by Carriers: Error 30007](<https://help.gohighlevel.com/en/support/solutions/articles/48001237726>)
  * [LC Phone Messaging Policy](<https://help.gohighlevel.com/en/support/solutions/articles/48001213941>)


6

## Frequently Asked Questions

Q: Where should I look up an SMS error code?

Open the failed message in Conversations and note the displayed code. LC Phone users should use the [LC Phone System - Error Code and Warning Dictionary](<https://help.gohighlevel.com/en/support/solutions/articles/155000005526>). Accounts connected to their own Twilio provider (BYOT) can also review the corresponding Twilio message log for additional context.

Q: The contact says they didn't receive my message, but no error shows. What should I do?

If the message shows as sent without a final delivery error, check the provider and carrier delivery status. Carrier filtering, handset availability, or delayed delivery can still affect the message after submission. Review message content and consent practices to reduce the likelihood of carrier filtering.

Q: What does it mean when a message is "filtered" by the carrier?

Carrier filtering occurs when the recipient's mobile carrier blocks the message due to suspected spam, prohibited content, or policy violations. Review the [How to Prevent SMS Filtering by Carriers: Error 30007](<https://help.gohighlevel.com/support/solutions/articles/48000982433>) article for mitigation strategies and best practices.

Q: How do I know if my A2P or Toll-Free registration is complete?

Check your phone number settings in HighLevel to confirm the number is associated with an approved A2P Campaign or Toll-Free verification record. If you see error codes 30032, 30033, or 30034, your registration may be incomplete or suspended. Review the Related Articles section for A2P and Toll-Free registration guidance.

Q: Can I retry a failed message immediately?

Yes, but only after resolving the root cause indicated by the error code. Retrying without fixing the issue may result in repeated failures, account restrictions, or further carrier filtering. Always apply the recommended resolution before retrying.

Q: What should I do if the error persists after troubleshooting?

If the issue continues after following the troubleshooting checklist and applying the recommended fixes, contact HighLevel Support with specific examples: the sending number, recipient number, timestamp, error code, and any relevant screenshots. This helps Support diagnose and resolve the issue efficiently.

Q: How do I avoid SMS delivery issues in the future?

Follow SMS best practices: obtain proper consent before messaging, avoid spam-like content, comply with carrier policies, ensure A2P or Toll-Free registration is complete, and monitor your account's daily send caps and ramp-up status. Review the [Best Practices for SMS Deliverability and Avoiding SMS Restrictions](<https://help.gohighlevel.com/support/solutions/articles/48000982474>) article for detailed guidance.

Q: What is the difference between LC Phone and BYOT (Bring Your Own Twilio)?

LC Phone is HighLevel's native phone system with integrated error reporting and the LC Phone Error Code Dictionary. BYOT accounts connect to their own Twilio account and use Twilio's message logs and error codes. The troubleshooting process is similar, but error code references and provider logs differ between the two systems.

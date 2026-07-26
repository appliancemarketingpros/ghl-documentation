# LC - Phone Messaging Policy

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001213941-lc-phone-messaging-policy](https://help.gohighlevel.com/support/solutions/articles/48001213941-lc-phone-messaging-policy)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Compliance

LC - Phone Messaging Policy

How sending limits, spam handling, and required consent language protect your SMS deliverability and reputation.

What You'll Learn

To protect agencies' SMS reputation and limit exposure, several safeguards have been implemented for LC - Phone. This messaging policy applies to all subaccounts using LC - Phone for communication within the CRM.

We want every message you send to reach its recipient unhindered by filtering or blockers. To make that possible, LC - Phone and its customers work together to prevent and eliminate unwanted messages — ensuring SMS is sent only to consenting parties and in line with applicable laws, industry standards, and guidelines.

Table of Contents

1

LC - Phone Messaging Policy & Violations

2

SMS Ramp-Up Model (V2)

3

Spam Message Handling

4

Opt-Out Language Addition

5

Sender Information Addition

6

Error and Opt-Out Rate Monitoring

7

Frequently Asked Questions

1

## LC - Phone Messaging Policy

All messaging transmitted via the platform — regardless of use case or phone number type (e.g., long code or toll-free) — needs to comply with Application-to-Person (A2P) messaging standards. All A2P messages originating from the system are subject to this policy, which covers rules and/or prohibitions regarding:

  * **Consent ("opt-in"):** Consent can't be bought, sold, or exchanged — for example, you can't obtain consent by purchasing a phone list from another party. SMS should only be sent to opted-in contacts.
  * **Revocation of Consent ("opt-out"):** The initial message sent to an individual must include language such as "Reply STOP to unsubscribe," so individuals can revoke consent at any time using a standard opt-out keyword.
  * **Sender Identification:** Every initial message must clearly identify the sender (the party that obtained the opt-in), except in follow-up messages of an ongoing conversation.
  * **Messaging Usage:** Messages must not relate to alcohol, firearms, gambling, tobacco, or other adult content.
  * **Filtering Evasion:** Content specifically designed to evade unwanted-messaging detection is not allowed. This includes intentionally misspelled words or non-standard opt-out phrases created to evade these mechanisms. Snowshoeing — spreading similar or identical messages across many phone numbers to evade detection — is not permitted.


This policy applies to all customers who use LC - Phone messaging services, in order to safeguard their messaging capabilities and services.

How We Handle Violations

When a violation is identified, we work with customers in good faith, where possible, to bring them back into compliance. However, to protect the ability of all customers to use messaging for legitimate purposes, we reserve the right to **suspend or remove platform access** for customers or end users who don't comply with this policy, or who don't follow applicable law or communications industry guidelines — in some cases with limited notice for serious violations.

What error screens will a subaccount see during a violation?

  * **Conversation Error:** "You have exceeded your SMS sending limit."
  * **Bulk Action:** "You are allowed to send 5000 message(s) in a day. You have already sent 5000 message(s). If you wish to proceed, 1 Message(s) will be failed."


![Conversation error screen showing SMS sending limit exceeded](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48222961915/original/2QKxVz00B7OVVQAHVK3y2npqoXsM7NyViA.png?1651581300)

![Bulk action error screen showing daily send limit reached](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48222962001/original/CJSFxDMFuf9RF8nd-vVYLdPc6GDRw2W76w.png?1651581314)

2

## SMS Ramp-Up Model (V2)

Starting February 1st, 2024, all subaccounts created under LC - Phone follow an 8-level ramp instead of the previous 7-day ramp with a lower limit. The table below details each level:

Level| SMS Sending Limit  
---|---  
1| 100  
2| 250  
3| 500  
4| 750  
5| 1500  
6| 2250  
7| 3000  
8| 3000+  
  
Note

This ramp does not start on the signup date — it starts on the day the first successful SMS message is sent.

How it works

  1. All subaccounts start at Level 1, enabling 100 SMS within 24 hours.
  2. To increase the sending limit, the subaccount must send the full level limit within a 24-hour window.
  3. After sending the full level limit within 24 hours, the subaccount is temporarily restricted from sending SMS for the next 24 hours. During this restriction, SMS sending is disabled.
  4. After 24 hours, the restriction lifts. The subaccount can send messages again and unlocks the next level's sending limit.


An example

  * A new subaccount starts on Level 1: 100 SMS within 24 hours.
  * To unlock Level 2, the subaccount must send 100 SMS within 24 hours.
  * After sending 100 SMS within 24 hours, the subaccount is restricted for 24 hours. Once that period ends, SMS sending resumes and Level 2's limit of 250 unlocks.
  * To unlock Level 3, the subaccount must send 250 SMS within 24 hours; after that, another 24-hour restriction applies before Level 3's limit of 500 unlocks.
  * This pattern of hitting the level's limit and waiting 24 hours continues until Level 8, which allows 3000+ SMS per day.


Why the change?

The ramp-up model was implemented to:

  1. Avoid SMS spam blasts from fake signups — new subaccounts follow the ramp-up model.
  2. Avoid getting subaccounts blocked due to suspicious activity.
  3. Avoid legal exposure from spamming non-consenting contacts. Only bulk SMS sending carries daily limitations, to prevent suspension from non-compliant messaging activity.


3

## Spam Message Handling

Every message sent from a subaccount ends up with one of four statuses:

  * **Sent:** No carrier response received yet — it can still resolve into any of the statuses below.
  * **Delivered:** Successfully delivered to the contact.
  * **Failed:** Canceled, or never forwarded to the carrier.
  * **Undelivered:** The message was flagged as suspicious or didn't fulfill the messaging policy.


Only Undelivered messages are considered here. Each one carries a specific error code, tracked at the message level, which is used to enable Temporary or Permanent DND (Do Not Disturb) at the contact level — so future SMS aren't sent to contacts who won't receive them, improving your deliverability rate. The table below summarizes the undelivered SMS error codes, what each means, and the remediation taken:

Response Code| Code Description| Remediation  
---|---|---  
30005| User Inactive / Number does not exist| Enable Temporary DND  
30003| Unreachable — Out of Service| Enable Temporary DND  
30004| Do not want SMS / DND enabled| Enable Permanent DND  
30006| Landline / incapable of receiving SMS| Enable Temporary DND  
30008| None of the above scenarios matched| Do nothing  
  
  * **Temporary DND:** DND set at the contact level can be revoked by the agency or location.
  * **Permanent DND:** DND cannot be revoked by the agency or location from the UI, because the contact is incapable of receiving messages or has opted out.
  * **Opt-Out Keyword:** Individuals must be able to revoke consent at any time by replying with a standard opt-out keyword like STOP or UNSUBSCRIBE. This also enables a permanent DND at the contact level.


Advantage

  * Restricts the location from sending SMS to non-relevant contacts, increasing deliverability and reducing the risk of being blocked.
  * Locations only send messages to contacts who have opted in.


Spam messaging error screens

  * **Conversation:** "Cannot send messages as DND is active for SMS."
  * **Bulk Action:** All SMS sent via workflow or bulk SMS automatically skips DND-marked contacts from the sender list.


![Conversation screen showing DND active for SMS](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053452149/original/MCPIyZBNxEMDLfROubCaT6EVYvv-erzHgQ.png?1757496520)

How to revoke the DND for a contact

  1. **For Temporary DND** — go to the contact's details and remove the DND flag. See the sample screen below.
  2. **For Permanent DND** — this cannot be revoked from the UI. Ask the contact to reply with "START," "YES," or "UNSTOP" to the number, which automatically removes the DND from the contact.


![Contact details screen with the DND flag removal option](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053452338/original/djBu37YNnY_M087ZaisF71IYZXVxBWlBRA.png?1757496591)

Note

If replying START doesn't revoke the DND and incoming/outgoing messages keep failing, please raise a support ticket.

4

## Opt-Out Language Addition

  * Consent for communications can't be bought — the only path is taking explicit consent from the user for SMS campaigns and communications.
  * Consent is taken by a specific entity — in this case, the subaccount that is the actual sender of these communications.
  * To comply with the messaging policy, every initial message sent to an end user must include two mandatory pieces of information: **Sender ID** and **Opt-Out Language**.
  * **Opt-Out Language:** The end user must be able to remove consent at any time, so each initial message includes opt-out keywords like STOP or UNSUBSCRIBE. The language "Reply STOP to unsubscribe" is added automatically.


Please Note

The Opt-Out Message setting applies when it's the **first** SMS sent to a new contact who has never texted your system number, across: (1) a Bulk Action in the Contacts area, (2) Workflow "Send SMS" actions, (3) Campaigns (legacy feature), and (4) One-on-One messages sent via the Conversations area.

![Sample message showing opt-out language appended to the first SMS](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053453499/original/QjJraDPQbBjkiFGdJqmioh3v3Rm-P-b_9w.png?1757497254)

How can I customize the opt-out message?

Go to **Sub-account → Settings → Phone Numbers → Advanced Settings → SMS Compliance** , where you can customize the opt-out message.

![SMS compliance settings screen for the opt-out message](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053453762/original/-GbEFXZQWEdvoFpHxolBlf7ptBnchqL_JA.png?1757497403)

![Opt-out message customization field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053454589/original/gDvz85IoJrfz0wAcKas2Ug3-vUZNGpyHXg.png?1757497788)

What happens if my message already has opt-out language?

The platform suppresses the auto-added opt-out line only when it detects a **full opt-out instruction** already in the message — for example, an unsubscribe phrase. It does not suppress insertion for incidental keywords used in ordinary sentences.

**Examples that suppress insertion:**

  * "Reply STOP to unsubscribe."
  * "Text STOP to opt out."
  * "Reply STOP to end."


**Example that does not suppress insertion:**

  * "If you want to stop by the office tomorrow, we're open 9–5."


What happens when an end user replies with the STOP keyword?

If an individual replies with a standard opt-out keyword like **STOP** , consent to send SMS is revoked. All upcoming and queued messages will fail, and a **permanent DND** is enabled at the contact level.

Important

This information is mandatory for end customers, so it's a required check on every initial message. The first outbound message in a conversation must include sender identification and opt-out language, regardless of other settings.

5

## Sender Information Addition

  * Consent for communications can't be bought — the only path is taking explicit consent from the user for SMS campaigns and communications.
  * Consent is taken by a specific entity — in this case, the location that is the actual sender of these communications.
  * To comply with the messaging policy, every initial message must include two mandatory pieces of information: **Sender ID** and **Opt-Out Language**.
  * **Sender ID:** Every message must clearly identify the sender (the party that obtained the opt-in), except in follow-up messages of an ongoing conversation. The sender info "Thanks, <Location Name>" is added automatically.


Please Note

The Sender ID feature applies to all Bulk Actions (bulk SMS), Workflows, Campaigns, and One-on-One conversations.

Sample message screen

![Sample SMS showing the auto-appended sender ID](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053454290/original/RFrhPHB8DSfzS3ESEC9vn0kEyBjZJM1YdA.png?1757497661)

How can I customize the Sender ID?

Go to **Sub-account → Settings → Phone Numbers → Advanced Settings → SMS Compliance** , where you can customize the Sender ID message.

![SMS compliance settings screen for the Sender ID message](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053454545/original/Zw_-iAF7hig8ZzQOpJgQXoU359UxdrUTmw.png?1757497773)

Please Note

This information is mandatory for end customers, so it's a required check on every initial message.

6

## Error and Opt-Out Rate Monitoring

We monitor messaging performance and take proactive measures to maintain healthy delivery rates — preventing carriers from blocking or permanently suspending accounts due to poor usage patterns. We monitor overall delivery performance for each account and apply corrective actions to keep delivery rates within acceptable limits.

Opt-Out and Bounce Rate Monitoring

The charts below outline the opt-out and bounce rate thresholds at which Warnings (W) and Suspensions (S) are triggered.

Locations Following Ramp-Up

Warnings/suspensions are based on the location's ramp level (L1, L2, etc.), the number of SMS messages sent, and the opt-out count or opt-out percentage.

![Opt-out rate warning and suspension thresholds by ramp level](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064877368/original/OvB291-hgT9EZ4nieVtbZ8Cr7uAKMnqPuQ.png?1770991583)

Locations Created Before Feb 4, 2024 (Following Messaging Limits)

Warning/suspension emails are triggered based on total SMS messages sent and the bounce count or bounce percentage.

![Bounce rate warning and suspension thresholds for pre-ramp locations](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064876943/original/BgSXd43w2xWGD_osl4Be55xDFmFG-J4zXQ.png?1770991257)

Error Rate Monitoring

The charts below outline the error rate thresholds at which Warnings (W) and Suspensions (S) are triggered.

Locations Following Ramp-Up

Based on ramp level, number of SMS messages sent, and error count or error percentage.

![Error rate warning and suspension thresholds by ramp level](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064877313/original/WtJjrAfPV7lqjNAVfjoY4jiMir6kuMccqg.png?1770991562)

Locations Created Before Feb 4, 2024 (Following Messaging Limits)

Based on total SMS messages sent and error count or error percentage.

![Error rate warning and suspension thresholds for pre-ramp locations](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064160668/original/Ex2774QQ4U7izMtOPXbkRmKzAnAdyHzWvA.png?1770200827)

Note

Locations created before **4th February 2024** did not follow the ramp-up process and were placed directly on messaging limits.

Important

Once an account enters **temporary suspension** , all outbound SMS will fail until **00:00 UTC** , when the suspension is automatically lifted.

What should we do when we get a violation email?

  1. Stop all workflows, campaigns, triggers, and/or bulk actions to contacts who have not explicitly opted in to receive messages from the subaccount.
  2. Enable and customize the Opt-Out Language and Sender ID message for your use case, so upcoming messages aren't flagged.
  3. Confirm with your client that no bulk communication, message blasts, or cold-prospecting campaigns will go out until you've replied to the ticket.


What are error and opt-out rates, and what's a good threshold?

  * A **high opt-out rate** indicates contacts have objected, complained, or marked your SMS as spam. A good opt-out rate is typically **0–1%**.
  * A **high delivery error rate** indicates you're sending SMS to contacts who are out of service, unreachable, or on a non-SMS-capable device such as a landline — or that carrier filters are refusing delivery due to prior sending behavior.


What do I do to get the subaccount suspension removed early?

The suspension lifts automatically within 24 hours. If the subaccount is permanently suspended, see the related article on account suspension to un-suspend it.

Note

One-on-one conversations, test SMS, resend message, and Missed Call Text Back are still allowed even while an account is suspended.

7

## Frequently Asked Questions

Q: Can I change or remove the Ramp-Up Model?

No. Previously agencies could adjust the SMS limit within or after the ramp period — that capability has been removed.

Q: Do one-to-one and Missed Call Text Back SMS count toward my daily limit?

Yes. These message types were previously excluded from the day's total, but they're now counted toward the limit.

Q: Can I send one-to-one messages during the 24-hour temporary restriction after hitting my level limit?

No. One-to-one messages used to be exempt from a temporary restriction — that exemption has been removed.

Q: I'd like to send more than 5000 SMS per day — how do I increase my limit?

Once your location hits the 8th-day mark (3000+ SMS per day), you can reach out to support and request a limit extension.

Q: What happens when we hit our daily limit — can we still respond if a lead replies?

No, you cannot respond manually to incoming messages once the limit is reached. Daily limits affect all messaging activity, including manual SMS in conversations, workflow automations, and bulk actions.

Q: How often does the SMS limit reset?

The limit refreshes every 24 hours. For a brand-new account, the limit increases each day according to the ramp table until day 8, when it caps at 3000+ per day.

Q: Can we undo the DND option in bulk?

No — this restriction exists specifically to prevent sending SMS in bulk again after DND has been enabled for those contacts.

Q: Does the auto-appended Sender ID and Opt-Out Language apply to every first text of a workflow or manual SMS?

Yes, whenever it's the first SMS to a new contact who has never texted your system number, across: a Bulk Action in the Contacts area, Workflow "Send SMS" actions, Campaigns (legacy feature), and One-on-One messages sent via the Conversations area.

Related Articles

[What is LC - Phone System?](<https://help.gohighlevel.com/en/support/solutions/articles/48001223546>) [How to Migrate an Agency and Sub-Account to LC - Phone?](<https://help.gohighlevel.com/en/support/solutions/articles/48001204027>) [Regulatory Bundle and Address Creation for Sub-Accounts](<https://help.gohighlevel.com/en/support/solutions/articles/48001213216>) [Toll-Free Number Registration for LC - Phone (US/Canada)](<https://help.gohighlevel.com/en/support/solutions/articles/48001222300>)

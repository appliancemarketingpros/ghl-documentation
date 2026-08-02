# Best Practices for SMS deliverability and Avoiding SMS Restrictions

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000000079-best-practices-for-sms-deliverability-and-avoiding-sms-restrictions](https://help.gohighlevel.com/support/solutions/articles/155000000079-best-practices-for-sms-deliverability-and-avoiding-sms-restrictions)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Deliverability

SMS Deliverability Best Practices

How to keep your error and opt-out rates in check, respond to violation emails, and prevent carrier-driven SMS suspensions.

Overview

This article outlines essential best practices to help you improve SMS deliverability and avoid carrier restrictions. By following these guidelines, you can ensure your messages reach your audience reliably and stay compliant with carrier policies.

Table of Contents

1

Error and Opt-out Rate Monitoring

2

What should we do when we get a violation email?

3

What are error and opt-out rates, and a good threshold?

4

How do I get the sub-account suspension removed early?

5

How to prevent future SMS suspension

6

Frequently Asked Questions

1

## Error and Opt-out Rate Monitoring

We are focused on helping our customers deliver trusted communications, and on making sure that the carrier does not block or suspend the account permanently based on bad usage.

We monitor the delivery rate of the overall account and take proactive measures to keep the delivery rate in check:

Please refer to [this](<https://help.gohighlevel.com/support/solutions/articles/48001213941-lc-phone-messaging-policy#section-6>) article for the thresholds at which **violation warning emails** are sent based on error rate and opt-out rate, as well as the thresholds at which **temporary messaging restrictions** are automatically applied.

Please Note

As soon as the account hits the temporary suspension, all upcoming outbound SMS will fail until 00:00 AM UTC.

2

## What should we do when we get a violation email?

  1. Stop all your workflows, campaigns, triggers, and/or bulk actions to contacts who have not explicitly opted in to receive messages from the sub-account.
  2. Enable and customize the Opt-Out language and Sender ID message as per your use case so that all upcoming messages are not flagged.
  3. Discuss this with your client to ensure that no bulk communication, message blasts, or cold prospecting campaigns are sent in the near future before we receive your reply to the ticket.


3

## What are error and opt-out rates, and a good threshold?

Opt-Out Rate

A high opt-out rate indicates that **contacts receiving your messages have objected, generated complaints, or marked your SMS as spam**. A good opt-out rate is typically in the range of **0–1%**. 

Delivery Error Rate

A high delivery error rate indicates that you are **sending SMS to contacts that are no longer in service, are unreachable, or use a non-SMS-capable device such as a landline**. This may also mean external carrier filters are refusing to deliver your SMS due to bad sending behavior in the past. A good error rate is typically in the range of **0–6%**. 

4

## How do I get the sub-account suspension removed early?

The sub-account suspension will be lifted in 24 hours. However, if the sub-account is **permanently suspended** , please refer to the article [Why is your account suspended](<https://help.gohighlevel.com/en/support/solutions/articles/48001207676>) to unsuspend the sub-account.

Prevention Guide

Eight ways to protect your delivery rate

Follow these practices to reduce your error rate and keep your SMS from being flagged.

5

## How to prevent future SMS suspension

The sub-account should be able to send SMS after 00:01 AM UTC the next day after you received the non-compliant email. Use the best practices below to reduce your error rate.

Step 1

Add Opt-Out language

Include opt-out language (**reply STOP / CANCEL to unsubscribe**) in the first SMS sent to every new contact.

![Opt-out language settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053555932/original/omypVzpD4ZIFIAoXgerZHkjna_VbAoHDZQ.png?1757587829)

Step 2

Add Sender information

Include an introduction of yourself or your company in the first SMS sent to every new contact.

Step 3

Do not message SMS-incapable devices

Avoid sending to landlines. **Enable Number Intelligence** — this feature looks up the number before sending and applies a temporary DND on the contact if it is not SMS-capable.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077257625/original/dGwqqQwxjlGMNWh04d_qRDQ0PiUEqxrAog.png?1785421473)

Step 4

Avoid public URL shorteners

Using public URL shorteners like bit.ly or tinyurl.com can harm SMS deliverability. Carriers — especially T-Mobile and AT&T — flag these as high risk due to their association with spam and phishing.

Carrier Restrictions

**T-Mobile** prohibits URL cycling and multiple redirects. Messages using such tactics may be blocked.

**AT &T** outright blocks public shorteners.

Best Practices

  * Use **custom** or **branded** short URLs linked to your business domain.
  * Limit redirects to **no more than one** , and avoid cloaking link destinations.
  * When possible, include the **full URL** to boost transparency (even if it takes extra characters).


Improving your URL practices can prevent filtering and ensure your messages reach their audience.

Step 5

Register your Business Profile, A2P Brand, and campaign

The messaging world is moving toward a state where, without these registrations, no messages will be delivered. You can view the Trust Center tab once the sub-account country is set to US.

[Trust Center Support Doc](<https://help.gohighlevel.com/support/solutions/articles/48001225526-lc-phone-system-trust-center>) [A2P Campaign Registration Best Practices](<https://help.gohighlevel.com/support/solutions/articles/48001229784-a2p-10dlc-campaign-approval-best-prac>)

Non-US Accounts

If the country is not set to US, you can still use the system by following these best practices so the delivery rate stays high and the SMS is not flagged. A2P campaign registration is an enhanced safety net for delivery, but it doesn't mean you cannot use the system without it.

Note

Campaign verification can take up to 1 week. If it is not approved after a week, please raise a support ticket so we can escalate the request to TCR.

Step 6

Capture consent on web form opt-ins

For future web form opt-in setups, include a checkbox so the lead gives consent when filling out the form (if that's where your leads opt in).

Below are examples of the web form opt-in flow.

When the **Phone Number** field is **Mandatory** in the web form opt-in:

  * Consent checkboxes should be separated for both Marketing and Non-Marketing messages.
  * Consent **checkboxes cannot be pre-selected** and **should be optional at all times**.
  * **Privacy Policy** and **Terms & Conditions** at the footer.


![Web form opt-in with mandatory phone number](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062250747/original/pVWeK4yDfAHpD4YrPxpNU_mtq4uCO-_baw.jpeg?1767888777)

When the **Phone Number** field is **not Mandatory** in the web form opt-in:

  * A consent checkbox is not required when the Phone Number field is not mandatory.
  * **Privacy Policy** and **Terms & Conditions** at the footer.


![Web form opt-in without mandatory phone number](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053553965/original/1jHn9-YOPznYisf4_S9772eWc4kkWtdzgw.png?1757586746)

Step 7 · Good to Have

Reference the opt-in source in the first message

The first message should state the source of how your leads opted in.

![First message referencing opt-in source](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155000318313/original/CdbUV4IqS1HJ_BfgCsqAOrDLVhYquft4Yw.png?1685694447)

Step 8 · Good to Have

Use double opt-in language

Add opt-in language so contacts are actively double opted-in via SMS and the web form checkbox (e.g., **reply 1 to subscribe**).

Also, review our [Messaging Policy](<https://help.gohighlevel.com/support/solutions/articles/48001213941>) for further guidance.

6

## Frequently Asked Questions

Q: How long does a temporary suspension last?

A temporary suspension lasts 24 hours. Outbound SMS will resume after 00:01 AM UTC the day after you received the non-compliant email.

Q: What error and opt-out rates trigger a suspension?

Please refer to [this](<https://help.gohighlevel.com/support/solutions/articles/48001213941-lc-phone-messaging-policy#section-6>) article.

Q: Can I get a suspension lifted early?

Temporary suspensions automatically lift after 24 hours. If your sub-account is permanently suspended, follow the steps in the "Why is your account suspended" article to request reinstatement.

Q: Do I need A2P registration if my account isn't US-based?

No. A2P registration is only available when the sub-account country is set to US. Non-US accounts can still send SMS by following these best practices to keep the delivery rate high and avoid being flagged.

Q: Why are my messages with shortened URLs failing?

Public URL shorteners like bit.ly and tinyurl.com are flagged as high risk by carriers. T-Mobile blocks URL cycling and multiple redirects, and AT&T blocks public shorteners outright. Use custom or branded short URLs on your own domain instead.

Q: How do I avoid sending to landlines?

Enable Number Intelligence. It looks up each number before sending and applies a temporary DND to contacts that aren't SMS-capable, protecting your error rate.

Q: How long does campaign verification take?

Campaign verification can take up to 1 week. If it isn't approved after a week, raise a support ticket so the request can be escalated to TCR.

Related Articles

[Understanding the Potential Delivery Issues of Text Messages with Shortened URLs](<https://help.gohighlevel.com/support/solutions/articles/48001240115-understanding-the-potential-delivery-issues-of-text-messages-with-shortened-urls>) [Messaging Policy](<https://help.gohighlevel.com/support/solutions/articles/48001213941>)

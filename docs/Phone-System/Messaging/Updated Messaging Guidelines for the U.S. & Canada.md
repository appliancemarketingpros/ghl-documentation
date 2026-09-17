# Updated Messaging Guidelines for the U.S. & Canada

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006960-updated-messaging-guidelines-for-the-u-s-canada](https://help.gohighlevel.com/support/solutions/articles/155000006960-updated-messaging-guidelines-for-the-u-s-canada)  
**Category:** Phone System  
**Folder:** Messaging

---

Messaging Compliance

A2P & Persona Messaging Requirements- US/Canada

We've simplified A2P requirements across the US and Canada to make messaging more consistent, reliable, and compliant.

Overview

This guide explains the messaging requirements and error codes related to **A2P (Application-to-Person)** registration and **Persona verification** for both domestic and international routes. Understanding these rules helps ensure that messages are delivered successfully and that compliance issues are avoided.

Table of Contents

1

Domestic Messaging (Within the US and Canada)

2

International Messaging (US or Canada to Other Countries)

3

Exception: Messaging to the United Kingdom (UK)

4

Key Takeaways

5

Frequently Asked Questions

1

## Domestic Messaging (Within the US and Canada)

When sending messages within the United States, Canada, or Puerto Rico, **A2P (Application-to-Person) registration is mandatory**.

What This Means

Any messages sent between domestic numbers — such as **US → US** , **US → CA** , or **CA → US/PR** — must originate from a registered A2P number. This requirement ensures compliance with carrier regulations aimed at preventing spam and unauthorized messaging.

**If A2P registration is missing** , messages sent without A2P registration will fail and return the following error:

Error 30034

Number not A2P compliant. Please register for A2P.

Example Scenarios

  * A message from a U.S. business number to a U.S. customer → **A2P required**
  * A message from a U.S. number to a Canadian number (or vice versa) → **A2P required**


### Rule for CA → CA Messaging

Numbers Purchased Before March 26, 2025

  * **A2P registration not required**
  * Messaging continues as usual


Numbers Purchased On or After March 26, 2025

  * Messages can be sent **with or without A2P registration**
  * If A2P registration is not completed, you only need to complete Persona verification


In Summary

All domestic messaging routes require an approved A2P registration for proper delivery — **except for CA → CA** , where older numbers are exempt and new numbers require either A2P registration or Persona verification.

2

## International Messaging (US or Canada to Other Countries)

For messages sent from the **US or Canada** to international destinations, A2P registration is **not required**. Just Persona verification is needed for these messages to be delivered successfully.

What This Means

International messaging relies on the sender's verified identity rather than A2P registration. Persona verification confirms that the sender's details have been authenticated and approved.

Message Behavior

  * If the sender's persona is verified, the message will be delivered normally. A2P verification would not be required in this case.
  * However, if there is **no A2P registration** and **no persona verification** , the system will block the message and return an error.


Error 1002

Message blocked. A2P or persona verification needed.

### Getting Error 1002? Here's How to Fix It

If Persona verification was not triggered at the time of purchasing your phone number, you can manually trigger it by following these steps:

Step 1

Go to **AI Agents**.

Step 2

Select **Voice AI**.

Step 3

Click **Enable Outbound Calls**.

Step 4

Enable the checkbox for **Persona** to trigger verification.

You're All Set

Once Persona verification is approved, messaging will resume normally.

Example Scenarios

  * Sending from a US number to a customer in France → **Allowed** (just Persona verification required)
  * Sending from a Canadian number to a customer in Australia → **Allowed** (just Persona verification required)
  * Sending without Persona verification → **Blocked** with Error 1002


Essentially, **international messages from US/CA numbers only require Persona verification, not A2P**.

3

## Exception: Messaging to the United Kingdom (UK)

The **UK** is a special case in international routing rules.

  * **Messages from the US to the UK** are **not allowed** and will fail automatically.
  * **UK-to-UK** messaging is permitted.


Error 21612

Message cannot be sent with the current combination of "To" and/or "From" parameters.

4

## Key Takeaways

Route| Requirement  
---|---  
Domestic (US / CA / PR)| Always requires A2P registration.  
International (US / CA → Other Countries)| Requires Persona verification only.  
No A2P or Persona| Results in blocked messages with Error 1002.  
US → UK| Not supported; Error 21612 returned.  
  
5

## Frequently Asked Questions

Q: What is the difference between A2P registration and Persona verification?

A2P registration approves an application-to-person messaging campaign with carriers and is required for domestic (US/CA/PR) messaging. Persona verification authenticates the sender's identity and is what unlocks international messaging from US/CA numbers.

Q: I'm seeing Error 30034. What should I do?

Error 30034 means your number is not A2P compliant. Complete A2P registration for that number before sending domestic messages, and delivery will resume once registration is approved.

Q: How do I trigger Persona verification if it wasn't done at purchase?

Go to **AI Agents → Voice AI** , click **Enable Outbound Calls** , then enable the **Persona** checkbox to trigger verification. Once approved, messaging resumes normally.

Q: Do I need A2P registration to message international customers?

No. International messages sent from US or Canada numbers only require Persona verification, not A2P registration. As long as your persona is verified, messages are delivered normally.

Q: Why can't I send messages from a US number to the UK?

US-to-UK messaging is not supported and fails automatically with Error 21612. Only UK-to-UK messaging is permitted for this route.

Q: Are Canadian numbers exempt from A2P registration?

Only for CA → CA messaging, and only for numbers purchased before March 26, 2025. Numbers purchased on or after that date can send with A2P registration or, if A2P is not completed, with Persona verification.

Q: What happens if a number has neither A2P registration nor Persona verification?

The message is blocked and the system returns Error 1002. Complete either A2P registration (for domestic routes) or Persona verification (for international routes) to restore delivery.

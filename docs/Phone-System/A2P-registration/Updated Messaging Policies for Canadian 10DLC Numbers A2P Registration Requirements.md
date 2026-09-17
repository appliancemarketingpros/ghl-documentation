# Updated Messaging Policies for Canadian 10DLC Numbers: A2P Registration Requirements

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004915-updated-messaging-policies-for-canadian-10dlc-numbers-a2p-registration-requirements](https://help.gohighlevel.com/support/solutions/articles/155000004915-updated-messaging-policies-for-canadian-10dlc-numbers-a2p-registration-requirements)  
**Category:** Phone System  
**Folder:** A2P registration

---

SMS Compliance

Updated Messaging Policies for Canadian 10DLC Numbers: A2P Registration Requirements

Learn when Canadian 10DLC numbers require A2P Brand & Campaign registration, when Persona verification can be used instead, and what to check before sending SMS or MMS to Canada or the United States.

Overview

Canadian 10DLC messaging requirements depend primarily on **where the message is being sent** and, for Canada-to-Canada traffic, **when the Canadian number was purchased**. Messages sent from a Canadian 10DLC number to U.S. recipients require approved A2P 10DLC registration, while qualifying Canada-only traffic may use Persona verification instead.

Use this guide to determine which registration path applies before sending messages and to understand what changes if your messaging route expands later.

These rules apply specifically to **Canadian 10-digit long code numbers**. Toll-free numbers use a separate Toll-Free Verification process.

Important

**Persona verification does not replace A2P registration when a Canadian 10DLC number sends messages to U.S. recipients.** Persona is an alternative only for qualifying Canada-to-Canada messaging from Canadian numbers purchased on or after March 26, 2025.

Table of Contents

What is Canadian 10DLC A2P Registration? Key Benefits of Understanding Canadian 10DLC Requirements Canadian 10DLC Registration Decision Table A2P Registration vs. Persona Verification Rules by Messaging Route How to Set Up Canadian 10DLC Messaging Compliance Troubleshooting Canadian 10DLC Messaging Frequently Asked Questions Related Articles

# **What is Canadian 10DLC A2P Registration?**  
  


A2P 10DLC registration identifies the business sending application-to-person messages and the messaging use case associated with those messages. For Canadian long-code numbers, whether A2P is required depends on the destination of the message and, for Canada-only traffic, the date the number was purchased.

A complete A2P setup includes an approved **Brand** , an approved **Campaign** , and the applicable sending phone number being associated with that Campaign. Persona verification is a separate identity-verification process and can be used instead of A2P only for specific Canadian messaging routes described below.

**Toll-free numbers:** Toll-free numbers do not use A2P 10DLC registration. They must follow the separate Toll-Free Verification process before eligible SMS/MMS traffic can be sent.

## **Key Benefits of Understanding Canadian 10DLC Requirements**  
  


Choosing the correct verification path before sending messages helps prevent avoidable delivery failures and ensures your registration matches the destination and use case you actually intend to use.

  * **Route Clarity:** Know immediately whether CA → CA or CA → US traffic requires A2P, Persona, or no additional A2P registration.
  * **Fewer Delivery Blocks:** Avoid sending from a Canadian number before the required verification path is complete.
  * **Correct Registration Path:** Avoid using Persona where an approved A2P Brand and Campaign are required.
  * **Easier Expansion:** Understand what must change if a Canada-only messaging program later begins messaging U.S. recipients.
  * **Faster Troubleshooting:** Distinguish registration issues, Campaign-linking issues, and unrelated carrier or content filtering.


## **Canadian 10DLC Registration Decision Table**  
  


The fastest way to determine the correct compliance path is to identify the message destination first, then check the number purchase date only when the traffic remains entirely within Canada.

Messaging Route| Number Purchase Date| Requirement| What to Do  
---|---|---|---  
**Canada → United States**|  Any purchase date| **A2P required**|  Complete Brand and Campaign registration, receive approval, and associate the sending number with the approved Campaign.  
**Canada → Canada**|  Before March 26, 2025| **A2P not required for this route**|  Continue Canada-only messaging while following all applicable consent, content, and carrier requirements.  
**Canada → Canada**|  On or after March 26, 2025| **A2P or Persona**|  Complete A2P registration or complete Persona identity verification if you choose not to register for A2P.  
**Toll-Free Messaging**|  Not applicable| **Separate Toll-Free Verification**|  Follow the Toll-Free Verification workflow instead of A2P 10DLC registration.  
  
## **A2P Registration vs. Persona Verification**  
  


A2P and Persona solve different compliance needs. A2P registers the sender and messaging use case with the carrier ecosystem, while Persona verifies the identity associated with the sub-account. Treating them as interchangeable outside the qualifying CA → CA scenario can cause messaging failures.

Verification| Purpose| Where It Works in This Guide  
---|---|---  
**A2P Brand & Campaign**| Registers the sender identity and messaging use case with the A2P 10DLC ecosystem.| Required for CA → US. Also valid for CA → CA.  
**Persona**|  Verifies the identity associated with the sub-account.| Alternative to A2P only for CA → CA when the Canadian number was purchased on or after March 26, 2025.  
  
**Already Persona verified?** Persona is generally completed once per sub-account. If the sub-account has already successfully completed Persona, you typically will not be asked to repeat the identity-verification process for future supported compliance actions.

## **Rules by Messaging Route**  
  


The recipient's destination is the first decision point. A Canadian number that works without A2P for Canada-only messaging may require a completely different compliance path as soon as U.S. recipients are added.

Canada → United States

**A2P registration is required** when a Canadian 10DLC number sends SMS or MMS to U.S. recipients. This applies regardless of when the Canadian number was purchased.

Do not rely on Persona alone for this route. Complete the applicable Brand and Campaign registration and confirm the sending number is associated with the approved Campaign before sending.

Canada → Canada: Number Purchased Before March 26, 2025

A2P registration is **not required** for Canada-only messaging from qualifying Canadian 10DLC numbers purchased before March 26, 2025.

This exemption applies to the A2P registration requirement only. Consent, prohibited-content, carrier-filtering, opt-out, and other messaging requirements still apply.

Canada → Canada: Number Purchased On or After March 26, 2025

Canada-only messaging can proceed using either:

  1. **A2P Brand & Campaign registration**, or
  2. **Persona identity verification** if you choose not to complete A2P.


If the messaging program later expands to U.S. recipients, the Persona-only path is no longer sufficient and A2P registration becomes required.

## **How to Set Up Canadian 10DLC Messaging Compliance**  
  


Complete only the verification path that matches your sending route. Correct setup before messaging helps prevent registration-related failures and avoids unnecessary rework if the same number will later be used for U.S. traffic.

Step 1

Identify Your Messaging Route

Determine whether the Canadian 10DLC number will send messages only to Canadian recipients or whether any messages will be sent to U.S. recipients.

Step 2

Check the Number Purchase Date for Canada-Only Messaging

If the route is CA → CA, determine whether the number was purchased **before March 26, 2025** or **on/after March 26, 2025**. If you cannot confirm the original purchase date, contact Support with the phone number and Location ID before selecting a compliance path.

Step 3

Complete A2P Registration When Required or Selected

  1. Go to **Settings → Phone System → Trust Center**.
  2. Under **A2P Messaging (SMS)** , start or open your registration.
  3. Complete the appropriate **Brand registration**.
  4. After the Brand is eligible, complete the required **Campaign registration** , including messaging use case, sample messages, and consent details.
  5. Wait until the required Brand and Campaign reviews are approved.
  6. Confirm the Canadian sending number is associated with the approved Campaign before sending A2P traffic.


**Canadian Standard Brands:** When a Canadian registered business uses a Standard Brand, use the accepted Canadian **BN-9** format—the first nine numeric digits of the Business Number. Enter the legal business information exactly as it appears in official records.

For the detailed workflows, see [Registering Your A2P Brand](<https://help.gohighlevel.com/en/support/solutions/articles/155000008140>) and [A2P Campaign Registration: Step by Step Guide and FAQs](<https://help.gohighlevel.com/en/support/solutions/articles/155000004539>).

Step 4

Complete Persona When Using the CA → CA Alternative

If the Canadian number was purchased on or after March 26, 2025, will message only Canadian recipients, and you choose not to register for A2P, complete Persona identity verification when prompted.

Persona is generally a one-time verification per sub-account. For details, see [Identity Verification for Phone Number Purchases](<https://help.gohighlevel.com/support/solutions/articles/155000005798-identity-verification-for-phone-number-purchases-us-ca-pr-il->).

Step 5

Test Messaging and Monitor the Registration Status

After the applicable verification is complete, test with a legitimate opted-in recipient on the intended route. If a message fails, review the displayed error and confirm the number's registration and Campaign association before changing message content or routing.

## **Troubleshooting Canadian 10DLC Messaging**  
  


A failed message does not always mean the Canadian-number policy itself is wrong. Check the route, verification path, number-to-Campaign association, and message compliance separately to identify the actual cause.

Issue| What to Check  
---|---  
**CA → US message fails with Error 30034**|  Confirm the Brand and Campaign are approved and that the sending number is associated with the approved Campaign. Newly approved registrations may also require time to propagate across carriers.  
**Newer CA → CA number cannot send**|  Confirm that either A2P registration or Persona verification has been successfully completed.  
**Older CA → CA number still has delivery failures**|  The pre-March 26, 2025 exemption removes the A2P requirement for that route only. Review recipient consent, opt-out status, carrier filtering, prohibited content, number status, and the specific delivery error.  
**Toll-free number cannot send**|  Do not troubleshoot it as a Canadian 10DLC A2P issue. Check the number's Toll-Free Verification status instead.  
**Messaging destination changed**|  Re-evaluate the compliance path. A Persona-only Canadian number must complete A2P before it begins messaging U.S. recipients.  
  
**A2P approval does not guarantee every message will be delivered.** Carrier filtering, prohibited content, recipient opt-outs, consent requirements, number configuration, and other messaging policies can still affect delivery.

## **Frequently Asked Questions**  
  


Q: Can Persona replace A2P when I message U.S. recipients from a Canadian number?

No. Canadian 10DLC numbers messaging U.S. recipients require A2P registration. Persona alone is not sufficient for CA → US messaging.

Q: My Canadian number was purchased before March 26, 2025. Can I send within Canada without A2P?

Yes, A2P registration is not required for qualifying CA → CA messaging from those numbers. Other consent, content, carrier, and platform requirements still apply.

Q: My Canadian number was purchased after March 26, 2025 and the sub-account already passed Persona. Do I need Persona again?

Persona is generally a one-time identity verification per sub-account. If it has already been successfully completed, you typically will not need to repeat it for the qualifying CA → CA path.

Q: What happens if I use Persona for CA → CA and later start messaging the United States?

Complete A2P Brand and Campaign registration and associate the sending number with the approved Campaign before beginning CA → US messaging.

Q: Does this policy apply to Canadian toll-free numbers?

No. Toll-free numbers do not use A2P 10DLC registration. They follow the separate Toll-Free Verification process.

Q: What about messages from a Canadian number to Puerto Rico?

Canadian-number messaging to Puerto Rico follows the broader domestic A2P requirements. Complete A2P registration rather than relying on the CA → CA Persona exception.

Q: Why am I seeing Error 30034 even though my A2P Campaign was approved?

The number may not yet be associated with the approved Campaign, or carrier registration may still be propagating. Confirm the Campaign association first before resending.

Q: Does A2P approval guarantee that my Canadian messages will always be delivered?

No. Registration satisfies the applicable sender-registration requirement, but carriers can still filter or reject messages based on content, consent, recipient status, prohibited use cases, routing, or other carrier rules.

### **Related Articles**  
  


[ What is A2P 10DLC Brand and Campaign Registration? ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002380>) [ Registering Your A2P Brand ](<https://help.gohighlevel.com/en/support/solutions/articles/155000008140>) [ A2P Campaign Registration: Step by Step Guide and FAQs ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004539>) [ Identity Verification for Phone Number Purchases ](<https://help.gohighlevel.com/support/solutions/articles/155000005798-identity-verification-for-phone-number-purchases-us-ca-pr-il->) [ Error 30034: How to Link a Phone Number to an Approved A2P Campaign ](<https://help.gohighlevel.com/support/solutions/articles/155000008316-how-to-link-a-phone-number-to-an-approved-a2p-campaign>) [ Toll-Free Number Verification Guide for LC Phone (US/Canada) ](<https://help.gohighlevel.com/support/solutions/articles/48001222300-toll-free-number-verification-guide-for-lc-phone-us-canada->)

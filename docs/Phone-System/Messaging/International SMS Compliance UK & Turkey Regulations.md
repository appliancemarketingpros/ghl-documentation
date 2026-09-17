# International SMS Compliance: UK & Turkey Regulations

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001240411-international-sms-compliance-uk-turkey-regulations](https://help.gohighlevel.com/support/solutions/articles/48001240411-international-sms-compliance-uk-turkey-regulations)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Compliance

International SMS Compliance: UK & Turkey Regulations

Understand the current sender, registration, and message-content requirements that affect SMS delivery to recipients in the United Kingdom and Turkey.

Overview

International SMS delivery depends on the rules established by the destination country's regulators and mobile carriers. The United Kingdom requires compliant sender types and regulatory approval for UK long codes, while Turkey blocks international A2P SMS containing URLs as of April 1, 2026.

This guide explains the requirements that affect LC Phone and connected Twilio accounts, the actions needed to remain compliant, and the error codes you may see when a message is blocked.

Table of Contents

What is International SMS Compliance? Key Benefits of International SMS Compliance United Kingdom SMS Compliance How to Meet UK Registration Requirements Turkey SMS Compliance How to Prepare for UK and Turkey SMS Compliance Troubleshooting International SMS Delivery Frequently Asked Questions Related Articles

# **What is International SMS Compliance?**

International SMS compliance refers to the country-specific rules that determine which sender types, registrations, and message content can be used when sending Application-to-Person (A2P) messages. A sender that works for one destination may not be eligible for another because carriers and regulators apply different requirements by country.

For the United Kingdom, sender identity and UK long-code registration are central requirements. For Turkey, the primary international restriction covered here is the prohibition on URLs and links in international A2P SMS.

## **Key Benefits of International SMS Compliance**

Following destination-specific requirements helps reduce preventable message failures and makes it easier to identify whether a delivery problem is caused by sender eligibility, registration, message content, or carrier filtering.

  * **Improved Deliverability:** Use sender types and message formats accepted by the destination country's carriers.
  * **Reduced Message Failures:** Avoid unsupported routes, unregistered sender types, and prohibited content.
  * **Clearer Troubleshooting:** Recognize errors such as 21612 and 30007 and understand what they indicate.
  * **Regulatory Readiness:** Keep UK long-code KYC and Regulatory Compliance requirements up to date.
  * **Safer Automation:** Update workflows, campaigns, and templates before country-specific restrictions cause delivery failures.


## United Kingdom SMS Compliance

UK carriers restrict A2P messaging from unsupported international long codes and require UK long codes to be connected to approved Regulatory Compliance information. Choosing the correct sender type and completing the required verification are essential before relying on a UK number for business messaging.

### UK Enforcement Timeline

The UK requirements were introduced in stages. The dates below help distinguish the original international long-code restrictions from the later Regulatory Compliance requirements for UK long codes.

Date| Requirement  
---|---  
June 1, 2023| UK carriers began blocking international long-code A2P traffic.  
May 27, 2024| New UK long-code purchases require an approved Regulatory Compliance bundle.  
July 30, 2024| Full carrier enforcement for international long-code traffic was established across UK networks.  
September 30, 2024| All new and existing UK long codes must be connected to an approved UK Regulatory Compliance bundle.  
  
### **Supported UK Sender Options**

The appropriate sender depends on whether you need local two-way messaging, branded one-way messaging, or a higher-volume messaging solution.

  * **UK Long Code:** Requires applicable KYC information and an approved Regulatory Compliance bundle.
  * **Alphanumeric Sender ID:** Suitable for supported one-way branded messaging use cases.
  * **Short Code:** An option for supported higher-volume messaging use cases that require dedicated provisioning.


Important: US → UK Messaging

SMS sent from a US number to a UK recipient is not supported in the documented international routing flow and can fail with **Error 21612**. UK-to-UK messaging is the supported route for this scenario.

### **UK KYC and Regulatory Compliance Requirements**

UK long-code users must provide identity or business information appropriate to the number type. The exact information can vary based on whether the number is local, national, mobile, or toll-free and whether the registrant is an individual or business.

Common information can include the registrant's name, business name, registered address, business registration details, authorized representative information, contact information, and supporting verification documents when required.

## **How to Meet UK Registration Requirements**

The registration path depends on whether the number is managed through LC Phone or through your own connected Twilio account. Use the registration interface that corresponds to the phone provider configured for the location.

### **For LC Phone-Managed Numbers**

LC Phone-managed UK numbers use the Regulatory Bundle and Address tools available inside HighLevel. Complete the required KYC information and ensure the applicable approved bundle is associated with the UK number.

  1. Go to **Settings → Phone System**.
  2. Open **Regulatory Bundle / Address**.
  3. Create or open the applicable UK regulatory bundle.
  4. Enter the required KYC information and upload supporting documents when requested.
  5. Submit the bundle for review.
  6. Associate the approved bundle with the applicable UK long code.


![Regulatory Bundle and Address screen showing a UK regulatory bundle](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029451904/original/xP4YxYjNMymTeOQNKJgsXJuLA-uHhKt12w.png?1721283310)

Regulatory Bundle / Address is used to create and manage required UK regulatory information for LC Phone-managed numbers.

### **Purchasing a UK Number with LC Phone**

When purchasing a UK number, review the number's capabilities and address requirements before completing the purchase. Numbers that require regulatory information must be connected to an approved bundle as part of the compliant setup.

![UK phone numbers displayed in the phone number purchase screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029451969/original/OR2cXkGFFA1DFaUdmuJon6m9Or6z8ztUGQ.png?1721283395)

Review UK number type, capabilities, and regulatory requirements before completing the purchase.

### **For Connected Twilio Accounts**

If the location uses its own connected Twilio account, UK number purchasing and Regulatory Compliance bundle management are completed in Twilio rather than through the LC Phone registration interface.

  1. Open the Twilio Console.
  2. Create and submit the applicable UK Regulatory Compliance bundle.
  3. Provide the required KYC information and documentation.
  4. Purchase or configure an eligible UK sender.
  5. Monitor failed messaging traffic and update non-compliant routes as needed.


![Twilio Buy a Number screen filtered to United Kingdom SMS-capable numbers](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069209192/original/V7YNZpTLICw41XPFjxXXc-lgTGLEpIhIOA.png?1776257427)

Connected Twilio accounts manage UK number purchasing and regulatory requirements directly in Twilio.

## **Turkey SMS Compliance**

Effective April 1, 2026, Turkey's Information and Communication Technologies Authority (BTK) requires mobile operators to block international A2P SMS containing URLs. This restriction affects message content rather than only promotional traffic, so transactional and authentication messages must also be reviewed.

Effective April 1, 2026

International A2P SMS sent to Turkish recipients must not contain URLs, hyperlinks, shortened links, or tracking links.

### **Content That Must Be Removed**

Review every SMS template, workflow, campaign, and automated notification that can send to a Turkish recipient. Links inserted dynamically by a custom value should be treated the same as links written directly into the template.

  * Full website URLs
  * Public or branded shortened URLs
  * Tracking links
  * Hyperlinks or internet addresses
  * Dynamic fields that resolve to a URL


### **Messages Covered by the Rule**

The restriction is not limited to marketing messages. International A2P messages containing URLs can be blocked regardless of the business purpose of the message.

  * Order confirmations
  * Shipping updates
  * Appointment reminders
  * Transactional notifications
  * One-time passcodes (OTPs)


### **Error 30007 and Turkey**

Messages blocked by a Turkish carrier because of the URL restriction may return **Error 30007**. However, Error 30007 is a general carrier-filtering error and does not uniquely identify the Turkey URL rule.

The same error can occur when a carrier filters a message because of its content, sender identity, consent, or another compliance requirement. Always review the destination country, message body, sender, and applicable compliance rules before determining the cause.

### If You Have a Local Turkish Business Entity

Businesses formally registered in Turkey that must continue sending URL-containing SMS can use the local pathway currently documented for this requirement. This requires local business eligibility and additional provider configuration.

  1. Establish a direct contract with Posta Güvercini.
  2. Authorize Posta Güvercini as the service provider through the Turkish Message Management System (IYS).
  3. Contact HighLevel Support to complete the applicable technical setup and routing.


    
    
    **Good to Know:** If you do not have a qualifying local Turkish business entity, remove URLs from international SMS sent to Turkish recipients.

## **How to Prepare for UK and Turkey SMS Compliance**

A proactive compliance review helps identify unsupported senders and prohibited message content before customers experience delivery failures. Check both your phone-number configuration and every automation capable of sending internationally.

  1. **Identify the destination countries you message.**  
Confirm whether your workflows, campaigns, or users send SMS to UK or Turkish recipients.
  2. **Review the sender used for UK traffic.**  
Do not rely on an unsupported international long-code route. Use an eligible UK sender and complete the applicable registration.
  3. **Complete UK KYC and Regulatory Compliance requirements.**  
For LC Phone-managed numbers, manage the bundle through Phone System. For connected Twilio accounts, complete the applicable registration in Twilio.
  4. **Review US-to-UK messaging routes.**  
If messages originate from a US number and are sent to the UK, update the route because this combination is not supported and can return Error 21612.
  5. **Audit SMS content sent to Turkey.**  
Search workflows, campaigns, templates, custom values, and automated notifications for URLs, shortened links, or tracking links.
  6. **Replace links in Turkish SMS.**  
Use URL-free instructions, a phone number, or another communication channel when the recipient needs additional information.
  7. **Test and monitor delivery.**  
Send controlled test messages and review message errors so unsupported sender routes or carrier filtering can be identified quickly.


## **Troubleshooting International SMS Delivery**

International message failures should be investigated by checking the sender country, destination country, sender type, registration status, message content, and delivery error together. An error code alone may not identify every compliance issue.

Error 21612 when messaging the UK

Check the sender and recipient countries. US-to-UK SMS is not supported in the documented route and can return Error 21612. Use an eligible UK sender for UK messaging.

A UK long code is not sending

Confirm the number type is eligible and that the required UK KYC and Regulatory Compliance bundle has been approved and associated with the number.

Error 30007 when messaging Turkey

Review the message for URLs, shortened links, tracking links, or dynamic values that generate a URL. If no link is present, investigate other carrier-filtering causes because Error 30007 is not exclusive to Turkey's URL restriction.

Messages fail only in one country

Country-specific sender and content rules vary. A sender or template that works in another country can still be blocked by the destination country's carriers or regulator.

## **Frequently Asked Questions**

Q: Can I send SMS from a US phone number to a UK recipient?

US-to-UK SMS is not supported in the documented international route and can fail with Error 21612. Use an eligible UK sender for UK messaging.

Q: Do all UK long codes require Regulatory Compliance approval?

Yes. New and existing UK long codes covered by the UK requirements must be connected to an approved UK Regulatory Compliance bundle before they can be relied on for compliant service.

Q: Can I use a URL shortener in an SMS sent to Turkey?

No. Turkey's international A2P SMS restriction includes shortened URLs as well as full URLs, tracking links, and other internet addresses.

Q: Does Turkey's URL restriction apply to OTP and transactional messages?

Yes. International A2P SMS containing URLs can be blocked regardless of whether the message is promotional, transactional, or used for authentication.

Q: Does Error 30007 always mean Turkey blocked a URL?

No. Error 30007 indicates carrier filtering and can occur for multiple content, sender, or compliance reasons. For messages to Turkey, a URL is one important cause to check.

Q: Do the Turkey restrictions also block WhatsApp or email?

The regulation described in this article applies to international A2P SMS. Other communication channels have their own policies and requirements.

Q: Where should I register a UK number if I use my own Twilio account?

Connected Twilio accounts manage their UK Regulatory Compliance bundle and number setup directly in the Twilio Console. LC Phone-managed numbers use the Regulatory Bundle / Address tools available in HighLevel.

### **Related Articles**

[ Know Your Customer (KYC) in the United Kingdom ](<https://help.gohighlevel.com/support/solutions/articles/155000002831-know-your-customer-kyc-in-the-united-kingdom>) [ Updated Messaging Guidelines for the U.S. & Canada ](<https://help.gohighlevel.com/support/solutions/articles/155000006960-updated-messaging-guidelines-for-the-u-s-canada>) [ How to Prevent SMS Filtering by Carriers: Error 30007 ](<https://help.gohighlevel.com/support/solutions/articles/48001237726>) [ Configure SMS Compliance Settings ](<https://help.gohighlevel.com/support/solutions/articles/155000004684>) [ LC - Phone Messaging Policy ](<https://help.gohighlevel.com/support/solutions/articles/48001213941>)

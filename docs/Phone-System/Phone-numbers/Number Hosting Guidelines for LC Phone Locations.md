# Number Hosting Guidelines for LC Phone Locations

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001230556-number-hosting-guidelines-for-lc-phone-locations](https://help.gohighlevel.com/support/solutions/articles/48001230556-number-hosting-guidelines-for-lc-phone-locations)  
**Category:** Phone System  
**Folder:** Phone numbers

---

Hosted SMS & MMS

Number Hosting Guidelines for LC Phone Locations

Keep voice service with your existing carrier while enabling eligible phone numbers for SMS and MMS messaging through LC Phone.

Overview

**Number Hosting** , also called Hosted SMS or Hosted Messaging, lets eligible businesses use SMS/MMS in HighLevel with a phone number they already own through another carrier. The original carrier continues handling voice calls while messaging is routed through LC Phone.

Because ownership and voice service remain with the existing carrier, Number Hosting is different from porting or migrating a phone number. A verification and authorization process is required before hosted messaging can be activated.

This guide explains eligibility, required information, setup, messaging compliance, expected timelines, post-activation checks, and common hosting issues.

Important

Hosting approval does not replace messaging compliance. Applicable 10DLC numbers must meet A2P registration requirements, toll-free numbers used for SMS/MMS to US or Canadian recipients must complete Toll-Free Verification, and all messaging must follow consent, sender-identification, opt-out, and content requirements.

Table of Contents

What is Number Hosting (Hosted SMS / Hosted Messaging)? Key Benefits of Number Hosting Number Hosting vs. Porting Supported and Unsupported Number Types What You Need Before Requesting Number Hosting How Number Hosting Works How to Set Up Number Hosting Messaging Compliance for Hosted Numbers What Happens After Hosted Messaging Is Activated? Timeline Expectations Troubleshooting Number Hosting Frequently Asked Questions Related Articles

# **What is Number Hosting (Hosted SMS / Hosted Messaging)?**  
  


Number Hosting enables SMS/MMS messaging on an eligible phone number that remains owned and voice-enabled through another carrier. Instead of moving the phone number itself, hosted messaging changes only how supported text-message traffic is routed.

Your original carrier continues handling voice calls and ownership of the number. Once the hosting request is approved, supported SMS/MMS traffic is handled through LC Phone so the number can be used for messaging within HighLevel.

## **Key Benefits of Number Hosting**

  
Hosted messaging is useful when a business wants to preserve its current voice provider and established phone number while adding supported SMS/MMS capabilities inside HighLevel.

  * **Keep Your Existing Number:** Continue using the phone number customers already recognize.
  * **Keep Existing Voice Service:** Voice calling remains with the current carrier instead of being moved to LC Phone.
  * **No Number Port Required:** Hosting adds supported messaging without transferring ownership of the number.
  * **Use HighLevel Messaging:** Send and receive supported SMS/MMS through the HighLevel messaging experience after activation.
  * **Maintain Separate Voice and Messaging Providers:** Businesses can preserve an existing voice configuration while using LC Phone for messaging.


## **Number Hosting vs. Porting**  
  


Hosting and porting both let a business continue using an existing phone number, but they change different parts of the phone service. Choose hosting when voice should stay with the existing carrier; choose porting when the phone number itself needs to move to another carrier.

Feature| Number Hosting| Porting  
---|---|---  
**Number Ownership**|  Remains with the current carrier.| Transfers to the destination carrier.  
**Voice Service**|  Remains with the current carrier.| Moves with the number to the destination provider.  
**SMS/MMS**|  Hosted through LC Phone after approval.| Handled by the destination carrier after the port.  
**Carrier Transfer**|  No.| Yes.  
**Best Used When**|  You want to keep your existing carrier for voice but use HighLevel for messaging.| You want the destination provider to manage the entire phone number.  
  
**Need the entire number moved instead?** Use the [Porting Options: US In-App vs International Manual Process](<https://help.gohighlevel.com/support/solutions/articles/48001211919-porting-options-us-in-app-vs-international-manual-process>) guide.

## **Supported and Unsupported Number Types**  
  


Number Hosting is available only for supported numbers and provider configurations. Confirm eligibility before starting because unsupported number types cannot be activated through the hosted messaging workflow.

Number Type / Scenario| Eligible?| Guidance  
---|---|---  
**US/Canada Local Landline**| **Generally Yes**|  Most eligible landline numbers can use Hosted Messaging after verification and approval.  
**US/Canada Toll-Free Number**| **Generally Yes**|  Hosted messaging is generally supported, but Toll-Free Verification is required for SMS/MMS to US and Canadian recipients.  
**Number Without Existing SMS Service**| **Yes, if otherwise eligible**|  The number must meet all other hosting requirements.  
**Number Already Using SMS With Another Provider**| **No, as currently configured**|  Do not make changes to existing messaging service until Support confirms the appropriate next step.  
**Mobile / Cellular Number**| **No**|  Mobile numbers cannot be hosted through this workflow.  
**Twilio Voice Number in Another Twilio Account**| **No**|  A number already owned by a Twilio account for voice cannot be hosted for messaging on a different Twilio account.  
**Number Outside the US/Canada**| **No**|  Hosted SMS is currently limited to supported US and Canadian numbers.  
  
## **What You Need Before Requesting Number Hosting**  
  


Preparing the correct account and number information before contacting Support helps the hosting request move into verification without unnecessary follow-up.

  * **Location ID:** The HighLevel sub-account where Hosted Messaging should be activated.
  * **Phone Number(s):** Provide each requested number in E.164 format, such as **+1XXXXXXXXXX**.
  * **Number Owner Access:** The authorized owner or representative must be available to complete ownership verification and authorization.
  * **Current Carrier Information:** Be prepared to confirm the carrier or other ownership information if requested during verification.
  * **Messaging Compliance Information:** Prepare the business, consent, use-case, and opt-in information needed for A2P 10DLC or Toll-Free Verification when applicable.


## **How Number Hosting Works**  
  


Number Hosting uses an ownership-verification and authorization process to confirm that the requester has permission to route messaging for the phone number. Hosting is activated only after the required verification and carrier review are complete.

Stage| What Happens  
---|---  
**1\. Request**|  The Location ID and eligible phone number(s) are provided to HighLevel Support.  
**2\. Ownership Verification**|  The authorized number owner confirms control of the requested number(s).  
**3\. Letter of Authorization**|  The number owner signs the required LOA authorizing hosted messaging.  
**4\. Carrier Review**|  Twilio and applicable carrier systems review the hosting request and may require additional confirmation.  
**5\. Activation**|  Approved SMS/MMS routing is activated through LC Phone.  
**6\. Messaging Registration**|  Complete or confirm A2P 10DLC or Toll-Free Verification requirements before relying on hosted outbound messaging.  
  
![Number Hosting request screen showing hosted number entry and US messaging compliance requirements](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155061748220/original/pGXKSlb9E2FOtPnMKfcLnTf81bqbWSWOHQ.png?1767340421)

Hosted messaging requests require number verification, and applicable 10DLC and toll-free numbers must also meet US messaging registration requirements.

## **How to Set Up Number Hosting**  
  


A complete request requires the correct destination Location ID, eligible phone numbers, and action from the authorized number owner. Completing each verification step promptly helps prevent the request from remaining pending.

### **Step 1: Confirm the Phone Number Is Eligible**

Confirm that the number is a supported US or Canadian landline or toll-free number, is not a mobile number, and is not already using an incompatible messaging configuration.

### **Step 2: Find the HighLevel Location ID**

The Location ID identifies the sub-account where Hosted Messaging should be enabled. You can locate it in the sub-account URL while logged into HighLevel.

![HighLevel sub-account URL showing the Location ID](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080138957/original/FPHYKCKvebYgOrvoZwkabvrKNBVFH7lg6Q.png?1788538388)

The Location ID appears in the sub-account URL and uniquely identifies the destination sub-account.

### **Step 3: Prepare the Phone Number List**

Provide each number you want hosted in E.164 format. For example: **+15551234567**. If requesting multiple eligible numbers, clearly list each number so Support can associate them with the correct Location ID.

### **Step 4: Contact HighLevel Support**

Contact **HighLevel 24/7 Live Chat Support** and provide:

  * Destination Location ID
  * Phone number(s) to host
  * Any requested ownership or carrier details


### **Step 5: Complete Ownership Verification and the LOA**

HighLevel provides the Hosted Messaging verification process. The authorized number owner must complete ownership verification and sign the Letter of Authorization. Carrier confirmation may also be required.

### **Step 6: Wait for Approval and Activate Messaging**

After the request passes verification and review, hosted SMS/MMS routing is activated. Complete the applicable messaging registration and validation steps below before relying on the number for production messaging.

## **Messaging Compliance for Hosted Numbers**  
  


Number Hosting authorizes the routing of supported messaging traffic, but carrier registration and messaging-policy requirements still apply. Approval to host a number should not be treated as approval to send unrestricted SMS or MMS.

Requirement| What to Know  
---|---  
**A2P 10DLC**|  Applicable 10-digit local numbers used for US business messaging must be associated with the appropriate approved Brand and Campaign before messaging.  
**Toll-Free Verification**|  Toll-free numbers used to send SMS/MMS to US and Canadian recipients must be successfully verified before messaging.  
**Consent / Opt-In**|  Only message contacts who have provided valid consent for the applicable business and messaging use case.  
**Sender Identification**|  Initial outbound messaging must clearly identify the business sending the message.  
**Opt-Out Handling**|  Provide required opt-out language and honor opt-out requests such as STOP.  
**Content Rules**|  Hosted messaging remains subject to HighLevel messaging policies and carrier restrictions on prohibited or restricted content.  
  
**Do not begin production messaging solely because the hosting request shows approved.** Confirm the number's applicable messaging registration is also complete.

## **What Happens After Hosted Messaging Is Activated?**

After activation, voice and messaging continue using separate service paths. A short validation confirms that hosted SMS/MMS works in the correct sub-account while the existing carrier still handles voice calls normally.

  * **Confirm hosted messaging is active** in the intended HighLevel sub-account.
  * **Send an outbound test SMS** to a separate phone number.
  * **Reply to the test SMS** and confirm the inbound message appears in Conversations.
  * **Test MMS** when your number and messaging use case support it.
  * **Verify voice calling remains with the original carrier** by placing inbound and outbound voice tests through the existing voice configuration.
  * **Confirm A2P 10DLC or Toll-Free Verification status** when applicable.
  * **Review workflows and automations** that will use the hosted number before enabling production traffic.


## **Timeline Expectations**

Hosted Messaging requires external verification and carrier review, so activation is not immediate. Promptly completing ownership verification and authorization helps prevent avoidable delays.

Typical Approval Time: 3–10 Business Days

Many requests complete in approximately one week, but timing can vary based on ownership verification, carrier responsiveness, additional documentation, or further review requirements.

## **Troubleshooting Number Hosting**

Most hosting delays or messaging failures are caused by number eligibility, incomplete authorization, existing SMS service, or missing messaging registration. Identify the issue below before submitting another request.

The Number Is a Mobile / Cellular Number

Mobile numbers are not eligible for this Number Hosting workflow. Use another supported messaging or number-transfer option.

The Number Already Has SMS With Another Provider

A number with an existing SMS service is not eligible as-is. Contact Support before changing or disabling the existing messaging configuration so you can confirm the correct migration or hosting path.

The Hosting Request Is Still Pending

Confirm that ownership verification and the Letter of Authorization were completed. Additional carrier confirmation or verification can extend the normal review period.

Hosting Is Approved but SMS Is Not Sending

Confirm A2P 10DLC or Toll-Free Verification requirements are complete for the number and messaging route. Also review SMS compliance settings, contact consent, and any message error shown in Conversations or workflow execution details.

Inbound SMS Is Not Appearing in HighLevel

Confirm the hosting request is fully activated for the intended Location ID and test again from an unrelated phone number. If activation is complete and inbound messages still do not appear, contact HighLevel Support with the Location ID and affected number.

Voice Calling Changed Unexpectedly

Number Hosting is intended to change messaging routing only. If voice calling changes unexpectedly, verify the number's configuration with the original voice carrier and contact HighLevel Support if the issue began during hosting activation.

## **Frequently Asked Questions**

Q: Does Number Hosting transfer ownership of my phone number?

No. Your number remains owned and managed by the original carrier. Only supported SMS/MMS routing is hosted through LC Phone.

Q: Will my voice service move to HighLevel?

No. Voice service remains with your existing carrier. Number Hosting is specifically for supported messaging.

Q: Can I host a mobile or cellular phone number?

No. Mobile/cellular numbers are not supported by this Number Hosting workflow.

Q: Can I host a number that already has SMS enabled elsewhere?

Not in its current configuration. Contact HighLevel Support before changing the existing messaging service so the appropriate path can be confirmed.

Q: Can I request hosting for multiple numbers?

Yes. Multiple eligible numbers can be included in a hosting request. Clearly list each number and confirm that every number meets the hosting and messaging-registration requirements.

Q: Does hosting approval mean my number is ready to send SMS immediately?

Not necessarily. Confirm that all applicable A2P 10DLC or Toll-Free Verification requirements are approved before sending production messaging.

Q: How long does Number Hosting usually take?

Typical approval is approximately 3–10 business days. Carrier responsiveness, incomplete authorization, or additional verification can extend the timeline.

Q: Can numbers outside the US and Canada use Hosted Messaging?

No. The current Number Hosting workflow supports eligible numbers in the United States and Canada.

### **Related Articles**

[ A2P 10DLC Registration: Brand and Campaign Registration ](<https://help.gohighlevel.com/support/solutions/articles/155000002380>) [ Toll-Free Number Verification Guide for LC Phone (US/Canada) ](<https://help.gohighlevel.com/support/solutions/articles/48001222300-toll-free-verification-guide-for-lc-phone-us-canada->) [ Updated Messaging Guidelines for the U.S. & Canada ](<https://help.gohighlevel.com/support/solutions/articles/155000006960-updated-messaging-guidelines-for-the-u-s-canada>) [ LC Phone Messaging Policy ](<https://help.gohighlevel.com/support/solutions/articles/48001213941-isv-messaging-policy>) [ Configure SMS Compliance Settings ](<https://help.gohighlevel.com/support/solutions/articles/155000004684/>) [ Porting Options: US In-App vs International Manual Process ](<https://help.gohighlevel.com/support/solutions/articles/48001211919-porting-options-us-in-app-vs-international-manual-process>)

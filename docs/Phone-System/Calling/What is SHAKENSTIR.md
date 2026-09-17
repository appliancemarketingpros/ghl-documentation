# What is SHAKEN/STIR?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006429-what-is-shaken-stir-](https://help.gohighlevel.com/support/solutions/articles/155000006429-what-is-shaken-stir-)  
**Category:** Phone System  
**Folder:** Calling

---

SHAKEN/STIR is a caller authentication framework that helps carriers verify that a caller is authorized to use the phone number displayed on an outbound call. It uses digital certificates to authenticate caller ID information, helping reduce caller ID spoofing and establish trust with receiving carriers.

  


SHAKEN/STIR can improve caller trust and may help with call completion and answer rates, but it does not directly remove “Spam Likely” or other nuisance labels.

* * *

**TABLE OF CONTENTS**

    * What is SHAKEN/STIR?
    * Key Benefits of SHAKEN/STIR
    * SHAKEN/STIR, CNAM, and Voice Integrity
    * Requirements for SHAKEN/STIR Registration
    * How to Enable SHAKEN/STIR
      * Automatic Enrollment Through A2P Registration
      * Manual SHAKEN/STIR Registration
    * Important Notes
    * Frequently Asked Questions


* * *

## **What is SHAKEN/STIR?**

  


SHAKEN/STIR is a set of protocols used to authenticate caller ID information and help carriers determine whether an outbound caller is authorized to use the displayed phone number.

  


  * **STIR** stands for Secure Telephone Identity Revisited.  
  

  * **SHAKEN** stands for Signature-based Handling of Asserted information using toKENs.


  


When an outbound call is placed, SHAKEN/STIR uses digital certificates to authenticate the caller ID information. Receiving carriers can use this authentication information when evaluating the call.

Depending on the receiving carrier and device, authenticated calls may be more likely to receive a trusted or verified indication.

  


  


Shaken/STIR ensures that your number is what people see when their phone is ringing. It increases trustworthiness  
and helps avoid getting flagged as spam."

  


  


> **Important:** SHAKEN/STIR authenticates caller ID information. It does not guarantee that a call will display as “Trusted” or “Verified,” and it does not directly remove “Spam Likely” or other nuisance labels.

* * *

## **Key Benefits of SHAKEN/STIR**

  


SHAKEN/STIR helps establish the authenticity of legitimate outbound calls and provides the authentication foundation for additional caller-reputation tools.

  


  * **Authenticate Caller ID:** Helps carriers verify that your business is authorized to use the phone number displayed on an outbound call.  
  

  * **Reduce Caller ID Spoofing:** Makes it more difficult for unauthorized callers to impersonate your phone number.  
  

  * **Improve Carrier Trust:** Provides receiving carriers with authentication information that can help them evaluate legitimate calls.  
  

  * **Support Call Answer Rates:** Authenticated calls may be more likely to receive a trusted or verified indication, depending on the receiving carrier.  
  

  * **Enable Voice Integrity:** SHAKEN/STIR registration is required before eligible U.S. numbers can be submitted for Voice Integrity.


* * *

## **SHAKEN/STIR, CNAM, and Voice Integrity**

  


SHAKEN/STIR, CNAM, and Voice Integrity work together to improve caller authentication, identification, and reputation, but each serves a different purpose.

  


Feature| What It Does| Important Limitation  
---|---|---  
**SHAKEN/STIR**|  Authenticates caller ID information and helps carriers verify that the caller is authorized to use the phone number| Does not remove nuisance or spam labels  
**CNAM**|  Associates a U.S. phone number with a registered business or personal name| Name display is not guaranteed and does not remove spam labels  
**Voice Integrity**|  Registers eligible U.S. numbers with major caller-ID analytics providers for reputation review| Provider reviews happen separately, and label changes may take time  
  
Using these features together can help establish caller authenticity, provide caller-name identification, and improve phone-number reputation.

* * *

## **Requirements for SHAKEN/STIR Registration**

  


Before registering for SHAKEN/STIR through HighLevel, make sure your business meets the registration requirements.

A valid **Employer Identification Number (EIN)** is required for the documented SHAKEN/STIR registration process in HighLevel.

  


> **Note:** Businesses without an EIN do not qualify for the documented SHAKEN/STIR registration process. If you do not have an EIN and need to address reputation or spam-label issues for eligible U.S. phone numbers, review the **Free Caller Registry** as an alternative way to submit numbers for reputation consideration.

* * *

## **How to Enable SHAKEN/STIR**

  


Depending on your account setup, eligible phone numbers may be enrolled automatically through qualifying A2P registration, or you can configure SHAKEN/STIR through the HighLevel Trust Center.

  


### **Automatic Enrollment Through A2P Registration**

  


If you have completed a qualifying A2P SMS registration, eligible phone numbers may be enrolled in SHAKEN/STIR automatically.

  


You can review your SHAKEN/STIR registration status from the Trust Center.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080506419/original/xL2QPb5F1aGcJg4fw_IgqDelx1-soArajA.png?1788963143)

  


  


This applies to all new A2P applications submitted after **April 23, 2025** , and older sub-accounts are also being updated automatically.

  


> **Note:** Automatic enrollment depends on registration eligibility and account configuration. If SHAKEN/STIR is not configured for your account, use the manual registration option below.

  


  


### **Manual SHAKEN/STIR Registration**

  


If you have not been enrolled through A2P registration, you can configure SHAKEN/STIR manually from the Trust Center.

  


  1. Go to your HighLevel sub-account.  
  

  2. Navigate to **Settings → Phone Numbers → Trust Center**.  
  

  3. Locate the **SHAKEN/STIR** registration option.  
  

  4. Enter the requested business information.  
  

  5. Review your information for accuracy.  
  

  6. Submit the registration.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080506639/original/5lK9UeM0tTZbTfD8wm5KLozL7A-TWR_TVQ.png?1788963246)

  


  


Once your SHAKEN/STIR registration is configured, eligible numbers can use the authentication framework for outbound calls.

* * *

## **Important Notes**

  


Keep the following points in mind when using SHAKEN/STIR.

  


**1\. SHAKEN/STIR does not remove spam labels:** A phone number can be successfully authenticated and still display as “Spam Likely,” “Potential Spam,” or another nuisance label. Spam classifications can be influenced by call patterns, complaints, analytics-provider data, and previous phone-number activity.

  


  


**2\. Use Voice Integrity for reputation concerns:** If an eligible U.S. phone number is incorrectly receiving spam or nuisance labels, use Voice Integrity to submit the number to supported caller-ID analytics providers for reputation review.

  


  


**3\. CNAM performs a different function:** CNAM associates a business or personal name with a U.S. phone number. It does not replace SHAKEN/STIR authentication and does not guarantee that your registered name will appear on every recipient's device.

  


  


**4\. Caller display is controlled by receiving networks:** SHAKEN/STIR authentication does not guarantee that recipients will see a “Trusted,” “Verified,” or similar indicator. Display behavior depends on the receiving carrier and device.

  


  


**5\. SHAKEN/STIR is required for Voice Integrity:** Your business must have SHAKEN/STIR configured before eligible U.S. numbers can be submitted through HighLevel's Voice Integrity registration process.

* * *

## **Frequently Asked Questions**

  


**Q. Does SHAKEN/STIR remove “Spam Likely” labels?**

No. SHAKEN/STIR authenticates caller ID information but does not directly control phone-number reputation or remove nuisance labels. For eligible U.S. numbers experiencing reputation issues, use Voice Integrity for reputation review.

  


  


**Q. Do I need an EIN to register for SHAKEN/STIR?**

Yes. A valid Employer Identification Number (EIN) is required for the documented SHAKEN/STIR registration process in HighLevel.

  


  


**Q. What can I do if I don't have an EIN?**

Businesses without an EIN do not qualify for the documented SHAKEN/STIR registration process. If you are trying to address spam or reputation issues for an eligible U.S. number, review the Free Caller Registry as an alternative reputation-remediation option.

  


  


**Q. Is SHAKEN/STIR the same as CNAM?**

No. SHAKEN/STIR authenticates caller ID information and helps carriers verify that the caller is authorized to use a number. CNAM associates a business or personal name with a U.S. phone number.

  


  


**Q. Do I need SHAKEN/STIR before registering for Voice Integrity?**

Yes. SHAKEN/STIR must be configured before you can submit eligible U.S. phone numbers for Voice Integrity registration.

  


  


**Q. Does SHAKEN/STIR guarantee that my calls will show as “Trusted” or “Verified”?**

No. SHAKEN/STIR provides authentication information to receiving carriers, but the receiving carrier and device ultimately determine whether and how a trusted or verified indication is displayed.

  


  


**Q. Why is my number still showing as “Spam Likely” after SHAKEN/STIR registration?**

SHAKEN/STIR authenticates the caller but does not determine the phone number's reputation. Spam labels may be based on factors such as call volume, recipient complaints, calling patterns, analytics-provider data, or the number's previous activity. For eligible U.S. numbers, review Voice Integrity for reputation remediation.

  


  


**Q. Will completing A2P registration automatically enable SHAKEN/STIR?**

Eligible phone numbers associated with qualifying A2P registrations may be enrolled in SHAKEN/STIR automatically. You can review your current registration status in the HighLevel Trust Center.

* * *

#

# Troubleshooting: Not Receiving the OTP to Verify Your WhatsApp Number

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007214-troubleshooting-not-receiving-the-otp-to-verify-your-whatsapp-number](https://help.gohighlevel.com/support/solutions/articles/155000007214-troubleshooting-not-receiving-the-otp-to-verify-your-whatsapp-number)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# Troubleshooting: Not Receiving the OTP to Verify Your WhatsApp Number

If you are unable to receive the OTP (One-Time Password) while verifying your WhatsApp number in a sub-account, this article will help you identify the cause and resolve the issue.

## Why This Issue Happens

The most common reason OTP verification fails is that the phone number you are trying to onboard is already registered with the WhatsApp Business App or WhatsApp Messenger. A number can only be actively used on one WhatsApp platform at a time through a standard connection.

**Note:** This one-platform-at-a-time rule applies to the standard onboarding path. If your account is eligible for WhatsApp Coexistence, the same number can run on both the WhatsApp Business App and the API simultaneously through a separate, dedicated onboarding flow that does not go through this OTP check the same way. If you want to keep using the app and CRM on the same number, check whether Coexistence is available before applying Option 2 below.

## Check if the Number Is Already Registered

Please verify whether the phone number is currently active on:

  * WhatsApp Business App, or
  * Regular WhatsApp Messenger


If the number is already registered, WhatsApp will block OTP delivery during onboarding. Below are reliable and practical ways to check whether a phone number is registered on WhatsApp Business.

**Method 1: Use WhatsApp's Click to Chat Feature**

  * Open a browser.
  * Enter the following URL (replace with the full number including country code):


    
    
    https://wa.me/<countrycode><phonenumber>
    
    Example: https://wa.me/919876543210

  * Press Enter.


Result Interpretation:

  * **If WhatsApp opens** → The number is registered on WhatsApp (could be personal or business).
  * **If you see "Phone number shared via url is invalid"** → The number is not registered on WhatsApp.


**Method 2: Check Inside the WhatsApp Business App**

  * Save the number in your phone contacts.
  * Open WhatsApp.
  * Start a new chat → Search for the contact.


Indicators:

  * If the contact appears → The number is on WhatsApp.
  * If the contact does not appear → Not registered.


Business App Indicator:

  * If the profile shows "Business Account" or "Verified Business," the number is on WhatsApp Business.
  * Business accounts often show a business name, business category, and an optional catalog.


## Choose One of the Following Solutions

1| Use a Different Phone Number (Recommended)

  * Use a fresh phone number that has never been registered on WhatsApp.
  * Proceed with onboarding using the new number.

  
---|---  
2| Remove the Existing WhatsApp AccountIf you must use the same number, follow these steps carefully:

  * Install WhatsApp (Business or regular) on your mobile device using the same number.
  * Open WhatsApp and go to Settings.
  * Select Account → Delete Account.
  * Confirm deletion of the WhatsApp account from the mobile device.
  * Wait a few minutes, then retry onboarding and OTP verification in your sub-account.

Deleting the WhatsApp account will permanently remove chat history and data associated with that number.  
---|---  
  
## Still Not Receiving the OTP?

If the phone number:

  * Is not registered on WhatsApp or WhatsApp Business, and
  * You are still unable to receive the OTP,


Please raise a support ticket with the following details:

  * Phone number (with country code)
  * Sub-account ID
  * Screenshot or exact error message shown during OTP verification
  * Approximate time of the failed OTP attempt


Our support team will investigate this further with Meta.

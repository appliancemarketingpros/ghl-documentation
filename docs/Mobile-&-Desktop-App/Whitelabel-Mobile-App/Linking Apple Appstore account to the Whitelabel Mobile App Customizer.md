# Linking Apple Appstore account to the Whitelabel Mobile App Customizer

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007232-linking-apple-appstore-account-to-the-whitelabel-mobile-app-customizer](https://help.gohighlevel.com/support/solutions/articles/155000007232-linking-apple-appstore-account-to-the-whitelabel-mobile-app-customizer)  
**Category:** Mobile & Desktop App  
**Folder:** Whitelabel Mobile App

---

# **Mobile App Onboarding Flow:**  
**App Store API Key, Bundle Identifier, and Firebase Configuration**

**Overview**

This guide explains every action you need to take in HighLevel’s Mobile App Builder to prepare your white‑label mobile app for submission to Apple and Google..

  
You will:

1.**Create an App Store Connect API key** so HighLevel can automatically handle future submissions and updates.

2\. **Register a unique bundle identifier** that Apple and Firebase will recognize as your app’s ID.

3\. **Connect Firebase** by uploading your configuration files to enable push notifications, analytics, and crash reporting.

Completing all three steps ensures your build process is seamless and future releases require minimal effort.

### Please note

  * An Apple Developer Program account with Admin access is required before you begin.
  * Keep the Key ID, Issuer ID, and downloaded `.p8` file secure; Apple only allows you to download these once.
  * The bundle identifier must be unique across the entire App Store and must exactly match the IDs used in Firebase.
  * Use the same Google account throughout the Firebase steps to avoid permission errors.
  * If you are rebuilding an existing app, confirm that your existing app uses the same bundle identifier and Firebase project.


## **What is the AppStore Onboarding Flow?**

HighLevel’s appstore onboarding flow is a once‑per‑app wizard that collects the credentials required to compile, sign, and publish your whitelabelled mobile app on the Apple AppStore for your customers with an iOS device to download. After you finish these steps, HighLevel can build and push updates without manual intervention, and features such as push notifications will work instantly.

##   


  


## **How to Complete the Onboarding Flow**

  


### **Step 1 – Generate an App Store Connect API Key**  
**Video tutorial:[ https://app.arcade.software/share/OYkGxoZSQrDPyo7tDDYj](<https://app.arcade.software/share/OYkGxoZSQrDPyo7tDDYj>)**

  1. **Open the Apple portal -** Go to _<https://appstoreconnect.apple.com/access/integrations/api>_. You will land on the **Users and Access › Keys** page. 
  2. **Choose App Store Connect API -** In the left sidebar, select **Keys** under **App Store Connect API**. 
  3. **Generate the key** \- Click **Generate API Key** , give the key an easily recognisable name (for example, _HighLevel Mobile App Automation_), and click **Generate**. 
  4. **Download the**`**.p8**`**file** \- The file appears once only. Save it somewhere secure such as a locked password vault.
  5. **Copy the IDs** \- In the key table, copy the **Key ID**. Your **Issuer ID** appears at the top of the page. You will paste both values, plus the `.p8` file, into HighLevel's Mobile App Customizer.
  6. **Upload in the Mobile App Customizer** \- Return to the Mobile App Builder, expand **App Store Connection** , and upload the three pieces of information.


  
**Quick note:**

You can use one API key for multiple apps. If a key is ever compromised, revoke it in App Store Connect and create a new one, then update the value in HighLevel.

### **Step 2 – Register the Bundle Identifier**  
**Video tutorial:**[**https://app.arcade.software/share/VUWqWe0qiHyZ3ImZWken**](<https://app.arcade.software/share/VUWqWe0qiHyZ3ImZWken>)

  


1\. Launch the **App Setup stage** in the HighLevel wizard. You will see a field labelled Package Name / Bundle Identifier. 

  


2\. Click **Register** to open the dialog. HighLevel validates your Apple account and shows the team that will own the identifier. 

  


3\. Enter a **reverse‑DNS identifier** , for example **`com.youragency.appname`**. Stick to lowercase letters, numbers, and periods.

  


4\. Review Apple’s definition, Click the small info icon to read Apple’s explanation of bundle identifiers and why they must be unique. 

  


5\. **Confirm and save** HighLevel registers the identifier in your Apple Developer account. If the ID is already taken, you will see an error and must choose a different string.

  


6\. Enable capabilities (optional). If you require services such as Apple Sign‑In or Push Notifications, you can enable them later in your Apple Developer portal under Certificates, Identifiers & Profiles.

**Why this matters** \- The bundle identifier ties together your code signing, push certificates, and App Store listing. Using the same ID across Apple and Firebase avoids mismatched signing errors during build time.

### **Step 3 – Upload Firebase Configuration Files**

  


**Video tutorial:[ https://app.arcade.software/share/M0PMs6CwsZWTO4IXrx9r](<https://app.arcade.software/share/M0PMs6CwsZWTO4IXrx9r>)**

  


1\. **Open Firebase Console** \- Go to `https://firebase.google.com/` and click Go to console. Sign in with your Google account. 

  


2\. Create or **select a projec** t Click **Add project** if this is your first time, or open an existing project that will own the app.

  


3\. Add iOS and Android apps **Click Add App, choose iOS** , and enter the bundle identifier from Step 2.

  


4\. Download the config files For iOS **download `GoogleService-Info.plist** `. Keep the default file names.

  


5.**Upload in HighLevel** Return to the Setup Firebase stage, drag‑and‑drop files into the upload area, and click Continue.

  


6\. Wait for validation. HighLevel parses the files and confirms that the bundle identifiers match those registered in Apple Developer. Once validated, push notifications and analytics are enabled.

**Advanced** \- To enable APNs push notifications via Firebase Cloud Messaging, you can upload your `.p8` push key in the Project Settings › Cloud Messaging tab inside Firebase. HighLevel does not require this, but it allows you to send notifications from Firebase directly.

  


**Frequently Asked Questions**

Q: Do I need a separate API key for each app?

A: A single App Store Connect API key can authorize multiple apps. You may create additional keys if you prefer to isolate access.

Q: My bundle identifier is already in use. What should I do?

A: Append your company initials or region code, for example `com.youragency.appname.na`, until the ID is unique.

Q: I lost the `.p8` file. What now?

A: Revoke the key in **App Store Connect › Users and Access › Keys**, then create and upload a new key in HighLevel.

Q: Can I change the Firebase project later?

A: Yes, but you must regenerate and upload new `plist` and `json` files that reference the same bundle identifier. Remember to update your Apple Push keys if you move projects.

Q: How long does Apple review take after I finish these steps?

A: First‑time reviews typically take 1-3 business days, though the queue can be longer during holidays or major events.

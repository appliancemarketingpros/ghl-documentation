# Whitelabel mobile app Build failures

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007252-whitelabel-mobile-app-build-failures](https://help.gohighlevel.com/support/solutions/articles/155000007252-whitelabel-mobile-app-build-failures)  
**Category:** Mobile & Desktop App  
**Folder:** Whitelabel Mobile App

---

# White‑Label Mobile App — **Build Failures (Update/Resubmission)**

_A practical checklist to diagnose and fix build errors after you update your app._

  
Pre‑flight checks (do these before you press **Build)**

  


  1. **App exists in the stores**
     * **iOS:** Confirm the app record is created in **App Store Connect → Apps** (correct **Bundle ID** , platform **iOS**).
     * **Android:** Confirm the app record is created in **Google Play Console → All apps** (correct **package name**).
  2. **Contact details are valid**
     * **Phone number** includes **country code** and uses **E.164** format (e.g., `+1…`, `+44…`).
     * **Emails/URLs** are live, public, and on your company domain.
  3. **Metadata passes store rules**
     * **Descriptions** are **under the character limits** shown in the UI counters.
     * **No emojis** or decorative symbols in name, subtitle, or descriptions.
     * **Default locale** is **English (United States)** — `en‑US` (some UIs may display it as `eng-us`).
     * Links for **Privacy Policy** and **Terms** open without login and use **HTTPS**.
  4. **Apple account hygiene**
     * Two‑factor auth is on; **Agreements, Tax, and Banking** has **no pending items**.
  5. **Google Play account hygiene**
     * Play Console is verified for your organization; **API access** is configured (Cloud project linked, service account added, permissions granted).


* * *

## **Step‑by‑step fixes for common build failures**

# **Apple Developer Account & Certificates**

### **1\. Apple Developer Agreement has expired**

** _Error in log:_**_"A required agreement is missing or has expired. This request requires an in-effect agreement that has not been signed or has expired."_

**Fix:**

  * 1\. Go to https://developer.apple.com/account and sign in as the Account Holder.
  * 2\. Accept any pending agreement banner shown on the dashboard or under Agreements, Tax, and Banking.
  * 3\. Also check App Store Connect at https://appstoreconnect.apple.com for additional agreements (e.g. Paid Apps).
  * 4\. Retry the build from your HighLevel Mobile App Customizer.


###   


### **2\. iOS Certificate not available on Developer Portal**

** _Error in log:_**_"Certificate 'XXXXXXXXXX' (stored in your storage) is not available on the Developer Portal."_

**Fix:**

  * 1\. Contact HighLevel Mobile Support and share your iOS bundle ID and the certificate ID from the error.
  * 2\. Support will clear the stale certificate reference so a fresh one can be generated on the next build.
  * 3\. Retry the build once support confirms the cleanup.   
  


### **3\. Provisioning profile does not include the signing certificate**

** _Error in log:_**_"Provisioning profile \"match AppStore com.yourapp\" doesn't include signing certificate ..."_

**Fix:**

  * 1\. Contact HighLevel Mobile Support and share your iOS bundle ID + the error message.
  * 2\. Support will regenerate the provisioning profile in your Apple Developer account.
  * 3\. Retry the build.  
  


### **4\. Provisioning profile missing a capability or entitlement**

** _Error in log:_**_"Provisioning profile ... doesn't support the Communication Notifications capability." / "doesn't include the ... entitlement."_

**Fix:**

  * 1\. Go to https://developer.apple.com/account → Certificates, Identifiers & Profiles → Identifiers.
  * 2\. Select your bundle ID, scroll to Capabilities, turn ON the capability named in the error, and click Save.
  * 3\. Contact HighLevel Mobile Support to regenerate the provisioning profile.
  * 4\. Retry the build.  
  


# **App Store Connect (iOS)**

### **5\. A review submission is already in progress**

** _Error in log:_**_"Cannot submit for review – A review submission is already in progress."_

**Fix:**

  * 1\. Sign in to https://appstoreconnect.apple.com → My Apps → your app.
  * 2\. Open the version that shows "Waiting for Review" or "In Review".
  * 3\. Click Remove from Review (top right) to cancel it, OR wait for Apple to finish.
  * 4\. Retry the build once the previous version is no longer in review.  
  


### **6\. App Store version is not in a valid state**

** _Error in log:_**_"appStoreVersions with id '...' is not in valid state. This resource cannot be reviewed."_

**Fix:**

  * 1\. Open https://appstoreconnect.apple.com and check the version status banner (e.g. Rejected, Metadata Rejected, Developer Rejected).
  * 2\. Fix the underlying issue flagged by Apple, OR remove the blocked version from the (...) menu next to its name.
  * 3\. Retry the build.  
  


### **7\. Missing release notes (What's New)**

**_Error in log:_**_"The provided entity is missing a required attribute – You must provide a value for the attribute 'whatsNew'."_

**Fix:**

  * 1\. Open HighLevel Mobile App Customizer → Release Notes / What's New field.
  * 2\. Enter a real sentence describing what changed (e.g. "Improved booking flow and fixed login issues on iPhone 15"). Avoid generic text like "Bug fixes" — Apple sometimes filters it out.
  * 3\. Save and retry the build.  
  


### **8\. iPad screenshot missing**

** _Error in log:_**_"App screenshot missing (APP_IPAD_PRO_3GEN_129). A screenshot with type ipadPro129 is required."_

**Fix:**

  * 1\. Open HighLevel Mobile App Customizer → iOS screenshots.
  * 2\. Upload iPad Pro 12.9-inch screenshots (2048 × 2732 pixels). You can resize your iPhone mockup if needed.
  * 3\. Save and retry the build.  
  


### **9\. Phone number in invalid format**

** _Error in log:_**_"The phone number must be in a valid format. Preface the phone number with '+' followed by the country code."_

**Fix:**

  * 1\. Open HighLevel Mobile App Customizer → support phone number field.
  * 2\. Update it to include the country code with a + sign (e.g. +1 555 123 4567).
  * 3\. Make sure the same number is also valid in App Store Connect → App Information → Contact Information.
  * 4\. Save and retry.  
  


### **10\. Same category selected twice**

** _Error in log:_**_"You may not select the same category twice for your app."_

**Fix:**

  * 1\. Open https://appstoreconnect.apple.com → your app → App Information → General Information.
  * 2\. Set Primary as Productivity and Secondary categories to two different values (or leave Secondary blank).
  * 3\. Save and retry the build.  
  


### **11\. iOS app not yet created in App Store Connect**

** _Error in log:_**_"Could not find app with app identifier 'com.yourapp' in your App Store Connect account."_

**Fix:**

  * 1\. Sign in to https://appstoreconnect.apple.com and click (+) → New App in My Apps.
  * 2\. Pick iOS, fill in the app name and language, and select the bundle ID that matches the one in your HighLevel customizer.
  * 3\. Create the IOS app submission
  * 4\. Save the listing, then retry the build.  
  


# **Google Play Console (Android)**

### **12\. Google Play Android Developer API is disabled**

** _Error in log:_**_"Google Play Android Developer API has not been used in project ... before or it is disabled."_

**Fix:**

  * 1\. Click the exact URL in the error message (it contains your project number).
  * 2\. Sign in with the Google account that owns the Google Cloud project.
  * 3\. Click Enable to turn on the Google Play Android Developer API.
  * 4\. Wait 2–3 minutes, then retry the build.  
  


### **13\. Google Play service account credentials missing or invalid**

** _Error in log:_**_"play_services.json doesn't seem to be a JSON file." / "missing client_email" / file is empty {} or null._

**Fix:**

  * 1\. Confirm with HighLevel Mobile Support that a Google Cloud service account has been generated for your agency.
  * 2\. If self-managing: open https://console.cloud.google.com → IAM & Admin → Service Accounts → your account → Keys → Add Key → Create new JSON key, and download the file.
  * 3\. Share the JSON file with HighLevel Mobile Support so they can upload it for your build.
  * 4\. Retry the build.  
  


### **14\. Missing short description (promotional text)**

**_Error in log:_**_"This app has no short description (promotional text) for language en-US."_

**Fix:**

  * 1\. Open https://play.google.com/console → your app → Main store listing.
  * 2\. Fill in the Short description (max 80 characters).
  * 3\. Confirm the default language is set to English – United States.
  * 4\. Save and retry the build.  
  


### **15\. Version code already used**

** _Error in log:_**_"Version code XXX has already been used."_

**Fix:**

  * 1\. Retry the build — most of the time HighLevel will auto-bump the version code on the next run.
  * 2\. If it keeps failing, contact HighLevel Mobile Support and share your Android package name.
  * 3\. In Play Console → Production → Releases, confirm the previous build was actually published or rolled back (not stuck in draft).  
  


### **16\. App is suspended on Google Play**

** _Error in log:_**_"The app is suspended."_

**Fix:**

  * 1\. Open https://play.google.com/console → your app → Policy status.
  * 2\. Read the exact violation reason listed by Google and fix the underlying issue (content, icon/name, restricted features, etc.).
  * 3\. Submit an appeal from the Policy status page if you believe the suspension was incorrect.
  * 4\. Retry the build once Google reinstates the app.  
  


### **17\. App name already used by another app**

** _Error in log:_**_"Cannot add localization due to app name. You cannot add this localization because the app name is already being used by another app."_

**Fix:**

  * 1\. Open HighLevel Mobile App Customizer → app name field, and change it to something unique.
  * 2\. If you own the trademark, file a name release claim at https://support.google.com/googleplay/android-developer/answer/2363332.
  * 3\. Save and retry the build.  
  


### **18\. Package not found / first upload to Play Console**

** _Error in log:_**_"Package not found: com.youragency.app."_

**Fix:**

  * 1\. Sign in to https://play.google.com/console → Create app, and fill in the basic details.
  * 2\. Manually upload the very first .aab file (request a copy from HighLevel Mobile Support) to the Internal Testing track.
  * 3\. Future builds will work automatically after that.  
  


### **19\. Health declaration incomplete**

** _Error in log:_**_"You must complete the health declaration."_

**Fix:**

  * 1\. Open https://play.google.com/console → your app → Policy → App content.
  * 2\. Complete the Health section (and any other incomplete declarations).
  * 3\. Save and retry the build.  
  


# **Temporary Infrastructure (just retry)**

### **20\. Gradle daemon crashed / Build agent out of memory**

** _Error in log:_**_"Gradle build daemon disappeared unexpectedly" / "AAPT2 Daemon ... unexpectedly exit" / "Daemon vm is shutting down"._

**Fix:**

  * 1\. Simply retry the build from your HighLevel Mobile App Customizer.
  * 2\. If it fails 3 times in a row, contact HighLevel Mobile Support.  
  


### **21\. Apple infrastructure outage (502 Bad Gateway)**

**_Error in log:_**_"Status Code: 502 (bad gateway) – Bad Gateway"_

**Fix:**

  * 1\. Wait 15–30 minutes.
  * 2\. Check https://developer.apple.com/system-status to confirm Apple's services are operational.
  * 3\. Retry the build.

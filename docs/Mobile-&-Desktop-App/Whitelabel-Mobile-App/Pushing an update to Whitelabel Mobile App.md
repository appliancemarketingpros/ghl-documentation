# Pushing an update to Whitelabel Mobile App

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007242-pushing-an-update-to-whitelabel-mobile-app](https://help.gohighlevel.com/support/solutions/articles/155000007242-pushing-an-update-to-whitelabel-mobile-app)  
**Category:** Mobile & Desktop App  
**Folder:** Whitelabel Mobile App

---

# **Updating Your Live iOS App in App Store Connect**

Once your app is live on the App Store, you may need to **release updates** with bug fixes, new features, or branding changes. This guide walks you through updating your existing app.

* * *

# **Prerequisites**

  * Access to your **Apple Developer Account**
  * A new **app build** (uploaded via Xcode or Transporter)
  * Updated **metadata** (screenshots, description, etc. if needed)


* * *

## **Step 1: Start a New Build**

  1. Click on Launch App > Generate Build > Start App build
  2. Build progress will show on screen, wait till it gets completed.


  


## **Step 2: Log in to App Store Connect**

  1. Visit [App Store Connect](<https://appstoreconnect.apple.com/>).
  2. Log in using your Apple Developer credentials.
  3. From the **Apps Dashboard** , select the app you want to update.


>  _You’ll see your app listed with the current live version._

* * *

## **Step 3: Create a New Version**

  1. Inside your app page, click the **Add New Version** button.
  2. Enter the **new version number** (must match the build version uploaded from Xcode).


⚠️ **Note:** Version numbers must be sequential (e.g., 1.0 → 1.1 → 1.2).

* * *

## **Step 4: Update App Information (if needed)**

  * **What’s New in This Version** – Describe bug fixes or new features.
  * **Screenshots/Previews** – Update if UI/UX has changed.
  * **Metadata** – Adjust description, keywords, or support URLs if required.


* * *

## **Step 5: Attach the New Build**

  1. Under the **Build Section** , click **Select a Build before you submit**.
  2. Choose the newly uploaded build.
  3. Save changes.


* * *

## **Step 6: Review Privacy & Compliance**

  * Confirm your **Privacy Policy URL**.
  * Revisit the **App Privacy questionnaire** if any new data collection has been introduced.


* * *

## **Step 7: Submit for Review**

  1. Double-check all fields (icon, screenshots, metadata).
  2. Click **Submit for Review**.
  3. Apple’s review team will test the update before releasing it.


* * *

## **⚠️ Common Update Errors**

  * ❌ Build not visible – Ensure you uploaded via Xcode/Transporter with the correct version.
  * ❌ Version mismatch – The version number in App Store Connect must match Xcode.
  * ❌ App rejected – Review rejection reason, fix, and resubmit.

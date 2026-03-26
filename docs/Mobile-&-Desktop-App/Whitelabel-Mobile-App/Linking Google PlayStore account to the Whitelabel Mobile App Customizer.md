# Linking Google PlayStore account to the Whitelabel Mobile App Customizer

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007233-linking-google-playstore-account-to-the-whitelabel-mobile-app-customizer](https://help.gohighlevel.com/support/solutions/articles/155000007233-linking-google-playstore-account-to-the-whitelabel-mobile-app-customizer)  
**Category:** Mobile & Desktop App  
**Folder:** Whitelabel Mobile App

---

# **Google Play: Connect Account and App Setup**

## **Overview**

This article consolidates the full Google Play onboarding flow inside HighLevel’s Agency App Manager. You will connect your Google Play Developer account, then register your Android package name so HighLevel can build and submit your branded app. The steps here merge both tutorials into a single, complete walkthrough.

### Please note

  * You need a Google Play Developer account with Admin access before you begin.
  * Your package name must be unique and permanent, choose it carefully since it cannot be changed after publishing.
  * Use only lowercase letters, numbers, and periods in the package name, for example com.brand.appname.
  * Keep your Google account signed in during the whole flow to prevent permission errors.


****

## **Covered in this Article**

  * What this workflow does
  * Prerequisites
  * Connect your Google Play Developer account in HighLevel
  * Register your Android package name in App Setup
  * Validation and common errors
  * FAQs


## **Prerequisites**

  * A paid Google Play Developer account with Admin rights.
  * Access to the Google account that owns the Play Developer account.
  * A clear package name plan that follows reverse DNS format, for example com.company.product.


## **Step 1: Connect your Google Play Developer account in HighLevel**

  


**Video tutorial:<https://app.arcade.software/share/vN0AiiOM6x2ZTKlsUqD9>**

  


  1. **Open Agency App Manager**
     * In HighLevel, go to **Mobile App** in the left navigation.
     * Open **Agency App Manager**. You should see two tiles: **Apple App Store** and **Google Playstore** , each with a **Set Up** button.
     * Confirm the **Steps** rail on the left shows **Distribution**.  
  

  2. **Start the Google Play connection**
     * Click **Set Up** on the **Google Playstore** tile.
     * The connection form loads for Play Store.  
  

  3. **Name the connection**
     * In **Play Store account name** , type a short label you and your team will recognize, for example your agency or brand name.
     * Use a unique label if you plan to connect multiple Play accounts later.  
  

  4. **Open Google Play Console using the built in link**
     * Click the link in the form to open the Google Developer account page. The link takes you to **﻿[![icon](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155062059746/original/vySdHUQJmHcgZuq_iptJP2rBYZ_bsXsx-w.png?1767731032) GoogleGoogle Play for business | Launch & monetize your apps | Google Play Console](<https://play.google.com/console/developers>)﻿ ** in a new tab.
     * Sign in to the Google account that owns the **Google Play Developer** program. If you are already signed in, confirm it is the correct account.  
  

  5. **Verify access in Play Console**
     * Make sure you can reach the Developer Console home screen.
     * If Google prompts you to accept updated terms or verify your account, complete those prompts.
     * If you see a permission error, ask the Owner or an Admin to grant you **Admin** access under **Users and permissions**.  
  

  6. **Return to HighLevel and save**
     * Go back to the HighLevel tab.
     * Confirm the **Play Store account name** field is filled.
     * Click **Save** or **Continue** to store the connection details.
     * The Google Playstore tile will now reflect that the account is connected. If it still shows Not Connected, refresh the page and try again.  
  

  7. **Quick checks before moving on**
     * You are signed in to the correct Google account in the browser.
     * Your Play Developer account is active and in good standing.
     * You have Admin level permissions in Play Console.


**  
Tip** : If you manage several Google accounts in the same browser, open an incognito window and sign in only to the account that owns the Play Developer program. This avoids linking the wrong account.

  


## **Step 2: Register your Android package name in App Setup**

  


**Video Tutorial:<https://app.arcade.software/share/xiKjlvnbJ6kHP1CBc8oW>**

  


  1. In the same connection workflow, **open the App Setup** stage.  
  

  2. Click **Registe** r to create your Android package name.  
  

  3. Enter the **identifier in reverse DNS format** , for example com.youragency.clientapp. Avoid spaces or uppercase characters.  
  

  4. **Confirm to register**. HighLevel validates the value and completes registration. You will see a success state when the package name is registered.  
  

  5. Continue to the next stage of your app distribution setup, or return later if you still need to prepare assets.


## **Validation and common errors**

  * **Package name already taken** : Choose a new value, for example add initials or a region code such as [com.youragency.clientapp.na](<http://com.youragency.clientapp.na>).  
  

  * **Insufficient permissions** : Make sure you are an Admin on the Play Developer account, or ask the account Owner or an Admin to grant you access under Users and permissions.  
  

  * **Mismatch with build** : Ensure the package name in your app’s build files matches the registered value. Use the same identifier consistently in your Android project and in any related services.


## **Frequently Asked Questions**

Q: Do I need to be an Admin in Play Console to complete this?

A: Yes, Admin or Owner access is required to manage app registration and distribution settings.

Q: Can I change the package name later?

A: No, once the app is published the package name is permanent. If you need a different name later, you must publish it as a new app.

Q: What is a good naming pattern for agencies with many client apps?

A: Use a stable reverse DNS base plus a client suffix, for example com.agencyname.clientbrand.

Q: Do I have to create a new Play Developer account for every brand?

A: No, one Play Developer account can own multiple apps. Use clear labels for each connection in HighLevel so you can track which app belongs to which client.

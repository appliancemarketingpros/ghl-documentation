# How to Create a Whitelabel Membership PWA in Legacy Memberships

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001224426-how-to-create-a-whitelabel-membership-pwa-in-legacy-memberships](https://help.gohighlevel.com/support/solutions/articles/48001224426-how-to-create-a-whitelabel-membership-pwa-in-legacy-memberships)  
**Category:** Memberships & Communities  
**Folder:** Membership/Courses Sites

---

Creating a whitelabel membership Progressive Web App (PWA) allows businesses to offer a seamless, branded experience without the need for a traditional mobile app. This guide walks you through setting up, customizing, and deploying your PWA using HighLevel. You'll also find installation instructions, and comparisons with native mobile apps.

  

    
    
    **Important:** The Membership PWA is available only in the Legacy Memberships experience. It is not supported in the Client Portal experience. If your location is using Client Portal, switch to Legacy Memberships before configuring the PWA.

  


* * *

**TABLE OF CONTENTS**

  * What is a Whitelabel Membership PWA?
  * Key Benefits of Using a Whitelabel Membership PWA
  * Why You Should Consider Creating a PWA : Key Differences
  * Prerequisites: Prepare Your Membership and Branding
  * How to Set Up Your Whitelabel Membership PWA
  * Troubleshooting the Membership PWA
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is a Whitelabel Membership PWA?**

  


A Progressive Web App (PWA) is a web-based application that provides a mobile app-like experience without requiring users to download it from an app store. HighLevel's Whitelabel Membership PWA allows businesses to customize the look, branding, and functionality of their membership site while maintaining full control over content and user experience.

  


Unlike native mobile apps, PWAs are accessed through a web browser and can be installed directly onto a user's device without going through Apple’s App Store or Google Play. This makes them a flexible and cost-effective alternative for businesses wanting to offer an app-like experience without the complexity of native app development.

  


In HighLevel, the Membership PWA is part of the Legacy Memberships experience. It is separate from the Client Portal and Client Portal mobile app.

* * *

## **Key Benefits of Using a Whitelabel Membership PWA**

  


  * **Works Across All Devices:** Accessible on mobile, tablet, and desktop without separate development.


  


  * **App-Like Experience:** Learners can open the membership portal from their Home Screen, desktop, or application launcher.


* * *

## **Why You Should Consider Creating a PWA : Key Differences**

  


Feature| PWA| Native Mobile App  
---|---|---  
Installation| Installed via browser, no app store required| Downloaded from App Store/Google Play  
Updates| Automatically updated when refreshed| Requires manual updates via app stores  
Offline Capability| Internet access is generally required; availability of previously loaded content may vary.| Full offline functionality  
Push Notifications| Availability depends on the device, browser, operating system, and HighLevel feature support.| Fully supported  
Performance| Fast and lightweight| Generally faster for complex apps  
Approval Process| No app store approval required| Subject to App Store/Google Play guidelines  
  
  


* * *

## **Prerequisites: Prepare Your Membership and Branding**

  


Before configuring your Membership PWA, it’s important to ensure your branding and membership structure are set up correctly. This foundation improves your user’s experience and makes your PWA feel polished and professional.

  


**Customize Your Branding:** Switch to Legacy Memberships, then navigate to **Memberships > Courses > Settings** and configure the available branding and app settings. Upload your business logo, choose your color scheme, and add a favicon for browser tab branding. These visual elements appear throughout the app and reinforce your brand identity.

  


**Set Up Your Membership Structure:** In Legacy Memberships, navigate to **Memberships > Courses > Products** to create or review your courses, offers, access levels, and related content. Create product tiers, add courses, and configure pricing and access levels. Organizing your content now ensures a smooth learning journey inside the PWA.

  


**Link a Custom Domain (Optional):** Connect a custom domain (e.g., app.yourbrand.com) via Settings > Domains. Adding a branded domain enhances trust and gives your PWA a more polished, app-like experience.

  


Once these steps are complete, you’re ready to begin configuring your Membership PWA.

* * *

## **How to Set Up Your Whitelabel Membership PWA**

  


### **Access Memberships**

  


To begin setting up your Membership PWA, In the sub-account, navigate to **Memberships**. If Client Portal opens, use the Memberships switcher to move to **Legacy Memberships**. Then select **Courses > Settings** from the top navigation menu. This will open the Membership Settings area, where you’ll find key configuration options.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155043790988/original/Jw_NBG-BSTHD4Pr_3QhBnvoaUZbm9u2adA.png?1742714853)

  


### **Select App Settings**

  


Once you’ve navigated to Courses > Settings, you’ll land on the main configuration page for your memberships. From here, look for the App Settings tile. This is where you’ll customize how your Progressive Web App (PWA) appears and behaves on both desktop and mobile devices.

  


If the **App Settings** tile is not visible, confirm that the location is using Legacy Memberships rather than Client Portal.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155043790991/original/xDipl4dNfcTNskX1LzA_GSVxyZljptM94w.png?1742714874)

  


  


### **Enable PWA Installation**

  


Enabling PWA installation allows your users to “install” your app on their devices just like a native app, improving accessibility and engagement. Once enabled, After PWA installation is enabled, learners can install it from supported browsers. The available installation option and wording vary by browser, operating system, and device.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076517577/original/BOTGuB2amhBSSHAJ6yt9yLrov4SsGlvq4w.png?1784648504)

  


  


### **Customize Your PWA Settings**

  


Once you’ve toggled Enable PWA to “on” inside the App Settings area, you’ll unlock a set of configuration fields that define how your PWA appears and behaves. This is where the real customization begins—giving your app its name, identity, and look.

  


**App Name, Short Name & Description**

  


These fields shape how your app is presented to users across devices:

  


**Name:** This is your full app name, shown during installation prompts and in the app title bar.

  


**Short Name:** A shortened version of your app name that appears on home screens or in tighter display areas (e.g., app folders).

  


**Description:** A brief sentence that tells users what your app is about. It’s helpful context, especially when users are installing your PWA from the browser prompt.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155043791012/original/Vcoc6hZ7Kw6KldhhkG8b-AVcFs2zAA6-kQ.png?1742714955)

  


  


**App Icon**

  


You’ll need to upload two icons—a larger (512x512) and smaller (192x192) version. These are used across different devices and platforms, such as splash screens, app drawers, and home screens. While the system will automatically choose which icon to use based on screen size, we recommend uploading versions that match each dimension exactly. Icons must be in .jpg or .png format, and they should be visually identical to maintain brand consistency.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155043791026/original/LeloYP5WvL80RZy5Mfks-XLr05u7e8MxQQ.png?1742714981)

  


  


**App Colors**

  


HighLevel offers a selection of predefined color palettes for your app theme. These colors affect the styling of UI elements like buttons and headers. You can’t manually enter custom hex codes right now, but the palette choices are designed for strong contrast and visual clarity across devices. Just click to select the one that best fits your brand.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155043791031/original/r4pk9ZjA6VlRPciApO7AtBgJb-MVOCjLRA.png?1742715007)

  


**Save Your Settings**

  


After you’ve entered your app details, uploaded icons, and chosen your theme color, make sure to click Save in the upper-right corner. If you don’t save, none of your changes will apply when users try to install your PWA.

* * *

**Installing the PWA on a Windows Computer:**

  


After you are done customizing and enabling your Membership PWA, all that is needed to be done by your client is for them to click on this icon in their Browser Address Bar in **Chrome, when logging in to your Memberships Login Portal:**

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261426288/original/MbJoVwLdImX7MlCkuaUrRXz-474N0gpvdQ.png?1667582738)

  


  


And it would allow them to access your PWA on their desktop as a shortcut:

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261427004/original/2Dji97cvlDG-JSG1rm-xsv5ItSi1diOsDg.png?1667582951)

* * *

**Installing PWA on a Mac Computer:**

  


#### **Chrome or Microsoft Edge**

  1. Open the Membership login portal.  
  

  2. Sign in to the membership account.  
  

  3. Select the install icon in the browser address bar.  
  

  4. Confirm the installation.


####   


#### **Safari on supported macOS versions**

  


  1. Open the Membership portal in Safari.  
  

  2. Select **File > Add to Dock**.  
  

  3. Enter the app name.  
  

  4. Select **Add**.


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48261435611/original/p4ATAFL_gbARRLkJuKIPjBtPuF03iwQa1Q.png?1667586436)

* * *

### **Installing PWA on an Android device:**

  


For the most consistent installation experience, open the Membership login portal in Google Chrome. It can be installed by Adding the PWA to your Home Screen from your Chrome browser as in the video below.

  


  * Sign in to the membership account.  
  

  * Open the Chrome menu.  
  

  * Select **Install app** or **Add to Home screen**.  
  

  * Follow the on-screen instructions.


  
  


* * *

### **Installing PWA on an iOS Mobile Device:**

  


  * Open the Membership login portal in Safari.  
  

  * Sign in to the membership account.  
  

  * Tap the **Share** icon.  
  

  * Select **Add to Home Screen**.  
  

  * Review the app name and tap **Add**.


  
  


  


* * *

## **Troubleshooting the Membership PWA**

  


**App Settings is not visible**

Confirm that the location is using Legacy Memberships. The Membership PWA cannot be configured from the Client Portal experience.

  


**The installation option does not appear**

Confirm that PWA installation is enabled and the settings have been saved. Open the published Membership portal using HTTPS, sign in through a supported browser, and check the browser menu for Install app or Add to Home Screen.

  


**Updated branding is not appearing**

Remove the previously installed PWA, clear the relevant browser cache, reopen the Membership portal, and install the PWA again.

  


**Users are opening Client Portal instead**

Confirm which membership experience is active and switch to Legacy Memberships before using the Membership PWA.

* * *

## **Frequently Asked Questions**

  


**Q: Can I still submit my PWA to the App Store?**

The Membership PWA is designed to be installed directly from a supported browser. Packaging it with a third-party native wrapper is outside HighLevel’s standard Membership PWA setup and may require developer support and separate compliance with Apple or Google requirements.

  


For a supported branded native app experience, review HighLevel’s Client Portal Branded Mobile App options.

  


**Q: Does my PWA work offline?**

An internet connection is generally required to sign in, load courses, and access current membership content. Previously loaded content may remain temporarily available depending on the device and browser, but complete offline access is not guaranteed.

  


**Q: Can I send push notifications with a PWA?**

Push-notification availability depends on the device, browser, operating system, and notification functionality supported by HighLevel. Installing the Membership PWA does not automatically enable push notifications.

  


**Q: Do I need a developer to set up a whitelabel PWA?**

No, HighLevel's interface makes it easy to configure without coding skills.

* * *

### **Related Articles**

  


  * [How to Set Up the Client Portal ](<https://help.gohighlevel.com/en/support/solutions/articles/155000000193>)  
  

  * [Client Portal App – Custom Mobile App Notifications ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004592>)  
  

  * [Legacy Membership to Client Portal Migration ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002045>)

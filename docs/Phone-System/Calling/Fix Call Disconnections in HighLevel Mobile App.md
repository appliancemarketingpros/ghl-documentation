# Fix Call Disconnections in HighLevel Mobile App

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001172952-fix-call-disconnections-in-highlevel-mobile-app](https://help.gohighlevel.com/support/solutions/articles/48001172952-fix-call-disconnections-in-highlevel-mobile-app)  
**Category:** Phone System  
**Folder:** Calling

---

Mobile App Support

# Fix Call Disconnections in HighLevel Mobile App

Resolve call disconnection issues by configuring the correct permissions for background app refresh and microphone access on your mobile device.

What You'll Learn

If your calls disconnect immediately when using the HighLevel mobile app, the issue typically stems from disabled background app refresh or missing microphone permissions. This prevents the app from maintaining active call sessions.

This guide walks you through enabling the required permissions on both iOS and Android devices to ensure uninterrupted calling functionality.

Table of Contents

1

Why Calls Disconnect in the Mobile App

2

How to Enable Background App Refresh on iOS

3

How to Enable Microphone Permissions on iOS

4

How to Enable Background App Refresh on Android

5

How to Enable Microphone Permissions on Android

6

Frequently Asked Questions

1

## Why Calls Disconnect in the Mobile App

When calls disconnect immediately upon answering in the HighLevel mobile app, the root cause is typically one or both of the following permission issues:

**Background App Refresh Disabled** — The app cannot maintain active sessions when running in the background, causing calls to drop when the screen locks or you switch apps.

**Microphone Access Denied** — Without microphone permissions, the app cannot capture audio input, which terminates the call connection immediately.

Both permissions must be enabled to ensure stable call functionality. Follow the platform-specific instructions below to configure your device correctly.

2

## How to Enable Background App Refresh on iOS

Background App Refresh allows the HighLevel app to maintain call connections even when the app is not actively displayed on your screen. Follow these steps to enable it on your iPhone or iPad:

Step 1

Open iOS Settings

Launch the **Settings** app from your home screen.

Step 2

Navigate to General Settings

Scroll down and tap **General**.

Step 3

Access Background App Refresh

Tap **Background App Refresh** from the General menu.

Step 4

Enable Global Background Refresh

At the top of the screen, ensure **Background App Refresh** is set to either **Wi-Fi** or **Wi-Fi & Cellular Data** (not Off).

Step 5

Enable for HighLevel App

Scroll through the list of apps and locate **HighLevel**. Toggle the switch to enable Background App Refresh for the HighLevel app.

Configuration Complete

Background App Refresh is now enabled for HighLevel. Your calls will remain connected even when the app is in the background.

3

## How to Enable Microphone Permissions on iOS

Microphone access is required for the HighLevel app to capture audio during calls. Follow these steps to grant microphone permissions:

Step 1

Open iOS Settings

Launch the **Settings** app from your home screen.

Step 2

Locate the HighLevel App

Scroll down through your installed apps and tap **HighLevel**.

Step 3

Enable Microphone Access

Find the **Microphone** option and toggle it to **On** (the switch will turn green).

Permission Granted

Microphone access is now enabled for HighLevel. You can make and receive calls with audio capture working correctly.

4

## How to Enable Background App Refresh on Android

On Android devices, background app refresh functionality is managed through battery optimization settings. Follow these steps to ensure HighLevel can maintain call connections:

Step 1

Open Android Settings

Launch the **Settings** app from your app drawer or home screen.

Step 2

Navigate to Apps

Tap **Apps** (or **Apps & notifications** depending on your Android version).

Step 3

Select HighLevel App

Scroll through your app list and tap **HighLevel**.

Step 4

Access Battery Settings

Tap **Battery** or **Battery usage** from the app info screen.

Step 5

Disable Battery Optimization

Select **Unrestricted** or **Don't optimize** to prevent Android from limiting HighLevel's background activity. This ensures the app can maintain call connections when running in the background.

Note

Menu names and paths may vary depending on your Android device manufacturer and OS version. Look for options labeled "Battery optimization," "Background restrictions," or "Power saving exclusions."

Configuration Complete

Background activity is now unrestricted for HighLevel. The app can maintain call sessions even when the screen is off or other apps are in use.

5

## How to Enable Microphone Permissions on Android

Granting microphone permissions allows the HighLevel app to capture audio during calls. Follow these steps to enable microphone access on Android:

Step 1

Open Android Settings

Launch the **Settings** app from your app drawer or home screen.

Step 2

Navigate to Apps

Tap **Apps** (or **Apps & notifications** depending on your Android version).

Step 3

Select HighLevel App

Scroll through your app list and tap **HighLevel**.

Step 4

Access Permissions

Tap **Permissions** from the app info screen.

Step 5

Enable Microphone Access

Tap **Microphone** and select **Allow** or **Allow only while using the app**.

Permission Granted

Microphone access is now enabled for HighLevel. You can make and receive calls with audio capture working correctly.

6

## Frequently Asked Questions

Q: Why do my calls work fine on the desktop app but disconnect on mobile?

Desktop browsers typically grant persistent permissions and don't apply battery-saving restrictions. Mobile operating systems (iOS and Android) require explicit permissions for background activity and microphone access to protect user privacy and battery life. Follow the steps in this guide to configure your mobile device correctly.

Q: Will enabling background app refresh drain my battery faster?

Background app refresh uses minimal battery power when the app is not actively performing tasks. HighLevel only maintains background activity during active calls or when checking for notifications. The impact on battery life is negligible compared to the benefit of uninterrupted call functionality.

Q: I've enabled all permissions but calls still disconnect. What should I do?

First, verify that both background app refresh and microphone permissions are enabled by revisiting the Settings menu. If the issue persists, try restarting your device and testing a call again. Some Android devices have additional manufacturer-specific battery management settings that may need adjustment. Contact HighLevel support if the problem continues after trying these steps.

Q: Do I need to grant these permissions every time I update the HighLevel app?

No. Once you grant these permissions, they persist across app updates. However, major iOS or Android OS updates may occasionally reset some permission settings, so it's worth checking your permissions again if you experience call disconnections after an operating system upgrade.

Q: Can I receive calls while using other apps on my phone?

Yes. With background app refresh enabled, HighLevel can maintain call sessions even when you switch to other apps, check emails, or browse the web. The call audio will continue uninterrupted as long as both permissions (background refresh and microphone) remain enabled.

Q: Are these permission requirements the same for tablets?

Yes. iPads use the same iOS permission system as iPhones, and Android tablets use the same Android permission system as phones. Follow the appropriate iOS or Android instructions in this guide based on your tablet's operating system.

Q: What happens if I disable these permissions after enabling them?

If you disable background app refresh or microphone permissions, calls will begin disconnecting immediately upon answering, just as they did before you enabled the permissions. You'll need to re-enable these permissions following the steps in this guide to restore call functionality.

Q: Does HighLevel access my microphone when I'm not on a call?

No. HighLevel only activates microphone access during active calls. iOS and Android display visual indicators (such as an orange dot on iOS or a microphone icon on Android) whenever an app is actively using the microphone, providing transparency about microphone usage.

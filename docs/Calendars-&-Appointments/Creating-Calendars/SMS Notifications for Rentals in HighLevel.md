# SMS Notifications for Rentals in HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008416-sms-notifications-for-rentals-in-highlevel](https://help.gohighlevel.com/support/solutions/articles/155000008416-sms-notifications-for-rentals-in-highlevel)  
**Category:** Calendars & Appointments  
**Folder:** Creating Calendars

---

Rental Management

# SMS Notifications for Rental Bookings

Send automated SMS messages for rental booking confirmations, reminders, cancellations, and updates to keep customers and your team informed in real time.

What You'll Learn

This guide shows you how to configure SMS notifications for rental bookings in HighLevel. You'll learn which rental events support SMS, how to choose recipients, customize message templates, send test messages, and apply best practices for automated rental communication.

All configuration happens in Rentals Global Settings and applies automatically to every rental booking, giving you consistent, real-time SMS updates without manual follow-up.

Table of Contents

1

What Are SMS Notifications for Rental Bookings?

2

Key Benefits

3

Supported Rental Booking SMS Events

4

Recipient Options for Rental SMS Notifications

5

SMS Templates and Message Body

6

Sending a Test SMS

7

SMS Setup Requirements

8

How to Set Up SMS Notifications for Rental Bookings

9

Troubleshooting SMS Notifications

10

Frequently Asked Questions

11

Related Articles

1

## What Are SMS Notifications for Rental Bookings?

SMS Notifications for Rental Bookings allow you to send automated SMS messages when important rental booking events occur. These notifications help keep contacts and business users informed without requiring manual follow-up.

Rental SMS notifications are managed from Calendar Settings › Rentals › Global Settings › Notifications. Each notification type can be edited individually, allowing you to control the SMS message, recipient, template, and test delivery before enabling it for live rental bookings.

Because SMS is configured at the global Rentals level, your notification rules apply consistently to all rental bookings, giving you automated, real-time communication at scale.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077999603/original/RVMFvUXxGrcKpDBBBQ22s9PDSn13xt2cKw.png?1786353751)

2

## Key Benefits

SMS gives businesses a faster way to reach contacts and internal teams when booking activity changes. This helps reduce missed updates and supports better communication throughout the rental booking lifecycle.

**Faster Communication** — Send booking updates directly to recipients by SMS, reaching them where they're most likely to see it: their phones.

**Improved Show-Up Rates** — Use timely reminders to help contacts remember upcoming rental bookings, reducing no-shows and last-minute confusion.

**Flexible Recipient Control** — Choose whether SMS messages go to the contact, the business, or both, so each party receives only relevant messages.

**Custom Message Content** — Edit the SMS message body or select an existing SMS template to maintain your brand voice and include booking-specific details.

**Easy Testing** — Send a test SMS before using the message for live bookings, so you can validate merge fields, timing, and formatting without notifying real customers.

**Less Manual Follow-Up** — Automate common booking updates such as confirmations, cancellations, reminders, and follow-ups, freeing your team to focus on higher-value tasks.

3

## Supported Rental Booking SMS Events

Rental booking SMS events help you decide when automated messages should be sent. Each event represents a specific booking status or booking lifecycle moment, allowing you to customize communication for different situations.

SMS notifications can be configured for these rental booking events:

Event Type

Unconfirmed (Status: Unconfirmed)

Sends when a booking is requested with an unconfirmed status. Useful for concierge approvals or manual checks before confirming.

Event Type

Confirmation (Status: Booked)

Sends when a booking is confirmed or booked, or when its status changes from unconfirmed to confirmed.

Event Type

Cancellation

Sends when a booking is canceled, notifying customers and internal teams immediately.

Event Type

Rescheduled

Sends when dates or times of an existing booking are modified, keeping everyone updated on the new schedule.

Event Type

Reminder

Sends before the booking starts, based on the schedule you configure (e.g., 24 hours before, 1 hour before).

Event Type

Follow-Up

Sends after the booking is completed. Great for review requests, feedback collection, or upsell opportunities.

Each notification event can be edited separately, so the message and recipients can match the purpose of that event.

4

## Recipient Options for Rental SMS Notifications

Recipient settings control who receives each SMS notification. This allows businesses to keep customers informed while also notifying internal teams when booking activity changes.

Depending on the notification type, you can choose:

  * **Contact** — Sends the SMS to the customer or contact associated with the rental booking.
  * **Business** — Sends the SMS to the business recipient configured for rental booking communication (for example, a main rental operations number).


You can enable one or both recipient options based on how your team wants to manage booking updates. For example:

  * Send customer-facing messages (e.g., "Your rental starts tomorrow at 9:00 AM") only to the Contact.
  * Send internal alerts (e.g., "New rental booked for Unit #4 this weekend") only to the Business number.
  * Send both if it's important that the customer and your team receive the same real-time update.


5

## SMS Templates and Message Body

SMS templates make it easier to maintain consistent messaging across rental booking notifications. Each notification type includes a default message, and users can customize the content to match their business needs.

Inside the SMS tab, you can:

  * Select an existing SMS template from the **SMS template** dropdown.
  * Customize the **Message body** directly.
  * Use supported custom values to personalize messages with booking-specific details like contact name, booking start time, timezone, and listing name.
  * Reset the message back to the default content when needed using the "Reset to default" link.


You can configure different templates for Contact and Business recipients where available, tailoring tone, detail level, and calls to action for each audience.

Example default message content includes contact details and rental booking details, such as: "Hi {{contact.name}}, Your booking is confirmed for {{rentalBooking.start_time}} {{rentalBooking.timezone}}."

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078000352/original/BnZsQEws5M5qMwSZdU2xsUpz2Slx_knBIQ.png?1786354136)

6

## Sending a Test SMS

Testing helps confirm that the message looks correct before it is used for real rental bookings. This is especially helpful when using custom values, editing templates, or enabling a new notification type.

To send a test SMS:

  1. Open the Rental notification you want to test.
  2. Go to the **SMS** tab.
  3. Review or update the message body.
  4. Enter a test phone number in the **Test SMS (enter phone number with country code)** field.
  5. Include the country code, such as `+1234567890`.
  6. Click **Send a test SMS**.
  7. Review the message on the receiving phone to check merge fields, verify links, and confirm tone and length.
  8. Make any needed edits before saving.


If the test SMS button is unavailable, confirm that a valid phone number is entered and that SMS services are configured for the location.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078000450/original/OOwLcHq-G8WRRK-rA2ZnkZPnFOSEHe5MkQ.png?1786354195)

7

## SMS Setup Requirements

SMS notifications depend on the location's messaging setup. Before enabling Rental SMS notifications, make sure the location is configured to send SMS messages through HighLevel.

Before going live, confirm:

  * The location has SMS sending configured in Settings › Phone & SMS.
  * The sending number is available and properly set up.
  * Recipient phone numbers are valid and include proper country codes.
  * Message content follows your business communication and compliance requirements (e.g., only send to contacts who have opted in to receive SMS).
  * Your provider is not blocking messages for compliance reasons (e.g., missing A2P registration in the US).


SMS usage may be subject to applicable messaging costs and compliance rules based on your account setup and phone configuration. Keep messages short and focused on essential details to minimize cost per segment.

8

## How to Set Up SMS Notifications for Rental Bookings

Proper setup ensures booking updates are sent to the right recipients with the right message. Configure each notification event individually so confirmations, reminders, cancellations, and follow-ups match the communication needs of your business.

Step 1

Open Rentals Global Settings

Go to **Calendars** in HighLevel.

Open **Calendar Settings**.

Select **Rentals**.

Click **Global settings**.

Open **Notifications** to see all rental notification types.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078000672/original/6CXHmBqsJBbft52ADLHAXYv-iB4uZ0xLEg.png?1786354312)

Step 2

Choose a Notification Type to Configure

In the Notifications list, click the **Edit** (pencil) icon next to the event you want to configure (e.g., Reminder or Confirmation).

Step 3

Open the SMS Tab and Enable SMS

Inside the notification editor, select the **SMS** tab.

Toggle the **Disable SMS notifications** switch to **Off** (enabled) for that notification type.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078000975/original/Tmubhg4G_1rUGPjznURCLUWF_XyZ-tYiew.png?1786354476)

Step 4

Select Recipients

Under **Who should receive this notification?** , expand the recipient sections:

  * **Contact** — Check this to send the SMS to the customer/renter.
  * **Business** — Check this to send the SMS to your internal business number.


You can enable one or both recipient options depending on your communication needs.

Step 5

Choose or Edit the SMS Template

Pick an existing SMS template from the **SMS template** dropdown, or use the default template provided (often labeled "None").

Edit the **Message body** as needed, inserting custom values via the merge-field ({ }) picker icon for personalization (e.g., {{contact.name}}, {{rentalBooking.start_time}}).

If different messaging is needed for Contact vs Business, configure each recipient's template separately where the option is available.

Step 6

Configure Timing for Reminders and Follow-Ups (If Applicable)

For **Reminder SMS** : set how long before the booking start time the message should send (e.g., 24 hours, 1 hour).

For **Follow-Up SMS** : set how long after the booking end time it should send (e.g., 2 hours after, next day).

Step 7

Send a Test SMS

Enter a test phone number with country code in the **Test SMS** field (e.g., +12345678900).

Click **Send a test SMS**.

Confirm the message looks correct:

  * Check merge fields
  * Verify links
  * Confirm tone and length


Step 8

Save and Repeat for Other Event Types

Click **Save** to apply your changes to the current notification.

Click **Save changes** on the main Notifications page if required.

Repeat steps 2–7 for any additional event types (e.g., Cancellations, Reschedules) you want to support via SMS.

Success

Once saved, SMS will automatically send whenever the configured rental booking event occurs, following the rules you set in Global Settings.

9

## Troubleshooting SMS Notifications

Troubleshooting helps identify why an SMS notification may not send or why the recipient may not receive the expected message. Start by checking the notification settings, recipient configuration, and SMS setup for the location.

Common things to check:

  * Confirm SMS is enabled for the specific notification event (toggle is Off/enabled, not On/disabled).
  * Confirm the correct recipient option is selected (Contact and/or Business).
  * Check that the message body is not blank.
  * Verify the recipient has a valid phone number with proper country code.
  * Include the country code when sending a test SMS (e.g., +1 for US/Canada).
  * Confirm SMS services are configured for the location in Settings › Phone & SMS.
  * Review contact communication preferences or restrictions where applicable.
  * Send a test SMS before using the notification for live bookings to validate setup.
  * Check that your provider is not blocking messages for compliance reasons (e.g., missing A2P registration).


10

## Frequently Asked Questions

Q: Where do I configure SMS notifications for Rental bookings?

Go to Calendars › Calendar Settings › Rentals › Global settings › Notifications, then edit the notification event and open the SMS tab.

Q: Which Rental booking events support SMS?

SMS can be configured for unconfirmed bookings, confirmations, cancellations, reschedules, reminders, and follow-ups.

Q: Can I choose who receives the SMS?

Yes. You can configure recipients such as the Contact, the Business, or both where available.

Q: Can I customize the SMS message?

Yes. You can edit the message body, select an existing SMS template, and use supported custom values to personalize content.

Q: Can I send a test SMS before saving?

Yes. Enter a test phone number with country code and click "Send a test SMS" to preview the message.

Q: What should I do if the test SMS button is disabled?

Check that a valid phone number with country code is entered and that SMS services are configured for the location.

Q: Do I need to set up SMS separately for each rental listing?

No. SMS notifications are configured at Rentals › Global Settings › Notifications and apply at the booking level across all listings.

Q: Can I send SMS only to my internal team and not to customers?

Yes. For any notification type, you can enable SMS for the Business recipient while leaving Contact unchecked, effectively making that SMS an internal alert.

Q: Can I use different SMS wording for customers and for the business?

Yes. The feature supports per-recipient templates, so the Contact can receive a customer-friendly message while the Business receives a more operational note with extra details.

Q: Are SMS templates required?

You can select an SMS template where available or customize the message body directly. Each notification comes with a default message you can edit.

Q: Do SMS notifications replace email, in-app, or WhatsApp notifications?

No. SMS is an additional channel for Rental booking notifications. Other channels can still be configured separately.

Q: Do SMS messages support custom values?

Yes. Supported custom values can be used to personalize rental booking messages, such as contact or booking details.

11

## Related Articles

  * [Global Settings in Rentals](<https://help.gohighlevel.com/support/solutions/articles/155000006640-global-settings-in-rentals>)
  * [Rentals Calendars - Overview & How to Get Started ](<https://help.gohighlevel.com/support/solutions/articles/155000006649-rentals-calendars-overview-how-to-get-started>)  
  

  * [Calendar: Email, In-App, SMS & WhatsApp Appointment Notifications ](<https://help.gohighlevel.com/support/solutions/articles/155000003441-calendar-email-in-app-sms-whatsapp-appointment-notifications>)  
  

  * [How To Enable/Disable Rentals For Your Locations ](<https://help.gohighlevel.com/support/solutions/articles/155000006740-how-to-enable-disable-rentals-for-your-locations>)  
  

  * [Using Custom Values in Calendars ](<https://help.gohighlevel.com/support/solutions/articles/155000007763-using-custom-values-in-calendars>)  
  

  * [Getting Started: Setup Email, Phone & SMS in HighLevel ](<https://help.gohighlevel.com/support/solutions/articles/155000005058>)[](<https://help.gohighlevel.com/support/solutions/articles/155000006649-rentals-calendars-overview-how-to-get-started>)

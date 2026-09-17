# Client Portal Appointments: Book and Manage Meetings

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008569-client-portal-appointments-book-and-manage-meetings](https://help.gohighlevel.com/support/solutions/articles/155000008569-client-portal-appointments-book-and-manage-meetings)  
**Category:** Client Portal  
**Folder:** Client Portal

---

Client Portal

Client Portal Appointments: Book and Manage Meetings

Let clients book, review, reschedule, and cancel eligible appointments directly from the HighLevel Client Portal.

What You'll Learn

Client Portal Appointments lets clients book, view, and manage meetings without leaving the HighLevel Client Portal. Clients can review appointments in **Today** , **Upcoming** , and **Past** views, use a calendar view, and book from one or more calendars you make available.

Available client information is automatically filled during booking, while businesses remain in control of which calendars accept Client Portal bookings and whether the Appointments app appears in the portal.

Current Availability

**Appointments are currently available only in the new Client Portal UI.** Support for branded apps is coming soon.

Release Scope

This article covers the currently released calendar-based appointment experience. Service-menu booking and additional appointment-related event-management capabilities referenced as future enhancements are not part of the setup documented below.

Table of Contents

1\. What is Client Portal Appointments? 2\. Key Benefits of Client Portal Appointments 3\. Availability and Configuration Requirements 4\. View and Manage Appointments 5\. Book Appointments from the Client Portal 6\. Use Multiple Calendars for Client Portal Booking 7\. How to Set Up Client Portal Appointments 8\. Troubleshooting Client Portal Appointments 9\. Frequently Asked Questions 10\. Related Articles

# **What is Client Portal Appointments?**  
  


Client Portal Appointments brings scheduling directly into the Client Portal so clients can access meetings and booking options from the same place they use for other business resources. Keeping appointment activity inside the portal reduces the need to search through booking links, confirmation emails, or separate scheduling tools.

Once Appointments and at least one eligible calendar are enabled, clients can:

  * View appointments under **Today** , **Upcoming** , and **Past**.
  * Use a calendar view to locate appointments by date.
  * Book new appointments without leaving the Client Portal.
  * Select from one or multiple calendars enabled for Client Portal booking.
  * Review appointment details.
  * Reschedule or cancel eligible appointments.
  * Start another booking after an appointment has been completed.


## **Key Benefits of Client Portal Appointments**  
  


Bringing appointment access and booking into the Client Portal gives clients more control over scheduling while allowing businesses to determine exactly which booking options are available. This creates a more connected self-service experience without changing the calendar rules used to manage availability.

  * **Centralized Appointment Access:** Clients can review and manage appointments from the Client Portal instead of relying only on emails or separate booking links.
  * **Simplified Booking:** Clients can choose an available calendar, date, and time without leaving the portal.
  * **Multiple Calendar Options:** Businesses can make one or several eligible calendars available for clients to choose from.
  * **Less Repeated Data Entry:** Existing client contact information is automatically filled where available during booking.
  * **Appointment Self-Service:** Clients can cancel or reschedule appointments when those actions are permitted by the calendar's policies.
  * **Faster Repeat Booking:** Clients can begin another booking after an appointment has been completed.
  * **Administrative Control:** Businesses control both the Appointments app's visibility and which individual calendars accept Client Portal bookings.


## **Availability and Configuration Requirements**  
  


Client Portal Appointments depends on both the portal experience and calendar-level configuration. Understanding each requirement helps prevent situations where the Appointments app is visible but clients cannot select a calendar or complete a booking.

Requirement| What It Controls| Required?  
---|---|---  
**New Client Portal UI**|  Provides the currently supported Client Portal Appointments experience.| Yes  
**Appointments App Permission**|  Controls whether Appointments appears in the Client Portal navigation.| Yes  
**Client Portal Booking on a Calendar**|  Controls whether that individual calendar appears as a booking option.| Yes, for each calendar  
**Branded Client Portal App**|  Branded-app support is not included in the current release.| Not currently supported  
  
Two-Part Setup

Enabling the Appointments child app does not automatically enable calendar booking. At least one individual calendar must also have **Client Portal booking** enabled.

## **View and Manage Appointments**  
  


Appointment views help clients understand what is happening now, what is scheduled next, and what has already taken place. Clients can also open individual appointments to review meeting information and access the management actions allowed by the calendar's policies.

From **Appointments** in the Client Portal, clients can use **Today** , **Upcoming** , and **Past** to organize their meetings. A calendar view provides another way to locate appointments by date.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080525228/original/qqq_9YFew4gq9Hy6BelIW4UDfXtTSHBHVQ.png?1788971394)

**Screenshot:** Client Portal Appointments page showing the calendar view, Today/Upcoming/Past tabs, appointment cards, and More details links.

### **View Appointment Details and Available Actions**

Opening an appointment gives clients a focused view of the meeting information and any actions currently available. Cancellation and rescheduling options appear only when the appointment remains eligible under the calendar's configured policies.

  1. Open **Appointments** from the Client Portal navigation.
  2. Locate the appointment you want to review.
  3. Click **More details**.
  4. Review the appointment information.
  5. If available, select **Cancel** or **Reschedule**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080525282/original/0cGLDz1m9ov8FthhQR4r6J4Xm9409PAvdg.png?1788971421)

Whether an appointment can be canceled or rescheduled depends on the cancellation and rescheduling rules configured for that calendar. For more information, see [Cancellation & Reschedule Policy (Booking Widget)](<https://help.gohighlevel.com/support/solutions/articles/155000002738-cancellation-reschedule-policy-booking-widget->).

## **Book Appointments from the Client Portal**  
  


The Client Portal booking flow lets clients choose from the calendars you make available and select an eligible date and time without leaving the portal. Existing contact information is automatically filled where available, while the selected calendar continues to determine which dates and times can be booked.

  1. Open **Appointments** in the Client Portal.
  2. Click **Book Appointment**.
  3. Select an available calendar.
  4. Select an available date.
  5. Choose an available time.
  6. Complete the booking.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080525340/original/Z0DyFwUzuPOCTxVAfPeXD1S7Z8DeRPbJxA.png?1788971442)

The dates and times shown to the client are determined by the selected calendar's availability and scheduling rules. Office hours, slot duration, minimum scheduling notice, buffers, appointment limits, existing bookings, and connected-calendar conflicts can affect which time slots appear.

For more information, see [Adjusting Availability Settings for Individual Calendars](<https://help.gohighlevel.com/support/solutions/articles/48001155718>).

## **Use Multiple Calendars for Client Portal Booking**  
  


Enabling multiple calendars gives clients a choice of booking options while allowing you to control exactly which calendars appear in the Client Portal. This is useful when separate calendars represent different appointment types, departments, locations, or team members.

**Client Portal booking is enabled individually for each calendar.** You can enable one calendar or repeat the configuration for each additional calendar clients should be able to select.

Option| Purpose| Required for Multiple Client Portal Calendars?  
---|---|---  
**Client Portal Calendar Selector**|  Displays the individual calendars that have Client Portal booking enabled.| Yes  
**Group Calendar**|  Combines calendars into a separate grouped booking experience under a shared link.| No  
  
A Group Calendar is not required solely to expose several individual calendars through Client Portal Appointments. For more information about Group Calendars, see [HighLevel Group Calendar Overview and Setup Guide](<https://help.gohighlevel.com/support/solutions/articles/48001161037-highlevel-group-calendar-overview>).

## **How to Set Up Client Portal Appointments**  
  


Client Portal Appointments requires configuration in both calendar settings and Client Portal App Permissions. App Permissions controls whether clients can access the Appointments app, while the individual calendar setting determines which calendars can be selected for new bookings.

**Complete both setup steps.** Enabling only the Appointments child app does not make a calendar available, and enabling only a calendar does not make the Appointments app visible.

### **Step 1: Enable Client Portal Booking for a Calendar**

Each calendar must be explicitly enabled for Client Portal booking before clients can select it. This lets you expose only the calendars appropriate for Client Portal users while keeping other calendars unavailable through this booking channel.

  1. Go to **Calendars** and open **Calendar settings**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080525360/original/4Hlu9qVu7dSx77OJiiSz-RvgWFTC-6XgbA.gif?1788971461)

  2. Under **Meetings → Calendars** , locate the calendar you want to make available.
  3. Click the **Edit calendar** icon.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080525458/original/zcXDyWkEXx7ZFxkRVdyCFFJVft_HPAINZQ.png?1788971548)

  4. In the calendar editor, expand **Advanced settings**.
  5. Select **Booking channels**.
  6. Turn on **Client Portal booking**.
  7. Click **Save changes**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080525528/original/lG-JMQVf0wBx0UvHA0frdE19Y7KrTQ3WDw.png?1788971589)

Repeat these steps for every additional calendar clients should be able to select when booking through the Client Portal.

### **Step 2: Enable Appointments in Client Portal App Permissions**

Enabling the Appointments child app makes the appointment experience visible inside the Client Portal. App Permissions are configured at the sub-account level, so the selected child-app visibility applies to contacts using that sub-account's Client Portal.

  1. Go to **Memberships**.
  2. Open **Client Portal**.
  3. Select **Settings**.
  4. Open **App Permissions**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080525542/original/mnjZJ-E2lap5gbw2NVQ0GtQrcXyXIBOK0A.png?1788971616)

  5. Locate **Appointments** in the child-app list.
  6. Enable **Appointments**.
  7. Click **Save Settings**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080525579/original/hVk_lHQtBAVXmfKv_RUaaUq9spsP5zs9FQ.png?1788971652)

**Important:** Enabling Appointments in App Permissions does not automatically make every calendar available for booking. Each calendar you want clients to select must also have **Client Portal booking** enabled under its Booking channels settings.

For more information about controlling Client Portal apps, see [App Permissions in Client Portal: Enabling/Disabling Child Apps and Authentication](<https://help.gohighlevel.com/support/solutions/articles/155000002136-app-permissions-in-client-portal-enabling-disabling-a-child-app>).

## **Troubleshooting Client Portal Appointments**  
  


Most Client Portal appointment issues are caused by one of the two required permissions, an individual calendar rule, or use of an unsupported portal experience. Compare the client's experience with the checks below before changing the calendar or recreating an appointment.

Issue| What to Check  
---|---  
**Appointments does not appear in the portal**|  Confirm the client is using the new Client Portal, Appointments is enabled in App Permissions, and the changes were saved.  
**Appointments appears, but no calendars are available**|  Enable Client Portal booking under Advanced settings → Booking channels for at least one individual calendar.  
**A calendar appears, but a time slot is missing**|  Review availability, scheduling notice, buffers, appointment limits, existing bookings, and connected-calendar conflicts.  
**Cancel or Reschedule is unavailable**|  Review whether the calendar permits the action and whether its cancellation or rescheduling restriction window has passed.  
**The time-zone selector is missing**|  Check whether Disable Contact Timezone is enabled for the sub-account.  
**A recent permission change is not visible**|  Confirm the change was saved, then have the client refresh the portal or sign out and sign back in.  
  
## **Frequently Asked Questions**  
  


Q: Does enabling Appointments automatically make every calendar available?

No. Enabling Appointments makes the app visible, but each calendar must separately have **Client Portal booking** enabled under **Advanced settings → Booking channels**.

Q: Can I make only certain calendars available in the Client Portal?

Yes. Client Portal booking is enabled individually, allowing you to select exactly which calendars clients can choose from.

Q: Do I need to create a Group Calendar to show multiple calendars?

No. The Client Portal can display multiple individually enabled calendars through its calendar selector. Group Calendars are a separate grouped booking feature.

Q: Do the calendar's existing availability rules still apply?

Yes. The Client Portal booking flow uses the selected calendar's availability and scheduling rules when determining which dates and times clients can book.

Q: Can Appointments be enabled for only one client?

App Permissions are configured at the sub-account level. Enabling or disabling Appointments controls its visibility for contacts using that sub-account's Client Portal rather than for one individual contact.

Q: What happens if I disable the Appointments child app later?

Appointments is removed from the Client Portal experience, but the calendars and appointment records configured elsewhere in HighLevel are not deleted. You can re-enable the app later.

Q: Are Client Portal Appointments available in branded apps?

Not in the current release. Client Portal Appointments is currently available only in the new Client Portal UI.

Q: Can clients book services or use additional event-management features from this screen?

The current release covers standard calendar-based appointments. Service-menu booking and additional appointment-related event-management capabilities are outside the workflow documented in this article.

### **Related Articles**  
  


[App Permissions in Client Portal: Enabling/Disabling Child Apps and Authentication](<https://help.gohighlevel.com/support/solutions/articles/155000002136-app-permissions-in-client-portal-enabling-disabling-a-child-app>) [How to Set Up a Booking Calendar in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000005061>) [Cancellation & Reschedule Policy (Booking Widget)](<https://help.gohighlevel.com/support/solutions/articles/155000002738-cancellation-reschedule-policy-booking-widget->) [Adjusting Availability Settings for Individual Calendars](<https://help.gohighlevel.com/support/solutions/articles/48001155718>) [Disable Contact Timezone - How to Remove Ability to Adjust Timezones When Scheduling](<https://help.gohighlevel.com/support/solutions/articles/48000982200-disable-contact-timezone-how-to-remove-ability-to-adjust-timezones-when-scheduling>) [Unified Client Portal Experience](<https://help.gohighlevel.com/support/solutions/articles/155000008402-unified-client-portal-experience>)

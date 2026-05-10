# List of all outgoing system generated emails

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001209235-list-of-all-outgoing-system-generated-emails](https://help.gohighlevel.com/support/solutions/articles/48001209235-list-of-all-outgoing-system-generated-emails)  
**Category:** Email  
**Folder:** General

---

Email Reference

List of All Outgoing System Emails

A complete reference of every system-generated email — what it is, what triggers it, and how to disable it where possible.

What You'll Learn

Every outgoing system email the platform sends, organized by scope. **Sub-Account / Location Level** emails are tied to individual locations (appointments, reviews, social planner, payments). **Agency Level** emails are sent from the agency itself (password resets, user provisioning, payment failures, registration status).

Table of Contents

1

Sub-Account / Location Level Emails

2

Invoice & Payment Notification Emails

3

Agency Level Emails

4

A2P & Toll Free Verification Notifications

5

Frequently Asked Questions

6

Additional Resources

1

## Sub-Account / Location Level Emails

Email 1.1

New Appointment Request

Sent from the **Unassigned Calendar** and the **Group Calendar** when someone books an appointment.

![New Appointment Request notification email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48252656817/original/HaUAl_kuzcg5njAp7EfZN7bRcJJFQtvlAA.png?1663872783)

Note on Sender

If you're wondering why calendar emails are being sent from no-reply@support.domain.com, it's likely due to default sender settings. [Learn how Calendar Email Sender Addresses work](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>).

How to Disable

Disable "New Appointment Requests" for assigned users in Group Calendars

Open **Locations Settings → Calendar Settings** , open the calendar, click the **3\. Confirmation** tab, and save.

![Disable New Appointment Requests on a Group Calendar](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48252827089/original/4raiJ9DfsyCZUproWQAFBU8qdbUXaC_Rsg.png?1663941035)

How to Disable

Disable "New Appointment Requests" in Unassigned Calendar

Open **Locations Settings → Calendar Settings** , open the calendar, click the **3\. Confirmation** tab, remove the email(s), and save.

![Remove emails from the Unassigned Calendar Confirmation tab](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48252827085/original/kfcgFMaRBedVPmRfd5hoeEZnQrEu377X3g.png?1663941034)

![Confirmation tab settings on Unassigned Calendar](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48253316570/original/75I9IfgNAJbDy9tDhOm2aqsOA__d6jBTkA.png?1664264542)

Please Note

If the calendar settings for _auto confirmation_ and _send appointment alert emails_ are enabled, appointment owners will still receive appointment request emails. The development team is rolling out a fix in an upcoming calendar update.

Email 1.2 · Can be disabled

Appointment Review Request — Email & SMS

Sent to a contact after an appointment, asking them to leave a review.

![Appointment Review Request email and SMS](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48189218359/original/Zfqpk9L21fqO1a6BE3-xQ4di5penLhmFgg.png?1644563046)

Please Note

When sending a review request, the **signed-in user** is listed as the sender of the message.

![Signed-in user shown as the sender on a review request](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48252650500/original/a7pwrO-vCEj6bTZ0G_T1PAo_w_QdbBZkSw.png?1663870327)

If you want to send a review request from the **contact's assigned user** , use the Workflows action _"Send Review Request"_ instead — it sends the request on behalf of the assigned user.

![Workflow Send Review Request action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029814545/original/qnBAl7pqUO17YV4BxidTCsidG3PayKMOdw.jpg?1721830376)

Email 1.3 · Can be disabled

Social Planner — Reconnect Expired Token Notification

Sent when a connected social account's auth token expires and needs to be reconnected.

![Social Planner reconnect expired token notification — example 1](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48253062195/original/B_kRBa1B1MtPI1vRxlOyEYdimetXLwFedQ.png?1664178280)

![Social Planner reconnect expired token notification — example 2](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48253062801/original/U1UqfGwWPmfJ5r25Kd52CW4jpu5O_-Yamg.png?1664178471)

![Social Planner reconnect expired token notification — example 3](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48253069352/original/yvegNEM8_ctEjA13OkqVlg6bk3-Ft4m3SA.png?1664179997)

Please Note

When sending an email notification, the **signed-in user** is listed as the sender of the message.

Email 1.4 · Can be disabled

New Review Email

Sent when a new public review is submitted on one of the location's connected platforms.

![New review notification email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48189208813/original/G4qVenOaP3CWDAM6Xa8LK21SGcrUUMz_Zg.png?1644562058)

2

## Invoice & Payment Notification Emails

Two audiences receive invoice-related emails: the **business / sub-account** (for failures and skips that need attention) and the **end customer** (for invoice receipts, successful payments, and upcoming auto-payments).

Audience

For the business / sub-account

Email 2.1

Invoice payment attempt failed for the end customer

![Invoice payment attempt failed — sent to the business](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029814237/original/FRnmN6T8fDG3dFeYg4nVBJLqlussGThM0g.jpg?1721830175)

Email 2.2

Invoice payment successful by end customer

![Invoice payment successful — sent to the business](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029814039/original/e_a43i2g--_4y5mlcwv3iT7YZW4BJbMfdA.jpg?1721830058)

Email 2.3

Error in auto-payment of a recurring template

![Error in auto-payment of a recurring template](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029813971/original/2J7_puL8ozxkIlHbqK8Gq7b55ECMr2nLfA.jpg?1721830007)

Email 2.4

Skipping auto-payment because the invoice amount was manually updated

![Skipping auto-payment because amount was manually updated](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029813924/original/jdFlKe9-3j_Fpno-iAvpEN8scEZagEdYMg.jpg?1721829967)

Audience

For the end customer

Email 2.5

Invoice received

![End customer — invoice received](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029812903/original/Bb4fH2Ebn6GdGUWxMb5hlQ6Ms7RZSHhoGQ.jpg?1721829377)

Email 2.6

Payment for an invoice is successful

![End customer — payment successful](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029812820/original/FRvZXinN01kA1nyI1dwH2jaxBB5tdELB5w.jpg?1721829316)

Email 2.7

Payment attempt for an invoice has failed

![End customer — payment attempt failed](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029812301/original/bye8zPVJW1OiR9aHQaC0YlfMjLb4AJ31SQ.jpg?1721828962)

Email 2.8

Upcoming auto-payment information

![End customer — upcoming auto-payment notice](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029812267/original/Pv_YVUQa6ul5B8HQK0PlH9lxQQeBWDRm-g.jpg?1721828923)

Email 2.9

Auto-payment failed for a recurring template

![End customer — auto-payment failed for recurring template](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029812081/original/zXgHSVUj31Fg9p7jcpl_9K_5zM8fJDB09Q.jpg?1721828780)

3

## Agency Level Emails

Email 3.1

Reset Password

Sent when a user requests a password reset from the login page.

![Reset Password email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029811938/original/QX5Rvdq9jNa2Z2NttWlthUQSgrP7AqLBIg.jpg?1721828685)

Email 3.2

Verification Code Email

Sent during sign-in when an additional verification code is required.

![Verification code email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029811879/original/pyOXMZ8vHCWdO9OAe26Xuu0bd7SvR8cfXw.jpg?1721828652)

Email 3.3 — Variant A

New User Email Notification — to the agency

Notifies the agency when a user is added to an agency account or a sub-account.

![Agency notification when a user is added](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48189212059/original/W3ejvk7Io-eKoZ9aKIiBjwjILuQ1DD3wkg.png?1644562368)

Email 3.3 — Variant B

New User Welcome — username & password

Sent to a newly-provisioned user with their username and password.

![New user welcome with credentials](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48189214634/original/LtfzuABjvbIWmu7va-XwqMnRSgADUWNtbg.png?1644562602)

Email 3.3 — Variant C

Agency notified of a new SaaS sale

Sent to the agency when a SaaS plan signup occurs.

![Agency notification of a new SaaS sale](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48189215119/original/R266vIgYMCL2wUCMWsqAzPsVZsM4Cp3QFA.png?1644562707)

Email 3.4

Payment Failed for the Client

Sent to the agency when a client's recurring SaaS payment fails to process.

![Payment failed for the client](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48189204118/original/OTGSUgFaZBbGPGOw4lzAHWy8mghNuXnU4Q.png?1644561544)

Email 3.5

New YEXT Sale — Internal Email

Internal-only notification sent to the agency when a YEXT listing service is purchased.

![New YEXT sale internal notification](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48189205286/original/DEkzpBjD94xC9jPPKqAN-uVBBKlb7iakxg.png?1644561720)

4

## A2P & Toll Free Verification Notifications

A2P and Toll Free registration status updates are emailed to the **agency owner** and **admins** , sent from noreply@donotreply.leadconnectorhq.com.

Notifications fire on these status updates from the carriers:

**A2P Brand** — Rejection, Approvals

**A2P Campaign** — Submitted, Rejection, Approvals

**Toll Free** — Submitted, Pending Review, Rejections, Approvals

![A2P / Toll Free verification status email — sample 1](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029811639/original/umlvv8vgTjlQgIs_znfJnZ97wPb2VUOMng.jpg?1721828484)

![A2P / Toll Free verification status email — sample 2](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029811606/original/PRE1KB3STKEp90VD4Fk0CLwTGxSr_6FQcQ.jpg?1721828453)

![A2P / Toll Free verification status email — sample 3](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029811251/original/puUfhZEobdr3AE7FTK1ysZpOunddwXFcpA.jpg?1721828226)

5

## Frequently Asked Questions

Q: Can I disable every system email?

Not all of them. Emails marked _Can be disabled_ in this article have a setting that controls them. Reset Password, Verification Code, and credentialed New User emails are essential for account access and cannot be turned off.

Q: Why is the calendar email coming from no-reply@support.domain.com instead of my own address?

That's the default sender used when no Mailgun subdomain or SMTP integration is configured for the location. Read the [Calendar Email Sender Addresses](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>) guide to set up your own sender domain.

Q: Who is shown as the sender on review request emails?

The signed-in user is listed as the sender by default. To send from the contact's **assigned user** , use the Workflows action _Send Review Request_ instead — it sends on the assigned user's behalf.

Q: Are invoice emails sent to the business and the customer at the same time?

They're separate notification streams. The business gets summary emails on failures, successes, and skipped auto-payments; the end customer gets receipts, payment confirmations, upcoming auto-payment notices, and failure notifications addressed to them. Same triggering events, different recipients.

Q: Who receives A2P and Toll Free verification emails?

Agency owners and admins. They're sent from noreply@donotreply.leadconnectorhq.com and cannot be redirected to a different recipient.

Q: Can I customize the look and content of these system emails?

Most account-level emails (Reset Password, Verification Code, New User) cannot be customized. Sub-account emails like Appointment Confirmations and Review Requests can be tailored from their respective settings pages, and onboarding emails can be customized — see the linked guide in Additional Resources.

Q: My users aren't receiving system emails — what should I check?

Verify the email address is correct on the user record, check spam/junk folders (especially for password resets), confirm the user's email domain isn't blocking the sender, and confirm any agency-level email settings haven't disabled the specific notification.

Additional Resources

[How to Customize the Onboarding Email Sent to New Sub-Account Users](<https://help.gohighlevel.com/support/solutions/articles/155000001317-how-to-customize-the-onboarding-email-that-is-sent-to-new-sub-account-users->) [How to Send New Membership Users Custom Emails with Login Information](<https://help.gohighlevel.com/support/solutions/articles/48001147956-how-to-send-new-membership-users-custom-emails-with-their-login-information>) [How to Use the Email Builder and its In-line Editor](<https://help.gohighlevel.com/support/solutions/articles/155000000087-how-to-use-the-email-builder-and-its-in-line-editor>) [How Calendar Email Sender Addresses Work](<https://help.gohighlevel.com/en/support/solutions/articles/48000979925>)

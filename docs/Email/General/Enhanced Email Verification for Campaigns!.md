# Enhanced Email Verification for Campaigns!

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003090-enhanced-email-verification-for-campaigns-](https://help.gohighlevel.com/support/solutions/articles/155000003090-enhanced-email-verification-for-campaigns-)  
**Category:** Email  
**Folder:** General

---

Email Compliance

Verify Your From Email Address Before Sending Campaigns

A short OTP-based check that protects your sender reputation and prevents anyone from spoofing your email address.

What Changed

Previously, From email addresses on campaigns were not verified. That oversight made identity spoofing possible and could damage sender reputation.

To enhance security, we now require verification of your **From email address** before sending an email campaign. Only valid, verified addresses can be used — preventing anyone from spoofing your sender identity.

Table of Contents

1

When Verification Is Not Required

2

How to Verify Your Email

3

Verify From the Settings Page

4

Frequently Asked Questions

Video Walkthrough

1

## When Verification Is Not Required

Two cases skip the OTP verification step:

Exception 1

Custom domains provided under LC Email

If your sending domain is one of the custom domains issued under LC Email, ownership is already verified and the From address is trusted automatically.

Exception 2

Location admin email present in settings

If the From address matches the Location admin email already saved in your settings, it's treated as verified — no OTP required.

2

## How to Verify Your Email

Step 1

Open Email Marketing and create a campaign

Navigate to **Email Marketing** and start a new campaign.

Step 2

Enter the email you want to verify

In the sender email field, type the address you'd like to use as the From address.

Step 3

Click "Verify Now"

A **Verify Now** button appears next to the unverified address. Click it to trigger the OTP email.

![Sender email field with the Verify Now button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031199950/original/kaNwiSY0fmopj5MlBf7bYD_wdR0NYuUzDA.png?1723866095)

Step 4

Enter the 6-digit OTP from your inbox

Open the email at the address you entered, copy the 6-digit One-Time Password, and paste it into the verification dialog.

![OTP entry screen for email verification](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031199951/original/ckUZs8FxIzpfRLvjOS8JZmn-TUUZvrIAsQ.png?1723866095)

Step 5

Done — your email is verified

Once the OTP is accepted, the address is verified and can be used as the From email for any future campaign.

You're All Set

Verified addresses persist across all your campaigns — you only need to verify each address once.

3

## Verify From the Settings Page

You can verify an address before you start a campaign by going to the settings page and clicking **Verify an email**. The OTP flow is identical to the in-campaign one.

![Verify an email from the settings page](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031199952/original/8plDBApPogd_CPPjESiBP3Bmm06Kyd2WRQ.jpeg?1723866095)

4

## Frequently Asked Questions

Q: Why is email verification required now?

Without verification, anyone could enter any email address in the From field — including domains they don't own. That opens the door to identity spoofing and damages your sender reputation. Verifying ownership of the From address closes that loophole.

Q: How long does the OTP stay valid?

OTPs expire after a short window for security. If yours expires, click **Verify Now** again to receive a fresh code.

Q: I didn't receive the OTP — what should I check?

Check your spam folder, confirm the email address was typed correctly, and make sure your inbox isn't filtering messages from no-reply senders. If it still doesn't arrive after a minute, request a new OTP.

Q: Do I need to verify the same email more than once?

No. Once an address is verified, it's marked as verified for your account and can be used for any future campaign without going through OTP again.

Q: Can I verify multiple From addresses?

Yes. Repeat the verification flow for each address you'd like to use. All verified addresses appear in the sender email dropdown the next time you build a campaign.

Q: Does verification apply to workflow Send Email actions too?

This requirement is enforced on email **campaigns**. Workflow-driven sends follow the configured workflow sender address. If you'd like the same protection on workflow emails, verify the From address you use there as well.

Q: My campaign won't send and says the address isn't verified — what now?

Open the campaign, click **Verify Now** next to the From address, complete the OTP flow, and resend. You can also verify ahead of time from **Settings → Verify an email**.

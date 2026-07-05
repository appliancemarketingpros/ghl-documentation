# Send Test Email Error in Campaign's Email step: An error occurred, please try again

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001155002-send-test-email-error-in-campaign-s-email-step-an-error-occurred-please-try-again](https://help.gohighlevel.com/support/solutions/articles/48001155002-send-test-email-error-in-campaign-s-email-step-an-error-occurred-please-try-again)  
**Category:** Email  
**Folder:** Troubleshooting Email

---

Workflow Automation

Send Email Trigger Action Not Firing

A quick checklist for the most common reasons a Send Email action in a workflow silently fails to fire.

Overview

If you see the error below, or the Send Email trigger action just isn't firing, work through the checks in this article to find and fix the cause.

Table of Contents

1

The Error

2

Troubleshooting Checklist

3

FAQ

1

## The Error

If you see this error message, or the Send Email trigger action is not firing at all, work through the checklist below.

![Send Email trigger action error message](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48283729294/original/3bUMFoidpu7Vm4OpR7NqHHyKGtvS9em_bA.png?1677268053)

2

## Troubleshooting Checklist: Please Check If…

Check 1

Merge field syntax in the email/SMS content

Check the email or SMS content for a **missing }** or for **overusing {{{**.

Check 2

Custom values are valid

Especially the links — see the [list of valid custom values](<https://gohighlevelassist.freshdesk.com/support/solutions/articles/48001078171-custom-values-merge-fields>).

![Example of custom values](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48054130934/original/du8IHP5qTYEaAkFDIyC-2fTUe9xhjhdOTg.png?1597456147)

Check 3

Email addresses are valid

For example: `test@gmail,com` with a comma instead of a dot will cause the action to fail.

Check 4

The From field is a valid email address format

For example, change `ABC company` to its actual email address, like [info@abccompany.com](<mailto:info@abccompany.com>).

![From field formatted as an email address](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48054130847/original/neWcoOfxnrs8lrS3TBPg6Jokou4hu4qoCg.png?1597455849)

3

## FAQ

Q: What does "missing }" or "overusing {{{" actually mean?

Merge fields use double curly braces, like `{{contact.first_name}}`. If a closing brace is missing, or if there's an extra opening brace (three instead of two), the parser can't resolve the merge field and the action fails to fire.

Q: Where do I find the list of valid custom values?

See the [list of valid custom values](<https://gohighlevelassist.freshdesk.com/support/solutions/articles/48001078171-custom-values-merge-fields>) linked in Check 2 above — it covers the supported syntax and naming.

Q: Will one bad custom value break the whole email, or just that line?

A single invalid or malformed custom value can prevent the entire action from firing, not just the line it's on. That's why it's worth checking every merge field and custom value in the email, not just the ones you suspect.

Q: Does the From Name need to match the From Email exactly?

No, but the From field itself must contain a properly formatted email address — not a company name or plain text. A display name alongside a valid email is fine; a name with no email is not.

Q: I checked all four items and the email still isn't sending — what next?

Double-check the workflow's trigger conditions and any preceding steps that might be preventing the contact from reaching this action, then reach out to support with the workflow name and a screenshot of the error for further investigation.

Q: Does this checklist apply to Send SMS actions too?

Yes — merge field syntax and custom value validity (Checks 1 and 2) apply the same way to Send SMS actions. Checks 3 and 4 are specific to email since they involve email address formatting.

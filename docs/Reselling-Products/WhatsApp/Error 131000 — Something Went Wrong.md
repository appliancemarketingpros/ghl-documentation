# Error 131000 — Something Went Wrong

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007939-error-131000-something-went-wrong](https://help.gohighlevel.com/support/solutions/articles/155000007939-error-131000-something-went-wrong)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

Troubleshooting GuideError 131000 — Something Went WrongUnderstand why WhatsApp messages fail with error code 131000, what causes it, and how to diagnose and resolve it step by step.  
---  
What you'll learn| + What error 131000 means| + All known causes| + How to diagnose it| + Step-by-step resolution  
---|---|---|---  
  
* * *

**TABLE OF CONTENTS**

  * What is Error 131000?
  * Known Causes
  * How to Resolve It
  * How to Prevent It
  * Related Error Codes
  * Frequently Asked Questions


* * *

What is Error 131000?Something Went Wrong — a catch-all internal server error returned when the WhatsApp API fails for an unknown reason  
---  
  
Error **131000** is a WhatsApp Cloud API error officially titled **"Something Went Wrong"**. It is returned as an **HTTP 500 Internal Server Error** when a message fails to send due to an unknown or unspecified reason on Meta's end — or when something in your account configuration, access token, template, or API request has caused the system to fail in a way it cannot describe more specifically.

This is what the error looks like in the API response:
    
    
    "errors": [
      {
        "code": 131000,
        "title": "Something Went Wrong",
        "message": "Message failed to send due to an unknown error."
      }
    ]

Error 131000 is a **catch-all error** — it covers multiple different underlying causes that all surface the same generic message. Because Meta does not return a more specific reason, diagnosing the root cause requires checking several areas of your account and API setup systematically.
    
    
    **According to Meta's official documentation:** Error 131000 can occur when the API fails to process the signature for a business public key, when a GraphQL request fails, when the GraphQL endpoint returns an error, or during temporary server-side outages. It can also be triggered by configuration issues on your account.

* * *

Known CausesAll confirmed and commonly reported reasons for this error  
---  
1\. Temporary Meta server issue or outageError 131000 is often a transient error caused by a temporary problem on Meta's servers. If the WhatsApp Business Platform is experiencing downtime, degraded performance, or maintenance, this error may appear across all messages regardless of your configuration. This is typically the first cause to rule out.  
---  
2\. Expired or invalid access tokenThe access token used to authenticate API requests has expired, been revoked, or does not include the required permissions — specifically `whatsapp_business_management` and `whatsapp_business_messaging`. An invalid token can cause API calls to fail with error 131000 instead of a more specific auth error.  
---  
3\. WhatsApp Business Account (WABA) is restricted or flaggedIf your WABA is in a restricted, flagged, or limited state — due to a policy violation, low quality rating, or pending review — messages may fail with error 131000 instead of returning a more specific account error code.  
---  
4\. Template not approved or in an invalid stateAttempting to send a template that is still **In Review** , **Rejected** , **Paused** , or **Disabled** can cause error 131000. Similarly, using a template name or language code that does not match the approved template in Meta Business Manager can trigger this error.  
---  
5\. Attempting to send a free-form message outside the 24-hour windowIf more than 24 hours have passed since the recipient last messaged you and you try to send a free-form (non-template) message, the API may return error 131000. Outside the customer service window, only approved template messages can be sent.  
---  
6\. Invalid or malformed phone numberThe recipient's phone number is missing the country code, contains spaces or special characters, or is otherwise incorrectly formatted. The API may return error 131000 for malformed numbers rather than a more specific validation error.  
---  
7\. Business public key signature failure or GraphQL endpoint errorAs documented by Meta, error 131000 can be triggered when the API fails to process the signature when setting a business public key, when a request to the GraphQL endpoint fails, or when the GraphQL endpoint returns an error. This is typically a Meta-side infrastructure issue.  
---  
8\. App or API configuration issueAn incorrect configuration in the Meta Developer app — such as a misconfigured webhook, a stale system user token, or a mismatch between the phone number ID and the app — can cause error 131000 when sending messages.  
---  
  
* * *

How to Resolve ItWork through these steps in order to identify and fix the issue  
---  
  
Step 1 **Check Meta's platform status for an active outage**

Visit [metastatus.com/whatsapp-business-api](<https://metastatus.com/whatsapp-business-api>) to check if WhatsApp's servers are experiencing an outage or degraded performance. If there is an active incident, **wait for Meta to resolve it** before retrying. Do not continue troubleshooting account-specific settings if a platform-wide outage is confirmed — the error will resolve itself once the incident is cleared.

Step 2 **Retry the message after a short wait**

If no outage is reported, wait a few minutes and retry the message. Error 131000 is often a temporary server-side failure that resolves on its own. If the error occurs only once or intermittently, a simple retry is often sufficient. If it persists consistently, continue to the next steps.

Step 3 **Verify your access token is valid and has the correct permissions**

Go to the **Meta Access Token Debugger** at [developers.facebook.com/tools/debug/accesstoken](<https://developers.facebook.com/tools/debug/accesstoken/>) and paste your token. Confirm:

| The token is valid and has not expired  
---  
| The token includes both `whatsapp_business_management` and `whatsapp_business_messaging` permissions  
---  
| The token is a **permanent system user token** — not a short-lived user token that expires after hours  
---  
  
If the token is expired or missing permissions, generate a new permanent access token in the Meta Developer dashboard and update your CRM integration with the new token.

Step 4 **Check your WhatsApp Business Account status**

Log in to **Meta Business Suite** and go to your WhatsApp Business Account. Check that:

| Your WABA status is **Active** — not Restricted, Flagged, or Disabled  
---  
| Your phone number status is **Connected** and its quality rating is not Red  
---  
| There are no policy violation notifications or pending actions on your account  
---  
  
Step 5 **Verify the template status and configuration**

In your CRM or Meta Business Manager, go to **Message Templates** and confirm that the template you are using is:

| Status is **Active** — not In Review, Rejected, Paused, or Disabled  
---  
| The template name in your API request exactly matches the name in Meta Business Manager (case-sensitive)  
---  
| The language code in your request matches the approved template language exactly (e.g. `en_US` not `en`)  
---  
  
Step 6 **Verify the recipient phone number format**

Confirm the recipient number includes the correct **international country code** with no spaces, hyphens, or special characters. For example, a US number should be formatted as `15551234567` — not `+1 (555) 123-4567`. Also confirm the number is registered on WhatsApp by testing with a different known-valid number.

Step 7 **If persistent — try the known workaround: create a new app in the Meta Developer Console**

If all the above checks pass and the error persists, this workaround has resolved the issue for many users and is confirmed by the Meta Developer community:

| 1 Create a new app in the **Meta Developer Console** at [developers.facebook.com](<https://developers.facebook.com>)  
---  
| 2 Add your phone numbers and templates to the new app  
---  
| 3 Generate a new **permanent access token** for the new app  
---  
| 4 Reconfigure your webhook to point to the new app  
---  
| 5 Update your CRM integration with the new token and app configuration, then test  
---  
      
    
    This workaround has been verified by the Meta Developer community and resolves the error for the majority of persistent 131000 cases. It addresses underlying configuration or app-level corruption that cannot be fixed by simply updating tokens.

Step 8 **Contact support if the error persists**

If none of the above steps resolve the issue, contact our support team with the following information so we can escalate to Meta:

  * The exact API request payload that is failing
  * The full API error response including any `fbtrace_id` values
  * The timestamp of when the error first appeared and how frequently it occurs
  * Whether the error is isolated to specific templates, numbers, or recipients
  * Confirmation of which steps above you have already completed

  
---  
  
* * *

How to Prevent ItBest practices to reduce the likelihood of encountering error 131000  
---  
| **Use a permanent system user token** — short-lived tokens expire and can cause authentication failures. Generate a permanent token via Meta's System Users to avoid intermittent auth-related errors  
---  
| **Monitor your WABA health regularly** — check your account status, phone number quality rating, and any policy notifications in Meta Business Suite to catch restrictions before they block messaging  
---  
| **Always use approved templates for outbound messages** — only send template messages to contacts who are outside the 24-hour customer service window. Attempting free-form messages outside this window can cause failures  
---  
| **Implement retry logic with exponential backoff** — since error 131000 is often transient, build retry logic into your API integration that waits progressively longer between retries rather than hammering the API immediately  
---  
| **Validate phone number formats before sending** — ensure all recipient numbers are in the correct international format before submitting them to the API  
---  
| **Subscribe to Meta's status page alerts** — set up notifications at [metastatus.com](<https://metastatus.com>) so you are informed immediately when WhatsApp's platform experiences an outage  
---  
  
* * *

Related Error CodesOther errors you may encounter in similar situations  
---  
Error Code| Title| Description  
---|---|---  
131005| Access Denied| Permission is either not granted or has been removed. Check your access token permissions.  
131031| Account Locked| Your WABA has been restricted or disabled for violating a platform policy.  
131047| Re-engagement Message| More than 24 hours have passed since the recipient last replied. Use a template message instead of a free-form message.  
132001| Template Does Not Exist| The template does not exist in the specified language or has not been approved yet.  
1| API Unknown| Invalid request or possible server error. Check the WhatsApp Business Platform Status page and verify your request format.  
  
* * *

Frequently Asked QuestionsCommon questions about error 131000  
---  
Q: Error 131000 appeared suddenly and everything was working before — what happened?Sudden appearance of error 131000 with no changes on your end is most commonly caused by a temporary Meta server issue or a short-lived platform outage. Check the Meta status page first. If no outage is reported, verify your access token has not expired and your WABA is still in good standing. This error can also appear suddenly when Meta makes infrastructure changes that affect specific app configurations.  
---  
Q: Should I retry immediately when I get error 131000?Yes — a short wait and retry is the first step for error 131000, as it is often a transient server-side error. However, do not retry in a tight loop. Wait at least 30–60 seconds before the first retry, and use exponential backoff for subsequent attempts. If the error persists after several retries, begin investigating the specific causes listed in this article.  
---  
Q: Will I be charged for messages that return error 131000?No. Messages that fail before delivery do not open a conversation and are not billed. You will not be charged for any message that returns error 131000.  
---  
Q: Error 131000 is only happening to one specific recipient — is it their issue?If the error is isolated to a single contact, it is more likely a recipient-side issue — such as the number not being on WhatsApp, the 24-hour window having expired, or an invalid number format. Try sending a template message to the same number and also test with a different known-valid recipient to confirm whether the issue is specific to that contact or broader.  
---  
Q: Meta has no official fix for this error — what can I actually do?That is correct — Meta classifies 131000 as a generic unknown error and does not publish a guaranteed fix. However, the steps in this article — particularly checking the access token, WABA status, and template health, and if needed creating a new app and reconfiguring the token and webhook — have resolved the issue for the majority of users who have reported it. If all else fails, open a Direct Support ticket with Meta providing the `fbtrace_id` from the error response.  
---  
Quick SummaryError 131000 is a generic HTTP 500 failure that covers multiple root causes. Start by checking Meta's platform status for an outage, then wait and retry. If it persists, verify your access token, WABA status, template health, and phone number format. If all checks pass, the confirmed community workaround is to create a new app in the Meta Developer Console and reconfigure your token and webhook. Contact support with your `fbtrace_id` if the issue continues.  
---

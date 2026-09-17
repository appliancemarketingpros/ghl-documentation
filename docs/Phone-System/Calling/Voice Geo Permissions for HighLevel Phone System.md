# Voice Geo Permissions for HighLevel Phone System

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981435-voice-geo-permissions-for-highlevel-phone-system](https://help.gohighlevel.com/support/solutions/articles/48000981435-voice-geo-permissions-for-highlevel-phone-system)  
**Category:** Phone System  
**Folder:** Calling

---

Phone System Security

# Voice Geo Permissions for HighLevel Phone System

Control which countries your HighLevel location can call to reduce toll fraud risk and unexpected international charges.

What You'll Learn

This article explains how Voice Geo Permissions work, how they protect your account, and how to request changes for LC Phone or manage them directly in Twilio for non-LC accounts.

You'll learn which countries are enabled automatically, how to request permission for additional destinations, and how to troubleshoot calls blocked by geographic restrictions.

Table of Contents

1

What Are Voice Geo Permissions?

2

Why Voice Geo Permissions Are Used

3

Countries Automatically Enabled for LC Phone Voice

4

How to Request Changes to LC Phone Geo Permissions

5

Managing Geo Permissions for Twilio / Non-LC Phone Accounts

6

Troubleshooting Calls Blocked by Geo Permissions

7

Related Articles

8

Frequently Asked Questions

1

## What Are Voice Geo Permissions?

Voice Geo Permissions control which countries a HighLevel location can call. Limiting access to only the destinations a business actually needs helps reduce the risk of unauthorized international calling, toll fraud, and unexpected charges.

By default, HighLevel enables common calling destinations based on your location's business profile and phone number ownership. Higher-risk destinations may require manual approval through support or direct configuration in Twilio for non-LC Phone accounts.

2

## Why Voice Geo Permissions Are Used

International calling fraud—also known as toll fraud—occurs when unauthorized users gain access to a phone system and place calls to premium-rate or high-cost international destinations. Without geographic restrictions, compromised accounts can generate thousands of dollars in fraudulent charges within hours.

Voice Geo Permissions mitigate this risk by limiting outbound calling to approved destinations. If an account is compromised, attackers cannot exploit it to dial unauthorized countries, significantly reducing financial exposure and service disruptions.

Important

Only enable countries your business actively needs. Broader international calling access can increase exposure to unauthorized calls and unexpected usage charges if an account is compromised.

3

## Countries Automatically Enabled for LC Phone Voice

LC Phone automatically enables common calling destinations based on the location's business profile and phone number ownership. Higher-risk destinations require manual approval through HighLevel support.

The following destinations are typically enabled by default:

**United States and Canada** — Enabled for all LC Phone locations regardless of business country.

**Home Country** — The country where the location's business is registered is automatically enabled.

**Phone Number Purchase Country** — If a location purchases a phone number from a specific country, that destination is automatically enabled for outbound calling.

Important Distinction

A country appearing in the LC Phone pricing documentation does not mean it is enabled for your location. Geographic permission and call pricing are separate settings. To call a destination, both pricing and permission must be in place.

4

## How to Request Changes to LC Phone Geo Permissions

LC Phone locations cannot modify Voice Geo Permissions directly. Changes must be requested through HighLevel support. The request is reviewed by the phone team to ensure the destination aligns with your business needs and fraud prevention policies.

Follow these steps to request a change:

Step 1

Open HighLevel Support Chat

Navigate to the HighLevel platform and open the support chat widget. Choose the option to contact support for technical assistance.

Step 2

Provide Your Location ID

Include the Location ID for the account requiring the permission change. This ensures the request is applied to the correct location.

Step 3

List the Countries to Enable or Disable

Specify which countries you need to enable or disable for voice calling. Be clear about whether you are requesting access for new destinations or removing existing ones.

Step 4

Confirm Voice Permissions

Clarify that the request applies to voice calling. If you also need changes to SMS permissions, specify that separately.

Step 5

Wait for Review and Approval

The phone team will review your request and notify you once the permission change is applied. Processing time may vary depending on the destination and fraud risk assessment.

Tip

Include a brief business justification when requesting access to higher-risk destinations. This helps support process your request more quickly.

5

## Managing Geo Permissions for Twilio / Non-LC Phone Accounts

Locations connected directly to Twilio (non-LC Phone accounts) manage destination permissions in the Twilio Console rather than through the LC Phone support process. This allows you to enable or disable countries independently without submitting a support request.

Follow these steps to configure Voice Geo Permissions in Twilio:

Step 1

Log in to the Twilio Console

Navigate to <https://www.twilio.com/console> and sign in with your Twilio account credentials.

Step 2

Search for Geo Permissions

Use the Twilio Console search bar to find "Geo Permissions" or navigate to the Voice settings section where geographic permissions are managed.

Step 3

Open Voice Geographic Permissions

Select the Voice Geographic Permissions panel to view and modify the list of enabled calling destinations.

Step 4

Enable or Disable Countries

Toggle the permission switch for each country you want to enable or disable. Changes take effect immediately once saved.

Note

Twilio may require additional verification or approval for certain high-risk destinations. Review Twilio's fraud prevention policies before enabling new countries.

## Troubleshooting Calls Blocked by Geo Permissions

If an outbound call fails with a geographic restriction error, use the following diagnostic steps to identify and resolve the issue:

**Confirm the Destination Country Code** — Verify that you are dialing the correct international country code and phone number format. Incorrect formatting can cause calls to fail before permission checks.

**Verify Whether the Destination Is Enabled** — Check whether the destination country is enabled for your location. For LC Phone, contact support. For Twilio, review the Geo Permissions settings in your Twilio Console.

**Confirm Your Phone System Type** — Determine whether your location uses LC Phone or Twilio. The process for enabling countries differs between the two systems.

**Verify the Location's Business Country** — Confirm the country where your location's business is registered. The home country should be enabled automatically for LC Phone locations.

**Test from Another Location** — If possible, attempt the same international call from another location within your agency. If the call succeeds elsewhere, the issue is specific to your location's permissions.

**Review Call Error Logs** — Check the call logs in HighLevel or Twilio for error messages. Geographic restriction errors typically include country-specific details that can help diagnose the block.

Tip

If you continue to experience issues after enabling a country, wait 5-10 minutes for permission changes to propagate fully across the phone system before retrying the call.

7

## Related Articles

  * [Phone International Calling Rates](<https://help.gohighlevel.com/en/support/solutions/articles/155000008083>)
  * [Troubleshooting Call Failures](<https://help.gohighlevel.com/en/support/solutions/articles/48000981696>)
  * [Connecting Twilio to HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/155000002352>)


8

## Frequently Asked Questions

Q: Why can I call some countries but not others?

Voice Geo Permissions are configured individually for each country. Your location may have permissions for common destinations like the US and Canada but not for higher-risk or less frequently called countries. Contact HighLevel support to request additional destinations for LC Phone accounts, or configure them directly in Twilio for non-LC Phone accounts.

Q: Are the United States and Canada enabled automatically?

Yes. LC Phone automatically enables calling to the United States and Canada for all locations, regardless of the location's business country. These destinations do not require manual approval.

Q: Does purchasing a phone number in another country enable calling there?

Yes. If you purchase a phone number from a specific country through LC Phone, that destination is automatically enabled for outbound calling. This allows you to call numbers in the same country where your phone number is registered.

Q: How do I request access to another country with LC Phone?

Open HighLevel support chat, provide your Location ID, and specify which countries you need to enable for voice calling. The phone team will review your request and notify you once the permission change is applied.

Q: Does enabling a country for voice also enable it for SMS?

No. Voice and SMS permissions are managed separately. If you need SMS access to a specific country, you must request that permission independently. Refer to the SMS Geographic Permissions documentation for details.

Q: Does this article apply to Twilio / BYOT locations?

Yes, but the process differs. Twilio-connected locations (BYOT) manage Voice Geo Permissions directly in the Twilio Console rather than through HighLevel support. Refer to the section "Managing Geo Permissions for Twilio / Non-LC Phone Accounts" in this article.

Q: Will enabling more countries change my calling rates?

No. Enabling a country for Voice Geo Permissions does not change the per-minute calling rate. Rates are determined by the destination and number type, as published in the LC Phone pricing documentation. Permissions only control whether calls can be placed, not how much they cost.

Q: Why is a country blocked even though it appears in the pricing list?

A country appearing in the pricing documentation does not mean it is enabled for your location. Geographic permission and call pricing are separate settings. To call a destination, both pricing and permission must be in place. If a country is blocked, request permission through HighLevel support or enable it in Twilio.

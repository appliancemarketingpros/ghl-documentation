# Default Headers for Dedicated Sending Domains

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004428-default-headers-for-dedicated-sending-domains](https://help.gohighlevel.com/support/solutions/articles/155000004428-default-headers-for-dedicated-sending-domains)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Deliverability

Setting Default Headers (From Name & From Email) for Your Dedicated Sending Domain

Configure a fallback From Name and From Email keeping your emails authenticated and your brand consistent.

Overview

A **default header** provides a fallback From Name and From Email for outbound messages sent via a dedicated sending domain. ensuring deliverability and brand consistency without any manual intervention.

Table of Contents

1

When to Use Default Headers

2

Prerequisites

3

Setting Default Headers

4

How Default Headers Work in Practice

5

Example: Finished Default Header Setup

6

Best Practices & Considerations

7

Common Troubleshooting Scenarios

8

Frequently Asked Questions

1

## When to Use Default Headers

Use Case 1

Fallback for DMARC Failures

If a campaign's From address does not align with your dedicated sending domain's DKIM/SPF records, the platform will automatically substitute the default header so the message is still authenticated and delivered.

Use Case 2

Maintain Consistent Branding

Even if a typo or misconfiguration causes a non-aligned From address, recipients will see your brand's domain in the From field rather than a rejected or unfamiliar address.

Use Case 3

Regulatory & Compliance Requirements

Industries with strict email authentication requirements — such as finance and healthcare — should configure default headers to prevent DMARC rejections or quarantine actions that could interrupt critical communications.

2

## Prerequisites

Before configuring default headers, confirm the following are in place.

Requirement 1

You're Working in a Sub-Account

Default headers can only be set on dedicated sending domains managed within a sub-account. Agency-level domains do not support per-sub-account default header configuration.

Requirement 2

Your Dedicated Sending Domain Is Added and Validated

You must have completed DNS setup — including CNAME, DKIM, and SPF records — for your custom sending domain (e.g., email.yourbrand.com).

A green checkmark next to your domain under **Settings → Email Service → SMTP Service → Dedicated Domain and IP** confirms it is validated and ready.

3

## Setting Default Headers (From Name & From Email)

Default headers are configured per dedicated domain within a sub-account. Navigate to the location below to access the setting.

Navigation

Sub-Account Settings → Email Service → SMTP Service → Dedicated Domain and IP → Set Headers

![Dedicated Domain and IP settings showing Set Headers option](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044882641/original/l67IXG1nmKTdfTeM8aYyho5Bi4sdRCZDsw.png?1744290467)

Find your validated domain and click "Set Headers" to open the configuration panel.

![Set Headers form showing From Name and From Email fields](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044882742/original/u4kpWwg9k_Mdzc7Ts-PGYh3_0vTOcvXr5w.png?1744290526)

Enter your fallback From Name and From Email, then save.

How It's Applied

The default header is applied to emails sent through the dedicated domain **only when DMARC alignment fails**. If the campaign's From address already aligns with your domain, the campaign's original From Name and From Email are used as-is.

4

## How Default Headers Work in Practice

Step 1

Campaign Configuration

When creating a broadcast or workflow email, you set a campaign-level From Name and From Email.

If the campaign's From Email (e.g., sales@differentdomain.com) does not match your dedicated sending domain (e.g., email.yourbrand.com), DMARC alignment will fail at send time.

Step 2

DMARC Check & Fallback Decision

At send time, the platform checks DMARC alignment between the campaign's From address and the sending domain's DKIM/SPF records. One of two things happens:

Alignment Passes

The email is sent with the campaign's original From Name and From Email.

Alignment Fails

The platform substitutes the default header you configured — the email is sent with your fallback From Name and From Email instead.

Step 3

Recipient Experience

  * Recipients see a valid From Name and From Email that matches your authenticated sending domain.
  * The email remains DMARC-compliant and is less likely to be rejected or flagged as spam.


5

## Example: Finished Default Header Setup

Scenario

Setting| Value  
---|---  
Dedicated Sending Domain| email.yourbrand.com (validated)  
Default Header — From Name| YourBrand Support  
Default Header — From Email| support@email.yourbrand.com  
  
Broadcast / Workflow Email Configured by the User

Field| Value  
---|---  
Campaign From Name| Jane from YourBrand  
Campaign From Email| jane@anotherdomain.com (does not align with email.yourbrand.com)  
  
What Recipients See at Send Time

If Campaign From Email Aligns

From: Jane from YourBrand <jane@email.yourbrand.com> (or whatever aligned address you selected)

If DMARC Alignment Fails — Default Header Applied

From: YourBrand Support <support@email.yourbrand.com>

How to Confirm It Worked

  1. Send a test email using a non-aligned From Email (domain mismatch intentional).
  2. Open the received email and check its From address — it should match your configured default header.


6

## Best Practices & Considerations

A

Configure Default Headers Before Sending

Always set up your fallback header before launching major campaigns. If a DNS or DMARC misconfiguration occurs mid-send, the default header kicks in automatically — but only if it's already been saved.

B

Monitor Replies

The default From Email can be any address on your sending domain, but ensure that mailbox is actively monitored or aliased correctly (e.g., support@yourbrand.com forwarding to the right team) so customer replies don't go unread.

C

Test Before Scaling

Send a small internal test using a non-aligned From address to confirm the platform defaults correctly. Check both inbox placement and DMARC status before rolling out to your full audience.

D

Understand Propagation Delays

Changes to DNS records (DKIM, SPF, TXT) can take up to 48 hours to fully propagate. If you launch campaigns before propagation completes and no default header is set, messages may be rejected. Default headers protect against this window.

E

Segregate by Sub-Account

If you manage multiple brands or departments, create separate sub-accounts — each with its own dedicated domain and default headers — for fully isolated sending control and reputation management.

7

## Common Troubleshooting Scenarios

Issue| Possible Cause| Resolution  
---|---|---  
"Set Headers" option is not visible| You're in an agency-level view, or the domain is not validated under a sub-account.| Switch to the correct sub-account. Add and validate a dedicated domain under **Settings → Email Service → SMTP Service → Dedicated Domain and IP**.  
Emails still failing to send after fallback| DNS records (DKIM/SPF) are incomplete or incorrectly formatted.| Double-check DNS entries for your sending domain. Use an online DKIM/SPF validator. Allow up to 48 hours for propagation before testing again.  
Fallback header not applied when expected| The campaign From address aligns with the sending domain (even if unintentional), so no fallback is triggered.| Verify the campaign's From Email is genuinely non-aligned (domain mismatch). Review DMARC reports to confirm alignment failures.  
Recipients see the wrong From Name or From Email| The campaign or workflow hard-codes a display name that overrides expectations.| Edit the campaign/workflow From Name and From Email. Ensure the fallback header is correctly spelled and contains no stray spaces.  
SSL certificate not issued for the sending domain| Missing or incorrect CNAME/DNS records for domain validation.| In **Settings → Dedicated Domain** , click "Edit DNS Info" and follow the instructions exactly. Wait for propagation before retrying verification.  
  
8

## Frequently Asked Questions

Q: Does the default header override every email, or only when DMARC fails?

Only when DMARC alignment fails. If your campaign's From Email already matches your dedicated sending domain, the platform sends the email exactly as configured in the campaign — the default header is never applied. It is purely a fallback mechanism.

Q: Can I set different default headers for each dedicated domain?

Yes. Default headers are configured per dedicated domain. If your sub-account has multiple validated sending domains, each one can have its own independent From Name and From Email fallback.

Q: What happens if I don't set a default header?

If no default header is configured and a campaign's From address doesn't align with your sending domain, those emails may fail DMARC checks and be rejected or sent to spam by recipient mail servers. Setting a default header is strongly recommended before launching any campaigns.

Q: Does the default header affect the Reply-To address?

No. The default header only controls the From Name and From Email fields. If you have set a Reply-To address in your campaign or workflow, that Reply-To will continue to be used regardless of whether the fallback was triggered.

Q: Can the default From Email be on a different subdomain from my sending domain?

The default From Email must align with your validated dedicated sending domain for DMARC compliance. For example, if your sending domain is email.yourbrand.com, your default From Email should use that same domain (e.g., support@email.yourbrand.com).

Q: Will contacts notice when the default header is used instead of the campaign's From address?

Yes — they will see the fallback From Name and From Email rather than what the campaign specified. However, since both names come from your brand, this is typically transparent to the recipient. The more important outcome is that the email is delivered and authenticated rather than rejected.

Related Articles

[How to Set Up a Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001226115>) [SSL Certificate for Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) [How to Migrate My Agency Over to LC - Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>)

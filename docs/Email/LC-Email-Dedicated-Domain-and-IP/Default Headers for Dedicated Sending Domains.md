# Default Headers for Dedicated Sending Domains

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004428-default-headers-for-dedicated-sending-domains](https://help.gohighlevel.com/support/solutions/articles/155000004428-default-headers-for-dedicated-sending-domains)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Deliverability

Default Headers & the From Email Fallback Chain for Your Dedicated Sending Domain

How the Default Header overrides your campaigns and workflows — and exactly what address is used when the Default Header, the campaign/workflow From Email, and your Business Profile email are all left blank.

What You'll Learn

The **Default Header** sets a From Name and From Email for a dedicated sending domain. Once configured, it **always overrides** the From Name and From Email set on any campaign or workflow sent through that domain — regardless of what was typed into the campaign or workflow itself.

This article also covers what happens as each layer is left blank: if the Default Header, the campaign/workflow From Email, **and** your Business Profile email are all empty, the platform still finds a way to send — using an automatically generated **reply@ <your-subdomain>** address.

Table of Contents

1

When to Use a Default Header

2

Prerequisites

3

Setting the Default Header

4

How the Override Works in Practice

5

The Full Fallback Chain When Everything Is Blank

6

Example: Three Scenarios Side by Side

7

Best Practices & Considerations

8

Common Troubleshooting Scenarios

9

Frequently Asked Questions

1

## When to Use a Default Header

Use Case 1

Enforce One Sender Identity Across Every Send

Set the From Name and From Email once at the domain level, and every campaign and workflow sent through that domain uses it automatically — even if a teammate types a different From Name or From Email into an individual campaign or workflow, the Default Header takes over at send time.

Use Case 2

Regulatory & Compliance Requirements

Industries with strict communication standards — such as finance and healthcare — can lock every outbound email to a single, approved sender identity by setting a Default Header, removing the risk of any individual campaign or workflow going out under an unapproved From Name or From Email.

2

## Prerequisites

Before configuring a Default Header, confirm the following are in place.

Requirement 1

You're Working in a Sub-Account

Default Headers can only be set on dedicated sending domains managed within a sub-account. Agency-level domains do not support per-sub-account Default Header configuration.

Requirement 2

Your Dedicated Sending Domain Is Added and Validated

You must have completed DNS setup — including CNAME, DKIM, and SPF records — for your custom sending domain (e.g., email.yourbrand.com).

A green checkmark next to your domain under **Settings → Email Service → SMTP Service → Dedicated Domain and IP** confirms it is validated and ready.

3

## Setting the Default Header (From Name & From Email)

The Default Header is configured per dedicated domain within a sub-account. Navigate to the location below to access the setting.

Navigation

Sub-Account Settings → Email Service → SMTP Service → Dedicated Domain and IP → Set Headers

![Dedicated Domain and IP settings showing Set Headers option](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044882641/original/l67IXG1nmKTdfTeM8aYyho5Bi4sdRCZDsw.png?1744290467)

Find your validated domain and click "Set Headers" to open the configuration panel.

![Set Headers form showing From Name and From Email fields](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044882742/original/u4kpWwg9k_Mdzc7Ts-PGYh3_0vTOcvXr5w.png?1744290526)

How It's Applied

Once saved, the Default Header **always overrides** the From Name and From Email configured on any campaign or workflow sent through this dedicated domain — there is no condition attached, it applies to every send. If you leave the Default Header fields blank, the platform moves down the fallback chain described in Section 5.

4

## How the Override Works in Practice

Step 1

Campaign or Workflow Configuration

When creating a broadcast or workflow email, you can still set a campaign-level From Name and From Email as usual. This is what will be used **only if** no Default Header is configured for the sending domain.

Step 2

Default Header Check at Send Time

At the moment the email sends, the platform checks whether a Default Header is saved for the dedicated domain. If one is set, it takes priority automatically — the campaign's or workflow's own From Name and From Email are ignored, not just used as a backup.

Step 3

Recipient Experience

  * If a Default Header is set, recipients always see that From Name and From Email — regardless of what was entered on the campaign or workflow.
  * Because the address comes from your authenticated sending domain, the email stays DMARC-compliant and is less likely to be rejected or flagged as spam.


5

## The Full Fallback Chain When Everything Is Blank

A Default Header is only the first check the platform makes. Every email needs a valid From Name and From Email to send, so the platform works down a four-tier fallback chain until it finds one — even if every field along the way was left empty.

Tier 1 — Highest Priority

Default Header on the Dedicated Domain

If a Default Header is saved for the sending domain, it is used — always. Nothing below this tier is ever checked.

Tier 2

Campaign or Workflow From Name & From Email

If the Default Header is left blank, the platform uses whatever From Name and From Email was typed directly into that specific campaign or workflow.

Tier 3

Business Email From Your Business Profile

If **both** the Default Header and the campaign/workflow From Email are left blank, the platform checks the Business Email saved under your **Business Profile**. If one is present, that address is used as the From Email for the send.

Tier 4 — Final Safety Net

Auto-Generated reply@<your-subdomain> Address

If **all three** of the above are blank — no Default Header, no campaign/workflow From Email, and no Business Profile email — the platform automatically generates a From address using your active, validated sending subdomain, in the format reply@<your-subdomain>, and uses it to send the email. This guarantees a send never fails purely for lack of a configured sender address.

Priority| Source Checked| Used When…  
---|---|---  
1| Default Header| It is set for the domain (always wins if present)  
2| Campaign / Workflow From Name & Email| Default Header is blank  
3| Business Profile — Business Email| Default Header AND campaign/workflow From Email are both blank  
4| Auto-generated reply@<subdomain>| Default Header, campaign/workflow From Email, AND Business Profile email are all blank  
  
Watch Out

This chain exists so a send is never blocked purely because a From address wasn't configured somewhere — not so you can skip configuring one. Reaching Tier 4 means recipients see a generic reply@ address instead of your brand's name, which looks less trustworthy and can hurt open rates. Set at least a Business Email in your Business Profile as a safety net beneath your Default Header.

6

## Example: Three Scenarios Side by Side

Setup

Setting| Value  
---|---  
Dedicated Sending Domain| email.yourbrand.com (validated)  
Business Profile — Business Email| hello@yourbrand.com  
Campaign From Name / Email (when filled in)| Jane from YourBrand / jane@email.yourbrand.com  
  
What Recipients See in Each Scenario

Scenario 1 — Default Header Is Set

From: YourBrand Support <support@email.yourbrand.com>  
The campaign's "Jane from YourBrand" name and address are ignored completely, even though they were correctly configured and properly aligned to the domain.

Scenario 2 — Default Header Blank, Campaign From Email Filled In

From: Jane from YourBrand <jane@email.yourbrand.com>  
With no Default Header saved for the domain, the campaign's own From Name and From Email are used as configured (Tier 2).

Scenario 3 — Default Header AND Campaign From Email Both Blank

From: YourBrand <hello@yourbrand.com>  
With both of those blank, the platform falls to Tier 3 and uses the Business Email saved in the Business Profile.

Scenario 4 — Default Header, Campaign From Email, AND Business Profile Email All Blank

From: reply@email.yourbrand.com  
With every layer above empty, the platform falls all the way to Tier 4 and auto-generates a reply@ address on your active, validated sending subdomain so the email still sends.

How to Confirm It Worked

  1. Save a Default Header whose From Name and From Email differ from a campaign's configured values, then send a test — confirm the Default Header wins.
  2. Clear the Default Header and the campaign's From Email, but keep a Business Email saved — send a test and confirm the Business Email is used.
  3. Clear all three (Default Header, campaign/workflow From Email, and Business Profile email) and send a test — confirm the From address comes back as reply@ your validated subdomain.


7

## Best Practices & Considerations

A

Decide Before You Set It — It Overrides Everything

Because the Default Header overrides every campaign and workflow sent through the domain, confirm this is the sender identity you want used across the board before saving it. Any campaign-level From Name or From Email your team configures afterward will be ignored while the Default Header is active.

B

Keep a Business Email on File as a Safety Net

Since Tier 3 of the fallback chain uses the Business Email in your Business Profile, keep that field filled in even if you rely on a Default Header day-to-day. It's the difference between a send falling back to your business's own address versus falling all the way to an auto-generated reply@ address.

C

Monitor Replies

The Default Header's From Email can be any address on your sending domain, but ensure that mailbox is actively monitored or aliased correctly (e.g., support@yourbrand.com forwarding to the right team) so customer replies don't go unread. This applies just as much to an auto-generated reply@ address — check that mailbox too if you ever land on Tier 4.

D

Test Before Scaling

Send a small internal test to confirm the Default Header is being applied. Check that the From Name and From Email recipients actually see match your Default Header configuration — not whatever was typed into the campaign or workflow, and not a fallback tier you didn't intend to reach.

E

Tell Your Team It's Set

A Default Header silently overrides whatever From Name and From Email a teammate configures at the campaign or workflow level. Make sure anyone building campaigns or workflows on this domain knows a Default Header is active, so they aren't confused when their custom From address never actually gets used.

F

Segregate by Sub-Account

If you manage multiple brands or departments, create separate sub-accounts — each with its own dedicated domain and Default Header — for fully isolated sending control and reputation management.

## Frequently Asked Questions

Q: Does the Default Header override every email, or only in certain situations?

The Default Header overrides **every** campaign and workflow email sent through that dedicated domain — always, not just as a backup. As long as a Default Header is saved, it takes priority over any From Name and From Email configured on a campaign or workflow, even if the campaign's own address was correctly configured. It is only skipped when the Default Header fields themselves are left blank, in which case the platform moves to the next tier of the fallback chain.

Q: What's the full order of priority for the From address?

In order: (1) the Default Header set on the dedicated domain, (2) the From Name and From Email typed into the specific campaign or workflow, (3) the Business Email saved in your Business Profile, and (4) an auto-generated reply@<your-subdomain> address if all three of the above are blank. See the full fallback chain for details.

Q: Does the platform ever check my Business Profile for a From Email?

Yes. If no Default Header is set on the dedicated domain and the campaign or workflow itself has no From Email configured, the platform looks at the Business Email saved in your Business Profile and uses that address before falling back any further.

Q: What happens if the Default Header, the campaign/workflow From Email, and my Business Profile email are all left blank?

The platform still needs to send the email, so it automatically builds a From address using your active, validated sending subdomain in the format reply@<your-subdomain>. This guarantees delivery is never blocked by a missing sender address, but you have no control over the name or mailbox recipients see, so it's best treated as a safety net rather than a strategy.

Q: Can I set a different Default Header for each dedicated domain?

Yes. The Default Header is configured per dedicated domain. If your sub-account has multiple validated sending domains, each one can have its own independent From Name and From Email override.

Q: Does the Default Header apply to workflows, or only broadcast campaigns?

Both. The Default Header, and every tier of the fallback chain below it, applies to any email sent through the dedicated domain, whether it's triggered by a broadcast campaign or by a workflow action.

Q: Does the Default Header affect the Reply-To address?

No. The Default Header only controls the From Name and From Email fields. If you have set a Reply-To address on your campaign or workflow, that Reply-To continues to be used regardless of the Default Header or which fallback tier was used.

Q: Should the Default Header's From Email use the domain I validated?

Yes. The Default Header's From Email should sit on your validated dedicated sending domain (e.g., if your domain is email.yourbrand.com, use something like support@email.yourbrand.com) so it stays properly authenticated by the SPF and DKIM records you set up. The same applies to the auto-generated Tier 4 address, which is always built on your active, validated subdomain for this reason.

Related Articles

[How to Set Up a Dedicated Sending Domain](<https://help.gohighlevel.com/en/support/solutions/articles/48001226115>) [SSL Certificate for Dedicated Sending Domain](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) [How to Migrate My Agency to LC - Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>)

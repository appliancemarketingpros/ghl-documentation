# Action Required: International SMS Compliance Updates — UK & Turkey

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001240411-action-required-international-sms-compliance-updates-uk-turkey](https://help.gohighlevel.com/support/solutions/articles/48001240411-action-required-international-sms-compliance-updates-uk-turkey)  
**Category:** Phone System  
**Folder:** Messaging

---

This article covers two active international SMS compliance regulations that affect senders using HighLevel's LC Phone or Twilio-connected accounts:United Kingdom — International long codes have been blocked for A2P SMS since June 2023. All UK long codes now require regulatory approval (RC bundle) and KYC verification. Turkey — Effective April 1, 2026, all international A2P SMS containing URLs, hyperlinks, or shortened links are blocked by order of Turkey's BTK authority.If you send SMS to recipients in either country, read the relevant section below and take action immediately.  
---  
  
  
United Kingdom: International Long Codes Blocked + 2024 Compliance Requirements

Overview

If you send SMS messages to UK mobile numbers, your deliverability and compliance are at risk unless you update your sender types. Starting June 1, 2023, UK carriers began blocking international long codes for Application-to-Person (A2P) traffic. In 2024, further regulatory requirements were introduced for UK long codes themselves.

  


What Changed in 2023

Carrier Blocking of International Long Codes

From June 1, 2023, UK network operators started blocking SMS from non-UK long codes. These numbers were originally designed for Person-to-Person (P2P) use, but many businesses were using them for A2P traffic, which carriers now classify as abuse of P2P routes.

Impact: Any SMS sent to UK recipients from an international long code is likely to fail.

  


What Changed in 2024

Twilio and UK regulators layered on stricter compliance requirements:

1\. Regulatory Compliance Bundles (RC Bundles)

  * From May 27, 2024, all new UK long codes require an approved RC bundle before they can send SMS or make calls.

  * From September 30, 2024, all UK long codes (new or existing) must have an approved RC bundle.


2\. Know Your Customer (KYC)

  * Businesses must provide documentation to verify their identity and intended use case before using UK long codes.


3\. Full Enforcement of Blocking

  * By mid-2024, all UK carriers had aligned to enforce these rules.

  * Traffic from international long codes is universally blocked.

  * Unregistered UK long codes will also fail.


  


What You Need to Do

Step 1 — Stop Using International Long Codes

  * If you are still sending SMS from non-UK numbers to UK recipients, switch immediately.


Step 2 — Use an Approved Sender Type

  * UK Long Code (Local Number) — Requires KYC and regulatory approval.

  * Alphanumeric Sender ID — For one-way traffic; brand your sender name (e.g., YourCompany).

  * Short Code — For higher-volume or two-way messaging; apply for a UK short code (12–16 weeks provisioning).


Step 3 — Register Your Numbers

  * Submit your Regulatory Compliance (RC) bundle in the Twilio Console.

  * Provide the necessary KYC documents (business name, address, use case, etc.).


Step 4 — Monitor Message Logs

  * In Twilio Console, use Messaging Insights to filter "From Country ≠ UK" and "To Country = UK" to find non-compliant traffic.

  * Look for blocked or undelivered messages and update routing accordingly.


  


How to Buy a UK Number in Twilio

  1. Go to: Console → Develop → Phone Numbers → Buy a number

  2. Set Country = UK

  3. Un-check Voice (if you want SMS-only)

  4. Select an SMS-capable number and complete the RC bundle submission![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069209192/original/V7YNZpTLICw41XPFjxXXc-lgTGLEpIhIOA.png?1776257427)


  


UK Timeline Recap

Date| Milestone  
---|---  
June 1, 2023| UK carriers begin blocking international long codes  
May 27, 2024| New UK long codes require RC bundle approval  
July 30, 2024| Full carrier enforcement across all UK networks  
Sept 30, 2024| All UK long codes (new + existing) must have RC approval  
  
  


UK Key Takeaways

  * International long codes cannot be used for UK SMS.

  * All UK long codes now require KYC and regulatory compliance.

  * Alphanumeric Sender IDs and short codes remain valid alternatives.

  * Act now to avoid message failures and regulatory issues.


  


  


Turkey: International SMS Containing URLs Now Blocked

Effective April 1, 2026 — Turkey's Information and Communication Technologies Authority (BTK) has blocked all international A2P SMS containing URLs, hyperlinks, or shortened links sent to Turkish recipients. Blocked messages return error code 30007 and operators may issue fines.  
---  
  
  


What's Happening?

Turkish mobile operators are now blocking any international A2P SMS that contains internet addresses, URLs, hyperlinks, or shortened links. This is enforced by the Bilgi Teknolojileri ve İletişim Kurumu (BTK) — Turkey's national communications regulator.

Messages blocked under this regulation will:

  * Return error code 30007 (carrier-level filtering)

  * Fail to deliver to the recipient

  * Potentially result in fines from Turkish operators


This applies to ALL SMS types — including order confirmations, shipping updates, appointment reminders, and one-time passcodes (OTPs).  
---  
  
  


What You Need to Do

Step 1 — Immediately Remove All URLs from Messages Sent to Turkey

Remove the following from any SMS template or workflow targeting Turkish recipients:

  * Full URLs (e.g., https://example.com/order/123)

  * Shortened URLs (e.g., bit.ly/abc, hl.link/xyz)

  * Hyperlinked or anchor text pointing to any URL

  * Tracking links embedded in messages


Step 2 — Update Your Templates and Workflows

  1. Go to your HighLevel sub-account.

  2. Open any SMS templates, workflows, or campaigns targeting Turkish recipients.

  3. Remove or replace all URLs. Use a phone number, email, or plain-text instructions instead.

  4. Save and republish affected templates or workflows.

  5. Test delivery by sending a URL-free message to a Turkish number.


If You Have a Local Turkey Business Entity

If your business is registered in Turkey and must continue sending URLs via SMS, you need a compliant local messaging pathway:

  1. Secure a direct contract with Posta Güvercini, a BTK-licensed local messaging platform.

  2. Authorize Posta Güvercini as your service provider via the Turkish Message Management System (IYS).

  3. Contact HighLevel Support to finalize the technical setup and routing.


? This pathway requires a formal business registration in Turkey and a direct contract with Posta Güvercini. Without a local entity, you must remove all URLs from your messages.  
---  
  
  


  


No Action Needed If…

  * You are not sending SMS to Turkey, OR

  * Your messages to Turkish recipients contain no URLs or hyperlinks.


  


Turkey Timeline Recap

Date| Milestone  
---|---  
April 1, 2026| BTK regulation takes effect — all international SMS with URLs blocked  
Ongoing| Turkish operators enforce error code 30007 and may issue fines  
  
  


  


Turkey Key Takeaways

  * All international A2P SMS containing URLs are blocked in Turkey as of April 1, 2026.

  * Affected messages return error code 30007.

  * Remove all URLs, shortened links, and hyperlinks from templates targeting Turkish recipients.

  * A local Turkey entity + Posta Güvercini contract is the only approved pathway for URL-containing SMS.


  


FAQs

Does the Turkey URL block affect OTPs and transactional messages?

Yes. The BTK regulation applies to all international A2P SMS regardless of message type, including one-time passcodes, order confirmations, and shipping notifications.

Can I use a URL shortener to avoid the Turkey block?

No. Shortened URLs are explicitly included in the block. All forms of internet addresses — full URLs, short links, and hyperlinks — are blocked.

What is error code 30007?

Error 30007 is a carrier-level filtering error indicating the message was blocked before delivery. For Turkey, it means the operator detected a URL in an international SMS. For UK, it can also indicate the sender type is not approved for A2P traffic.

Does the Turkey regulation affect WhatsApp or email?

No. This regulation applies specifically to international A2P SMS. WhatsApp, email, and other channels are not affected.

Do I need an RC bundle for UK numbers on LC Phone?

Yes. If you are using LC Phone (not your own Twilio account), HighLevel handles the underlying carrier relationship, but you still need to ensure your phone number type is compliant. Contact HighLevel Support if you are unsure about your UK number setup.

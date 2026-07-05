# Email Authentication - DMARC

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001224630-email-authentication-dmarc](https://help.gohighlevel.com/support/solutions/articles/48001224630-email-authentication-dmarc)  
**Category:** Email  
**Folder:** LC Email

---

Email Compliance

DMARC for Email Authentication

Understand what DMARC is, how to configure it, and how to resolve common failures when using shared sending domains.

Important — Gmail & Yahoo Requirement

Starting February 2024, [Gmail](<https://blog.google/products/gmail/gmail-security-authentication-spam-protection/>) and [Yahoo](<https://blog.postmaster.yahooinc.com/post/730172167494483968/more-secure-less-spam>) require DKIM and DMARC authentication for all senders. We strongly recommend setting up both.

For full details, see our article on [Google and Yahoo authentication changes in 2024](<https://help.gohighlevel.com/en/support/solutions/articles/155000001634>).

What You'll Learn

DMARC (Domain-based Message Authentication Reporting and Conformance) verifies emails by combining SPF and DKIM. It lets domain owners define what happens to unauthorized email — monitor it, quarantine it, or reject it outright.

This article covers what DMARC is, how to read and configure a DMARC record, how the authentication flow works, and how to resolve DMARC failures when sending through a shared domain.

Table of Contents

1

What is DMARC?

2

What is a DMARC Record?

3

How Does DMARC Work?

4

Resolving DMARC Failures on Shared Domains

1

## What is DMARC?

DMARC — Domain-based Message Authentication Reporting and Conformance — is a free technical standard that verifies emails by combining SPF and DKIM. Introduced in 2012, it helps prevent email fraud like phishing by letting domain owners specify how unauthorized use of their domain should be handled via a policy tag (**p=**).

There are three policy levels:

p=none

Monitor only

Monitors your email traffic. No action is taken on failing messages — useful for initial visibility.

p=quarantine

Send to spam

Unauthorized emails are directed to the recipient's spam or junk folder instead of the inbox.

p=reject

Block entirely — the goal state

The strictest and recommended final policy. Unauthorized emails are not delivered at all.

2

## What is a DMARC Record?

A DMARC record lives in a TXT-type DNS entry named **_dmarc**. It is composed of tags assigned with values, separated by semicolons. Here is the simplest valid record:

Example — Minimum DMARC Record

v=DMARC1; p=none;

The table below explains all available tags and their default values:

Tag| Name| Default| Description  
---|---|---|---  
v| DMARC Version| DMARC1| Must always be "DMARC1". If missing or incorrect, the entire record is ignored.  
p| Policy| none| Action for emails failing DMARC checks: **none** (monitor), **quarantine** (spam), **reject** (block).  
adkim| DKIM Alignment| r| **r** (Relaxed): DKIM domains sharing a common Organizational Domain pass. **s** (Strict): Requires exact domain match.  
aspf| SPF Alignment| r| Same as adkim but for SPF. **r** (Relaxed) or **s** (Strict) matching of the SPF domain against the From domain.  
sp| Sub-domain Policy| p= value| Explicit policy for sub-domains under this DMARC record. Inherits the parent p= value if not set.  
fo| Forensic Reporting Options| 0| **0** : Report if all mechanisms fail. **1** : Report if any fail. **d** : Report on DKIM failure. **s** : Report on SPF failure.  
ruf| Forensic Report URI| none| Where to send forensic (failure) reports. Format: mailto:address@example.org  
rua| Aggregate Report URI| none| Where to send aggregate XML feedback reports. Format: mailto:address@example.org  
rf| Reporting Format| afrf| Format for individual forensic reports.  
pct| Percentage| 100| Percentage of failing messages the policy applies to. Only valid with quarantine or reject.  
ri| Reporting Interval| 86400| Frequency (in seconds) for receiving aggregate XML reports. Default is 86400 (24 hours).  
  
Pro Tip

Not sure how to structure your DMARC record? Use a free [DMARC generator tool](<https://dmarcian.com/dmarc-record-wizard/>) to build one correctly.

3

## How Does DMARC Work?

DMARC works across three phases: Authentication, Reporting, and Conformance (policy enforcement). Each configuration serves to authenticate emails and define how failures are handled.

Phase 1

Authentication

  * **SPF / DKIM Check:** Receiving servers verify SPF or DKIM authentication methods.
  * **Domain Alignment:** Validates whether the SPF domain (Return-Path) or DKIM domain (d=) aligns with the "From" domain in the email header.
  * **DMARC Policy:** Extracts and enforces the DMARC policy from the DNS record of the "From" domain.


Example Configurations — Authentication

SPF passes and aligns with the "From" domain → DMARC passes:

v=DMARC1; p=none; aspf=r;

DKIM passes and aligns with the "From" domain → DMARC passes:

v=DMARC1; p=none; adkim=s;

Both SPF and DKIM fail → DMARC fails:

v=DMARC1; p=reject;

Phase 2

Alignment Modes

  * **Relaxed (r):** Allows subdomains in SPF/DKIM checks, comparing them to the "From" domain. A subdomain sharing the same Organizational Domain passes.
  * **Strict (s):** Requires an exact match of the SPF/DKIM domain with the "From" domain. No subdomain exceptions.


Phase 3

Reporting

  * **Aggregate Reports (rua):** Periodic XML reports with pass/fail results, sent to addresses specified with the rua tag.
  * **Forensic Reports (ruf):** Detailed failure reports sent to the ruf address. Many providers limit these due to privacy concerns.
  * **Reporting Interval (ri):** Controls how frequently aggregate XML reports are sent. Default is 86400 seconds (24 hours).


Example Configurations — Reporting

Aggregate reports every 24 hours:

v=DMARC1; p=none; rua=mailto:postmaster@mydomain.com; ri=86400;

Forensic reports every 7 days:

v=DMARC1; p=none; ruf=mailto:postmaster@mydomain.com; ri=604800;

Phase 4

Conformance (Policy Enforcement)

  * **DMARC Policy (p):** Defines how receiving servers handle emails that fail DMARC checks — none, quarantine, or reject.
  * **Percentage (pct):** Specifies what percentage of failing messages the policy is applied to. Useful for gradual rollout.


Example Configurations — Rollout Strategy

Start with quarantine at 50% for testing:

v=DMARC1; p=quarantine; pct=50;

Move to full reject enforcement:

v=DMARC1; p=reject;

4

## Resolving DMARC Failures on Shared Domains

Note

DMARC is not required to send emails from shared domains on the LeadConnector email system.

When you switch to the LeadConnector email system, or have not configured your own Mailgun or SMTP, all emails are sent through a shared domain. If your "From" address domain has a strict DMARC policy (**p=reject** or **p=quarantine**), you may see the following error:

![DMARC policy error message shown in the email sending interface](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155029885740/original/XbxWJPF5hf31tJ4qc-FOom23fD_efkCL9A.jpg?1721914780)

DMARC p=reject error displayed when using a shared domain

Error Message

"The domain in your from address has a p=reject DMARC policy. Without a dedicated sending domain configured, most inbox providers will reject your messages, resulting in elevated bounces. To avoid elevated bounces, use company emails."

Your actual DMARC record: v=DMARC1; p=reject

How to Fix

Temporarily set your DMARC policy to p=none

Log in to your DNS provider and update your **_dmarc** TXT record so the policy reads **p=none**. This ensures messages are delivered even when DMARC fails, while you work toward configuring a dedicated sending domain.

Heads Up

Relaxing to **p=none** reduces your domain's protection against spoofing. Treat this as a temporary measure and set up a dedicated sending domain as soon as possible to restore full DMARC enforcement.

5

## Frequently Asked Questions

Q: Do I need DMARC to send emails at all?

DMARC is not strictly required to send email, but Gmail and Yahoo now require it for bulk senders (5,000+ emails/day). Even below that threshold, setting up DMARC improves deliverability and protects your domain from spoofing.

Q: What's the difference between p=quarantine and p=reject?

**p=quarantine** sends failing messages to the recipient's spam folder — they can still be found. **p=reject** instructs receiving servers to block the message entirely so it never reaches the recipient at all.

Q: Where do I add my DMARC record?

Add a **TXT record** in your domain's DNS settings. The host/name field should be _dmarc and the value should be your DMARC policy string (e.g., v=DMARC1; p=none;). Your DNS provider's control panel is where you make this change.

Q: Why is DMARC failing even though I have SPF and DKIM set up?

DMARC requires both authentication _and_ alignment. SPF or DKIM can pass technically but still cause DMARC to fail if the authenticated domain doesn't align (match) with the "From" domain in your email header. Check that your SPF return-path domain or DKIM d= domain matches your sending "From" domain.

Q: Can I use a personal Gmail or Yahoo address as my From address?

No. Gmail and Yahoo enforce strict DMARC policies (**p=reject**) on their own domains. If you send email using a @gmail.com or @yahoo.com address through a third-party platform, the messages will be rejected. Always use a domain you own and control as your From address.

Q: How long does a DMARC record change take to propagate?

DNS changes typically propagate within 15 minutes to 1 hour, though full global propagation can take up to 48 hours depending on your DNS provider and the TTL setting on the record.

Q: What's the recommended path to get to p=reject?

Start with **p=none** to collect aggregate reports and understand your email traffic. Once legitimate sources are all passing, move to **p=quarantine; pct=25** and gradually increase the percentage. When you're confident all legitimate mail passes, switch to **p=reject** for full enforcement.

Additional Resources

[Achieving Compliance: Meeting Google and Yahoo's Email Sender Requirements in 2024](<https://help.gohighlevel.com/support/solutions/articles/155000001634-achieving-compliance-meeting-google-and-yahoo-s-email-sender-requirements-in-2024>) [Email Sending Guide: Email Best Practices & Email Warm Up](<https://help.gohighlevel.com/support/solutions/articles/155000001021-email-sending-guide-email-best-practices-email-warm-up>)

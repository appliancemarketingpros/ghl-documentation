# Reverse DNS white labeling - Dedicated IP

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001154-reverse-dns-white-labeling-dedicated-ip](https://help.gohighlevel.com/support/solutions/articles/155000001154-reverse-dns-white-labeling-dedicated-ip)  
**Category:** Email  
**Folder:** LC Email

---

Email Infrastructure

Reverse DNS (rDNS) for Dedicated IPs

Display your company name as the sender instead of a third-party service — improve deliverability, trust, and brand consistency.

Overview

When recipients open your email, showing your company name in the "From" or "Sender" field is far more professional — and more trustworthy — than displaying "Sent by Mailgun" or another third-party service. Configuring reverse DNS (rDNS) on your dedicated IP is how you make that happen.

Proper rDNS setup improves deliverability, reduces the chance emails are flagged as spam, and keeps your branding consistent across every campaign you send.

Table of Contents

1

What is Reverse DNS (rDNS)?

2

Common rDNS Mistakes

3

How to Set Up rDNS

4

Frequently Asked Questions

1

## What is Reverse DNS (rDNS)?

Reverse DNS is essentially the opposite of a standard DNS lookup. Rather than mapping a domain name to an IP address, rDNS translates an IP address into its associated hostname. This works for both IPv4 and IPv6 addresses and is used to verify the authenticity of the server sending your email.

In practice, rDNS converts the IP address of your sending mail server into a hostname (e.g., mail.yourcompany.com). Mailbox providers perform this lookup to confirm that the IP belongs to a legitimate domain. In email sending, this allows your company name — not "Sent by Mailgun.com" — to appear as the sender in recipients' inboxes.

Important Distinction

rDNS configuration for your dedicated IP is **not** the same as masking the CNAME of mailgun.org in your DNS settings. These are two separate configurations. rDNS specifically controls what hostname appears when a mailbox provider looks up your sending IP address.

The Payoff

Correct rDNS setup ensures your company name is shown as the sender, improves inbox placement, and builds recipient trust — all without the recipient ever seeing the underlying delivery infrastructure.

2

## Common rDNS Mistakes

Accurate rDNS configuration is critical for deliverability and sender reputation. These are the three most common mistakes to avoid:

Mistake 1

Incorrect or Missing PTR Record

A PTR (Pointer) record is required to verify that your sending mail server matches the IP address in the email. Without a valid PTR record, mailbox providers cannot confirm your identity. Ensure your PTR record is correctly configured and returns a valid hostname for the IP being queried.

Mistake 2

Mismatched Hostname (Forward-Confirmed rDNS Failure)

The hostname returned by your PTR record must resolve back to the same IP address — and vice versa. This bidirectional check is called Forward-Confirmed Reverse DNS (FCrDNS). A mismatch causes lookup failures and reduces trust.

**Example:** If your PTR record returns mail.yourwebsite.com for IP 8.8.8.8, then a forward DNS lookup of mail.yourwebsite.com must also resolve to 8.8.8.8.

Mistake 3

Hostname That Doesn't Resolve

If the hostname in your PTR record doesn't resolve to any IP at all, mailbox providers will flag this as a significant trust issue — which can lead to delivery failures. Always verify that your A record is correctly published before submitting the hostname for rDNS.

Key Takeaway

Your PTR record must point to a valid hostname, and that hostname's A record must resolve back to the same IP. Both directions must be consistent and resolvable.

3

## How to Set Up rDNS

Dedicated IP Required

rDNS can only be configured on a **dedicated IP**. Shared IPs do not support this because rDNS resolves to only one hostname per IP address. A dedicated IP is required for this setup.

Follow these steps to configure rDNS for your dedicated IP:

Step 1

Add an A Record at Your Hosting Provider

Log in to your DNS hosting provider and add an A record pointing your chosen hostname to your dedicated IP address. The record format will look like:

A mail.yourcomain.com 123.45.67.89

Step 2

Navigate to Agency Settings

Go to **Agency Settings → Email Service**.

Step 3

Open Dedicated Domain and IP

In the **SMTP Service** tab, click **Dedicated Domain And IP** in the LeadConnector section.

![SMTP Service tab showing Dedicated Domain And IP button](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155009612052/original/IUIljk9XIJS27U3BT_o4jUzNTpWR7LasGg.png?1696855911)

Click Dedicated Domain And IP in the LeadConnector SMTP section

Step 4

Open Reverse DNS (PTR) Settings

In the Dedicated IP section, click the **three-dot menu** next to your dedicated IP and select **Reverse DNS (PTR)**.

![Three-dot menu on dedicated IP showing Reverse DNS \(PTR\) option](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155009612160/original/cwkp94jqGl-jc1vsViWXa2bvRMaphEwmkw.png?1696855977)

Select Reverse DNS (PTR) from the three-dot menu on your dedicated IP

Step 5

Enter Your A Record Hostname

Enter the same hostname you used in your A record (e.g., mail.yourcompany.com). The PTR record will be updated on the back end to point to the hostname you provide.

![Reverse DNS \(PTR\) configuration screen with hostname input field](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155009613038/original/Oge0tXLX2gyJh_WWlLh5Xdb0TiEVuC-AJA.png?1696856251)

Enter the hostname matching your A record to complete PTR configuration

You're All Set

Once the PTR record is updated, your dedicated IP will resolve to the hostname you configured. Mailbox providers will now display your company name as the sender rather than a third-party service name.

4

## Frequently Asked Questions

Q: Can I set up rDNS on a shared IP?

No. rDNS resolves to only one hostname per IP address, so it is only supported on dedicated IPs. Shared IPs are used by multiple senders and cannot be uniquely assigned to your domain's hostname.

Q: What is a PTR record and why does it matter?

A PTR (Pointer) record maps an IP address back to a hostname. Mailbox providers use it to verify that the server sending email is who it claims to be. Missing or incorrect PTR records are a common cause of email rejection and spam filtering.

Q: Does rDNS replace DKIM or SPF authentication?

No. rDNS, DKIM, and SPF serve different purposes and are all complementary. DKIM signs the email content, SPF authorizes sending IPs, and rDNS verifies the identity of the sending server's IP. For best deliverability, all three should be configured correctly.

Q: How long does it take for rDNS changes to propagate?

PTR record updates on the back end are typically applied quickly, but DNS propagation can take anywhere from a few minutes to 48 hours depending on TTL settings and how frequently resolvers cache records.

Q: How do I verify that my rDNS is set up correctly?

You can verify your rDNS by running a reverse DNS lookup on your dedicated IP using a tool like **MXToolbox** or the command line (nslookup / dig -x). The result should return your configured hostname. Then confirm a forward lookup of that hostname resolves back to your IP.

Q: Will rDNS affect how my emails look to recipients?

Yes. With correct rDNS, your company name or domain appears in the "Sender" or technical headers instead of a third-party service provider's name. This improves perceived legitimacy and brand recognition, particularly in clients that display the sending server details.

Q: Can I use any hostname, or does it need to match my sending domain?

The hostname doesn't have to exactly match your From domain, but it must be a valid, fully resolvable hostname that you own and control. Best practice is to use a subdomain of your primary sending domain (e.g., mail.yourcompany.com) for consistency and trust signals.

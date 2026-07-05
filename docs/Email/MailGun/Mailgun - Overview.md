# Mailgun - Overview

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981677-mailgun-overview](https://help.gohighlevel.com/support/solutions/articles/48000981677-mailgun-overview)  
**Category:** Email  
**Folder:** MailGun

---

EMAIL INFRASTRUCTURE

Mailgun: What It Is, Pricing, and Domain Setup Options

Learn what Mailgun is, how pricing works, which domain or subdomain to use, and the pros and cons of each setup option.

What You'll Learn

Mailgun is the email delivery service that powers bulk sending on the platform. In this article, you'll learn what Mailgun is, how pricing works, which domains or subdomains to use, and the pros and cons of different setup options so you can choose the best configuration for your agency and clients.

Table of Contents

1

What is Mailgun?

2

Key Benefits of Using Mailgun

3

How Much Will Mailgun Cost?

4

What Domain Should I Use?

5

Frequently Asked Questions

6

Related Articles

1

## What is Mailgun?

Mailgun is a third-party service used to send emails in bulk — similar to how Twilio is used to send text messages and calls. For new onboarding agencies, you'll be using [LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001220605>) by default.

Tip

Not sure if you need Mailgun at all? Read [What is LC Email?](<https://help.gohighlevel.com/en/support/solutions/articles/48001220605>) first — most new agencies won't need to set up Mailgun separately.

2

## Key Benefits of Using Mailgun

  * **Reliable bulk email sending** — send large volumes of emails through a dedicated, reputable email infrastructure.
  * **Branded sending domains** — use your own domain or subdomains so emails look professional and on-brand.
  * **Flexible setup options** — choose between one shared subdomain or multiple client-specific subdomains based on your needs.
  * **Better deliverability control** — optimize DNS and MX records to improve inbox placement and reduce issues from poor-quality lists.


3

## How Much Will Mailgun Cost?

Note

Learn more about Mailgun [pricing](<https://www.mailgun.com/pricing/>) directly on their site — plans and rates can change at any time.

  * Mailgun's **Basic plan** starts at **$15/month**.
  * Mailgun's **Foundation plan** starts at **$35/month**.
  * Mailgun's **Scale plan** starts at **$90/month**.


4

## What Domain Should I Use?

We recommend using a subdomain with Mailgun, like **mg.mydomain.com**. Using a subdomain, you'll still be able to send emails from your root domain, e.g. **you@mydomain.com**.

Heads Up

If you use a subdomain, make sure you configure MX records for it for optimal delivery. This is configured within your Mailgun account.

Important

You can only add domains you own. You'll need to update the domain's DNS records to verify that you're an authorized owner or sender for that domain.

There are two different ways to set up Mailgun:

Option 1

One Sub-domain

Set up one sub-domain in Mailgun for your agency domain and use that same sub-domain for email sending across all of your client accounts.

Option 2

Multiple Sub-domains

Set up a subdomain in Mailgun for each of your clients' domains and use that subdomain for sending on their specific account. You can also set up a unique domain/subdomain per location to capture cold inbound emails — [learn more about Cold Email Inbound Setup here](<https://help.gohighlevel.com/support/solutions/articles/48001185801-cold-email-inbound-setup>).

Setup Option| Pros| Cons  
---|---|---  
One Sub-domain| Easy setup — only one subdomain to configure for a domain you already control. Emails are white-labeled to your agency domain, or you can use a generic domain to avoid showing any agency branding.| If your domain gets disabled (a bad score due to bounce rates) email stops working for all of your clients, since every account is powered by the same domain. The fix: don't send spammy emails to poor-quality lists.  
Multiple Sub-domains| Emails are white-labeled per client domain. If a client's domain gets disabled, email only goes down for that one client account.| Difficult setup — time-consuming to configure a subdomain for every client and get access to each of their domains.  
  
5

## Frequently Asked Questions

Q: Do I need Mailgun if I'm already using LC Email?

No. New onboarding agencies use LC Email by default, which doesn't require a separate Mailgun setup. Mailgun is typically used for agencies who need their own dedicated bulk-sending infrastructure.

Q: Can I switch from one shared subdomain to multiple client subdomains later?

Yes. You can migrate clients to their own dedicated subdomains at any time, though it requires setting up new DNS records and re-verifying each domain.

Q: What happens if my shared Mailgun domain gets suspended?

With a single shared subdomain, a suspension affects every client using that domain. Keeping your list quality high and avoiding spammy sends is the best way to prevent this.

Q: Do I need to already own the domain I want to use with Mailgun?

Yes. You can only add domains you own, and you'll need to update the domain's DNS records to verify ownership before you can send from it.

Q: Should I use my root domain or a subdomain?

A subdomain (e.g. mg.mydomain.com) is recommended. It keeps bulk sending separate from your root domain's reputation while still letting you send from an address like you@mydomain.com.

Q: Does Mailgun pricing scale with how many clients I send for?

Mailgun's plans (Basic, Foundation, Scale) are priced by sending volume rather than by number of client domains, so adding more clients on the same plan doesn't automatically increase cost — sending volume does.

Related Articles

[Step-by-step guide to set up Mailgun](<https://help.gohighlevel.com/en/support/solutions/articles/48001219824>) [Mailgun Setup Checklist](<https://help.gohighlevel.com/en/support/solutions/articles/48001175336>) [How to Setup Replies in Mailgun](<https://help.gohighlevel.com/en/support/solutions/articles/48000987293>) [Mailgun: Private API Key Setup](<https://help.gohighlevel.com/en/support/solutions/articles/48000981682>)

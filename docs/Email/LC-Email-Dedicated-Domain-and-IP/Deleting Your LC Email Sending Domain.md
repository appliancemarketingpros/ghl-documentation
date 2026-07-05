# Deleting Your LC Email Sending Domain

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003212-deleting-your-lc-email-sending-domain](https://help.gohighlevel.com/support/solutions/articles/155000003212-deleting-your-lc-email-sending-domain)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Infrastructure

How to Delete Your LC Email Dedicated Sending Domain

When and why to remove a dedicated sending domain from your sub-account, where to find it, and how to delete it safely.

Overview

Your LC Email dedicated sending domain is the email domain connected to your sub-account for sending and receiving email communication. You can have multiple domains and sub-domains connected to a single location, so knowing how to add and remove them is important.

[Learn more about LC Email dedicated sending domains →](<https://help.gohighlevel.com/en/support/solutions/articles/48001226115>)

Table of Contents

1

Why You'd Want or Need to Delete Your Domain

2

Where to Find Your Dedicated Sending Domains

3

How to Delete Your Dedicated Sending Domain

4

Frequently Asked Questions

1

## Why You'd Want or Need to Delete Your Domain

There are a few common reasons why you may need to remove a dedicated sending domain from your sub-account.

Reason 1

You Added the Wrong Domain

Sometimes the wrong domain gets added, which prevents the DNS records from connecting correctly and stops email from working. In this case, delete the incorrect domain and add the right one.

Reason 2

You Changed Domains for Your Business

If your business rebrands or moves to a new domain, you'll want your sending domain to match. This is also important for email reputation — providers like Google look for consistency between your sending domain and your business identity when evaluating the legitimacy of your emails.

Reason 3

Your Domain Was Marked as Spam and Deliverability Is Low

High-volume marketing sends can lead to spam complaints that damage your domain's reputation score. When deliverability drops significantly, switching to a fresh domain is often necessary. If you've decided to stop sending from the affected domain entirely, there's no reason to keep it connected to your sub-account.

Note

These are the most common reasons, but there may be others depending on your specific use case and business needs.

2

## Where to Find Your Dedicated Sending Domains

All email sending domains are managed inside the **Email Services** section of your sub-account settings.

Navigation

Settings → Email Services

![Navigating to Settings in the sub-account](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032625907/original/2_-VQ3O57oJG2a_uIc8nPUD56YmP2YHiJg.jpg?1725993012)

![Email Services section in sub-account settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032625911/original/n8zdGiX9Wc_BUq9aRnPIfJ-DplDEDh16nw.jpg?1725993021)

Settings → Email Services — your dedicated sending domains are managed here.

3

## How to Delete Your Dedicated Sending Domain

Once you're in the Email Services section of your location settings, follow these two steps to delete your dedicated sending domain.

Step 1

Open Dedicated Domain Settings

In the Email Services section, look for the **Dedicated Domain and IP** button on the right side of the screen.

Click it to view all connected sending domains on this sub-account.

![Dedicated Domain and IP button in Email Services](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032625704/original/cbPXDzi8WwYJbMJ17V6rRb9yE6k1zvPhkw.jpg?1725992653)

Click "Dedicated Domain and IP" to see all sending domains connected to this location.

Step 2

Delete the Domain

  * Click the **three-dot menu** in the top-left corner of the domain card to open its actions menu.
  * Select **Delete Domain** from the menu.
  * A confirmation popup will appear. Confirm to permanently remove the domain from your sub-account.


![Three-dot actions menu on the domain card](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032625837/original/JlFhET4WPCO06FGgWFn5zSM4zBi37wcfhw.jpg?1725992863)

Click the three-dot menu on the domain card.

![Delete Domain option in the actions menu](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032625843/original/86FJLae4GVP0SsYg0uwhOaSXsdJyJB9h2w.jpg?1725992876)

Select "Delete Domain" from the actions menu.

![Confirmation popup to confirm domain deletion](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032625847/original/Kt2ypyv0iB2fllZW2Pplzpklok_ZRGBAIQ.jpg?1725992888)

Confirm the deletion in the popup. This action cannot be undone.

Important

Deleting a domain from your sub-account is permanent. The domain's DNS association with this sub-account is removed immediately, and any email sending from this location using that domain will stop. You can re-add the domain at any time.

4

## Frequently Asked Questions

Q: What happens after my email domain is deleted from my sub-account?

Once deleted, the DNS association between that domain and your sub-account is removed. The domain itself is not affected — your DNS records at your registrar remain intact. This means you can immediately connect the domain to another email service or re-add it to any sub-account if needed.

Q: Can I reconnect my sending domain to the same sub-account after deleting it?

Yes. You can re-add the domain at any time by going to **Settings → Email Services → Dedicated Domain → + Add Domain** and entering the same domain again. Keep in mind that DNS changes may take some time to propagate depending on your domain hosting provider.

Q: Will deleting my sending domain negatively affect my email deliverability?

It depends on the situation. If the domain you're deleting had a strong, healthy reputation, switching to a new domain means starting fresh — the new domain will need time to build up a positive reputation score, which can temporarily reduce deliverability.  
  
On the other hand, if the domain you're deleting already has a poor reputation due to spam complaints, replacing it with a fresh domain may actually improve your deliverability over time.

Q: Do I need to remove my DNS records from my registrar when I delete the domain?

Not necessarily. Deleting the domain from the platform only removes it from your sub-account — it does not touch your DNS records at your registrar. If you plan to re-add the domain later (to this or another sub-account), you can leave the DNS records in place. If you're moving to a completely different email provider, you may need to update or replace those records.

Q: What happens to emails already scheduled or queued for sending when I delete the domain?

Scheduled emails and active workflows that reference the deleted domain will likely fail to deliver after the domain is removed. Before deleting, it is best practice to pause any active campaigns or workflows tied to that sending domain and redirect them to a different domain.

Q: How many dedicated sending domains can I have per sub-account?

You can connect multiple domains and sub-domains to a single sub-account location. There is no hard limit on the number of dedicated sending domains per sub-account, so you can organize sending domains to match different teams, brands, or use cases.

Related Articles

[How to Set Up a Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001226115>) [How to Migrate My Agency Over to LC - Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>) [SSL Certificate for Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>)

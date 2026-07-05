# Managing Default Unsubscribe Links in LC Email

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001225534-managing-default-unsubscribe-links-in-lc-email](https://help.gohighlevel.com/support/solutions/articles/48001225534-managing-default-unsubscribe-links-in-lc-email)  
**Category:** Email  
**Folder:** LC Email

---

Email Compliance

Managing Default Unsubscribe Links in LC Email

Learn how to enable or disable the default unsubscribe link and how to manually place one using a tag — keeping your emails compliant with CAN-SPAM and GDPR.

Important

This article covers **default unsubscribe links** in LC Email only. If you want to create a **custom unsubscribe experience or link** , see: [Creating and Managing Custom Unsubscribe Links](<https://help.gohighlevel.com/support/solutions/articles/155000004799-creating-and-managing-custom-unsubscribe-links>).

Table of Contents

1

What is an Unsubscribe Link?

2

Why Include an Unsubscribe Link (Legal Compliance)

3

How to Enable / Disable the Default Unsubscribe Link

4

How to Manually Add the Unsubscribe Link

5

What Happens If You Use Both Methods?

6

Frequently Asked Questions

1

## What is an Unsubscribe Link?

An unsubscribe link allows your contacts to opt out of receiving future emails from your business. This is a legal requirement under email compliance laws like the CAN-SPAM Act and GDPR. The LC Email system helps you meet these regulations by automatically including an unsubscribe link in your email footers — unless you choose to disable it.

2

## Why Include an Unsubscribe Link (Legal Compliance)

Beyond best practices, unsubscribe links are a legal requirement under multiple international regulations. Failing to include them can lead to serious financial penalties. Digital laws vary globally, but most countries mandate that marketing emails must include a clear opt-out option.

United States — CAN-SPAM Act

The CAN-SPAM Act (Controlling the Assault of Non-Solicited Pornography And Marketing), enforced by the **Federal Trade Commission (FTC)** , requires all commercial emails to include a clear mechanism for recipients to unsubscribe.

European Union — GDPR

The General Data Protection Regulation (GDPR), mandatory since **May 2018** , includes **Article 17 — the Right to Erasure**. Subscribers can request that their personal data be deleted, and you are legally obligated to honor that request.

Important — GDPR Right to Erasure

If a contact unsubscribes from an email list, they are exercising their right to erasure. As the data controller (the email sender), you are legally required to honor that request and stop processing or retaining their data.

Non-compliance with GDPR can result in a fine of **€20 million or 4% of your company's annual global turnover** — whichever is higher. Including an unsubscribe link ensures that you:

✓

Respect user consent

✓

Stay compliant with local and international laws

✓

Protect your business from costly legal repercussions

✓

Build trust by giving recipients control over their communications

✓

Maintain a clean, engaged contact list

✓

Prevent account suspension due to non-compliant sending practices

3

## How to Enable / Disable the Default Unsubscribe Link

The platform includes an unsubscribe link in all emails by default. You can turn it off if you prefer to manually place your own link — but if you do, you must use the `{{unsubscribe}}` tag in every email.

1

Navigate to Sub-Account Settings → Business Profile

![Sub-Account Settings navigation to Business Profile](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044100029/original/jPgWkvjShX9JZwTacRfVwdZi-Fl8mwG30Q.png?1743083285)

2

Scroll Down to the General Tab

![Business Profile General tab showing unsubscribe link settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044100189/original/CfTkTKvr4DtFzTfisOmVp9OTuVUC_bhSqw.png?1743083377)

3

Customize the Unsubscribe Link

You can personalize the unsubscribe experience by customizing the text or destination of the link. Toggle **"Include Unsubscribe Link"** ON. The content of this setting will be automatically added to the footer of all emails sent from this sub-account.

![Toggle to enable Include Unsubscribe Link in Business Profile General settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044100498/original/_RCWSNzTAdH2audMXJAVTC7oNhavLjklWQ.gif?1743083598)

Important

If you turn off the default unsubscribe link, you **must** manually include the `{{unsubscribe}}` tag in each email to remain compliant with email regulations.

4

## How to Manually Add the Unsubscribe Link

If you prefer full control over placement and formatting, you can insert an unsubscribe link directly into any email using a built-in tag.

How to Use the Tag

Open the LC Email Builder (in Conversations, Email Campaigns, or Email Templates under the Marketing tab). Place your cursor where you want the link to appear, then type or paste:

{{unsubscribe}}

Alternatively, use the built-in custom value called **UNSUBSCRIBE LINK** found under the **EMAIL** custom values section.

![LC Email Builder showing how to insert the unsubscribe tag into an email](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044102505/original/4ten5iXcnoVcQ3IAmA-JQWkblQdKsg-H0g.gif?1743084767)

Please Note

When the email is sent, the `{{unsubscribe}}` tag is automatically converted into a clickable link that lets the contact opt out.

5

## What Happens If You Use Both Methods?

Including more than one unsubscribe link in an email may confuse recipients and impact your branding. Here's what happens when both are active in the same email:

1

**Default unsubscribe link** — automatically added to the footer when enabled in Business Profile settings.

2

**Manual`{{unsubscribe}}` tag** — inserted directly into your email template at a specific location.

If Both Are Active in the Same Email

⚠

Two unsubscribe links will appear — one from the manual tag and one automatically in the footer.

⚠

This creates a cluttered email design that may reduce click-through or conversion rates.

⚠

It may confuse contacts if the two links look different or lead to different destinations.

Best Practice — Use Only One Method Per Email

✓

If you want precise control over placement and appearance, insert `{{unsubscribe}}` manually and **disable** the default footer link.

✓

If the footer position is acceptable, rely on the default setting and skip the manual tag.

6

## Frequently Asked Questions

Q: Is an unsubscribe link required in every email?

Yes — it is legally required. Either the default footer link or the `{{unsubscribe}}` tag must be present in every LC Email message.

Q: Can I change what the unsubscribe link says?

You can't edit the default label produced by the `{{unsubscribe}}` tag, but you can customize the text around it or build a fully branded unsubscribe page. For a fully custom experience, see [Creating and Managing Custom Unsubscribe Links](<https://help.gohighlevel.com/support/solutions/articles/155000004799-creating-and-managing-custom-unsubscribe-links>).

Q: What if I remove the default and forget to add a manual tag?

Your email will send without an unsubscribe link — this is a violation of email compliance policies and can result in the suspension of your sending ability. Always verify that one method is present before sending.

Q: Can I track who unsubscribed?

Yes. You can view unsubscribed contacts in your contact list by filtering for the **Unsubscribed** status.

Related Articles

[What is LC Email?](<https://help.gohighlevel.com/support/solutions/articles/48001220605-what-is-lc-email->) [Creating and Managing Custom Unsubscribe Links](<https://help.gohighlevel.com/support/solutions/articles/155000004799-creating-and-managing-custom-unsubscribe-links>) [Email Sending Guide: Email Best Practices & Email Warm Up](<https://help.gohighlevel.com/support/solutions/articles/155000001021-email-sending-guide-email-best-practices-email-warm-up>)

# Hide The SMTP Setup Help Doc Link

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001065654-hide-the-smtp-setup-help-doc-link](https://help.gohighlevel.com/support/solutions/articles/48001065654-hide-the-smtp-setup-help-doc-link)  
**Category:** Email  
**Folder:** SMTP Providers

---

Agency Settings

Hiding the SMTP Setup Help Doc Link

A short custom CSS snippet to remove the SMTP setup help doc link from your clients' view.

Overview

This article is a brief guide on how to hide the SMTP setup help doc link using a custom CSS snippet in your agency settings.

Table of Contents

1

What this link looks like

2

Hide it with a custom CSS snippet

3

Frequently Asked Questions

1

## What this link looks like

If you don't want your clients to see the SMTP setup help doc link shown below, follow the steps in the next section to hide it.

![The SMTP setup help doc link as it appears by default](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032853011/original/eP8muhxmKz6vk0vz9iAKhy17sMVPvCBtdA.jpg?1726245732)

2

## Hide it with a custom CSS snippet

Step 1

Open Agency Settings

Log into your account and go to **Settings → Agency Settings** , then scroll down to the **Custom CSS** field.

Step 2

Paste the following code
    
    
    .hl__smtp-help-doc {
      display: none;
    }

Step 3

Save your changes

Save the Custom CSS field. The SMTP setup help doc link will now be hidden from view.

Good to Know

If you decide to show the SMTP setup help doc link again later, simply remove this code from the Custom CSS field.

3

## Frequently Asked Questions

Q: Will hiding the link affect my clients' ability to set up SMTP?

No. This only hides the visible help doc link — it doesn't change or restrict the underlying email service settings or functionality.

Q: Where exactly do I paste the custom CSS?

In **Settings → Agency Settings** , scroll down to the **Custom CSS** field and paste the snippet there.

Q: Does this apply to one sub-account or the whole agency?

Custom CSS set at the agency level applies across your agency's client-facing views. Check your specific settings location if you only want it applied more narrowly.

Q: How do I bring the link back later?

Remove the .hl__smtp-help-doc snippet from the Custom CSS field and save — the link will reappear.

Q: Can I hide other elements the same way?

Yes, the same approach works for other elements that expose a stable CSS class — target the class with display: none; in the Custom CSS field.

Q: Could a future update break this snippet?

It's possible if the underlying class name changes in a future release. If the link reappears unexpectedly after an update, check whether the class name has changed.

Related Articles

[How to Setup SMTP Providers](<https://help.gohighlevel.com/a/solutions/articles/48001059689?portalId=48000045315>)

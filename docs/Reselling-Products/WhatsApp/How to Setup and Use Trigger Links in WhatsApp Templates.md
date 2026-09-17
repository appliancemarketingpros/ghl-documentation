# How to Setup and Use Trigger Links in WhatsApp Templates

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006279-how-to-setup-and-use-trigger-links-in-whatsapp-templates](https://help.gohighlevel.com/support/solutions/articles/155000006279-how-to-setup-and-use-trigger-links-in-whatsapp-templates)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# Add Trigger Links to WhatsApp Templates

Add Trigger Link tracking to your WhatsApp V2 templates in CRM to capture button (or link) clicks, branch workflows, and follow up based on real intent with no extra integrations. This guide explains what the feature is, the two ways to add tracked CTAs, setup steps, and limits to help you launch quickly and confidently.

TABLE OF CONTENTS

What is Trigger Link in WhatsApp Templates?  
---  
Key Benefits of Trigger Link in WhatsApp Templates  
Prerequisites  
WhatsApp Trigger Link Options  
Button Limits & Design Guidelines  
How to Set Up & Use Trigger Links  
Frequently Asked Questions  
Related Articles  
  
## What is Trigger Link in WhatsApp Templates?

WhatsApp Templates Trigger Link Support lets you place tracked, automation-ready CTAs in WhatsApp V2 templates. When a contact taps a Trigger Link (as a button or inline link), CRM records the click so your workflows can branch immediately — similar to Trigger Links in email and SMS — enabling targeted offers, timely reminders, and measurable engagement.

**Works with:** WhatsApp V2 sending action inside Workflows| **Tracks:** Which CTA/link a contact tapped  
---|---  
**Automates:** Branches on Trigger Link Clicked, sends follow-ups, sets tags, updates fields, etc.| **Design options:** Trigger Link Button (recommended) or Inline Trigger Link in the body text  
  
## Key Benefits of Trigger Link in WhatsApp Templates

These benefits help you decide when to use Trigger Links and how to structure templates for the best conversion and clean analytics.

  * **Click-level attribution:** See exactly which CTA a contact tapped for precise routing.
  * **Smarter automation:** Branch workflows on the clicked link and send tailored next steps.
  * **Faster testing:** Run controlled A/B tests on button labels or link destinations to improve conversion.
  * **Clean handoffs:** Use tags/fields from clicks to personalize sales or service follow-ups.
  * **No extra tools:** Track natively in CRM — no external tracking required.


## Prerequisites

Confirm access and approvals first so your templates send and track correctly.

  * Active WhatsApp connection (CRM WhatsApp subscription) and completed Meta onboarding
  * Sub-account access with permission to create Templates and edit Workflows
  * One or more Trigger Links created (Marketing → Trigger Links → Links)
  * Approved or approvable WhatsApp V2 templates (category, sample content, and variables filled correctly)


## WhatsApp Trigger Link Options (Choose One or Use Both)

You can place tracked CTAs as buttons or inline links. Buttons are cleaner and easier to tap; inline links are useful when your copy needs a sentence-level link.

  * **Trigger Link Button (recommended):** Add a button whose type is Trigger Link and map it to your link.
  * **Inline Trigger Link (body text):** Insert a variable and map it to a Trigger Link; the link appears inside the message body.


## Button Limits & Design Guidelines

Keep CTAs clear and compliant to maximize clicks and prevent confusion.
    
    
    Limit: Total buttons per message must not exceed 2 (Trigger Link buttons + normal buttons), matching Meta's URL button limit for WhatsApp templates.

  * Prefer 1–2 focused CTAs to reduce choice overload.
  * Use descriptive labels (for example, "See Pricing," "Book Pickup") that map cleanly to workflow branches.
  * Provide sample content for variables during template creation to streamline Meta approval.
  * If sending a follow-up template later (no reply yet), prepare and get that template approved in advance.


## How to Set Up & Use Trigger Links in WhatsApp Templates

Follow the sequence below — from creating Trigger Links to building click-based branches — so you can test quickly and deploy safely.

1| Create a Trigger Link

  * Go to Marketing → Trigger Links → Links.

![Navigating to Marketing, Trigger Links, Links](https://jumpshare.com/share/1hddN9YA9hV2zGO1r5Ur+/GIF+Recording+2025-09-09+at+10.47.53+PM.gif)

  * Click Add Link, name it (for example, "20% Off Introductory Offer"), and paste the destination URL (for example, a landing page with a form).
  * Click Save.

![Saving a new Trigger Link](https://jumpshare.com/share/YI6cvgrsItux5YQdBO5V+/Screen+Shot+2025-09-09+at+10.52.46+PM.png)  
---|---  
2| Create a WhatsApp Template

  * Go to Settings → WhatsApp → Templates and click Create Template.

![Creating a new WhatsApp template](https://jumpshare.com/share/KhynY0il5K98xUlKoRID+/GIF+Recording+2025-09-09+at+10.57.41+PM.gif)

  * Fill in the Template name, set Category (for example, Marketing), and choose the Language.
  * (Optional) Add a Header (for example, an image logo) for visual impact.
  * Write the Body copy. Add variables where needed (for example, contact First Name), and include sample content for approval.
  * (Optional) Add a Footer (for example, "Reply STOP to opt out").

![Adding a footer to the WhatsApp template](https://jumpshare.com/share/5g5li2TrM5VfjL6wWcrE+/GIF+Recording+2025-09-09+at+11.02.14+PM.gif)  
---|---  
3| Add a Triggered CTA (Choose A or B)A) Trigger Link Button (recommended)

  * In the template editor, add Button → Type: Trigger Link.
  * Select the Trigger Link you created in Step 1.
  * Keep total buttons to 2 or fewer.
  * Click Create.

![Adding a Trigger Link button to a template](https://jumpshare.com/share/jpzQXWHgdKAOgfpRixks+/GIF+Recording+2025-09-09+at+11.08.59+PM.gif)B) Inline Trigger Link (body text)

  * Place the cursor in the Body where the URL should appear.
  * Click Add variable, then map that variable to your Trigger Link (for example, "20% Off Introductory Offer").
  * Add sample content (paste the destination URL) for Meta approval.

![Adding an inline Trigger Link variable to the body text](https://jumpshare.com/share/npixuhtkSElsxK1hXAz4+/GIF+Recording+2025-09-09+at+11.18.27+PM.gif)  
---|---  
4| Submit and Approve

  * Click Create/Save to submit the template to Meta for approval.
  * After approval, your template will show as Active.

![Template showing as Active after Meta approval](https://jumpshare.com/share/JJ5VmeiZ0xfp5KlUj0tQ+/Screen+Shot+2025-09-10+at+12.48.13+AM.png)  
---|---  
5| Track via Workflow

  * Go to Automation → Workflows → Create from scratch (name it, for example, "Track 20% Offer – WhatsApp").
  * Click Add New Trigger.
  * Select Trigger Link Clicked as the workflow trigger.
  * Click Add Filters and choose Trigger Link from the dropdown.
  * Select the link you previously created and used in the WhatsApp template.
  * Click Save Trigger.
  * Publish the workflow and monitor results in Workflow History and Template Analytics (delivered, read, button clicks).

![Publishing the workflow and monitoring results](https://jumpshare.com/share/f51lXJvSrIOgHrV8c7Qu+/GIF+Recording+2025-09-10+at+12.54.36+AM.gif)  
---|---  
  
## Frequently Asked Questions

Q: Do I need integrations to track button clicks?

No. Trigger Links are tracked natively in CRM and can power workflow branches.

Q: What's the difference between a Trigger Link button and an inline Trigger Link?

Buttons are cleaner and easier to tap; inline links live in the body text. Both track clicks and can trigger workflow branches.

Q: How many buttons can I use in one message?

The combined total of Trigger Link buttons and normal buttons is two.

Q: Can I follow up if the contact hasn't replied yet?

Yes, but use an approved template for outbound messages that fall outside a reply window.

Q: How do I know which CTA performed best?

Use Template Analytics and Workflow History to compare button and link clicks and downstream conversions.

Q: Can I personalize the template (for example, first name)?

Yes. Insert variables and include sample content for Meta approval; the variable renders per contact at send time.

## Related Articles

WhatsApp Full Setup Guide for Agency

WhatsApp and the Sub-Account Set Up

How to Create a WhatsApp Template

Interactive WhatsApp Messages

WhatsApp Template Statuses and Best Practice

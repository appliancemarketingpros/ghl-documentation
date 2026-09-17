# How to create a WhatsApp Template?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000000861-how-to-create-a-whatsapp-template-](https://help.gohighlevel.com/support/solutions/articles/155000000861-how-to-create-a-whatsapp-template-)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

WhatsApp Templates

How to Create a WhatsApp Template

Create WhatsApp templates in HighLevel using supported content, variables, media, and buttons. The template builder now validates common variable errors inline so you can correct them before saving and submitting the template to Meta.

What You'll Learn

Learn how to create and submit a WhatsApp template, add valid numbered variables, fix inline validation errors, and avoid common variable-placement issues before Meta review. You will also learn how the updated Reputation review-request preset handles variables automatically.

Table of Contents

  1. What is a WhatsApp Template?
  2. Key Benefits
  3. Template Category Validation
  4. Before You Create a Template
  5. How to Create a WhatsApp Template
  6. Variable Validation Rules
  7. Submit and Track Approval
  8. Edit, Resubmit, or Clone a Template
  9. Frequently Asked Questions
  10. Related Articles


# What is a WhatsApp Template?  
  


WhatsApp templates are pre-approved message formats used for business-initiated WhatsApp communication. HighLevel lets you build templates with text, variables, optional media, and interactive buttons before submitting them to Meta for approval.

The template builder now checks supported variable syntax and placement while you create the template. Invalid variables are flagged inline so they can be corrected before the template is saved.

## Key Benefits of WhatsApp Template Variable Validation  
  


Inline validation helps catch formatting mistakes while the template is still being written, reducing avoidable corrections after submission and making variable requirements easier to understand.

  * **Immediate feedback:** Invalid variables are identified directly in the template builder.
  * **Fewer avoidable rejections:** Common variable-format problems can be corrected before submission.
  * **Clearer formatting:** The builder guides users toward supported numbered placeholders such as `{{1}}` and `{{2}}`.
  * **Reliable presets:** New Reputation review-request templates use a valid structure without ending the body in a variable.


## Template Category Validation  
  


Selecting the correct template category helps Meta understand the purpose of your message. Category requirements are separate from variable validation, so both the message content and variable structure should be correct before submission.

  * **Marketing:** Promotional offers, announcements, engagement, and similar promotional communication.
  * **Utility:** Transactional or customer-requested updates such as confirmations, reminders, and service information.
  * **Authentication:** Authentication and verification messages that follow Meta's supported authentication structure.


## Before You Create a WhatsApp Template  
  


Confirming WhatsApp access and preparing your message content in advance helps you move through template creation without interruptions.

  * The sub-account has an active WhatsApp subscription.
  * WhatsApp onboarding has been completed successfully.
  * You know the appropriate template category and language.
  * You have realistic sample values ready for any variables used in the template.


## How to Create a WhatsApp Template  
  


Creating the template in the correct order makes it easier to validate required fields, variables, and sample content before submission.

Step 1

Open WhatsApp Templates

From your sub-account, go to **Settings > WhatsApp > Templates**, then click **Create Template**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080743368/original/nqmo51R1VzVXawLINWrgqOHsYkYcBLkw1g.png?1789145369)

Step 2

Complete the Template Details

  * **Template Name:** Enter a supported template name using lowercase letters and underscores.
  * **Category:** Select Marketing, Utility, or Authentication based on the message purpose.
  * **Language:** Select the template language.
  * **Header:** Optionally add text, supported media, or a custom variable where available.


Step 3

Add the Body, Footer, and Variables

Write the main message in the **Body**. Use **Add Variable** for dynamic placeholders such as `{{1}}` and `{{2}}`. A short Footer can also be added when needed.

Enter a realistic sample value for every variable used so Meta can review how the completed message will appear.

Step 4

Add Optional Buttons

Add supported interactive buttons when your template requires an action, such as Quick Reply, Visit Website, Call Phone Number, Copy Offer Code, or Marketing Opt-Out.

## Variable Validation Rules  
  


The template builder now checks supported variable syntax and Body placement as you type. When a supported validation rule fails, the affected field is flagged inline and the template cannot be saved until the variable is corrected.

Rule| Valid| Invalid  
---|---|---  
**Numbered placeholder**| `{{1}}`, `{{2}}`| `{{1$}}`  
**Balanced braces**| `{{1}}`| `{{1` or `{{1}}}`  
**Body placement**| `Hi {{1}}, your appointment is confirmed.`| `{{1}} your appointment is confirmed.`  
  
Body Variable Placement

A WhatsApp template **Body cannot begin or end with a variable**. Add regular text before and after the placeholder.

**Valid:** `Hi {{1}}, your order is ready.`  
**Invalid:** `{{1}} your order is ready.`  
**Invalid:** `Your order is ready for {{1}}`

Header and Body Validation

Malformed variables are validated in both the **Header** and **Body**. The beginning/end placement restriction specifically applies to the Body. Correct the highlighted variable before saving the template.

### Reputation Review-Request Preset

The default Reputation review-request preset has been updated so new templates no longer end with a trailing variable. New review-request templates created from the preset should meet the Body variable-placement rule without requiring a manual correction.

## Submit and Track Approval Status  
  


Inline variable validation removes common formatting problems before submission, but Meta still reviews the full template for category, content, and policy compliance.

  1. Review the template content, category, variables, sample values, and buttons.
  2. Correct any inline variable-validation errors.
  3. Click **Create** when the template is ready.
  4. Go to **Settings > WhatsApp > Templates** to monitor the template status.


**Important:** Passing inline variable validation does not guarantee Meta approval. A template can still be rejected for category, content, policy, duplicate-template, or other review requirements.

## Edit, Resubmit, or Clone a WhatsApp Template  
  


Existing templates can be updated after a rejection or cloned when you want to reuse an approved structure. Variable validation also helps catch supported formatting problems while editing cloned or resubmitted content.

Edit or Resubmit

  1. Go to **Settings > WhatsApp > Templates**.
  2. Open the three-dot menu for the template.
  3. Select **Edit template** , make the required changes, then submit again.


Clone a Template

  1. Open the three-dot menu for the template you want to duplicate.
  2. Select **Clone template**.
  3. Rename the template and update any content, variables, or buttons as needed.
  4. Correct any inline validation errors, then create the new template.


## Frequently Asked Questions  
  


Q: Why can't I save my WhatsApp template?

Check the Header and Body for highlighted variable errors. Invalid tokens, missing or extra braces, or a Body that starts or ends with a variable must be corrected before saving.

Q: What variable format should I use?

Use numbered placeholders such as `{{1}}`, `{{2}}`, and `{{3}}`. Keep the braces balanced and avoid unsupported characters inside the placeholder.

Q: Can the Body start or end with a variable?

No. Add regular text before and after the variable. For example, use `Hi {{1}}, your appointment is confirmed.` rather than starting the message with `{{1}}`.

Q: Does inline validation guarantee Meta will approve my template?

No. Inline validation catches the supported variable-format and placement issues described above. Meta still reviews the template for category, content, policy, and other approval requirements.

Q: Do I need to fix the default Reputation review-request template?

New Reputation review-request templates use an updated preset that no longer ends with a trailing variable, so no manual change is required for that specific issue.

### Related Articles  
  


  * [WhatsApp Template Statuses and Best Practice](<https://help.gohighlevel.com/support/solutions/articles/155000001623>)
  * [WhatsApp Template Categorization Guidelines](<https://help.gohighlevel.com/support/solutions/articles/155000001058-template-categorisation-guidelines>)
  * [WhatsApp Media Templates](<https://help.gohighlevel.com/support/solutions/articles/155000002330>)
  * [How to Setup and Use Trigger Links in WhatsApp Templates](<https://help.gohighlevel.com/support/solutions/articles/155000006279-how-to-setup-and-use-trigger-links-in-whatsapp-templates>)
  * [WhatsApp Settings](<https://help.gohighlevel.com/support/solutions/articles/155000006911>)
  * [How to Send Review Requests via WhatsApp](<https://help.gohighlevel.com/support/solutions/articles/155000004326>)

# WhatsApp Template Statuses and Best Practice

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001623-whatsapp-template-statuses-and-best-practice](https://help.gohighlevel.com/support/solutions/articles/155000001623-whatsapp-template-statuses-and-best-practice)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

WhatsApp TemplatesWhatsApp Template Statuses and Best PracticesUnderstand WhatsApp template approval, inline variable validation, common rejection reasons, sending requirements, and template statuses in HighLevel.  
---  
  
What You'll Learn

Learn how WhatsApp template review works, which variable problems are now caught before saving, which issues can still cause Meta rejection, how to interpret template statuses, and what to check before sending.

Table of Contents

  1. What are WhatsApp Message Templates?
  2. Key Benefits of WhatsApp Template Best Practices
  3. Template Migration
  4. Sample Variable Values
  5. Variable Validation Before Save
  6. Approval Process
  7. Common Template Rejection Reasons
  8. Sending WhatsApp Templates
  9. WhatsApp Template Statuses
  10. How to Review and Manage Templates
  11. Frequently Asked Questions
  12. Related Articles


# What are WhatsApp Message Templates?  
  


WhatsApp message templates are pre-approved message formats used for business-initiated Marketing, Utility, and Authentication communication. Approved templates allow businesses to initiate messaging outside the 24-hour customer service window while following WhatsApp requirements.

Templates must be approved by Meta before they can be used. After approval, their quality status can also change based on customer feedback and other quality signals.

## Key Benefits of WhatsApp Template Best Practices  
  


Following template formatting and quality best practices helps reduce avoidable submission problems and makes it easier to maintain reliable WhatsApp messaging after approval.

  * **Earlier error detection:** supported variable-format problems are now flagged in the template builder before saving.
  * **Fewer avoidable submissions:** malformed placeholders can be corrected before Meta review.
  * **Clearer approval troubleshooting:** builder validation errors are separated from Meta rejection reasons.
  * **Better template health:** monitoring quality and status changes helps identify templates that may need attention.


## Template Migration — Important Notice  
  


Understanding how templates are brought into HighLevel helps prevent confusion when a template exists in Meta but is not available in the sub-account.

When you first connect your WhatsApp Business Account to HighLevel, existing templates from Meta are imported as part of onboarding.

**After the initial import, templates should be created and managed inside HighLevel for consistent availability in the CRM.**

**Best practice:** Create new WhatsApp templates from **Settings > WhatsApp > Templates** so they are available in the workflows and messaging areas where you intend to use them.

## Sample Variable Values  
  


Sample values show Meta what dynamic content will look like when the template is sent. Every variable used in a template should have a realistic sample value during template creation.

![WhatsApp template sample variable values](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024924194/original/pom_P9j4uQOeludQsVMRpySTTfFyQYWwGQ.png?1713872158)

Add realistic sample values for variables used in the template.

## Variable Validation Before Save  
  


The WhatsApp template builder now validates supported variable formatting while you type. Instead of allowing certain invalid placeholders to be saved and discovered later during review, the affected Header or Body field is flagged immediately and saving is blocked until the error is corrected.

Validation Rule| Valid Example| Invalid Example  
---|---|---  
**Use numbered variables**| `{{1}}`, `{{2}}`| `{{1$}}`  
**Use balanced braces**| `{{1}}`| `{{1` or `{{1}}}`  
**Add text around Body variables**| `Hi {{1}}, your order is ready.`| `{{1}} your order is ready.`  
  
Body Placement Rule

A template Body cannot begin or end with a variable. Add regular text before and after the placeholder. This placement rule applies specifically to the Body.

Header and Body Validation

Malformed variables such as unsupported characters, missing braces, or extra braces are flagged in both the **Header** and **Body** where variables are supported.

### Reputation Review-Request Preset

The default Reputation review-request preset has also been updated. New templates created from the preset no longer end the Body with a trailing variable, so the preset meets the new Body-placement validation rule without requiring a manual correction.

## Approval Process  
  


Passing the builder's inline checks confirms that the supported variable-validation rules have been satisfied. Meta still reviews the complete template for category, content, formatting, and policy compliance.

**Approved:** The template becomes available for sending and may initially display **Active - Quality Pending**.

**Rejected:** Review the reason provided by Meta, correct the template when possible, and follow the available edit, resubmit, or appeal path.

**Important:** Inline variable validation reduces avoidable formatting mistakes but does **not** guarantee template approval.

## Common Template Rejection Reasons  
  


Some variable-format problems are now prevented before saving, while other formatting, content, or policy issues may still be identified during Meta review. Knowing the difference helps you troubleshoot at the correct stage.

### Caught Before Save

  * Malformed or unbalanced variable braces, such as `{{1` or `{{1}}}`.
  * Unsupported variable tokens or characters, such as `{{1$}}`.
  * A Body that begins or ends with a variable.


### May Still Be Identified During Submission or Meta Review

  * Non-sequential variables, such as `{{1}}`, `{{2}}`, and `{{4}}` when `{{3}}` is missing.
  * Too many variable parameters relative to the message content.
  * Content that does not meet WhatsApp Business or Commerce requirements.
  * Requests for prohibited or sensitive information.
  * Threatening, abusive, or otherwise prohibited content.
  * Unsupported character, length, or formatting requirements.
  * Duplicate templates with substantially the same Body and Footer content.


![WhatsApp template rejection example](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024924765/original/bANeo0nAPgu7BC2MFPs18SXmyeDD8Nrz7Q.png?1713872446)

## Sending WhatsApp Templates  
  


Approved templates allow your business to initiate supported WhatsApp conversations, including communication outside the 24-hour customer service window.

Once a template is **Active** , it can be selected in supported messaging areas. Continue monitoring template quality because a previously active template can later be paused or disabled.

**Best practice:** Send relevant messages to contacts who expect to hear from your business. Negative feedback can affect template quality and availability.

## WhatsApp Template Statuses  
  


Template status tells you whether a message is still being reviewed, ready to send, experiencing quality issues, or unavailable. Check the current status before troubleshooting a template that cannot be used.

Status| What It Means  
---|---  
**In Review**|  Meta is reviewing the template.  
**Rejected**|  The template was not approved. Review the rejection reason before editing, resubmitting, or appealing.  
**Active - Quality Pending**|  Approved and ready to send, but not enough quality feedback has been collected yet.  
**Active - High Quality**|  The template is active and has strong quality signals.  
**Active - Medium Quality**|  The template is active but receiving some negative quality signals. Monitor it closely.  
**Active - Low Quality**|  The template remains active but is at greater risk of being paused.  
**Paused**|  The template cannot currently be sent because of quality-related restrictions.  
**Disabled**|  The template is unavailable for sending.  
**Appeal Requested**|  An appeal has been submitted and is awaiting a decision.  
  
![WhatsApp template status view](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024925270/original/MeSdtU1yIn3tBYgblzakubUS9tTBMZi0OA.jpeg?1713872747)

## How to Review and Manage WhatsApp Templates  
  


Checking template status and validation errors from one place makes it easier to determine whether a template needs editing, additional review time, or quality improvements.

  1. Go to **Settings > WhatsApp > Templates**.
  2. Locate the template you want to review.
  3. Check its current status before making changes.
  4. If you are creating or editing a template, correct any inline Header or Body variable errors before saving.
  5. If Meta rejected the template, review the rejection reason and update the applicable content or formatting.
  6. After approval, continue monitoring quality status as the template is used.


For complete creation instructions, see [How to Create a WhatsApp Template](<https://help.gohighlevel.com/support/solutions/articles/155000000861-how-to-create-a-whatsapp-template->).

## Frequently Asked Questions  
  


Q: Why can't I save my WhatsApp template?

Check the Header and Body for inline variable errors. Unsupported tokens, missing or extra braces, or a Body that starts or ends with a variable must be corrected before saving.

Q: What variable format should I use?

Use numbered placeholders such as `{{1}}`, `{{2}}`, and `{{3}}`. Keep both braces balanced and do not add unsupported characters inside the placeholder.

Q: Can a template Body begin or end with a variable?

No. Add regular text before and after the variable. The builder now flags this placement problem inline and prevents saving until it is corrected.

Q: If the builder accepts my variables, is Meta approval guaranteed?

No. Inline validation only confirms the supported variable-format and placement rules checked by the builder. Meta can still reject a template for other formatting, content, category, duplication, or policy reasons.

Q: Why was my template rejected even though no variable error appeared?

The template may have failed another Meta requirement, such as category alignment, content or policy rules, unsupported formatting, duplicate content, or other parameter requirements.

Q: Does the Reputation review-request preset need to be manually fixed?

New Reputation review-request templates use an updated preset that no longer ends the Body with a trailing variable, so no manual correction is required for that specific validation rule.

Q: What should I do if an active template moves to Low Quality or Paused?

Review the message content and audience relevance, reduce behavior that may be generating negative feedback, and monitor the template's quality status before continuing high-volume usage.

### Related Articles  
  


  * [How to Create a WhatsApp Template](<https://help.gohighlevel.com/support/solutions/articles/155000000861-how-to-create-a-whatsapp-template->)
  * [Why WhatsApp Templates Are Rejected with an “Invalid Format” Error](<https://help.gohighlevel.com/support/solutions/articles/155000006330-why-whatsapp-templates-are-rejected-with-an-invalid-format-error>)
  * [WhatsApp Template Categorization Guidelines](<https://help.gohighlevel.com/support/solutions/articles/155000001058-template-categorisation-guidelines>)
  * [WhatsApp Media Templates](<https://help.gohighlevel.com/support/solutions/articles/155000002330>)
  * [WhatsApp Quality Rating, Status Changes, and Messaging Limits](<https://help.gohighlevel.com/support/solutions/articles/155000002659-about-your-whatsapp-business-phone-number-s-quality-rating>)
  * [WhatsApp: Send Message Templates](<https://help.gohighlevel.com/support/solutions/articles/155000003069>)

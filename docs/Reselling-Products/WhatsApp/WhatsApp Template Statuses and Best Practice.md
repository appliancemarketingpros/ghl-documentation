# WhatsApp Template Statuses and Best Practice

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001623-whatsapp-template-statuses-and-best-practice](https://help.gohighlevel.com/support/solutions/articles/155000001623-whatsapp-template-statuses-and-best-practice)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

Feature GuideWhatsApp Message TemplatesEverything you need to know about creating, submitting, and managing WhatsApp message templates in HighLevel.  
---  
What you'll learn| ✓ Template approval process| ✓ Common rejection reasons| ✓ Sending templates| ✓ Template statuses explained  
---|---|---|---  
  
* * *

**TABLE OF CONTENTS**

  * Overview
  * Template Migration — Important Notice
  * Approval Process
  * Common Template Rejection Reasons
  * Sending WhatsApp Templates
  * WhatsApp Template Statuses
  * Frequently Asked Questions


* * *

OverviewWhat are WhatsApp message templates and why do you need them?  
---  
  
Templates are pre-approved message formats used to open **marketing** , **utility** , and **authentication** conversations with customers. They are the only type of message that can be sent to customers who have not messaged you in the last 24 hours, or who have never contacted your business before.

All templates must be **approved by Meta** before they can be sent. Once approved, templates can still be automatically paused or disabled if they receive negative customer feedback or low engagement.

* * *

⚠️ Template Migration — Important NoticePlease read this carefully before creating templates  
---  
  
When you first connect your WhatsApp Business Account to HighLevel, your existing templates from Meta are **imported once** as part of the onboarding process.

**After this initial import, there is no ongoing sync between Meta and HighLevel.** This means:

| ✘ Templates created directly in Meta Business Manager **after onboarding will not appear** in HighLevel  
---  
| ✘ Changes made to templates in Meta **will not be reflected** in HighLevel automatically  
---  
| ✓ All new templates must be **created directly inside HighLevel CRM** to be available for use  
---  
      
    
    **Important:** Always create and manage your WhatsApp templates inside HighLevel CRM — not in Meta Business Manager. Any template created outside of HighLevel after the initial onboarding will not be synced and will not be available to send from the CRM.

* * *

Approval ProcessWhat happens after you submit a template  
---  
  
Once you create and submit a template, it goes through Meta's review process. This typically takes **up to 24 hours**. Here's what happens next:

| ✅ **Approved** — Status is set to **Active - Quality Pending** and you can start sending it immediately  
---  
| ✘ **Rejected** — You can edit the template and resubmit, or appeal the decision  
---  
      
    
    If your template is approved, its status will be set to **Active - Quality Pending** and you can begin sending it to customers. If rejected, you can [edit and resubmit](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#editing>) it, or [appeal the decision](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#appeals>).

## How to Create a Template

## Sample Variable Values

When submitting templates, always include **sample variable values** to show Meta how the template will look when sent to customers. Samples can be added during template creation and help improve approval rates.

![Template samples screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024924194/original/pom_P9j4uQOeludQsVMRpySTTfFyQYWwGQ.png?1713872158)

* * *

Common Template Rejection ReasonsAvoid these mistakes to get your template approved faster  
---  
  
Templates are most commonly rejected for the following reasons:

| ✘ Variable parameters are missing or have mismatched curly braces. The correct format is `{{1}}`  
---  
| ✘ Variable parameters contain special characters such as `#`, `$`, or `%`  
---  
| ✘ Variable parameters are not sequential — e.g. `{{1}}`, `{{2}}`, `{{4}}` but `{{3}}` is missing  
---  
| ✘ Template content violates the [WhatsApp Commerce Policy](<https://www.whatsapp.com/legal/commerce-policy/>) — prices, fees, or product descriptions must comply  
---  
| ✘ Template requests sensitive information such as full payment card numbers or national ID numbers  
---  
| ✘ Template contains threatening or abusive content — e.g. threatening legal action or public shaming  
---  
| ✘ Template is a duplicate of an existing one — same body and footer wording will be automatically rejected  
---  
  
![Template rejection screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024924765/original/bANeo0nAPgu7BC2MFPs18SXmyeDD8Nrz7Q.png?1713872446)

* * *

Sending WhatsApp TemplatesWhen and how to send approved templates to customers  
---  
  
Once a template's status is set to **ACTIVE** , you can begin sending it to customers. You can send templates at any time — both inside and outside the 24-hour customer service window.
    
    
    A template's status can change automatically from **ACTIVE** to **PAUSED** or **DISABLED** based on customer feedback and engagement. We recommend monitoring status changes regularly and updating any templates that are in danger of being paused or disabled.

* * *

WhatsApp Template StatusesUnderstand what each status means for your templates  
---  
  
Templates can have the following statuses. You can view a template's current status by going to **WhatsApp > Templates > Status**.

Status| What it means  
---|---  
In Review| Template is under review by Meta. Review takes up to 24 hours.  
Rejected| Template was rejected for violating policies. You can edit and resubmit, or appeal.  
Active - Quality Pending| Approved but no quality feedback yet. Ready to send to customers.  
Active - High Quality| Received little to no negative feedback. Best performing status.  
Active - Medium Quality| Receiving some negative feedback. May soon become paused. Monitor closely.  
Active - Low Quality| Multiple customers gave negative feedback. Still sendable but at risk of being paused. Address issues urgently.  
Paused| Paused due to recurring negative feedback. Cannot be sent until quality improves.  
Disabled| Disabled due to recurring negative feedback. Cannot be sent to customers.  
Appeal Requested| An appeal has been submitted and is being reviewed by Meta.  
      
    
    ? Tip: You can view a template's current status by going to **WhatsApp > Templates > Status** inside HighLevel.

![Template status screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024925270/original/MeSdtU1yIn3tBYgblzakubUS9tTBMZi0OA.jpeg?1713872747)

* * *

Frequently Asked QuestionsCommon questions about WhatsApp message templates  
---  
❓ What are WhatsApp message templates and why do I need them?Templates are pre-approved message formats that let you reach out to customers who haven't messaged you in the last 24 hours, or who have never contacted your business before. They are essential for proactive outreach, marketing campaigns, and transactional notifications.  
---  
❓ How are templates different from regular WhatsApp messages?Regular (free-form) messages can only be sent within the 24-hour customer service window — after a customer has messaged you first. Templates can be sent at any time, to any contact, regardless of when they last messaged you.  
---  
❓ How long does template approval take?Approval typically takes **up to 24 hours**. You will receive a notification once a decision has been made by Meta.  
---  
❓ Why was my template rejected?The most common reasons are formatting errors in variable parameters, content that violates WhatsApp's Commerce or Business Policy, or the template being too similar to an existing one. Review the rejection reasons section above and fix the issue before resubmitting.  
---  
❓ My template status changed — what does that mean?Status changes like **Active - Low Quality** or **Paused** reflect how customers are responding to your template. Monitor these statuses regularly. If a template is paused, edit it to improve quality and resubmit for approval.  
---  
❓ What happens if my template receives negative feedback?If your template receives negative feedback or low engagement, Meta may automatically pause it to protect your phone number's quality rating. Pausing duration varies based on quality. You will be notified when a template is paused, and you can edit and resubmit it.  
---  
❓ Can I edit a paused template?Yes. You can edit a paused template to improve its content, then resubmit it for approval. Its status will change to **In Review** until Meta makes a decision.  
---  
❓ I created a template in Meta Business Manager but it's not showing in HighLevel — why?Templates are only imported from Meta **once during the initial onboarding**. After that, there is no ongoing sync. Any templates created in Meta after onboarding must be **recreated directly inside HighLevel CRM** to be available for use.  
---  
✅ You're all set!Always create and manage your WhatsApp templates inside HighLevel CRM. Keep an eye on template quality ratings, respond to feedback quickly, and ensure your templates comply with WhatsApp's policies to maintain high delivery rates.  
---

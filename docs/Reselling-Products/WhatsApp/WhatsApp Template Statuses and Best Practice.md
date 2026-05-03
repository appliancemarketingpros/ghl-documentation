# WhatsApp Template Statuses and Best Practice

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001623-whatsapp-template-statuses-and-best-practice](https://help.gohighlevel.com/support/solutions/articles/155000001623-whatsapp-template-statuses-and-best-practice)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

Templates are used in template messages to open marketing, utility, and authentication [conversations](<https://developers.facebook.com/docs/whatsapp/pricing#conversations>) with customers.

Unlike free-form messages, template messages are the only type of message that can be sent to customers who have yet to message you, or who have not sent you a message in the last 24 hours.

Templates must be approved before they can be sent in template messages. In addition, templates may be disabled automatically based on customer feedback and engagement. Once disabled, a template cannot be sent in a template message until its quality rating has improved or it no longer violates our [business](<https://www.whatsapp.com/legal/business-policy/>) or [commerce](<https://www.whatsapp.com/legal/commerce-policy/>) policies.

* * *

**TABLE OF CONTENTS**

  * Approval Process
  * Common Template Rejection Reasons
  * Sending WhatsApp Templates
  * WhatsApp Template Statuses
  * FAQs


* * *

# Approval Process

Once created, templates must undergo an approval process before they can be sent to customers. This process typically takes up to 24 hours. If approved, the template's status will be set to "Active - Quality pending," and you can start using it. If rejected, you have the option to edit and resubmit it for approval or appeal the decision.
    
    
    If your message template is approved, its status will be set to **Active - Quality pending** and you can begin sending it to customers. If it is rejected, you can [edit it](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#editing>) and resubmit for approval, or [appeal](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#appeals>) the decision.

## How to create a template

## Samples

When submitting templates, it's crucial to include sample variable values to visualize how the template will appear to customers. Samples can be added during template creation.

![Template samples screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024924194/original/pom_P9j4uQOeludQsVMRpySTTfFyQYWwGQ.png?1713872158)

* * *

# Common Template Rejection Reasons

Submissions are commonly rejected for the following reasons, so make sure you avoid these mistakes.

  * Variable parameters are missing or have mismatched curly braces. The correct format is `{{1}}`.
  * Variable parameters contain special characters such as `#`, `$`, or `%`.
  * Variable parameters are not sequential. For example, `{{1}}`, `{{2}}`, `{{4}}`, `{{5}}` are defined but `{{3}}` does not exist.
  * The message template contains content that violates WhatsApp's Commerce Policy: When you offer goods or services for sale, all messages and media related to your goods or services — including descriptions, prices, fees, taxes and required legal disclosures — constitute transactions. Transactions must comply with the [WhatsApp Commerce Policy](<https://www.whatsapp.com/legal/commerce-policy/>).
  * The message template contains content that violates the [WhatsApp Business Policy](<https://www.whatsapp.com/legal/business-policy/>): Do not request sensitive identifiers from users such as full payment card numbers, financial account numbers, or National Identification numbers. Requesting partial identifiers (e.g. last 4 digits of a Social Security number) is permitted.
  * The content contains potentially abusive or threatening content, such as threatening a customer with legal action or threatening to publicly shame them.
  * The message template is a duplicate of an existing template. If a template is submitted with the same wording in the body and footer of an existing template, the duplicate will be rejected.


![Template rejection screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024924765/original/bANeo0nAPgu7BC2MFPs18SXmyeDD8Nrz7Q.png?1713872446)

* * *

# Sending WhatsApp Templates

Once a template has been approved (its `status` is set to `ACTIVE`) you may begin sending it to customers.
    
    
    Note that a message template's status can change automatically from ACTIVE to PAUSED or DISABLED based on customer feedback and engagement. For this reason, we recommend that you [monitor status changes](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#monitoring-status-changes>) and take appropriate actions whenever a message template that you rely upon becomes, or is in danger of becoming, paused or disabled.

* * *

# WhatsApp Template Statuses

Templates can have the following statuses.

  * **In-Review:** Indicates that the template is still under review. Review can take up to 24 hours.
  * **Rejected:** The template has been rejected during our review process or violates one or more of our policies. See [Appeals](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#appeals>).
  * **Active - Quality pending:** The message template has yet to receive quality feedback or read-rate information from customers. Templates with this status can be sent to customers. See [Quality Rating](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#quality-rating>).
  * **Active - High Quality:** The template has received little to no negative customer feedback. Templates with this status can be sent to customers. See [Quality Rating](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#quality-rating>).
  * **Active - Medium Quality:** The template has received negative feedback from multiple customers, or low read-rates, but may soon become paused or disabled. Templates with this status can be sent to customers. See [Quality Rating](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#quality-rating>).
  * **Active - Low Quality:** The template has received negative feedback from multiple customers, or low read-rates. Templates with this status can be sent to customers but are in danger of being paused or disabled soon. We recommend addressing the issues customers are reporting. See [Quality Rating](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#quality-rating>).
  * **Paused:** The template has been paused due to recurring negative feedback from customers, or low read-rates. Templates with this status cannot be sent to customers. See [Template Pausing](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pausing>).
  * **Disabled:** The template has been disabled due to recurring negative feedback from customers. Templates with this status cannot be sent to customers.
  * **Appeal Requested:** Indicates that an appeal has been requested. See [Appeals](<https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#appeals>).


    
    
    You can view a template's status by going to **WhatsApp > Templates > Status**

![Template status screenshot](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024925270/original/MeSdtU1yIn3tBYgblzakubUS9tTBMZi0OA.jpeg?1713872747)

* * *

# FAQs

## **Q: What are WhatsApp message templates and why do I need them?**

WhatsApp message templates are pre-written message formats that let you initiate conversations with customers who haven't messaged you recently or haven't interacted with your business previously. They're crucial for proactive communication, marketing, and customer support.

## **Q: How are message templates different from regular WhatsApp messages?**

Regular WhatsApp messages can be sent freely to customers who have messaged you within the last 24 hours. Templates require approval and are the only way to reach out to new contacts or those who haven't been active within the last 24 hours.

## **Q: How long does the template approval process take?**

Approvals typically take up to 24 hours. You'll receive a notification once a decision is made.

## **Q: What are the common reasons my template might get rejected?**

Formatting errors with variables, content violating WhatsApp's policies, or the template being too similar to an existing one. Carefully review the policies and check your template's formatting.

## **Q: My template's status changed. What does that mean?**

Template statuses (like "Active - Low Quality" or "Paused") reflect customer feedback. Monitor these statuses to ensure you're only sending high-quality, well-received templates.

## **Q: What happens if my template receives negative feedback or low engagement?**

If your template receives negative feedback or low engagement, it may be paused automatically to protect the quality rating of your phone numbers. Pausing durations vary based on the template's quality rating, and you will be notified when a template is paused.

## **Q: Can I edit a paused template?**

Yes, you can edit a paused template to improve its content and address any issues contributing to negative feedback or low engagement. Once edited, you can resubmit it for approval, and its status will change to "In Review" until approved.

# How to Resubscribe After Unsubscribing from an Email List

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002948-how-to-resubscribe-after-unsubscribing-from-an-email-list](https://help.gohighlevel.com/support/solutions/articles/155000002948-how-to-resubscribe-after-unsubscribing-from-an-email-list)  
**Category:** Email  
**Folder:** Deliverability

---

Resubscribe gives contacts a simple way to opt back into your marketing emails after they’ve unsubscribed. This article explains how the resubscribe link on the unsubscribe success page works, how it affects DND and reporting, and how to verify everything in the contact record. You’ll also find workflow ideas and FAQs to help you manage consent and deliverability with confidence.

* * *

**TABLE OF CONTENTS**

  * What is Resubscribe in HighLevel?
  * Key Benefits of Resubscribe
  * Where the Resubscribe Link Appears
  * DND & Consent Updates
  * Reporting Notes
  * Automation Ideas (Optional)
  * How To Set Up & Test Resubscribe
  * Frequently Asked Questions
  * Related Articles
  * Configuring Unsubscribe Flows


* * *

# What is Resubscribe in HighLevel?

Resubscribe is a built-in option shown on the unsubscribe success page that lets a contact immediately opt back into email. When clicked, HighLevel updates the contact so they’re eligible to receive marketing emails again. This supports compliant, contact-initiated consent recovery without manual edits to the contact record.

* * *

## Key Benefits of Resubscribe

  


Understanding the value of resubscribe helps teams balance compliance with growth. The benefits below focus on faster recovery of consent, clearer CRM status, and smoother downstream reporting and automation.

  


  * **Frictionless consent recovery:** Contacts can opt back in with one click from the unsubscribe success page.  
  


  * **Cleaner CRM status:** Updates the contact’s email eligibility so you don’t need manual DND toggles.  
  


  * **Better campaign continuity:** Enables re-engagement sequences once a contact opts back in.  
  


  * **Compliance-friendly workflow:** Captures a positive, contact-initiated action to help support consent records.  
  


  * **Operational efficiency:** Reduces support tickets asking, “Please add me back.”


* * *

## Where the Resubscribe Link Appears

  


Knowing where the link displays helps you test end-to-end and set expectations for your team. The link appears on the unsubscribe success page after a contact completes an unsubscribe action.  
  


  * The resubscribe option shows on the **unsubscribe success page** after a contact opts out from an email.  
  


  * Availability may depend on the **unsubscribe flow type** configured in your account (One-Step, Two-Step, or Dynamic). Review your flow configuration to understand the exact experience (see **Configuring Unsubscribe Flows** in Related Articles).  
  


  * If you use **default LC Email unsubscribe links** or **custom unsubscribe implementations** , confirm the success-page behavior in a quick test (steps below).  
  


  * The link is intended for the same contact who unsubscribed; forwarded or altered links may not behave as expected.


  


_Screenshot placeholder & description:_  
_Unsubscribe success page with the**Resubscribe** link highlighted near the confirmation message._

* * *

## DND & Consent Updates

  
Resubscribe changes a contact’s eligibility to receive email. Learn what to look for so you can verify the change and keep consent records clear.  
  


  * Clicking **Resubscribe** updates the contact so they can receive marketing emails again (email eligibility).  
  


  * Verify the change in the contact record by reviewing **DND** status and **Activity/Consent** history.  
  


  * Use notes or tags (e.g., `Resubscribed - {date}`) to preserve auditability for your team.


_Screenshot placeholders & descriptions:_

  * _Contact record showing DND/Email status**before** resubscribe (Email = Unsubscribed/Blocked)._

  * _Contact record showing DND/Email status**after** resubscribe (Email = Eligible/Not in DND)._


  


_![image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066384601/original/p2MmPWsO9dTPjttroOcfJVK20reDjHgMzw.png?1772809466)_

* * *

## Reporting Notes

  


Campaign analytics may not immediately reconcile unsubscribe and resubscribe events. Set expectations with your team and choose the right reports when validating metrics.  
  


  * Some campaign statistics may still show the contact under **unsubscribed** for a period of time, even after they resubscribe.  
  


  * When validating performance, compare **message-level** and **contact-level** data, and check known timing/aggregation behavior in your email reporting documentation.  
  


  * Consider segmenting reports by **current eligibility** to get an accurate audience snapshot for future sends.  
  


* * *

## How To Set Up & Test Resubscribe

  


A quick test validates your unsubscribe flow, confirms the resubscribe link appears, and verifies the change in the contact record before you rely on it in production.  
  


  1. **Prepare a test contact**

     * Create or identify a contact you can email.

     * Confirm they can receive emails (not currently suppressed).  
  


  2. **Send a simple test email**

     * Include the **default unsubscribe link** in the footer (or your configured unsubscribe method).

     * Send the email to your test contact.  
  


  3. **Unsubscribe using the email**

     * Open the email and click **Unsubscribe**.

     * Complete the unsubscribe flow and reach the **success** page.  
  


  4. **Click “Resubscribe” on the success page**

     * On the success page, click the **Resubscribe** link to opt back in.  
![image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066384685/original/xP1HumHd4hylT7WkTnsSIpkPEZ3qILl3Sg.png?1772809504)

  5. _Screenshot placeholder & description:_  
_Unsubscribe success page with the**Resubscribe** call-to-action highlighted._  
  


  6. **Verify the contact record**

     * Open the test contact and confirm email eligibility is restored (review **DND** and recent **Activity** entries).

     * Add a tag/note such as `Resubscribed - {date}` for internal tracking.  
  
![image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066384818/original/nADOI8yaMIKksmoQjKx7dz4b12iK7b7_LQ.png?1772809563)


* * *

## Frequently Asked Questions

  
**Q: What if a contact resubscribes and later unsubscribes again?**  
A: The most recent action governs eligibility. Historical analytics may still show prior states; use current contact status for future audience targeting.

  
**Q: Can I trigger a workflow when someone resubscribes?**  
A: Yes. Use a Contact/DND status change or comparable trigger to start a confirmation email and tagging sequence.

  
**Q: Does resubscribe affect SMS or other channels?**  
A: Resubscribe is designed to restore **email** eligibility. Channel-specific preferences should be managed independently per your DND settings.

  
**Q: How fast do reports update after resubscribe?**  
A: Some statistics may continue to show the contact as unsubscribed for a period. Validate using contact-level status and recent activity when reconciling.

  
**Q: Will the resubscribe option work with custom unsubscribe implementations?**  
A: If you’ve customized the unsubscribe experience, confirm the success page includes the resubscribe option by running a quick test.

  
**Q: Can I bulk-resubscribe contacts?**  
A: Resubscribe is a contact-initiated action from the unsubscribe success page. For manual exceptions, follow your compliance and consent procedures.

  
**Q: What’s the best practice after someone resubscribes?**  
A: Send a short confirmation, provide preference links, and start a gentle re-engagement sequence rather than immediately adding to large broadcasts.

* * *

### Related Articles

  * ### 

[Configuring Unsubscribe Flows ](<https://help.gohighlevel.com/en/support/solutions/articles/155000006071>)  
  


  * [Managing Default Unsubscribe Links in LC Email ](<https://help.gohighlevel.com/en/support/solutions/articles/48001225534>)  
  


  * [Creating & Managing Custom Unsubscribe Links ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004799>)  
  


  * [Workflow Trigger: Contact/DND Change ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002477>)

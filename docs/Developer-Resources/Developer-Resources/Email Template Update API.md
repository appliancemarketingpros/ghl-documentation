# Email Template Update API

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007942-email-template-update-api](https://help.gohighlevel.com/support/solutions/articles/155000007942-email-template-update-api)  
**Category:** Developer Resources  
**Folder:** Developer Resources

---

This article explains how to update an existing HighLevel Email Builder template and its email settings using the PATCH /emails/builder/:templateId API endpoint. It covers supported fields, the simplified editor payload, setup steps, best practices, and common questions for developers managing templates through API integrations.

  

    
    
    **IMPORTANT** : For full endpoint details, request parameters, and response information, refer to the official API documentation: [Update a template with settings](<https://marketplace.gohighlevel.com/docs/ghl/emails/patch-template/>)

* * *

**TABLE OF CONTENTS**

  * What is Updating Email Builder Templates and Email Settings Using the API?
  * What is the Email Builder Template Update Endpoint?
  * Key Benefits of Updating Email Builder Templates by API
  * Supported Email Settings
  * Simplified Editor Payload
  * Updating Template Content and Settings Together
  * Workflow Template Considerations
  * Frequently Asked Questions


* * *

## **What is Updating Email Builder Templates and Email Settings Using the API?**

  


Updating Email Builder templates and email settings using the API allows developers to make changes to an existing Email Builder template without manually editing it inside HighLevel. With the PATCH /emails/builder/:templateId endpoint, you can update template content and supported email settings in a single API call.

  


This is useful for agencies, developers, and integration partners who manage email templates programmatically. Instead of making separate updates for template content and email settings, this endpoint helps streamline the update process while maintaining existing update behavior.

* * *

## **What is the Email Builder Template Update Endpoint?**

  


The Email Builder Template Update endpoint allows you to update an existing Email Builder template by using its templateId. This endpoint is designed for users who need API-based control over template content and supported email settings, such as subject line, sender details, and preview text.

  


**Endpoint** :

PATCH /emails/builder/:templateId

  


This endpoint supports updates to existing Email Builder templates. It can be used to update template content, email settings, or both in one request.

  


**Important** : This endpoint updates an existing Email Builder template. It should not be assumed to update sent campaigns, scheduled campaigns, or workflow email copies unless that behavior is confirmed for your specific use case.

* * *

## **Key Benefits of Updating Email Builder Templates by API**

  


API-based template updates help teams manage email content more efficiently, especially when working across multiple templates, locations, or integrations. This can reduce manual editing and make it easier to keep template content and settings consistent.

  


  * **Single API Call:** Update template content and supported email settings together instead of making separate changes.  
  

  * **Full Template Control:** Manage existing Email Builder template content through the API.  
  

  * **Email Settings Support:** Update subject, fromName, fromEmail, and previewText.  
  

  * **Cleaner Payload Structure:** Use editorType and editorContent instead of the previous structure using type, html/dnd, and isPlainText.  
  

  * **Automatic Plain Text Handling:** isPlainText is now derived automatically, reducing the need to send that value manually.  
  

  * **Backward Compatibility:** Existing update behavior is maintained while supporting the simplified payload.  
  

  * **Faster Campaign Preparation:** Quickly update reusable templates before using them in campaigns or other email workflows.


* * *

## **Supported Email Settings**

  


Email settings define how the email appears to recipients before and after they open it. Updating these fields through the API helps ensure the template has the correct sender information, subject line, and preview text before it is used.

The endpoint now supports updating the following email settings:

  


Field| Description| Required  
---|---|---  
`subject`| The email subject line displayed in the recipient’s inbox.| No  
`fromName`| The sender name displayed to recipients.| No  
`fromEmail`| The sender email address displayed to recipients.| No  
`previewText`| The short preview text shown by many inbox providers near the subject line.| No  
  
  


All template settings fields are optional. You can send only the fields you want to update.

  


**Validation note:** `fromEmail` is validated for proper email format. If an invalid email format is provided, the request may fail validation.

  


**Screenshot Placeholder:** Add a screenshot showing the Email Builder settings panel where subject, sender name, sender email, and preview text are configured in the HighLevel UI.

* * *

## **Simplified Editor Payload**

  


The simplified editor payload reduces the number of fields needed when updating template content. Instead of manually passing separate values for editor type, HTML or drag-and-drop content, and plain text status, the updated structure uses `editorType` and `editorContent`.

  


Previously, integrations may have used fields such as:

  


  * `type`
  * `html`
  * `dnd`
  * `isPlainText`


`  
`

The simplified structure uses:

  


  * `editorType`
  * `editorContent`


`  
`

With this update, `isPlainText` is derived automatically. This means you no longer need to manually send `isPlainText` when using the simplified editor payload.

  


Example simplified structure:
    
    
    {
      "editorType": "html",
      "editorContent": "<html><body><p>Your updated email content</p></body></html>"
    }

The exact `editorType` value should match the supported editor type for the template being updated.

**Screenshot Placeholder:** Add a screenshot or diagram showing the simplified payload structure with `editorType` and `editorContent` highlighted.

* * *

## **Updating Template Content and Settings Together**

  


Updating content and settings together is helpful when a template needs both design or copy changes and inbox-facing updates. For example, you may want to update the body content, subject line, sender name, and preview text at the same time.

  


Example request body:
    
    
    {
      "editorType": "html",
      "editorContent": "<html><body><p>Updated email template content.</p></body></html>",
      "subject": "Updated Email Subject",
      "fromName": "Your Business Name",
      "fromEmail": "sender@example.com",
      "previewText": "A short preview of your updated email."
    }

  


Because all template settings fields are optional, you can include only the fields that need to change.

Example request body for updating only email settings:
    
    
    {
      "subject": "New Subject Line",
      "fromName": "Your Business Name",
      "fromEmail": "sender@example.com",
      "previewText": "Updated inbox preview text."
    }

  


Example request body for updating only template content:
    
    
    {
      "editorType": "html",
      "editorContent": "<html><body><p>Only the template content is updated.</p></body></html>"
    }
    
    
    

* * *

## **Workflow Template Considerations**

  


Email templates used inside workflow steps may behave differently depending on how the template was added and whether edits are synced. A saved template added to a workflow may become a copied version inside the workflow step, so updates to the original template may not always apply to that workflow email.

  


Before relying on API updates for workflow emails:

  


  * Confirm whether the workflow email is synced with the original template.  
  

  * Review the workflow email step after updating the template.  
  

  * Test the workflow email before activating or relying on the automation.  
  


For workflow-specific behavior, review <span style="color:blue">Managing Email Templates in Workflow Steps</span>.

* * *

## **Frequently Asked Questions**

  


**Q: Can I update only the subject line without changing the template content?**  
Yes. All template settings fields are optional, so you can send only the `subject` field if that is the only value you want to update.

  


  


**Q: Can I update sender details through this endpoint?**  
Yes. The endpoint supports updating `fromName` and `fromEmail`.

  


  


**Q: Is`fromEmail` validated?**  
Yes. `fromEmail` is validated for proper email format.

  


  


**Q: Do I still need to send`isPlainText`?**  
No. With the simplified payload structure, `isPlainText` is derived automatically.

  


  


**Q: What fields replaced the older editor payload structure?**  
The simplified payload uses `editorType` and `editorContent` instead of the previous structure using `type`, `html/dnd`, and `isPlainText`.

  


  


**Q: Can this endpoint update both content and settings in one request?**  
Yes. You can update template content and supported email settings in a single API call.

  


  


**Q: Does this update existing templates only?**  
Yes. The endpoint is used to update an existing Email Builder template identified by `templateId`.

  


  


**Q: Will this automatically update templates already copied into workflows?**  
Not always. Workflow email behavior may depend on whether the workflow email is copied or synced with the original template. Review the workflow email step after updating a template.

  


  


**Q: What should I do after updating a template through the API?**  
Open the template in HighLevel, review the updated content and settings, then preview and test the email before using it.

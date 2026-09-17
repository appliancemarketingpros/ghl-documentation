# How to Use Merge Fields and Email Fallback Values

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008467-how-to-use-merge-fields-and-email-fallback-values](https://help.gohighlevel.com/support/solutions/articles/155000008467-how-to-use-merge-fields-and-email-fallback-values)  
**Category:** Merge Fields & Custom Variables  
**Folder:** Merge Fields & Custom Variables

---

Merge fields insert saved data into emails, messages, documents, workflows, calendars, and supported AI prompts. When the content is generated, a token such as `{{contact.first_name}}` is replaced with information from the relevant record. Use this guide to insert merge fields, add email fallback text, and troubleshoot missing values.

* * *

**TABLE OF CONTENTS**

  * What Are Merge Fields ?
  * Key Benefits of Merge Fields
  * Merge Fields, Custom Fields, and Custom Values
  * How Merge Fields Find the Correct Data
  * Common Merge Fields
  * How To Use Merge Fields 
  * How To Add Fallback Values in Emails
  * Troubleshooting Merge Fields
  * Frequently Asked Questions
  * Need Help?


  


* * *

# **What Are Merge Fields ?**  
  


A merge field is a placeholder that retrieves information from a platform record when content is generated. The contact, appointment, invoice, Company, booking, or other record available to the action determines which value appears.  
  


**Template:**  
  


`Hi {{contact.first_name}}, your appointment starts at {{appointment.only_start_time}}.`

  
**Generated message:**  
  


`Hi Sarah, your appointment starts at 3:30 PM.`  
  


**Recommended:** Insert fields through the Merge Field or Custom Value picker. The picker shows the fields supported by the area you are editing and reduces errors from manually typed tokens.

* * *

## **Key Benefits of Merge Fields**  
  


Merge fields make reusable content more personal without requiring manual edits for every recipient.  
  


  * **Personalization:** Add names, dates, booking details, invoice totals, and other saved information automatically.  
  

  * **Consistency:** Pull information directly from its platform record instead of retyping it.  
  

  * **Reusable templates:** Use one message or document for multiple recipients.  
  

  * **Faster automation:** Add dynamic data to workflows, campaigns, reminders, and supported AI prompts.


* * *

## **Merge Fields, Custom Fields, and Custom Values**  
  


These features work together, but each serves a different purpose.  
  


Type| Purpose| Example  
---|---|---  
**Custom field**|  Stores information that can differ by contact, Opportunity, Company, or another supported record.| Preferred service  
**Custom value**|  Stores reusable information that remains consistent across templates.| Support email address  
**Merge field**|  Retrieves a standard field, custom field, or custom value inside supported content.| `{{contact.first_name}}`  
  
* * *

## **How Merge Fields Find the Correct Data**  
  


Merge fields require the correct record context. A valid field can still resolve as blank when the required record or saved value is unavailable.  
  


  * **Contact fields** require a contact.  
  

  * **Appointment fields** require an appointment.  
  

  * **Invoice fields** require an invoice.  
  

  * **Company fields** use the Company associated with the contact.  
  

  * **Service-booking fields** require a Services booking.  
  

  * **AI fields** depend on the records available during the conversation or call.  
  


For example, a contact-only workflow may populate `{{contact.first_name}}` but leave `{{appointment.start_time}}` blank because no appointment is available to that workflow.  
  


**Raw phone format:** Fields ending in `_raw` remove spaces, parentheses, and dashes. Use raw phone values in links, tracking parameters, and other areas that require an unformatted number.

* * *

## **Common Merge Fields**  
  


The examples below cover frequently used fields. Use the picker for the complete list supported by the editor and record context you are using.

Category| Common Merge Fields  
---|---  
**Contact**| `{{contact.first_name}}`, `{{contact.name}}`, `{{contact.email}}`, `{{contact.phone_raw}}`  
**User**| `{{user.name}}`, `{{user.email}}`, `{{user.calendar_link}}`  
**Appointment**| `{{appointment.start_time}}`, `{{appointment.reschedule_link}}`, `{{appointment.cancellation_link}}`  
**Calendar**| `{{calendar.name}}`  
**Account**| `{{location.name}}`, `{{location.email}}`, `{{location.phone}}`  
**Current date**| `{{right_now.middle_endian_date}}`, `{{right_now.year}}`  
**Message**| `{{message.subject}}`, `{{message.body}}`  
**Invoice**| `{{invoice.number}}`, `{{invoice.total_amount}}`, `{{invoice.url}}`  
**Service booking**| `{{servicebooking.title}}`, `{{servicebooking.start_time}}`, `{{servicebooking.total_price}}`  
  
* * *

## **How To Use Merge Fields**  
  


Using the picker inserts the exact token supported by the current editor and helps prevent formatting errors.  
  


  1. Open the supported email, message, workflow action, document, calendar setting, or AI prompt.  
  

  2. Place the cursor where the personalized information should appear.  
  

  3. Click the **Merge Field** , **Custom Value** , or **{ }** icon.  
  

  4. Search for the field or open its category.  
  

  5. Select the field to insert its token.  
  

  6. Review the complete sentence around the token.  
  

  7. Save your changes.  
  

  8. Test using a record that contains the required data.  
  

  9. Confirm the correct value appears before publishing or activating the automation.  
  


**Best practice:** Use the picker instead of manually typing or copying tokens. Available fields can vary by product, account configuration, and record context.

* * *

### **Format List or Array Values in Workflow Text Fields**

  


List or array values can contain multiple records, such as order line items or data received through an Inbound Webhook. When supported list data is available in the workflow context, you can choose which field to extract and control how those values appear inside a workflow text field.

  


When you select a detected list or array from the Custom Value picker, an inline formatter appears instead of inserting the value immediately.

  


The formatter lets you configure:

  


  * **Field:** Choose the field you want to extract from each item in the list.


  


  * **Format:** Display the extracted values as comma-separated text, a bulleted list, a numbered list, or with a custom separator.


  


  * **Empty-list fallback:** Optionally provide fallback content for an empty list.


  


  * **Preview:** Review how the selected field and formatting will appear before inserting it.


  


After configuring the list, select **Insert** to add it at the cursor position. HighLevel saves the formatting rules with the value and renders the current list data when the workflow runs.

Text, number, date, and other single-value fields continue to use the existing instant-insert behavior.

  


**Example:** An Inbound Webhook provides a `line_items` list containing a `sku` field. You can select `sku`, choose a comma-separated format, and insert the formatted list into a supported workflow text field.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155081003042/original/pb3FCmp80TVtp7F_5ByU3xowWPexEc16Wg.gif?1789489398)

* * *

## **How To Add Fallback Values in Emails**  
  


Email fallback values prevent awkward blank spaces when a field has no saved value. They are supported in email templates, workflow emails, campaign emails, and bulk emails, including subject lines, preview text, and email body content.  
  


  1. Create or edit the email.  
  

  2. Insert or locate the merge-field tag.  
  

  3. Click the tag to open the **Default Text** editor.  
  

  4. Enter the text that should appear when the original value is empty.  
  

  5. Click **Save**.  
  

  6. Send a test using a contact whose field is blank.  
  


![Default Text editor showing a fallback value for an email merge field.](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079788325/original/ZwqbZCfohuF14VOFVitOafJ4ffJJPiMY8Q.png?1788259727)

  
**Example:**  
  


`Hi {{contact.first_name}}, your appointment is confirmed.`

Fallback text: `there`

When the first name is missing, the email displays:  
  


`Hi there, your appointment is confirmed.`

**Important:** A fallback applies only to that specific use of the merge field. It does not update the contact record, and the same field can use different fallback text elsewhere in the email.

* * *

## **Troubleshooting Merge Fields**  
  


Most merge-field issues are caused by missing source data, missing record context, or an unsupported field placement.  
  


Issue| What to Check  
---|---  
The value is blank| Confirm that the source record contains data and the action has the required record context.  
The raw token remains visible| Delete it and reinsert it from the picker. Confirm that the editor supports the field.  
The wrong user appears| Check the assigned user, appointment owner, or sender available to the action.  
A Company field is blank| Confirm that the contact is associated with the correct Company and that the selected field contains data.  
An email fallback does not appear| Confirm that the fallback was saved for that specific tag in a supported email area.  
An AI Agent uses the value awkwardly| Add instructions for missing values and test the prompt again.  
  
* * *

## **Frequently Asked Questions**  
  


**Q: Are merge fields available in editor?**  
No. Available fields depend on the product, editor, enabled features, permissions, and record context.  
  


**Q: Can I type a merge field manually?**  
Yes, but using the picker is more reliable because it inserts the exact supported token.  
  


**Q: Do email fallback values update CRM data?**  
No. A fallback changes only the generated email when the original value is empty.  
  


**Q: Can the same merge field have different fallback values?**  
Yes. Each occurrence in a supported email can have its own fallback text.  
  


**Q: What is the difference between Company and Account fields?**  
Company fields retrieve information from the Company associated with the contact. Account fields such as `{{location.name}}` retrieve information from the account.  
  


**Q: Can Voice AI and Conversation AI use merge fields?**  
Yes, in supported prompt and message fields. Use the Custom Value picker and test the conversation before launch.

* * *

## **Need Help?**  
  


If a merge field is blank, displays the raw token, or returns unexpected information, first confirm that the required source record and value are available when the content is generated.  
  


Before troubleshooting further, verify that:  
  


  * The source field contains a saved value.  
  

  * The action has access to the required record, such as a contact, appointment, Company, invoice, or booking.  
  

  * The merge field was inserted using the **Merge Field** , **Custom Value** , or **{ }** picker.
  * The selected editor supports the merge field you are using.  
  

  * The correct contact, assigned user, Company, appointment, or other related record is associated with the action.  
  

  * Email fallback text is saved for the specific merge-field occurrence.  
  

  * Your test record contains the information required to populate the field.  
  


If the issue continues, capture the merge-field token, where it is being used, the source record, and the generated result before contacting support. This information can help identify whether the issue is related to missing data, record context, or field support.

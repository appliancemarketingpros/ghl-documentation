# Facebook Conversions API Trigger in Workflows

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001185099-facebook-conversions-api-trigger-in-workflows](https://help.gohighlevel.com/support/solutions/articles/48001185099-facebook-conversions-api-trigger-in-workflows)  
**Category:** Integrations  
**Folder:** Facebook Integration

---

With Workflows, you can add Facebook Conversion event actions in automation to send conversion data back to Facebook without anyone being cookied by a Facebook pixel!

##   


## **Frequently Asked Questions**

  


**Q: Which initial Workflow Triggers can I use the FB Conversions event with?**

  


  1. For **Funnel events** in Facebook conversion API action, you can use the following triggers; Form Submitted, Survey Submitted, Customer Booked Appointment, and Order Form Submission.  
(For an appointment, it will only work with "Customer Booked appointment," not with "appointment," as appointments are the general triggers and "Customer Booked appointment" is the trigger for the widget; click" [here](<https://help.gohighlevel.com/support/solutions/articles/48001081184>) to learn more.)
  2. **For Lead Events:**

Facebook Lead Form Submission and Pipeline Stage Change are commonly used triggers; however, the Facebook Conversions API action is **not limited to these triggers**.

Other workflow triggers, such as **Contact Tag Added, Opportunity Status Changed, Contact Changed, or similar contact-based triggers** , can also be used **as long as the contact has valid Facebook attribution data available**.

For the conversion to be attributed and sent correctly to Meta, the contact should have Facebook attribution information, such as:

     * `fbclid` / Facebook Click ID (`fbc`), or
     * Paid Social (Facebook) attribution associated with the contact.
  3. For example, if a contact originally entered CRM through a Facebook ad and later has a tag added, a workflow triggered by **Contact Tag Added** can run the Facebook Conversions API action using the Facebook attribution information stored against that contact.

If the contact does not have the required Facebook attribution information, the workflow action may execute in HighLevel, but Meta may not be able to receive or correctly attribute the conversion.


  


**Q: Which Event Details Parameters do we need to use?**

Event Source URL

  


**Q: Which Customer Information Parameters can we use?**

Client IP address - do not hash

Client user agent - do not hash

Email Address

First Name

Surname

Browser ID (fbp) cookie – do not hash

Click ID (fbc) cookie – do not hash

  


**Q: Can I use Custom Values for the Access Token and Pixel Id?**

Yes, Custom Values will work in those fields.

  


**Q: Why isn't the {{Order.Amount}} custom value working with the "Order Form Submission" trigger?**

The {{Order.Amount}} custom value **only works with the Order Submitted trigger** because it relies on a completed payment. It won't work with Order Form Submission, as that trigger fires before payment is processed, so the order amount isn’t finalized yet.

  


**Q: Why don't I see test events in Facebook Business Manager?**

If you don't see a test conversion, check the Diagnostics tab for any errors. A common issue we've seen is when FB has blocked the domain, so check Settings > Scroll to the bottom to "Domains In Your Allow List," where you can approve the domain

  


**Q: How Events Deduplication is Handled?**

  


Event deduplication is handled automatically.

  


Funnels generate an `eventId` and store it with the contact’s attribution data. When a Conversion API action runs, the same `eventId` is sent to Meta (if available), allowing Meta to deduplicate browser and server events. No additional setup is required.

  


**Q: Does the 'Test Workflow' button work with testing FB conversions?**

Yes

  


**Q: Why is Facebook reporting the conversion as "Custom Event" when I selected "Lead"?**

This happens when you send test data (we're not sure why Facebook does this), but it will show "Lead" when you run a live conversion. 

  


**Q: Can I use the offline events with trigger names like 'Call', 'opportunity change status', 'tag', etc. with Facebook Conversion API action?**

  


**Yes.** These triggers can be used when the contact already has valid Facebook attribution information. HighLevel uses the available Facebook attribution data associated with the contact when sending the conversion event to Meta.

For example:

  * A contact enters through a Facebook ad and receives Facebook attribution data.
  * Later, a tag is added or the opportunity status changes.
  * A workflow triggered by that action can send a Facebook Conversions API event using the attribution information already associated with the contact.


**Important:** The workflow trigger itself does not create Facebook attribution data. The contact must already have the required attribution information from a previous Facebook interaction.

  


**Example 1:**

Contact created Facebook form submission, thus first attribution source will be Paid Social (Facebook). If you use workflow with Facebook form submitted trigger, the contact will have fbclid and workflow will send data to conversion API (CAPI).

  


Additional Behaviour -  
After sometime that contact got converted to opportunity with add/update opportunity trigger addition, you use opportunity status trigger in workflow to send the data to conversion api as contact from Facebook form submitted will pass fbclid.

  


**Example 2:**

Contact created google ad, organic google search or direct traffic,, thus first attribution source will be Paid Search (Google) or Direct Traffic. If the contact after certain time interacted with Facebook form and they fill the form, the latest attribution will be Paid Social(Facebook) with contact having fbclid. Now, if the agency runs workflow with Facebook form submitted > Facebook conversion API, it will send the data to conversion API with fbclid.

Additional Behaviour - After sometime that contact got converted to opportunity with add/update opportunity trigger addition, you use opportunity status trigger in workflow to send the data to conversion api as contact from Facebook form submitted will pass fbclid.

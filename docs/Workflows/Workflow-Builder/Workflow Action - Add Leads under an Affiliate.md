# Workflow Action - Add Leads under an Affiliate

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002691-workflow-action-add-leads-under-an-affiliate](https://help.gohighlevel.com/support/solutions/articles/155000002691-workflow-action-add-leads-under-an-affiliate)  
**Category:** Workflows  
**Folder:** Workflow Builder

---

### **What it does**

The "Add Leads under an Affiliate" action assigns a contact (lead) to an affiliate and their associated campaign, making sure affiliates are correctly credited.

  


You can now choose from three assignment methods for total flexibility.

  


**TABLE OF CONTENTS**

  * What it does
  * How to Use It
  * Assignment Methods


* * *

### **How to Use It**

  1. In your workflow, add the action: `**Add Leads under an Affiliate**`

  2. Choose your assignment method:

     * **Manual**

     * **Auto (Attribution)**

     * **Custom Mapping**

  3. Configure additional fields based on the method

  4. Save and publish the workflow


  


### **Assignment Methods**

1\. Manual : Manually assign a lead to a known affiliate in a specific campaign.  
**Best for:** Form submissions, internal routing, admin decisions.

**Steps:**

  * Select campaign
  * Select affiliate (from affiliates in that campaign)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155051076579/original/zf9NeSIstbZrgaKC3kFkK7sZO1-uHeZmgQ.jpeg?1754542880)


2\. Auto (Attribution via URL) : Automatically assign leads using `am_id` passed in the **URL parameters**.  
Supports **first** or **last click** attribution.

**Steps:**

  * Choose Attribution Method: First / Last
  * Make sure `am_id` is passed earlier in the funnel (e.g., form/page URL)![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155051076580/original/63YI_YvbtgPN_nWrRSsPLBAqqOBx6Bdw4A.jpeg?1754542880)


3\. Custom Mapping : Use if `am_id` is stored in a **custom field** or passed as a workflow value.  
**Best for:** API pushes, third-party systems, hidden fields on forms.

**Steps:**

  * Choose mapping source: custom field or workflow value
  * System reads value and assigns the lead to the matching affiliate![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155051076581/original/dAQymuHR9BhRgNu6cyn3hx96MgmIXtnDXw.jpeg?1754542881)


###

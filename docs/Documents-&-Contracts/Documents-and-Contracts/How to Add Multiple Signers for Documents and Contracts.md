# How to Add Multiple Signers for Documents and Contracts

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008358-how-to-add-multiple-signers-for-documents-and-contracts](https://help.gohighlevel.com/support/solutions/articles/155000008358-how-to-add-multiple-signers-for-documents-and-contracts)  
**Category:** Documents & Contracts  
**Folder:** Documents and Contracts

---

Documents & Contracts

# Multi-Role Signing for Documents and Contracts Templates

Define up to 6 signer roles per template and automate multi-party agreements through Workflows

What You'll Learn

Multi-role signing lets you define multiple signer roles (buyer, seller, witness, or custom roles) directly on your Documents and Contracts templates. When you send a document through a Workflow, HighLevel automatically populates and routes each role for signature.

This guide shows you how to configure signer roles on templates, assign fillable elements to each role, and send multi-party agreements through Workflows without manual re-entry.

Table of Contents

1

What is Multi-Role Signing?

2

Key Benefits

3

How Multi-Role Signing Works

4

How to Set Up Multi-Role Signing

5

Overriding Role Details in Workflows

6

Frequently Asked Questions

1

## What is Multi-Role Signing?

Multi-role signing allows you to define multiple signer roles on a single Documents and Contracts template. Each role represents a party to the agreement — buyer, seller, witness, or any custom role you define — and can be assigned specific fillable elements like signature boxes, date fields, and text inputs.

You can configure up to 6 signer roles per template. When you send a document through a Workflow, HighLevel automatically populates each role's details (name, email, phone number) and routes the document for signature in the order you define.

Before multi-role signing, templates supported only a single signer, requiring manual entry of additional parties for every multi-party agreement. Multi-role signing eliminates this repetitive work by letting you define roles once on the template and reuse them across all documents generated from that template.

2

## Key Benefits of Multi Role Signing

Multi-role signing streamlines multi-party agreement workflows and reduces manual data entry errors.

**Save Time on Multi-Party Agreements** — No need to manually re-enter signer details for every buyer-seller, client-co-signer, or tenant-guarantor agreement you send.

**Reduce Data Entry Errors** — Role values set on the template auto-populate when you send the document, cutting down on missed or mistyped signer information.

**Stay Flexible Per-Workflow** — Override any role's name, email, or phone number at the workflow level, so one template can serve many different deals without template duplication.

**Scale Complex Deals** — Real estate, contracting, and services businesses can route agreements requiring multiple signatures (e.g., buyer + seller + witness) in a single send.

**Support Up to 6 Signers Per Template** — Define as many roles as your agreement requires, up to the 6-role limit per template.

3

## How Multi-Role Signing Works

Multi-role signing separates role definition (on the template) from role assignment (in the Workflow). This separation lets you reuse templates across different agreements while maintaining flexibility per send.

Step 1

Define Roles on the Template

You create signer roles (buyer, seller, witness, or custom names) on your template and assign fillable elements (signature boxes, date fields, text inputs) to each role. Each role can have static values or custom field placeholders that resolve when the document is sent.

Step 2

Select the Template in a Workflow

Add the "Send Document" action in a Workflow and choose your multi-role template. HighLevel automatically detects all roles defined on the template and displays them in the Workflow action configuration.

Step 3

Auto-Population and Override

Role values from the template auto-populate in the Workflow action. You can override any role's name, email, or phone number at the workflow level if the specific agreement requires different details. Workflow-level values always take precedence over template defaults.

Step 4

Document Routing

When the Workflow sends the document, HighLevel routes it to each signer in the order you define. Each signer receives a unique signing link and completes their assigned fillable elements. The contact enrolled in the workflow becomes the primary recipient, and all other roles are populated based on the values set in the template or overridden in the Workflow action.

Implementation Guide

Setting Up Multi-Role Signing

Follow these steps to configure roles on your template and send multi-party documents through Workflows

4

## How to Set Up Multi-Role Signing

Follow these steps to configure multi-role signing on your Documents and Contracts template and send the document through a Workflow.

Step 1

Navigate to Documents and Contracts Templates

Go to **Payment****s > Documents & Contracts > Templates**. Open an existing template or create a new one.

The template is where you define which roles exist and what information each role needs to provide. This setup determines how your document will be routed when sent through Workflows.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077844103/original/6ERy16oKZI1l41XuHcZ5Ap2Egb1GbVizMg.png?1786077994)

  


Step 2

Add a Fillable Element to Your Template

In the template editor, add a fillable element — signature box, date field, text input, or any other supported field type. Click on the fillable element you just added.

Every role must have at least one fillable element assigned to it. Fillable elements define what each signer will complete when they receive the document.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077844307/original/MACsaJE0oSgwocuMa59FWEAJan38eU2mbw.png?1786078261)

Step 3

Create a New Role

With a signature element selected, click the **Add Role** option. This opens the role creation form.

The Add Role form is where you define who this signer is (buyer, seller, witness, or a custom role name) and how HighLevel should populate their contact information.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077870251/original/tkKeY9h0uX6gq3MCcUf8b5T1M7gdcmHiNQ.png?1786096043)

  


  


Step 4

Configure the Role Name and Contact Details

In the role creation form, enter a descriptive **Role Name** (e.g., "Witness," "Buyer," "Co-Signer"). This name will appear above the signature field when the signer receives the document.

For each role, you can set the **Name** , **Email** , and **Phone Number** fields in two ways:

  * **Static Value:** Enter a fixed value directly (e.g., "John Smith" or "john@example.com"). Use this when the role's information is always the same.
  * **Custom Field Placeholder:** Select a custom field from your contact records (e.g., {{contact.witness_name}} or {{contact.buyer_email}}). Use this when the role's information varies per contact and you want HighLevel to auto-populate it when the document is sent.


Custom field placeholders let one template serve many different agreements. When a Workflow sends the document, HighLevel resolves the placeholders from the enrolled contact's record, automatically filling in the correct signer details without manual entry.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077844539/original/QnVPKX6Mpspv1lEdes069BYSa05XuieShQ.png?1786078544)

Important

At least one fillable element must be assigned to the "Contact" role. The Contact role represents the primary recipient — the contact who enrolls in the Workflow and triggers the document send. Without a Contact role assignment, the "Send Document" Workflow action will not function properly.

Step 5

Assign Additional Signature to Roles

After creating a role, the signature you clicked is automatically assigned to that role. To assign more signatures to the same role (or to different roles), click add signature element in the template and select the role from the dropdown.

Each role can have multiple signature elements. For example, a "Buyer" role might need to sign, initial, and enter a date. Assigning all relevant fields to the correct role ensures each signer sees only the fields they need to complete.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077871086/original/CjqMEnjhjDp95CXO62S9Rg0yyeSGJEyPzw.png?1786096458)

  


  


Step 6

Save Your Template

Once you've added all roles and assigned fillable elements, click **Save**. Your template is now configured for multi-role signing and ready to use in Workflows.

Saving locks in your role configuration. Any Workflow that uses this template will automatically detect and display all roles you've defined.

Step 7

Add the Template to a Workflow

Navigate to **Automation > Workflows**. Create a new Workflow or edit an existing one. Add the **Send Document** action and select your multi-role template from the template dropdown.

The Workflow is where your template comes to life. When a contact enrolls in this Workflow, HighLevel generates the document with all roles populated and routes it for signature.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077868702/original/Fr3QQ9BsU6MUpD2mx2JJMogzUxefI9khyQ.png?1786095383)

Step 8

Review and Assign Roles in the Workflow

Once you select a multi-role template, HighLevel displays the **Assign Roles** section in the Workflow action configuration. This section shows all roles that have at least one fillable element assigned in the template.

Review the auto-populated role details. If you used custom field placeholders on the template, those placeholders will be visible here and will resolve when the Workflow runs. If you used static values, those values will be shown.

The Assign Roles section gives you one last chance to verify that each role is correctly configured before the document is sent. You can also override any role's details at this step (see Step 9).

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077871351/original/KQ0f0T95gb6HxRBpNKqiBhwFgk3pQZDvnA.gif?1786096609)

Step 9

Override Role Details (Optional)

If a specific agreement requires different details for any role, click **Edit** next to that role in the Assign Roles section. You can manually enter a new name, email, or phone number. Workflow-level values always take precedence over template defaults.

Overrides let you customize per-send without duplicating templates. For example, if your template uses a custom field placeholder for a "Witness" role, but one specific deal requires a different witness, you can enter that witness's details here and HighLevel will use them for this send only.

Step 10

Save and Publish the Workflow

Click **Save** on the Send Document action, then click **Publish** on the Workflow. When a contact enrolls in this Workflow, HighLevel generates the document, populates all role values (from the template or your Workflow overrides), and sends the document to each signer.

The contact who enrolled in the Workflow becomes the primary recipient (assigned to the "Contact" role). All other roles are populated based on the values you set in the template or overridden in the Workflow. Each signer receives a unique signing link via email (if email notifications are enabled in the Workflow action) and can complete their assigned fillable elements.

Publishing activates the Workflow. From this point forward, every contact who triggers this Workflow will receive a fully populated, multi-role document without any manual intervention.

5

## Overriding Role Details in Workflows

Workflow-level overrides let you customize signer details for individual document sends without editing the template. This flexibility means one template can serve many different agreements.

When you select a multi-role template in the "Send Document" Workflow action, HighLevel displays all role details from the template in the Assign Roles section. You can click **Edit** next to any role and change that role's name, email, or phone number directly in the Workflow action configuration. Values you enter at the workflow level always take precedence over the template defaults.

For example, you might have a template with a "Buyer" role set to a custom field placeholder like {{contact.buyer_name}}. For most sends, the Workflow resolves the placeholder from the contact record. But if you need to send to a different buyer for a specific deal, you can manually enter that buyer's details in the Workflow action, and HighLevel will use those values instead of the template default for that send only.

Tip

Use template-level custom field placeholders for roles that rarely change (e.g., your agency's name as a "Seller" role), and override at the workflow level for roles that vary per deal (e.g., different buyers, co-signers, or witnesses). This approach minimizes template duplication while maximizing flexibility.

6

## Frequently Asked Questions

Q: How many signer roles can I define on a single template?

You can define up to 6 signer roles per template. Each role must have at least one fillable element assigned to it.

Q: Do I need to assign the "Contact" role to a template element?

Yes. At least one fillable element must be assigned to the "Contact" role for the "Send Document" Workflow action to function properly. The Contact role represents the primary recipient — the contact who enrolls in the Workflow and triggers the document send.

Q: Can I use custom field placeholders for role details?

Yes. When defining roles on the template, you can use custom field placeholders for name, email, and phone number. HighLevel resolves these placeholders from the contact record when the document is sent. You can also override placeholders with static values at the workflow level if needed.

Q: What happens if I override a role's details in the Workflow?

Workflow-level values always take precedence over template defaults. If you enter a name, email, or phone number in the Workflow action, HighLevel uses those values for that specific send, leaving the template unchanged.

Q: Can I reuse one multi-role template for different deals?

Yes. One template can serve many different agreements. Use custom field placeholders for roles that rarely change, and override role details at the workflow level for roles that vary per deal (e.g., different buyers, co-signers, or witnesses).

Q: What is the signing order for multi-role documents?

HighLevel routes the document to each signer in the order you define when setting up the roles on the template. Each signer receives the document sequentially and completes their assigned fillable elements.

Q: Do all roles need to have signature boxes assigned?

No. Roles can have any combination of fillable elements — signature boxes, date fields, text inputs, or other supported field types. You define which elements each role needs based on your agreement requirements.

Q: Can I use multi-role signing for Proposals and Estimates?

Yes. Multi-role signing works with both Proposal and Estimate templates in the Documents and Contracts product area.

Q: Where can I see all the roles assigned to a sent document?

After a document is sent, navigate to the document view in Documents & Contracts. You'll see all assigned roles and their signing status. Each role shows the signer's name, email, and whether they've completed their signature.

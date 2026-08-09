# Workflow Action: Associate Records

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007718-workflow-action-associate-records](https://help.gohighlevel.com/support/solutions/articles/155000007718-workflow-action-associate-records)  
**Category:** Workflows  
**Folder:** CRM Workflow Actions

---

Workflow Automation

# Associate Records Workflow Action

Automatically create associations between the object and records from a different object using flexible filters and matching strategies.

What You'll Learn

The Associate Records workflow action eliminates manual effort by automatically finding and linking CRM records based on field values, merge fields, and custom matching rules.

This article explains how to configure the action, choose matching strategies, apply association labels, and use real-world workflows to model complex business relationships.

Beta Feature

The Associate Records workflow action is currently available in Beta through Labs. Enable it from **Settings → Labs → Associate Records - Workflow Action** before use. Beta features are in active development and may receive updates based on user feedback.

Table of Contents

1

What is the Associate Records Workflow Action?

2

Key Benefits

3

Feature Capabilities

4

How to Set Up the Associate Records Action

5

Real-World Use Case

6

Related Articles

7

Frequently Asked Questions

1

## What is the Associate Records Workflow Action?

The Associate Records workflow action automatically creates associations between CRM records based on field-level matching rules. It works across Contacts, Companies, Opportunities, and Custom Objects, allowing you to model complex business relationships without manual data entry.

When a workflow enrolls a record, the action searches for matching records using filters you configure—such as matching city, property type, or status—and creates associations using the strategy you define (earliest, latest, or all matches).

This action removes the need for external tools or custom code to maintain CRM relationships, and it keeps associations accurate as records are created or updated.

2

## Key Benefits

The Associate Records action delivers automation, accuracy, and flexibility for managing CRM relationships at scale.

**Reduces Manual Record Association** — Eliminate repetitive association tasks by automating record linking based on field values and business logic.

**Maintains Accurate Associations** — Automatically create associations as records are created or modified, ensuring relationships reflect current data.

**Builds Workflows Across Associated Records** — Create complex automation across standard and Custom Objects, modeling real-world processes directly in the CRM.

**Automates Processes Across Objects** — Replace third-party automation or custom code with native workflow actions that work seamlessly across your CRM.

**Supports Flexible Matching** — Use fixed values or merge fields from the enrolled record to dynamically identify matching records.

3

## Feature Capabilities

The Associate Records action provides flexible configuration options to handle a wide range of CRM workflows and business scenarios.

Feature 1

Multi-Object Support

Associate records across Contacts, Companies, Opportunities, and Custom Objects, based on the workflow type and configured object associations in your sub-account.

Feature 2

Field-Based Filters

Find records using one or more field-based filters with support for all applicable field types and their corresponding operators (equals, is, is not empty, contains, greater than, etc.).

Feature 3

Fixed Values and Merge Fields

Use fixed values (like "4" for bedrooms) or merge fields from the enrolled record (like contact.preferred_city) to dynamically match records based on real-time data.

Feature 4

Matching Strategies

Choose to associate with the earliest created record (the record created first), the latest created record (the record created most recently), or all matching records based on your business requirements.

Feature 5

Association Labels

Apply existing association labels to categorize and describe the relationship between records (e.g., "Potential Buyer", "Seller"). The selected label is applied to the trigger record.

Feature 6

Cross-Object Associations

Create associations between different objects (Contact to Property, Company to Opportunity) based on the associations configured in your sub-account.

Feature 7

Multi-Filter Logic

Add multiple filters with AND logic to create precise matching rules. A record must meet every condition to qualify for association.

4

## How to Set Up the Associate Records Action

Follow these steps to configure the Associate Records action in a Contact, Company, or Custom Object workflow.

Step 1

Enable the Feature in Labs

Navigate to **Settings → Labs** and enable the **Associate Records - Workflow Action** feature.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077497329/original/wO99TV_UQCyIiYu5wGvADNuJAUeJ1IZLjg.png?1785767436)

Step 2

Open or Create a Workflow

Open an existing workflow or create a new Contact, Company, or Custom Object workflow where you want to add the action.

Step 3

Add the Associate Records Action

Click the **+** icon to add a new action. Under the **Associations** category, select **Associate Records** (marked with a BETA tag).

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077507058/original/vs-r6KzVQfT0SpaPnk8kdqGjhTfWzCaroQ.png?1785772549)

Step 4

Name the Action (Optional)

In the **ACTION NAME** field, you can keep the default name "Associate records" or customize it to describe the specific association being created.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077507117/original/a6vuzGxhSqYUeF-ZBqdDQqE-mXoCnl2JvA.png?1785772592)

Step 5

Select the Object to Associate With

Under **CREATE ASSOCIATION WITH** , select the object type containing the records you want to associate (e.g., Property, Campaign, Company, Insurance Policy, Transaction).

Available objects depend on the associations configured in your sub-account. To associate with other object records, visit Associations settings.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077507180/original/kpIHrfIjHiH-ph1_cfi6bs1qyfqnzse0nA.png?1785772622)

Step 6

Configure Filters to Identify Matching Records

Under **FILTER RECORDS TO ASSOCIATE** , add one or more field-based filters. For each filter row:  
  


  * Select the field you want to match (e.g., Bedrooms, City, Property Type)  
  

  * Choose the operator (e.g., Equals, Is, Is not empty)  
  

  * Enter a fixed value or use merge fields from the enrolled record (indicated by the merge field icon)


  


Click **Add field** to add additional filter conditions. All filters use AND logic—a record must meet every condition to qualify.

At least one field-value pair must be provided for the action to work.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077507661/original/G8iRb_qmRhJy-CsqrUkEhsW4PM3rWVRATg.png?1785772870)

Step 7

Choose a Matching Strategy

Under **WHEN MULTIPLE RECORDS MATCH** , select how you want to handle multiple matching records:

  * **Associate with all matching records** — Creates associations with every record that meets the filter criteria
  * **Associate with earliest created record** — Associates only with the record that was created first
  * **Associate with latest created record** — Associates only with the record that was created most recently.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077507694/original/xdv4MzpzKet9doSF3TGhBzYZZbjexxtyMg.png?1785772915)

Step 8

Select an Association Label

Under **ASSOCIATION LABEL** , select an existing label to categorize the association (e.g., "Potential Buyer", "Seller").

The selected label will be applied to the trigger record. Some labels are paired (e.g., "Seller - Paired with Property" and "Potential Buyer - Paired with Interest Property").

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077507725/original/JsyEWQI8VtwXmFguq7qa2aJrDShkW6M_GA.png?1785772962)

Step 9

Save your Changes

Click **Save action** to add the configured action to your workflow. You can also click **Cancel** to discard changes.

Save and publish the workflow to activate the association automation.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077507779/original/V95cjMUVysjwtrIRPjWZn1j_LSD5p0-eUA.png?1785773001)

Step 10

View Your Association

To view the associate after the workflow has ran, go to **Contacts** > **Associations**  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077508422/original/XYDNjNUqwuUH1L4d3ZjtrAvGQSJLCPo7Wg.png?1785773366)**

Success

Once published, the workflow will automatically create associations whenever a record enrolls and matches the filter criteria you configured.

Automation in Action

Build Smarter CRM Workflows

The Associate Records action enables you to automate complex relationship management across Contacts, Companies, Opportunities, and Custom Objects—reducing manual effort and keeping your CRM accurate.

5

## Real-World Use Case

The Associate Records action is ideal for industries that require dynamic, rule-based associations between records. Here's a real estate agency example.

Use Case: Real Estate Buyer-Property Matching

A real estate agency uses a Custom Object called "Property" to track listings. When a new buyer Contact enrolls in a workflow, the Associate Records action automatically searches for Property records that match the buyer's preferences.

**Configuration:**

  * **Create Association With:** Property
  * **Filters:** Bedrooms (Number) equals 4, City (Dropdown single) is contact.preferred_city, Property Type (Dropdown single) is contact.preferred_type, and Property Name (Single line) is not empty
  * **Matching Strategy:** Associate with all matching records
  * **Association Label:** Potential Buyer


**Result:** Each buyer is automatically linked to all matching properties, and agents can see the list of interested buyers directly from each Property record. This eliminates manual association work and ensures buyers see relevant listings immediately.

This automation helps teams create and maintain associations without manually associating records one at a time, saving significant time as new contacts and properties are added to the system.

6

## Related Articles

  * [Getting Started with Workflows](<https://help.gohighlevel.com/en/support/solutions/articles/155000002288>)
  * [Notes on Custom Objects in HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/155000007493>)
  * [Associating Contacts using Custom Labels](<https://help.gohighlevel.com/en/support/solutions/articles/155000003918>)
  * [How to Use Custom Fields](<https://help.gohighlevel.com/en/support/solutions/articles/48001161579>)
  * [Creating and Editing Custom Objects](<https://help.gohighlevel.com/en/support/solutions/articles/155000003897>)


7

## Frequently Asked Questions

Q: Which objects are supported by the Associate Records action?

The action supports Contacts, Companies, Opportunities, and Custom Objects. Available target objects depend on the workflow type and the associations configured in your sub-account.

Q: Can I use merge fields in the filter values?

Yes. You can use merge fields from the enrolled record to dynamically match records based on real-time data—for example, using contact.preferred_city to match a Property's City field.

Q: What happens if no records match the filters?

If no records match the filter criteria, the action completes without creating any associations, and the workflow continues to the next step.

Q: How do I configure associations between objects in my sub-account?

To associate with other object records, visit your Associations settings. This is where you define which objects can be associated and configure association labels.

Q: How do I choose between "earliest", "latest", and "all" matching strategies?

Use "Associate with earliest created record" when you want to link to the oldest matching record. Use "Associate with latest created record" for the most recent match. Use "Associate with all matching records" when you want to create associations with every record that meets your criteria.

Q: Are association labels required?

Yes, you must select an association label when configuring the action. Labels help categorize and describe the relationship between records.

Q: Can I use multiple filters with OR logic?

No. The action currently supports only AND logic—a record must meet every filter condition to qualify for association. OR logic is not supported.

Q: Will the action update existing associations if the enrolled record changes?

The action creates associations when the workflow runs. If the enrolled record changes after enrollment, the associations are not automatically updated. You can configure additional workflow triggers to re-evaluate associations when specific fields change.

Q: Which label is applied to the trigger record?

The association label you select in the action configuration is applied to the trigger record (the record that enrolled in the workflow). If the label is paired, the corresponding paired label is applied to the associated record.

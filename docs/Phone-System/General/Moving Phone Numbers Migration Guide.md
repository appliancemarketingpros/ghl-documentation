# Moving Phone Numbers: Migration Guide

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006369-moving-phone-numbers-migration-guide](https://help.gohighlevel.com/support/solutions/articles/155000006369-moving-phone-numbers-migration-guide)  
**Category:** Phone System  
**Folder:** General

---

Phone Number Migration & Porting

Moving Phone Numbers: Migration & Porting Guide

Choose the correct process for moving one phone number or an entire VoIP inventory between LC Phone, Twilio, HighLevel sub-accounts, or an external carrier.

Overview

Moving a business phone number can mean either **migrating** it between supported phone environments or **porting** it from an external carrier. Choosing the correct path matters because each process has different account requirements, documentation, timelines, and compliance considerations.

This guide acts as the master decision point for LC Phone → Twilio, Twilio → LC Phone, LC Phone → LC Phone, same-agency number moves, and external-carrier or VoIP ports into HighLevel. It also includes dedicated guidance for businesses moving multiple or bulk VoIP numbers.

Use the decision tables below to identify your scenario first, then follow the linked detailed process for that specific move.

Important

Do not delete, release, disable, disconnect, or cancel a phone number with its current provider before a migration or port is confirmed complete. Doing so can interrupt service or jeopardize the transfer.

A separate Twilio Support ticket is **not required** for the supported cross-account LC Phone → Twilio, Twilio → LC Phone, and LC Phone → LC Phone across different agencies processes coordinated by HighLevel Support. This does not mean every scenario in this guide follows the same process.

Table of Contents

What is the Phone Number Migration & Porting Guide? Key Benefits of Choosing the Correct Phone Number Move Migration vs. Porting: What's the Difference? Choose the Correct Phone Number Move What You Need Before Moving Phone Numbers Moving Multiple or Bulk VoIP Numbers How to Set Up the Correct Phone Number Move What to Expect During and After the Move Post-Migration & Porting Validation Checklist Troubleshooting Phone Number Moves Frequently Asked Questions Related Articles

# **What is the Phone Number Migration & Porting Guide?**  
  


The Phone Number Migration & Porting Guide helps you determine how an existing phone number should be transferred based on its current provider, destination, account relationship, country, and number type. Instead of treating every transfer as one generic process, it directs you to the workflow that applies to your specific situation.

The guide covers supported migrations between LC Phone and Twilio, same-agency and cross-agency moves, and ports from external carriers or VoIP providers into HighLevel. It also explains what information to prepare before transferring multiple numbers so larger migrations can be organized before the request begins.

## **Key Benefits of Choosing the Correct Phone Number Move**  
  


Identifying the transfer type before submitting a request prevents unnecessary carrier coordination, missing documentation, incorrect destination details, and avoidable delays. It also helps you understand what must be reconfigured after the number reaches its destination.

  * **Correct Transfer Path:** Distinguish a phone-system migration from a carrier port before starting.
  * **Fewer Delays:** Gather the correct Account SID, Location ID, carrier records, billing documents, or regulatory information in advance.
  * **Bulk Planning:** Organize multiple VoIP numbers according to the process that actually applies to them.
  * **Better Cutover Preparation:** Keep source services active and plan validation before changing live call or messaging traffic.
  * **Compliance Readiness:** Verify A2P 10DLC, Toll-Free Verification, and applicable international regulatory requirements after the move.


## **Migration vs. Porting: What's the Difference?**  
  


Migration and porting both preserve an existing phone number, but they describe different transfer types. Knowing which one applies determines whether you use an in-app tool, HighLevel Support, or a carrier porting workflow.

Transfer Type| What It Means| Examples  
---|---|---  
**Migration**|  Moves a supported number between compatible phone environments or account structures.| LC Phone → Twilio, Twilio → LC Phone, LC Phone → LC Phone.  
**Porting**|  Transfers the number between telecommunications carriers and requires carrier ownership information or authorization.| External VoIP carrier, landline carrier, wireless carrier, or another non-Twilio provider → HighLevel.  
  
## **Choose the Correct Phone Number Move**  
  


Start with where the number currently lives and where it needs to go. The table below replaces the previous one-size-fits-all process and shows which workflow applies before you gather documents or contact Support.

Scenario| Transfer Type| Primary Process  
---|---|---  
**Case 1: LC Phone → Twilio**|  Migration| HighLevel Support coordinates the cross-account move.  
**Case 2: Twilio → LC Phone**|  Migration| HighLevel Support coordinates the cross-account move.  
**Case 3: LC Phone → LC Phone, Different Agencies**|  Migration| HighLevel Support coordinates the inter-agency move.  
**Case 4: LC Phone → LC Phone, Same Agency**|  In-App Move| Use Move Numbers for eligible US and Canada numbers.  
**Twilio → Twilio, Same Master Twilio Account**|  In-App Move| Use Move Numbers when otherwise eligible.  
**External Carrier / VoIP Provider → HighLevel**|  Porting| Use the US Port-In workflow when eligible or the applicable manual/international porting process.  
  
## **What You Need Before Moving Phone Numbers**  
  


The required information depends on whether the number is moving between supported phone environments or being ported from another carrier. Gathering the correct identifiers before starting prevents unnecessary back-and-forth and reduces the likelihood of rejected port requests.

Scenario| Prepare  
---|---  
**LC Phone → Twilio**|  Gaining Twilio Account SID, source HighLevel Location ID, phone number(s), and preferred cutover window.  
**Twilio → LC Phone**|  Losing Twilio Account SID, destination HighLevel Location ID, phone number(s), and preferred cutover window.  
**LC Phone → LC Phone, Different Agencies**|  Destination Location ID, source Location ID when available, phone number(s), and preferred cutover window. A Twilio Account SID is generally not required for this LC-to-LC move.  
**Same-Agency Move Numbers**|  Admin access, source and destination sub-accounts, compatible phone providers, and eligible US or Canada numbers.  
**International Migration**|  Phone number(s), country, number type, applicable Location ID, and Regulatory Bundle SID / Address SID when required for the country and number type.  
**External Carrier / VoIP Port**|  Carrier account information, service address, authorized contact, billing documentation, number list, destination Location ID, and wireless PIN/passcode when applicable.  
  
Phone Number Format

Provide phone numbers in **E.164 format** whenever possible. For example, a US number should appear as **+1XXXXXXXXXX**.

## **Moving Multiple or Bulk VoIP Numbers**  
  


Businesses moving an entire VoIP inventory should first determine whether the numbers are already hosted by LC Phone or Twilio or belong to another VoIP carrier. That distinction determines whether the numbers are migrated or ported and which documents, limits, and timelines apply.

Bulk Scenario| Current Guidance  
---|---  
**Same-Agency Eligible Numbers**|  Move Numbers currently allows up to **10 phone numbers per move**. Complete additional moves for remaining numbers.  
**Cross-Account LC Phone / Twilio Migration**|  Multiple eligible numbers can be included in one HighLevel Support request. Clearly identify the source, destination, and complete number list.  
**Eligible US In-App Port-In**|  Multiple landline numbers can be entered together, and multiple wireless numbers can be added to the request.  
**Manual / External VoIP Port**|  Provide the complete number list in E.164 format plus the required carrier ownership documents and account details.  
  
### **Bulk VoIP Porting Readiness Checklist**  
  


A clean inventory helps prevent one incorrect account detail from slowing down a larger port. Organize the information below before submitting numbers from an external VoIP provider.

  * List every number in E.164 format.
  * Identify whether each number is landline, wireless, local VoIP, or toll-free.
  * Confirm the current carrier or VoIP provider.
  * Confirm the carrier account number.
  * Confirm the legal customer/business name and service address exactly as the carrier has them on file.
  * Collect required wireless PINs or passcodes.
  * Identify the destination HighLevel Location ID.
  * Prepare a current billing statement or other accepted carrier ownership documentation.
  * Keep the source account and numbers active until the port is confirmed complete.


### **Manual Porting Documents**  
  


Manual US ports may require additional documentation when the number cannot use the standard in-app flow. Accurate carrier information is especially important because the losing carrier validates the request against its records.

  * **Signed Letter of Authorization (LOA)**
  * **Latest billing statement** that is no more than 90 days old
  * **Phone number list** in E.164 format
  * **Destination Location ID**
  * **Carrier account number**
  * **Wireless PIN / passcode** when applicable


**Do not cancel the losing carrier before completion.** Keep the phone numbers active until the carrier port is complete and inbound/outbound traffic has been validated in HighLevel.

## **How to Set Up the Correct Phone Number Move**  
  


Once you identify the correct source and destination, follow only the workflow that applies to that transfer. Using a migration process for an external carrier port—or a porting process for an LC Phone account move—can create unnecessary delays.

###   
**Case 1: LC Phone → Twilio**

Use this path when an LC Phone-managed number needs to move into a customer's own Twilio account. HighLevel Support coordinates the supported cross-account migration.

  1. Collect the **gaining Twilio Account SID**.
  2. Collect the HighLevel **Location ID** currently holding the number.
  3. Prepare all phone numbers in E.164 format.
  4. For international numbers, prepare applicable regulatory information required by the country and number type.
  5. Submit the complete migration request to HighLevel Support.


[ View Moving Phone Numbers Across Accounts → ](<https://help.gohighlevel.com/support/solutions/articles/48001240107-moving-phone-numbers-across-accounts-us-and-international->)

### **Case 2: Twilio → LC Phone**  
  


Use this path when a number currently resides in a customer's Twilio account and needs to move into an LC Phone sub-account.

  1. Collect the **losing Twilio Account SID**.
  2. Collect the **destination HighLevel Location ID**.
  3. Prepare all phone numbers in E.164 format.
  4. Prepare applicable international regulatory information when required.
  5. Submit the migration request to HighLevel Support.


[ View Moving Phone Numbers Across Accounts → ](<https://help.gohighlevel.com/support/solutions/articles/48001240107-moving-phone-numbers-across-accounts-us-and-international->)

### **Case 3: LC Phone → LC Phone Across Different Agencies**  
  


Use this path when an LC Phone number needs to move from a sub-account under one HighLevel agency to an LC Phone sub-account under another agency. This is a Support-coordinated cross-account migration.

  1. Collect the **destination Location ID**.
  2. Collect the **source Location ID** when available.
  3. Prepare the phone number list.
  4. Prepare applicable international regulatory information when required.
  5. Submit the migration request to HighLevel Support.


**A Twilio Account SID is generally not required for an LC Phone → LC Phone move across different agencies.**

[ View Moving Phone Numbers Across Accounts → ](<https://help.gohighlevel.com/support/solutions/articles/48001240107-moving-phone-numbers-across-accounts-us-and-international->)

### **Case 4: Move Numbers Between Sub-Accounts in the Same Agency**

Eligible same-agency moves do not use the cross-account Support process. The Move Numbers tool is designed for LC Phone → LC Phone and Twilio → Twilio moves under the same Master Twilio account.

  1. Go to **Agency Settings → Phone Integration → Sub Account Settings**.
  2. Click **Move Numbers**.
  3. Select the source and destination sub-accounts.
  4. Select up to **10 eligible phone numbers** per move.
  5. Review the destination and complete the move.


[ View Moving Numbers Between Sub-Accounts → ](<https://help.gohighlevel.com/support/solutions/articles/48001203968-moving-numbers-tool-across-sub-accounts>)

### **Case 5: Port a Number From an External Carrier or VoIP Provider**  
  


Use porting when the number belongs to a telecommunications provider outside the supported LC Phone/Twilio migration paths. US numbers may qualify for the in-app Port-In Numbers workflow, while unsupported US scenarios and international numbers follow separate porting processes.

#### **Eligible US In-App Port-In**

The current in-app workflow is available to Agency Owners and Agency Admins through Labs and can be used to submit and track eligible US port requests.

  1. Enable the applicable feature through Labs.
  2. Go to **Phone System → Phone Numbers**.
  3. Click **Add Number → Port-in Numbers**.
  4. Enter carrier, number, authorized contact, and service-address details.
  5. Upload the billing statement.
  6. Submit the request and save the Request SID.
  7. Ensure the authorized representative signs the auto-generated LOA and track progress from **Port-In Numbers**.


[ View How to Submit and Track Port-In Number Requests → ](<https://help.gohighlevel.com/support/solutions/articles/155000008078>)

[ View Porting Options: US In-App vs International Manual Process → ](<https://help.gohighlevel.com/support/solutions/articles/48001211919-porting-your-phone-number-non-twilio-number-to-a-location-subaccount>)

## **What to Expect During and After the Move**  
  


Timing and carrier coordination vary substantially between an account migration and a carrier port. Avoid planning around one universal timeline or guaranteed cutover window, and keep source services active until the destination has been validated.

Process| Current Guidance  
---|---  
**Cross-Account Migration**|  Typically approximately **1–2 business days** after HighLevel Support has all required information. International or regulatory-dependent moves may take longer.  
**Same-Agency Move Numbers**|  Completed through the in-app Move Numbers workflow. Verify the destination immediately after completion.  
**External Carrier Port — Fewer Than 50 Numbers**|  Approximately **2–4 weeks** after required documentation is submitted.  
**Larger / More Complex Port**|  Approximately **6–8 weeks** , depending on carrier and complexity.  
**Manual Port Cutover**|  The carrier provides a Firm Order Commitment (FOC) window after approval. Exact or same-day scheduling is not guaranteed.  
  
## **Post-Migration & Porting Validation Checklist**  
  


A number appearing in the destination does not guarantee that routing, messaging registration, compliance, or automation settings are ready. Test the moved numbers before closing the migration or canceling the previous provider.

  1. **Confirm every number appears in the correct destination.**
  2. **Place inbound test calls** from an unrelated phone number.
  3. **Place outbound test calls** using each representative number or number group.
  4. **Test inbound and outbound SMS** when messaging is enabled.
  5. **Review call routing and forwarding** , including assigned users, voicemail, ring groups, and workflows.
  6. **Review workflows and automations** that reference the old number assignment.
  7. **Verify A2P 10DLC** for applicable US 10-digit local numbers before relying on SMS.
  8. **Verify Toll-Free Verification** before sending SMS/MMS from applicable toll-free numbers to US or Canadian recipients.
  9. **Confirm international regulatory requirements** for country- and number-type-specific numbers.
  10. **Cancel the previous carrier only after the port is fully complete and the number is confirmed working.**


**Historical data:** Moving or porting a phone number does not automatically move contacts, conversation history, analytics, historical recordings, or voicemail assets into a new account or phone environment. Export or download anything that must be retained before source access is removed.

## **Troubleshooting Phone Number Moves**  
  


Most transfer problems come from choosing the wrong process, mismatched carrier records, unsupported account relationships, missing regulatory requirements, or post-move messaging configuration. Match the symptom below to the likely cause before resubmitting a request.

Move Numbers Is Unavailable

Confirm both sub-accounts are under the same agency, the phone environments are compatible, and the numbers are eligible US or Canada numbers. Twilio numbers must be under the same Master Twilio account for the in-app move.

A Port Request Is Rejected

Common causes include a mismatched service address, incorrect account number, invalid wireless PIN, unsigned LOA, suspended carrier account, or billing documentation that does not meet current requirements. Verify the information with the losing carrier before resubmitting.

An International Number Cannot Move

International availability and documentation vary by country and number type. Verify the destination's regulatory requirements, Address information, and applicable Regulatory Bundle before continuing.

The Number Moved but SMS Is Not Working

Review the destination's A2P 10DLC registration, Toll-Free Verification, SMS permissions, and country-specific messaging requirements. A successful number transfer does not automatically complete messaging compliance.

The Number Moved but Calls Route Incorrectly

Review forwarding, assigned users, voicemail, inbound call routing, IVR/workflow references, and other number-level settings in the destination.

## **Frequently Asked Questions**  
  


Q: How do I know whether my VoIP numbers need to be migrated or ported?

If the numbers already use LC Phone or a supported Twilio environment, they generally follow a migration path. If they belong to another external VoIP or telecommunications carrier, use the porting process.

Q: Can I move all of my VoIP numbers at once?

It depends on the transfer type. Same-agency Move Numbers supports up to 10 eligible numbers per move. Cross-account migrations can include multiple eligible numbers in one Support request. Eligible US port-in requests can also include multiple landline and wireless numbers.

Q: How long does a cross-account migration usually take?

A typical supported cross-account migration can take approximately 1–2 business days after HighLevel Support receives all required information. International or regulatory-dependent moves may take longer.

Q: How long does an external carrier port take?

Current guidance is approximately 2–4 weeks for port requests involving fewer than 50 numbers and approximately 6–8 weeks for larger or more complex ports. Carrier review and documentation can affect the timeline.

Q: Should I cancel my old phone provider after submitting a port request?

No. Keep the phone numbers and source carrier account active until the port is confirmed complete and you have tested calls and messaging in the destination.

Q: Does A2P 10DLC registration automatically move with a phone number?

Do not assume it does. Verify the destination's A2P registration and confirm applicable US local numbers are associated with the correct approved campaign before sending SMS.

Q: Does Toll-Free Verification move automatically?

Do not assume verification transfers automatically. Confirm the toll-free number's verification status before using it to send SMS or MMS to US or Canadian recipients.

Q: Will my contacts, conversations, recordings, and voicemails move with the number?

No. Moving the number does not automatically migrate contacts, conversations, analytics, historical call recordings, or voicemail assets into another account or phone environment.

Q: Can international phone numbers be moved or ported?

International migration and porting availability varies by country, number type, and carrier. Regulatory Bundles, Address information, supporting documents, or other country-specific requirements may apply. Contact HighLevel Support for international porting.

### **Related Articles**

[ Moving Phone Numbers Across Accounts (US and International) ](<https://help.gohighlevel.com/support/solutions/articles/48001240107-moving-phone-numbers-across-accounts-us-and-international->) [ Moving Numbers Between Sub-Accounts (Same Agency) ](<https://help.gohighlevel.com/support/solutions/articles/48001203968-moving-numbers-tool-across-sub-accounts>) [ Porting Options: US In-App vs International Manual Process ](<https://help.gohighlevel.com/support/solutions/articles/48001211919-porting-your-phone-number-non-twilio-number-to-a-location-subaccount>) [ How to Submit and Track Port-In Number Requests ](<https://help.gohighlevel.com/support/solutions/articles/155000008078>) [ A2P Campaign Registration: Step-by-Step Guide ](<https://help.gohighlevel.com/support/solutions/articles/155000004539-campaign-registration-step-by-step-guide-and-faqs>) [ Toll-Free Number Verification Guide for LC Phone (US/Canada) ](<https://help.gohighlevel.com/support/solutions/articles/48001222300-toll-free-verification-guide-for-lc-phone-us-canada->)

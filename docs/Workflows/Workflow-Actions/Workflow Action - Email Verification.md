# Workflow Action - Email Verification

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007749-workflow-action-email-verification](https://help.gohighlevel.com/support/solutions/articles/155000007749-workflow-action-email-verification)  
**Category:** Workflows  
**Folder:** Workflow Actions

---

Email Verification in Workflows helps validate contact email addresses before email-related workflow steps run. By checking email quality before sending, you can reduce bounces, protect sender reputation, and improve the quality of automated outreach. This article explains what the Email Verification action does, how to configure it, and how to use verification results to control workflow logic in HighLevel.

* * *

**TABLE OF CONTENTS**

  * What is Email Verification Action in Workflows?
  * Key Benefits of Email Verification Action in Workflows
  * Prerequisites for Email Verification
  * How Email Verification Works in Workflows
  * Using Email Verification Results in Workflow Logic
  * Recommended Placement in a Workflow
  * How To Use the Email Verification Action in Workflows
  * Best Practices for Email Verification in Workflows
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Email Verification Action in Workflows?**

  


The Email Verification action validates a contact’s email address inside a workflow before the contact reaches an email step. This helps confirm whether an email address is suitable for sending and gives you more control over how contacts move through automation based on email quality.

  


The Email Verification action can be added anywhere inside a workflow, but it is most commonly placed before a Send Email action. The system checks the contact’s email address and returns a verification outcome that can be used to continue the workflow, branch the contact into a different path, or prevent sending to addresses that may harm deliverability.

  


Email verification may check signals such as:

  


  * Syntax correctness

  * Domain validity

  * Mailbox existence

  * Risk indicators, such as disposable, inactive, or low-quality email addresses


* * *

## **Key Benefits of Email Verification Action in Workflows**

  


  * **Reduces email bounces:** Validate email addresses before sending to reduce failed delivery attempts.  
  


  * **Protects sender reputation:** Avoid sending to invalid or risky addresses that may negatively affect domain reputation.  
  


  * **Improves deliverability:** Support better inbox placement by sending to higher-quality email addresses.  
  


  * **Improves workflow decisioning:** Use verification results to continue, branch, or stop email-related actions.  
  


  * **Supports cleaner contact communication:** Focus email automation on contacts with email addresses that are more likely to receive messages.


* * *

## **Prerequisites for Email Verification**

  


Email Verification must be available and enabled for the sub-account before the workflow action can be used. Confirming access before building the workflow helps prevent setup issues and ensures verification can run as expected.

  


Before using this action, make sure:

  


  * **Email Verification is enabled for the sub-account.**  
**  
**

  * **The Contact is Not Excluded from Verification**

If the contact is excluded from verification, the Email Verification action will be skipped.  
  


  * **The workflow has access to the contact’s email address.**  
**  
**

  * **The action is placed before email-sending steps.**  
**  
**

  * **Any If/Else or condition logic is configured after the Email Verification action.**


  


**For enablement and billing details** , refer to [How to Enable and Rebill LC Email Verification](<https://help.gohighlevel.com/en/support/solutions/articles/48001235221>).

* * *

## **How Email Verification Works in Workflows**

  


Email Verification runs as part of the workflow sequence and checks the contact’s email address before the contact proceeds to later actions. Placing this action before email steps gives the workflow a chance to evaluate email quality before sending.

  


When a contact reaches the Email Verification action, HighLevel evaluates the email address and determines whether it appears valid, risky, or invalid. The workflow can then use the verification result in later actions or conditional logic.

  


Common outcomes include:

  


  * **Valid:** The email address passed verification and is more likely to be safe for sending.  
  


  * **Risky:** The email address may be deliverable but has risk signals that could affect deliverability or sender reputation.  
  


  * **Invalid:** The email address did not pass verification and should generally be excluded from email sends.


  


The workflow outcome depends on how you configure the steps after verification. You can allow verified contacts to continue, route risky contacts into a review or alternate path, or stop email sends for invalid addresses.

* * *

## **Using Email Verification Results in Workflow Logic**

  


Verification results are most useful when paired with workflow conditions. Conditional logic lets you decide what happens after the email address is checked, so contacts do not all have to follow the same path.

  


You can use Email Verification results to:

  


  * Continue the workflow for verified email addresses  
  


  * Send verified contacts to a Send Email action  
  


  * Route risky email addresses to a separate branch  
  


  * Skip email sending for invalid email addresses  
  


  * Stop the workflow or redirect contacts to another action


  


A common setup is to add an If/Else action after Email Verification and use the email verification result as the condition. For example, contacts with `isEmailVerified = true` can continue to the Send Email action, while contacts that do not meet the condition can be routed to another branch.

* * *

## **Recommended Placement in a Workflow**

  


The Email Verification action should usually be placed before any action that sends an email. This ensures the workflow checks email quality before attempting delivery.

  


**Recommended workflow order:**

  


  1. Trigger starts the workflow.  
  


  2. Add the Email Verification action.  
  


  3. Add an If/Else action or verification-based condition.  
  


  4. Send emails only to contacts that meet your verification criteria.  
  


  5. Route risky or invalid contacts to an alternate path, internal notification, tag, or workflow exit.


  


**Example workflow path:**

  


  * Contact enters workflow  
  


  * Email Verification runs  
  


  * If email is verified, continue to Send Email  
  


  * If email is risky or invalid, enable DnD or move the contact to another path  


  


![](https://jumpshare.com/share/hPf0HP6SJCEs3RFTGBoQ+/Screen+Shot+2026-05-12+at+21.04.19.png)

* * *

## **How To Use the Email Verification Action in Workflows**

  


Proper setup ensures the workflow checks email quality before sending messages. Adding the action before email steps and pairing it with decision logic gives you better control over which contacts receive automated emails.

  

    
    
    **Note:** Make sure **Email Verification** is **enabled** for the **sub** -**account** and the **Contact** is**Not Excluded from Verification.**
    

  


  1. Go to **Automation** > **Workflows**.  
  


  2. **Open** an **existing** workflow or **create** a **new** **workflow**.  
  
![](https://jumpshare.com/share/YRpMsB4TIg2S2w1O5fAU+/Screen+Shot+2026-05-12+at+21.18.02.png)  
  


  3. Add a relevant trigger like **Contact Created**.  
  
![](https://jumpshare.com/share/JoSzc90A3vIvZVV6Ji3U+/Screen+Shot+2026-05-12+at+21.24.47.png)  
  


  4. Click **+** to **add****** a **New Action**.  
  


  5. Search for and select **Email Verification** and click on **Save Action** button.  
  
![](https://jumpshare.com/share/q1IOQJjtSDyL81OkUavZ+/Screen+Shot+2026-05-12+at+21.26.18.png)  
  


  6. Place the action before any email action, such as **Send Email**.  
  


  7. Add an **If/Else** **C****ondition** action after Email Verification if you want to branch contacts based on verification results.  
  


  8. **Configure** the **logic** for valid, risky, or invalid email addresses.  
  


  9. Route verified contacts toward email steps.  
  


  10. Route risky or invalid contacts to an alternate path like DnD, or stop the workflow.  
  
![](https://jumpshare.com/share/bvP1Glj1pzRVwuc5dCRv+/GIF+Recording+2026-05-12+at+21.33.23.gif)  
  


  11. Test the workflow to confirm contacts follow the expected path.  
  


  12. **Save** and **Publish** the workflow.  
  
![](https://jumpshare.com/share/C7qmddV32Yz4AK5VkISI+/Screen+Shot+2026-05-12+at+21.35.41.png)


* * *

## **Best Practices for Email Verification in Workflows**

  


Using Email Verification with clear workflow logic helps reduce unnecessary sends and keeps automated communication focused on contacts with better-quality email addresses. Combine verification with strong email-sending practices for better deliverability outcomes.

  


  * Place Email Verification before every important email step where email quality matters.  
  


  * Use If/Else logic to separate verified contacts from risky or invalid contacts.  
  


  * Avoid sending marketing or automated emails to invalid addresses.  
  


  * Treat risky results carefully, especially for high-volume campaigns.  
  


  * Use tags, notes, or alternate paths to track contacts with risky or invalid emails.  
  


  * Review workflow execution history when testing verification logic.  
  


  * Use Email Verification as part of a broader deliverability strategy; it does not guarantee inbox placement.


* * *

## **Frequently Asked Questions**

  


**Q: Where should I place the Email Verification action in my workflow?**  
Place it before any Send Email action or email-related step. This lets the workflow validate the contact’s email address before sending.

  


**Q: Does Email Verification automatically stop the workflow?**  
The outcome depends on how the workflow is configured after the action. You can allow contacts to continue, branch them using If/Else logic, or stop email-related steps for risky or invalid emails.

  


**Q: What does a risky email mean?**  
A risky email may be deliverable but has signals that could affect bounce rate, sender reputation, or deliverability. You may want to route risky contacts to a separate path instead of sending automatically.

  


**Q: Should I send emails to invalid addresses?**  
Invalid addresses should generally be excluded from email sends to reduce bounces and protect sender reputation.

  


**Q: Can I use Email Verification with If/Else conditions?**  
Yes. Add an If/Else action after Email Verification and use the available verification result condition, such as `isEmailVerified`, to control the contact’s path.

  


**Q: Does Email Verification guarantee inbox placement?**  
No. Email Verification helps reduce sending to poor-quality addresses, but inbox placement also depends on sender reputation, content quality, domain setup, engagement, and email best practices.

  


**Q: Does the Email Verification action validate emails in real time?**  
Yes. The action checks the contact’s email address when the contact reaches that step in the workflow.

  


**Q: Do I need Email Verification enabled before using this action?**  
Yes. Email Verification must be enabled for the sub-account before it can be used in workflows.

* * *

### **Related Articles**

  


  * [Workflow Action - If/Else ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002471>)  
  


  * [How to Enable and Rebill LC Email Verification ](<https://help.gohighlevel.com/en/support/solutions/articles/48001235221>)  
  


  * [Workflow Action - Send Email ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002472>)  
  


  * [How to use the Email Risk Assessment Tool for LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/155000000577>)

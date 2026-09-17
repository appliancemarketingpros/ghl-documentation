# Configure SMS Compliance Settings

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004684-configure-sms-compliance-settings](https://help.gohighlevel.com/support/solutions/articles/155000004684-configure-sms-compliance-settings)  
**Category:** Phone System  
**Folder:** LC Phone System

---

SMS Compliance Settings help ensure your outbound SMS messages include the required sender identification and opt-out language when appropriate. These settings automatically add compliance information to your messages, helping support messaging requirements and reducing the risk of carrier filtering.

* * *

**TABLE OF CONTENTS**

  * What is SMS Compliance Settings?
  * Key Benefits of SMS Compliance Settings
  * How SMS Compliance Settings Work
    * 1\. First Outbound Message
    * 2\. Ongoing Conversations
    * 3\. Smart Detection
  * Before You Begin
  * How To Configure SMS Compliance Settings
  * When Settings Cannot Be Disabled
  * Periodic Sender ID & Opt-Out Updates
  * Tips, Guidelines & Rules
  * Frequently Asked Questions
  * Related Articles


* * *

## **What is SMS Compliance Settings?**

  


SMS Compliance Settings ensure that outbound SMS messages meet carrier and policy expectations by automatically appending **opt‑out language** (e.g., “Reply STOP to unsubscribe”) and **sender identification** (e.g., “Thanks, Alex at Main Street Dental”) when those elements are missing. Enabling these controls protects deliverability, reduces filtering risk, and supports a consistent, compliant experience.

* * *

## **Key Benefits of SMS Compliance Settings**

  


Understanding the value makes adoption easy. These benefits map directly to carrier guidelines and practical day‑to‑day messaging needs.  
  


  * **Compliance-by-default** : Automatically appends sender ID and opt‑out language to the first message when missing.  
  


  * **Reduced carrier filtering** : Adds the elements carriers expect, lowering the chance of messages being blocked.  
  


  * **Brand clarity** : **Sender identification** helps recipients recognize who is texting them, improving trust and reply rates.  
  


  * **Automated cadence** : Every‑X‑days control re‑inserts sender ID + opt‑out on a schedule (e.g., every 30 days) to maintain ongoing compliance.  
  


  * **De‑duplication** : Prevents duplicate opt‑out text when you already include it in your message template.


* * *

## **How SMS Compliance Settings Work**

  


Before configuring the settings, it's helpful to understand how they behave.

  


### **1\. First Outbound Message**

  


The first outbound SMS in a conversation automatically includes:

  


  * Sender information  
  

  * Opt-out language


  


This applies even if periodic compliance updates are disabled.

  


  


### **2\. Ongoing Conversations**

  


After the initial message, compliance text is not automatically repeated unless you enable **Periodic Sender ID & Opt-Out Updates**.

  


When enabled, HighLevel checks whether sender information and opt-out language are already present before adding them again.

  


### **3\. Smart Detection**

  


HighLevel does not duplicate compliance language if it detects a complete opt-out instruction already exists in your message.

  


For example:

  


✅ Reply STOP to unsubscribe.

✅ Text STOP to opt out.

❌ "If you want to stop by tomorrow..."

  


Only complete opt-out instructions prevent duplicate insertion. Individual words such as **stop** do not.

* * *

## **Before You Begin**

  


Before configuring SMS Compliance Settings:

  


  * Make sure you're logged into the correct sub-account.  
  

  * Decide whether you'll customize the default sender information or opt-out message.  
  

  * Determine whether you want periodic compliance reminders for ongoing conversations. 


* * *

## **How To Configure SMS Compliance Settings**

  


Follow these steps to configure opt‑out language, sender identification, and the recurring cadence so your messages stay compliant and deliver reliably.

  


  1. From the left menu of your, click on the **Settings** button.  
  
![](https://jumpshare.com/share/K3fdA2BT8KlKgJ2EzeWX+/Screen+Shot+2025-09-23+at+7.31.34+PM.png)  


  


  2. Click on the **Phone System** tab.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155061802556/original/sqNO1OzR2Ek3kFKJHsoPV7XpgGN-AptK_Q.png?1767377093)

  
  


  3. Click on **Messaging** from the top menu-bar.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155061802599/original/RyT_cLfF57VpybC6IAjZQZ6a1iqSkdyoyQ.png?1767377159)  
  


  4. Toggle **Make SMS compliant by adding an opt‑out message** to **ON**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155061802606/original/01V3P84leq1DWtPdeiZ0VdYuF3Hd3eysAg.png?1767377209)  
  


  5. Click on the **Customize** button to edit the opt-out text.  
  
![](https://jumpshare.com/share/HuXKcWb6RjGGRUgdo2w0+/GIF+Recording+2025-09-23+at+7.43.16+PM.gif)  
  


  6. Toggle **Make SMS compliant by adding sender information** to **ON**. Click on the **Customize** button to edit the sender information.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155061802644/original/b7WWvEmaaSWsKFMrXQIZz9GRYacyWrmyNw.png?1767377277)  
  


  7. Toggle **Enable periodic opt-out & sender info** to ON. This controls whether the system re-inserts sender info and opt-out language in ongoing conversations on a recurring schedule.  
  
In **Include sender ID and opt-out message every [1–60] days** , enter a value between **1 and 60**. On or after the interval, the next outbound message to a contact gets the compliance lines re-inserted if missing.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063989629/original/gvxLjON4-y9V-ZJ8gZNtLFvk_Np7LMDguQ.jpeg?1770037661)  
  

  8. Click Save.  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155063989771/original/comzp7Vtr5_iPzp-RcaKAUKzNzXXfHerkA.jpeg?1770037718)**


* * *

## **When Settings Cannot Be Disabled**

  


Depending on your account type, some compliance settings may be required and cannot be turned off.

  


These include:

  


  * Agencies in Trial Mode  
  

  * Sub-accounts created within the last 15 days  
  

  * Account Users and Admins without permission to change these settings


  


These restrictions help maintain consistent messaging compliance across accounts.

* * *

## **Periodic Sender ID & Opt-Out Updates**

  


If enabled, HighLevel automatically re-adds sender information and opt-out language to ongoing conversations.

  


Choose a value between **1 and 60 days**.  
  


On or after the selected interval, the next outbound message will include the compliance information again **only if it isn't already present.**

  


### **Example**

  


If the interval is set to **30 days** :

  


  * First SMS sent on June 1 → compliance information is included.  
  

  * Messages sent throughout June → no additional compliance text is added.  
  

  * The next outbound message sent on or after July 1 may include sender information and opt-out language again if they're missing. 


* * *

## **Tips, Guidelines & Rules**

  


  * The first message in any SMS conversation (including **Missed Call Text Back** and **review requests**) will always include both of the following. Example: _“Reply STOP to unsubscribe.”_  
  

  * The **Opt Out** message will only be added if it is not already included in the message.  
  

  * **Agencies in Trial Mode** cannot disable these checkboxes.  
  

  * **Locations/sub-accounts** created within the last **15 days** cannot disable these checkboxes.  
  

  * **Account Users and Admins** cannot disable these checkboxes.  
  

  * Strong, simple wording improves deliverability and avoids content that may be flagged by carriers.*  
  


  * Sender ID examples: _“Thanks, Jamie at Oak & Co.”_ or _“—Team Acme Fitness.”_  
  


  * Avoid spammy formatting, excessive emojis, URL shorteners, and vague brand references.


###   
**1\. Defaults & Behavior****  
**

**  
**

  * **New sub-accounts:** Enabled by default.  
  


  * **Existing sub-accounts:** Disabled by default.  
  


  * **First outbound message:** Sender info and opt-out language are always included on the first outbound message in a conversation, even if periodic insertion is disabled.


###   
**2\. Smart detection (opt-out suppression)**

  


  * The system suppresses re-insertion only when it detects a **full opt-out phrase** in your message (for example, an unsubscribe instruction), not when it sees a single keyword in normal context.  
  


  * Single words like “stop” inside regular sentences do **not** prevent sender info/opt-out insertion.  
Examples of phrases that should suppress insertion (if already present):  
  


  * “Reply STOP to unsubscribe.”  
  


  * “Text STOP to opt out.”  
  


  * “Reply STOP to end.”  
  
Non-suppression example: “If this time doesn’t work, stop by tomorrow.”


* * *

## **Frequently Asked Questions**

  


**Q: Can I disable sender ID or opt‑out language?**  
If you’re in trial mode, managing a location less than 15 days old, or have restricted user permissions, you may not be able to disable these options. HighLevel recommends keeping them enabled to maintain compliance.

  


  


**Q: What happens if my message already has opt‑out language?**  
A: HighLevel won’t add duplicate opt‑out text; it only appends the required line if it’s missing.

  


  


**Q: How do I customize the opt‑out or sender text?**  
A: Edit the text fields next to each control (or click **Customize** , if shown) in the SMS Compliance tab. Use clear, concise wording (e.g., “Reply STOP to unsubscribe.”).

  


  


**Q: What words are carrier compliant for out-out message?**

STOP, STOPALL, CANCEL, UNSUBSCRIBE, END, or QUIT.

* * *

## **Related Articles**

  


  * [How to Prevent SMS Filtering by Carriers: Error 30007](<https://help.gohighlevel.com/support/solutions/articles/48001237726-how-to-prevent-sms-filtering-by-carriers-error-30007>)  
  

  * [Best Practices for SMS deliverability and Avoiding SMS Restrictions](<https://help.gohighlevel.com/support/solutions/articles/155000000079-best-practices-for-sms-deliverability-and-avoiding-sms-restrictions>)  
  


  * [LC – Phone Messaging Policy](<https://help.gohighlevel.com/support/solutions/articles/48001213941-lc-phone-messaging-policy>)  
  


  * [Phone System Messaging Analytics Overview ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002625>)  
  


  * [Troubleshooting SMS Delivery ](<https://help.gohighlevel.com/en/support/solutions/articles/48000981696>)  
  


  * [Understanding Common SMS Delivery Errors](<https://help.gohighlevel.com/en/support/solutions/articles/48001208912>)

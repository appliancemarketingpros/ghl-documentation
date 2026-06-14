# Spintax: Create dynamic email variations automatically

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008067-spintax-create-dynamic-email-variations-automatically](https://help.gohighlevel.com/support/solutions/articles/155000008067-spintax-create-dynamic-email-variations-automatically)  
**Category:** Marketing  
**Folder:** Templates

---

Improve personalization and reduce repetitive messaging by generating multiple content variations from one template.

  


**TABLE OF CONTENTS**

  * What is Spintax
  * Why Use Spintax?
  * Spintax and Email Deliverability
    * Important
  * Common Use Cases/ Examples:
  * How to Use Spintax:
  * Using Custom Values Inside Spintax


###   
**What is Spintax**

Spintax allows you to create multiple variations of a message using a single template. HighLevel automatically selects one of the available options each time the content is sent, helping make messages feel more natural and less repetitive.

Spintax can be used in almost all email builders, across :

  * Conversations

  * Bulk Actions

  * Workflows

  * Email Builder


* * *

### **Why Use Spintax?**

Spintax is especially useful for cold email outreach, follow-ups, appointment reminders, and automated conversations. Spintax helps you in:

  * Create unique message variations automatically

  * Reduce repetitive content across campaigns

  * Personalize messages at scale

  * Test different messaging styles

  * Improve engagement with more natural communication


* * *

### **Spintax and Email Deliverability**

When every recipient receives the exact same email, mailbox providers may identify the content as highly repetitive.

Spintax helps create variations in your messages by rotating words, phrases, and sentences. This can help reduce content uniformity across large campaigns.

For example, instead of sending: Hey {{contact.firstname}}, you can use - {**SPIN** | Hi|Hello|Hey}

####   


#### _Important_

Spintax should be used thoughtfully. Modern email providers can recognize simple word substitutions, so changing only greetings may have limited impact.

For the best results:

  * Spin complete phrases or sentences instead of single words.

  * Combine Spintax with personalization and Custom Values.

  * Keep all variations natural and conversational.

  * Use Spintax to support testing and content variation, not as a replacement for good email practices.


* * *

### **Common Use Cases/ Examples:**

  * **Greetings**  
{**SPIN** | Hey|Hi|Hello} {{contact.first_name}}  
  

  * **Appointment Reminders**  
{**SPIN** |Just a reminder|Friendly reminder|Quick reminder} about your appointment tomorrow.  
  

  * **Follow-Up Messages**  
{**SPIN** |Checking in|Following up|Wanted to circle back} on our previous conversation.  
  

  * **Calls to Action**  
{**SPIN** |Would you like to learn more?|Interested in hearing more?|Want to schedule a quick call?}  
  

  * **Email Content Variations**  
{**SPIN** |Thanks for your interest|Appreciate your time|Thanks for connecting with us}


* * *

### **How to Use Spintax:**

  1. Open the email editor in HighLevel
  2. Add your content variations inside curly braces after the keyword **"****SPIN"** `{SPIN|}` and separate each option with a pipe `|`.

Example:

{**SPIN** |Hey|Hello|Hi} {{contact.first_name}}![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155073131268/original/x067rUmLsZWN3ws9aHhTx0L32G1dosVfDQ.png?1780912219)

  3. Save your message or template.
  4. When the message is sent, HighLevel automatically selects one of the options at random.


* * *

### **Using Custom Values Inside Spintax**

You can include Contact Fields and Custom Values directly within your Spintax variations. Each variation can contain different merge fields, allowing you to personalize messages in multiple ways.

  
**Example: {SPIN | Hi {{contact.firstname}} | Hi {{contact.lastname}}}**

Possible outputs:

  * Hi John
  * Hi Smith


You can also use Custom Values within your variations:  
**{SPIN | Learn more about {{customvalue1}} | See how {{customvalue2}} can help your business}**

Possible outputs:

  * Learn more about Website Design
  * See how Website Design can help your business


  
**Tip:** Each variation can contain different text, Contact Fields, or Custom Values, giving you greater flexibility when personalizing emails.

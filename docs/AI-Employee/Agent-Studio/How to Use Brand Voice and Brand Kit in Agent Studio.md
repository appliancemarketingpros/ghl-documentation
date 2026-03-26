# How to Use Brand Voice and Brand Kit in Agent Studio

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007510-how-to-use-brand-voice-and-brand-kit-in-agent-studio](https://help.gohighlevel.com/support/solutions/articles/155000007510-how-to-use-brand-voice-and-brand-kit-in-agent-studio)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

Apply your brand’s tone and visual identity directly inside Agent Studio so every AI-generated asset reflects your business consistently. This guide explains how to connect Brand Voices and Brand Kits to your generation nodes and ensure text, images, video, and audio stay aligned with your brand standards.

* * *

**TABLE OF CONTENTS**

  * What Is Brand Voice and Brand Kit in Agent Studio?
  * Key Benefits of Brand Integration in Agent Studio
  * How Branding Works Across Media Types
    * Text Generation
    * Image & Video Generation
    * Audio Generation
  * Brand Board Sync Behavior
  * How to Set Up Brand Voice and Brand Kit in Agent Studio
  * Multi-Brand Workflows
  * Frequently Asked Questions
  * Related Articles


* * *

# **What Is Brand Voice and Brand Kit in Agent Studio?**

  


Brand Voice and Brand Kit allow you to apply your brand identity to AI-generated content inside Agent Studio.

  


A **Brand Voice** controls how your content sounds:

  * Tone

  * Messaging style

  * Personality

  * Call-to-action style


  


A **Brand Kit** controls how your content looks:

  * Colors

  * Fonts

  * Logo

  * Visual identity


  


When selected inside a node, these settings guide the AI output automatically.

* * *

## **Key Benefits of Brand Integration in Agent Studio**

  


Using Brand Voice and Brand Kit inside Agent Studio ensures consistent, scalable branding.

  


  * **Consistent output:** Text, images, and media align with your brand automatically.


  


  * **Multi-brand workflows:** Assign different brands to different nodes within the same agent.


  


  * **Reduced manual edits:** Minimize rewriting and redesigning after generation.


  


  * **Automatic updates:** Changes to your Brand Board apply to future node runs.


  


  * **Improved quality control:** Built-in brand rules reduce off-brand messaging.


* * *

## **How Branding Works Across Media Types**

  


Once selected, branding influences:

  


### **Text Generation**

  * Writing style

  * Tone

  * Word choice

  * Call-to-action format


  


### **Image & Video Generation**

  * Brand colors

  * Logo placement

  * Font styling (where applicable)


  


### **Audio Generation**

  * Tone of script

  * Voice model mapping (if configured)


  


Brand rules are passed automatically to the AI when the node runs.

* * *

## **Brand Board Sync Behavior**

  


Brand settings are pulled from your Brand Boards.

  


If you update:

  * Colors

  * Logos

  * Messaging guidelines


  


Future node runs will reflect those changes automatically.

  


Existing generated content does not change retroactively.

* * *

## **How to Set Up Brand Voice and Brand Kit in Agent Studio**

  


Follow these steps:

###   


### **Step 1: Create Brand Boards (If Not Done)**

  1. ###  Go to **Marketing → Brand Boards**

  2. Create at least one:

     * Brand Voice

     * Brand Kit (Design Kit)


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066858028/original/mGV9vJ-hLs1eLorZRioP-J8vhr7z_jiIYw.png?1773392875)

  


###   


### **Step 2: Open Agent Studio**

  1. ###  Go to **AI Agents → Agent Studio**

  2. Open or create an agent

  3. Add a generation node (Text, Image, Video, Audio)


  


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066858286/original/ABUGMKqk7maVgzRfoXOL0BZpghLbIa6POQ.png?1773393025)

  


###   


### **Step 3: Select Brand Settings**

  1. ### 

Click the node to open its settings

  2. Locate the **Brand Voice** dropdown

  3. Select your desired Brand Voice

  4. Select a **Brand Kit**

  5. Click **Save**


  


You can also click **\+ Add New** to create a new brand without leaving the node.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155066858703/original/erMkIHFUte2dwQIzW7xTVsns0T21zGIpSQ.png?1773393192)

  


###   


### **Step 4: Test Output**

  1. ### 

Click **Test**

  2. Generate sample content

  3. Confirm tone and visuals match your brand


###   


### **Step 5: Publish**

  


Move the agent to Staging or Production once satisfied.

* * *

## **Multi-Brand Workflows**

  


You can assign different brands to different nodes.

  


This is useful when:

  


  * Agencies manage multiple client brands

  * Franchises share workflows but need localized tone

  * You are A/B testing messaging styles


  


Each node follows its assigned brand independently.

* * *

## **Frequently Asked Questions**

  


**Q: Do I need a Brand Board before using this?**

Yes. At least one Brand Voice and one Brand Kit must exist in Marketing → Brand Boards.

  


**Q: Will updating a Brand Kit change existing content?**

No. Only future node runs use updated settings.

  


**Q: Can I apply only a Brand Voice or only a Brand Kit?**

Yes. Leave one dropdown set to None if needed.

  


**Q: How many brands can I create?**

Multiple Brand Voices and Brand Kits can be stored per location. For manageability, keep totals reasonable.

  


**Q: Does this work with Ask AI?**

If Ask AI triggers a workflow containing branded nodes, the output inherits those brand settings.

  


**Q: Can I override brand tone inside a prompt?**

Yes. Manual instructions in the node apply for that run but do not modify your Brand Board.

  


**Q: Does Audio AI use custom voice models?**

If mapped inside your Brand Voice settings, supported voice models will apply automatically.

  


**Q: Is this available on all plans?**

Brand integration follows the same plan entitlements as Agent Studio.

* * *

## **Related Articles**

  


  * [How to Create a Brand Board](<https://help.gohighlevel.com/a/solutions/articles/155000003136?portalId=48000045315>)
  * [Brand Voice in Brand Boards](<https://help.gohighlevel.com/a/solutions/articles/155000005085?portalId=48000045315>)
  * [Brand Voice Integration in Content AI](<https://help.gohighlevel.com/a/solutions/articles/155000005308?portalId=48000045315>)
  * [How to Use the AI Agent Studio in HighLevel](<https://help.gohighlevel.com/a/solutions/articles/155000006058?portalId=48000045315>)
  * [Ask AI + Agent Studio Integration](<https://help.gohighlevel.com/a/solutions/articles/155000006677?portalId=48000045315>)

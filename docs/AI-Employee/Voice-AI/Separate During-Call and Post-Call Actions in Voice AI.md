# Separate During-Call and Post-Call Actions in Voice AI

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005267-separate-during-call-and-post-call-actions-in-voice-ai](https://help.gohighlevel.com/support/solutions/articles/155000005267-separate-during-call-and-post-call-actions-in-voice-ai)  
**Category:** AI Employee  
**Folder:** Voice AI

---

**TABLE OF CONTENTS**

  * Overview
  * What’s New
  * Key Improvements
  * How to Use It
  * Supported Action Types
    * During the Call
    * After the Call


##   
**Overview**

  


Voice AI actions are organized into during-call and post-call actions so you can clearly control what your agent does while speaking with a caller and what happens after the call ends. The updated action layout uses action cards, tabs, and focused configuration windows to make actions easier to create, review, edit, and manage.

  


  

    
    
    Note: If this experience is not visible in your account, go to **Settings > Labs** and enable Voice AI - Separate During and Post Call Actions, if available.

* * *

## **What Changed in the Action Builder**

  1. **Card-Based action layout**  
Actions appear as individual cards, making it easier to scan, edit, organize, and review configured actions.

  
_![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155046578046/original/3RvCiXMNSA2LtzG8exuGG0j1BJw0PbHxmA.png?1747168856)_  
  


  2. **Tabbed Layout**  
Actions are separated into **During the Call** and **After the Call** tabs, helping you distinguish actions that happen live during the conversation from actions that happen after the call ends.

  3. **Streamlined Creation Flow**  
Use the New Action button to add a supported action type and configure it in a focused setup window.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155046578089/original/3Njbttz4ii9VZ92LIuRU7Y2X5V-Rt_NZAw.jpeg?1747168934)

  4. **Individual Action Modals**  
Each action type opens in its own configuration window, so you can complete the required fields without scrolling through unrelated settings.  
  


  5. **Quick Delete Option**  
You can edit or delete actions from the action card menu without opening the full agent configuration flow.![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155046578104/original/vgrUiUJ44ABEyIWPDFmNZo4UTNYOadf1Nw.png?1747168957)


  


## Key Improvements

  1. **Improved Visual Hierarchy**  
Action types are now easier to distinguish thanks to better labels and grouped layouts.

  2. **Simplified Editing & Deletion**  
Edit or remove actions in fewer clicks — right from the action card.

  3. **Built-In Constraints & Smart Guidance**

     * **Visual counters** show you how many of each action type you're using.

     * **Tooltips and inline guidance** prevent misconfiguration:

       * Max **15 total actions** during a call

       * Only **1 appointment booking action** allowed

       * Up to **25 contact field update actions** after a call


##   
**How to Use?**

  


  1. Open the **Voice AI agent** you want to edit, and then click on + New Action

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077220323/original/ns8m1CxbVAAXfej1HZHnhh_736yQhwgRWQ.png?1785405521)  
  

  2. Choose the type of action you want to configure, for example, update contact field.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077220495/original/NsICyRQRyrpFBgI_E3dpYbfXDGRUtgSCLw.png?1785405579)  
  

  3. A focused modal will appear — fill in the required details.  
  


  4. ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077220612/original/OJ8VH1BbdMUKbDH7-G5w4Y0Ajuk4eMW86w.png?1785405617)  
  


  5. Save. Your new action will appear as a card under the appropriate tab.


  


## **Supported Action Types**

### During the Call

  * Call Transfer

  * Trigger Workflow

  * Send SMS

  * Book Appointment

  * Custom Actions (Beta)

  * Update Contact Field


### After the Call

  * Update Contact Field — Updates the contact silently after the conversation without interrupting the caller or requesting additional confirmation


  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155046578263/original/3HRS6002J0G6csS-Q6MWpGPDkXd5v8-rHg.jpeg?1747169446)

  


## **Choose When the Update Contact Field Action Runs**

  


When configuring the Update Contact Field action, choose when Voice AI applies the contact update. 

  


**During the Call**

Voice AI applies the update immediately during the conversation and includes a confirmation. Use this option when the agent should acknowledge or verify the updated information with the caller.

  


**After the Call**

Voice AI applies the update silently after the conversation. Use this option when the update should not interrupt the caller or add another confirmation to the conversation. This option can help keep conversations natural when updating details such as a city, address, preference, or other contact information

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077219883/original/1wSlhaTRz4I_1j4B3Sm-suahqhJfbPOqMg.png?1785405307)

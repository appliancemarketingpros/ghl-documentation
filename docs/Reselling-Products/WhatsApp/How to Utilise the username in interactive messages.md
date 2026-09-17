# How to Utilise the username in interactive messages

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008491-how-to-utilise-the-username-in-interactive-messages](https://help.gohighlevel.com/support/solutions/articles/155000008491-how-to-utilise-the-username-in-interactive-messages)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# Requesting a Contact's Phone Number with a WhatsApp Interactive Message

Use the Request Contact Info action in Automation to ask a contact to share their phone number directly inside a WhatsApp conversation — useful for contacts who message in using a WhatsApp username and don't have a number on file yet.

1| Add the Request Contact Info ActionGo to Automation, and inside your workflow select WhatsApp Interactive Messages. Click Request Contact Info, then write the body text of the message the contact will see.  
---|---  
![Configuring the Request Contact Info WhatsApp interactive message action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078988780/original/XmFZI4jdva1wpGwCxoub3IOKsfwvJrFYaQ.png?1787308225)2| Publish and Test the WorkflowPublish the workflow, then run a test to confirm the message sends and displays as expected.  
---|---  
![Publishing and testing the workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078988859/original/xLzFdCf8IdVtjeuuR7tpzhf9bDa4m8fOFw.png?1787308285)3| Check the Result in ConversationsOpen the conversation for the test contact. The To field, which previously showed the contact's phone number, now displays their WhatsApp username instead.  
---|---  
![Conversation showing the To field updated to the contact's WhatsApp username](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078991804/original/n2nZGU4nbjPzT6ulhXupcf1lgjg86cxjvw.png?1787309726)

Why This Matters

Not every contact you message on WhatsApp will have a phone number on file — some will only be reachable by their WhatsApp username. The Request Contact Info action gives you a direct, in-chat way to ask these contacts to share their number, rather than relying on them to volunteer it. It's worth testing this workflow with a username-only contact specifically, since that's the scenario where the To field switching to a username is expected and easiest to confirm.

## What the Contact Sees

When the contact taps to respond to the Request Contact Info message, WhatsApp opens their native Send Contact Info screen. This lets them choose exactly which details to share back with the business — their phone number, username, and any other contact card fields they have filled in — before tapping Send.  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078991790/original/BCxknTDlkcFPRg5B972-TtfZ9feLIfAM9w.png?1787309706)

If the contact leaves their username checked, as shown above, and taps Send, that's what causes the username to appear and update on your side — it's the contact's own confirmation, not something CRM fills in automatically. If they uncheck a field before sending, that detail won't come through.

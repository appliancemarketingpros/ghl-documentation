# Which Twilio phone number will the leads be getting the SMS from?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001152126-which-twilio-phone-number-will-the-leads-be-getting-the-sms-from-](https://help.gohighlevel.com/support/solutions/articles/48001152126-which-twilio-phone-number-will-the-leads-be-getting-the-sms-from-)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS · Messaging

How the “From” Number Is Chosen for SMS

Understand and control exactly which of your phone numbers your contacts see when you send them an SMS.

Overview

When you send an SMS to a lead or contact, it goes out from one of the phone numbers in your account. If you have more than one number, you may wonder which number your contact will actually see the message come from.

When sending SMS, the system follows a set of rules to determine which Twilio phone number is used as the sender. This ensures messages are sent from the most appropriate number, maintaining consistency and compliance. This article explains how that “From” number is chosen so you can predict and control it.

Table of Contents

1

The Short Version

2

The Priority Order, Explained

3

How to Assign Twilio Numbers to Users

4

Workflow Settings Option

5

Fallback Rules (When No User Number Exists)

6

Checking Which Number Was Used

7

How to Control Which Number Contacts See

8

Frequently Asked Questions

1

## The Short Version

The system picks the “From” number using a simple order of preference. It goes down this list and uses the **first** number that applies:

**1\. Caller-supplied number** — a number you specifically chose for that message.

**2\. User-assigned number** — the number assigned to the sending user.

**3\. Last-used number** — the number already being used in that conversation.

**4\. Default number** — your account’s default outbound number.

2

## The Priority Order, Explained

Priority 1

A number you specifically chose for that message

If you (or an automation) explicitly set a “From” number , for example, when you pick a specific number in a workflow SMS action or specify one through the API , that number is always used.

This gives you full control. If you want a message to come from a particular number, set it directly and it will take priority over everything else.

Requirement

The number you choose must be one that belongs to your account.

Priority 2

The number assigned to the sending user

If no specific number was chosen, the system looks at the **user** who is sending the message. If that user has their own dedicated number assigned for this location, the message is sent from that number. This is useful when each team member has their own phone number, so replies feel personal and land back with the right person.

If the staff member sending the SMS is listed under the sub-account’s **My Staff** tab **and** has a **dedicated Twilio number assigned** , the lead will receive the SMS from that assigned Twilio number. (It can be changed manually.)

Exception

If the assigned Twilio number is SMS-incompatible, the system will fall back to the **default outbound number**.

Priority 3

The number already being used in that conversation

If there’s no user-assigned number, the system checks whether the contact’s conversation is already tied to one of your numbers. If it is, the message continues going out from that same number.

This keeps a conversation consistent , your contact keeps seeing messages from the same number they’ve been chatting with.

Priority 4

Your account’s default number

If none of the above apply, the message is sent from your account’s **default outbound number**. This is the fallback used for most automated and system-generated messages when no other number is specified.

Tip

Make sure your default outbound number is set to the number you’d most want contacts to see when nothing else is specified.

![Diagram of the From number priority order](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053960857/original/fAxL4sKwzS_4yVbv2xvI4Ern0QSl-kiZuA.png?1758116362)

3

## How to Assign Twilio Numbers to Users

Step 1

Go to **Sub-Account Settings → My Staff**.

Step 2

**Edit** the user.

![Editing a user under the My Staff tab](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053959012/original/47E8wtytoJnuER0WSD4SpA2bNZ_p10Zfsw.png?1758115345)

Step 3

Expand the **Call & Voicemail Settings**.

Step 4

Assign a Twilio phone number to the user.

![Assigning a Twilio phone number under Call and Voicemail Settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053959210/original/ep5Tz931DpRQ7_j_Y5rXUwa9HDFnMJE8Bw.png?1758115465)

Learn more about [phone numbers for users / assigning Twilio numbers to users](<https://help.gohighlevel.com/en/support/solutions/articles/48001152124>).

4

## Workflow Settings Option

Inside the **Workflow builder** , you can also **manually choose which number to send SMS from**. When configuring a **“Send SMS” step** , you’ll see a dropdown for **“From Number.”**

This is useful when you want workflows to always send from a particular number, regardless of staff assignment or channel number.

![From Number dropdown in the workflow Send SMS step](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053959845/original/qlUVFLyfTCV5zYbFAhz3SS187jq-AOvDzg.png?1758115796)

5

## Fallback Rules (When No User Number Exists)

If the logged-in user is **not listed in the sub-account** , or **doesn’t have an LC number assigned** , the system will try the following in order:

Fallback 1

Channel Number

The **first LC number ever used with that contact**. This maintains conversation continuity.

Fallback 2

Default Outbound Number

If the channel number has been removed, the system will use the **default Twilio number** set at the account level.

6

## Checking Which Number Was Used

To confirm the exact Twilio number used in a conversation:

  * Hover over the **SMS message** in the conversation view.
  * Click the **three dots (…) → Details**.
  * This will show the **Twilio number** used to send that SMS.


![Checking the Twilio number used via the message Details menu](https://i.ibb.co/YjHc479/chrome-capture-2023-1-20.gif)

7

## How to Control Which Number Contacts See

**Want a specific number every time?** Set it directly on the message or automation — that always wins.

**Want messages to feel personal per team member?** Assign each user their own number.

**Want conversations to stay on the same number?** That happens automatically once a conversation is established.

**Everything else?** Set a reliable default outbound number for your account.

8

## Frequently Asked Questions

Q: My SMS is still coming from an old number even though I got a new one. Why?

This usually happens because of the **last-used number** rule. Once a conversation is established on a number, the system keeps using it for continuity. To switch, set the desired number explicitly on the message or automation, or update the user’s assigned number.

Q: Can I force every message in a workflow to send from one specific number?

Yes. In the **Workflow builder** , configure the **“Send SMS” step** and select a number from the **“From Number”** dropdown. A number set this way overrides staff assignment and channel number.

Q: What happens if a user’s assigned number can’t send SMS?

If the assigned Twilio number is SMS-incompatible, the system automatically falls back to the **default outbound number** so the message still goes out.

Q: Can I use any phone number as the “From” number?

No. The number you choose must be one that belongs to your account. You can’t send from a number that isn’t provisioned in your sub-account.

Q: How do I confirm which number a specific SMS was actually sent from?

Hover over the SMS in the conversation view, click the **three dots (…) → Details** , and the exact Twilio number used will be displayed.

Q: What number is used for automated or system-generated messages?

When no specific number is set and no user or conversation number applies, the system uses your account’s **default outbound number**. Set this to the number you’d most want contacts to see.

Related Articles

[Phone numbers for users / Assign Twilio Numbers to Users](<https://help.gohighlevel.com/en/support/solutions/articles/48001152124>) [SMS still coming from old Twilio number when I got a new one?](<https://help.gohighlevel.com/en/support/solutions/articles/48001152123>)

# How to Calculate SMS and MMS Costs

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001203458-how-to-calculate-sms-and-mms-costs](https://help.gohighlevel.com/support/solutions/articles/48001203458-how-to-calculate-sms-and-mms-costs)  
**Category:** Phone System  
**Folder:** Messaging

---

SMS Billing

How to Calculate SMS and MMS Costs

The factors that drive messaging costs, a step-by-step calculation method, and tips to manage expenses.

Overview

This article provides a comprehensive guide to calculating SMS and MMS costs using the platform. It covers the factors influencing costs, step-by-step calculation methods, and tips to manage and reduce messaging expenses effectively.

Important

This article only shows how to calculate SMS and MMS costs and what factors affect the calculation. If you want to know the pricing of these costs in your country, please refer to [LC Phone Pricing Structure](<https://help.gohighlevel.com/support/solutions/articles/48001223556-lc-phone-pricing-structure>).

Table of Contents

1

What Determines SMS Costs?

2

What Is an SMS Segment?

3

Steps to Estimate Outbound SMS Costs

4

SMS Cost Estimator Sheet

5

Understanding the Factors Impacting SMS Costs

6

Frequently Asked Questions

7

Related Articles

1

## What Determines SMS Costs?

There are many factors impacting SMS costs, such as the per-segment SMS cost, destination number, direction (inbound or outbound), attaching an image (MMS), emojis, carrier fees, and more. We encourage you to explore all of the SMS pricing on Twilio's [SMS Pricing](<https://www.twilio.com/en-us/sms/pricing/us>) page. We've outlined most of the factors impacting SMS costs below in the section "Understanding the Factors Impacting SMS Costs." We recommend reviewing this article and the SMS pricing in full to better understand SMS costs and pricing.

### Key Benefits of Understanding SMS and MMS Costs

Grasping the cost structure of SMS and MMS messaging helps in budgeting and optimizing communication strategies.

  * Accurate budgeting for messaging campaigns.
  * Optimization of message content to reduce costs.
  * Enhanced understanding of carrier fees and charges.
  * Ability to make informed decisions on using SMS vs. MMS.


2

## What Is an SMS Segment?

An SMS segment is a unit of measurement used to calculate SMS charges. Each segment consists of 160 characters if GSM-7 encoding is used. If the message exceeds this limit, it will be broken into multiple segments, increasing the cost.

  * A message with **160 characters = 1 segment.**
  * A message with **161 characters = 2 segments.**
  * The more segments your message contains, the higher the cost.


Important

Emojis can enhance engagement but increase SMS costs by triggering Unicode encoding, which reduces the character limit per segment to 70 instead of 160.

In cases where an internal error occurs before the message is handed off to the phone provider, you will not be charged. However, once a delivery attempt has been made, charges apply regardless of whether the message is successfully delivered. This includes SMS sent from toll-free numbers, A2P numbers, and those that cannot be delivered due to country restrictions or other limitations. We encourage users to carefully review their messages before sending, as refunds will not be issued for undelivered SMS.

It is important to know all of the SMS pricing, however, it is reasonable to assume your highest SMS costs will be related to sending outbound SMS. For this reason, we will walk you step by step through the process of estimating the cost of an outbound SMS in the next section.

3

## Steps to Estimate Outbound SMS Costs

There are four steps to estimating the cost of an outbound SMS: find the number of segments, look up the per-segment cost, look up carrier fees, and calculate. As we go to calculate the cost of an SMS, we use the Outbound SMS Cost Equation below.

Outbound SMS Cost Equation

Estimated Cost of Outbound SMS = [(Number of Segments) × (Per-Segment Cost)] + [(Number of Segments) × (Carrier Fees)]

Please Note

This estimation is for a single outbound SMS sent from a US number to another US number. There are many factors that can change the final cost of an SMS — see the section "Understanding the Factors Impacting SMS Costs" below. See [SMS Pricing here](<https://www.twilio.com/en-us/sms/pricing/us>); prices may change from time to time without notice.

Step 1

Find the Number of Segments in Your Text

After writing the message you want to send, copy the text message. Then open the [Messaging Segment Calculator](<https://twiliodeved.github.io/message-segment-calculator/>) and paste the copied text into it. See the "Number of Segments" to locate the number of segments. Keep this available as we continue.

![Messaging Segment Calculator showing number of segments](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155046379999/original/NFyvNSx9-p5vxdoypXnalX8bHUgDT0Ihaw.png?1746786747)

Step 2

Look Up Per-Segment Cost

  * Open up the [SMS Pricing page](<https://www.twilio.com/en-us/sms/pricing/us>). Select the country you are sending outbound messages to (destination country).
  * Then scroll down to "SMS/MMS Pricing." Locate your "Per-Segment Costs." In our example, we are sending an outbound SMS for long codes, so we choose $0.0083 for this example.


![SMS Pricing page showing per-segment costs](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053585937/original/WDxo_NAILHjloHXdxjemi8WHTSWFEvko5Q.png?1757602633)

Example

Estimated Cost of Outbound SMS = [(5)($0.0083)] + [(5)(Carrier Fees)]

Step 3

Look Up Carrier Fees (≈$0.005)

In the US and Canada, carriers like T-Mobile, AT&T, or Verizon charge you for inbound messages sent to their end users. Prices vary by carrier and change from time to time. To locate the carrier fees by carrier, see the [SMS Pricing page](<https://www.twilio.com/en-us/sms/pricing/us>). Scroll down to the "Carrier Fees" section and see the inbound SMS column for a specific carrier.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076658888/original/X0bfxUw3MI9Yf3yMji_YtmfSL4ySk1U7TQ.png?1784794407)

***Please note:** carrier fee prices vary based on the type of number (long code, toll-free, and short code).

Because carrier fees are unique to the end user's carrier, we can't calculate the cost until we know what carrier we're sending to. To overcome this, we can estimate. We suggest using ≈$0.005 as this is currently the highest carrier charge (as of the last edit to this article). Feel free to change this approximation to what feels best for your estimates based on the prices available on [SMS Pricing](<https://www.twilio.com/en-us/sms/pricing/us>).

Example

Estimated Cost of Outbound SMS = [(5)($0.0083)] + [(5)(≈$0.005)]

Step 4

Calculate

We are now ready to calculate the estimated cost of our text message. Let's walk through it step by step.

Estimated Cost of Outbound SMS = [(5)($0.0083)] + [(5)($0.005)]

First, multiply the number of segments (Step 1) by the per-segment cost (Step 2):

Estimated Cost of Outbound SMS = [$0.0415] + [(5)($0.005)]

Now multiply the number of segments (Step 1) by the estimated carrier fees (Step 3):

Estimated Cost of Outbound SMS = [$0.0415] + [$0.025]

Lastly, add the two sums together to finish the estimation:

Estimated Cost of Outbound SMS = $0.0665, or 6.65 cents

Important

This is an estimation. The final price can only be known after sending. Adding an image, hidden characters, emojis, and other factors can impact the cost of an SMS. To understand more of the factors impacting final SMS price, see "Understanding the Factors Impacting SMS Costs" below.

4

## SMS Cost Estimator Sheet

Use the SMS Cost Estimator Sheet to quickly calculate your SMS costs. Make a copy, enter your message details, and let the sheet do the work for you. Open the sheet from the link below and "Make a Copy" of it.

![SMS Cost Estimator Sheet preview](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053587341/original/KrUho7fdGsjOULh4tMf38c8tmuRphaoncA.png?1757603228)

**SMS Cost Estimator Sheet** — ("Make a Copy" of this sheet to edit it) — [Sheet Link](<https://docs.google.com/spreadsheets/d/1rhJKukw4Y8G2KCqpphuhY6Q51zrohNmraCChVh-ETAI/edit?usp=sharing>) (it can have old cost values).

Note

This is an estimator, final costs will vary based on additional factors. Learn more in "Understanding the Factors Impacting SMS Costs" below. See [SMS Pricing here](<https://www.twilio.com/en-us/sms/pricing/us>).

5

## Understanding the Factors Impacting SMS Costs

Many factors impact the cost of an SMS: direction (inbound/outbound), destination number, number of segments, carrier fees, number validation, adding an image, hidden characters, and more. Below we walk through the most common factors.

### Per-Segment Cost

An SMS consists of 160-character segments, with longer messages split into multiple segments, increasing costs. Emojis, images, and hidden characters can further impact pricing.

To find the per-segment cost, refer to Step 2 in the previous section.

To learn more about segments, see [What the Heck Is a Segment?](<https://www.twilio.com/en-us/blog/what-the-heck-is-a-segment-html>)

Important

In the US/Canada, one segment contains 160 characters, however, having between 161 to 320 characters will automatically result in 2 segments — having between 321 to 480 characters will result in 3 segments, and so on. Character lengths of segments also vary by countries and regions, which will impact the final SMS price. Most countries use 160 characters or 70 characters for segment lengths, depending on the encoding type. Generally, most messages use the standard GSM-7 encoding, which gives us 160 characters per segment.

### Number of Segments

SMS costs are based on the number of segments, meaning more segments = higher cost. For example, a 5-segment message costs approximately five times more than a single-segment SMS. Refer to "Steps to Estimate Outbound SMS Costs" above for a detailed breakdown.

For Example

A 5-segment message: [(5)($0.0083)] + [(5)($0.005)] = $0.0415 + $0.025 = **$0.0665, or 6.65 cents**

A 1-segment message: [(1)($0.0083)] + [(1)($0.005)] = $0.0083 + $0.005 = **$0.0133, or 1.33 cents**

#### Adding an Image (MMS)

MMS includes media attachments (e.g., images), which are charged differently than SMS. Adding an image shifts the message to [MMS pricing](<https://www.twilio.com/en-us/sms/pricing/us>), which includes both MMS message fees and carrier fees.

For Example

For a 5-segment message with an image:

Estimated Cost of MMS Text = [(Number of Segments)(Per-Segment MMS Cost)] + [(Number of Segments)(MMS Carrier Fees)]

= [(5)($0.02)] + [(5)($0.01)] = $0.10 + $0.05 = $0.15, or 15 cents

Messages sent can include up to 10 media files with a total size of up to 5MB. Anything over 5MB is uploaded to your media library, and a short link is created that you can send to the contact. Messages with over 5MB of media will not be accepted.

#### What Is UCS-2 Encoding?

UCS-2, which stands for "Universal Character Set 2," is a fixed-length character encoding where each character is stored in 16 bits (2 bytes). It supports many global languages, symbols, and emojis, but does not cover the entire Unicode range (UTF-16 is used for that). In SMS, UCS-2 encoding is triggered when a message contains non-GSM-7 characters (e.g., Chinese, Arabic, emojis, or special symbols).

#### How Does UCS-2 Affect SMS?

  * **Message Length:** SMS messages using UCS-2 can only hold 70 characters per message, compared to 160 characters with GSM-7.
  * **Segmentation:** If the message exceeds 70 characters, it is split into multiple parts. Each segment can carry up to 67 characters, since space is reserved for concatenation headers.


#### When Is UCS-2 Used on the Platform?

The platform automatically switches to UCS-2 encoding whenever an SMS includes characters outside the GSM-7 set. This typically happens if your message contains emojis, non-Latin scripts (e.g., Chinese, Arabic), or special symbols that GSM-7 cannot represent.

#### How Do Emojis Affect SMS Cost Calculation?

Emojis can enhance engagement but increase SMS costs by triggering Unicode encoding, which reduces the character limit per segment to 70 instead of 160.

**For example:** in the image below, we have a 1-segment message if we use the characters alone. However, adding some emojis increased the number of segments from 1 to 4.

![Emojis increasing segment count from 1 to 4](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042421358/original/7quk6dRuZmKnU-bNM8e2Y4gmruX0ttF23w.png?1740740698)

#### Hidden Characters

Many agencies copy/paste the SMS text body while designing automations. When you copy/paste text from a text editor like MS Word or Google Docs, sometimes hidden characters get appended to the string. These hidden characters can't be seen by the user, but they are present in the text.

**For example:** the simple phrase "Hey there" was copied from a webpage. Usually, it should be just 1 segment. But it actually contains many hidden (empty) characters, making it as large as 4 segments.

![Hidden characters inflating a simple phrase to 4 segments](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042421505/original/5wFok9T2iUpRW_T-QK5ezXLaD0WIAeBIEQ.png?1740740833)

You can use the [Segment Calculator](<https://twiliodeved.github.io/message-segment-calculator/>) to check the actual number of segments and character length of your SMS text.

Please Note

While pasting the contents of an SMS into a text editor, it's recommended to use the "paste as plain text" option instead of a simple paste.

To paste as plain text — **Windows:** press "Ctrl + Shift + V". **Mac:** press "Cmd + Shift + V".

### Carrier Fees

As we reviewed in Step 3 above, carrier fees are charged by carriers like Verizon, T-Mobile, and AT&T when you send a message to one of their end-user numbers. As shown in the Outbound SMS Cost Equation, carrier fees are charged by segment — meaning more segments in an SMS result in higher costs, since the number of segments is multiplied by the carrier fees.

Outbound SMS Cost Equation

Estimated Cost of Outbound SMS = [(Number of Segments)(Per-Segment Cost)] + [(Number of Segments)(Carrier Fees)]

*See how the number of segments is multiplied by the carrier fees: "[(Number of Segments)(Carrier Fees)]" — meaning a reduction in segments will reduce carrier fees. Remember, there's also a difference between SMS and MMS carrier fees.

For a non-LC sub-account, please [set up your Business Profile and A2P campaign inside the Twilio console](<https://support.twilio.com/hc/en-us/articles/1260801864489-How-do-I-register-to-use-A2P-10DLC-messaging>).

For an LC Phone sub-account, please set up A2P registration in the [LC Phone System Trust Center](<https://help.gohighlevel.com/support/solutions/articles/48001225526>).

![A2P registration setup screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042422409/original/grxV3dIpcJ46VS6xQzTUYfVarxbApl_ZWQ.png?1740741523)

### Carrier Lookup Fees

Carrier Lookup Fees (listed as CARRIER-LOOKUP-FEES on your invoice) are incurred on the first SMS you attempt to send to a contact. It's part of the [SMS / Phone Number Validation feature](<https://help.gohighlevel.com/support/solutions/articles/48001153968-sms-phone-number-validation-is-live>). This feature checks to see if a number is real and can receive SMS/MMS. This saves you money in the long run — without it, you'd risk sending a text to fake numbers and incurring full charges. With Number Validation, you can check whether a number is valid before sending, which is a lot cheaper over time.

### Direction (Inbound/Outbound)

In the example above, we calculated a 5-segment outbound message — meaning we're sending a message from our system to a number. However, if you receive a reply from that number, you're charged for inbound messages as well.

For example, open the SMS Pricing page, then locate the "Inbound" column to see the pricing for a particular inbound message. This reveals the inbound cost of an SMS for a long code (10-digit) number.

![Inbound pricing column on the SMS Pricing page](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155053590789/original/3tfdi-cbA3AnP-oFRS0WvIKLtoTQQ0KnOg.png?1757604842)

To calculate the cost of an inbound text, simply change the costs in the equation to the inbound cost listed on the SMS Pricing page, then run the calculation.

Estimated Cost of Inbound Text = [(Number of Segments)(Per-Segment Inbound SMS/MMS Cost)] + [(Number of Segments)(Inbound SMS/MMS Carrier Fees)]

*Be sure to reference the "Inbound" column on the SMS Pricing page, as well as SMS vs. MMS costs, when plugging in your variables.

### International Messaging

In the example above, we're sending from a US/Canada number to another US/Canada number. However, if you send a text to a non-US/Canada number, you'll be subject to the recipient country's fees. For example, sending from a US/Canada number to an Australian number will be charged based on Australian SMS pricing.

You can look up messaging rates for all countries by adjusting the "Messages in" drop-down and selecting the recipient country, as covered in Step 2 above.

In this example, per-segment costs in US/Canada might be $0.0083 while Australian costs are $0.0515 — roughly 6.5 times the standard US/Canada rate. Sending to international numbers can greatly impact SMS costs.

![International SMS pricing comparison](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155046380814/original/sV7XHBxOZeQlB0sK1XUNO_Ws6KSImPjrKg.jpeg?1746787451)

Note

Generally you're only charged the destination country's pricing, however, in some cases other fees can apply. Sending a single SMS as a test is a great way to see costs for these cases, as final pricing for international numbers varies based on international country rules and regulations.

6

## Frequently Asked Questions

Q: Am I charged for messages that fail to send?

If a message fails due to an internal error before reaching the carrier, you are not charged. However, once the message is handed off to the carrier, charges apply regardless of delivery success.

Q: Why are my SMS costs so high?

The most common reason is a message split into multiple segments. SMS pricing is based on segments, meaning more segments = higher cost — a 5-segment message costs about 5 times more than a single-segment SMS. Check "Steps to Estimate Outbound SMS Costs" and optimize message length before sending.

Q: How can I reduce the number of segments in my SMS to lower cost?

Open the Segment Calculator and paste your message into it. Work to reduce the "Number of Segments" shown to lower your total cost — watch especially for emojis and hidden characters from copy/paste.

Q: What are the factors that can impact SMS pricing?

Reducing segment count and not including images or attachments can help reduce cost, but there are other factors too — direction (inbound/outbound), destination country, carrier fees, and number validation. Review "Understanding the Factors Impacting SMS Costs" above for the full breakdown.

Q: Is the Carrier Lookup Fee charged every time I message a contact?

No — it's only incurred on the first SMS you attempt to send to a given contact, as part of the SMS/Phone Number Validation feature that checks whether the number is real and can receive SMS/MMS.

Related Articles

[LC Phone Pricing Structure](<https://help.gohighlevel.com/support/solutions/articles/48001223556-lc-phone-pricing-structure>) [Understanding A2P 10DLC Messaging Fees: Registration, Monthly, and Carrier Costs](<https://help.gohighlevel.com/support/solutions/articles/155000005200-understanding-a2p-10dlc-messaging-fees-registration-monthly-and-carrier-costs>)

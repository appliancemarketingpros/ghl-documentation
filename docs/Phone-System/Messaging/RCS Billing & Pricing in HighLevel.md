# RCS Billing & Pricing in HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007788-rcs-billing-pricing-in-highlevel](https://help.gohighlevel.com/support/solutions/articles/155000007788-rcs-billing-pricing-in-highlevel)  
**Category:** Phone System  
**Folder:** Messaging

---

Billing & Usage

How RCS Messaging Is Billed

How RCS charges are calculated from message type, direction, and country — including US vs. Non-US rules, segments, and carrier fees.

Overview

RCS billing depends on three primary factors: **message classification** (Basic RCS or Single RCS), **message direction** (outbound or inbound), and **country** (determined from the end user's phone number based on message direction).

The billing behavior also differs between the **United States** and **Non-US countries**.

What Is a Segment?

A segment is 160 UTF-8 bytes of the message body, rounded up. It is byte length, not character count, so emoji and non-Latin text use more bytes per character. Segments are always recalculated from the body — Twilio's own segment count is ignored because it is not reliable for RCS. An empty body still counts as 1 segment.

Table of Contents

1

RCS Message Types

2

What Is an RCS Segment?

3

Determining the Country for Billing

4

United States RCS Billing

5

Non-US RCS Billing

6

US vs. Non-US Classification at a Glance

7

RCS Carrier Fees

8

RCS Billing Decision Flow

9

Quick Reference

10

RCS Pricing by Country

11

Frequently Asked Questions

1

## RCS Message Types

RCS messages are classified as either **Basic RCS** or **Single RCS**.

The classification matters because it determines whether the message is billed **per segment** or **per message** , as well as which RCS rate applies.

Basic RCS

Text-only, classified by country

A text-only RCS message can be classified as Basic. The exact classification depends on the country.

**United States:** A text-only RCS message is always Basic, regardless of length. If it exceeds 160 UTF-8 bytes, it stays Basic — the extra length only increases the number of billable segments.

**Non-US:** A text-only message is Basic when the body is 160 UTF-8 bytes or fewer. If it exceeds 160 UTF-8 bytes, it is classified and billed as Single RCS instead — there is no segmentation for billing, so longer messages are treated as a single message, not multiple segments.

Summary Table

Region| Basic RCS Definition| Segmentation / Billing  
---|---|---  
US| Text-only, ≤ 160 UTF-8 bytes| Segmented & billed per 160 bytes  
Non-US| Text-only, ≤ 160 UTF-8 bytes| No segmentation; > 160 bytes = Single RCS  
  
Single RCS

Media, or long Non-US text

A message is classified as Single RCS when either of the following applies:

  * The message contains an **attachment or card media**.
  * For **Non-US traffic** , a text-only message exceeds **160 UTF-8 bytes**.


Any attachment or card media makes the message Single, regardless of the message's country or text length.

Important

A US text-only message does not become Single because of its length. It remains Basic and is billed based on its number of segments.

2

## What Is an RCS Segment?

An **RCS segment** refers to a portion of a text message that is split due to length limitations, specifically for RCS (Rich Communication Services) messaging. For US Basic RCS messages, billing is calculated using segments.

One segment represents **160 UTF-8 bytes of the message body**. The segment count is calculated by taking the UTF-8 byte length of the body, dividing it by 160, and rounding up.

  


Segments = max(1, ceil(UTF-8 byte length ÷ 160))

Examples

Message Body| Billable Segments  
---|---  
Empty body| 1  
1–160 UTF-8 bytes| 1  
161–320 UTF-8 bytes| 2  
321–480 UTF-8 bytes| 3  
481–640 UTF-8 bytes| 4  
  
Example 1

Message: "Hello, this is a test." (22 characters, all 1 byte each). Total bytes: 22 → **Segments: 1**

Example 2

Message: 200 English characters (200 bytes). Segments: **ceil(200 / 160) = 2**

Example 3

Message: 80 emojis (each emoji is 4 bytes, so 320 bytes). Segments: **ceil(320 / 160) = 2**

Bytes vs. Characters

Segment calculation is based on **UTF-8 bytes, not character count**. This matters because some characters require more than one UTF-8 byte:

  * Many standard English characters use 1 byte.  
  

  * Many non-Latin characters use multiple bytes.
  * Emoji commonly use multiple bytes.


As a result, two messages containing the same number of visible characters may have different segment counts.

How Segments Are Calculated

The platform recalculates the segment count directly from the message body. Twilio's reported segment count is not used for RCS segment billing because it may not reliably represent the RCS billing segment count. An empty message body still counts as one segment.

3

## Determining the Country for Billing

The country used for RCS pricing depends on the **direction of the message**.

Outbound RCS

Use the destination number's country

**Example:** Platform → Customer in the UK. The applicable RCS pricing is the UK rate.

Inbound RCS

Use the sender's (handset's) country

**Example:** Customer in the US → Platform. The applicable RCS pricing is the US rate.

Why This Matters

This country determination happens before applying the corresponding Basic or Single billing rules.

4

## United States RCS Billing

US RCS pricing works differently from Non-US pricing. For US traffic:

  * **Basic Outbound** → Per segment
  * **Basic Inbound** → Per segment
  * **Single / Rich Outbound** → Per message
  * **Single / Rich Inbound** → Per message


The platform's current US pricing likewise describes RCS Rich text as charged per segment and RCS Rich Media as charged per message.

Region| Message Type| Direction| Billing Unit| Price (USD $)  
---|---|---|---|---  
US| Basic RCS Text| Outbound| Per segment (160 UTF-8 bytes)| $0.0083  
US| Basic RCS Text| Inbound| Per segment (160 UTF-8 bytes)| $0.0083  
US| Rich / Single RCS| Inbound| Per message| $0.0165  
US| Rich / Single RCS| Outbound| Per message| $0.0220  
  
Important

US Basic RCS is billed per segment for both inbound and outbound messages.

US Billing Examples

Example 1 — Short Text-Only Message

An outbound US RCS message contains 120 UTF-8 bytes and no media. It is text-only, US, Basic RCS, 1 segment. Charge: **1 × $0.0083 = $0.0083**

Example 2 — Long Text-Only Message

An outbound US message contains 350 UTF-8 bytes and no media. Because it is US text-only traffic, it remains Basic RCS, regardless of length. Segment calculation: ceil(350 ÷ 160) = 3 segments. Charge: **3 × $0.0083 = $0.0249**. The message does not become Single simply because it exceeds 160 bytes.

Example 3 — Message With Media

An outbound US RCS message contains text plus an image. Because it contains media, it is classified as Single / Rich RCS and billed once per message. Charge: **$0.0220**. The text length does not cause additional RCS segments to be billed for this Single message.

5

## Non-US RCS Billing

Non-US RCS follows a different classification model. For Non-US traffic:

  * **Basic** → Per segment, if 160 UTF-8 bytes or fewer
  * **Single** → Per message
  * **Inbound** → Per message


The applicable static rate depends on the country. The platform's country-specific pricing pages similarly separate Non-US outbound RCS into **Basic** and **Single** pricing.

Text-Only Messages

**160 UTF-8 bytes or fewer** → Basic. **More than 160 UTF-8 bytes** → Single. This means message length can result in a real pricing difference outside the US.

Messages With Media

Any attachment or card media results in the message being classified as Single, regardless of its text length.

Non-US Examples

Example 1 — Short Text-Only Message

A Non-US outbound message contains 100 UTF-8 bytes with no attachment or card media. The message is **Basic RCS** → billed once at the country's Basic rate.

Example 2 — Long Text-Only Message

A Non-US outbound message contains 250 UTF-8 bytes. Even though there is no attachment or media, it exceeds the 160-byte Basic limit. The message is therefore **Single RCS** → billed once at the country's Single rate. It is not billed as two Basic segments.

Example 3 — Message With Media

A Non-US outbound message contains only 50 UTF-8 bytes of text but also contains an image. The presence of media makes the message **Single RCS** → billed once at the country's Single rate.

6

## US vs. Non-US Classification at a Glance

Scenario| US| Non-US  
---|---|---  
Text-only ≤ 160 UTF-8 bytes| Basic| Basic  
Text-only > 160 UTF-8 bytes| Basic — multiple segments| Single  
Attachment present| Single| Single  
Card media present| Single| Single  
Basic billing unit| Per segment| Per message  
Single billing unit| Per message| Per message  
  
The Key Distinction

US text-only messages remain Basic regardless of length. Non-US text-only messages become Single when they exceed 160 UTF-8 bytes.

7

## RCS Carrier Fees

Carrier fees may apply in addition to the base RCS message charge. Twilio publishes carrier-specific RCS fees, and those fees can differ by carrier, message type, and direction.

Within the platform, carrier fees are billed as follows:

Account / Usage Category| Carrier Fee Billing  
---|---  
Usage Category| Billed directly by Twilio  
Agency Accounts| Same pricing as Twilio  
Location Accounts| Twilio pricing + **5% markup**  
  
Note

Carrier fees should be considered separately from the base RCS message charge.

8

## RCS Billing Decision Flow

Use the following logic to determine how an RCS message will be billed.

Step 1 — Determine the Country

For **outbound** messages, use the destination number's country. For **inbound** messages, use the sender / handset's country.

Step 2 — Check for Media

Does the message contain an attachment or card media? **Yes** → Single RCS; bill once using the applicable country's Single / Rich rate. **No** → continue to Step 3.

Step 3 — Check Whether the Country Is the US

**If US:** text-only messages are Basic RCS, regardless of length. Calculate Segments = max(1, ceil(UTF-8 byte length ÷ 160)), then RCS charge = Number of segments × Basic US rate.

**If Non-US:** check the UTF-8 byte length. ≤ 160 bytes → Basic RCS, billed once at the country's Basic rate. > 160 bytes → Single RCS, billed once at the country's Single rate.

Step 4 — Apply Carrier Fees

Apply the applicable Twilio carrier fee and platform markup rules.

9

## Quick Reference

Question| Billing Rule  
---|---  
How is the applicable country determined for outbound?| Destination number's country  
How is it determined for inbound?| Sender / handset's country  
What is one segment?| 160 UTF-8 bytes  
Is segment size based on characters?| No, it is based on UTF-8 bytes  
Does an empty body have zero segments?| No, minimum is 1 segment  
Is Twilio's RCS segment count used?| No, segments are recalculated from the body  
Is US Basic outbound per segment?| Yes  
Is US Basic inbound per segment?| Yes  
Does long US text become Single?| No  
Does Non-US text > 160 UTF-8 bytes become Single?| Yes  
Does an attachment make a message Single?| Yes  
Does card media make a message Single?| Yes  
Are Single messages billed per segment?| No, they are billed per message  
Do carrier fees apply separately?| Yes  
  
Important Notes

  * RCS pricing varies by country and may change over time.
  * Carrier fees may apply in addition to the base RCS charge.
  * Twilio states that its messaging prices and carrier fees can change, so current country-specific pricing should be checked when exact rates are required.
  * The platform's **5% Location Account markup** applies to the applicable Twilio carrier pricing as described above.
  * Always determine the message's country and classification before calculating the final charge.


10

## RCS Pricing by Country

Pick your country from the dropdown to see its outbound Basic, outbound Single, and inbound RCS rates. All values are list prices in USD. The full table below lists every country as well.

United States *

Basic (Outbound)

$0.0083

per segment

Single (Outbound)

$0.0220

per message

Inbound

$0.0083

per message

Austria

Basic (Outbound)

$0.0979

per message

Single (Outbound)

$0.2252

per message

Inbound

$0.0075

per message

Belgium

Basic (Outbound)

$0.1667

per message

Single (Outbound)

$0.3834

per message

Inbound

$0.0075

per message

Brazil

Basic (Outbound)

$0.0599

per message

Single (Outbound)

$0.1378

per message

Inbound

$0.0250

per message

Canada

Basic (Outbound)

$0.0083

per message

Single (Outbound)

$0.0220

per message

Inbound

$0.0083

per message

Czech Republic

Basic (Outbound)

$1.5758

per message

Single (Outbound)

$3.6243

per message

Inbound

$0.0075

per message

Denmark

Basic (Outbound)

$0.0592

per message

Single (Outbound)

$0.1362

per message

Inbound

$0.0075

per message

Finland

Basic (Outbound)

$0.0861

per message

Single (Outbound)

$0.1980

per message

Inbound

$0.0075

per message

France

Basic (Outbound)

$0.0798

per message

Single (Outbound)

$0.1835

per message

Inbound

$0.0075

per message

Germany

Basic (Outbound)

$0.1120

per message

Single (Outbound)

$0.2576

per message

Inbound

$0.0075

per message

Ireland

Basic (Outbound)

$0.0779

per message

Single (Outbound)

$0.1792

per message

Inbound

$0.0075

per message

Italy

Basic (Outbound)

$0.0927

per message

Single (Outbound)

$0.2132

per message

Inbound

$0.0200

per message

Mexico

Basic (Outbound)

$0.1819

per message

Single (Outbound)

$0.4184

per message

Inbound

$0.0075

per message

Netherlands

Basic (Outbound)

$0.1143

per message

Single (Outbound)

$0.2629

per message

Inbound

$0.0075

per message

Norway

Basic (Outbound)

$0.0697

per message

Single (Outbound)

$0.1603

per message

Inbound

$0.0075

per message

Poland

Basic (Outbound)

$0.0457

per message

Single (Outbound)

$0.1051

per message

Inbound

$0.0075

per message

Portugal

Basic (Outbound)

$0.0501

per message

Single (Outbound)

$0.1152

per message

Inbound

$0.0450

per message

Romania

Basic (Outbound)

$0.0781

per message

Single (Outbound)

$0.1796

per message

Inbound

$0.0075

per message

Singapore

Basic (Outbound)

$0.0591

per message

Single (Outbound)

$0.1359

per message

Inbound

$0.0470

per message

Slovakia

Basic (Outbound)

$0.0883

per message

Single (Outbound)

$0.2031

per message

Inbound

$0.0100

per message

Spain

Basic (Outbound)

$0.0875

per message

Single (Outbound)

$0.2013

per message

Inbound

$0.0075

per message

Sweden

Basic (Outbound)

$0.0808

per message

Single (Outbound)

$0.1858

per message

Inbound

$0.0075

per message

United Kingdom

Basic (Outbound)

$0.0560

per message

Single (Outbound)

$0.1288

per message

Inbound

$0.0075

per message

Note

* United States Basic RCS is billed **per segment** (160 UTF-8 bytes). All other outbound Basic rates, and every Single rate, are billed **per message**. US Inbound Rich Media is $0.0165. Rates vary by country and may change over time; carrier fees may apply separately, and a 5% markup applies to Location Accounts.

11

## Frequently Asked Questions

Q: Why is my segment count different from what Twilio reports?

Segments are always recalculated directly from the message body using the UTF-8 byte length. Twilio's reported segment count is not used for RCS segment billing because it may not reliably represent the RCS billing segment count.

Q: Does a long US text message get charged as multiple messages?

No. A US text-only message stays Basic RCS regardless of length. Extra length only increases the number of billable **segments** — it is not reclassified as Single, and it is not billed as multiple separate messages.

Q: Why do two messages with the same number of characters cost different amounts?

Billing is based on UTF-8 bytes, not visible characters. Standard English characters typically use 1 byte, while many non-Latin characters and emoji use multiple bytes — so the same character count can produce a different byte length and therefore a different segment count.

Q: Does adding an image or attachment change how the message is billed?

Yes. Any attachment or card media classifies the message as Single / Rich RCS, regardless of country or text length. Single messages are billed once per message rather than per segment.

Q: How is the country decided when both parties are in different countries?

It depends on direction. For outbound messages, the destination number's country is used. For inbound messages, the sender / handset's country is used. This is determined before applying Basic or Single billing rules.

Q: Do carrier fees come out of my message charge, or are they extra?

Carrier fees are separate from and in addition to the base RCS message charge. For Location Accounts, Twilio carrier pricing has a 5% markup applied; Agency Accounts pay the same pricing as Twilio.

Q: Are the prices shown here final?

RCS pricing varies by country and may change over time, and Twilio states its messaging prices and carrier fees can change. Always check current country-specific pricing when you need exact rates.

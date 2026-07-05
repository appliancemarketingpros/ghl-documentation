# Phone System Pricing & Billing Guide

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001223556-phone-system-pricing-billing-guide](https://help.gohighlevel.com/support/solutions/articles/48001223556-phone-system-pricing-billing-guide)  
**Category:** Phone System  
**Folder:** LC Phone System

---

Overview

This guide outlines the full pricing structure for the native Phone System within the platform, including phone number rental, SMS/MMS messaging, voice calling, carrier pass-through charges, and A2P registration. Pricing matches Twilio's rates.

All prices are in USD. Country-specific pricing PDFs are attached at the bottom of this page.

Table of Contents

1

Phone Numbers

2

Messaging — SMS & MMS

3

Voice

4

A2P Pricing

5

Pass-Through Charges & Re-billing

6

Number Intelligence

7

Frequently Asked Questions

1

## Phone Numbers

All phone numbers are charged monthly. Below are the US/Canada rates:

Number Type| Monthly Cost  
---|---  
Local Numbers| $1.15 / month  
Toll-Free Numbers| $2.15 / month  
  
Note

For all other countries, refer to the country-specific pricing PDFs attached at the bottom of this page.

2

## Messaging — SMS & MMS

SMS

Per-segment pricing — US/Canada

Country| Outbound| Inbound  
---|---|---  
US| $0.00747| $0.00747  
Canada| $0.00747| $0.00747  
  
A 10% discount is applied to the $0.0083 list price for both local and toll-free numbers.

MMS

Per-segment pricing — US, Canada & Australia

Country| Outbound| Inbound  
---|---|---  
US| $0.0220| $0.0165 (Local) / $0.0200 (Toll-free)  
Canada| $0.0220| $0.0165 (Local) / $0.0200 (Toll-free)  
Australia| $0.3500| $0.3500 (Local & Toll-Free)  
  
For segment calculation details, refer to the [How to Calculate SMS and MMS Costs](<https://help.gohighlevel.com/support/solutions/articles/48001203458-how-to-calculate-sms-and-mms-costs>) guide.

Carrier Fees

Passed through by the recipient's carrier

Carrier fees are charged by the recipient's carrier on top of standard SMS/MMS rates. Amounts vary by carrier and message type.

Carrier| SMS Out| SMS In| MMS Out| MMS In  
---|---|---|---|---  
AT&T| $0.0035| $0.0035| $0.0090| $0.0090  
T-Mobile| $0.0045| $0.0025| $0.0100| $0.0100  
Verizon| $0.0045| $0.0070| $0.0070| —  
US Cellular| $0.0050| $0.0100| $0.0100| $0.0100  
All Other Carriers| $0.0040| $0.0100| $0.0100| —  
  
3

## Voice

Voice call costs are billed per minute. Below is the breakdown for US and Canada, plus additional charges for recording, transcription, and related services.

Outbound Calls

**Total:~~**~~~~$0.0180~~~~**~~ $0.0166 / minute**  
 _(Discount on US & Canada outbound calling rates)_

Component| Rate  
---|---  
Outbound USA| $0.0126/min (10% discount on $0.014 list)  
Client Minutes| $0.004/min  
  
Inbound — Web, Mobile, or Deskphone

**Total:~~~~**~~~~$0.0129~~~~**~~ ~~ $0.01165 / minute**  
 _(Discount on US & Canada inbound calling rates)_

Inbound calls have two legs: the call arriving at your platform number, and the forwarded leg to where you answer. Both are billed.

Component| Rate  
---|---  
Incoming Call (USA)| $0.00765/min (10% discount on $0.0085 list)  
Client Minutes| $0.004/min  
  
Inbound — USA Forwarding Number

Total: $0.02 / minute

Component| Rate  
---|---  
Incoming Call (USA)| $0.00765/min  
Outgoing Call (to forwarding number)| $0.0126/min  
  
International Forwarding

Forwarding to an international number (e.g., a UK mobile) uses Twilio's international rates for the second leg, which are higher than standard US/Canada rates.  
  


BILLING $ REGIONALS NOTES  
Calls are billed in full minutes, any partial minute rounds up. Calls to **Alaska** and **Yukon Territory** follow Twilio's regional pricing, not standard US/Canada rates.

  


Additional Voice Charges

Service| Rate  
---|---  
Call Recording| $0.0025/min  
Call Recording Storage| $0.0005/min/month  
Call Transcription| $0.024/min  
Answering Machine Detection| $0.0075/call  
Voicemail Drops| $0.0180/min  
Conference Calls| $0.0018 – $0.0040/min/participant (region-dependent)  
Amazon Polly (Text-to-Speech)| $0.00084/100 characters  
  
Conference Call Regional Rates

Region| Rate / Participant / Min  
---|---  
US| $0.0018  
Dublin| $0.0025  
Tokyo| $0.0030  
Singapore| $0.0030  
Sydney| $0.0030  
São Paulo| $0.0040  
  
4

## A2P Pricing

A2P Brand and Campaign registration fees for Low Volume and High Volume campaigns:

Type| Daily Segment Limit| Monthly Campaign Fee| One-Time Registration Fee  
---|---|---|---  
Sole Proprietor| 3,000 segments/day| Upto $2.10  
/Campaign| Up to $23.475  
(incl. $3 Fast Track)  
Low Volume (LV)| 600,000 segments/day| $1.50- $10.50  
/Campaign| Up to $23.475  
(incl. $3 Fast Track)  
High Volume (HV)| 600,000 segments/day| $10.50  
/Campaign| $68.625  
(incl. $3 Fast Track)  
  
IMPORTANT

  * **Submitting your campaign starts both your one time registration fee and monthly campaign fee, regardless of the review outcome.**  
  

  * **Don't want to continue?** Delete your campaign to stop future monthly charges.  
  

  * The **$3 Fast Track fee** is **non-refundable** and speeds up the campaign review process.  
  

  * **Starting February 1, 2026:** A2P campaign resubmissions are **free**. The previous **$15 resubmission fee** has been removed.


5

## Pass-Through Charges & Re-billing

Certain communication products are classified as **pass-through charges**. A fixed **5% markup** is applied to these charges at the location (sub-account) level, regardless of whether your agency has re-billing enabled.

Which charges get the 5% markup?

Category| Description  
---|---  
A2P Registration Fees| One-time Brand Registration, Campaign Registration, and recurring monthly campaign fees.  
SMS Carrier Fees| Carrier surcharges applied by mobile carriers for inbound and outbound SMS messages.  
MMS Carrier Fees| Carrier surcharges applied by mobile carriers for inbound and outbound MMS messages.  
Verified Caller ID| Charges associated with the Verified Caller ID service.  
RCS Messaging Carrier Fees| Carrier fees associated with Rich Communication Services (RCS) messaging.  
  
How Re-billing Works

The 5% markup above always applies to the categories listed. If your agency has re-billing enabled, your configured re-billing amount is applied in addition to this markup.

  * **Re-billing enabled:**   
Base cost → +5% location markup → + agency's configured re-billing amount.
  * **Re-billing disabled:**   
Base cost → +5% location markup only. No additional re-billing markup is added.


Example (Base SMS Carrier Fee = $10.00, Agency Reselling Multiplier = 2x)

Item| Rebilling Enabled| Rebilling Disabled  
---|---|---  
Base carrier fee| $10.00| $10.00  
5% location markup ($10.00 × 1.05)| $10.50| $10.50  
Agency rebilling ($10.50 × 2)| $21.00| —  
Final amount billed to the location| $21.00| $10.50  
  
Where to configure Re-billing?

Agency owners configure re-billing from **Agency View → Reselling → Core Services**. From there you can:

  * Set the Resell Amount (re-billing multiplier) for supported platform services.
  * Set custom pricing for Marketplace Apps.
  * Control the pricing your sub-accounts (locations) pay for supported products.


Key Points

  * The 5% markup always applies to the pass-through categories listed above, at the location (sub-account) level.
  * Enabling or disabling re-billing does not remove the 5% markup.
  * If re-billing is enabled, the configured re-billing amount is applied after the 5% markup has been added.


6

## Number Intelligence

Number Intelligence is a bundle of three functions that are turned on/off together. Refer to **Number Intelligence — Number Validation, Spam Detection, and Unknown Caller** for full details.

![Number Intelligence settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074921397/original/BjtQ36oYFNcmxgwnzeDrTp947lm9jNgt5A.png)

  * **Number Validation — $0.005 / call:** Before sending an SMS, check if the number is valid. If invalid, the SMS is not sent.
  * **Spam Detection — $0.005 / test:** When receiving an incoming US call, test it for spam and mark as "spam likely" if it fails.
  * **Name Lookup — $0.01 / lookup:** When receiving an incoming US call, look up the caller's name if the number is not linked to a contact or the contact name is empty.
  * **Number Format Lookups:** All number format lookups to support calls are free of cost.


7

## Frequently Asked Questions

Q: Why am I being charged for incoming SMS?

The native phone system charges for both inbound and outbound SMS at the same rate.

Q: Will SaaS rebilling work if I move sub-accounts to the native Phone System?

Yes, SaaS rebilling will continue to work with the native Phone System.

Q: Which categories have a 10% discount applied?

**Phone Numbers** — US and Canada only, all number types.  
**SMS** — US/Canada to US/Canada only, both inbound and outbound.  
**Voice Calls** — US/Canada to US/Canada only, both incoming and outgoing (excludes items listed in Additional Voice Charges).

Q: I was billed $20 right away but haven't made any calls. Is this expected?

Yes. The wallet auto-recharged as soon as the balance dropped below the threshold set in the wallet configurator.

![Wallet configurator](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074921482/original/fRdWrXrG4mZyZYHUrBkJuFzpnuX9Y_1eMg.png)

Q: Will I be charged if I encounter an error when sending an SMS?

If there's an internal error before the message is handed off to the phone provider, you won't be charged. However, charges apply to every message where a delivery attempt has been made — regardless of the final delivery status. This includes toll-free numbers, A2P numbers, and messages undeliverable due to country restrictions. Refunds will not be provided for undelivered SMS.

Q: Why am I getting charged for Call Recording Storage even though I didn't record calls recently?

Any call recording stored — including older recordings — incurs ongoing storage charges billed daily per sub-account. To avoid these charges, go to **Settings → Phone Numbers → Advanced Settings → Voice Calls → Call Recording** to automatically delete older recordings, or set the deletion period to 1 day and disable call recording for future calls.

![Call recording settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155074920889/original/3QRuC0klOSV2enbNRc8_wM_gz53n8JTg3g.png)

Q: Why do I pay Conference Call charges for all outgoing calls, even without a transfer?

The outgoing call flow is optimised for seamless, low-latency transfers. A Conference Call is initiated for all outgoing calls as part of the standard call flow implementation.

Attachments (3)

[ csv NumbersPricing_Updated.csv  
8.55 KB ](</helpdesk/attachments/155069177045>)

[ csv voice pricing Updated .csv  
30.7 KB ](</helpdesk/attachments/155074965168>)

[ csv Messaging_pricing_v300626 - Sms_Pricing (4) (2).csv  
56 KB ](</helpdesk/attachments/155075013958>)

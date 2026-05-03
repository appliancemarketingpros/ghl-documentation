# WhatsApp - Messaging Limits

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000001637-whatsapp-messaging-limits](https://help.gohighlevel.com/support/solutions/articles/155000001637-whatsapp-messaging-limits)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

Messaging limits are the maximum number of unique WhatsApp user phone numbers your business can deliver messages to, outside of a customer service window, within a moving 24-hour period.

Messaging limits are calculated and set at the **business portfolio level** and are shared by all business phone numbers within a portfolio. This means that if a business portfolio has multiple business phone numbers, it's possible for one number to consume all of the portfolio's messaging capability within a given period.

Business portfolios are initially limited to 250 messages in a 24-hour moving period, but this limit can be increased.

* * *

**TABLE OF CONTENTS**

  * Understanding WhatsApp Messaging Limits
  * Initial WhatsApp Messaging Limits
  * Increasing WhatsApp Messaging Limit
    * Scaling Paths
    * Approvals
    * Denials
    * Automatic Scaling
  * Best Practices
  * FAQs


* * *

### Understanding WhatsApp Messaging Limits

WhatsApp messaging limits define the maximum number of unique WhatsApp user phone numbers your business can send messages to outside of a customer service window within any rolling 24-hour period. These limits apply to business-initiated conversations — messages sent via marketing, utility, or authentication templates.

Importantly, limits are set at the **business portfolio level** , not per individual phone number. All business phone numbers within a portfolio share the same limit pool, so heavy usage by one number can impact the capacity available to others in the same portfolio.

* * *

### Initial WhatsApp Messaging Limits

Newly created business portfolios start with a messaging limit of 250. However, this limit can be increased to accommodate higher volumes. The available tiers are:

  * 250 (default for new business portfolios)
  * 2,000 (by completing a scaling path)
  * 10,000 (via automatic scaling)
  * 100,000 (via automatic scaling)
  * Unlimited (via automatic scaling)  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069298296/original/xCZrl1lrcq_07N-US7KNdv962MQNm9uIpg.png?1776342881)


    
    
    Note: Messaging limits are shared across all business phone numbers within a portfolio. A single high-volume number can consume the entire portfolio's daily limit.

* * *

### Increasing WhatsApp Messaging Limit

You can increase your messaging limit to 2,000 by completing one of the scaling paths below. After that, Meta will automatically increase your limit further if you meet the automatic scaling criteria.

## Scaling Paths

Complete any one of the following to become eligible for a limit increase to 2,000:

  * [Verify your business](<https://www.facebook.com/business/help/2058515294227817>) through Meta's business verification process.
  * Have your **solution provider verify your business** on your behalf (if you were onboarded through a solution partner).
  * Send **2,000 delivered messages** outside of customer service windows to unique WhatsApp user phone numbers within a 30-day moving period, using templates with a [high quality rating](<https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-quality>).


Once you complete one of these paths, Meta will analyze your message quality to determine if your number is eligible for a limit increase.

#### Approvals

If your request is approved, Meta will immediately increase your business phone number's messaging limit to 2,000 and notify you by email and developer alert. A `business_capability_update` webhook will also be triggered with the new limit value.

Once approved at 2,000, your limit can continue to grow automatically — see Automatic Scaling below.

#### Denials

If your request is denied, your messaging limit will remain at its current level. Meta will notify you via email and developer alert. An `account_alerts` webhook will be triggered indicating which alternative path you can take:

Alert Type| Action You Can Take  
---|---  
`INCREASED_CAPABILITIES_ELIGIBILITY_DEFERRED`| Send 2,000 delivered messages outside of customer service windows to unique WhatsApp users within 30 days, using high-quality templates.  
`INCREASED_CAPABILITIES_ELIGIBILITY_FAILED`| Send 2,000 delivered messages outside of customer service windows to unique WhatsApp users within 30 days, using high-quality templates.  
`INCREASED_CAPABILITIES_ELIGIBILITY_NEED_MORE_INFO`| [Verify your identity](<https://www.facebook.com/business/help/587323819101032>), or send 2,000 delivered messages outside of customer service windows within 30 days using high-quality templates.  
  
#### Automatic Scaling

Once your business portfolio's messaging limit has been increased to 2,000, Meta will automatically evaluate it for further increases. Your limit will be raised to the next tier within 6 hours if both of the following criteria are met:

  * You are sending **high-quality messages** across all of your business phone numbers and templates.
  * In the last 7 days, your business has **utilized at least half** of your current messaging limit.


    
    
    Automatic scaling moves your limit up one tier at a time: 2,000 → 10,000 → 100,000 → Unlimited. Each step happens within 6 hours of meeting the criteria.

* * *

### Best Practices

**Opt-In Consent:** Always ensure that customers have explicitly opted in to receive messages from your business on WhatsApp. Respect their privacy and preferences.

**Timely Responses:** Aim to respond to customer inquiries promptly. Quick responses enhance customer satisfaction and improve the overall customer experience.

**Personalization:** Tailor your messages to each customer whenever possible. Personalized messages tend to be more engaging and can foster stronger customer relationships.

**Value-Added Content:** Provide valuable content to your customers through WhatsApp, such as product updates, exclusive offers, and helpful tips related to your industry.

**Clear Communication:** Ensure your messages are concise, clear, and relevant. Avoid spammy or irrelevant content that could annoy customers.

**Example**
    
    
    **Send:** "Hi Sarah! We're excited to share that our Spring Collection has arrived! Check out the latest styles and enjoy 20% off your first purchase with code SPRING20. Shop now: [Link]"
    
    
    **Avoid:** "Hey Sarah! Did you know we sell shoes too? Come visit our store for amazing deals on footwear!!!! #ShoeLove"

**Security Measures:** Implement security measures to protect customer data and ensure the confidentiality of conversations. Avoid sharing sensitive information over WhatsApp.

**Feedback Loop:** Encourage customers to provide feedback on their experience with your business on WhatsApp. Use this feedback to improve your services and offerings.

* * *

### FAQs

#### **Q: How many conversations can I start with my WhatsApp Business account initially?**

#### New business portfolios start with a limit of 250 delivered messages to unique users per 24-hour moving period.

#### **Q: What does it mean that limits are at the "portfolio level"?**

#### All business phone numbers within the same business portfolio share a single messaging limit. If one phone number sends a high volume of messages, it reduces the capacity available to other numbers in the same portfolio for that period.

#### **Q: What does it mean to have a 'business-initiated' conversation?**

#### This refers to any message your business sends to a customer outside of a customer service window — typically through marketing, utility, or authentication templates. These count toward your messaging limit.

#### **Q: How can I increase my conversation limit?**

#### Complete any one of these scaling paths to reach the 2,000 tier:

  * #### Verify your business through Meta's business verification process.

  * #### Have your solution provider verify your business.

  * #### Send 2,000 delivered messages to unique WhatsApp users within 30 days using high-quality templates.


#### After reaching 2,000, your limit can increase automatically to 10,000, 100,000, and Unlimited based on your usage and message quality.

#### **Q: Is there a way to get my limit increased automatically?**

#### Yes. Once your portfolio is at 2,000, Meta automatically evaluates your limit for increases. If you've used at least half your current limit in the past 7 days and are sending high-quality messages, your limit will be raised to the next tier within 6 hours.

#### **Q: Why does message quality matter for increasing my conversation limit?**

#### WhatsApp prioritizes a positive user experience. Sending high-quality, relevant messages builds trust with both users and Meta's systems, and is a requirement for both initial approval and ongoing automatic scaling.

#### **Q: Where can I check my current conversation limit?**

#### In [WhatsApp Manager](<https://business.facebook.com/wa/manage/home/>), go to **Account tools > Messaging limits** panel.

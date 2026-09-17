# Meta Pixel Tracking for Events

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008595-meta-pixel-tracking-for-events](https://help.gohighlevel.com/support/solutions/articles/155000008595-meta-pixel-tracking-for-events)  
**Category:** Marketing  
**Folder:** Events

---

Meta Pixel tracking in HighLevel Events helps organizers measure how visitors move from viewing an event to completing an RSVP or ticket order. By connecting a Meta Pixel to an individual event, you can map attendee actions to Meta events and measure important conversion points. Ticketed events can also send purchase details such as order value, currency, ticket quantities, and ticket identifiers.

* * *

**TABLE OF CONTENTS**

  * What is Meta Pixel Tracking for Events?
  * Key Benefits of Meta Pixel Tracking for Events
  * Supported Meta Pixel Tracking Events
  * Purchase Data Sent to Meta
  * How To Setup Meta Pixel Tracking for Events
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Meta Pixel Tracking for Events?**

  


Meta Pixel Tracking for Events connects attendee activity in a HighLevel event with Meta conversion events. This gives organizers better visibility into registration intent, completed registrations, and ticket purchases generated through their event marketing.

  


Meta Pixel tracking is configured independently for each event under **Settings → Link & tracking**.

* * *

## **Key Benefits of Meta Pixel Tracking for Events**

  


  * **Conversion visibility:** Measure attendee activity from the initial event page visit through a completed RSVP or ticket order.  
  

  * **Flexible event mapping:** Choose which Meta event should fire for each supported attendee action.  
  

  * **Event-level configuration:** Configure Meta Pixel tracking independently for each event.  
  

  * **Ticket purchase insights:** Track multiple stages of the ticket checkout journey.  
  

  * **Revenue context:** Send supported purchase details with completed ticket orders.  
  

  * **Duplicate-event protection:** Session-based deduplication helps reduce repeated conversion signals.


* * *

## **Supported Meta Pixel Tracking Events**

  


RSVP and Ticketed events have different attendee journeys, so HighLevel provides tracking actions that correspond to the steps visitors complete for each event type.

  


Event type| Supported attendee actions  
---|---  
**RSVP Events**|  Event page viewed, RSVP started, RSVP completed  
**Ticketed Events**|  Event page viewed, Checkout started, Ticket selection completed, Registration form submitted, Payment details submitted, Ticket order completed  
  
  


Event Type| Attendee Action| When It Fires  
---|---|---  
**RSVP**|  Event page viewed| When a published event page is loaded  
**RSVP**|  RSVP started| When a visitor opens the RSVP form  
**RSVP**|  RSVP completed| When the RSVP is successfully confirmed  
**Ticketed**|  Event page viewed| When a published event page is loaded  
**Ticketed**|  Checkout started| When the attendee begins checkout  
**Ticketed**|  Ticket selection completed| When ticket selection is completed  
**Ticketed**|  Registration form submitted| When the registration form is submitted  
**Ticketed**|  Payment details submitted| When payment details are submitted  
**Ticketed**|  Ticket order completed| When the ticket order is successfully completed  
  
  


Completed ticket orders are tracked for both paid tickets and **$0 orders**.  
  


**Purchase data:** Completed ticket orders can also send order value, currency, ticket quantities, and ticket identifiers to Meta.  
  


**Deduplication:** HighLevel uses session-based deduplication to help prevent the same attendee action from being reported multiple times because of browser back navigation, page refreshes, payment redirects, or repeated completion checks.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079933950/original/2wr708qTk62B0A5O1VZdWhvpdHEjWn6eiw.png?1788362576)

* * *

## **Purchase Data Sent to Meta**

  


A completed ticket order can provide more context than a registration count alone. Commerce details help organizers evaluate the value and composition of ticket purchases generated through their event marketing.  
  


Completed ticket orders can include:  
  


  * **Order value:** The value associated with the completed ticket order.
  * **Currency:** The currency associated with the order.
  * **Ticket quantities:** The number of tickets represented in the order.
  * **Ticket identifiers:** Identifiers associated with the tickets included in the transaction.  
  


This additional data is associated with completed ticket orders and can support campaign reporting focused on revenue outcomes rather than registrations alone.

* * *

## **How To Setup Meta Pixel Tracking for Events**

  


Using the correct Meta Pixel ID and mapping the attendee actions that matter to your campaign ensures the conversion data represents the event journey you want to measure.

  


### 1\. Locate Your Meta Pixel ID

  


Locate the Pixel ID for the Meta data source you want to connect to your event.

HighLevel's existing Meta documentation explains how to locate the Dataset ID used as the Pixel ID in Meta Events Manager.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079934081/original/Qk4kMpRcJ9x7MQmEjdhVOKSFdfdIVwLzRg.png?1788362650)  


  


[**How to set up a Funnel Event Pixel for Facebook Conversion API?**](<https://help.gohighlevel.com/support/solutions/articles/48001236281?utm_source=chatgpt.com>)

  


###  2\. Open Link & tracking

  


  1. In your HighLevel sub-account, go to **Memberships → Events**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079934348/original/wbJEUuNvvYHsDawbdh1YP838tNuPskUXMw.png?1788362841)  
  

  2. Select the event you want to track.  
  

  3. Open **Settings** and**** Select **Link & tracking**.
  4. Locate the **Meta Pixel** settings.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079934419/original/dMdBG7IG1iyv6dQ__wosrkxfGorpxLvH1g.png?1788362895)


###   
  


### 3\. Add the Meta Pixel ID  
  


Enter the **Meta Pixel ID** associated with the Meta data source you want to use for this event.

Meta Pixel tracking is configured independently for each event, so confirm that you are editing the correct event before configuring the mappings.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079934567/original/OUp8f5LCNZIc8mxoFisPGUee1zyQ0oDpQA.png?1788362985)  
  


### 4\. Map Attendee Actions to Meta Events  
  


Use the **Event mapping** options to choose which Meta event should fire for each supported attendee action.  
  


For RSVP events, configure mappings for:  
  


  1. Event page viewed  
  

  2. RSVP started  
  

  3. RSVP completed  
  


For Ticketed events, configure mappings for:  
  


  1. Event page viewed  
  

  2. Checkout started  
  

  3. Ticket selection completed  
  

  4. Registration form submitted  
  

  5. Payment details submitted  
  

  6. Ticket order completed


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079934781/original/cwnhhJHVQf4bqr0na5-4hqBCXbA4N_6CqA.png?1788363055)

  
  


### 5\. Test the Attendee Journey

  


Use the published event experience to verify the actions that matter to your tracking plan. The **Event page viewed** action is defined for published event-page loads, so testing against the public experience is the appropriate way to validate that part of the journey.

  


For an RSVP event, test the page view, opening the RSVP form, and a successful RSVP. For a Ticketed event, test the relevant checkout stages through a completed order, including a $0 ticket order when that is part of your use case.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079934969/original/oj3FhtZr5neYQkb-b848rkEnTd4b-16Lfg.png?1788363171)

* * *

## **Frequently Asked Questions**

  


**Q: Is Events Meta Pixel tracking the same as an Ad Manager conversion pixel?**  
No. Events Meta Pixel tracking is configured directly within an individual HighLevel event under **Settings → Link & tracking**. Ad Manager conversion tracking uses a separate configuration process.

**Q: Do I need to install Funnel tracking code to use Meta Pixel tracking for Events?**  
The native Events integration is configured directly in the event using the Meta Pixel ID and Event mapping settings. Funnel tracking code belongs to a separate Funnel or Website tracking setup.

**Q: Are $0 ticket orders tracked?**  
Yes. Successfully completed $0 ticket orders are tracked as completed ticket orders.

**Q: Can Meta Pixel tracking report attendee check-ins?**  
Check-in is not listed as a supported Meta Pixel tracking action for this feature. HighLevel provides separate Events workflow triggers for registration and check-in automation.

**Q: Does previewing an unpublished event trigger Event page viewed?**  
The feature defines **Event page viewed** as occurring when a published event page is loaded.

* * *

## **Related Articles**

**  
**

  * **[How to Create and Manage Events in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000008071-how-to-create-and-manage-events-in-highlevel-private-beta-?utm_source=chatgpt.com>)  
  
**
  * **[How to set up a Funnel Event Pixel for Facebook Conversion API?](<https://help.gohighlevel.com/support/solutions/articles/48001236281?utm_source=chatgpt.com>)  
  
**
  * **[Facebook Conversions API Trigger in Workflows](<https://help.gohighlevel.com/support/solutions/articles/48001185099-facebook-conversions-api-trigger-in-workflows?utm_source=chatgpt.com>)  
  
**
  * **[Events and Workflows Integration](<https://help.gohighlevel.com/support/solutions/articles/155000008431-events-and-workflows-integration?utm_source=chatgpt.com>)  
  
**
  * [**Embed Events with Code Snippet**](<https://help.gohighlevel.com/support/solutions/articles/155000008342-embed-events-with-code-snippet?utm_source=chatgpt.com>)

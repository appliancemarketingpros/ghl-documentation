# User Lifecycle Events via Webhooks

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007884-user-lifecycle-events-via-webhooks](https://help.gohighlevel.com/support/solutions/articles/155000007884-user-lifecycle-events-via-webhooks)  
**Category:** Workflows  
**Folder:** Webhooks Workflow Actions

---

HighLevel now supports webhook events for user lifecycle activity, allowing developers to receive real-time notifications whenever users are created, updated, or deleted.

These webhook events help external systems stay synchronized without relying on polling or manual checks.

* * *

**TABLE OF CONTENTS**

  * User Lifecycle Events via Webhooks
  * Frequently Asked Questions
  * Related Articles


* * *

## **Supported User Lifecycle Events**  
  


The following webhook events are now available:  
  


  * `user.created`  
  

  * `user.updated`  
  

  * `user.deleted`  
  


These events are triggered whenever a user is created, updated, or removed inside HighLevel.

* * *

## **Available Webhook Events**  
  


### **user.created**  
  


Triggered when a new user is created.

Common use cases:  
  


  * Provisioning external accounts  
  

  * Syncing users to third-party systems  
  

  * Triggering onboarding workflows


###   
**user.updated**  
  


Triggered when user information changes.  
  


Common use cases:  
  


  * Syncing profile updates  
  

  * Updating permissions or roles  
  

  * Keeping external CRMs synchronized


###   
**user.deleted**  
  


Triggered when a user is deleted.  
  


Common use cases:  
  


  * Removing external access  
  

  * Revoking permissions  
  

  * Cleaning up downstream systems


* * *

## **Event Delivery Behavior**  
  


Webhook events are delivered in real time whenever supported user lifecycle actions occur.  
  


Additional delivery features include:  
  


  * Automatic retry attempts for failed deliveries  
  

  * Event IDs for idempotency handling  
  

  * Delivery logs for troubleshooting and diagnostics


##   
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070955665/original/Q_ZgzvkBG3qQAWScA5DlmrlcvbCe9Xo8IQ.png?1778386305)**  
  


  


This screenshot demonstrates:  
  


  * Inbound webhook flow  
  

  * Real-time event delivery  
  

  * Third-party integration flow  
  

  * Webhook-triggered automation behavior


* * *

## **Webhook Security**  
  


User lifecycle webhooks use signed requests to help verify event authenticity.

Security features include:  
  


  * HMAC request signing  
  

  * Event identifiers for duplicate prevention  
  

  * Retry handling for failed webhook deliveries  
  


Always validate webhook signatures before processing incoming webhook events.

* * *

## **Common Use Cases**  
  


Developers commonly use these events to:  
  


  * Sync users across multiple platforms  
  

  * Automate onboarding and offboarding  
  

  * Maintain analytics and reporting pipelines  
  

  * Trigger provisioning workflows  
  

  * Keep external systems updated in real time


* * *

## **Frequently Asked Questions**  
  


**Q: What user events are supported?**  
A: HighLevel currently supports `user.created`, `user.updated`, and `user.deleted`.

**Q: Are webhook deliveries retried if they fail?**  
A: Yes. Failed webhook deliveries are automatically retried automatically.  
  


**Q: Are webhook requests signed?**  
A: Yes. User lifecycle webhooks support HMAC request signing.  
  


**Q: Can webhook events be used for external user synchronization?**  
A: Yes. These events are designed to support real-time synchronization across external systems.  
  


**Q: Do webhook events include unique event IDs?**  
A: Yes. Event IDs are included to support idempotent processing and duplicate prevention.

* * *

## **Related Articles**

  


  * [Webhook: New SaaS Plan Created](<https://help.gohighlevel.com/en/support/solutions/articles/155000005897>)

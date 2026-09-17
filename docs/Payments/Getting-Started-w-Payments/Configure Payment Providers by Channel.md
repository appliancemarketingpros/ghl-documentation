# Configure Payment Providers by Channel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007346-configure-payment-providers-by-channel](https://help.gohighlevel.com/support/solutions/articles/155000007346-configure-payment-providers-by-channel)  
**Category:** Payments  
**Folder:** Getting Started w/ Payments

---

This article explains how payment providers work across different channels, what is supported today, what is planned, and how Default and Preferred provider settings affect checkout behavior.

* * *

**TABLE OF CONTENTS**

  * Overview of Configuring Payment Providers by Channel
  * Key Benefits of Configuring Payment Providers by Channel
  * Supported Channels
  * How Provider Selection Works
  * Live Mode vs Test Mode
  * How to Configure Payment Providers by Channel
  * Frequently Asked Questions
  * Related Articles


* * *

# **Overview of Configuring Payment Providers by Channel**

  


Configuring payment providers by channel allows you to assign specific payment providers to different parts of your business, such as funnels, forms, stores, and invoices. Instead of relying on a single global default provider, HighLevel enables channel-level control so payments are routed based on where the transaction originates. This provides flexibility to optimize payment experiences, reduce fees, and tailor provider usage to specific use cases.

* * *

## **Key Benefits of Configuring Payment Providers by Channel**

  


  * **More Flexibility:** Use different payment providers for different sales experiences  
  

  * **Better Optimization:** Route payments based on fees, regions, or provider strengths  
  

  * **Safer Testing:** Experiment with new providers in Test mode without affecting live transactions  
  

  * **Cleaner Setup:** No need to constantly switch your account’s default provider


* * *

## **Supported Channels**

  


Supported channels are Funnels - One Step Order Forms, Funnels - Two Step Order Forms, Forms, Stores, Calendars

Invoices, Invoice Auto Payment, Payment Links, Courses, Communities and Surveys.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067633090/original/d0j6u9ylm4TpDI-BrOs4PfEep9Itb8VYXQ.png?1774368085)

* * *

## **How Provider Selection Works**

  


Payment provider selection in HighLevel follows a simple set of rules that determine which provider is used at checkout.

  


  * **Provider Priority:** Channel-level settings override the global default provider. If no provider is set for a channel, the global default is used. Only connected providers are available to select when selecting a provider.  
  

  * **Supported Provider Combinations:** You can use **PayPal + one other provider** (e.g., Stripe or NMI). Multiple non-PayPal providers together are not supported (e.g., Stripe + NMI).  
  

  * **Editing Providers:** You can remove any selected provider. PayPal can be added or removed alongside another provider. PayPal cannot be directly replaced by another provider (must be removed first).


* * *

## **Live Mode vs Test Mode**

  


Separating Live and Test configurations allows you to experiment with providers without affecting real transactions. This is essential for validating integrations and testing checkout experiences safely.  
**  
**

  * **Live Mode:** Used for real customer transactions  
**  
**

  * **Test Mode:** Used for testing payment flows without processing real payments  
  


  * Each mode can have different providers assigned per channel


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067638393/original/vAb6zwylvoef4-UHOhI8aPzxrjKxX9n-4Q.jpeg?1774371017)

* * *

## **How to Configure Payment Providers by Channel**

  


Proper setup ensures payments are routed correctly and prevents failed transactions. Follow these steps to configure providers effectively.

  


  1. Navigate to **Payments**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067631348/original/y9zs559O-BlpJo8pGRgUZLOjBnzHxJfXhg.png?1774367145)  
  


  2. Click on **Integrations**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067631491/original/0ESzJdAoiZEg8MqdvQy1SnzMCYd12BfCrg.png?1774367197)  
  


  3. Click **Configure Providers.**  
  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067631597/original/ZiHHcn6x0hQFTZntSoROfbNZufPQxHwOhA.png?1774367229)**  
  


  4. Toggle between**Live** or **Test** mode as needed.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067631664/original/hSdp81mLzvEZ509gfNwCxxH3TMDpi-IeBA.png?1774367267)  
  


  5. Select your preferred payment provider(s) for each channel  
  

     * **Adding a Provider:** Click the '**+** ' next to a channel and select from connected providers in the dropdown(Stripe, PayPal, Square, etc.). You can add PayPal and one additional provider (e.g., Stripe or NMI).” The dropdown only shows providers that are already connected in the account.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067632534/original/8vaQLn5Y8LhYyGJfGqQiVuntG4SHFd87sA.png?1774367777)  
  

     * **Removing a Provider:** Click the '**X'** next to the provider. Confirm removal when prompted.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067632102/original/TlxTt5Z5IhFCCrJa7fuFEENhPgWFwi_gbg.png?1774367508)  
  

     * **Resetting a Provider:** Resetting removes custom configuration. Channel will revert to the global default provider.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155067632883/original/YGjbOlnveYthZ6ecEG9S1qLypgDJy5DPIw.png?1774367942)


* * *

## **Frequently Asked Questions**

**  
**

**Q: What happens if a Preferred Provider is disconnected?**

If a provider used at the channel level is disconnected from the integrations page, the system automatically falls back to the default provider. If you reconnect it later, you’ll need to select it again as the preferred provider for the channel.

  


**Q: Can I configure providers at a more granular level (e.g., per store or funnel)?**  
Not yet. Today, configuration is at the channel level. More granular control (per store, funnel, or asset) is planned for future updates

  


**Q: Can I remove all providers from a channel to disable payments?**  
No. If all providers are removed, HighLevel will revert the channel to the global default provider to prevent accidental loss of payment functionality. This is designed to prevent accidental removal of payment options for active services. Payments are only hidden if no providers are connected at all.

  


**Q: How many payment providers can I use on a checkout?**  
You can use PayPal plus one additional provider (e.g., Stripe or NMI). Using multiple non-PayPal providers together is not supported.

**  
**

**Q: How does the default provider affect channel configuration?**  
The default provider acts as a fallback. If you set a provider at the channel level, it overrides the default. If no channel-level provider is set, the default is used.

  


**Q: What payment options will customers see at checkout?**  
If both a default provider and PayPal are configured, customers will see both options. If PayPal is not configured, only the default provider will be displayed.

* * *

## **Related Articles**

  


  * [Getting Started - Connect Stripe](<https://help.gohighlevel.com/en/support/solutions/articles/155000005073>)  
  

  * [Supported Payment Providers & Methods by Product Area (What Works Where)](<https://help.gohighlevel.com/en/support/solutions/articles/155000006075>)  
  

  * [Authorize.net integration for processing payments](<https://help.gohighlevel.com/en/support/solutions/articles/48001231144>)  
  

  * [How to set up the NMI integration?](<https://help.gohighlevel.com/en/support/solutions/articles/48001235741>)  
  

  * [How to send your first Invoice](<https://help.gohighlevel.com/en/support/solutions/articles/155000006908>)

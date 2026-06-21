# How to integrate with Mercado Pago for accepting payments?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007562-how-to-integrate-with-mercado-pago-for-accepting-payments-](https://help.gohighlevel.com/support/solutions/articles/155000007562-how-to-integrate-with-mercado-pago-for-accepting-payments-)  
**Category:** Payments  
**Folder:** Payment integrations, methods and settings

---

In this article, you will learn how to connect your Mercado Pago account so you can accept payments inside HighLevel. To complete the setup, you will need your Mercado Pago production credentials, and you may also need to configure webhook notifications inside your Mercado Pago developer settings.

* * *

**TABLE OF CONTENTS**

  * What is Mercado Pago?
    * Key Benefits of Mercado Pago
    * Prerequisites and Requirements
    * Important Notes
    * How To Set Up Mercado Pago
    * Frequently Asked Questions
    * Related Articles


* * *

# **What is Mercado Pago?**

  


Mercado Pago is a payment provider that businesses can use to accept payments from customers, especially across LATAM markets. HighLevel integrates with Mercado Pago so businesses can connect it directly inside their account instead of relying on separate workarounds or manual payment setups.

  


Once connected, businesses can manage the provider from **Payments** > **Integrations** and choose where to use it across supported payment channels in HighLevel.

* * *

## **Key Benefits of Mercado Pago**

  


  * **Localized experience:** Offer payment methods your customers already trust  
  

  * **Better conversions:** Reduce friction at checkout with familiar providers  
  

  * **Market expansion:** Tap into a fast-growing LATAM payments ecosystem  
  

  * **More control:** Decide how and where Mercado Pago fits into your payment stack


* * *

## **Prerequisites and Requirements**

A successful Mercado Pago setup depends on having the right credentials, account settings, and webhook information ready before you start. 

  


Before you begin, make sure you have:  
  


  * A Mercado Pago account with CVV/CVC-less support enabled.  
  


  * Access to your Mercado Pago developer dashboard.  
  


  * Your business website URL, in case Mercado Pago requests it while enabling production credentials.


  

    
    
    **Note:** Live payments require **production credentials** (not test credentials). Production credentials are tied to an app you create in Mercado Pago under **Your integrations**.

  


You will need these values from Mercado Pago:  
  


  * Public Key  
  


  * Access Token  
  


  * Country of account  
  


  * Webhook secret


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069831895/original/1Aat3aYQRlWyDQHDQ59Rag_wxd1cmCPErw.png?1776970626)

* * *

## **Important Notes**

  


  * Use **production****credentials** for real payments. Test credentials are only for testing and will not process live transactions.  
  

  * Keep your **Access Token** private and store it securely.  
  

  * Depending on your Mercado Pago country setup, available options may vary. Different countries have different minimum accounts, refer to FAQ for details.  
  

  * Your Mercado Pago account must have CVV less support enabled for this integration to work as expected.  
  

  * Mercado Pago doesn’t allow two checkout elements to be launched on one single page, for example you cannot keep two 1 step order forms on a funnel


* * *

## **How To Set Up Mercado Pago**

  


Proper setup ensures HighLevel can connect to Mercado Pago, route payments correctly, and receive payment event updates through webhooks. Completing each step carefully helps avoid failed connections and sync issues later.

_  
_

#### _**Step 1:** Open Mercado Pago in Payment Integrations_

  


  1. In HighLevel, go to **Payments** from the left navigation.  
  


  2. Open the **Integrations** tab.  
  


  3. Find **Mercado Pago** in the provider list and click **Connect**.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832129/original/taj8X46fLefiAXolSkiz3AUvnmFM44oF8g.png?1776971042)

  


  


#### **_Step 2:_**_Get your Mercado Pago production credentials_  
  


  1. Sign in to your Mercado Pago account.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832147/original/M9VaZu3rSe2OoADTckeiwvOQSBewXynEFg.png?1776971109)  
  


  2. Open the Mercado Pago developer area.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832148/original/hOVjVHRRDI3koe73BWH9zPgpqkflpXeD6A.png?1776971109)  
  


  3. Go to **Your integrations**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832177/original/WTOYFXq1KerSVJUWpInZfzQUsofZOW2AvQ.png?1776971141)  
  


  4. Open an existing application or create a new one.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832194/original/HA4gyUuUiVM9TfdrPTdkrLXjmJOgZvjdCQ.png?1776971153)  
  


  5. Go to **Production credentials** and copy the **Public Key** and **Access Token**. If production credentials are not active yet, complete any required business details such as your industry and website.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832209/original/1mngD4zHZ-pF2z4a9JQt_3mR7SB1PfbI9w.png?1776971168)


  


  
**If you need to create a new application:**

  


If you do not already have an application inside Mercado Pago, create one first. In most cases, Mercado Pago will ask you to:

  


  1. Enter an application name.  
  


  2. Choose the payment type or business use case for online payments.  
  


  3. Confirm your setup details.  
  


  4. Enable production credentials and use them in step 2.


  


  


#### **_Step 3:_**_Enter your Mercado Pago credentials in HighLevel_  
  


  1. Paste the **Public Key** into the matching field.  
  


  2. Paste the **Access Token** into the matching field.  
  


  3. Choose the correct **country** or **account region**.  
  


  4. Generate or enter your **Webhook Secret** in the matching field.  
  


  5. Click **Save** or **Connect**.


  


Once saved, your Mercado Pago account should be linked, now we will enable webhooks in Mercado Pago app.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069007852/original/wW-R8AsJkUZUKngMhHUTCRTcAIzhYuNpVQ.png?1776076918)

  


  


#### **_Step 4:_**_Configure webhooks in Mercado Pago_

  


Some Mercado Pago integrations require webhook notifications so payment events can sync correctly back to your platform. Log in to your Mercado Pago account and go to the developer panel. (<https://www.mercadopago.com.br/developers/en>)  
  


  1. In Mercado Pago, open the application used for the integration and go to **Webhooks**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832596/original/MTOhOFM4qPTN0zzxB0QdxF1gpihv6Nssiw.png?1776971609)  
  


  2. Click **Configure notifications**.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832599/original/iETOoBf_gCEfuEmi0YcvMAtMuea7eZ7Lnw.png?1776971622)  
  


  3. Complete the required webhook setup so payment events sync correctly back to HighLevel.  
  


     * Paste the webhook URL into the Production mode URL field: <https://backend.LeadConnectorhq.com/payments/mercado-pago/webhook>  
  
[](<https://backend.leadconnectorhq.com/payments/mercado-pago/webhook>)

     * Add Webhook secret same as on Lead Connector page  
  


     * Select the ‘Payment’ event required for your integration.  
  


     * Save your changes.


  


  


#### **_Step 5:_**_Assign Mercado Pago by channel_

  


After the integration is connected, open Manage**Provider Configurations** for Mercado Pago in HighLevel.  
  


  * Toggle between **Live** and **Test** mode as needed.  
  


  * Assign Mercado Pago to the channels where you want it to be available.


  


For more details about assigning payment providers by channel, see [Configure Payment Providers by Channel](<https://help.gohighlevel.com/en/support/solutions/articles/155000007346>).

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155069832740/original/bgsGZOK0Gv25D1Ug2iwFj8do7IHdChpReA.png?1776971875)

* * *

## **Frequently Asked Questions**

  


**Q: Are there any minimum amount conditions in my country?**

Yes. Mercado Pago has specific minimum and maximum payment amount rules depending on the payment method. If you create a product that does not meet these conditions, the payment may fail. Current reference is based on Mercado Pago's supported payment limits:

  


_Credit and Debit Cards_

  * Visa, Mastercard, American Express, Naranja, Cabal, and Sucrédito
  * Minimum amount for one time payments: $100.00
  * Minimum amount for installment purchases: $100.00 per installment
  * Maximum amount: $15,000,000.00  
  


 _Easy Payment and Rapipago_

  * Minimum amount: $100.00
  * Maximum amount: $1,000,000.00  
  


Reference: <https://www.mercadopago.com.ar/ayuda/monto-minimo-maximo-medios-de-pago_620>

  


**Q: What happens if I create a product in USD currency?**

At the moment, Mercado Pago does not dynamically convert the currency for this setup. It is recommended to keep your product or service currency the same as your domestic Mercado Pago account currency.

  


For example, if your Mercado Pago account is based in Argentina, you should use Argentine Peso for your product pricing.

  


**Q: I added two checkout or payment elements to my funnel, but they are not working**

Mercado Pago does not allow this because of its security conditions. You can only open one checkout screen in one active session. To avoid payment issues, make sure your funnel uses only one active Mercado Pago checkout or payment element at a time.  


  


For example, two or more order forms with card capturing element on a single funnel or webpage won’t be loaded. 

  


**Q: What happens if CVV less support is not enabled on my account?**

It is strongly recommended to enable CVV less support on your Mercado Pago account. Without it, features such as subscriptions, off session payments, and SaaS mode may not work correctly.

  


**Q: What countries are supported for this integration?**

Colombia, Argentina, Chile, Mexico, Ecuador, Uruguay, Peru, Brazil, El Salvador

  


**Q: How do I generate a webhook secret?**

A webhook secret is a random, high entropy string used to sign payload requests. This string can very well be a password that you can remember, but it should match at Lead Connector and Mercado Pago side. You may also use web based webhook secret generator, which will generate a hmac-sha256 algorithm based secret like this, these are more secure - e70fd2ccfed7cf82596fe0494925a0ada87e3b03873a83150bd5458754650211 (only for example)

  


**Q: What is CVV/CVC less account enablement**

CVV or CVC is the 3 or 4 digit security code printed on a credit or debit card. It is commonly used to verify online or phone transactions and helps reduce fraud.

  


In saved card payment flows, especially when charging customers off session or starting subscriptions using an already saved card, asking the customer to enter the CVV every time can create friction and increase drop off.

To avoid this, some payment providers support CVV less flows. In these flows, the card is securely vaulted in a way that allows smoother repeat payments and better compatibility with Lead Connector features such as subscriptions, off session payments, and SaaS related billing flows.

Your Mercado Pago account may already have this enabled, but you will need to verify this with the Mercado Pago support team. If it is not enabled, you will need to request activation from them.

* * *

## **Related Articles**

[  
](<https://help.gohighlevel.com/en/support/solutions/articles/155000007346>)

  * [Configure Payment Providers by Channel](<https://help.gohighlevel.com/en/support/solutions/articles/155000007346>)  
  

  * [Supported Payment Providers & Methods by Product Area (What Works Where)](<https://help.gohighlevel.com/en/support/solutions/articles/155000006075>)  
  

  * [Payment Links](<https://help.gohighlevel.com/en/support/solutions/articles/155000002177>)

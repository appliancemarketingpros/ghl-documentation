# How To Integrate Shopify With HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001203620-how-to-integrate-shopify-with-highlevel](https://help.gohighlevel.com/support/solutions/articles/48001203620-how-to-integrate-shopify-with-highlevel)  
**Category:** Integrations  
**Folder:** Shopify

---

Connect your Shopify store to HighLevel to bring ecommerce activity into your CRM and automation workflows. This integration helps you use Shopify data for follow-ups, abandoned checkout recovery, customer communication, and store-related automation. Proper setup ensures HighLevel can securely access the Shopify data needed for supported e-commerce features.

* * *

**TABLE OF CONTENTS**

  * What is the Shopify Integration?
  * Key Benefits of the Shopify Integration
  * Integrating Shopify with a HighLevel sub-account is a two-step process:
    * Step-1: Create a Custom App in your Shopify Store
    * Step-2: Connect Shopify to your Account
  * Frequently Asked Questions
  * Related Articles


* * *

## **What is the Shopify Integration?**

  


The Shopify integration connects an existing Shopify store to a HighLevel sub-account using a Shopify custom app and Admin API access token. This connection allows HighLevel to access supported Shopify data and events so users can build ecommerce-related workflows, use Shopify variables, and manage follow-up actions more effectively.

  


Integrating Shopify with HighLevel lets you automate marketing, sync customer data, and drive more sales. This guide shows you the integration process step by step.

* * *

## **Key Benefits of the Shopify Integration**

  


Connecting Shopify with HighLevel gives your team a stronger way to manage ecommerce follow-up and customer engagement from one place. Once connected, Shopify activity can support automation, communication, and ecommerce data workflows inside HighLevel.

  


  * **Centralized ecommerce data:** Bring supported Shopify store activity into HighLevel so customer and order-related information can be used more effectively.  
  

  * **Workflow automation:** Use Shopify-related events to trigger follow-up workflows, reminders, and customer communication.  
  

  * **Abandoned checkout recovery:** Create abandoned checkout workflows to help recover missed sales opportunities.  
  

  * **Personalized communication:** Use Shopify variables in supported emails, SMS messages, and workflow actions after Shopify triggers run.  
  

  * **Improved customer follow-up:** Help teams respond faster to ecommerce activity without manually checking Shopify for every update.


* * *

## **Integrating Shopify with a HighLevel sub-account is a two-step process:**

  


  1. Create a custom app in your Shopify store to generate the Admin API access token.
  2. Connect Shopify to your HighLevel sub-account using the token and store details.


  


### **_Step-1: Create a Custom App in your Shopify Store_**

Before we setup integration we need to create a custom app in your Shopify store.

  


1\. Log in to your **Shopify** store and click **Apps** from your Shopify dashboard.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070301923/original/OgilUaUoT855kIHogfKm3RVrwcoqDGuT3A.png?1777546940)

  


  


2\. Click **Develop apps** at the top of the screen.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070301974/original/FD7_tE9gnDaOfaE_-nYAHHCxoI6IJgdzsQ.png?1777546969)

  


  


3\. Click **Allow custom app development**.

**Note** : If custom app development is already enabled, Shopify will take you directly to the app creation screen.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303063/original/b2DKxs4ZDgV-FTDC51eJm92022ASLVLang.png?1777547454)

  


  


4\. On the next screen, click **Allow custom app development** again to confirm.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303102/original/vmrIP__bhaktG7L8o1mliZGUkJXK9H0rRQ.png?1777547484)

  


  


5\. Click on **Create an app**

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303222/original/nfo6a1B09ejyVb6zWPdUdPaC5I_MMlrj-g.png?1777547507)

  
  


6\. Enter a name for the App (for example "Marvel's App"), select your **email** under **App developer**

and click on **Create App**

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303331/original/OV794zSuy2NSY3TUEhw-jYGQqhOmnRJSdA.png?1777547572)

  
  


7\. Click **Configure Admin****API** scopes to set up the required **Admin API permissions.**

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303553/original/WNusiFXLgmKADsGDcQFTmYEUd8-kxCzeEg.png?1777547700)

  


  


8\. Search or scroll to **Orders** , then enable at least the **read_orders** permission.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303621/original/UxYW6T82jtKH2woMy5Ko6GY-KguLkt0D4g.jpeg?1777547736)

  


  


9\. Add the **read_customers** scope. In configuration edit the **Admin API Integrations**. In this section under

customers, select the**read_customers** tick box.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303740/original/FEDZK4YQCuPUfVETKI3nvT22Fxj40TxKGg.png?1777547799)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303754/original/on70vWh2aI7vQZ_hL9zIPZpR6l_F0qo8RQ.png?1777547808)

  


  


10\. Search or scroll to **Products** , then enable at least the **read_products** permission.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303857/original/ynxIh1-AMDpDkW14uVdKG-IvmrhcA1b3Sw.png?1777547852)

  


  


11\. After enabling read access for **Orders** , **Customers** , and **Products** , click **Save** in the top-right corner.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303923/original/iGpY-Q3ciZdaTjONOgdLbIpEuNu5LFXgyA.png?1777547904)

  


  


12\. After saving the app, click **Install app**.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303948/original/t_t3Ou6S3-FiOH_boNiauWFZVYcOO2Svlw.png?1777547932)

  


  


13\. In the confirmation pop-up, click **Install**.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070303992/original/44aCNQOaeqsDK60YRHWJssr9kRdBSV4dJw.png?1777547962)

  


  


14\. After the app is installed, go to the **API credentials** section and click **Reveal token once** to view the **Admin API access token** required for the Shopify integration.

**Important:** Shopify may only show this token once. Copy and store it securely before leaving the page.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070304019/original/LfehzsTl2yXkyQJ5kp3Enbp91Pvf_aufZQ.png?1777547991)

  


  


15\. Copy the **Admin API access token** by clicking the **clipboard icon**.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070304069/original/PDYyyJFUAltl1bPZzoSheYbXtrVAs-fGYA.png?1777548021)

  


  


### **_Step-2: Connect Shopify to your Account_**

  


1\. In your Sub-Account go to **Settings > Integrations** and click **Connect** under Shopify

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070304197/original/zmZoCAetnjFPKBPzNbLSJQa8Q38IDKfoDg.png?1777548083)

  


  


2\. Paste the **Admin API access token** you copied and enter "Name of your Shopify store" and click **Connect**

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070304329/original/ar5BtvTm0r2WALMJwSh5-hvf2EdbfHTaXQ.png?1777548125)

  


  


3\. Shopify is now connected to your HighLevel sub-account. You can begin using Shopify data in supported workflows, automations, and ecommerce follow-up processes.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070304428/original/o_1WDDuKDl4G4wU9Ejy4qt998LuC8S5kcQ.png?1777548170)

* * *

## **Frequently Asked Questions**

  


**Q: Does Shopify need to be connected before I can use Shopify data in automations?  
** Yes. Shopify must be connected to HighLevel before Shopify-related data can be used in supported workflows and automations. After the integration is connected, you can set up abandoned checkout workflows, follow-up messages, and other ecommerce automations separately in HighLevel.

  


**Q: What should I do if I lose the Shopify Admin API access token?**  
Shopify shows the token through the **Reveal token once** option. If the token is no longer available, return to Shopify and generate a new usable token or create a new custom app, then reconnect Shopify in HighLevel.

  


**Q: Can I use Shopify data in workflow messages?**  
Yes. Shopify variables can be used in supported workflow email, SMS, and internal notification fields when the data is available from the Shopify trigger payload.

  


**Q: Why is my Shopify connection not working?**  
Check that the **Admin API access token** was copied correctly, the **Shopify store name** is entered correctly, and the required Shopify Admin API scopes, including read access for orders, customers, and products, are enabled.

  


**Q: What Shopify permissions are needed to complete the setup?**  
Shopify custom app is required to generate the **Admin API access** token used to connect your Shopify store with HighLevel. After the token is generated, you can enter it in Settings > Integrations > Shopify to complete the connection.

* * *

## **Related Articles**

  


  * [](<https://help.gohighlevel.com/en/support/solutions/articles/48001203897>)[Automatic abandoned cart checkout emails for online store](<https://help.gohighlevel.com/en/support/solutions/articles/155000001718>)  
  

  * [Shopify Elements in HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/48001203897>)  
  
[](<https://help.gohighlevel.com/en/support/solutions/articles/48001203898>)
  * [How To Use Shopify Variables](<https://help.gohighlevel.com/en/support/solutions/articles/48001203898>)  
  

  * [How to migrate Shopify stores to HighLevel](<https://help.gohighlevel.com/en/support/solutions/articles/155000004056>)

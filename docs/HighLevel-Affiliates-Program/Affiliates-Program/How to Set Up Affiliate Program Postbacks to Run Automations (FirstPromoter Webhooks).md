# How to Set Up Affiliate Program Postbacks to Run Automations (FirstPromoter Webhooks)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001163126-how-to-set-up-affiliate-program-postbacks-to-run-automations-firstpromoter-webhooks-](https://help.gohighlevel.com/support/solutions/articles/48001163126-how-to-set-up-affiliate-program-postbacks-to-run-automations-firstpromoter-webhooks-)  
**Category:** HighLevel Affiliates Program  
**Folder:** Affiliates Program

---

In this article, we will cover how to set up postbacks (webhooks) for your affiliate links so that you can run automation off sales when someone signs up using your affiliate link.

  


  


**NOTE:**
    
    
    This Article is for the _[HighLevel Affiliate Program](<https://help.gohighlevel.com/support/solutions/folders/48000666024>),_ **NOT** [Affiliate Manager Feature](<https://help.gohighlevel.com/en/support/solutions/articles/48001223169>) found in your sub-accounts.

  

    
    
    **Update**
    You can now opt-in to receive email notifications for referral activity in the portal.
    
    To do so...
    - Click your profile name in the top-right of the Affiliate Dashboard.
    - Open Notification Settings.
    - Turn notifications on and customize
    [](<https://youtu.be/lTrGOaAz_kg>)[](<https://youtu.be/lTrGOaAz_kg>)
    
    **By default, these notifications may be turned off, so it's worth checking this setting.**
    
    Turning notifications on is highly recommended. It’s the easiest way to stay informed without needing to check your portal every time something changes.
    

  


  


  


  


  


* * *

## **Step-by-step guide on setting up affiliate program postbacks (webhooks).**

# **You'll need a few things to get started:**

  * Download [The Core Postback Snapshot](<https://affiliates.gohighlevel.com/?fp_ref=ghl-main&share=t0dvleIVwCNE53PqKgaU>) \- this provides the templates for you to follow this tutorial step-by-step in order to set up postbacks.
  * Open your [Affiliate Dashboard](<https://help.gohighlevel.com/support/solutions/articles/48001202637-how-to-use-affiliate-portal>)


**  
  
**

### **1\. Initial Setup & Navigation**

  * Open your agency account
  * Go to a sub-account specific for affiliates or one that is dedicated and will not trigger other campaigns or flows.
  * Click on the **[Affiliate Portal](<https://help.gohighlevel.com/support/solutions/articles/48001202637-how-to-use-affiliate-portal>)** tab.
  * Click on **Promoter Reports**
  * Scroll down to **Postbacks** and click it

  


### **2\. Workflows**

  


**For each Postback, you will need a corresponding Workflow that starts with an[Inbound Webhook](<https://help.gohighlevel.com/support/solutions/articles/48001237383-how-to-use-the-inbound-webhook-workflow-premium-trigger>) trigger.**

  


That means for every workflow, you'll need to...

  1. Create the postback
  2. Send a test postback
  3. Fetch the sample request inside the workflow
  4. Save the mapping reference
  5. Save and publish the workflow


  


Without a sample payload, the workflow trigger will not save correctly.

  
  


WorkFlow | Postback name| Campaign| Trigger Name| Referral State| Purpose  
---|---|---|---|---|---  
1 - Lead HighLevel| 1- Lead (Step 1)| HighLevel Affiliate Program| Lead Subscribed| Subscribed| Captures the Lead that Fills out step 1 of checkout form  
2 - Trial Postback HighLevel| 2 - On Trial (Step 2)| HighLevel Affiliate Program| New Referral| Signup | Captures when a customer completes checkout and start a trial  
3 - HighLevel Customer| 3 - HighLevel Customer| HighLevel Affiliate Program| New Customer| Lead Becomes Referral | Captures when a customer makes a charge in-app (Might not be a commissionable)  
4 - Paying Affiliate Commission| 4 - Paying Affiliated Customer| HighLevel Affiliate Program| New Commission| Reward Created| Captures when a trial ends or when the customer makes a commissionable payment  
5 - Cancelled Customers| 5 - Cancellation| HighLevel Affiliate Program| Lead Cancelled| Lead Cancelled| Captures when a customer cancellation is triggered and subscription ends  
  
**  
**

  


  


**The 5 Core Postbacks**

  


Following along with the table above, you will set up five postbacks to correspond with the five workflows included in [The Core Postback Snapshot](<https://affiliates.gohighlevel.com/?fp_ref=ghl-main&share=t0dvleIVwCNE53PqKgaU>)

  1. Lead Subscribed
  2. New Referral (Trial Started)
  3. First Payment Customer
  4. New Commission
  5. Cancelled Customer


  


  

    
    
    ## Step 1: Lead Subscribed Postback
    
     
    
    This triggers when someone completes the first step of the affiliate signup form but has not started a trial yet.
    
     
    
    ### Create the Postback
    
     
    
    Inside Postbacks:
      
        * Click **Create Postback**
        *  Name: 1 - Lead Subscribed
        * Campaign: HighLevel Affiliate Program
        * Trigger: Lead Subscribed
    
     
    
    ### Connect the Workflow
    
     
      
        1. Open the corresponding workflow
        2. Copy the **Webhook URL**
        3.  Paste it into the Postback URL field
    
     
    
    ### Send Test Data
    
     
      
        1. Click **Test Postback**
        2.  Go back to the workflow trigger
        3. Click **Fetch Sample Request**
        4.  Save the mapping reference
        5. Save the trigger
        6. Save the workflow
    
     
    
    * * *
    
     
    
    ## Step 2: Trial Signup / New Referral
    
     
    
    This triggers when someone starts a trial.
    
     
    
    ### Create the Postback
    
     
      
        * Name: 2 - Trial Signup
        * Campaign: HighLevel Affiliate Program
        * Trigger: New Referral
    
     
    
    ### Connect the Workflow
    
     
    
    Paste the second workflow webhook URL into the Postback URL field.
    
     
    
    ### Finish Setup
    
     
      
        * Click **Test Postback**
        *  Fetch the sample request
        * Save the mapping reference
        * Save the workflow
    
     
    
    * * *
    
     
    
    ## Step 3: First Payment Customer
    
     
    
    This triggers the first time a user becomes a paying customer.
    
     
    
    This can happen when:
    
     
      
        * A trial user makes an in-app payment
        * A trial converts into a paid customer
    
     
    
    >  
>     
>     **Important:** This trigger only fires once per customer.
>     
>      
    
     
    
    ### Create the Postback
    
     
      
        * Name: 3 - First Payment Customer
        * Campaign: HighLevel Affiliate Program
        * Trigger: New Customer
    
     
    
    ### Connect the Workflow
    
     
    
    Paste the webhook URL from the third workflow.
    
     
    
    ### Finish Setup
    
     
      
        * Click **Test Postback**
        *  Fetch the sample request
        * Save the mapping reference
        * Save the workflow
    
     
    
    * * *
    
     
    
    ## Step 4: New Commission
    
     
    
    This triggers every time a commission is generated.
    
     
    
    Unlike the previous trigger, this can happen multiple times for the same customer.
    
     
    
    ### Create the Postback
    
     
      
        * Name: 4 - New Commission
        * Campaign: HighLevel Affiliate Program
        * Trigger: New Commission
    
     
    
    ### Connect the Workflow
    
     
    
    Paste the webhook URL from the fourth workflow.
    
     
    
    ### Finish Setup
    
     
      
        * Click **Test Postback**
        *  Fetch the sample request
        * Save the mapping reference
        * Save the workflow
    
     
    
    >  
>     
>     **Tip:** If you do not want contacts repeatedly re-entering workflows every time a commission occurs, disable workflow re-entry or use tagging logic instead.
>     
>      
    
     
    
    * * *
    
     
    
    ## Step 5: Cancelled Customer
    
     
    
    This triggers when a customer account is cancelled.
    
     
    
    ### Important
    
     
    
    The cancellation postback fires when the account actually closes, not when the cancellation request is submitted.
    
     
    
    Examples:
    
     
      
        * Trial users remain active until the trial ends
        * Paid users remain active until the billing cycle finishes
    
     
    
    ### Create the Postback
    
     
      
        * Name: 5 - Cancelled Customer
        * Campaign: HighLevel Affiliate Program
        * Trigger: Lead Cancelled
    
     
    
    ### Connect the Workflow
    
     
    
    Paste the webhook URL from the fifth workflow.
    
     
    
    ### Finish Setup
    
     
      
        * Click **Test Postback**
        *  Fetch the sample request
        * Save the mapping reference
        * Save the workflow
    
     
    
    * * *
    
     
    
    ## Publish Your Workflows
    
     
    
    After all five workflows are configured:
    
     
      
        1. Open each workflow
        2. Click **Publish**
        3.  Click **Save**
    
     
    
    If workflows are not published, postbacks will not trigger.

##   


  


  


  


**  
**

## **Adding a SubID**

# **Understanding and Setting Up Sub IDs**

Sub IDs are crucial for tracking the origin of your leads, sources, or trials. They help you pinpoint exactly where your traffic is coming from.

  

    
    
    Recommendation: Since creating a unique link for every piece of content is tedious, it is recommended to create one Sub ID to use for the entire platform (e.g., Instagram) to track its overall performance.

  


  


### **  
**

###   


  


  


  


##   


  


  


## **Email Notification Settings**

  


**You can enable automated email notifications from FirstPromoter.****These emails help you track new leads and payments directly through your inbox.**

  
[](<https://youtu.be/lTrGOaAz_kg>)[](<https://youtu.be/lTrGOaAz_kg>)

  


**  
**

  


**  
**

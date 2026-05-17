# Workflow Trigger - Messaging Error Code - SMS

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003201-workflow-trigger-messaging-error-code-sms](https://help.gohighlevel.com/support/solutions/articles/155000003201-workflow-trigger-messaging-error-code-sms)  
**Category:** Workflows  
**Folder:** Workflow Triggers

---

**TABLE OF CONTENTS**

  * Overview
  * Trigger Name
  * Trigger Description
  * How to Configure
  * Example


* * *

## **Overview**

The "Messaging Error - SMS" trigger allows you to initiate workflows automatically whenever a SMS has resulted in undelivered state and returned one of the below-mentioned error code.

##   


## **Trigger Name**

Messaging Error - SMS

##   


## **Trigger Description**

This trigger activates a WorkFlow based on the error received for an undelivered message. This can be used for taking relevant measures to clean the contact list eventually improving the delivery rate.

##   


## **How to Configure**

  1. **Choose a Workflow Trigger:**

     * **Select " Messaging Error - SMS" from the dropdown list.**
  2. **Workflow Trigger Name:**

     * **Provide a descriptive name for the trigger to identify it within your workflow easily.**
  3. **Filters:**

     * **You can add filters to narrow down the trigger to specific error codes mentioned below:**  
  


Code| Description  
---|---  
30007| Carrier Violation  
30034| A2P Registration Pending on Number|   
  
30032| Toll Free Number not Verified  
30005| User Inactive/Number does not exist  
30003| Unreachable/Out of Service Number  
30004| Do not want SMS/DND enabled  
30006| Landline/Incapable to receive SMS  
30023| US A2P 10DLC - Daily Message Cap Reached  
21408| Permission to Send SMS Not Enabled for Region  
30008| Unknown Error  
21606| Invalid 'From' Phone Number  
21211| Invalid 'To' Phone Number  
21614| To' Number Is Not a Valid Mobile Number  
21610| User Replied with STOP (Opted Out)  
30011| MMS Not Supported by Recipient Number or Region  
30033| A2P Campaign Suspended or Deleted  
21661| From' Number Is Not SMS-Capable  
21635| To' Number Cannot Be a Landline  
30037| Outbound Messaging Disabled  
30002| Sub-Account Suspended  
  
##   


## **Example**

**Let’s say you are running an SMS campaign to promote a new product, and you want to automatically remove contacts who have a high chance on not getting the messages next time or want to add a tag to re trigger them an SMS after sometime.some time**

  1. **Choose a Workflow Trigger:**

     * **Trigger: Messaging Error - SMS**
  2. **Workflow Trigger Name:**

     * **Name: Messaging Error - SMS**
  3. **Filters:**

     * **Filter Type: Error Code is**
     * **Error Name: 30007 - Carrier Violation**  
**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033086504/original/iv8aR4ZsYOgRmu7gfYc1HJCccorQpor0dQ.jpeg?1726659711)**
  4. **Further, this can be created into if else if different actions is needed as shown below:**  
****![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155033086528/original/vGMb8HREi0nL0poEZYc-KF4Qw_uRJHKyBQ.jpeg?1726659731)****

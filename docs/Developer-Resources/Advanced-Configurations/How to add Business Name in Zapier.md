# How to add Business Name in Zapier

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001164926-how-to-add-business-name-in-zapier](https://help.gohighlevel.com/support/solutions/articles/48001164926-how-to-add-business-name-in-zapier)  
**Category:** Developer Resources  
**Folder:** Advanced Configurations

---

choose webhooks Custom Request

select Post

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48069683091/original/JTw7jqk3Y9e2Ngofa-JyVSXXNJ47SgEbKg.png?1605054675)

<https://api.gohighlevel.com/zapier/contact/add_update>

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48069683093/original/1p6htLF_7L_Oc1qLo16DVu18cnZcDGVChA.png?1605054675)

  


  


AUTHORIZATION Bearer YouRlocationAPIKEYHERE

Content-Type application/json

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48069683092/original/im6CubDaMZN_nQ2bZqOSaRBW50_kbasM6w.png?1605054675)

  


Here is the data (fillin the info from the previous steps of the zap)

  


{  
"first_name": "zap",  
"last_name": "Zaptest3",  
"name": "D Zaptest",  
"email": "dzap@zap.com",  
"phone": "9516403455",  
"address1": "123 My St.",  
"city": "Meridian",  
"country": "US",  
"state": "Idaho",  
"postalCode": "83646",  
"companyName": "RoboCoach",  
"contact_type": "customer"  
}

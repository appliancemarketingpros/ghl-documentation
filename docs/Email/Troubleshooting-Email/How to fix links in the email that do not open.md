# How to fix links in the email that do not open?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001151622-how-to-fix-links-in-the-email-that-do-not-open-](https://help.gohighlevel.com/support/solutions/articles/48001151622-how-to-fix-links-in-the-email-that-do-not-open-)  
**Category:** Email  
**Folder:** Troubleshooting Email

---

If links in your emails are not opening, it’s usually caused by an issue with your tracking domain or DNS configuration. This article walks you through why this happens and provides steps to troubleshoot and fix the issue.

  


  


  

    
    
    **Note:** This video example uses Mailgun, but the same principles apply to all providers.

* * *

**TABLE OF CONTENTS**

  * What Causes Email Links to Not Open?
    * How Email Link Redirects Work
    * How To Fix Links in Emails That Do Not Open
    * Troubleshooting Common Issues
    * Related Articles


* * *

# **What Causes Email Links to Not Open?**

  


Email links usually don’t open because the **tracking domain isn’t set up correctly** or isn’t resolving in DNS.

  


When an email is sent, the link is rewritten so it passes through a tracking domain before sending users to the final page. If that tracking domain has a DNS or SSL issue, the redirect breaks and the link won’t open.

  


To fix this, make sure your tracking domain is configured properly. This means the correct CNAME record is in place, the domain resolves in DNS and the HTTPS/SSL is active. Once these are set correctly, the redirect works again and your links will open normally.

  

    
    
    **Note:** Link tracking (redirecting links through a tracking domain) is used by most email providers to enable click tracking and ensure proper link routing. However, **[Email Tracking](<https://help.gohighlevel.com/en/support/solutions/articles/155000003213>)**(such as open and click reporting inside HighLevel) are only available when using LC Email.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070162151/original/K15npCUzv1qi8NIKobiSJza24O7kCZaQaA.png?1777399256)

* * *

## **How Email Link Redirects Work**

  


Understanding how links behave behind the scenes makes it easier to diagnose why they fail.  
  


  1. Your original link is replaced with a tracking link.  
  


  2. The tracking link routes through a subdomain (e.g., email.yourdomain.com).  
  


  3. This subdomain relies on a **CNAME record** in your DNS.  
  


  4. If the DNS or SSL is misconfigured, the redirect fails and the link may not open.


* * *

## **How To Fix Links in Emails That Do Not Open**

  


####  _**Step 1:** Identify Your Tracking Domain_

  


  * From your Agency Dashboard, go to**Settings** >**Email Services** > **Location Settings**.  
  

  * Find the domain used for email tracking (e.g., email.yourdomain.com) for the location you would like to troubleshoot.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070163225/original/dBsHWHN98kdOUSD_rBfWPAvHnlo6zpbIGg.png?1777400124)

  


  


#### _**Step 2:** Check Your CNAME Record_

  


Go to [MX toolbox](<https://mxtoolbox.com/CnameLookup.aspx>) or [Whatsmydns](<https://www.whatsmydns.net/>) to look up the CNAME record. Enter your tracking lookup domain as defined below

  


  1. Copy your tracking domain found in step 1 (e.g., mg.yourdomain.com)  
  

  2. Add email. in front → [](<//email.mg.yourdomain.com>)_email.mg.yourdomain.com_[](<//email.mg.yourdomain.com>)  
  
**For example:**  
  
If you set up _mg.companyname.com_ , you will look up the CNAME record for email.mg.companyname.com  
  
If you set up _replies.companyname.com_ , you will look up the CNAME record for email.replies.companyname.com[](<//replies.companyname.com>)**[](<//replies.companyname.com>)****[](<//replies.companyname.com>)****[](<//replies.companyname.com>)****[](<//replies.companyname.com>)****[](<//replies.companyname.com>)**  
  
If you set up _support.companyname.com, y_ ou will look up the cname record for _email.support.companyname.com_

  


The result should return a valid CNAME record. If you see **"DNS record not found"** , your CNAME is missing or incorrect.  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070243288/original/lvHcfFvJJgGbWq7VDpBDC_OV4l3Os5cNcA.png?1777480548)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070244734/original/CRtpx0qOclPZf4bzq6WDfJRHbxBkXP4PTg.png?1777481515)

  


  


#### _**Step 3:** Check Your CNAME Record_

  


Log in to your DNS provider and Locate the CNAME record for your tracking domain. Ensure:  
  


  * Host is only the subdomain (e.g., email.mg, not full domain)  
  

  * Value points to your provider’s tracking domain


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070247826/original/VPNK5vb32wmqp5BoP-7oNByINEQrRKImNQ.png?1777484783)

  


  


####  _**Step 4:** Ensure HTTPS is Enabled_

  


Tracking domains must support HTTPS. Go to your provider settings and ensure the tracking protocol is set to HTTPS. Wait for SSL provisioning if recently updated.  
  


[](<https://help.mailgun.com/hc/en-us/articles/360011566033-How-to-Enable-HTTPS-Tracking-Links>)[](<https://help.mailgun.com/hc/en-us/articles/360011566033-How-to-Enable-HTTPS-Tracking-Links>)[Click here for more information on How to Enable HTTPS Tracking Links](<https://help.mailgun.com/hc/en-us/articles/360011566033-How-to-Enable-HTTPS-Tracking-Links>)[](<https://help.mailgun.com/hc/en-us/articles/360011566033-How-to-Enable-HTTPS-Tracking-Links>)[](<https://help.mailgun.com/hc/en-us/articles/360011566033-How-to-Enable-HTTPS-Tracking-Links>)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070244057/original/9J_4NYHimCj5o882fj48_Kwu5hTXhTeERA.png?1777481018)

  


  


####  _**Step 5:** Test Your Links_

  


Send a test email from HighLevel. Click the link and confirm it redirects properly to the final URL.

  


_  
_

#### _**Step****6:** Contact Support if the Issue Persists_

  


If your links still do not open, contact your **domain/DNS provider** (e.g., GoDaddy, Cloudflare, Google Domains).  
  


  * Ask them to verify that your **CNAME record for the tracking domain is correctly set up and resolving**.  
  

  * Share screenshots of your DNS records as shown below for faster troubleshooting.


  


If your DNS provider confirms everything is correct and the issue continues, **[](<https://help.gohighlevel.com/en/support/solutions/articles/48001204857>)**[](<https://help.gohighlevel.com/en/support/solutions/articles/48001204857>)[Contact HighLevel Customer Support](<https://help.gohighlevel.com/en/support/solutions/articles/155000000969>)[](<https://help.gohighlevel.com/en/support/solutions/articles/48001204857>)**[](<https://help.gohighlevel.com/en/support/solutions/articles/48001204857>)**.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155070244555/original/SFX68oZGxh9oG7a6deTu8uvYoUBRbkC0lA.png?1777481329)

* * *

## **Troubleshooting Common Issues**

  


Even after following the setup steps, some configurations can still cause links to fail. Reviewing these common issues can help you quickly identify what might still be wrong.

  


  * **CNAME record not found** : If MXToolbox shows “DNS record not found,” the tracking domain CNAME is missing. Re-add the record in your DNS provider  
  

  * **Wrong CNAME value** : The CNAME must point to your email provider’s tracking host. If it points elsewhere, links will not redirect properly.  
  

  * **Using the full domain in the Host field** : In most DNS providers (like GoDaddy or Namecheap), you should only enter the subdomain (e.g., email or email.mg), not the full domain like _email.yourdomain.com_.  
  


Correct host name format (common setups):

    * If your subdomain is _mg.companyname.com_ → Host should be _email.mg_
    * If your subdomain is _replies.companyname.com_ → Host should be _email.replies_
    * If your subdomain is _support.companyname.com_ → Host should be _email.support_  
  

  * **Cloudflare proxy enabled** : If you’re using Cloudflare, the record must be set to DNS Only (No Proxy).  
  

  * **HTTPS not enabled** : Some providers require HTTPS tracking to be enabled in their settings. If HTTP is used or SSL is not active, links may fail to open.  
  

  * **DNS not fully propagated** : After making changes, it can take up to 24–48 hours for DNS updates to apply globally.


* * *

## **Related Articles**

  


  * [Email Tracking for LC Email](<https://help.gohighlevel.com/en/support/solutions/articles/155000003213>)  
  

  * [Google Dedicated Sending Domain Setup (LC Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001240481>)  
  

  * [How to Add a Domain and Verify DNS Record](<https://help.gohighlevel.com/en/support/solutions/articles/155000002220>)  
  

  * [Connecting Your Domain on GHL - A Guide](<https://help.gohighlevel.com/en/support/solutions/articles/155000005132>)

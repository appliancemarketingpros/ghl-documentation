# How to Migrate a WordPress Site to HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005010-how-to-migrate-a-wordpress-site-to-highlevel](https://help.gohighlevel.com/support/solutions/articles/155000005010-how-to-migrate-a-wordpress-site-to-highlevel)  
**Category:** Sites  
**Folder:** Wordpress

---

Migrate an existing WordPress site to HighLevel using the LC Migrator Plugin or White-Glove Migration Assistance. A WordPress site can be migrated with little to no downtime when done correctly. This guide explains how to prepare the site, complete the migration, test the migrated version, and go live with reduced downtime.

* * *

**TABLE OF CONTENTS**

  * What is Migrating a WordPress Website to HighLevel?
  * Key Benefits of Migrating WordPress Websites to HighLevel
  * WordPress Migration Options in HighLevel
  * Traditional Migration vs HighLevel Migration
  * Before You Migrate: Pre-Migration Checklist
  * How to Avoid Downtime During Migration
  * How To Migrate a WordPress Site Using the LC Migrator Plugin
  * How To Request White-Glove Migration Assistance
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is Migrating a WordPress Website to HighLevel?**

  


WordPress migration in HighLevel moves an existing WordPress website from another host into HighLevel WordPress hosting. The migration transfers site content, design, media, themes, plugins, and database information so the website can run from HighLevel.

  


HighLevel supports two migration options:

  


  * **LC Migrator Plugin:** A guided plugin-based migration from your existing WordPress site into HighLevel.  
  


  * **White-Glove Migration Assistance:** An agency-only option where the HighLevel team assists with the migration process.


  


![](https://jumpshare.com/share/OXNVVEI4fMhNUyvxypLC+/Screen+Shot+2026-05-26+at+18.20.01.png)

* * *

## **Key Benefits of Migrating WordPress Websites to HighLevel**

  


  * **Centralized WordPress hosting:** Manage WordPress websites inside HighLevel instead of using a separate hosting provider.  
  


  * **Guided migration options:** Use the LC Migrator Plugin or request White-Glove Migration Assistance if you are an agency user.  
  


  * **Reduced downtime risk:** Prepare DNS, test the migrated site, verify SSL, and keep old hosting active during propagation.  
  


  * **Agency-friendly workflow:** Agencies can migrate client sites and request assistance from the WordPress migration area.  
  


  * **Post-migration visibility:** Review domain status, SSL status, and uptime tools after launch.


* * *

## **WordPress Migration Options in HighLevel**

  


Choose the migration option based on your access level and how much assistance you need. The LC Migrator Plugin is best for users who have WordPress admin access to the current site, while White-Glove Migration Assistance is available for agencies that want help with the migration.

  

    
    
    **Important:** White-Glove Migration Assistance is **available to agency users only**. Sub-account users will only see the LC Migrator Plugin option.

  


Migration Method| Best For| Required Access| Technical Level| Availability| Notes  
---|---|---|---|---|---  
LC Migrator Plugin| Moving a live WordPress site from another host into HighLevel| WordPress admin access on the source site| Beginner to intermediate| Agency and sub-account users| Recommended for most standard migrations.  
White-Glove Migration Assistance| Agencies that want migration help from HighLevel| Agency access and migration request details| Beginner| Agency users only| Sub-account users do not see this option.  
Clone Existing HighLevel WordPress Site| Duplicating a WordPress site already hosted in HighLevel| Existing HighLevel-hosted WordPress site| Beginner to intermediate| Based on account permissions| Cloning is different from migrating a site from an external host.  
  
* * *

## **Traditional Migration vs HighLevel Migration**

  


Traditional WordPress migration often requires separate tools for file transfer, database export, DNS updates, SSL setup, and hosting support. HighLevel migration keeps the migration workflow closer to the hosting environment, which helps agencies move client sites with fewer disconnected steps.

  


**Area**| **Traditional WordPress Migration**| **HighLevel WordPress Migration**  
---|---|---  
Migration workflow| Often handled across multiple hosting, backup, and database tools| Managed through HighLevel migration options  
Technical effort| May require manual file and database handling| Uses the LC Migrator Plugin or agency migration assistance  
Agency support| Depends on the external hosting provider| White-Glove Migration Assistance is available for agency users  
Go-live process| DNS and SSL are usually managed separately| Domain, DNS, and SSL setup are handled from HighLevel site settings  
Post-launch review| Requires separate monitoring or hosting tools| Site status, SSL, and uptime tools are available in HighLevel  
  
* * *

## **Before You Migrate: Pre-Migration Checklist**

  


Preparing access, backups, DNS settings, and the destination site before migration helps reduce downtime and gives you a safer rollback path if anything needs to be corrected.

  

    
    
    **Tip:** Keep the original website live while the migrated version is prepared and tested.

  


Before starting the migration, complete the following checklist:

  


  * Confirm you have access to the current WordPress admin dashboard.  
  


  * Confirm you have access to the domain or DNS provider.  
  


  * Create or confirm a recent backup of the current website.  
  


  * Create the destination WordPress site in HighLevel.  
  


  * Confirm the correct server location was selected for the destination site.  
  


  * Review active plugins and themes for known compatibility issues.  
  


  * Pause major content, design, plugin, or theme changes during the migration window.  
  


  * Lower your DNS TTL before migration where your DNS provider allows it. Use the lowest practical value supported by your provider or follow the TTL guidance shown during HighLevel domain setup.  
  


  * Keep the original hosting account active until after migration, testing, and DNS propagation.  
  


  * Confirm whether you are migrating from an external WordPress host or cloning a site already hosted in HighLevel.


* * *

## **How to Avoid Downtime During Migration**

  


Downtime is usually caused by DNS timing, untested site changes, SSL issues, or cancelling old hosting too early. Follow these steps before and after migration to keep the original site available while the migrated version is prepared.

  


  1. **Lower DNS TTL Before Migration**  
  


TTL (Time To Live) controls how quickly DNS changes update globally. Set TTL to **300 seconds (5 minutes)** at least **24 hours before migration** where your DNS provider allows it.  
  


  2. **Always Use a Staging Environment**  
  


Never migrate directly to a live website without testing. Use the migrated HighLevel site as the staging environment before switching DNS.  
  


Verify:  
  


     * Website functionality

     * Plugin compatibility

     * Design consistency

     * Mobile responsiveness  
  


  3. **Keep the Old Website Active Temporarily**  
  


Do not cancel your old hosting immediately. Keep it active for **24–48 hours after DNS changes** so visitors can still access the site while DNS propagation completes.  
  


  4. **Verify SSL Certificates**  
  


Confirm HTTPS works correctly after migration. Without SSL, browsers may show security warnings and SEO performance may suffer.


* * *

## **How To Migrate a WordPress Site Using the LC Migrator Plugin**

  


The LC Migrator Plugin moves a WordPress site from another hosting provider into HighLevel. Use this option when you have access to the existing WordPress admin dashboard.

  


  1. Click on **Sites > WordPress**.  
  


  2. Click on **Activate WordPress** if you don't have WordPress hosting activated yet.  
  
![](https://jumpshare.com/share/lDa08LO4lXrRMdOOFI7n+/7CrG8ZYicNN2JMiyRGD0fqbkznnGAsAsug.png)  
  

  3. Select From **blank** , click **Create** , fill out your site's details, and finally hit **Create WordPress site**.  
  
![](https://jumpshare.com/share/kokO2FY2ehCDYeRBu7gy+/GIF+Recording+2026-05-26+at+19.02.59.gif)  
  

  4. Under your Wordpress site > **Info** > **Import Your Existing Website** , select the One-click migration using **LeadConnector Migrator Plugin**.  


  5. Click on **Download Plugin** and make sure the zip is downloaded.   
  
![](https://jumpshare.com/share/XPA4mlo3OwtK97EkJzNz+/Screen+Shot+2026-05-26+at+19.04.57+%281%29.png)  
  


  6. Go to the **Wordpress Admin**.   
  
![](https://jumpshare.com/share/m1qDyR3Dpa7klObmanQz+/Screen+Shot+2026-05-26+at+19.09.28.png)  
  

  7. Go to your **Plugins** > **Add Plugin > Upload Plugin** and upload the zip file.  
  


  8. After uploading, click on **Install** **Plugin**.  
  
![](https://jumpshare.com/share/Om9EtOqf0HNZY2PSRkYS+/GIF+Recording+2026-05-26+at+19.12.03.gif)  
  


  9. Once the installation is done, click on **Activate Plugin**.  
  
![](https://jumpshare.com/share/3uFZ3fy16hiSlRFyPC2w+/Screen+Shot+2026-05-26+at+19.14.38.png)  
  


  10. Click on **Leadconnector** and **sign in** to your LeadConnector/HighLevel account.  
  
![](https://jumpshare.com/share/kHq5m0w7Okm2qOBhOo5q+/Screen+Shot+2026-05-26+at+19.17.02.png)  
  


  11. **Choose** the **website** you **wish** to **migrate** from the provided dropdown list.  
  
![](https://jumpshare.com/share/Qq0DbtprnXfBaxKsl1GA+/-1Fih9nLBXb3KwwxsgpgwZ5pE78f-Jk5AQ.png)  
  


  12. Click the **Start Migration** button. You'll see clear progress updates. Relax as the migration proceeds in the background.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072229822/original/VkpOkm9qEd-Z8OutKkEAY8HceMIfBJAmPQ.jpeg?1779803588)  
  


  13. Once the migration finishes, click **View Your New Website** to explore your freshly migrated site. Optionally, rate your experience to help us improve!  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155072229860/original/egXwEHbRo2nJ5fpZP-a4zOlLc_dgjR0-Fg.jpeg?1779803602)


* * *

## **How To Request White-Glove Migration Assistance**

  


White-Glove Migration Assistance lets agency users request help from HighLevel for a WordPress migration. Use this option when you prefer assisted migration or are managing a client site that needs extra support.

  


  

    
    
    **Note:** White-Glove Migration Assistance is **available to agency users only**. Sub-account users will not see this option.

  


  1. Go to your Wordpress site management > **Info** > **Import Your Existing Website**.  

  2. Click on the **Request Help** button under **White-Glove Migration Assistance**.  
  
![](https://jumpshare.com/share/1l6GUCr9K1QHvJtgj1d7+/Screen+Shot+2026-05-26+at+19.33.44.png)  
  


  3. **Complete** the **migration** **request** **form** with the required site and access details.  
  


  4. Review the information for accuracy.  
  
![](https://jumpshare.com/share/VLtgII3Qq8Ola3VCLZKQ+/GIF+Recording+2026-05-26+at+19.37.13.gif)  
  

  5. **Submit** the request and follow the provided instructions.  
  

  6. Keep the original site and hosting active until the migration has been completed, tested, and launched.  
  
![](https://jumpshare.com/share/TZnaSPOvQ9o325hRXRQD+/Screen+Shot+2026-05-26+at+19.37.53.png)


* * *

## **Frequently Asked Questions**

  


**Q: Will my site go offline during migration?**  
The original site should remain live while you migrate and test the new version. Downtime risk is usually highest during DNS changes, so prepare DNS ahead of time, test before launch, and keep old hosting active temporarily.

  


**Q: Why do I not see White-Glove Migration Assistance?**  
White-Glove Migration Assistance is available to agency users only. Sub-account users may only see the LC Migrator Plugin option.

  


**Q: What should I do if DNS is still pointing to my old host?**  
Confirm the correct DNS records were added at your DNS provider and allow time for propagation. If your provider supports Domain Connect, use it to reduce manual setup errors.

  


**Q: What should I do if SSL is pending or the site shows a browser warning?**  
Confirm DNS has verified successfully and that the correct domain is connected to the WordPress site. SSL can only issue correctly after the required DNS records are in place and verified.

  


**Q: Why are images or media files missing after migration?**

Missing media may be caused by an incomplete migration, blocked file paths, plugin issues, or references that still point to the old environment. Review the media library, page content, and plugin settings after migration.

  


**Q: What should I do if plugins break after migration?**

Review the migrated site for plugin conflicts and use the WordPress Plugin Troubleshooter if needed. Some plugins may require reactivation, updated settings, or compatibility checks after migration.

  


**Q: Can I edit the original website while migration is running?**  
Avoid major edits during the migration window. Changes made to the original site after migration starts may not appear on the migrated version unless they are migrated again or manually recreated.

* * *

### **Related Articles**

  


  * [WordPress - How to Add Domains to Sites ](<https://help.gohighlevel.com/en/support/solutions/articles/155000002547>)  
  


  * [How to Get Customer Support for WordPress Issues](<https://help.gohighlevel.com/en/support/solutions/articles/155000006934>)  
  


  * [Understanding the Migration View: What You See vs. What Sub-Accounts See ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004997>)  
  


  * [Setup Guide for WordPress Hosting ](<https://help.gohighlevel.com/en/support/solutions/articles/155000006777>)  
  


  * [Cloning Wordpress Websites in HighLevel ](<https://help.gohighlevel.com/en/support/solutions/articles/155000004189>)  
  


  * [How to Use the WordPress Plugin Troubleshooter](<https://help.gohighlevel.com/en/support/solutions/articles/155000006064>)

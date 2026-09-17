# How to Set Up WordPress Hosting for Clients

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001199648-how-to-set-up-wordpress-hosting-for-clients](https://help.gohighlevel.com/support/solutions/articles/48001199648-how-to-set-up-wordpress-hosting-for-clients)  
**Category:** Sites  
**Folder:** Wordpress

---

# 

HighLevel WordPress Hosting lets agencies create, migrate, and manage WordPress websites for client sub-accounts directly inside HighLevel.

  


This article explains how to create a WordPress site, give the appropriate users access, manage domains, backups, and advanced settings, and understand which features are available to agency users versus client users.

* * *

LeadConnector plugin (auto-installed on new hosted sites)

If your WordPress site is newly provisioned via HighLevel Hosting, HighLevel automatically installs the LeadConnector (LC) plugin during setup.

Use the Plugin Status indicator in your HighLevel WordPress dashboard to confirm whether the plugin is Connected or Disconnected.

### Setting up a new WordPress Site

  1. To set up your WordPress site, you need to have purchased the WordPress hosting feature under the Sites tab. Once this has been done, you can get started by clicking the "+ Create Site" button.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587928/original/5Dc4BJsxtu_DvAlMygRPzMuPN4sLu-EkxQ.png?1783584600)  
  


  2. Choose if you wish to create a site from scratch, using a template, or clone an existing site  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587930/original/eSUQEFHq52gbTLuSCTOJSE4Z-oqsjejI_g.png?1783584600)  
  


  3. Fill in the Site and User details.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587926/original/vEsIn1DAW6-DYhUrwUGYeTvVL46G97xbzA.png?1783584600)


Wait for 2-5 minutes till the installation is complete.

  4. After the installation is complete, you will have access to the WordPress dashboard, user management, backup & restore, and some additional settings.  
  
  


### The WordPress Dashboard

Here you can access your site and admin portal, as well as manage your Additional Domains & Primary Domain.

Moving an existing site? Import an existing WordPress site seamlessly using our proprietary LC Migrator plugin, or take advantage of our free white-glove migration assistance.

You can also effortlessly Refresh Cache for the WordPress Site directly from this dashboard.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587932/original/nlEHid7iuHVt02AiKjuC-BltphjqAOSigg.png?1783584601)

### User Management

Here you can manage all users for the site.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587925/original/-SB9KXnAOwAL5pslun_fZC8vBlsX_EZS1Q.png?1783584600)

### Backup & Restore

Here you will see the backups for the last 30 days. Backups happen daily at 05:00 AM CST.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587934/original/-P52sspFbXASQA4_baupzvycSDlCE_1LkA.png?1783584601)

You can also initiate manual backups as needed as shown in the video below:

More Tutorials from the Community:

  * https://youtu.be/zvfav4EXnE4

  * https://youtu.be/7z9A0d4Ml4c

  * https://youtu.be/ROQLp8_D8Vc


### Advanced Settings

  1. You can manage FTP Access and Communication Settings here.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587927/original/w-ymw15A09GbO1WRRD-HsnKmM3bw36xV6w.png?1783584600)  
  


  2. Cache Management can be accessed from Advanced Settings.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587933/original/Vs_yXRARxytJOOcBF9g90fRIoS2wtfDJGA.png?1783584601)  
  


  3. Enable or disable WordPress Debugging: Utilize this tool to access PHP error messages, warnings, notices, and other developer-related notifications on your website.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587931/original/KImBDfvvgutg8WrZK02L3mBl87Ebgm1hRg.png?1783584600)  
  


  4. Server Settings: Manage your WordPress Database using phpMyAdmin.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155075587929/original/0MkPak1ziSXw6lLLq6SQIzV8YcY87usARA.png?1783584600)


### Adding an Additional Domain

Once your site is ready to publish, you can connect your domain to the WordPress site.

Please follow our dedicated article for instructions on connecting your domain with the WordPress site.

### Common Issues & Troubleshooting

1\. Plugin not installing

  * Confirm you have admin access

  * Check hosting restrictions


2\. Site not displaying widgets

  * Clear cache (plugin/server/CDN)

  * Disable conflicting plugins temporarily


3\. Connection errors

  * Recheck credentials

  * Ensure the correct location/account is selected in HighLevel


### Frequently Asked Questions

Q: I'm unable to add the same domain to my other subaccount/location.

A: The same domain/subdomain can't be used in 2 locations simultaneously.

Q: Why can't I update my primary domain?

A: The primary domain can be updated if you have successfully added an additional domain first.

Q: I've added the A / CNAME record, but the domain is still not being added.

A: This can happen due to a few reasons:

  * There is a typo in your domain name: In this scenario, fixing the typo will resolve your issue.

  * Your DNS changes haven't been propagated yet: In this case, you must wait longer and try again after a few hours or the next day to see if it works.

  * Your DNS configuration is not set up correctly: Please get in touch with your Domain Provider and discuss the errors with their support team.

  * Multiple conflicting records: Maybe you have conflicting records for the same subdomain (for example, if blog.mydomain.com has a CNAME record pointing to wp3.msgsndr.com but it also has an A record pointing to some other provider). In such cases, removing the duplicate record will fix your issue.


Q: I can't connect my root domain (ex., mydomain.com).

A: Please make sure there are no additional A, AAAA, TXT records, etc. if you plan to use that slug/root domain for WordPress.

Q: How many WordPress sites can I have per sub-account?

A: You can have as many sites as you wish under a single account, there are no limitations! :)

Q: How can I request to cancel a client's WordPress subscription?

A: To begin a WordPress Cancellation Request, you must navigate to "Delete Site" under the Advanced settings of your WordPress Dashboard.

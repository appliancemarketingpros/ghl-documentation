# SSL Certificates for Dedicated LC Email Domains

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001227438-ssl-certificates-for-dedicated-lc-email-domains](https://help.gohighlevel.com/support/solutions/articles/48001227438-ssl-certificates-for-dedicated-lc-email-domains)  
**Category:** Email  
**Folder:** LC Email

---

Email Infrastructure

SSL Certificates for Email Domains

Keep your email links secure and working by understanding and managing SSL certificates on your dedicated domain.

Overview

SSL certificates (Secure Sockets Layer) ensure that links included in your emails are secure and accessible by encrypting tracking URLs, open URLs, and click URLs. Without a valid SSL certificate, those links will break — recipients will see errors instead of your content.

When a dedicated domain is added and verified, an SSL certificate is issued automatically. Your domain will show one of three statuses: **SSL Issued** (certificate active), **SSL Pending** (being generated), or **SSL Unknown** (not yet generated or issued).

Table of Contents

1

Why Do I Need an SSL Certificate?

2

Where to See SSL Certificates

3

How to Set Up SSL Certificates for Email Domains

4

Frequently Asked Questions

1

## Why Do I Need an SSL Certificate?

Without a valid SSL certificate, recipients may see broken links or security warnings when clicking through your emails. This harms your sender reputation and reduces engagement. Ensuring SSL is issued and valid is critical for successful email campaigns.

Prevent Broken Links

Avoid the "secure connection" error

SSL certificates ensure links in your emails are functional and prevent the "This site can't provide a secure connection" error from appearing when recipients click them.

Enhance Security

Encrypted links that inspire trust

SSL secures communication between your domain and recipients, ensuring tracking, open, and click URLs are all encrypted end-to-end.

Maintain Engagement

Keep clicks flowing without disruption

Preventing errors means higher engagement — recipients can access your content without hitting security warnings or broken-link pages.

2

## Where to See SSL Certificates

To access SSL management for your custom email domain, follow these steps:

Step 1

Navigate to **Location Settings**.

Step 2

Select **Email Services**.

Step 3

On the right side, click the **Dedicated Domain And IP** button. This opens the domain management screen where you can check SSL status and take action if needed.

![Location Settings navigation to Email Services](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032685878/original/KpOIuYa-wAWeMlovftKhUZ22a_CPT3yJ0w.jpg?1726063683)

Navigating to Email Services in Location Settings

![Dedicated Domain And IP panel showing SSL certificate status](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032685971/original/f-IR_ph9PrvRzNEdzHK_OIJnoKQstusv3g.jpg?1726063742)

The Dedicated Domain And IP screen showing SSL certificate statuses

3

## How to Set Up SSL Certificates for Email Domains

Setting up or resolving SSL issues for your custom domain is straightforward. Follow the two steps below to ensure your certificate is issued or reissued correctly.

Step 1

Verify the Domain

Go to **Settings → Email Services → Dedicated Domain And IP** and click the **Verify Now** button next to your domain. You'll be taken to your domain DNS page — confirm all records are correctly set up and verified.

DNS Instructions for Common Providers

[GoDaddy](<https://www.godaddy.com/help/manage-dns-zone-files-680>)

[Google Domains](<https://support.google.com/a/answer/48090?hl=en>)

[Hostgator](<https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom>)

[Hover](<https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-CNAME-MX-TXT-and-SRV-Updated-Aug-2015->)

[Namecheap](<https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/cpanel-email-deliverability-tool--spf-and-dkim-records/>)

[Squarespace](<https://support.squarespace.com/hc/en-us/articles/205812348-Opening-Advanced-DNS-settings>)

[AWS (Route 53)](<https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html>)

[Cloudflare](<https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/>)

[Bluehost](<https://www.bluehost.com/help/article/dns-management-add-edit-or-delete-dns-entries>)

[Hostinger](<https://www.hostinger.com/tutorials/how-to-use-hostinger-dns-zone-editor>)

[InMotion](<https://www.inmotionhosting.com/support/domain-names/create-cname-record/>)

[Hostwinds](<https://www.hostwinds.com/guide/how-to-change-cname-record/>)

Once your DNS records are verified, click the **Verify domain** button to issue or reissue your SSL certificate.

![Verify domain button to issue SSL certificate](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032685638/original/_xOi8GDwehFPSNgObxk2fnYzk3M092RvKg.png?1726063543)

Click "Verify domain" to trigger SSL issuance

Step 2

Check SSL Status

  * **SSL Issued:** No further action needed — your domain is secured.
  * **SSL Pending:** Reverify the domain by following Step 1 again. This prompts the system to complete certificate generation.
  * **SSL Unknown:** Follow the domain verification process again. If SSL remains unknown after verification, review your DNS records and retry.


![SSL certificate status indicator on the domain management screen](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155032685791/original/fvZ-XxXyOUUiH8CamxriFOGDlmTle4T8oQ.png?1726063609)

SSL status indicators: Issued, Pending, or Unknown

You're All Set

Once SSL shows as **Issued** , your domain and email campaigns are secure, functional, and ready to send.

4

## Frequently Asked Questions

Q: What should I do if my email link URLs are broken?

Go to **Settings → Email Services → Dedicated Domain And IP** and click **Verify domain** to reissue the SSL certificate. Once SSL is re-issued, your links will resolve correctly.

Q: What does "This site can't provide a secure connection" mean?

This error means the SSL certificate for your domain is not properly issued. Verify the domain again from the **Dedicated Domain And IP** screen to resolve it.

Q: What should I do when SSL is Pending or Unknown?

Reverify the domain by following the domain verification steps. This prompts the system to generate a new SSL certificate. If the status persists, double-check that all DNS records are correctly set up for your domain.

Q: Is there a cost for the SSL certificate?

No. SSL certificates are issued automatically at no additional cost when you add and verify a dedicated domain. You do not need to purchase or configure a certificate separately.

Q: How long does it take for the SSL certificate to be issued?

In most cases, the certificate is issued within a few minutes of domain verification. If it shows as **Pending** for more than 15–30 minutes, try reverifying the domain to trigger reissuance.

Q: Does SSL apply to all email links, including tracking and unsubscribe URLs?

Yes. The SSL certificate covers all URLs generated by the email system for your dedicated domain, including tracking URLs, open pixels, click links, and unsubscribe links.

Q: Will my contacts notice any downtime if I need to reissue the SSL?

Reissuance is nearly instant and happens in the background. Contacts clicking links in previously sent emails may briefly see an error during the few minutes it takes to reissue, but links will resolve correctly once the new certificate is active.

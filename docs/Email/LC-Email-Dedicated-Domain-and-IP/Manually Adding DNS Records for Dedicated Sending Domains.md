# Manually Adding DNS Records for Dedicated Sending Domains

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000004427-manually-adding-dns-records-for-dedicated-sending-domains](https://help.gohighlevel.com/support/solutions/articles/155000004427-manually-adding-dns-records-for-dedicated-sending-domains)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Deliverability

Manually Adding DNS Records for Your Dedicated Sending Domain

How to create the required DNS records in your hosting provider's dashboard, with quick links to instructions for the most common providers.

What This Covers

To authenticate your dedicated sending domain, you need to add specific DNS records inside your domain hosting provider's dashboard. The platform generates the exact values you need — your job is to copy them into the correct fields in your registrar or DNS manager. This article shows you what to expect and links you directly to the instructions for the most common providers.

Table of Contents

1

The DNS Records You'll Need to Add

2

DNS Provider Setup Guides

3

Frequently Asked Questions

1

## The DNS Records You'll Need to Add

After adding your domain inside the platform, you'll be shown a screen listing the specific DNS records required to authenticate it. Each record includes a **Type** , **Name/Host** , and **Value** that you'll copy directly into your DNS provider's dashboard.

![DNS records screen in the platform showing the records to add](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155039360663/original/HzBGtABLJsce2UkbD9t9VMG5rxqjnhBPfg.png?1736199195)

The platform provides the exact DNS record values — copy each one into your DNS provider's dashboard.

Heads Up

When entering the **Name/Host** value in your DNS provider, do **not** include the root domain (e.g. companyname.com). Only enter the prefix shown — for example, if the record shows **replies.companyname.com** , enter only **replies** in the Name field.

![Example of DNS records being added in a provider dashboard](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155039361554/original/T5G5pq9wi3Y0FuJFrDMUewd5qA0IECShbQ.jpeg?1736202012)

Example of DNS records entered in a provider's DNS management interface.

2

## DNS Provider Setup Guides

Click your DNS provider below to open that provider's official documentation on adding DNS records.

[GoDaddy](<https://www.godaddy.com/help/manage-dns-zone-files-680>)| [AWS Route 53](<https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html>)  
---|---  
[Google Domains](<https://support.google.com/a/answer/48090?hl=en>)| [Cloudflare](<https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/>)  
[HostGator](<https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom>)| [Bluehost](<https://www.bluehost.com/help/article/dns-management-add-edit-or-delete-dns-entries>)  
[Hover](<https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-CNAME-MX-TXT-and-SRV-Updated-Aug-2015->)| [Hostinger](<https://www.hostinger.com/tutorials/how-to-use-hostinger-dns-zone-editor>)  
[Namecheap](<https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/cpanel-email-deliverability-tool--spf-and-dkim-records/>)| [InMotion Hosting](<https://www.inmotionhosting.com/support/domain-names/create-cname-record/>)  
[Squarespace](<https://support.squarespace.com/hc/en-us/articles/205812348-Opening-Advanced-DNS-settings>)| [Hostwinds](<https://www.hostwinds.com/guide/how-to-change-cname-record/>)  
  
Tip

Don't see your provider listed? Search for "**[Your Provider Name] add DNS records** " in your provider's help center — the steps for adding TXT, MX, and CNAME records are similar across all major registrars.

3

## Frequently Asked Questions

Q: How many DNS records do I need to add?

You need to add 5 records in total: 2 TXT records (one for SPF, one for DKIM), 2 MX records (mxa.mailgun.org and mxb.mailgun.org), and 1 CNAME record. All 5 values are shown on the DNS records screen in the platform after you add your domain.

Q: How long does it take for DNS records to propagate after I add them?

Propagation time varies by provider. Many providers (like Cloudflare and Siteground) apply changes within minutes. Others (like GoDaddy and Namecheap) can take anywhere from 30 minutes to 48 hours. If the platform's verification shows a red ✗ immediately after adding the records, wait 15–30 minutes and click **Verify DNS Settings** again before troubleshooting further.

Q: Should I include my root domain (e.g. companyname.com) in the Name/Host field?

No. Most DNS providers automatically append the root domain. Enter only the prefix shown in the platform. For example, if the platform shows **replies.companyname.com** as the hostname, enter only **replies** in the Name field. Entering the full domain can result in a doubled hostname like **replies.companyname.com.companyname.com** , which will fail verification.

Q: What if I don't have access to my DNS provider?

Contact whoever manages your domain — this is typically your web developer, IT team, or the company that registered your domain. Share the DNS record values from the platform's DNS records screen with them and ask them to add the records on your behalf.

Q: I added all the records but some still show a red ✗. What should I do?

First, double-check that each record's Type, Name, and Value match exactly what the platform shows — watch out for extra spaces or including the root domain in the Name field. Then wait a few more minutes and click **Verify DNS Settings** again. If the issue persists after 24 hours, check your DNS provider's dashboard to confirm the records were saved correctly, or contact support.

Q: Will adding these DNS records affect my existing email (e.g. Google Workspace)?

It depends on whether you're using a subdomain or your main domain. If you're setting up a subdomain (e.g. replies.companyname.com), the MX records for the subdomain won't interfere with your main domain's email. However, if you're adding records for your main domain (companyname.com) and it already has Google Workspace MX records, adding the Mailgun MX records will conflict. In that case, use a subdomain instead.

Related Articles

[How to Set Up a Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001226115>) [SSL Certificate for Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>) [How to Migrate My Agency Over to LC - Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>)

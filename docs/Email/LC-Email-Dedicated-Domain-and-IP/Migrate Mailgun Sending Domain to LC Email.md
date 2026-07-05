# Migrate Mailgun Sending Domain to LC Email

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000003211-migrate-mailgun-sending-domain-to-lc-email](https://help.gohighlevel.com/support/solutions/articles/155000003211-migrate-mailgun-sending-domain-to-lc-email)  
**Category:** Email  
**Folder:** LC Email Dedicated Domain and IP

---

Email Infrastructure

Move Your Sending Domain from Mailgun to LeadConnector

How to delete a sending domain in Mailgun and recreate it under LeadConnector Email so all sending goes through the platform.

What This Covers

If you previously set up a sending domain in Mailgun and want to migrate it to LeadConnector Email, the process is straightforward: remove the domain from Mailgun, then add the same domain inside the platform.

Your existing DNS records (TXT, MX, CNAME) can remain in place — they point to Mailgun's infrastructure, which LeadConnector Email also uses under the hood.

Table of Contents

1

Delete the Domain from Mailgun

2

Add the Domain in LeadConnector

3

Frequently Asked Questions

1

## Delete the Domain from Mailgun

Step 1

Navigate to Domain Settings in Mailgun

Log in to your Mailgun account. Go to **Sending → Domain Settings**. In the top-right dropdown, make sure the correct domain you want to migrate is selected.

![Mailgun Sending > Domain Settings with domain selected in top-right dropdown](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48280266614/original/jhvqfR085Lovd-qZJ6jhxAiNkHrOPcvx4g.png?1675802157)

Mailgun — Sending → Domain Settings. Confirm the correct domain is selected in the top-right dropdown.

Step 2

Delete the domain

Scroll to the bottom of the Domain Settings page and click **Delete**. Confirm the deletion when prompted.

![Delete button at the bottom of Mailgun Domain Settings](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48280266633/original/v58M1hzv9FXxvGVERJ2ZR4_EFX0qCl162A.png?1675802167)

Scroll to the bottom of Domain Settings and click Delete.

Important

Deleting the domain from Mailgun is permanent. Any API keys or SMTP credentials scoped specifically to this domain will stop working. Make sure you are no longer sending through Mailgun before proceeding.

2

## Add the Domain in LeadConnector

Once the domain is removed from Mailgun, add the same domain as a Dedicated Sending Domain inside the platform. Follow the standard dedicated domain setup flow:

In your sub-account

Go to Settings → Email Services → Dedicated Domain → + Add Domain

Enter the same domain name you just deleted from Mailgun and click **Add & Verify**. The platform will display the DNS records you need to confirm are in place.

Tip

Because LeadConnector Email also uses Mailgun's infrastructure, your existing DNS records (SPF TXT, DKIM TXT, MX, and CNAME) may not need to change. After clicking **Verify DNS Settings** , the platform will confirm which records are already correct with a green checkmark.

You're All Set

Once all DNS records show green checkmarks, your domain is fully migrated to LeadConnector Email. Send a test email from the Conversations section to confirm everything is working.

3

## Frequently Asked Questions

Q: Do I need to update my DNS records after moving the domain to LeadConnector?

Usually not. LeadConnector Email uses the same underlying Mailgun infrastructure, so the SPF, DKIM, MX, and CNAME records you already added for Mailgun are compatible. After adding the domain in the platform and clicking **Verify DNS Settings** , any records that are already correct will show a green checkmark immediately.

Q: Will I lose any email history or sending reputation when I delete the domain from Mailgun?

Email logs stored in the Mailgun dashboard will no longer be accessible once the domain is deleted from Mailgun. However, your domain's external sending reputation (as seen by recipient mail servers) is tied to your DNS records and IP addresses — not the Mailgun account — so switching to LeadConnector Email does not reset your deliverability standing.

Q: What happens to emails that were already queued or in-flight in Mailgun at the time of deletion?

Emails already accepted and queued by Mailgun before you deleted the domain should still be delivered. However, to avoid any risk, complete all pending sends in Mailgun first and confirm the queue is empty before deleting the domain.

Q: Can I use the same domain on multiple sub-accounts after migrating?

Each sub-account configures its own dedicated sending domain independently. You can add the same domain to more than one sub-account if your use case requires it, but be mindful that this can affect how sending reputation is tracked per account.

Q: Can I move the domain back to Mailgun if I change my mind?

Yes. You would reverse the process: remove the domain from the platform's Dedicated Domain settings and re-add it inside Mailgun. Your DNS records should still be in place and can be reverified in Mailgun. Note that any platform sending that happened in the interim will not appear in Mailgun's logs.

Q: Is there any downtime in email sending during the migration?

There can be a brief window between deleting the domain in Mailgun and completing verification in the platform where emails using that domain may not send successfully. To minimize this window, have the platform's dedicated domain setup ready to complete immediately after deleting from Mailgun. The whole process typically takes only a few minutes.

Q: Do I still need a Mailgun account after migrating to LeadConnector Email?

No. Once all your sending domains are migrated and verified in LeadConnector Email, you no longer need to maintain a separate Mailgun account for email sending through the platform. LeadConnector Email handles the email infrastructure directly.

Related Articles

[How to Set Up a Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/support/solutions/articles/48001226115-how-to-set-up-a-dedicated-sending-domain-lc-email->) [How to Migrate My Agency Over to LC - Email](<https://help.gohighlevel.com/en/support/solutions/articles/48001222501>) [SSL Certificate for Dedicated Sending Domain (LC - Email)](<https://help.gohighlevel.com/en/support/solutions/articles/48001227438>)

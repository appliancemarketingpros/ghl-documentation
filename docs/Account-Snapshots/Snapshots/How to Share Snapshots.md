# How to Share Snapshots

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000982513-how-to-share-snapshots](https://help.gohighlevel.com/support/solutions/articles/48000982513-how-to-share-snapshots)  
**Category:** Account Snapshots  
**Folder:** Snapshots

---

Snapshots • Sharing • Assets Protection

How to Share Snapshots

Share reusable Snapshot configurations with the right recipients, choose the appropriate link type, and control how protected assets behave when a Snapshot crosses agency boundaries.

What You'll Learn

Snapshot sharing lets agencies distribute reusable configurations through controlled share links without rebuilding assets manually. This guide explains the available link types, Assets Protection, mixed Snapshots, protected-asset review, and how Snapshot sharing differs from SaaS provisioning.

You'll also learn how sharing, importing, and loading work together and what to do when you need to distribute an updated Snapshot.

Important

Sharing, importing, and loading are different Snapshot actions. **Sharing** generates access to a Snapshot, **importing** adds a shared Snapshot to the recipient's agency-level Snapshot library, and **loading** applies selected Snapshot assets to a sub-account.

Table of Contents

1

What is Snapshot Sharing?

2

Key Benefits of Snapshot Sharing

3

Link Types & When to Use Them

4

Sharing Snapshots That Contain Protected Assets

5

Snapshot Sharing vs. SaaS Provisioning

6

How To Set Up Snapshot Sharing

7

Frequently Asked Questions

8

Related Articles

1

# What is Snapshot Sharing?

Snapshot Sharing is the process of generating a share link or invitation that gives another recipient access to a reusable Snapshot. A Snapshot can contain selected configuration assets such as workflows, funnels, forms, templates, calendars, and other supported account settings.

When another agency receives a share link, it imports the Snapshot into its agency-level Snapshot library. The imported Snapshot can then be loaded into the appropriate sub-account according to the access and restrictions associated with the share.

Share-link options let you control who can access a Snapshot, whether the link can be reused, and whether Assets Protection should restrict protected content from being redistributed outside the receiving agency.

2

## Key Benefits of Snapshot Sharing

Snapshot sharing makes repeatable configurations easier to distribute while giving agencies control over recipient access and protected content. Choosing the right sharing method helps balance speed, consistency, and protection.

**Faster Deployment:** Distribute proven workflows, funnels, templates, and other configurations without rebuilding them manually.

**Consistency:** Give recipients access to standardized configurations that can be imported and reused.

**Controlled Access:** Choose reusable, single-use, agency-restricted, or sub-account-restricted sharing methods.

**Assets Protection:** Allow protected assets to be used within the receiving agency while restricting their redistribution outside that agency.

**Mixed Snapshot Sharing:** Continue sharing eligible non-protected assets even when the Snapshot also contains protected assets.

**Pre-Share Visibility:** Review protected assets that will be excluded before completing an external share.

3

## Link Types & When to Use Them

Each Snapshot sharing option controls who can access the Snapshot and how the link can be used. Selecting the appropriate link type reduces accidental reuse and helps match access to the intended recipient.

Link Type| Who Can Import| Behavior / Best Use  
---|---|---  
**Permanent Link**|  Anyone with the active URL| Reusable for repeated imports. Best when the same Snapshot needs to be distributed more than once.  
**One-Time Link**|  Anyone with the URL until the permitted import is completed| Designed for a single successful import. Generate another link for another recipient.  
**Email Link**|  The intended email recipient| A single-use sharing experience delivered by email instead of manually copying the URL.  
**Agency-Restricted Link**|  Only agencies whose relationship numbers are specified| Restricts access to approved agencies. Multiple agency relationship numbers can be specified when supported by the sharing workflow.  
**Sub-Account Restricted Link**|  Only the designated sub-account| Best when the Snapshot must be limited to a specific destination rather than broadly reusable.  
**Marketplace Share Link**|  Eligible buyers through the HighLevel App Marketplace listing| Used as part of Marketplace Snapshot distribution. Assets Protection is automatically applied to help prevent protected assets from being repackaged or resold.  
  
**Selling on the Marketplace:** From **Agency View > Account Snapshots**, use the Snapshot action menu and select **Sell on Marketplace** to begin the guided Marketplace listing workflow.

![Sell on Marketplace Snapshot workflow](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155064696055/original/FFdPVRdO1QCb0YJu2yo0CaeVfGr8Ss_JUw.gif?1770819813)

4

## Sharing Snapshots That Contain Protected Assets

Assets Protection controls what happens when protected Snapshot content would leave an agency. Protected assets can be reused across sub-accounts and Snapshots inside the receiving agency, but the protected status remains attached and restricts external redistribution.

Applying Assets Protection to a Snapshot You Share

Turn on **Assets Protected** when generating the share if you want applicable Snapshot assets to remain protected after the recipient imports them. Recipients can use those protected assets within their agency, but protected content remains restricted from external redistribution or resale.

Sharing a Snapshot That Already Contains Protected Assets

If the Snapshot contains protected assets inherited from an earlier protected Snapshot, those assets can continue to be used internally. When the Snapshot is shared outside the agency, protected assets are excluded while eligible non-protected assets continue through the share.

**Important:** The presence of protected content does not make the entire Snapshot unshareable. Mixed Snapshots can still be shared externally; only the protected assets are held back.

### **Review Protected Assets Before Sharing**

When protected content is detected during external sharing, HighLevel provides a review of the assets that cannot leave the agency and the eligible assets that can continue. Expand asset groups when you need to inspect individual items before completing the share.

![Pre-share review showing protected assets that will be excluded from an external Snapshot share](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079639423/original/E7foOi4Auy87TrfEgsQWdNFHXG4a6NkMrA.png?1788098960=)

![Expanded protected-asset review showing individual Snapshot asset sharing status](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079639427/original/ynk1V7vKC42k6ZVMz8XJE7wwx_KblmGv4Q.png?1788098976=)

For the complete protection model, see [Assets Protected Snapshots (Called "IP Protected" Earlier)](<https://help.gohighlevel.com/support/solutions/articles/155000002852-assets-protected-snapshots-called-ip-protected-earlier->).

5

## Snapshot Sharing vs. SaaS Provisioning

Manual Snapshot sharing and SaaS provisioning can both distribute Snapshot configurations, but they solve different onboarding needs. Understanding the distinction prevents share links from being confused with automated SaaS account creation.

Workflow| How It Works| Best For  
---|---|---  
**Snapshot Sharing**|  You generate a share link or invite. The recipient imports the Snapshot and then uses it in the appropriate account workflow.| Manual distribution to agencies, clients, partners, or specific destinations.  
**SaaS Provisioning**|  A Snapshot is attached to a SaaS plan and can be automatically applied when checkout provisions a new sub-account.| Automated SaaS onboarding and repeatable account creation.  
  
For automated SaaS provisioning, see [Getting Started with the SaaS Configurator](<https://help.gohighlevel.com/support/solutions/articles/155000008015-getting-started-with-the-saas-configurator>).

6

## How To Set Up Snapshot Sharing

Proper setup ensures the Snapshot reaches the intended recipient with the correct access and protection settings. Confirm permissions and refresh the Snapshot when needed before generating the share.

Required Access

The user must have the appropriate Snapshot permissions. If the sharing action is unavailable, verify that **Share/Import Snapshots** access is enabled for that user.

Before Sharing Updated Content

If the source sub-account changed after the Snapshot was created, [refresh the Snapshot](<https://help.gohighlevel.com/support/solutions/articles/48000982583-refresh-or-update-snapshots>) first so the share contains the intended current assets.

Step 1

Open My Snapshots

From **Agency View** , go to **Account Snapshots > My Snapshots**.

![Account Snapshots page showing My Snapshots](https://jumpshare.com/share/QmzbOAYgy2d10wuvVx9A+/Screen+Shot+2025-12-10+at+8.01.02+PM.png)

Step 2

Open the Share Snapshot Workflow

Locate the Snapshot you want to distribute, open the **⋯ three-dot** action menu, and select **Share Snapshot**.

![Snapshot action menu showing Share Snapshot](https://jumpshare.com/share/ogUl0SQhW4w2Fy8vph9O+/Screen+Shot+2025-12-10+at+8.06.36+PM.png)

Step 3

Choose a Share Option

Select the sharing method that matches the intended recipient and reuse requirements:

  * **Permanent Link** for reusable sharing.
  * **One-Time Link** for a single-use share.
  * **Email Link** for single-use delivery by email.
  * **Agency-Restricted** to limit access to specified agencies.
  * **Sub-Account Restricted** to limit the Snapshot to the selected destination.


Step 4

Configure Assets Protection (Optional)

Turn on **Assets Protected** when you want the applicable Snapshot assets to remain protected after the recipient imports them. Protected assets can be reused within the receiving agency but remain restricted from external redistribution or resale.

![Share Snapshot modal with Assets Protection enabled](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080790014/original/J98dDhBlRFMrf3IRwqjvrl0I4uXCbmdd9Q.png?1789242364)

Enable Assets Protection before generating the protected share.

Step 5

Review Protected Assets When Applicable

If the Snapshot already contains protected assets and the share would send content outside the agency, review the protected content shown before continuing. Protected assets will be excluded while eligible non-protected assets can continue through the share.

Step 6

Generate and Share the Link

  1. Click **Get Link**.
  2. Copy the generated link and send it to the intended recipient.


![Generated Snapshot share link ready to copy](https://jumpshare.com/share/KAsxVvxJwfGqQHYm728A+/Screen+Shot+2025-12-10+at+9.35.56+PM.png)

7

## Frequently Asked Questions

Q: Can I share a Snapshot that contains protected assets?

Yes. If the Snapshot contains both protected and non-protected assets, the eligible non-protected assets can still be shared externally. Protected assets are excluded when they would leave the agency.

Q: Do I need to remove protected assets manually before sharing a mixed Snapshot?

No. HighLevel identifies protected assets during external sharing and excludes them while allowing eligible assets to continue.

Q: Can the receiving agency reuse protected assets internally?

Yes. Protected assets can be reused across sub-accounts and Snapshots inside the receiving agency. Their protected status continues to follow them.

Q: Can the receiving agency re-share or resell protected assets to another agency?

No. Protected assets remain restricted when they would leave the receiving agency.

Q: If I update a Snapshot after sharing it with another agency, does the recipient receive the changes automatically?

No. External agencies do not receive Snapshot updates automatically. Refresh the Snapshot, generate the appropriate updated share, and have the external agency import the updated Snapshot.

Q: How do I update sub-accounts inside my own agency?

Refresh the Snapshot first. You can then use **Push Updates** for eligible linked sub-accounts inside your agency and choose which refreshed assets to send.

Q: I shared a Snapshot but the recipient did not see my newest assets. What happened?

The Snapshot may not have been refreshed after the source sub-account changed. Refresh the Snapshot so the new or modified assets are captured, then share the updated Snapshot again.

Q: Why don't I see the option to share a Snapshot?

Check the user's Snapshot permissions. The appropriate **Share/Import Snapshots** permission must be enabled for the user to perform Snapshot sharing actions.

8

### Related Articles

[ Assets Protected Snapshots (Called "IP Protected" Earlier) ](<https://help.gohighlevel.com/support/solutions/articles/155000002852-assets-protected-snapshots-called-ip-protected-earlier->) [ Snapshots - Overview ](<https://help.gohighlevel.com/support/solutions/articles/48000982511>) [ Creating New Snapshots in HighLevel ](<https://help.gohighlevel.com/support/solutions/articles/48000982512-creating-new-snapshots-in-highlevel>) [ How to Import Snapshots in HighLevel ](<https://help.gohighlevel.com/support/solutions/articles/155000007995-how-to-import-snapshots-in-highlevel>) [ Refresh or Update Snapshots ](<https://help.gohighlevel.com/support/solutions/articles/48000982583-refresh-or-update-snapshots>) [ Granular Permissions for Snapshots ](<https://help.gohighlevel.com/support/solutions/articles/155000004594-granular-permissions-for-snapshots>)

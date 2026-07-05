# Why won't my DNS records work in SquareSpace?

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001153705-why-won-t-my-dns-records-work-in-squarespace-](https://help.gohighlevel.com/support/solutions/articles/48001153705-why-won-t-my-dns-records-work-in-squarespace-)  
**Category:** Email  
**Folder:** MailGun

---

Domain & DNS Setup

Can't Update DNS Records on Squarespace?

Squarespace blocks DNS record changes made from Google Chrome. Here's how to work around it.

What You'll Learn

Per Squarespace's own support team, DNS record changes cannot be saved when made from the Google Chrome browser. This article explains the issue and the quick fix.

Table of Contents

1

Why DNS Changes Fail on Squarespace

2

The Fix: Switch Browsers

3

Frequently Asked Questions

1

## Why DNS Changes Fail on Squarespace

Per Squarespace's own support documentation, they do not allow changes to DNS records to be made through the **Google Chrome** browser. If you're logged into your Squarespace domain settings in Chrome, your new or edited DNS records — such as the ones needed to connect your sending domain — may fail to save, even though the interface doesn't always show a clear error.

2

## The Fix: Switch Browsers

To fix this, simply use a different browser to add or edit your DNS records in Squarespace.

  * Open your Squarespace domain / DNS settings in **Firefox** , **Safari** , or **Microsoft Edge** instead of Chrome.
  * Re-add the DNS records and save. They should go through without issue.


Good to Know

Once saved in a non-Chrome browser, the records stay in place — you don't need to keep using that browser going forward.

3

## Frequently Asked Questions

Q: Is this a Squarespace issue or something on our end?

It's on Squarespace's side. Their own support team has confirmed that DNS record edits made in Google Chrome don't get saved correctly.

Q: Which browsers work for adding DNS records?

Firefox, Safari, and Microsoft Edge have all been confirmed to work. Chrome is the only browser with this known limitation.

Q: I already tried adding records in Chrome — do I need to redo everything?

Just re-add the same records in a different browser. If the earlier attempt didn't save, there's nothing to undo — simply enter the records again correctly.

Q: Will this affect Chrome on mobile too?

This has been reported with Chrome on desktop. If you run into the same problem on Chrome mobile, switching to another browser or app should resolve it as well.

Q: How do I know if my DNS records actually saved?

Refresh your Squarespace DNS settings page after saving and confirm the records are listed. You can also use a DNS lookup tool to check propagation once you've waited a few minutes.

Q: How long does it take for DNS records to propagate after saving?

Propagation is usually quick, but it can take anywhere from a few minutes up to 24-48 hours depending on your domain's TTL settings.

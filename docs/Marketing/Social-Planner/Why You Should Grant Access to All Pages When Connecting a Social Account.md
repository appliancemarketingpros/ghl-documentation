# Why You Should Grant Access to All Pages When Connecting a Social Account

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008432-why-you-should-grant-access-to-all-pages-when-connecting-a-social-account](https://help.gohighlevel.com/support/solutions/articles/155000008432-why-you-should-grant-access-to-all-pages-when-connecting-a-social-account)  
**Category:** Marketing  
**Folder:** Social Planner

---

### **The problem this prevents**

If posts to a previously connected Facebook Page suddenly start failing with a token or permission error, the most common cause is a later reauthorization of the same Facebook account that didn't include that Page.  
  
Facebook issues one authorization per Facebook user per app. When you connect (or reconnect) your Facebook account and choose which Pages to share, that selection replaces your previous one. Any Page you leave unchecked is deauthorized, even if it's actively connected in another sub-account (location).  
  
**Example:**

  1. Your Facebook account manages Pages A and B.
  2. In Location 1, you connect Facebook and grant access to Page A only. Posting works fine.
  3. Later, in Location 2, you connect the same Facebook account and grant access to Page B only.
  4. Page A is now deauthorized. Posts in Location 1 begin failing with a token error as Social Planner has a valid token for only Page B.


###   
  
**Recommended best practice**

When the Facebook authorization screen asks which Pages to share, select **all Pages** associated with the account. This makes every Page available for connection from any eligible location, without breaking existing connections or requiring reauthorization later.

> **Note:** Granting access to all Pages does not connect every Page to every location. You still choose which Page each location uses.

  
  
**Adding Pages later**

You can grant access to additional Pages at any time by reconnecting the account. **Important:** During reauthorization, keep all previously selected Pages checked and add the new ones. Unchecking a Page revokes access to it and will break the connection in any location where that Page is connected.  
Already seeing token errors?

  1. Reconnect the Facebook account and select **all Pages** this time.
  2. In each location where posting was failing, verify the Page connection in Social Planner. Reconnect the Page if it still shows an error.


###   
  
**FAQ**

  
**Will all my Pages be posted to automatically?**  
No. Granting access only makes Pages available. You choose which Page each location connects to.  
  
**Can I grant access to additional Pages later?**  
Yes. However, you'll need to reconnect the social account and complete the authorization flow again to grant permission to the newly selected Pages and existing added pages. To avoid this extra step, we recommend granting access to all Pages during the initial connection.  
  
**Does this apply to other platforms?**  
This behavior is specific to Facebook and Instagram, where the newest authorization replaces the previous one. For other platforms, granting access to all available profiles is still a good practice wherever the option exists.

# Wishlisting Products in Ecommerce Stores

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008699-wishlisting-products-in-ecommerce-stores](https://help.gohighlevel.com/support/solutions/articles/155000008699-wishlisting-products-in-ecommerce-stores)  
**Category:** E-commerce store  
**Folder:** E-Commerce Store

---

Ecommerce

Wishlisting Products in Ecommerce Stores

Let logged-in customers save products they want to revisit and manage those saved items from a dedicated Wishlist experience.

What You'll Learn

Product Wishlisting in HighLevel Ecommerce Stores lets logged-in customers save products from the storefront and return to them later through the Customer Access Center. Store owners can enable wishlisting on supported product elements, customize the wishlist button, and add a Wishlist option to customer navigation.

Proper setup requires Customer Login and a connected store domain. This guide covers the storefront experience, Customer Access Center behavior, configuration steps, troubleshooting, and the exact locations where customers can save and manage products.

Login and Domain Requirement

Customers must be logged in to use Wishlist. A valid store domain must also be connected and configured with a default page linked to the store so Customer Login and Wishlist access can function correctly.

Table of Contents

1\. What is Wishlisting in Ecommerce Stores? 2\. Key Benefits of Wishlisting 3\. Where Wishlist Appears in the Store 4\. Customer Login and Wishlist Experience 5\. How To Setup Wishlisting in Ecommerce Stores 6\. Manage Saved Products in the Wishlist 7\. Troubleshooting 8\. Frequently Asked Questions 9\. Related Articles

# **What is Wishlisting in Ecommerce Stores?**  
  


Wishlisting lets logged-in customers save products they are interested in without adding them to the cart. Saved products can then be reviewed from a dedicated Wishlist page connected to the Customer Access Center.

Store owners can enable the wishlist control on supported storefront elements and customize its appearance. This creates a convenient way for shoppers to remember products and return to them later without interrupting the normal shopping journey.

## **Key Benefits of Wishlisting in Ecommerce Stores**  
  


Wishlisting gives customers a lightweight way to remember products while they browse. For store owners, it adds a useful customer-experience feature without requiring shoppers to immediately place products in their cart.

  * **Save Products for Later:** Customers can keep products they want to revisit without adding them to the cart.
  * **Simpler Product Discovery:** Saved items remain organized in a dedicated Wishlist rather than requiring customers to locate them again.
  * **Customer-Specific Experience:** Wishlist access is tied to authenticated Customer Access Center use.
  * **Multiple Storefront Entry Points:** Wishlisting can be enabled on Product List, Product Details, and Featured Product elements.
  * **Customizable Appearance:** Adjust the active wishlist icon color and wishlist button background color.
  * **Convenient Navigation:** Add My Wishlist to the logged-in customer navigation so saved products are easy to reach.


## **Where Wishlist Appears in the Store**  
  


Wishlist controls can appear wherever supported product elements are displayed. Enabling the feature in the appropriate Store Builder element lets customers save products while browsing or while reviewing an individual product.

Store Element| Wishlist Experience  
---|---  
**Product List**|  Displays a wishlist control on supported product cards while customers browse the catalog.  
**Product Details**|  Lets customers save the product directly from its Product Details Page.  
**Featured Product**|  Lets customers save products displayed through a Featured Product element.  
  
### **Product List Experience**

Product List wishlisting gives shoppers a fast way to save an item without opening its Product Details Page. This is especially useful when customers are comparing several products in the same catalog view.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080659322/original/htXV9LHcbZbBBu0ryhPa4mwbzFmMNkNkXw.png?1789097251)

### **Product Details Experience**

The Product Details Page can display the same wishlist control alongside the product's purchasing information, allowing a customer to save the item while reviewing its details.

  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080659346/original/4xk0sqkOppvC-ko0Gqd6ns_5j_aP2QlB3A.png?1789097326)

## **Customer Login and Wishlist Experience**

Wishlists are designed for authenticated customers so saved products can be associated with their customer experience. Customer Login and the Customer Access Center therefore form an important part of the wishlist workflow.

  * Customers must be logged in before using Wishlist.
  * If a logged-out customer attempts to use Wishlist, the Customer Access Center login experience is prompted.
  * After login, customers can access **My Wishlist** from configured storefront navigation.
  * The dedicated Wishlist page displays saved products and provides controls to remove items.
  * A valid store domain must be configured for Customer Login to function correctly.


### **Wishlist in Customer Navigation**

Adding My Wishlist to the customer menu creates a direct route from the live storefront to the customer's saved products. Logged-in customers can then move between their orders, wishlist, and account controls from the same navigation area.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080659334/original/BBOg95W11IbIxTA9TA3OAIG1bi5kPICphg.png?1789097285)

## **How To Setup Wishlisting in Ecommerce Stores**

Enabling the wishlist on product elements and adding a customer-navigation link ensures shoppers can both save products and return to them later. Complete the storefront, login, and domain configuration before testing the live experience.

### **Step 1: Open the Store Builder**

Open the store you want to edit so wishlist controls can be configured on the product elements where customers browse and review products.

  1. Go to **Sites → Stores**.
  2. Open the applicable Ecommerce Store.
  3. Open the Store Builder and navigate to the page containing the product element you want to configure.


### **Step 2: Enable and Customize Wishlist Products**

Wishlist settings are configured on supported product elements. Enable the feature wherever customers should be able to save products, then adjust the available colors to match the storefront design.

  1. Select the **Product List** , **Product Details** , or **Featured Product** element.
  2. Open **General** settings.
  3. Expand **Wishlist Products**.
  4. Turn on **Enable wishlist for products**.
  5. Choose the **Wishlist Icon Active Color**.
  6. Choose the **Wishlist Button Background Color**.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080659351/original/5XA93TgDIflYs3cCOrr6NHVCg5EW1OscPQ.png?1789097349)

### **Step 3: Add My Wishlist to Customer Navigation**

A My Wishlist menu item gives logged-in customers a predictable way to open their saved-product list from the store. Configure the menu item to route directly to the Wishlist page in the Customer Access Center.

  1. Select the store's **Navigation Menu**.
  2. Open **General → Customer Login**.
  3. Turn on **Enable Customer Login** if it is not already enabled.
  4. Add or configure a menu item named **My Wishlist**.
  5. Set **Go To** to **Go to Customer Access Center**.
  6. Set **Page** to **Wishlist**.
  7. Submit the menu configuration.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080659336/original/prqIr49zcfbsfjJd_c1leDrHuxwuEpr8tA.png?1789097301)

### **Step 4: Verify the Store Domain**

Customer Login depends on the live store domain. Confirm the domain is connected and that its default page points to a page in the Ecommerce Store before testing the wishlist as a customer.

  1. Confirm the store has a valid connected and verified domain.
  2. Confirm the domain's default page is linked to a page within the store.
  3. Correct the domain configuration before testing Customer Login if either requirement is missing.


### **Step 5: Save, Publish, and Test**

Testing the published storefront confirms that wishlist buttons, login behavior, customer navigation, and saved-product access work together as expected.

  1. Save the Store Builder changes.
  2. Publish the updated store.
  3. Open the live storefront.
  4. Test the wishlist while logged out and confirm the login experience appears.
  5. Log in as a customer and save a product.
  6. Open **My Wishlist** and confirm the product appears.


## **Manage Saved Products in the Wishlist**

The dedicated Wishlist page gives logged-in customers one place to review products they previously saved. Customers can return to a product for more information or remove products they no longer want to keep in the list.

  1. Log in through the store's Customer Login.
  2. Open **My Wishlist** from the configured customer menu.
  3. Review the saved products.
  4. Select **View Product** to return to a product when needed.
  5. Use the remove control to delete a product from the Wishlist.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080659366/original/L98-MS5VQdpVP5rDb2AvsVvF1hXmZccsWw.png?1789097377)

## **Troubleshooting Product Wishlists**  
  


Wishlist issues usually involve the product-element toggle, Customer Login configuration, navigation routing, publication status, or store domain setup. Checking these requirements individually helps isolate the missing part of the customer journey.

Issue| What to Check  
---|---  
**The wishlist button does not appear**|  Confirm Enable wishlist for products is turned on for the applicable Product List, Product Details, or Featured Product element, then save and publish the page.  
**A logged-out customer cannot save a product**|  Wishlist requires customer authentication. Confirm Customer Login is enabled and the login experience can open successfully.  
**My Wishlist is missing from the customer menu**|  Open Navigation Menu settings and confirm a menu item routes to Customer Access Center → Wishlist.  
**The Customer Login button does not work**|  Confirm a valid domain is connected and that the domain's default page is linked to a store page.  
**A saved product does not appear in Wishlist**|  Confirm the customer is logged in, verify the product was actually saved, and refresh the Wishlist page before testing again.  
  
## **Frequently Asked Questions**  
  


Q: Do customers need to log in before using Wishlist?

Yes. Wishlist requires customer login. If a logged-out customer attempts to use it, the Customer Access Center login experience is prompted.

Q: Which store elements support wishlisting?

Wishlist can be enabled on the Product List, Product Details, and Featured Product elements.

Q: Can customers remove products from their Wishlist?

Yes. Customers can open their dedicated Wishlist page and remove products they no longer want saved.

Q: Can I change the appearance of the wishlist button?

Yes. Supported settings include the active wishlist icon color and wishlist button background color.

Q: Why does Wishlist require a store domain?

Customer Login relies on the store's live domain. A valid connected domain with a default page linked to the store is required for the authenticated customer experience to function correctly.

Q: Do I need to add My Wishlist to the navigation menu?

Adding My Wishlist gives customers a direct storefront route to the dedicated Wishlist page and is the recommended setup when Customer Login is enabled.

Q: Does adding a product to Wishlist also add it to the cart?

No. Wishlist saves a product for later reference. Customers still choose the product and use the normal purchase flow when they are ready to buy.

### **Related Articles**  
  


[ Customer Login for Ecommerce Stores ](<https://help.gohighlevel.com/support/solutions/articles/155000005125>) [ Customer Access Center – View Orders & Digital Downloads ](<https://help.gohighlevel.com/support/solutions/articles/155000004100/>) [ How to Set Up an E-Commerce Online Store ](<https://help.gohighlevel.com/support/solutions/articles/155000001157-how-to-set-up-an-e-commerce-online-store-websites->) [ Custom Product Details Page for E-commerce Stores ](<https://help.gohighlevel.com/support/solutions/articles/155000006238>) [ Getting Started - Create & Sell Products ](<https://help.gohighlevel.com/support/solutions/articles/155000005071/>) [ How to Set Up a Root Domain or Subdomain ](<https://help.gohighlevel.com/support/solutions/articles/48001153720>)

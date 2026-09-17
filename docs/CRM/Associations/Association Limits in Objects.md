# Association Limits in Objects

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005346-association-limits-in-objects](https://help.gohighlevel.com/support/solutions/articles/155000005346-association-limits-in-objects)  
**Category:** CRM  
**Folder:** Associations

---

Association Limits let you control how many records can be linked between objects, helping maintain cleaner and more accurate relationship data. This article shows the supported relationship types, how to configure limits, and what users see when an association limit is reached.

* * *

**TABLE OF CONTENTS**

  * What Are Association Limits?
  * Supported Relationship Types
  * How to Set Up Association Limits
  * Use Case: Real Estate Management
  * How Association Limits Work?
  * Related Articles


* * *

# **What Are Association Limits?**

  


Association limits let you control how many records can be linked together between objects. These rules ensure data remains organized, prevent over-association, and are now visually enforced in the UI.

  


  * Avoids over-linking between records.
  * Helps keep data structures clean.
  * Reduces user confusion when the limits are reached with clear UI feedback.


* * *

## **Supported Relationship Types**

  

    
    
    **Note:** **Limits** are **enforced** **per** **label** and reflected in the user interface..

  


### **For multi-label associations:**

  


  * **One-to-One** (1:1)
  * **One-to-N** (where N ≤ 1000)
  * **One-to-Many**
  * **N-to-Many** (where N ≤ 1000)
  * **Many-to-Many**


  


### **For single-label contact-to-contact associations:**

  


  * **One-to-One (1:1)**
  * **Many-to-Many**
  * **Custom N-to-N**


* * *

## **How to Set Up Association Limits**

  


  1. Go to your sub-account, Navigate to **Settings** > **Objects.**  
  

  2. **Select** any **Custom****Object** or **Contacts** and click on the **three dots** > **Edit****.**  
  

  3. Go to the **Associations** tab.  
  
![](https://jumpshare.com/share/7GVfIHfungV6UIeTZFbd+/GIF+Recording+2026-09-01+at+16.49.02.gif)  
  

  4. Click **Create** **Association** or **edit** an **existing** **association**.  
  
![](https://jumpshare.com/share/IUPEThTYYavmnw8mFx7w+/Screen+Shot+2026-09-01+at+16.51.55.png)  
  

  5. **Choose** **either** a **single** **label** or a **pair** **of** **labels**.  
  

  6. Under **Configure** **Relationship** , select the type (e.g. 1:1, 1:N) and **define** **limits** **if** **applicable.**  
  

  7. Use the Preview section to confirm constraints before saving.  
  

  8. The configured associations are also shown in the associations tab.  
  
![](https://jumpshare.com/share/IA3QvW6bQnhekYOhefFk+/GIF+Recording+2026-09-01+at+17.19.41.gif)


* * *

## **Use Case: Real Estate Management**

  


A **real** **estate** **agency** wants to **ensure** that **each Agent manages no more than 50 Properties** :

  


  * Create a **one-to-N relationship** from **Agent** to **Property**  
  

  * **Set** the******limit** as **N = 50**  
  

  * When an agent hits this cap, users will see a UI warning and can no longer assign more properties, ensuring balanced workloads.


* * *

## **How Association Limits Work?**

  


If you try to associate beyond the allowed count, an error message will be shown instantly, this helps in clear and efficient management of the data-structures

* * *

### **Related Articles**

  


  * [Associating Contacts using Custom Labels](<https://help.gohighlevel.com/en/support/solutions/articles/155000003918>)  
  

  * [Associations Between Opportunities, Companies & Custom Objects](<https://help.gohighlevel.com/en/support/solutions/articles/155000004033>)  
  

  * [Custom Object Templates: Pre-Built CRM Setup in One Click](<https://help.gohighlevel.com/en/support/solutions/articles/155000007819>)

# Using custom values in dashboards and custom reports

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008433-using-custom-values-in-dashboards-and-custom-reports](https://help.gohighlevel.com/support/solutions/articles/155000008433-using-custom-values-in-dashboards-and-custom-reports)  
**Category:** Dashboards  
**Folder:** Configuring Dashboards

---

### Overview

Custom values let you insert dynamic, location-specific data into your dashboards — so one dashboard automatically adapts to whichever sub-account is viewing it.

Instead of hardcoding a value like a business name or address, you insert a token (e.g. `{{ location.name }}`). When the dashboard is viewed, the token resolves to the actual value for that location.

* * *

### ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078132262/original/WV8Wx3v7fUk5AJlSjr0TNDrqOFi9hnoVOQ.png?1786453125)

### Who can use this

Dashboard/Custom Report **editors** can configure custom values. Viewers see the resolved values.

* * *

### Where custom values are supported

Wherever you see the **{}** button next to a text input, custom values are supported.

**Widget conditions** When adding a condition to a widget, click {} in the value field to insert a token instead of a static value.

**Dashboard elements**

  * **Embed** — insert a token inside the URL field (e.g. `https://myagency.crm.com/embed/{{ location.id }}/page/main`)
  * **Title** — insert a token in the title text field (e.g. `{{ location.name }} — Performance Dashboard`)
  * **Text box** — insert a token inside the rich text editor; the token appears as plain text inline with your content


* * *

### Available custom values

When you click {}, a picker opens with three categories:

**Location** Fields that resolve based on the sub-account:

  * Location Id
  * Location Name
  * Email
  * Phone
  * Website
  * Address
  * City
  * State
  * Country
  * Postal Code
  * Timezone


**User** Fields that resolve based on the logged-in user:

  * User Id
  * Email
  * Phone
  * Role
  * Type
  * First Name
  * Last Name
  * Name
  * Full Name


**Custom values** All values you have created under **Settings → Custom values** for that location. These appear organised by folder. You can search across all three categories using the search bar at the top of the picker.

* * *

### How to insert a custom value — step by step

**In widget conditions:**

  1. Open a dashboard and click **Edit mode**.
  2. Add or edit a widget and go to the **Conditions** tab.
  3. Set the field (e.g. Address) and operator (e.g. Is).
  4. Click the **{}** button in the value input field.
  5. Browse or search — Location, User, or Custom values.
  6. Select a field. The token is inserted ( `{{ }}`).
  7. Click **Save**.


**In dashboard elements:**

  1. Open a dashboard and click **Edit mode**.
  2. Click **Add element** and choose Embed, Title, or Text box.
  3. Click the **{}** button next to the relevant input field.
  4. Browse or search — Location, User, or Custom values.
  5. Select a field. The token is inserted.
  6. Click **Save**.
  7. Switch to **View mode** — the token resolves to the actual value for that location.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078132288/original/RaLk9_q57K5NqotHogvMd4qzhMsHFbFYZQ.png?1786453142)

* * *

### What happens when a token has no value

If a token cannot be resolved (e.g. the field has no value set for that location), it resolves as **blank** in view mode.

To avoid blank values:

  * For **Location** and **User** fields — ensure the sub-account profile is complete under Settings.
  * For **Custom values** — ensure the value has been created and filled in under **Settings → Custom values** for each location.


* * *

### Setting up custom values

To use your own custom values beyond the built-in Location and User fields:

  1. Go to **Settings → Custom values**.
  2. Click **\+ Add custom value**.
  3. Enter a name and value. Optionally assign it to a folder.
  4. Click **Create**.


The custom value now appears in the {} picker under **Custom values** when editing your dashboard.

* * *

### Frequently asked questions

**1\. Can I mix static text and tokens in the same field?** Yes. You can type static text and insert tokens in the same field. For example: `Welcome to {{ location.name }}. Your address is {{ location.address }}.`

**2\. Does the dashboard re-resolve when I switch sub-accounts?** Yes. When the sub-account context changes, all tokens resolve to the values for the active location.

**3\. Can viewers insert custom values?** No. Only editors can insert custom values. Viewers see the resolved values only.

**4\. Is Image element supported?** No. Custom values are supported in Embed - if the image is present as URL, it can be rendered via Embed.

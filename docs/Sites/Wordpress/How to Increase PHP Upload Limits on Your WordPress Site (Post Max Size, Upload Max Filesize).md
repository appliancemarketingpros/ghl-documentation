# How to Increase PHP Upload Limits on Your WordPress Site (Post Max Size, Upload Max Filesize)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005108-how-to-increase-php-upload-limits-on-your-wordpress-site-post-max-size-upload-max-filesize-](https://help.gohighlevel.com/support/solutions/articles/155000005108-how-to-increase-php-upload-limits-on-your-wordpress-site-post-max-size-upload-max-filesize-)  
**Category:** Sites  
**Folder:** Wordpress

---

If your WordPress site is hosted with us and you are experiencing issues uploading large files, themes, or plugins (such as encountering the "exceeds the maximum upload size for this site" error), you likely need to increase your PHP size restrictions.

You can easily bypass these default limits by modifying your site's .htaccess file directly from your WordPress dashboard.

⚠️ IMPORTANT LIMITATION: The maximum upload limit that can be reliably set using the .htaccess method is 300MB.

  * If you input values above 300MB, the new limit might visually appear in your Media Library, but the actual upload will still fail.

  * For files larger than 300MB, server-level configuration is required.


## Step-by-Step Guide

### Step 1: Install a File Manager Plugin

To edit your site's core files without needing FTP access, you can use a plugin.

  1. Log into your WordPress Admin Dashboard.

  2. Navigate to Plugins > Add New from the left sidebar.

  3. Search for "WP File Manager" (or any similar reputable file manager plugin).

  4. Click Install Now, and then Activate.


### Step 2: Locate Your .htaccess File

  1. Open your newly installed WP File Manager from the left sidebar.

  2. Navigate to your root directory, typically named public_html (this is the folder where your core WordPress files are installed).

  3. Look for a file named .htaccess.


? Pro Tip: Because .htaccess is a core system file, it is sometimes hidden by default. If you don't see it, go to your File Manager settings/preferences and enable "Show Hidden Files".

### Step 3: Edit the .htaccess File

  1. Right-click on the .htaccess file and select Code Editor (or Edit).

  2. Scroll to the very bottom of the text document.

  3. Copy the following lines of code and paste them at the bottom. You can adjust the 128M values to fit your specific needs (up to 300M):


  


php_value upload_max_filesize 128M

php_value post_max_size 128M

php_value memory_limit 2048M

php_value max_execution_time 600

php_value max_input_vars 10000

  


  4. Click Save & Close (or Update) to apply the changes.


### Step 4: Verify Your Changes

You should immediately verify that WordPress has recognized the new limits.

  1. From your WordPress dashboard, go to Media > Add New.

  2. Look below the upload area. You should see text that says: "Maximum upload file size: 128 MB" (or whatever value you set).


## Troubleshooting

  * Still seeing the old limit? Clear your browser cache, as well as any caching plugins or server-side CDN caching you have active, then refresh the page.

  * Are your uploads still failing despite the limit increase? Ensure the specific file format you are trying to upload is supported by WordPress for security reasons.

  * Need more than 300MB? As noted above, anything higher than 300MB needs to be configured at the server level and cannot be forced through .htaccess.


Still stuck? If your limits are still not updating after following these steps, or if you need assistance configuring a limit higher than 300MB, please reach out and contact our support team!

  


* * *

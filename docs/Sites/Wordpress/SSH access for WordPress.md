# SSH access for WordPress

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005588-ssh-access-for-wordpress](https://help.gohighlevel.com/support/solutions/articles/155000005588-ssh-access-for-wordpress)  
**Category:** Sites  
**Folder:** Wordpress

---

For developers and advanced users, Secure Shell (SSH) access provides a direct, secure, and encrypted connection to your WordPress server environment.

With SSH, you can execute commands, manage files in bulk, and utilize tools like WP-CLI without relying on the standard WordPress admin dashboard or basic FTP clients.

## Why Use SSH Access?

  * Advanced File Management: Move, copy, edit, or delete large volumes of files instantly.

  * WP-CLI Support: Manage plugins, themes, users, and database operations using command-line interface tools directly on your server.

  * Efficient Troubleshooting: Review server error logs and diagnose complex issues in real-time.

  * Ironclad Security: Unlike standard FTP, all data transferred over SSH is fully encrypted and secure.


## Step 1: Locate Your SSH Credentials

Before you can connect to your server, you need to retrieve your unique connection credentials from your CRM dashboard.

  1. Log into your account and navigate to Sites > WordPress.

  2. From the WordPress dashboard, open the Advanced Settings tab.

  3. Locate the FTP/SSH Access section.  
  


Here, you will find the four pieces of information required to make your connection:

  * Host / Server Address: (e.g., wp1.msgsndr.com or a specific IP address)

  * Username: Your unique server login name.

  * Password: Your generated server password (you may need to click an eye icon or "Generate" to reveal it).

  * Port: Typically 22 for SSH, but always use the specific port listed on your screen.


## Step 2: Connecting to Your Server

Once you have your credentials handy, you can connect using your computer's built-in terminal or a third-party SSH client.

### For Mac and Linux Users (Using Terminal)

  1. Open the Terminal application on your computer.  
  


  2. Type the following command, replacing the placeholder text with your actual credentials:  
  


  3. ssh username@hostname -p port


  4. (Example: ssh wpuser_12345@wp1.msgsndr.com -p 22)

  5. Press Enter. If this is your first time connecting to this specific server, you will see a message asking if you want to continue connecting. Type yes and press Enter.

  6. When prompted, paste your Password.

  7. ? Note: For security reasons, your cursor will not move and characters will not appear while you are typing or pasting your password. This is normal.

  8. Press Enter. You are now securely connected to your server!


### For Windows Users (Using PowerShell or PuTTY)

Option A: Windows PowerShell (Recommended)

Windows 10 and newer versions have a built-in SSH client. You can simply open the PowerShell app and use the exact same ssh command as the Mac/Linux instructions above.

Option B: PuTTY (Third-Party Client)

If you prefer a graphical interface or are using an older version of Windows:

  1. Download, install, and open[ PuTTY](<https://www.putty.org/>).

  2. In the Host Name (or IP address) field, paste your Host credential.

  3. In the Port field, enter your Port number.

  4. Ensure the Connection Type is set to SSH, then click Open.

  5. A black terminal window will appear asking "login as:". Enter your Username and press Enter.

  6. Enter your Password (again, it will be invisible as you type) and press Enter.


## Troubleshooting Common SSH Issues

  * "Connection Refused" Error: Verify that you are using the exact Port number listed in your dashboard. Also, double-check that your local computer's firewall or office network isn't blocking outgoing SSH traffic.

  * "Permission Denied (publickey, password)" Error: This means your username or password is incorrect. Ensure there are no extra spaces copied at the beginning or end of your credentials. Try generating a new password in the dashboard if the issue persists.

  * Timeout Errors: The server might be temporarily unreachable, or your local IP address might have been temporarily blocked by the server's firewall due to too many failed login attempts. Wait 15 minutes and try again.


Need Advanced Help? If you are unable to connect via SSH after verifying your credentials, please reach out to our 24/7 support team for backend assistance!

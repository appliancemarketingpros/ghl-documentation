# File Size Limits for Attachments in SMS and Email

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48001208913-file-size-limits-for-attachments-in-sms-and-email](https://help.gohighlevel.com/support/solutions/articles/48001208913-file-size-limits-for-attachments-in-sms-and-email)  
**Category:** Phone System  
**Folder:** Messaging

---

Conversations · Attachments

Attachment Size Limits for SMS & Email

Understand file size limits for SMS and email, and send larger files effortlessly with Media Library links and auto-generated video thumbnails.

Overview

This article explains the file size limits of attachments for both SMS and email sent through the platform. It also introduces a powerful enhancement — Attachments Made Easy in Conversations — which lets you send larger files effortlessly via Media Library links and auto-generates video thumbnails to boost engagement.

Table of Contents

1

Key Benefits of Understanding File Size Limits

2

Impact on Users

3

SMS Attachment Size Limits

4

Email Attachment Size Limits

5

How to Upload Attachments in Conversations

6

Paste Attachments from Clipboard

7

How to Send Larger Files

8

Frequently Asked Questions

9

Related Articles

Video Walkthrough

1

## Key Benefits of Understanding File Size Limits

Knowing attachment limits helps you avoid failed deliveries and ensures your emails and messages are optimized for deliverability and engagement.

  * Prevents delivery issues caused by large files
  * Ensures compliance with MMS and email provider rules
  * Simplifies file handling using the built-in Media Library
  * Boosts open and click rates with interactive video thumbnails
  * Reduces manual effort and reliance on third-party file hosting


2

## Impact on Users

  * Reduces manual workarounds like compressing or hosting files externally.
  * Speeds up the attachment process with direct device uploads.
  * Improves engagement by making emails more visually appealing and interactive.
  * Ensures smooth delivery across SMS and email by auto-managing limits.


3

## SMS Attachment Size Limits

SMS messages can only contain text. To include attachments like images, videos, or audio files, you must use MMS, which is supported differently depending on the phone number type and carrier. If you're attaching a file to an SMS, it is automatically converted to an MMS. The following file types are supported for MMS:

**JPEG**

**PNG**

**GIF**

Please Note

Some file types like MP3, MP4, and PDF may work depending on the carrier and device. You can also check out Twilio’s list of supported media types here: [Twilio Supported File Types](<https://help.twilio.com/articles/223181188>).

Part 1

Carrier-Specific File Size Limits for MMS

The recommended best practice is to keep MMS attachments **under 500 KB** to ensure successful delivery across all carriers.

Carrier| Long Code MMS| Toll-Free MMS| Short Code MMS  
---|---|---|---  
AT&T*| 1.0 MB| 0.6 MB| 0.6 MB  
T-Mobile| 1.5 MB| 0.6 MB| 1.0 MB  
Verizon| 1.0 MB| 0.6 MB| 1.2 MB  
  
Part 2

Short Code, Toll-Free, and Long Code Support for MMS

As of **October 2022** , **Toll-Free numbers support MMS**. Before that, they supported SMS only.

Message Type| Supports MMS?| Recommended Max Size  
---|---|---  
Long Code (10DLC)| ✅ Yes| ~500 KB – 1 MB  
Short Code| ✅ Yes| Up to 5 MB  
Toll-Free| ✅ Yes _(Since Oct 2022)_|  Up to 5 MB  
  
4

## Email Attachment Size Limits

Attachment limits for email depend on the email provider used. Exceeding these limits can cause emails to bounce or be undeliverable.

Good to Know

The platform's email composer allows **up to 20 MB** in attachments. Files above this size will be automatically uploaded to the **Media Library** and sent as clickable links.

Email Provider| Max Attachment Size  
---|---  
Gmail| 25 MB  
Yahoo Mail| 25 MB  
Outlook.com| 10 MB  
Mailgun| 25 MB  
  
5

## How to Upload Attachments in Conversations

Uploading files directly in the Conversations composer has been made easier and more flexible with the new attachment workflow. Whether you're sending an SMS or an email, you can now upload files from your device or choose from your Media Library — all from within the message composer. This process eliminates the need to manually compress files or use third-party hosting platforms, streamlining your workflow and improving the customer experience. Here is a step-by-step process for uploading or attaching files.

Step 1

Access the Attachment Options

To begin, open a conversation under the **Conversations** tab and click the **three-dot icon (•••)** in the message composer.

![Three-dot icon in the message composer](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044663694/original/VghkbqBAuqr7F9TfukAwR8BHZYkE5mrw0w.png?1744036309)

Step 2

Choose Your Attachment Source

After clicking the three-dot icon, select **“Attach Files”**. You'll see two options:

![Attach Files options](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155044664243/original/e_BCXDXK9OyFh8A9HY6SbLrdGNs4rJ6OUg.png?1744036710)

**Upload from System** — choose a file from your local device.

**Choose from Media Library** — select a previously uploaded file.

Step 3

Automatic Handling for Large Files

If the file exceeds **20 MB (for email)** or **any size for SMS** , the platform will automatically upload it to the **Media Library** and insert a **clickable link** into your message.

This ensures that your message is delivered without hitting size limits.

Important

**Video Uploads Get Auto-Generated Thumbnails.** When uploading a video file through the Media Library, the platform will automatically generate a **GIF thumbnail** to be shown in your email, making your message more engaging and clickable.

6

## Paste Attachments from Clipboard

Instead of opening the attachment menu, you can attach files by pasting them.

  1. Copy a supported file or image on your computer.
  2. Click inside the message composer in Conversations.
  3. Press **Ctrl + V** (Windows) or **Cmd + V** (Mac), or right-click and **Paste**.


The pasted file attaches instantly to the current message and respects the same size limits and media-handling rules described above.

![Pasting an attachment from the clipboard](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155060706026/original/GL2S766DxhqHpZ2qVnlPEZTuSqpCUN0luA.gif?1765880533)

7

## How to Send Larger Files

  * Upload directly via the email/SMS composer.
  * Files larger than 20 MB are auto-hosted via the Media Library and inserted as links.
  * Use cloud hosting only if needed outside the platform.
  * Add videos via the Media Library for interactive thumbnails.


8

## Frequently Asked Questions

Q: What happens to files over 20 MB?

They are auto-uploaded to the Media Library and sent as clickable links.

Q: Can I upload attachments directly from my device?

Yes! You can choose between uploading from your system or browsing the Media Library.

Q: Can I attach videos to an SMS?

Yes, videos are sent as hosted links — not embedded files — to avoid delivery issues.

Q: Do Toll-Free numbers support MMS?

Yes! Since October 2022, Toll-Free numbers now support MMS and attachments.

Q: Will video attachments generate a preview in emails?

Yes — GIF thumbnails are auto-generated for video files uploaded via the Media Library.

Q: What's the safest file size to guarantee MMS delivery?

Keeping MMS attachments under 500 KB is the recommended best practice to ensure successful delivery across all carriers.

Q: Why did my SMS turn into an MMS?

SMS can only carry text. As soon as you attach a file such as an image, GIF, or video, the message is automatically converted to an MMS so the media can be delivered.

Related Articles

[Attachments Made Easy in Conversations](<https://help.gohighlevel.com/support/solutions/articles/155000001323-attachments-made-easy-in-conversations>) [How to Attach Files to MMS Using Custom Values](<https://help.gohighlevel.com/support/solutions/articles/48001218845-how-to-attach-files-to-mms-using-custom-values>)

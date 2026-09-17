# How to send Images, Video, Audio and Document via WhatsApp

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005142-how-to-send-images-video-audio-and-document-via-whatsapp](https://help.gohighlevel.com/support/solutions/articles/155000005142-how-to-send-images-video-audio-and-document-via-whatsapp)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

WhatsApp Automation

# How to Send Images, Video, Audio and Documents via WhatsApp

Send media messages from a workflow using the WhatsApp Media action

Table of Contents

  * How to Send Images, Video, Audio and Documents via WhatsApp
  * FAQ


**Note:** WhatsApp media messages can only be sent inside the 24-hour customer service window — the period that opens after a customer sends a message and closes 24 hours after their last message. Outside this window, only approved message templates can be sent.

## How to Send Images, Video, Audio and Documents via WhatsApp

1

Go to the **Automation** tab in your dashboard.

![Automation tab in dashboard](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045580731/original/u8aJHt15WV4o6TlmrA3C5pvxt-_MCPLYUw.png?1745485217)

2

Click on **Create Workflow** , then select **Start from Scratch**.

![Create workflow, start from scratch](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045580825/original/zxm_pvd2hKpDcuUwfhiV1uVKIBFHO7cuWg.png?1745485288)

3

Click on the **"+" icon** to add a new workflow step.

![Add new workflow step](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045581489/original/lJB_r3TEqJyspIG6jsV4KnrvLgs9QMfmIw.png?1745485753)

4

Search for **"WhatsApp: Customer Service Window Check"** and select it. This step confirms the message will only send while the 24-hour window is open.

![WhatsApp Customer Service Window Check step](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045581858/original/U3jhl-Ru6fnVb-9WzReTQ21Yb3FeCeHdPw.png?1745485943)

5

Under the **Open** branch, click the **"+" icon** to add the next step.

![Add step under Open branch](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045582056/original/prxqdl3Cc38Z8fif9qBqttuQqAQXkYdcIA.png?1745486079)

6

Select the **WhatsApp Media** action, choose the **From Number** , and specify the **Media Type** — Audio, Image, Video, or Document.

![Choose From Number and Media Type](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045582495/original/YYIHFCIxxH8Pmzh8dUmBFNDKn6jPrvUdkA.png?1745486309) ![From Number and Media Type detail view](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045582664/original/aLcgcTu0SHWcRNBeQQOL1wRRTIXes6sT_g.png?1745486413)

7

Click **Save Action** to complete the step.

![Save Action](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155045582765/original/-N8jHztIRqZY3TvcjN2H9O_fzvRt-7TDWg.png?1745486493)

## FAQ

Q: How do I ensure the workflow is within the active customer window?

After starting your workflow, click the **"+" icon** and search for **"WhatsApp: Customer Service Window Check."** This step ensures the message is only sent while the customer's 24-hour response window is open.

Q: Can I test the media message in real time?

Yes. Once your workflow is set up and published, you can trigger it under test conditions to confirm the media sends correctly.

Q: What media options can I send via WhatsApp?

You can send audio files, images, videos, documents, and other supported file types through the **Media Type** dropdown in the action settings.

Q: How do I choose the sending number for the media message?

In the **WhatsApp Media** action, select the **From Number** that's already connected to your account.

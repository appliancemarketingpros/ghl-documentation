# Error 131053 — Media Upload Error

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007937-error-131053-media-upload-error](https://help.gohighlevel.com/support/solutions/articles/155000007937-error-131053-media-upload-error)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

Troubleshooting GuideError 131053 — Media Upload ErrorUnderstand why media messages fail to send with error code 131053, which file types and sizes are supported, and how to fix it.  
---  
What you'll learn| + What error 131053 means| + Supported media types and sizes| + All known causes| + Step-by-step fix  
---|---|---|---  
  
* * *

**TABLE OF CONTENTS**

  * What is Error 131053?
  * Supported Media Types and Size Limits
  * Known Causes
  * How to Resolve It
  * How to Prevent It
  * Related Error Codes
  * Frequently Asked Questions


* * *

What is Error 131053?Media Upload Error — WhatsApp was unable to upload the media file attached to the message  
---  
  
Error **131053** is a WhatsApp Cloud API error officially titled **"Media Upload Error"**. It occurs when the WhatsApp API fails to upload a media file you are trying to send — such as an image, video, audio file, document, or sticker. The message is not delivered and the media is not sent.

This is what the error looks like in the API response:
    
    
    "errors": [
      {
        "code": 131053,
        "title": "Media upload error",
        "message": "Media upload error",
        "error_data": {
          "details": "Unable to upload the media used in the message."
        }
      }
    ]

The `error_data.details` field in the webhook response often contains a more specific reason for the failure — such as the exact unsupported MIME type. Always check this field first when diagnosing the error.
    
    
    Example of a specific detail message:
    "Unsupported Image mime type image/webp. Please use one of image/png, image/jpeg."

* * *

Supported Media Types and Size LimitsReference this table before uploading any media to avoid error 131053  
---  
  
The WhatsApp Business API only supports specific file formats and sizes. Any file outside these specifications will trigger error 131053.

Type| Max Size| Supported Formats  
---|---|---  
Image| 5 MB| `image/jpeg`, `image/png` — Must be 8-bit, RGB or RGBA. WebP is NOT supported for regular image messages.  
Video| 16 MB| `video/mp4`, `video/3gpp` — Must use H.264 video codec and AAC audio codec. Single or no audio stream only.  
Audio| 16 MB| `audio/aac`, `audio/mp4`, `audio/mpeg`, `audio/amr`, `audio/ogg` (OPUS codec only)  
Document| 100 MB| PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx), and most common document formats. Any file type not supported as another media type can be sent as a document.  
Sticker| 100 KB| `image/webp` only — Static WebP (outbound). Must be exactly **512 x 512 pixels** with transparent background.  
      
    
    **Important:** WebP images (image/webp) are **only supported as Stickers**. Sending a WebP file as a regular image message will always return error 131053. Convert WebP to JPEG or PNG before sending as an image.

* * *

Known CausesAll confirmed reasons for error 131053 based on Meta documentation  
---  
1\. Unsupported file format or MIME typeThe most common cause. The file format is not on WhatsApp's supported list — for example, sending a `.webp` as a regular image, a `.tiff`, a `.gif`, or a video using the wrong codec. Even if the file extension looks correct, the actual MIME type matters — a file renamed to `.jpg` but encoded as WebP internally will still fail.  
---  
2\. File size exceeds the limitThe file is larger than the allowed maximum for its type. WhatsApp applies size limits **after encryption** , which means the effective size of the file on WhatsApp's end may be slightly larger than the original file. Keep files well within the limits: images under 5 MB, videos under 16 MB, audio under 16 MB, documents under 100 MB, and stickers under 100 KB.  
---  
3\. Corrupted or invalid media fileThe file is corrupted, incomplete, or contains hidden metadata or attributes that cause WhatsApp's media processor to reject it. This sometimes happens with images that have been edited or exported with non-standard encoding.  
---  
4\. Sticker does not meet specificationsStickers have very specific requirements: WebP format, exactly **512 x 512 pixels** , transparent background, and under **100 KB**. Any deviation from these requirements — wrong dimensions, no transparency, too large, or wrong format — will return error 131053.  
---  
5\. Video uses an unsupported codecVideos must use the **H.264 video codec** and **AAC audio codec**. Videos encoded with H.265 (HEVC), VP9, AV1, or other codecs will fail. Also, videos must have a single audio stream or no audio stream — multiple audio tracks are not supported.  
---  
6\. Media URL is not publicly accessibleWhen sending media via a URL (link-based), the URL must be **publicly accessible over HTTPS**. If the URL requires authentication, is behind a firewall, uses HTTP instead of HTTPS, returns a redirect (302), or is not accessible from Meta's servers, the upload will fail with error 131053.  
---  
7\. URL does not end with a recognized file extensionWhen using a URL to send media, the URL should end with the correct file extension (e.g. `.jpg`, `.mp4`, `.pdf`). Dynamic URLs without a clear file extension can confuse Meta's media processor.  
---  
  
* * *

How to Resolve ItWork through these steps to identify and fix the media issue  
---  
  
Step 1 **Check the error_data.details field in the webhook response**

The webhook triggered by the failed message contains a `error_data.details` field with a specific reason. Check this value first — it will often tell you exactly what is wrong, such as the unsupported MIME type or the reason the file could not be processed.

Step 2 **Verify the file format against the supported types table above**

Check the actual format of your file — not just the file extension. Use the conversions below if your file is in an unsupported format:

Unsupported Format| Convert To| Notes  
---|---|---  
WebP (as image)| JPEG or PNG| WebP is only allowed as a Sticker, not a regular image  
GIF| MP4 video| Animated GIFs are not supported — convert to a short MP4  
TIFF / BMP / HEIC| JPEG or PNG| Convert using any image editor  
MOV / AVI / MKV| MP4 (H.264 + AAC)| Use HandBrake or ffmpeg to re-encode with correct codecs  
WAV / FLAC / WMA| AAC or MP3| Convert audio format to a supported type  
Large file over limit| Compress or send as Document| Documents allow up to 100 MB — useful for large files  
  
Step 3 **Check the file size is within limits**

Confirm the file is below the maximum size for its type. If it is too large, compress it before re-uploading. Use tools like **TinyPNG** for images, **HandBrake** for videos, and export documents to PDF format to reduce size. Keep files well under the limit — sizes are measured after encryption, which can increase the effective size slightly.

Step 4 **If using a URL, verify the media URL is correct and publicly accessible**

|  URL must start with `https://` — HTTP URLs are not accepted  
---  
| URL must be publicly accessible without authentication or login — paste it in an incognito browser to test  
---  
| URL should end with the correct file extension — e.g. `.jpg`, `.mp4`, `.pdf`  
---  
| URL must not return a redirect (302 response) — Meta's servers do not follow redirects. Use the final, direct URL  
---  
  
Step 5 **Re-export or re-save the file to clear hidden attributes**

If the file type and size are correct but the upload still fails, the file may have hidden metadata or attributes causing the issue. Re-save or re-export the file from its original application. For images, tools like **imagecompressor.com** can clean hidden attributes. For videos, re-encoding with HandBrake or ffmpeg forces a clean output file.

Step 6 **Contact support if the issue persists**

If the file meets all format and size requirements and the upload still fails, contact our support team with:

  * The file type, format, and size
  * The full error response including the `error_data.details` value
  * Whether you are using a URL or direct file upload
  * The URL of the media file if URL-based (confirm it is publicly accessible)

  
---  
  
* * *

How to Prevent ItBest practices to avoid media upload failures  
---  
| **Always use JPEG or PNG for images** — these are the safest and most universally supported formats. Avoid WebP, TIFF, BMP, and HEIC for regular image messages  
---  
| **Encode all videos as MP4 with H.264 + AAC** before uploading. This is the safest combination and works on all devices and WhatsApp versions  
---  
| **Keep file sizes well under the limits** — sizes are applied after encryption, so aim for images under 4 MB, videos under 15 MB, and stickers under 80 KB to have a safe margin  
---  
| **Host media on a reliable, publicly accessible HTTPS server** — avoid using temporary links, signed URLs that expire, or URLs that require cookies or authentication  
---  
| **Test media URLs before using them in messages** — open the URL in an incognito browser window to confirm it is publicly accessible and returns the correct file directly  
---  
| **When in doubt, send as a Document** — if a file is in an unusual format or close to the size limit, send it as a Document type. Documents accept a wider range of formats and support up to 100 MB  
---  
  
* * *

Related Error CodesOther media-related errors you may encounter  
---  
Error Code| Title| Description  
---|---|---  
131052| Media Download Error| WhatsApp could not download media from the URL provided. Caused by broken links, slow servers, or inaccessible files.  
131051| Unsupported Message Type| The message type itself is not supported by the WhatsApp Business API.  
100| Invalid Parameter| One or more API parameters are invalid or incorrectly formatted in the request.  
131026| Message Undeliverable| Message was not delivered — caused by invalid number, blocked contact, or marketing frequency cap.  
  
* * *

Frequently Asked QuestionsCommon questions about error 131053  
---  
Q: My image is a JPEG but I am still getting error 131053 — why?The file extension does not always match the actual encoding. A file saved as `.jpg` could internally be encoded as WebP or another format. Check the `error_data.details` field for the exact MIME type that was detected. Re-export the file from an image editor as JPEG to ensure it is correctly encoded.  
---  
Q: Can I send GIF animations on WhatsApp Business API?No. Animated GIFs are not supported by the WhatsApp Business API. If you need to send an animation, convert it to a short **MP4 video** using H.264 and AAC codecs. WhatsApp will play it inline in the conversation.  
---  
Q: My video is under 16 MB and in MP4 format — why is it still failing?MP4 is the correct container but the video must also use the correct codecs: **H.264 for video** and **AAC for audio**. Many MP4 files use H.265 (HEVC) or other codecs that WhatsApp does not support. Use HandBrake or ffmpeg to re-encode the video with H.264 + AAC to ensure compatibility.  
---  
Q: Can I send WebP images on WhatsApp Business API?Yes, but **only as Stickers**. WebP files sent as regular image messages will always return error 131053. If you want to send a WebP image as a regular image, convert it to JPEG or PNG first. If you want to send it as a sticker, it must be exactly 512x512 pixels, have a transparent background, and be under 100 KB.  
---  
Q: What is the difference between error 131052 and error 131053?**Error 131052** (Media Download Error) occurs when WhatsApp cannot download media from a URL you provided — the URL may be broken, slow, or inaccessible. **Error 131053** (Media Upload Error) occurs when WhatsApp can access the file but cannot process or upload it — usually due to an unsupported format, incorrect codec, or corrupted file.  
---  
Quick SummaryError 131053 means WhatsApp could not upload the media file. Start by checking the `error_data.details` field for the exact reason. Most cases are caused by an unsupported format, wrong codec, or file exceeding the size limit. Convert images to JPEG or PNG, videos to MP4 with H.264 and AAC, and keep files well under the size limits. If using URLs, ensure they are HTTPS, publicly accessible, and end with the correct file extension.  
---

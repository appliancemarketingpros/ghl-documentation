# Expanded File Type Support in HighLevel Media Library

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008425-expanded-file-type-support-in-highlevel-media-library](https://help.gohighlevel.com/support/solutions/articles/155000008425-expanded-file-type-support-in-highlevel-media-library)  
**Category:** Media Storage  
**Folder:** Getting Started w/ Media Storage

---

Media Library

# Expanded File Type Support in HighLevel Media Library

Upload RAW photos, design source files, CAD models, audio projects, databases, and 60+ additional file formats with improved validation and error reporting.

What You'll Learn

HighLevel's Media Library accepts a significantly wider range of file types, including professional photography RAW formats, design project files, 3D models, audio production projects, database files, and specialized document formats.

This article covers all newly supported formats, explains improved upload validation and error reporting, and provides guidance for managing files that browsers cannot preview natively.

Table of Contents

1

What is Expanded File Type Support?

2

Key Benefits

3

Supported File Categories

4

Understanding File Previews

5

Upload Validation Improvements

6

Frequently Asked Questions

1

## What is Expanded File Type Support?

Expanded File Type Support is a comprehensive upgrade to HighLevel's Media Library upload system that accepts more than 60 additional file formats across professional photography, design, motion graphics, audio production, CAD/3D modeling, database management, and specialized document categories.

Previously, the Media Library accepted a limited catalog of common image formats, basic documents (PDF, Office files), MP4-family video, MP3-family audio, and ZIP archives. Any file outside this list was rejected with a generic "File type not allowed" error, even when the file was legitimate and useful for your business workflows.

This enhancement eliminates those restrictions while maintaining security and performance standards. All previously supported file types continue to work unchanged, and the system includes improved error reporting, format-specific validation, and a unified preview experience for files that browsers cannot render natively.

2

## Key Benefits

Expanded file type support brings professional-grade flexibility to HighLevel's Media Library, enabling you to centralize more of your client assets and project files within the platform.

**Professional Photography Workflows** — Upload RAW camera files (CR2, NEF, ARW, DNG) from Canon, Nikon, Sony, and other professional cameras, plus HEIF format from newer iPhones and high-end devices.

**Design Source Files** — Store Adobe InDesign projects (INDD, IDML), CorelDRAW files (CDR), Photoshop documents (PSD, PSB), Apple Keynote presentations, and OpenDocument formats (ODT, ODS, ODP) for complete asset management.

**Motion Graphics & Audio Production** — Upload project files from Adobe After Effects (AEP), Adobe Premiere Pro (PRPROJ), Sony Vegas (VEG), Ableton Live (ALS), FL Studio (FLP), and Logic Pro (LOGICX).

**CAD & 3D Modeling** — Store AutoCAD files (DWG, DXF) and 3D model formats (OBJ, FBX, STL) for architecture, engineering, product design, and manufacturing workflows.

**Database & Data Files** — Upload Microsoft Access databases (MDB, ACCDB), SQLite files, SQL scripts, calendar data (ICS), and LDAP directory files (LDIF).

**Additional Video & Audio Formats** — Support for Flash Video (FLV), Matroska (MKV), AVCHD (MTS, M2TS), 3GPP mobile video, AAC audio, FLAC lossless audio, and RealAudio formats.

**Clearer Error Messages** — Specific rejection reasons replace generic "File type not allowed" errors, and the upload interface no longer gets stuck when disallowed files are selected.

3

## Supported File Categories

The Media Library organizes newly supported file types into seven major categories. Each format receives a unique icon and consistent handling for storage, organization, and preview.

Category 1

RAW & Advanced Photo Formats

**RAW Camera Files:** CR2 (Canon), NEF (Nikon), ARW (Sony), DNG (Adobe universal RAW)

**High-Efficiency Formats:** HEIF (High Efficiency Image Format from iPhone 7+ and other modern devices)

**Additional Formats:** BMP (bitmap), SVGZ (compressed SVG), PSD (Photoshop document), PSB (large Photoshop document)

Category 2

Design & Publishing Files

**Adobe InDesign:** INDD (project file), IDML (InDesign Markup Language for compatibility)

**CorelDRAW:** CDR (vector graphics)

**Apple Keynote:** Keynote presentation files

**OpenDocument Formats:** ODT (text), ODS (spreadsheet), ODP (presentation)

**eBook & Publishing:** EPUB (reflowable eBook), XPS (XML Paper Specification), PPSX (PowerPoint slideshow)

Category 3

Motion Graphics & Audio Production Projects

**Adobe Creative Cloud:** AEP (After Effects project), PRPROJ (Premiere Pro project)

**Sony Vegas:** VEG (video editing project)

**Digital Audio Workstations:** ALS (Ableton Live set), FLP (FL Studio project), LOGICX (Logic Pro project)

Category 4

CAD & 3D Modeling Files

**AutoCAD:** DWG (drawing file), DXF (Drawing Exchange Format)

**3D Model Formats:** OBJ (geometry definition), FBX (Autodesk exchange format), STL (stereolithography for 3D printing)

Category 5

Database & Data Files

**Microsoft Access:** MDB (Access 2003 and earlier), ACCDB (Access 2007 and later)

**SQLite & SQL:** SQLITE (database file), SQL (script file)

**Data Exchange:** LDIF (LDAP directory), ICS (calendar data)

Category 6

Additional Video & Audio Formats

**Video:** FLV (Flash Video), MKV (Matroska), MTS/M2TS (AVCHD from camcorders), 3GPP (mobile video)

**Audio:** AAC (Advanced Audio Coding), FLAC (lossless compression), RealAudio formats

Category 7

Fonts & Archives

**Font Files:** EOT (Embedded OpenType for legacy browsers)

**Archives:** 7z (7-Zip compressed archive)

All Formats Ready

Upload Professional Assets Without Restriction

More than 60 new file types are supported — from RAW photos to CAD files to audio production projects.

4

## Understanding File Previews

Many of the newly supported file types cannot be rendered natively in web browsers. HighLevel provides a consistent experience for these files through the "Preview not available" interface, which displays the file's icon, name, size, and format information.

This section explains which files can be previewed and which display the fallback interface.

Scenario 1

Files That Display "Preview Not Available"

**RAW Camera Files:** CR2, NEF, ARW, DNG — browsers cannot decode proprietary RAW formats from camera manufacturers.

**High-Efficiency Images:** HEIC, HEIF — newer image codecs require specialized rendering libraries not widely supported in browsers.

**Design Source Files:** PSD, PSB, INDD, IDML, CDR — these are complex project files requiring native applications to render.

**CAD Files:** DWG, DXF — AutoCAD formats require specialized CAD viewers.

**3D Models:** OBJ, FBX, STL — 3D formats require WebGL rendering engines not enabled by default in the Media Library.

**Production Project Files:** AEP, PRPROJ, VEG, ALS, FLP, LOGICX — these are proprietary application project files that only open in their native software.

**Compressed SVG:** SVGZ — while SVG is browser-native, compressed SVGZ requires extraction before rendering.

**All Audio Files:** Audio playback is not supported in the preview interface; files display metadata only.

Scenario 2

Files with Browser-Native Preview Support

Standard image formats (JPEG, PNG, GIF, WebP, SVG) display normally in the Media Library preview.

Video files with browser-supported codecs (MP4, WebM with H.264 or VP9) play inline.

PDFs render using the browser's built-in PDF viewer.

Download to View

For files that show "Preview not available," click the download button to save the file to your computer and open it in the appropriate native application (Adobe Creative Cloud, AutoCAD, Ableton Live, etc.).

5

## Upload Validation Improvements

In addition to accepting more file types, the upload validation system received significant enhancements to handle edge cases and provide clearer feedback.

Improvement 1

Extension-Based MIME Inference

Browsers sometimes report ambiguous MIME types (for example, "application/octet-stream" for unrecognized files). The system now cross-references the file extension with a comprehensive mapping table to infer the correct MIME type and validate the file properly. This prevents legitimate files from being incorrectly rejected due to browser metadata inconsistencies.

Improvement 2

Multi-Candidate MIME Resolution

Some file extensions can represent multiple content types (for example, .webm can be video or audio). The system checks all valid MIME candidates for a given extension and accepts the file if any candidate matches an allowed type. This ensures formats with overlapping extensions are handled correctly.

Improvement 3

Dynamic Size Limits by Content Type

The previous flat file size limit applied uniformly to all uploads. The system now enforces content-specific size limits (for example, video files may have different limits than documents or images). This provides more appropriate constraints based on the type of asset being uploaded.

Improvement 4

Specific Rejection Reasons

When an upload is rejected, the error message specifies why the file was blocked (for example, "File type not supported," "File size exceeds 50MB limit for videos," or "File extension does not match content type"). This eliminates guesswork and helps you address validation issues quickly.

Improvement 5

Stuck Spinner Fix

Previously, selecting a disallowed file type sometimes caused the upload interface to display an endless spinner without resolving to an error state. Rejected uploads now display an error message immediately and provide a close button to clear the failed upload from the queue.

Clearer Feedback

These validation improvements ensure that legitimate files are accepted reliably and that errors provide actionable information rather than generic failure messages.

6

## Frequently Asked Questions

Q: Do I need to enable any settings to use the new file types?

No. All newly supported file types are automatically enabled for all HighLevel accounts. Simply upload files with the supported extensions, and the system accepts them.

Q: Will my existing uploaded files be affected?

No. All existing files in your Media Library remain unchanged and continue to function exactly as before. This is an additive update that does not modify, migrate, or alter previously uploaded content.

Q: Can I preview RAW photo files in the Media Library?

No. RAW camera files (CR2, NEF, ARW, DNG) cannot be rendered natively in web browsers. When you click on a RAW file, the Media Library displays a "Preview not available" screen with the file's metadata. To view the file, download it and open it in a photo editing application such as Adobe Lightroom or Photoshop.

Q: What are the file size limits for newly supported formats?

File size limits vary by content type. Videos typically have higher limits than documents or images. If you attempt to upload a file that exceeds the size limit for its type, the system displays a specific error message indicating the maximum allowed size.

Q: Can I use these files in email campaigns or workflows?

Yes. Once uploaded, all files in the Media Library can be referenced in workflows, email campaigns, and other HighLevel features exactly the same way as traditional image and document files. For example, you can attach a PDF or database file to an email, or reference a design file in a workflow action.

Q: Why does my file show "Preview not available" instead of rendering?

Browsers can only render a limited set of file formats natively (standard images, video with supported codecs, PDFs, and some document types). Files like RAW photos, CAD drawings, 3D models, and production project files require specialized software to open. The "Preview not available" screen confirms that your file uploaded successfully and provides metadata; you can download the file to view it in the appropriate application.

Q: Are there any file types still not supported?

Yes. The Media Library does not accept executable files (.exe, .app, .bat, .sh), system files, or formats that pose security risks. If you attempt to upload an unsupported file type, the system displays a specific error message indicating why the file was rejected.

Q: What happens if the browser reports an incorrect MIME type for my file?

The upload validation system uses extension-based MIME inference when the browser sends an ambiguous or incorrect content type (such as "application/octet-stream"). The system cross-references your file's extension with a comprehensive mapping table to determine the correct MIME type and validate it properly. This prevents legitimate files from being incorrectly rejected due to browser metadata issues.

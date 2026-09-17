# How to Access and Manage Media Storage Using Ask AI

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008357-how-to-access-and-manage-media-storage-using-ask-ai](https://help.gohighlevel.com/support/solutions/articles/155000008357-how-to-access-and-manage-media-storage-using-ask-ai)  
**Category:** AI Employee  
**Folder:** Ask AI

---

Media Library & AI

# Media Storage × AskAI Integration

Manage your media library, Google Drive, and Canva files through natural-language conversations in AskAI.

What You'll Learn

Media Storage capabilities are available within AskAI, enabling you to browse, organize, and manage your media library—including connected Google Drive and Canva accounts—using conversational commands.

This article explains how to use AskAI to perform media workflows, what operations are supported, and how approval-based safeguards keep you in control of every change.

Table of Contents

1

What is Media Storage × AskAI Integration?

2

Key Benefits

3

Media Library Capabilities

4

Google Drive Integration

5

Canva Integration

6

User Control and Safeguards

7

How to Use AskAI for Media Storage

8

Frequently Asked Questions

1

## What is Media Storage × AskAI Integration?

Media Storage × AskAI Integration brings media library management into HighLevel's AI assistant. You can browse, organize, and act on files, folders, Google Drive contents, and Canva designs through natural-language conversations.

Instead of navigating through the media library interface, you describe what you want to do—move files, create folders, check storage usage, export Canva designs—and AskAI guides you through the workflow, requesting approval before making any changes.

This integration represents the first phase of Media Storage's AI journey, making existing product capabilities available as AskAI skills and laying the foundation for richer media workflows.

2

## Key Benefits

The Media Storage × AskAI Integration delivers conversational control over your media assets with built-in safeguards.

**Faster media housekeeping** — Find, organize, move, and clean up files through a conversation instead of navigating the media library interface.

**Storage visibility on demand** — Ask what's consuming storage without opening a usage view.

**Connected sources in one place** — Reach Google Drive and Canva from the same conversation as your own media.

**Safer execution** — Approval-based writes and trash-only deletes keep you in control of every action.

**Foundation for richer media workflows** — This integration establishes the infrastructure for advanced AI-powered media operations in future releases.

3

## Media Library Capabilities

AskAI provides comprehensive control over your HighLevel media library through conversational commands.

Capability 1

Browse and Organize Files

List and filter files and folders in your media library. Create new folders, rename files and folders, and update their details. Move files and folders into target folders. Find a specific file by its media URL or ID and view its folder path.

Capability 2

Import Files from External URLs

Import a file into your media library from an external URL. AskAI validates the URL server-side before importing the file.

Capability 3

Trash and Restore

Move a single file or folder to trash, or move multiple files and folders to trash in one request. Restore previously trashed items. All deletion is recoverable—permanent deletion is not available through AskAI.

Capability 4

Understand Storage Usage

Ask for the total media storage consumed by your sub-account or request storage usage broken down by group or category.

Capability 5

Browse Stock Assets

List the background and texture assets available to your sub-account.

Note

Deletion always moves items to trash and requires confirmation. Files are never permanently erased through AskAI.

4

## Google Drive Integration

When Google Drive is connected as a media-storage source, AskAI can manage Drive files and folders directly. AskAI retrieves the Drive connection automatically—you never need to look up connection IDs manually.

Capability 1

Check Connection Status

Verify whether Google Drive is connected as a media-storage source for your sub-account. Retrieve the connected Drive account details and storage quota.

Capability 2

List and Filter Drive Files

List files in your connected Google Drive with optional folder, search, or file-type filters. List Drive folders separately.

Capability 3

Create Drive Folders

Create a new folder in your connected Google Drive directly through AskAI.

Note

Uploading local files directly to Google Drive through AskAI and downloading Drive files through AskAI are not supported. URL-based import into the media library is available instead.

5

## Canva Integration

When Canva is connected to your sub-account, AskAI can list designs, create new designs, upload media assets to Canva, and export designs in available formats.

Capability 1

Check Connection and User Details

Verify whether Canva is connected and identify the connected Canva user.

Capability 2

List and Review Designs

List Canva designs and open a design's details and edit link. Review a design's pages and its available export formats.

Capability 3

Create New Designs

Create a new Canva design directly from AskAI.

Capability 4

Upload Media Assets

Upload a media file into Canva as an asset and check the upload's status.

Capability 5

Export Designs

Export a Canva design in an available format and retrieve the exported file once the export completes.

Safe by Design

Every Action Requires Your Approval

AskAI never makes irreversible changes to your media. All write operations—create, rename, move, trash, restore, import, and Canva actions—require explicit confirmation before they run.

6

## User Control and Safeguards

AskAI is designed to assist you without taking irreversible action on your media. Multiple safeguards ensure you remain in control at every step.

**Approval-based writes** — Every change—create, rename, move, trash, restore, import, Canva create/upload/export—is presented for explicit approval before it runs.

**Read-only listing** — Operations that only read data (listing files, checking usage, reviewing designs, browsing Drive contents) run directly and change nothing.

**Trash-only deletion** — Deletion is always recoverable. Permanent deletion is not reachable through AskAI.

**Connection validation** — Canva and Google Drive actions require that the integration is connected for your sub-account. If it isn't, AskAI prompts you to connect it rather than guessing.

**No invented IDs** — AskAI never invents a file, folder, design, or connection ID. It looks up the value first or asks you to provide it.

**Server-side URL validation** — External URLs that Media Storage fetches are validated server-side before any import occurs.

**Sub-account scoping** — Every operation is scoped to your current sub-account. Existing Media Storage permissions and access rules continue to apply.

7

## How to Use AskAI for Media Storage

Using AskAI to manage media storage requires only a conversational description of your task. AskAI will request any additional details and present the proposed action for your approval.

Step 1

Open AskAI

Navigate to AskAI in your HighLevel account.

Step 2

Describe Your Media Task

Type or speak the media task you want to complete. Use natural language—for example, "Show me the files in my media library" or "Create a folder called Q3 Creatives."

Step 3

Provide Additional Details

If AskAI needs more information—such as the target folder for a move operation or a file URL for import—it will ask follow-up questions.

Step 4

Review the Proposed Action

AskAI will present the action it plans to execute. Review the details carefully.

Step 5

Approve the Action

When prompted, approve the action. AskAI will execute it and confirm completion.

Example Requests

  * "Show me the files in my media library."
  * "Create a folder called Q3 Creatives."
  * "Move these images into the Q3 Creatives folder."
  * "Import this image from a URL into my media library."
  * "Restore the files I trashed."
  * "How much storage is my sub-account using?"
  * "Is my Google Drive connected to my media?"
  * "List the folders in my Google Drive."
  * "Show my Canva designs."
  * "Export this Canva design as a PNG."


8

## Frequently Asked Questions

Q: Does AskAI require me to provide file IDs or connection IDs?

No. AskAI retrieves connection details automatically and looks up file, folder, and design IDs based on your conversational description. You never need to provide technical identifiers manually.

Q: Can I permanently delete files through AskAI?

No. All deletion through AskAI is trash-only and recoverable. Permanent deletion is not available through AskAI to prevent irreversible data loss.

Q: What happens if I ask AskAI to work with Google Drive or Canva but I haven't connected them?

AskAI will inform you that the integration is not connected and prompt you to connect it. It will not attempt to guess or proceed without a valid connection.

Q: Can I upload files from my computer to Google Drive through AskAI?

No. Uploading local files directly to Google Drive through AskAI and downloading Drive files through AskAI are not supported in this release. URL-based import into your media library and Canva is available instead.

Q: Do I need to approve every action AskAI performs?

You need to approve all write operations—create, rename, move, trash, restore, import, and Canva actions. Read-only operations such as listing files, checking usage, or reviewing designs run directly without approval because they make no changes.

Q: Will AskAI show storage usage for my entire agency or just my sub-account?

AskAI shows storage usage for your current sub-account. Agency-level storage breakdown is not included in this release.

Q: Can AskAI move files between my media library and Google Drive?

Not directly. AskAI can list and create folders in Google Drive and import files from external URLs into your media library. Moving files between the two systems is not supported in this release.

Q: Does this integration change existing Media Storage permissions?

No. All operations performed through AskAI are scoped to your current sub-account and respect existing Media Storage permissions and access rules.

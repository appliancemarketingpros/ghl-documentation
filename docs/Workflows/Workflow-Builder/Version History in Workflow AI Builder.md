# Version History in Workflow AI Builder

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008368-version-history-in-workflow-ai-builder](https://help.gohighlevel.com/support/solutions/articles/155000008368-version-history-in-workflow-ai-builder)  
**Category:** Workflows  
**Folder:** Workflow Builder

---

Workflow Automation

# Version History in Workflow AI Builder

Track and restore every AI-generated workflow iteration with artifact cards that preserve your entire build history.

What You'll Learn

The Workflow AI Builder tracks every iteration it creates. Each AI build or edit produces an artifact card in the chat, allowing you to restore any previous version in one click.

This article explains how artifact cards work, how to restore versions, and how version history integrates with the existing Version History tab to create a unified timeline of all workflow changes.

Table of Contents

1

What is Version History in AI Builder?

2

Key Benefits

3

How Artifact Cards Work

4

How to Use Version History in AI Builder

5

Understanding Unsaved Indicators

6

Integration with Version History Tab

7

Frequently Asked Questions

8

Related Articles

Video Walkthrough

  


1

## What is Version History in AI Builder?

Version History in AI Builder preserves every iteration the AI Assistant creates when building or editing workflows. Each change generates an artifact card that appears inline in the chat conversation, creating a complete timeline of all AI-generated modifications.

These artifact cards allow you to restore any previous version with a single click, eliminating the need to manually rebuild workflows when an AI edit removes a trigger, overwrites an action configuration, or makes unwanted changes. All iterations remain accessible and restorable, creating a bidirectional and non-destructive version control system.

The feature integrates with the existing Version History tab, creating a unified timeline where AI-generated versions and manual edits appear together as a single source of truth for version numbering.

2

## Key Benefits

Version History in AI Builder transforms how you work with AI-generated workflows by providing safety, flexibility, and confidence when experimenting with changes.

**One-Click Recovery** — Restore any previous iteration instantly when an AI edit removes triggers, overwrites action configurations, or makes unwanted changes. No manual rebuilding required.

**Seamless Workflow** — Restore versions without leaving the AI Assistant or breaking your conversation flow. Continue working immediately after reverting changes.

**Safe Experimentation** — Try bold edits and aggressive changes with confidence. Compare results, then roll back instantly if the iteration misses the mark.

**Non-Destructive Versioning** — Restoring older iterations preserves newer ones. Jump back and forth freely between versions without destroying any iteration.

**Complete Transparency** — Visual indicators show which version currently matches your canvas, and which versions remain unsaved when auto-save is disabled.

3

## How Artifact Cards Work

Artifact cards provide visual representation and control for each AI-generated workflow iteration. Understanding their components helps you navigate version history efficiently.

Component 1

Artifact Card Generation

Every build or edit from the AI Assistant produces an artifact card that appears inline in the chat, positioned exactly where the change occurred in your conversation. This creates a chronological timeline of all AI-generated modifications.

Component 2

Current Version Indicator

The artifact card matching your current canvas displays a purple border. This visual marker ensures you always know which iteration you are viewing, even when multiple versions exist in the chat history.

Component 3

Restore Controls

Each artifact card includes a three-dot menu with "Restore this version" as an option. Selecting this option reverts your canvas to that iteration instantly. The purple border moves to the restored card, and the previously current card gains restore controls.

Component 4

Bidirectional Navigation

Restoring an older iteration keeps newer versions restorable. You can jump back and forth between any iterations without destroying them. No version is ever permanently deleted through the restore process.

[Screenshot: Artifact cards in chat showing purple border on current version and three-dot menu with restore option on previous versions]

Workflow Tip

Experiment Without Fear

Version history lets you try aggressive AI edits with complete safety. Test bold changes, compare results, and revert instantly if needed.

4

## How to Use Version History in AI Builder

Follow these steps to track, compare, and restore AI-generated workflow iterations using artifact cards.

Step 1

Prompt the AI Assistant

Open the Workflow AI Builder and prompt the AI Assistant to build or edit your workflow. The AI generates the workflow based on your prompt.

Step 2

View the First Artifact Card

An artifact card appears in the chat immediately after the AI completes the build. This card displays a purple border, indicating it matches your current canvas.

Step 3

Make Additional Changes

Prompt the AI to make another change to your workflow. The AI generates a new iteration and creates a second artifact card in the chat.

Step 4

Track Current Version

The purple border moves to the newest artifact card. The previous card no longer shows the purple border but remains visible in your chat history.

Step 5

Restore a Previous Version

Click the three-dot menu on any older artifact card and select "Restore this version." The canvas reverts to that iteration instantly. The purple border moves to the restored card.

Pro Tip

You can restore versions multiple times in any order. Newer iterations remain accessible even after restoring older ones, allowing you to compare different approaches freely.

5

## Understanding Unsaved Indicators

When auto-save is disabled for your location, artifact cards display an "Unsaved" pill to indicate which versions have not been saved manually. This indicator helps you track which iterations exist only in memory.

The unsaved indicator only appears when auto-save is turned off. When auto-save is enabled, all iterations are saved automatically and the indicator never appears on artifact cards.

Important

If you see an "Unsaved" pill on an artifact card, manually save the workflow before navigating away to preserve that iteration. Unsaved versions will be lost if you leave the workflow without saving.

[Screenshot: Artifact card showing "Unsaved" pill when auto-save is disabled]

6

## Integration with Version History Tab

Artifact cards in the AI Builder sync with the Version History tab, creating a unified timeline where AI-generated versions and manual edits appear together. The Version History tab remains the single source of truth for version numbering.

Each artifact card includes a "Show in version history" option in its three-dot menu. Selecting this option opens the Version History tab and highlights the corresponding entry, allowing you to view the full context of both AI and manual changes.

Unified Timeline

All workflow versions—whether created by the AI Assistant or manual edits—appear in chronological order in the Version History tab. This provides complete visibility into your workflow's evolution.

[Screenshot: Version History tab showing both AI-generated and manual versions in unified timeline]

7

## Frequently Asked Questions

Q: What happens to newer versions when I restore an older iteration?

Newer versions remain fully accessible and restorable. Restoring an older iteration does not delete or destroy any newer versions. You can jump back and forth between any iterations without losing work.

Q: Do artifact cards appear for manual edits I make to the workflow?

No. Artifact cards only appear for builds and edits generated by the AI Assistant. Manual edits you make directly to the workflow canvas do not create artifact cards in the chat, but they do appear in the Version History tab.

Q: How do I know which version is currently on my canvas?

The artifact card matching your current canvas displays a purple border. This visual indicator updates automatically whenever you restore a different version or the AI generates a new iteration.

Q: What does the "Unsaved" pill mean on an artifact card?

The "Unsaved" pill appears when auto-save is disabled for your location and indicates the version has not been saved manually. You must save the workflow manually to preserve that iteration. This indicator never appears when auto-save is enabled.

Q: Can I restore a version from the Version History tab instead of using artifact cards?

Yes. The Version History tab displays all workflow versions, including AI-generated iterations. You can restore any version from the Version History tab using the standard restore controls. The artifact card's "Show in version history" option takes you directly to that version in the tab.

Q: How many artifact cards can appear in a single AI Builder conversation?

There is no limit to the number of artifact cards that can appear in a conversation. Every AI build or edit generates a new card, creating a complete timeline of all AI-generated changes for that workflow.

Q: Do I need to manually save after restoring a version?

Only if auto-save is disabled for your location. When auto-save is enabled, restored versions are saved automatically. When auto-save is disabled, you must save manually to preserve the restored version.

Q: Can I delete artifact cards from the chat history?

No. Artifact cards are permanent parts of the conversation history and cannot be deleted. They provide a complete record of all AI-generated iterations for reference and restoration.

8

## Related Articles

Explore these resources to learn more about workflow automation and AI Builder features in HighLevel.

[Workflow AI Builder](<https://help.gohighlevel.com/support/solutions/articles/155000006100-workflow-ai-builder>)

[Workflow Notes, Action Notes & Sticky Notes](<https://help.gohighlevel.com/support/solutions/articles/155000003914-workflow-notes-action-notes-sticky-notes>)

[Workflow AI Assistant](<https://help.gohighlevel.com/support/solutions/articles/155000003970-workflow-ai-assistant>)

[Workflow Builder: Learn More Using AI](<https://help.gohighlevel.com/support/solutions/articles/155000005631-workflow-builder-learn-more-using-ai>)

# Entrance Animations for Sections, Rows & Columns

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008330-entrance-animations-for-sections-rows-columns](https://help.gohighlevel.com/support/solutions/articles/155000008330-entrance-animations-for-sections-rows-columns)  
**Category:** Sites  
**Folder:** Funnels and Websites

---

Funnels & Websites

# Entrance Animations for Sections, Rows & Columns

Animate entire layout blocks with automatic sequencing, dozens of entrance effects, and granular control over timing, easing, and mobile behavior.

What You'll Learn

This article explains how to apply entrance animations to Sections, Rows, and Columns in HighLevel's page builder. You can choose from dozens of animation styles, adjust timing and easing, and let the builder sequence each block automatically as visitors scroll.

You'll learn how to preview animations before committing, control whether animations run on mobile devices, and create cohesive page reveals without calculating delays by hand.

Table of Contents

1

What Are Entrance Animations for Layout Blocks?

2

Key Benefits

3

Available Animation Categories

4

Animation Settings & Controls

5

How Automatic Sequencing Works

6

How to Apply Entrance Animations

7

Mobile Animation Controls

8

Related Articles

9

Frequently Asked Questions

1

## What Are Entrance Animations for Layout Blocks?

Entrance animations for Sections, Rows, and Columns let you animate entire layout blocks in the page builder. Instead of animating each element individually, you can apply a single entrance animation to a Section, Row, or Column and everything inside that block animates together.

When a visitor scrolls a block into view, the animation plays automatically. The builder sequences animations in hierarchical order—Section, then Row, then Column, then content—so each block waits for the one above it to finish before it begins. This eliminates the need to calculate delays manually and ensures your page reveals itself in a deliberate, cohesive order.

Blocks stay visible after they animate in. Content waiting to animate sits in its normal state rather than disappearing, so visitors never see blank space or flicker as they scroll.

2

## Key Benefits

Applying entrance animations to layout blocks provides several advantages over animating individual elements:

**No Manual Delay Calculations** — The builder sequences animations automatically. You never calculate delays yourself, even when you add, remove, or reorder blocks.

**Cohesive Page Reveals** — Animate entire Sections, Rows, or Columns in one step. Your page feels deliberate and professional without custom CSS.

**Scroll-Triggered Playback** — Animations fire when a block scrolls into view, so nothing plays off-screen and your page feels responsive to visitor interaction.

**Mobile Controls Per Block** — Animations are off on mobile by default. Turn them on for individual Sections, Rows, or Columns when you want the motion on phones.

**Automatic Correction on Published Pages** — Sequencing on already-published pages corrects itself when they render, with no re-save required.

3

## Available Animation Categories

HighLevel provides dozens of entrance animations organized into nine categories. Each category includes multiple directional or stylistic variations:

Fade

Fade Animations

In, Up, Down, Left, Right — blocks fade in while sliding from the specified direction.

Slide

Slide Animations

Up, Down, Left, Right — blocks slide in from off-screen in the specified direction.

Bounce

Bounce Animations

In, Up, Down, Left, Right — blocks bounce into position from the specified direction with an elastic effect.

Flip

Flip Animations

Flip, Flip In X, Flip In Y — blocks rotate around their horizontal or vertical axis.

Rotate

Rotate Animations

In — blocks rotate clockwise while fading into view.

Zoom

Zoom Animations

In — blocks scale up from a smaller size while fading into view.

Light Speed

Light Speed Animations

Left, Right — blocks slide in with a skew effect for a fast, dynamic entrance.

Infinite Loop

Infinite Loop Animations

Glow, Rocking, Bounce — blocks continuously repeat the animation after entering, ideal for call-to-action sections.

4

## Animation Settings & Controls

After selecting an entrance animation, you can adjust how the block enters using four settings:  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077504212/original/wpVV2t3QyaCLTW-g2VFV9Lmzn8HzQV48SQ.png?1785770963)  


Setting| Range| Purpose  
---|---|---  
Duration| 0.1s to 3s| How long the animation takes to complete  
Delay| 0s to 5s| How long to wait before the animation begins  
Scale| 0.5× to 2×| The size multiplier at animation start (zoom effects)  
Easing| Linear, Ease-in, Ease-out, Ease-in-out| The acceleration curve of the animation  
  
Preview Instantly

Hover any entrance animation card in the sidebar and it plays on the selected block on the canvas. Move your cursor away and the preview clears. This lets you compare options side by side before committing.

5

## How Automatic Sequencing Works

HighLevel sequences entrance animations in hierarchical order:

  1. The Section animates first.
  2. Rows inside that Section animate after the Section finishes.
  3. Columns inside each Row animate after the Row finishes.
  4. Content (elements) inside each Column animates after the Column finishes.


Each block waits for the one above it to complete before it begins. If you add a new Row between two existing Rows, the builder inserts it into the sequence automatically. If you remove a block, the sequence closes the gap. You never recalculate delays manually.

Animations trigger when a block scrolls into view. Blocks that have already animated remain visible. Content waiting its turn stays in its normal state rather than disappearing, so visitors see a smooth reveal without flicker or blank space.

Sequencing on Published Pages

Sequencing corrects itself automatically when a page renders. Existing published pages benefit from the updated sequencing logic without requiring a re-save.

Quick Summary

Animations Sequence Automatically

HighLevel sequences Sections, Rows, Columns, and content in hierarchical order. Each block waits for the one above it to finish, so you never calculate delays yourself—even when you add, remove, or reorder blocks.

6

## How to Apply Entrance Animations

Follow these steps to apply an entrance animation to a Section, Row, or Column:

Step 1

Select a Layout Block

Click a Section, Row, or Column on the canvas to select it. The block's bounding box appears with resize handles.

Step 2

Open the Animations Tab

In the right sidebar, click the **Animations** tab, then expand the **Entrance Animation** section.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077483438/original/QcQlk1o3TSVD2GqvFyhIdGACg882g7ygig.png?1785760450)

Step 3

Preview Animation Options

Hover over any entrance animation card. The animation plays immediately on the selected block on the canvas. Move your cursor away to clear the preview.

Step 4

Choose an Animation

Click the animation card you want to apply. The animation is assigned to the block and appears in the Entrance Animation section.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077483158/original/wilEsaPE24eEaoooJ9aEfBcG4q4uOrYqiA.gif?1785760276)

Step 5

Adjust Animation Settings

Tune the animation using the sliders and dropdowns:

  * **Duration** — 0.1s to 3s
  * **Delay** — 0s to 5s (adds wait time before this block animates, in addition to sequencing delay)
  * **Scale** — 0.5× to 2× (start size for zoom effects)
  * **Easing** — Linear, Ease-in, Ease-out, Ease-in-out  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077483354/original/2nOnf_kmiKS_aq2ljP8Udh573Ezy2jAQAA.gif?1785760402)


Step 6

Save and Publish

Click **Save** in the top-right corner of the page builder, then publish the page. The animation plays on the live page when a visitor scrolls the block into view.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077483628/original/fVQ5ZhMPTF3eJ4AmqWz12RKNNyn_rVSSYg.png?1785760520)

  


7

## Mobile Animation Controls

Entrance animations are disabled on mobile devices by default. This keeps mobile pages fast and eliminates motion that can slow down phones or distract mobile visitors.

You can enable animations on mobile for individual Sections, Rows, or Columns using the **Enable animations on mobile** toggle in the Animations tab. When you turn this toggle on, the block animates on mobile devices. When you leave it off, the block appears immediately without animation on mobile.

The builder re-sequences animations on mobile around blocks that have the toggle disabled. If a Section is set to animate on mobile but the Row inside it is not, the Row appears immediately and the next block in the hierarchy waits for the Section to finish before it begins. This ensures the order stays correct across devices.

Note

The mobile toggle is per block. You can enable animations on mobile for high-priority Sections and leave them off for others, giving you fine-grained control over mobile performance and user experience.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155077482841/original/XGKZWQxyliYbC3ii4PxLK-vBzxehY9IjJw.png?1785760119)

8

## Related Articles

  * [How to Use Sections, Rows, and Columns in the Page Builder](<https://help.gohighlevel.com/en/support/solutions/articles/155000005513>)
  * [Animating Individual Elements in Funnels and Websites](<https://help.gohighlevel.com/en/support/solutions/articles/155000005657>)
  * [Using Saved Element Templates in the Page Builder 9](<https://help.gohighlevel.com/en/support/solutions/articles/155000006457>)


## Frequently Asked Questions

Q: Can I animate individual elements inside a Section or Row?

Yes. You can apply entrance animations to Sections, Rows, Columns, and individual elements. When you animate both a parent block (like a Row) and an element inside it, the element waits for the Row to finish animating before it begins. The builder sequences everything hierarchically.

Q: What happens if I add a new Row between two existing Rows that already have animations?

The builder inserts the new Row into the animation sequence automatically. It waits for the Row above it to finish, then animates, then the Row below it begins. You don't recalculate delays manually—HighLevel handles the sequencing for you.

Q: Do animations play on already-published pages?

Yes. The sequencing logic corrects itself automatically when a page renders. Existing published pages benefit from the updated sequencing without requiring a re-save. If you previously applied animations to elements, the builder sequences them correctly alongside any new Section, Row, or Column animations.

Q: Can I preview an animation before applying it?

Yes. Hover any entrance animation card in the Animations tab and it plays on the selected block on the canvas. Move your cursor away and the preview clears. This lets you compare multiple animations side by side before choosing one.

Q: Why are animations disabled on mobile by default?

Animations on mobile can slow down phones and distract visitors. HighLevel disables them by default to keep mobile pages fast and focused. You can enable animations per block when you want motion on mobile using the Enable animations on mobile toggle.

Q: What happens to blocks that are waiting to animate?

Blocks waiting to animate sit in their normal state. They don't disappear or become invisible while waiting. This ensures visitors see the page content without blank space or flicker as they scroll.

Q: Do entrance animations work with saved element templates?

Yes. When you drop a saved element template into a Section, Row, or Column that has an entrance animation, the element sequences correctly with the parent block. The element waits for its parent to finish animating before it begins.

Q: Can I use different animations for Sections, Rows, and Columns on the same page?

Yes. Each Section, Row, and Column can have its own entrance animation, duration, delay, scale, and easing. The builder sequences them hierarchically regardless of which animation you choose for each block. This gives you maximum creative control over how your page reveals itself.

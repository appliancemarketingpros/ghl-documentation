# WhatsApp Template Error: “body: Parameter at index contains URL”

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006052-whatsapp-template-error-body-parameter-at-index-contains-url-](https://help.gohighlevel.com/support/solutions/articles/155000006052-whatsapp-template-error-body-parameter-at-index-contains-url-)  
**Category:** Reselling Products  
**Folder:** WhatsApp

---

# WhatsApp Template Error: "body: Parameter at index contains URL"

Why this happens, and two ways to fix it.

## What This Means

Your message template was approved **without** a URL inside the body's variable(s), but at send time you're putting a **URL inside a body parameter** (e.g., `{{1}}`). For anti-phishing and quality reasons, **Meta does not allow full URLs inside body placeholders**. Links must be part of the template itself or placed in **buttons** (with optional dynamic suffixes).

![URL in body parameter error](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155051772003/original/KEPgYVPEZhXjVxYEcMTTet1OnBTAXJDUHg.png?1755499219)

## Why It Happens

  * You're passing text like `https://example.com/deal/123` into a variable `{{1}}`.
  * The template's body was approved as plain text (variables expected to be names, codes, dates — not links).
  * You used a URL shortener in a variable (many are blocked in parameters).
  * You need a **URL button** instead of a body variable.


## How to Fix It (Choose One)

Option A — Make the Link Static in the Body

Use a template where the **full URL** is written directly in the approved body (no variable).

Example body

"Hi {{1}}, please review your offer: https://example.com/offers"

**When to use:** The link is the same for everyone.

Option B — Use a CTA Website Button

Create/modify the template to include a **Call-to-Action (CTA) Website button** :

  * **Button URL (base):** `https://example.com/order/`
  * **Button text:** "View Order"


**When to use:** The URL needs a unique, per-recipient suffix (e.g., an order or contact ID) — the base URL is approved once, and only the dynamic suffix is filled in at send time.

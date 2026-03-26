# PDF Generation for Invoices and Receipts

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005216-pdf-generation-for-invoices-and-receipts](https://help.gohighlevel.com/support/solutions/articles/155000005216-pdf-generation-for-invoices-and-receipts)  
**Category:** Payments  
**Folder:** Invoices & Estimates

---

This article outlines the recent upgrade to the PDF generation pipeline for invoices and receipts in HighLevel. This update enhances performance, eliminates timeouts, and reduces support overhead, resulting in a faster and more reliable user experience across all PDF-related workflows.

**TABLE OF CONTENTS**

  * What is the PDF Generation Pipeline?
  * Key Benefits of the PDF Pipeline
  * How To Experience the New PDF Engine
  * Performance Comparison
  * Frequently Asked Questions


  


* * *

## What is the PDF Generation Pipeline?

The PDF generation pipeline is the system responsible for producing downloadable and email-ready PDF documents for invoices and receipts. It powers user actions such as downloading an invoice directly from the interface or triggering receipt delivery through automated workflows.

This pipeline is essential for ensuring end customers receive timely and accurate documentation of their payments and billing.

  


## Key Benefits of the PDF Pipeline

The re-engineered pipeline delivers substantial improvements in speed, reliability, and customer satisfaction. These enhancements directly impact both manual downloads and automated email workflows involving invoices and receipts.

  * Average PDF generation time reduced by approximately 80%  
  


  * P95 latency reduced by 75%, ensuring a faster response even in higher-load scenarios  
  


  * Timeout-related failures have been completely eliminated in production  
  


  * All invoice and receipt workflows now complete more quickly and reliably  
  


  * Reduction in support tickets related to failed or missing PDFs  
  


  * Increased customer trust and satisfaction due to near-instantaneous document delivery  
  


## How To Experience the New PDF Engine

Users do not need to take any manual action to take advantage of the updated PDF pipeline. The improvements have been rolled out across the platform and are already in effect for all relevant use cases.

  * All invoice and receipt downloads initiated through the interface are now significantly faster.  
  


  * Automated workflows that email receipts or invoices to contacts now complete without timeout errors.  
  


  * No configuration changes or updates are required from users.  
  


## Performance Comparison

The following table summarizes the performance improvements resulting from the new PDF generation pipeline:

Metric| Before| After| Improvement  
---|---|---|---  
Average Generation Time| ~14.8 seconds| 2.97 seconds| 80% faster  
P95 Latency| ~19.5 seconds| 4.8 seconds| 75% faster  
Timeout Failures| ~1%| 0%| 100% reliability  
  
##   


* * *

## Frequently Asked Questions

Q: Do I need to enable or configure anything to use the improved pipeline?  
No. The new pipeline is already active and applies to all workflows and downloads involving invoice and receipt PDFs.

Q: What if a PDF fails to generate or is delayed?  
Since the rollout, timeout-related issues have been eliminated. Any new issues may be unrelated and should be reported to support for further investigation.

Q: Are existing workflows automatically upgraded?  
Yes. Any workflow that includes invoice or receipt PDF generation or email actions will automatically benefit from the performance improvements.

Q: Can I observe the difference in performance?  
Yes. Users are encouraged to manually download an invoice or trigger a receipt email via workflow to experience the improved speed.

Q: Will this change affect other document types?  
This update specifically applies to invoice and receipt PDFs. Other document types are not affected by this release.

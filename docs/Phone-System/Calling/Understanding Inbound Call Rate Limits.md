# Understanding Inbound Call Rate Limits

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005314-understanding-inbound-call-rate-limits](https://help.gohighlevel.com/support/solutions/articles/155000005314-understanding-inbound-call-rate-limits)  
**Category:** Phone System  
**Folder:** Calling

---

Phone System

Understanding Inbound Call Rate Limits

Learn how inbound call rate limits apply to IVR, Voice AI, and regular phone numbers, how simultaneous calls are treated, and what happens when a rate-limit violation occurs.

Overview

HighLevel applies inbound call rate limits to help protect voice infrastructure from abusive, automated, or unusually high call patterns while keeping legitimate calls available.

The applicable threshold depends on whether a phone number is connected to an IVR, connected to Voice AI, or using standard inbound call routing.

These limits are measured using documented call-rate thresholds rather than a universal concurrent-call limit, making it important to distinguish call volume from the number of calls that happen to arrive at the same time.

Important

**Inbound and outbound Voice AI limits are different.** The thresholds in this article apply to inbound phone calls. Do not use outbound Voice AI calling limits or Voice AI Chat Widget concurrency limits when evaluating phone-number-based inbound Voice AI traffic.

Table of Contents

What is HighLevel Inbound Call Rate Limiting? Key Benefits of Understanding Inbound Call Rate Limits How Inbound Call Rate Limits Are Measured Concurrent Inbound Calls and Voice AI Inbound Call Rate Limit Reference What Happens When a Limit Is Exceeded? How to Set Up Routing for High Inbound Call Volume Best Practices for High Inbound Call Volume Frequently Asked Questions Related Articles

# **What is HighLevel Inbound Call Rate Limiting?**  
  


Inbound call rate limiting controls how frequently calls can arrive from or be directed to specific phone numbers before HighLevel identifies the traffic as potentially abusive or excessive. The thresholds vary based on the type of inbound call handling configured for the number.

A rate limit is not the same thing as a concurrency limit. Rate limits measure call volume over a period of time, while concurrency describes how many calls are active at the same moment.

## **Key Benefits of Understanding Inbound Call Rate Limits**  
  


Knowing which threshold applies to each phone number helps you plan call routing, prepare for high-volume events, and distinguish legitimate simultaneous traffic from patterns that may trigger abuse protections.

  * **Traffic Planning:** Understand how much inbound traffic different routing types can accept before a documented rate threshold is exceeded.
  * **Voice AI Clarity:** Separate phone-based Voice AI rate limits from unrelated browser-widget or outbound Voice AI limits.
  * **Abuse Protection:** Reduce the risk that repeated automated or spam calls trigger account-level safeguards.
  * **Better Routing:** Choose IVR, Voice AI, or standard live-answer routing based on your expected call pattern.
  * **Faster Recovery:** Know when a blocked call is an individual violation and when Support assistance is required.


## **How Inbound Call Rate Limits Are Measured**  
  


HighLevel's documented inbound protections evaluate call volume based on the originating caller number and the destination phone number. Understanding the difference helps identify whether traffic is concentrated from one caller or concentrated on one business number.

Measurement| What It Represents| Example  
---|---|---  
**From a number**|  Calls originating from the same caller phone number.| One external number repeatedly calling your business numbers.  
**To a number**|  Calls arriving at the same HighLevel phone number.| Many different callers contacting the same business line.  
**Violation cap**|  The number of rate-limit violations recorded within an hour.| More than five violations can trigger an account-wide inbound call block.  
  
**Threshold wording matters:** A limit written as **> 200 calls per minute** means the rate must exceed 200 calls per minute before that documented threshold is violated.

## **Concurrent Inbound Calls and Voice AI**

Simultaneous inbound calls are often confused with rate limiting. For phone-number-based Voice AI, HighLevel currently publishes an inbound call-rate threshold but does not publish a separate per-number, per-location, or per-agent concurrent-session ceiling in the inbound phone documentation.

Example: 10 callers reach the same Voice AI number at once

Ten calls arriving during the same minute are below the documented **> 200 calls-per-minute** threshold for a Voice AI-connected number.

However, the published HighLevel KB does not define a separate phone-based Voice AI concurrency ceiling, so this should not be interpreted as a guarantee of unlimited simultaneous sessions. Correct number assignment, call-routing mode, and Voice AI working hours must still allow the agent to answer.

Voice Experience| Published Limit| Applies Here?  
---|---|---  
**Phone-number-based Voice AI**|  Inbound rate threshold of >200 calls/minute from or to a number.| Yes  
**Voice AI Chat Widget**|  20 concurrent browser-based Voice AI calls per location.| No. This is a separate WebRTC/browser experience.  
**Outbound Voice AI**|  Uses separate outbound call-rate and daily limits.| No. Outbound rules do not define inbound capacity.  
  
## **Inbound Call Rate Limit Reference**

The routing method assigned to the phone number determines which documented threshold applies. IVR-connected numbers are excluded from these specific inbound rate-limit rules, while Voice AI and regular numbers use different call-per-minute thresholds.

Number Type| From One Number| To One Number| When Exceeded  
---|---|---|---  
**IVR-Connected**|  Not subject to these inbound rate-limit rules| Not subject to these inbound rate-limit rules| These specific rate-limit violations do not apply.  
**Voice AI-Connected**| **> 200 calls/minute**| **> 200 calls/minute**| The triggering call is blocked and one violation is recorded.  
**Regular Number**| **> 10 calls/minute**| **> 15 calls/minute**| The triggering call is blocked and one violation is recorded.  
  
**Regular number** refers to a standard inbound number that is not being handled through IVR or Voice AI for the applicable call path.

## **What Happens When a Limit Is Exceeded?**

HighLevel records a violation when a Voice AI or regular-number call exceeds the applicable rate threshold. A single violation affects the triggering call, while repeated violations can escalate into an account-wide inbound calling restriction.

Individual Rate-Limit Violation

When the applicable calls-per-minute threshold is exceeded, the current triggering call is blocked and one violation is recorded.

More Than Five Violations Within One Hour

All inbound calls for the affected account can be blocked. Contact **HighLevel Support** for assistance reviewing the traffic and restoring inbound calling.

## **How to Set Up Routing for High Inbound Call Volume**

Proper routing ensures calls reach the intended destination before you evaluate whether call volume itself is the issue. Configure the number based on whether callers should reach Voice AI immediately, try human users first, or enter an IVR workflow.

Step 1

Identify the Number's Call-Handling Type

Determine whether the number should use IVR, Voice AI, or normal team-member/forwarding routing. The applicable inbound rate threshold depends on this call path.

Step 2

Configure Voice AI Routing When AI Should Handle Calls

  1. Go to **AI Agents → Voice AI**.
  2. Open the applicable Voice AI agent.
  3. Open the **Deploy** tab.
  4. Assign the required phone number or number pool.
  5. Select **Answer calls directly** when Voice AI should answer immediately, or **Use as backup** when humans should have the first opportunity to answer.
  6. Review the agent's **Working Hours** so it is available when inbound calls are expected.  
  
  
  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080154635/original/9qw-oxHorINzLeTsi5BDcBDI8jumxCHfqg.png?1788555475)


  
For the complete configuration workflow, see [Voice AI - How to Configure Inbound Call Flow](<https://help.gohighlevel.com/support/solutions/articles/155000003431-inbound-call-flow-for-voice-ai-calls>).

Step 3

Configure Live-Answer Capacity Separately

Rate-limit capacity and human-answer capacity are different. If calls are routed to team members, make sure the correct Web App, Mobile App, phone, or VoIP Deskphone devices are enabled.

HighLevel can also ring up to **six additional team members** through the Ring More Team Members option. The first configured destination to answer takes the call.

Step 4

Use IVR When It Matches the High-Volume Call Flow

If callers should navigate a menu before reaching a person or department, build the IVR in **Automation → Workflows** and assign it to the phone number's Call Forwarding configuration. IVR-connected numbers are not subject to the specific inbound rate-limit thresholds described in this article.

Step 5

Validate Routing Before a High-Volume Event

Place normal test calls to confirm the correct destination answers. If you expect a campaign, broadcast, event, or other traffic pattern that may approach the documented thresholds, contact HighLevel Support before launch to review the expected inbound volume.

## **Best Practices for High Inbound Call Volume**

High-volume inbound calling works best when routing, staffing, AI availability, and spam protections are planned together. Rate limits are only one part of the complete inbound call path.

  * **Use the Correct Routing Type:** Choose IVR, Voice AI, or regular call routing based on the actual caller experience you need.
  * **Plan for Traffic Concentration:** A large number of calls to the same regular number can reach its destination threshold much faster than Voice AI-connected traffic.
  * **Watch Repeated Callers:** The originating-number threshold can be triggered even when calls are distributed across multiple destination numbers.
  * **Protect Voice AI From Spam:** Use available Voice AI spam-detection and blocking controls to reduce repeated unwanted calls.
  * **Do Not Mix Inbound and Outbound Limits:** Outbound Voice AI uses a separate set of rate and daily limits.
  * **Escalate Planned Traffic Spikes:** Contact HighLevel Support when expected traffic may approach the published thresholds.


## **Frequently Asked Questions**

Q: If 10 calls reach my Voice AI number at the same time, can Voice AI handle them?

Ten calls arriving during the same minute are below the documented Voice AI inbound threshold of more than 200 calls per minute from or to a number. HighLevel does not currently publish a separate phone-based Voice AI per-number, per-location, or per-agent concurrency ceiling in the inbound phone documentation, so the rate-limit threshold should not be interpreted as a guarantee of unlimited simultaneous sessions. Confirm the agent's number assignment, routing mode, and working hours before relying on it for peak traffic.

Q: Is there a published concurrent-call limit for phone-based Voice AI?

The current inbound phone documentation publishes calls-per-minute thresholds rather than a separate concurrent-session ceiling for phone-based Voice AI.

Q: Does the 20-concurrent-call Voice AI limit apply to inbound phone numbers?

No. The documented 20-concurrent-call limit applies to the **Voice AI Chat Widget** , which uses a browser-based WebRTC experience. It should not be used as the documented limit for inbound phone-number-based Voice AI.

Q: What happens when a Voice AI or regular-number rate limit is exceeded?

The call that exceeds the documented threshold is blocked and one violation is recorded. If the affected account accumulates more than five violations within one hour, inbound calls can be blocked and HighLevel Support assistance is required.

Q: Are IVR-connected numbers completely unrestricted?

IVR-connected numbers are not subject to the specific inbound rate-limit thresholds described in this article. Other routing, platform, carrier, or account rules can still apply, so this should not be interpreted as a statement that no other restrictions exist.

Q: If I spread calls across several phone numbers, will that prevent violations?

Distributing legitimate traffic can reduce concentration on a single destination number, but it does not eliminate the originating-number threshold. Repeated calls from the same external number can still trigger the applicable "from a number" limit.

Q: Are human or softphone answering limits the same as the inbound rate limit?

No. The inbound rate limit controls call traffic into HighLevel. Whether a human answers depends on your configured team members, enabled devices, simultaneous-ring settings, timeout, and user availability.

Q: Do these limits also apply to outbound Voice AI calls?

No. Outbound Voice AI calling has its own call-rate, daily, phone-number, and calling-hours rules. Use the outbound Voice AI documentation when evaluating outbound campaigns.

### **Related Articles**

[ Inbound Calls: IVR, AI, Routing & Call Flow Explained ](<https://help.gohighlevel.com/support/solutions/articles/155000007498-inbound-call-handling-ivr-ai-routing-call-flow-explained>) [ Voice AI - How to Configure Inbound Call Flow ](<https://help.gohighlevel.com/support/solutions/articles/155000003431-inbound-call-flow-for-voice-ai-calls>) [ Phone Number Edit Configuration | Incoming Call Settings ](<https://help.gohighlevel.com/support/solutions/articles/155000006881-phone-number-edit-configuration-incoming-calls-settings->) [ Voice AI Chat Widget ](<https://help.gohighlevel.com/support/solutions/articles/155000006056-how-to-use-the-voice-ai-voice-widget>) [ How to Use Smart Call Ending & Spam Protection in Voice AI ](<https://help.gohighlevel.com/support/solutions/articles/155000008622-how-to-use-smart-call-ending-spam-protection-in-voice-ai>) [ Voice AI Outbound Calling ](<https://help.gohighlevel.com/support/solutions/articles/155000006598-voice-ai-outbound-calling>)

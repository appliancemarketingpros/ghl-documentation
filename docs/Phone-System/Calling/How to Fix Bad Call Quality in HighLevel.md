# How to Fix Bad Call Quality in HighLevel

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/48000981694-how-to-fix-bad-call-quality-in-highlevel](https://help.gohighlevel.com/support/solutions/articles/48000981694-how-to-fix-bad-call-quality-in-highlevel)  
**Category:** Phone System  
**Folder:** Calling

---

Calling & Telephony

# How to Fix Bad Call Quality in HighLevel

Diagnose and resolve choppy audio, one-way calls, dropped connections, and other call-quality issues

What You'll Learn

Bad call quality shows up as choppy or robotic audio, one-way audio, echo, dropped calls, or long delays between speakers. These symptoms typically result from network instability, device configuration issues, or local setup problems.

This article walks you through a step-by-step troubleshooting process to identify and resolve call-quality issues in HighLevel.

Note

This article focuses on calls that connect but have poor or unstable audio. If calls consistently fail to connect, immediately disconnect, or show a specific error code, use the relevant call-error troubleshooting article instead.

Table of Contents

1

What is Bad Call Quality?

2

Key Benefits of Resolving Call-Quality Issues

3

How to Fix Bad Call Quality

4

Understanding Call-Quality Warnings

5

Common Symptoms and Where to Check

6

Escalating to HighLevel Support

7

Related Articles

8

Frequently Asked Questions

1

## What is Bad Call Quality?

Bad call quality refers to audio issues during a connected call. Common symptoms include:

  * Choppy, robotic, or garbled audio
  * One-way audio (you can hear them, but they can't hear you, or vice versa)
  * Echo or feedback
  * Long delays between speakers
  * Calls that drop intermittently or disconnect unexpectedly


Because HighLevel calling relies on an internet connection, network instability, device issues, or local configuration problems can affect call quality.

2

## Key Benefits of Resolving Call-Quality Issues

Fixing call-quality problems improves communication reliability and supports better customer and team experiences:

**Increased Call Reliability:** Reduce dropped calls and support smoother conversations.

**Better Customer Experience:** Help callers hear agents clearly and communicate without repeated interruptions.

**Improved Team Productivity:** Reduce time spent troubleshooting call-quality issues.

**Reduced Missed Opportunities:** Improve communication reliability during important customer conversations.

**Professional Brand Image:** Clear audio supports a more professional calling experience.

3

## How to Fix Bad Call Quality

Follow this troubleshooting process in order to identify and resolve the cause of poor call quality:

Step 1

Confirm the Issue Scope

Determine whether the issue affects one user, one device, one network, or every user in the location. This helps narrow down whether the problem is device-specific, network-specific, or broader.

Step 2

Check the Current Network

If possible, compare Wi-Fi with a wired connection or another stable network. If call quality is poor on Wi-Fi, test the same call over a wired Ethernet connection when available. A successful wired test can help identify whether the Wi-Fi network is contributing to the issue.

Step 3

Close Bandwidth-Heavy Applications

Pause streaming, backups, downloads, VPN-heavy applications, or other traffic competing with the call. Video conferencing, cloud syncing, or large file transfers can consume bandwidth and degrade call quality.

Step 4

Check the Microphone and Headset

Confirm the correct microphone and speaker are selected in your device settings or HighLevel calling interface. Test a different headset or microphone if available. Poor hardware or incorrect input/output selection can cause one-way audio or echo.

Step 5

Update and Restart the Calling Environment

Refresh the HighLevel Web App, restart your browser or mobile app, and ensure the application is current. Outdated browser or app versions can cause compatibility issues with real-time audio.

Step 6

Restart Network Equipment if Necessary

Power cycling can resolve temporary network issues. Unplug the affected network equipment (router or modem), wait about 30 seconds, reconnect it, and allow the connection to fully restore before testing another call.

Step 7

Review Call-Quality Warnings

Check for high-rtt, high-jitter, high-packet-loss, or low-mos warnings displayed during or after the call. These indicators point to specific network or connection issues. See the Understanding Call-Quality Warnings section for details.

Step 8

Test the Connection

Internet speed alone does not determine call quality. Test latency, jitter, packet loss, and connection stability in addition to upload and download speed. Tools that measure network quality (not just bandwidth) provide more accurate diagnostics.

Step 9

Review Network and Firewall Configuration if the Problem Persists

Corporate firewalls, VPNs, security software, or restrictive network policies can interfere with real-time audio. If call-quality problems occur only on a specific managed network, ask your IT team to review HighLevel's voice-network requirements. Browser extensions, VPNs, security tools, communication apps, or background software can also interfere with microphone access or network performance. Temporarily disable likely conflicts and test another call.

Step 10

Escalate to HighLevel Support

If the problem continues after completing the steps above, escalate to HighLevel Support with example calls and timestamps. See the Escalating to HighLevel Support section for the required information.

4

## Understanding Call-Quality Warnings

HighLevel displays call-quality warnings when network conditions fall below thresholds that support clear audio. These warnings help identify the underlying cause of poor call quality.

Web App Call-Quality Warnings

The Web App may display the following warnings during or after a call:  
  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155079995260/original/ql0KG04hQxAkVf9vUvtUrsbaVqGjYYT14A.jpeg?1788431600)  
  


high-rtt

High round-trip time (latency). This measures the delay in the audio path. High latency can create noticeable conversation delays.

high-jitter

Inconsistent packet arrival. Jitter measures variation in packet arrival time. Lower values generally provide more consistent audio; sustained high jitter can cause crackling or robotic sound.

high-packet-loss

Voice packets are being lost in transit. Packet loss represents voice packets that do not reach their destination. Ideally packet loss should be negligible; sustained packet loss can cause missing or choppy audio.

Mobile App Call-Quality Warnings

The Mobile App may display the following warnings during or after a call:

high-rtt

High round-trip time (latency). This measures the delay in the audio path. High latency can create noticeable conversation delays.

high-jitter

Inconsistent packet arrival. Jitter measures variation in packet arrival time. Lower values generally provide more consistent audio; sustained high jitter can cause crackling or robotic sound.

high-packet-loss

Voice packets are being lost in transit. Packet loss represents voice packets that do not reach their destination. Ideally packet loss should be negligible; sustained packet loss can cause missing or choppy audio.

low-mos

Overall call-quality score is below the expected range. MOS (Mean Opinion Score) is a composite measure of call quality. Low MOS indicates degraded audio quality from one or more factors.

5

## Common Symptoms and Where to Check

Use this table to identify which area to troubleshoot based on the symptom you are experiencing:

Symptom| Common Area to Check  
---|---  
Robotic or choppy audio| Jitter, packet loss, Wi-Fi or network congestion  
Long delay between speakers| Latency / RTT  
One-way audio| Microphone permissions, device selection, network or firewall  
Echo| Speaker/microphone setup or headset configuration  
Call drops intermittently| Network instability or packet loss  
Only one user is affected| Device, browser/app, headset, or local network  
Multiple users are affected| Shared network, router/firewall, or broader service issue  
  
6

## Escalating to HighLevel Support

If the problem continues after completing the troubleshooting steps above, contact HighLevel Support with the following information:

  * Location ID
  * User experiencing the issue
  * Example contact/phone number
  * Exact call date and timestamp
  * Whether the call was inbound or outbound
  * Web App or Mobile App
  * Network used at the time (Wi-Fi, Ethernet, cellular)
  * Any high-rtt, high-jitter, high-packet-loss, or low-mos warning shown
  * Whether the issue is reproducible


Providing this information helps Support diagnose the issue more quickly and accurately.

7

## Related Articles

  * [Outbound Calls with Dialer in Web App (Softphone)](<https://help.gohighlevel.com/en/support/solutions/articles/48000981431>)
  * [How To Forward Inbound Calls to Mobile App](<https://help.gohighlevel.com/en/support/solutions/articles/48001224659>)
  * [Fix Call Disconnections in HighLevel Mobile App](<https://help.gohighlevel.com/en/support/solutions/articles/48001172952>)


8

## Frequently Asked Questions

Q: Why do my calls sound robotic or distorted?

Robotic or distorted audio usually results from jitter (inconsistent packet arrival) or packet loss. This can occur when network congestion, Wi-Fi instability, or competing bandwidth usage disrupts the steady flow of voice data. Check for high-jitter or high-packet-loss warnings, close bandwidth-heavy applications, and test your connection quality.

Q: Why can't the other person hear me?

One-way audio (where you can hear the caller but they cannot hear you, or vice versa) is typically caused by incorrect microphone or speaker selection, denied microphone permissions, or firewall/network restrictions blocking audio in one direction. Check device settings, grant microphone permissions in your browser or app, and review network firewall rules.

Q: Why is bad call quality affecting only one user?

If only one user is affected, compare that user's device, headset, browser or app version, permissions, and network with a user whose calls work correctly. The issue is likely specific to that user's local setup rather than a broader platform or account problem.

Q: Why does call quality become worse only at certain times of day?

Time-of-day degradation often points to network congestion or competing bandwidth usage during peak hours. Compare call-quality warnings and network conditions during good and bad periods. Your internet service provider (ISP) may also throttle bandwidth during high-usage times, or shared office networks may experience congestion when many users are active.

Q: Why does my call work on one network but not another?

A network-specific issue may involve Wi-Fi quality, firewall rules, VPNs, routing, or local congestion. If calls work on a home network but fail on a corporate or public network, the managed network may have firewall restrictions, content filtering, or security policies that interfere with real-time audio. Ask your IT team to review HighLevel's voice-network requirements.

Q: What should I do if I've tried all troubleshooting steps and the issue persists?

Contact HighLevel Support with the affected Location ID, user, example call details (contact/phone number, date, timestamp), whether the call was inbound or outbound, Web App or Mobile App, network used, any quality warnings displayed, and whether the issue is reproducible. This information helps Support diagnose the problem quickly.

Q: Do I need to use a wired connection for all calls?

No. Many users successfully make calls over Wi-Fi. A wired Ethernet connection is recommended as a troubleshooting step to determine whether Wi-Fi instability is contributing to poor call quality. If call quality improves over Ethernet, the Wi-Fi network may need optimization (router placement, channel selection, interference reduction).

Q: Why does internet speed not guarantee good call quality?

Voice calls require low latency, low jitter, and minimal packet loss — not just high download or upload speed. A fast connection with high latency or packet loss will still produce poor call quality. Test network quality (latency, jitter, packet loss, stability) in addition to bandwidth when troubleshooting call issues.

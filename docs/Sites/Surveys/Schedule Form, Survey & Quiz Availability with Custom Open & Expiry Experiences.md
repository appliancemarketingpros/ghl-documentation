# Schedule Form, Survey & Quiz Availability with Custom Open & Expiry Experiences

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008711-schedule-form-survey-quiz-availability-with-custom-open-expiry-experiences](https://help.gohighlevel.com/support/solutions/articles/155000008711-schedule-form-survey-quiz-availability-with-custom-open-expiry-experiences)  
**Category:** Sites  
**Folder:** Surveys

---

Forms • Surveys • Quizzes

Schedule Form, Survey & Quiz Availability with Custom Open & Expiry Experiences

Control exactly when Forms, Surveys, and Quizzes accept responses, then customize what visitors experience before opening and after closing.

What You'll Learn

HighLevel lets you schedule when a Form, Survey, or Quiz starts and stops accepting responses. You can choose specific opening and closing times, apply one time zone to the schedule, and create a custom page or URL redirect for visitors who arrive outside the active submission window. This guide explains the available schedule options, visitor states, setup workflow, use cases, and troubleshooting steps.

Existing Forms, Surveys, and Quizzes

Scheduling is optional. Existing Forms, Surveys, and Quizzes continue working as before when **Schedule visibility** is not enabled.

Table of Contents

1\. What is Scheduled Availability? 2\. Key Benefits 3\. Availability States and Scheduling Options 4\. Custom Open and Expiry Experiences 5\. Common Use Cases 6\. How To Setup Scheduled Availability 7\. Troubleshooting 8\. Frequently Asked Questions 9\. Related Articles

# **What is Scheduled Availability for Forms, Surveys, and Quizzes?**  
  


Scheduled Availability lets you define an active response window for a Form, Survey, or Quiz. Instead of publishing an experience and manually disabling it later, HighLevel can automatically transition it from **Not open yet** to **Accepting responses** and then to **Closed** according to the schedule you configure.

Visitors who arrive before the opening time or after the closing time can see a customized page or be redirected to another URL. This allows the same Form, Survey, or Quiz to follow the lifecycle of an event, promotion, webinar, contest, registration period, or other time-sensitive campaign.

## **Key Benefits of Scheduled Availability**  
  


Scheduled visibility reduces manual campaign management while giving visitors a deliberate experience at every stage of the response window. It is especially useful when submissions must begin or end at a defined time.

  * **Automatic Opening:** Publish ahead of time and begin accepting responses at the scheduled opening time.
  * **Automatic Expiration:** Stop accepting new responses automatically when the configured deadline arrives.
  * **Flexible Scheduling:** Open right away or on a specific date, and remain open indefinitely or close at a specific time.
  * **Time Zone Control:** Apply a defined time zone to both opening and closing times.
  * **Custom Pre-Launch Experience:** Give early visitors useful context instead of an unavailable form.
  * **Custom Expiry Experience:** Explain that submissions are closed or guide visitors to a different next step.
  * **Redirect Options:** Send visitors to another URL before opening or after closing.
  * **Less Manual Work:** Avoid relying on someone to disable the experience at the campaign deadline.


## **Availability States and Scheduling Options**  
  


The scheduling controls determine when responses are accepted and clearly show the current stage of the configured availability window. Understanding each option helps prevent accidental early access or submissions after a deadline.

Setting| Option| Behavior  
---|---|---  
**Opens**|  Right away| Accepts responses as soon as the experience is published and available.  
**Opens**|  Pick a date| Waits until the selected date and time before accepting responses.  
**Closes**|  Never| Does not have a scheduled closing time.  
**Closes**|  Pick a date| Stops accepting new responses at the selected date and time.  
**Time zone**|  Selected time zone| Applies to both the opening and closing schedule.  
  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080667002/original/NODEGm4pN5ZKhxMtO6XqmwZKyWZoadlnVg.png?1789108576)

### **Understanding the Availability Timeline**

When scheduled dates are configured, the timeline helps you see whether the current time falls before the opening window, inside the active response period, or after the closing deadline. The three states are **Not open yet** , **Accepting responses** , and **Closed**.

## **Custom Open and Expiry Experiences**  
  


Scheduling controls more than whether submissions are allowed. Separate visitor experiences let you communicate clearly with someone who arrives too early or too late and direct them toward the most appropriate next action.

### **Before the Form, Survey, or Quiz Opens**

A pre-open experience is useful when you publish or distribute the URL before the campaign begins. Instead of exposing the response fields early, visitors can see a launch message, event-opening time, instructions, or another relevant notice.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080666983/original/4mwTfeAcDrxk8_O74supGywgvB6tuSMhCg.png?1789108556)

### **After the Form, Survey, or Quiz Closes**

The post-close experience appears after the configured closing time, when new submissions are no longer accepted. Use it to explain that registration has ended, provide another offer, direct visitors to a waitlist, or communicate what they should do next.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080666931/original/DYj-aH5SMzILfPTNwcuTDeGAHCjWJJfJSQ.gif?1789108534)

### **Show a Page vs. Open a Link**

Each unavailable state can guide the visitor in one of two ways. Choose the option that best matches the next step in your campaign.

Option| Best For  
---|---  
**Show a page**|  Displaying customized messaging directly to the visitor using the built-in rich content editor.  
**Open a link**|  Redirecting visitors to another page, offer, waitlist, event, or destination URL.  
  
**Tip:** Use the built-in preview when creating a custom page so you can confirm the visitor-facing message is clear before the scheduled window begins or ends.

## **Common Use Cases for Scheduled Availability**

Scheduling is most valuable when the response window should match a campaign deadline or launch date. The visitor experience can then reinforce that timing without requiring manual changes at the start or end of the campaign.

Use Case| How Scheduling Helps  
---|---  
**Event Registrations**|  Automatically close registrations when the event or webinar deadline passes.  
**Flash Sales**|  Restrict a form or survey to the exact promotion window.  
**Webinar Launches**|  Publish early while displaying a registration-opens-soon experience.  
**Quizzes and Contests**|  Create a defined participation period and automatically stop new entries afterward.  
**Post-Campaign Traffic**|  Redirect late visitors to a waitlist, alternate offer, landing page, or upcoming event.  
**Coupon Promotions**|  Prevent new submissions after the promotional deadline.  
  
## **How To Setup Scheduled Availability for a Form, Survey, or Quiz**

A complete schedule includes the active response window, the correct time zone, and the experiences visitors should receive outside that window. Configure and preview all three before sharing the Form, Survey, or Quiz publicly.

### **Step 1: Open the Form, Survey, or Quiz**

Scheduled availability is configured on the individual asset, allowing different Forms, Surveys, and Quizzes to use different campaign windows.

  1. Go to **Sites**.
  2. Open **Forms** , **Surveys** , or **Quizzes**.
  3. Open the item you want to schedule.


### **Step 2: Enable Schedule Visibility**

The scheduling controls remain inactive until Schedule visibility is enabled, which lets existing unscheduled experiences continue operating normally.

  1. Open the **Settings** tab.
  2. Locate the Form, Survey, or Quiz settings.
  3. Enable **Schedule visibility**.


### **Step 3: Configure the Opening and Closing Window**

The opening and closing controls define the exact period when visitors are allowed to submit responses.

  1. For the opening time, choose **Right away** or **Pick a date**.
  2. If using Pick a date, select the opening date and time.
  3. For the closing time, choose **Never** or **Pick a date**.
  4. If using Pick a date, select the closing date and time.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155080666909/original/eel12UZvbpBvjw11PqR44MsXD352qKcNKA.png?1789108505)

### **Step 4: Select the Time Zone**

The selected time zone applies to both scheduled times, so it should match the time zone your campaign team intends to use when communicating deadlines.

  1. Open the **Time zone** selector.
  2. Select the time zone that should control the opening and closing schedule.


### **Step 5: Configure What Visitors See Before Opening**

A clear pre-open message prevents visitors from assuming the experience is broken or unavailable unexpectedly.

  1. Expand **Before the form opens** , **Before the survey opens** , or the equivalent Quiz option.
  2. Choose **Show a page** to create a custom message, or **Open a link** to redirect visitors.
  3. If using a page, customize the visitor-facing content.
  4. Preview the result.


### **Step 6: Configure What Visitors See After Closing**

The expiry experience gives late visitors a clear next step after new submissions are blocked automatically.

  1. Expand **After the form closes** , **After the survey closes** , or the equivalent Quiz option.
  2. Choose **Show a page** or **Open a link**.
  3. Configure the message or destination.
  4. Preview the result.


### **Step 7: Save and Test the Experience**

Testing the complete lifecycle helps catch time-zone mistakes, incorrect dates, or visitor messaging that does not match the campaign before the public response window begins.

  1. Click **Save**.
  2. Review the configured timeline.
  3. Preview the visitor experience.
  4. Confirm the intended opening and closing dates and time zone.
  5. Publish or distribute the Form, Survey, or Quiz according to your normal campaign workflow.


## **Troubleshooting Scheduled Availability**

Most scheduling issues can be isolated by checking whether scheduling is enabled, reviewing the selected time zone, and confirming the current time falls inside the configured response window.

Issue| What to Check  
---|---  
**The experience is accepting responses earlier than expected**|  Confirm the opening option is not set to Right away and verify the scheduled date, time, and time zone.  
**The experience still accepts responses after the intended deadline**|  Verify that the closing option is set to Pick a date rather than Never and confirm the configured time zone.  
**Visitors see the pre-open page when the experience should be open**|  Compare the current time with the configured opening time in the selected schedule time zone.  
**Visitors see the closed page too early**|  Review the closing date, closing time, and time zone for an incorrect value.  
**The wrong visitor message appears**|  Confirm you edited the correct state: Before opening or After closing.  
**The redirect does not go to the intended destination**|  Review the URL configured under Open a link and test the destination separately.  
**An existing Form, Survey, or Quiz changed unexpectedly**|  Confirm whether Schedule visibility was enabled. Items without scheduling enabled continue using their existing behavior.  
  
## **Frequently Asked Questions**

Q: Does scheduled availability work with Forms, Surveys, and Quizzes?

Yes. Schedule visibility is available for all three builder types.

Q: Do I have to set both an opening date and a closing date?

No. You can open the experience Right away or on a specific date, and you can set it to Never close or close on a specific date.

Q: Does one time zone apply to both opening and closing?

Yes. The selected schedule time zone applies to both configured times.

Q: What happens when the closing time is reached?

New submissions are blocked automatically and visitors receive the configured after-close page or redirect.

Q: Can I redirect visitors instead of displaying an unavailable message?

Yes. Choose Open a link for the applicable before-open or after-close state and configure the destination URL.

Q: Can I use different visitor experiences before opening and after closing?

Yes. The pre-open and post-close states are configured separately, allowing each stage to have its own page or redirect.

Q: Will enabling a closing time delete previous submissions?

No. The closing schedule controls whether new responses are accepted after the deadline; it does not represent a deletion action for existing submissions.

Q: What happens if Schedule visibility is turned off?

The Form, Survey, or Quiz continues using its normal availability behavior without the scheduled opening and closing window.

### **Related Articles**

[How to Create a Contact Form in HighLevel](<RELATED_ARTICLE_1_URL>) [Right Sidebar in Form and Survey Builder](<RELATED_ARTICLE_2_URL>) [Quiz Builder Guide](<RELATED_ARTICLE_3_URL>) [Forms, Surveys & Quizzes - On Submit Message Customisation](<RELATED_ARTICLE_4_URL>) [Create Forms & Surveys Inside the Site Builder](<RELATED_ARTICLE_5_URL>) [How to Use Embedding Options for Forms](<RELATED_ARTICLE_6_URL>)

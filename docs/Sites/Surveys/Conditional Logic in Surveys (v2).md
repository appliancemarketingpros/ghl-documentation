# Conditional Logic in Surveys (v2)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000005564-conditional-logic-in-surveys-v2-](https://help.gohighlevel.com/support/solutions/articles/155000005564-conditional-logic-in-surveys-v2-)  
**Category:** Sites  
**Folder:** Surveys

---

Conditional Logic v2 helps you build smarter, more personalized surveys by changing what respondents see and where they go based on their answers. Create dynamic experiences by showing or hiding fields, displaying custom messages, redirecting users, disqualifying responses, or sending respondents to different slides—all without creating multiple surveys.  
  


**Important**  
  


  * Conditional Logic v2 is available only for **newly created or cloned surveys**.  
  

  * Conditional Logic rules **are not included in account snapshots**.  
  


* * *

**TABLE OF CONTENTS**

  * What Is Conditional Logic in Surveys?
  * Key Benefits
  * What’s New in v2
  * Available Actions
  * How to Set Up Conditional Logic
  * Creating Multiple Survey Outcomes
  * Supported Operators by Field Type
  * Survey-Specific Features
  * Jump To
  * Rule Filtering
  * Rule Behavior & Evaluation
  * Best Practices
  * Frequently Asked Questions
  * Related Articles


* * *

# **What Is Conditional Logic in Surveys?**  
  


Conditional Logic automatically performs actions based on a respondent’s answers. Instead of showing every question to every respondent, you can create personalized survey experiences that adapt in real time.

For example, you can:  
  


  * Display additional questions based on previous answers.  
  

  * Skip irrelevant sections.  
  

  * Show personalized messages.  
  

  * Redirect respondents to another webpage.  
  

  * Disqualify respondents that don’t meet your criteria.  
  

  * Jump respondents directly to another slide.  
  


This helps reduce survey length, improve completion rates, and collect more relevant information.

* * *

## **Key Benefits**  
  


Conditional Logic helps you create more intelligent survey experiences while reducing unnecessary questions.  
  


  * **Personalize the survey experience:** Display only questions relevant to each respondent.  
  

  * **Improve completion rates:** Skip unnecessary questions and shorten surveys.  
  

  * **Automatically qualify leads:** Identify qualified and unqualified respondents instantly.  
  

  * **Create multiple survey paths:** Send respondents to different slides based on their answers.  
  

  * **Reduce manual review:** Automatically perform actions instead of reviewing responses later.  
  

  * **Build advanced survey flows:** Combine multiple rules for dynamic experiences.


* * *

## **What’s New in v2**  
  


Conditional Logic v2 introduces several improvements:  
  


  * Simplified three-step rule builder  
  

  * **Between** operator for numbers, scores, monetary, and date fields  
  

  * Jump To slide branching  
  

  * Expanded support for additional field types  
  

  * Show or hide Text, HTML, Images, and Terms & Conditions elements  
  

  * Rule filtering by field or slide  
  

  * Loop protection to prevent circular routing  
  

  * Improved accessibility and localized labels


* * *

## **Available Actions**  
  


Conditional Logic supports the following actions.  
  


**Action**| **Description**  
---|---  
Show / Hide Fields| Display or hide fields, questions, or slides.  
Display Custom Message| Show personalized messages based on responses.  
Redirect to URL| Send respondents to another webpage after submission.  
Disqualify Lead| Automatically mark respondents as unqualified.  
Jump To| Skip directly to another slide or question within the survey.  
  
  
**Note:** Rules are evaluated from top to bottom. When multiple rules match, later Show/Hide rules override earlier ones, while Redirect, Display Message, Disqualify, and Jump To execute according to their evaluation behavior.

* * *

## **How to Set Up Conditional Logic**  
  


Conditional Logic rules are created directly inside the Survey Builder after your survey questions and slides have been added.  
  


### **Step 1:**_Open the Survey Builder_  
  


From the account dashboard, navigate to **Sites** , open **Surveys** , and select an existing survey or create a new one.  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076853899/original/VJX-0DI7DWjRw53SswqAqPpsxBipAh1iaA.png?1785040325)**

###   
**Step 2:**_Review Your Survey Structure_  
  


Before creating logic, verify your survey contains all required questions, slides, and outcome pages.

For example, you may want separate slides for:  
  


  * Qualified respondents  
  

  * Disqualified respondents  
  

  * Booking appointments  
  

  * Thank-you pages  
  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155076853903/original/qpzkUoz_cSPfNWqlRcv1UsfJ2N7wwlO25A.png?1785040341)**

###   
**Step 3:**_Open Conditional Logic_  
  


Click **Conditional Logic** from the Survey Builder toolbar or open it from the right-side panel.

###   
**Step 4:**_Create a Rule_  
  


Select **Add New Condition**.  
  


Choose the action you want to perform:  
  


  * Show or Hide Fields  
  

  * Display Message  
  

  * Redirect to URL  
  

  * Disqualify Lead  
  

  * Jump To


###   
**Step 5:**_Configure the Logic_  
  


Build your rule using the three-step builder.  
  


### **Select Field**

Choose the question or slide that will trigger the rule.  
  


### **Select State**

Choose an operator such as:  
  


  * Is Equal To  
  

  * Contains  
  

  * Greater Than  
  

  * Between  
  

  * Is Empty


###   
**Provide Value**  
  


Enter or select the value that must match before the rule runs.  
  


You can also combine multiple conditions using:  
  


  * **AND** — every condition must be true.  
  

  * **OR** — any condition can be true.  
  


**Note:** A single rule can use either **AND** or **OR** , but not both.

###   
**Step 6:**_Configure the Action_  
  


Depending on the selected action, configure one of the following:  
  


  * Select fields to show or hide.  
  

  * Enter a custom message.  
  

  * Enter a redirect URL.  
  

  * Select the destination slide.  
  

  * Mark the respondent as disqualified.


###   
**Step 7:**_Save and Preview_  
  


Save the rule and preview your survey to verify every response path behaves as expected before publishing.

* * *

## **Creating Multiple Survey Outcomes**  
  


Conditional Logic allows one survey to produce multiple outcomes depending on how respondents answer.

For example:  
  


### **Qualified Path**  
  


If a respondent meets your qualification criteria:  
  


  * Continue to the next questions.  
  

  * Jump directly to a booking slide.  
  

  * Display a qualified thank-you message.


###   
**Disqualified Path**  
  


If a respondent doesn’t qualify:  
  


  * Display a custom message explaining they aren’t eligible.  
  

  * Jump directly to a disqualification slide.  
  

  * Stop asking unnecessary questions.  
  


###   
**Temporary Branches**  
  


You can temporarily send respondents to another slide to collect additional information before continuing with the survey.  
  


Example:  
  


Question 3  
  


↓  
  


Additional Information Slide  
  


↓  
  


Return to Slide 5  
  


**Note:** Conditional Logic prevents circular paths that would create an endless loop (for example, Slide A → Slide B → Slide A).

###   
**Supported Fields**  
  


Conditional Logic supports the following survey fields.

###   
**Input Fields**  
  


  * Single Line Text  
  

  * Multi Line Text  
  

  * Number  
  

  * Monetary  
  

  * Score  
  

  * Date Picker  
  

  * Dropdown (Single)  
  

  * Dropdown (Multiple)  
  

  * Radio Select  
  

  * Checkbox  
  

  * Terms & Conditions  
  

  * File Upload  
  

  * Signature  
  


### **Static Elements**  
  


  * Text  
  

  * HTML  
  

  * Image  
  


**Note:** Calendar fields aren’t supported.

* * *

## **Supported Operators by Field Type**  
  


**Field Type**| **Supported Operators**  
---|---  
Text| Equal To, Not Equal To, Contains, Starts With, Ends With, Is Empty, Is Filled  
Number, Score, Monetary| Equal To, Greater Than, Less Than, Between, Is Empty, Is Filled  
Date| Equal To, Before, After, Between, Is Empty, Is Filled  
Single Dropdown, Radio| Equal To, Not Equal To, Is Empty, Is Filled  
Multi Dropdown, Checkbox| Equal To, Not Equal To, Is Empty, Is Filled  
Terms & Conditions| Is Checked, Is Not Checked  
File Upload, Signature| Is Empty, Is Filled  
  
* * *

## **Survey-Specific Features**

###   
**Jump To**  
  


Jump respondents directly to another survey slide based on their answers.  
  


  * Triggered when respondents select **Next**
  * Supports branching within surveys  
  

  * Prevents circular routing


* * *

## **Rule Filtering**  
  


Filter rules by:  
  


  * Field  
  

  * Slide  
  


This makes complex surveys easier to manage.

* * *

## **Rule Behavior & Evaluation**  
  


Understanding how rules are evaluated helps prevent unexpected behavior.  
  


  * Rules are evaluated from top to bottom.  
  

  * Redirect, Display Message, and Disqualify execute only the first matching rule.  
  

  * Show/Hide rules can override previous rules.  
  

  * Jump To evaluates when respondents move to the next slide.  
  

  * Text comparisons ignore capitalization and extra spaces.  
  

  * Date comparisons use your account’s timezone.


* * *

## **Best Practices**  
  


Following these recommendations helps create predictable survey experiences.  
  


  * Create all slides before adding Conditional Logic.  
  

  * Give every survey field a unique Query Key.  
  

  * Keep rule logic as simple as possible.  
  

  * Test every possible survey path.  
  

  * Use **Between** for numeric and date ranges.  
  

  * Preview every Jump To path before publishing.  
  

  * Avoid creating unnecessary or overlapping rules.


* * *

## **Frequently Asked Questions**  
  


**Q: Can I mix AND and OR within the same rule?**

No. Each rule supports either **AND** or **OR** logic.

  
**Q: Can I have multiple Conditional Logic rules?**

Yes. Each rule runs independently according to its position in the rule list.  
  


**Q: How can I create different outcomes for qualified and disqualified respondents?**

Create separate slides for each outcome, then use **Jump To** , **Display Message** , or **Disqualify Lead** actions to send respondents to the appropriate path based on their answers.  
  


**Q: Can I send respondents to another slide and then continue the survey?**

Yes. Use **Jump To** to branch respondents to another slide before continuing to the remaining survey questions. Circular routing is automatically prevented.  
  


**Q: What happens if multiple rules match?**

Redirect, Display Message, and Disqualify execute the first matching rule. Show/Hide actions continue evaluating and may override earlier rules.  
  


**Q: Why don’t fields appear in the Conditional Logic dropdown?**

Verify that every survey field has a unique Query Key, then refresh the Conditional Logic panel.

* * *

## **Related Articles**

  


  * [](<https://help.gohighlevel.com/support/solutions/articles/155000003634-math-calculations-in-forms-surveys>)[Math Calculations in Forms/Surveys](<https://help.gohighlevel.com/en/support/solutions/articles/155000003634>)  
  

  * [](<https://help.gohighlevel.com/support/solutions/articles/155000004191-survey-create-contact-on-partial-completion>)[Survey Create Contact on Partial Completion](<https://help.gohighlevel.com/en/support/solutions/articles/155000004191>)[](<https://help.gohighlevel.com/support/solutions/articles/155000003259-workflow-trigger-survey-submitted>)


#

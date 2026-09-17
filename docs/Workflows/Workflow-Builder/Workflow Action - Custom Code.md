# Workflow Action - Custom Code

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000002253-workflow-action-custom-code](https://help.gohighlevel.com/support/solutions/articles/155000002253-workflow-action-custom-code)  
**Category:** Workflows  
**Folder:** Workflow Builder

---

**TABLE OF CONTENTS**

  * What is Custom Code?
  * How it works
    * 1\. Add Action
    * 2\. Programming Language
    * 3\. Property to be included in code
    * 4\. Code Editor
    * 5\. Enhanced console support
    * 6\. External HTTP Request
    * 7\. Format Code
    * 8\. Test your Code
    * Custom Code AI
      * Overview:
      * Previous Behaviour:
      * What’s New?
      * How to Use It?
      * Use Cases
  * Points to Remember


# **What is Custom Code?**

  


Custom Code is a powerful tool that will allow users to create custom logic they want to achieve and are not available currently. This provides flexibility and control beyond the pre-built actions, enabling users to automate complex tasks and integrate with various services not natively supported. This is a Premium Action.

  


  


# **How it works**

## **1\. Add Action**

  * In the workflows select the "+" icon to add an action and search for "Custom Code".


## **  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024378232/original/WRJzyc6QLm9ZtRTV2p7zAeFh-pRxSKzRuw.png?1712923757)**

  


## **2\. Programming Language**

  * The code can be written in JavaScript. This will be the default language selected.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024378127/original/vCWA7jTLsUWY_h-z1Ck3SO08t0yZYuihhw.png?1712923705)

## **3\. Property to be included in code**

  * Now what if there are values in the triggers or actions above the custom code and you want to use them in the code. That's where this field comes to use.
  * These fields allow us to reference values from previous steps in our code by adding them to a dictionary called InputData.
  * You can enter the Key in the "Key" input field and assign a value to it by selecting the value through the custom value picker.
  * You can add multiple properties by clicking on "Add Property"
  * For example, if a trigger gives us information about a customer, which we then need to manipulate, we can add their name to the  _Input Data_ fields and reference it with  _i inputData.keyName or inputData['keyName']_____


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024378049/original/mkwVkOObW-V10c1bOgLQ0DJC0CQ4fjQ5qA.png?1712923663)

  


  


  


## **4\. Code Editor**

  * You can write the code in the Code Editor
  * A sample code is pre populated for your reference.
  * Output should also be written in the code formatter itself.
  * Output should be a JavaScript Object or Array of Objects.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155024378027/original/kHyz3pZI-RI9S0Ca4p1YvYPCBejYVve4_A.png?1712923639)

  


## **5.****Enhanced console support**

  


This feature captures and logs all `console.log` outputs from user code, allowing user to debug and monitor the code more effectively.

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155027875958/original/K0BsznDm80JrDaTX-UqXEfvu2vtqvIOWhw.png?1718802876)  


## **6\. External HTTP Request**

  * Custom code supports external HTTP requests
  * Click on "HTTP Request" button above the code editor
  * Select from the following -
    * Get Method
    * Post Method
    * Put Method
    * Patch Method
    * Delete Method
    * Head Method
    * Options Method
  * The selected request will populate at the bottom in the code editor


  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031663651/original/NWpdt8gG-WfHVs1EiibGgGHoluVDhrgsmA.png?1724674043)**  


  


**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031663702/original/Ob9Ll6kArI7ngGwSq70HnuiJ-UcNJ5nc0g.png?1724674052)**

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155031665905/original/4Da5WUEasD9nTmpu84KkQQfFfHeykeDoJg.png?1724675586)

  


## **7\. Format Code**

  * You can also format the code. Use the "Format Code" button in the bottom of the code editor to change the code into more readable format. 
  * Properly formatted code is easier to read and understand.
  * For instance, consistent indentation, spacing, and line breaks help identify code blocks, functions, or sections of a document.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040260049/original/2i2TDFNI9mLohJ2WLF-OAPHwbzYWsPt7FQ.png?1737545882)

  


## **8\. Test your Code**

  * Testing the code is a mandatory step, if the test is not done then user will not be able to use the output of the code in the subsequent steps.
  * To test the code click on the "Test your Code" button.
  * When you click on the button a new pop up will open where you can run the test.
  * There can be 2 scenarios, first where you have added properties and second where you have not.
  * In case there are properties are added you can enter the sample values in the "Test Setup" tab and test the Response.
  * In case there are no properties added, you can directly check the response.
  * Click on the "Test your Code" button to check the response.
  * Post clicking on the test button, if there are no errors in the code them it will show "Test Result Success" and if there is an error in code then the result will be "Test Result Failed" and you would have to recheck the code to remove the error.  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040704154/original/lnc7U0ylQXPQU2iUjFC1urV6_Mb0BMMvIQ.png?1738228691)

  


**  
![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040704225/original/LFTyDgiuqeZ56sE6AoR7bBSsZOa4sDQVeA.jpeg?1738228725)**![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040704299/original/AFkt23K95-pVPzvItG697Rm9goHpeEv9uw.png?1738228746)

  


  


**9\. Check Input Values in Execution logs**

  


  * Now check the input values in the Execution logs also.
  * Go to the execution you want to check the values for and click on more details.


  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040260812/original/RgJrOqeucNAjU44v9pesVqODOUf6f7u54g.png?1737546274)

  


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155040260857/original/rbE0v-1cwhoPJWnMg0T5DsAaTTNISu9Flw.png?1737546291)

  


10\. Return a response directly from their custom code.  


  


**Key Benefits:**

  * This improvement allows for a more streamlined coding experience, making it easier to write, debug, and manage custom asynchronous code.
  * This new capability simplifies handling asynchronous operations and improves the overall efficiency of custom scripts.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155028307901/original/Hq5-hpYYprjyTt27r2647tAzQvd185kgWQ.png?1719479946)

  


### **Custom Code AI**

  


#### Overview:

Writing custom code in workflows just got smarter, faster, and easier—thanks to AI! We’re thrilled to introduce Code with AI (Beta), enabling users to generate custom code snippets with just a simple description.

#### Previous Behaviour:

  * Previously, creating custom code within workflows required users to write JavaScript code from scratch, which could be time-consuming and required programming expertise.
  * Manually map input properties from previous workflow steps to use within the code.
  * Test and debug code manually before implementation.
  * This process demanded a significant investment of time and technical skill.


#### What’s New?

  * Now we have AI-Assisted Code Generation. With Code with AI, the process is streamlined:
  * AI-Powered Code Generation – Describe the desired functionality in plain language, and AI will generate JavaScript code for you.
  * Automated Property Integration – AI intelligently incorporates relevant input properties based on your description.
  * One-Click Implementation – Quickly review and insert AI-generated code into your workflow.
  * Regenerate if Needed – Not happy with the first result? Click Generate again for a fresh version.


Pro Tip: 

Be as specific as possible in your prompt for the best results!

#### How to Use It?

  * Select: Choose Custom Code action in your workflow.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042527561/original/nAuVDOdQnA_E5f_4vFRoyZnV4uiwuuVPLQ.png?1740997277)  


  * Activate AI: Click "Build with AI" to open the AI assistant.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042527587/original/NGS2QkhHBqVWTPkey7Js2HHEO9y-OxhfMw.png?1740997301)

  * Describe: Input your desired functionality (e.g., "I have an API that returns a date in MM-DD-YYYY format. Can you help me convert it to YYYY-MM-DD.").
  * Generate: Click Generate and let AI craft the code for you.


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042527680/original/wHemORBiauxMu8J1jd5jKPyo-Ukw5r0AHg.png?1740997376)

![image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042527732/original/bbQ38-TfLfpWsC2KL8rjDbSwD0pjs1xVfA.png?1740997417)

  * Regenerate - Want to make any changes in the Code, mention the changes in the text box and click on "Regenerate"


![image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042527814/original/IdROuIKWKKyiOz_M_FaiBWIqEXTOuU2tsA.jpeg?1740997504)

  * Implement: Review the output and click Use Code to insert it into your workflow.


![image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155042527822/original/raFUyfiaiJllR7EUEYNmwx7IBk8zZpL5tw.jpeg?1740997515)

#### Use Cases

  * Data Formatting – Automatically format phone numbers or dates to match your preferred style.
  * API Integration – Generate code to connect with external services via HTTP requests.
  * Mathematical Calculations – Compute interest rates, discount percentages, or other formulas dynamically.
  * String Manipulation – Extract key details from text, such as email addresses from subject lines.
  * Conditional Logic – Implement custom decision-making processes, like routing leads based on specific criteria.


  


  


  


  


  


# **Points to Remember**

  * Custom value will not be passed when you are testing your code.Only the contact information will be passed when testing a code. Other properties used in the code will not pass while testing.
  * Testing the code is mandatory. No output will be available for untested code in subsequent action.
  * Use the Property fields to assign key names and map values from previous steps. Use inputData.keyName or inputData['keyName'] to access the values within the code.

# Agent Studio - Router Tool (AI & Conditional Router)

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007404-agent-studio-router-tool-ai-conditional-router-](https://help.gohighlevel.com/support/solutions/articles/155000007404-agent-studio-router-tool-ai-conditional-router-)  
**Category:** AI Employee  
**Folder:** Agent Studio

---

Agent Studio Router helps you control how conversations move between nodes in Agent Studio. As the name implies, a router directs the workflow from one node to the next based on specific logic or conditions. This article explains how to use AI Router, Conditional Router, and No Condition routing to build smarter conversation paths based on intent, logic, or an always-on transition.

* * *

**TABLE OF CONTENTS**

  * What is the Router Tool in Agent Studio?
  * Key Benefits of the Router Tool in Agent Studio 
  * Using AI Router
  * Using Conditional Router
  * Using No Condition
  * Using Router Inside Sequential Nodes
  * How To Use the Routing Tool in Agent Studio
  * Example Flow
  * Best Practices
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is the Router Tool in Agent Studio?**

  


Agent Studio Router controls how an agent moves from one node to another based on conversation context or logic. It helps you create flexible paths inside your graph so the next step is chosen based on what the user says, what data has been captured, or whether the flow should always continue to the next node.

  


The Router supports three routing approaches:

  


  * **AI Router** : Uses natural language intent to decide which path to take.  
  


  * **Conditional Router** : Uses saved variables and logic rules to determine the next node.  
  


  * **No Condition** : Always moves to the next connected node without evaluating intent or logic.


  


The Router can be used in agent flows and inside Sequential Nodes, which allows a linear process to branch when needed before continuing.

* * *

## **Key Benefits of the Router Tool in Agent Studio**

  


  * **Smarter branching** : Route users based on what they mean, not just fixed keywords.  
  


  * **More control** : Use variables and logic rules to move contacts to the right next step.  
  


  * **Cleaner graph design** : Connect nodes more intentionally instead of forcing everything into one path.  
  


  * **Flexible flow building** : Combine AI routing, conditional logic, and always-on routing in the same agent.  
  


  * **Better user experience** : Help contacts reach the right outcome faster with fewer unnecessary steps.  
  


  * **Support for more advanced automations** : Add dynamic decision-making inside Agent Studio and Sequential Nodes.


* * *

## **Using AI Router**

  


AI Router is best when the next step depends on what the user means in natural language. Instead of checking for an exact value, the AI reviews the user’s message and matches it to the most appropriate intent you define.

  


**Use AI Router when:**

  


  * users may respond in different ways that mean the same thing  
  


  * you want to branch based on interest, sentiment, or conversational intent  
  


  * the path should be chosen from natural language instead of a stored variable


  


Example intents:

  


  * **User wants to invest in silver**  
  


  * **User does not want to invest in silver**


  


In this setup, the Router evaluates the user’s last message and sends the conversation to the matching connected node.  
  


![](https://jumpshare.com/share/VI6v7INolYvCBP15V3pA+/Screen+Shot+2026-03-31+at+21.12.20.png)

* * *

## **Using Conditional Router**

  


Conditional Router is best when routing depends on a known value that has already been captured in the conversation. This is useful when a tool, form field, choice, or earlier node stores a value that can be evaluated with logic.

  


**Use Conditional Router when:**

  


  * you already have a saved variable to evaluate  
  


  * the route depends on a fixed value such as Yes, No, positive, or negative  
  


  * you need explicit rule-based branching instead of AI interpretation


  


Conditional routes use logic fields such as:

  


  * **Variable**

  * **Operator**

  * **Value**


  


Example:

  


  * Variable: `{{runtime.userChoice_eyro}}`

  * Operator: `equals (EQ)`

  * Value: `Yes`


  


That route can send the user to a proceed path, while another condition can send them to a different node.

  
![](https://jumpshare.com/share/wktANOfKtUOFcHZZWWcw+/Screen+Shot+2026-03-31+at+21.14.33.png)  


* * *

## **Using No Condition**

  


No Condition is useful when you want the Router to move forward every time without evaluating intent or logic. This creates an always-on route and works well as a bridge between steps in a larger conversation flow.

  


**Use No Condition when:**

  


  * the next node should always run after the current one  
  


  * you want a simple transition between nodes  
  


  * a step has already collected the needed information and should now continue automatically


  


When enabled, the route acts as an always path to the next connected node.

  


![](https://jumpshare.com/share/QinbbLPyNiYY12ZSIgGK+/Screen+Shot+2026-03-31+at+21.17.08.png)

* * *

## **Using Router Inside Sequential Nodes**

  


Router can also be used inside Sequential Nodes, which allows a mostly linear flow to branch when needed. This is helpful when a sequence should continue in order but still needs an AI-based or logic-based decision before moving forward.

  


**This approach works well when:**

  


  * a sequence needs a decision point before the next step  
  


  * a user’s answer should redirect them to different outcomes  
  


  * you want to combine structured flows with dynamic routing


  


![](https://jumpshare.com/share/tJr24ofDTDJb2xhHjjnw+/GIF+Recording+2026-03-31+at+21.20.14.gif)

* * *

## **How To Use the Routing Tool in Agent Studio**

  


A well-structured Router setup ensures conversations move intelligently based on user intent or defined logic. Follow the steps below to configure both AI-based and rule-based routing inside your agent.

  


  1. From the left navigation menu, click **AI Agents** and then select the **Agent Studio** tab at the top of the page.  
  
![](https://jumpshare.com/share/zexM4XYJb4ZN67edOpbJ+/Screen+Shot+2026-03-31+at+21.30.00.png)  
  

  2. **Create** a **New Agent** or **click** on an existing **Agent's****name** to **open** it.  
  
![](https://jumpshare.com/share/b9AkqFZdviXcCjptrwI2+/Screen+Shot+2026-03-31+at+21.27.54.png)  
  

  3. **Add** a **Trigger** like Chat Message or Form Submitted, etc.  
  

  4. Add an **AI****Agent** and configure it.  
  
![](https://jumpshare.com/share/lkDj473SlSXKIqrJKjAe+/GIF+Recording+2026-03-31+at+21.45.09.gif)  
  

  5. From the **Flow Control** panel on the left, **drag the Router node onto the canvas to insert a decision point in your conversation flow**.  
  
![](https://jumpshare.com/share/8tnlg7DSgrZXz9dweYr9+/Screen+Shot+2026-03-31+at+21.56.30.png)  
  

  6. Once placed, the **Edit Router panel opens on the right** , where you can choose the **routing****mode** and begin configuring how the conversation should branch.  
  

  7. In the Router configuration panel, choose between **AI Router and Conditional Router** under the “**Router Type** ” section. This selection determines whether the routing decision will be based on AI intent detection or rule-based logic.  
  
![](https://jumpshare.com/share/FVms2LHqWAfQ9CtphNft+/Screen+Shot+2026-03-31+at+21.59.17.png)  
  

  8. **Configure** the **router** :  
  


     * For **AI Router** , add the intents that should determine each path. Each intent represents a branch the conversation can follow when the AI detects matching intent from the user’s message.  
  
![](https://jumpshare.com/share/jW2IKGkLZ7iimOEMsozO+/GIF+Recording+2026-04-01+at+18.27.34.gif)  
  


     * For **Conditional Router** , add one or more conditions using the correct variable, operator, and value. 

Switch to **Conditional Router** if you want routing decisions to be based on structured data instead of natural language interpretation. This mode evaluates variables and predefined logic to determine the next step.  
  


Enter a clear **Label** for the condition branch to identify it within the conversation graph. This label appears on the node connection and helps keep complex flows organized.  
  


Select the **Condition Type** to define how multiple rules are evaluated. Choose whether all conditions must match (AND) or if any single condition can match (OR).  
  


In the condition editor, select the **Variable** , choose the appropriate **Operator** , and define the expected **Value**. This tells the Router exactly what data to evaluate before proceeding down that branch.

  
![](https://jumpshare.com/share/7dDVSMoCgA6psjx5xIsb+/GIF+Recording+2026-04-01+at+18.21.02.gif)  
  


     * For **No Condition** , enable the toggle so the route always continues to the next node.  
  
![](https://jumpshare.com/share/gsL6cP1tnxBoh6dS8wV4+/Screen+Shot+2026-04-01+at+18.22.24.png)  
  


  9. **Connect** each **route****output** to the correct **destination****node** in your graph.  
  
![](https://jumpshare.com/share/6I7auL2jvAPr7ecotmTQ+/Screen+Shot+2026-04-01+at+18.30.36.png)  
  

  10. **Save** your Router settings.  
  

  11. **Test** the **conversation** to confirm each route leads to the correct next step.  
  

  12. **Save** , **Publish** and **Deploy** the workflow.  
  
![](https://jumpshare.com/share/jHwppkWcAJJVItrnCIQh+/Screen+Shot+2026-04-01+at+18.33.03.png)


* * *

## **Example Flow**

  


A practical example makes it easier to see how different Router types work together in one agent. The flow below shows how AI routing, always-on routing, and condition-based routing can support a complete user journey.

  


**Example flow:**

  


  1. The agent asks the user about the silver price and uses **Web Search** to provide the information.  
  


  2. The agent then asks whether the user wants to invest in silver.  
  


  3. An **AI Router** evaluates the user’s response:  
  


     * If the user wants to invest, the flow moves to the next node.  
  


     * If the user does not want to invest, the flow routes to a thank-you node.  
  


  4. The next node captures the user’s email.  
  


  5. A **No Condition** route always moves the flow to a confirmation step.  
  


  6. A **Single Choice** node asks whether the user wants to proceed.  
  


  7. A **Conditional Router** checks the saved answer:  
  


     * If the value equals **Yes** , the flow moves to the proceed path.  
  


     * If the value equals **No** , the flow moves to a different outcome.  
  


* * *

## **Best Practices**

  


Strong routing design makes your agent easier to maintain and helps reduce errors during testing. Clear route labels, intentional logic, and realistic test cases make it easier to understand why a user reached a specific path.

  


  * Use **AI Router** when user responses may vary in wording but share the same intent.  
  


  * Use **Conditional Router** when the decision depends on a saved value.  
  


  * Use **No Condition** when the flow should always continue.  
  


  * Keep route labels clear so each branch is easy to understand.  
  


  * Test each route path before publishing your agent.  
  


  * Link to related setup articles when a route depends on variables or other tools.


* * *

## **Frequently Asked Questions**

  


**Q: What is the difference between AI Router and Conditional Router?**  
AI Router evaluates natural-language intent, while Conditional Router checks a saved value using logic such as variable, operator, and value.

  


**Q: When should I use No Condition?**  
Use No Condition when the flow should always move to the next connected node without evaluating intent or logic.

  


**Q: Can I use Router inside Sequential Nodes?**  
Yes. Router can be used inside Sequential Nodes so a linear flow can branch before continuing.

  


**Q: Do I need a variable for AI Router?**  
No. AI Router uses the user’s natural-language response and the intents you define.

  


**Q: Do I need a variable for Conditional Router?**  
Yes. Conditional Router works best when the value has already been captured and stored for evaluation.

  


**Q: What happens if no intent or condition matches?**  
Make sure each route is connected to the correct next node and include a fallback path where needed so the conversation can continue as expected.

  


**Q: What should I do if a route is not going to the expected node?**  
Review the route configuration, confirm the correct node connections, and test the conversation again to verify the intent or condition is set up correctly.

  


**Q: Does the Router add extra AI message cost?**

Only AI Router executions count toward your LLM billing. Conditional and No-Condition modes are free.

  


**Q: What happens if no intent or condition matches?**

The flow follows the “Default” edge. If none is connected, the conversation ends with an error log entry.

  


**Q: Can I mix AI and Conditional routing in one node?**

One Router node supports one mode at a time, but you can chain multiple Routers back-to-back.

  


**Q: Is intent training required?**

No. The LLM classifies on-the-fly from your intent names and the current conversation context.

  


**Q: How do I debug misplaced routes?**

Open the Execution Log → Routing tab to see the detected intent, reasoning, and confidence or the evaluated condition string.

  


**Q: Will the floating panel replace all pop-ups in Agent Studio?**

Yes, future node types will use the same non-modal panel to keep the canvas visible.

* * *

### **Related Articles**

  


  * [](<https://help.gohighlevel.com/support/solutions/articles/155000006058-how-to-use-the-ai-agent-studio-in-highlevel>)[Agent Studio Overview](<https://help.gohighlevel.com/en/support/solutions/articles/155000007393>)  
  


  * [How to Use the AI Agent Studio in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000006058-how-to-use-the-ai-agent-studio-in-highlevel>)  
  


  * [Ask AI + Agent Studio Integration](<https://help.gohighlevel.com/en/support/solutions/articles/155000006677>)  
  


  * [How to Set Up Agent Studio Triggers for Real-Time Starts](<https://help.gohighlevel.com/en/support/solutions/articles/155000007310>)  
  


  * [How to Use Custom Values and Variables in Agent Studio](<https://help.gohighlevel.com/en/support/solutions/articles/155000007432>)

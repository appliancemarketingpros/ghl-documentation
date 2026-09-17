# Test & Optimize Conversations AI Agents with Prompt Optimizer

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008435-test-optimize-conversations-ai-agents-with-prompt-optimizer](https://help.gohighlevel.com/support/solutions/articles/155000008435-test-optimize-conversations-ai-agents-with-prompt-optimizer)  
**Category:** AI Employee  
**Folder:** Conversation AI

---

Conversations AI

# Test & Optimize Conversations AI Agents with Prompt Optimizer

Validate and improve your Conversations AI agent before it interacts with live customers by generating realistic chat scenarios, running live tests, reviewing AI evaluations, and applying prompt improvements only after you approve them.

What You'll Learn

Prompt Optimizer helps you test how a Conversations AI agent behaves across realistic customer scenarios without changing the production prompt during testing. You can review full chat transcripts, validate configured actions, understand why tests pass or fail, and compare AI-generated prompt variations.

You’ll also learn how to configure test runs, review usage, use manual or automatic optimization, and apply an improved prompt after reviewing the changes.

Labs Feature

Prompt Optimizer for Conversations AI is available as a Labs feature. Labs features are actively being improved and may change over time based on customer feedback.

Table of Contents

  1. What Is Prompt Optimizer for Conversations AI?
  2. Key Benefits of Prompt Optimizer for Conversations AI
  3. The Three-Phase Workflow
  4. Configure
  5. Test: Real Chats, Real Actions
  6. Improvise: AI-Guided Prompt Optimization
  7. Important Considerations
  8. Frequently Asked Questions
  9. Related Articles


1

## What Is Prompt Optimizer for Conversations AI?

Prompt Optimizer helps you identify prompt weaknesses before your Conversations AI agent interacts with real customers. It generates realistic customer scenarios, runs live chat conversations against a cloned version of your agent, evaluates the outcomes, and recommends prompt improvements based on what happened during testing.

The workflow is built around three phases: **Configure** , **Test** , and **Improvise**. Together, these phases help you create a test plan, inspect actual agent behavior, understand failures, and improve the editable prompt without changing your production prompt until you choose to apply a variation.

Important

Although Prompt Optimizer tests a cloned version of your agent, configured Conversations AI actions can still execute during testing. Consider using dedicated test calendars, workflows, routing destinations, and other test resources where appropriate.

2

## Key Benefits of Prompt Optimizer for Conversations AI

Prompt Optimizer helps you move from manual trial-and-error testing to a repeatable process for validating agent behavior and improving prompt quality.

**Automated Scenario Generation:** Creates realistic customer scenarios based on your prompt, configured actions, knowledge base, appointment setup, and business context.

**Live Chat Testing:** Runs actual Conversations AI chat executions instead of relying on static prompt previews.

**Action Validation:** Tracks whether configured actions occur at the expected point in a conversation.

**AI-Powered Evaluation:** Explains what passed, what failed, and why each chat did or did not meet the expected outcome.

**Prompt Optimization:** Generates improved prompt variations from failed conversations and tests those variations against the selected scenarios.

**Prompt Comparison:** Uses Prompt Diff to show exactly what changed before you apply an optimized version.

**Production Protection:** Keeps your production prompt unchanged until you select **Use Prompt**.

**Multi-Language Testing:** Keeps generated scenarios, customer messages, evaluations, and optimized prompts aligned to the agent’s configured language.

**Scenario Reuse:** Lets you reuse scenarios from earlier runs to compare performance after prompt or configuration changes.

3

## The Three-Phase Workflow

Configure, Test, and Improvise form a continuous testing cycle. Each phase has a different purpose, but together they help you validate the experience your customers are likely to have before you apply prompt changes to production.

Phase 1

Configure

Generate or reuse customer scenarios, choose how many chat executions to run, and review usage before testing.

Phase 2

Test

Run live chat conversations, review transcripts, validate action invocation, and inspect AI-scored results.

Phase 3

Improvise

Analyze failed chats, generate prompt variations, compare changes, and apply the variation you want to use.

4

## Configure

A useful test run starts with meaningful scenarios. Prompt Optimizer builds scenarios from the agent’s existing configuration so you can test behavior that reflects the prompt, knowledge, appointment setup, and available actions.

### Generate Test Scenarios

Prompt Optimizer can generate contextual scenarios based on your agent configuration. Each scenario can include a customer persona, opening message, expected agent behavior, and priority level.

  * Prompt and configured language
  * Knowledge Base content
  * Appointment setup
  * Configured Conversations AI actions
  * Business context


![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078246509/original/YhVLptu1ZcKBi9gEXGBb3wAsWDwxbA9pUg.png?1786541413)

### Reuse Previous Scenarios

Reuse scenarios from earlier runs when you want to measure whether a prompt or configuration change improved the same customer situations instead of starting with a completely new test set.

### Configure Chat Executions

Running more than one chat execution for a scenario can help expose inconsistent behavior. Choose how many executions you want to run per scenario before starting the test.

### Review Usage Before Testing

Before a run begins, Prompt Optimizer shows usage information and a pre-run review so you can confirm the selected scenarios, expected message usage, and temporary contact handling.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078246564/original/vluIToGpYSZfTjWOxKdBuXW7_85DFlKfFg.png?1786541455)

### Temporary Test Contacts

Prompt Optimizer creates temporary contacts for chat execution and cleans them up after testing. This keeps test conversations separate from your normal customer records.

Important

Temporary test contacts do not prevent configured actions from executing. For actions such as appointment booking, workflows, handovers, transfers, and follow-ups, use test resources where appropriate.

5

## Test: Real Chats, Real Actions

The Test phase shows how the cloned agent actually behaves in conversation. Prompt Optimizer sends customer-style messages, waits for the agent’s replies, tracks relevant action evidence, and evaluates the completed chat against the expected scenario behavior.

### Live Chat Executions

These are live Conversations AI executions rather than static previews. Each run captures the customer messages, agent replies, conversation timeline, and available action evidence.

Executions can move through statuses such as **Waiting** , **In Progress** , **Evaluating** , **Completed** , or **Failed**.

### Action Invocation Tracking

Prompt Optimizer can track configured actions during testing, including:

  * Appointment Booking
  * Human Handover
  * Workflow Trigger
  * Bot Transfer
  * Stop Bot
  * Auto Follow-up
  * Contact Field Update
  * Knowledge Base Query


Important

Real actions may fire during testing. Review the connected calendar, workflow, routing destination, field update, or other configured resource before running scenarios against production-connected actions.

### Review Chat Transcripts

Open individual executions to inspect the customer messages, agent responses, and action evidence. Transcript review is especially useful when you need to determine whether a failure came from prompt instructions, knowledge availability, or action configuration.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078246609/original/_Nk9_28SAsqasMbxozRHQXYOK_s44ctDqQ.png?1786541486)

### AI Evaluation and Scoring

Each chat is evaluated against the expected behavior defined for the scenario. Prompt Optimizer provides a pass/fail outcome and AI reasoning that explains why the chat did or did not satisfy the expected result.

Because large language models are probabilistic, repeated executions of the same scenario may not produce identical results. Use the scores as directional guidance and review the supporting transcript and reasoning.

### Overall Results

After the run completes, review the overall accuracy, number of passed and failed chats, scenario-level results, and individual execution details to decide whether the prompt needs further improvement.

6

## Improvise: AI-Guided Prompt Optimization

The Improvise phase turns test failures into prompt improvement opportunities. Prompt Optimizer uses failed conversations and evaluation reasoning to generate a revised editable prompt and test whether that variation performs better.

### Manual Improvise

Use **Improvise** when you want to generate one optimized variation at a time.

  1. Review the failed chats and AI reasoning.
  2. Click **Improvise**.
  3. Prompt Optimizer generates an updated prompt variation.
  4. The variation is tested against the selected scenarios.
  5. Review the updated accuracy, chats, reasoning, and Prompt Diff.


### Auto Optimize

Use **Auto** to run multiple optimization attempts automatically. Auto Optimize continues within its configured limits until the target accuracy is reached, the maximum variation limit is reached, or the run stops for another supported reason.

### AI Failure Analysis

The optimizer reviews failed chats and can identify issues such as:

  * Missing action triggers
  * Weak clarification logic
  * Unsupported Knowledge Base answers
  * Incomplete booking flows
  * Poor handoff behavior
  * Missing or ambiguous prompt instructions


### Prompt Rewriting

Prompt Optimizer rewrites the editable prompt to address the identified weaknesses while preserving the required Conversations AI prompt structure.

### Prompt Diff

Use **Prompt Diff** to compare the original prompt and an optimized variation before applying anything to production. Review the changed instructions and confirm that they still match your intended customer experience.

### Best Variation and Variation History

When multiple variations exist, Prompt Optimizer highlights the highest-performing one with the **Best Variation** label. Variation history stores the accuracy, test results, AI reasoning, and prompt differences so you can compare iterations.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/155078246686/original/2herHGCzS3wsbdeNuTZl7M2f4q7CeXCuQA.png?1786541532)

### Apply an Optimized Prompt

  1. Select the variation you want to use.
  2. Review the **Prompt Diff** and **AI Reasoning**.
  3. Confirm that the new instructions align with your requirements.
  4. Click **Use Prompt** to apply the selected prompt to the production agent.


7

## Important Considerations

Prompt Optimizer is designed to help you improve agent behavior, but test results and actions still need human review. Use these considerations to interpret results correctly and reduce unintended production activity.

Note

Large language model evaluations and prompt rewrites can vary between runs. Treat accuracy as directional guidance rather than an absolute guarantee of production behavior.

Note

Auto Optimize runs operate within configured variation limits and may stop before reaching a target accuracy.

Note

Chat executions include timeout protection so long or stuck conversations do not prevent the overall run from completing.

Note

A failed evaluation can reflect strict scoring criteria, ambiguous expected behavior, missing knowledge, action configuration, or prompt wording. Review the transcript and reasoning before changing the prompt.

Important

Configured Conversations AI actions can execute during testing. Use test calendars, workflows, routing destinations, and other isolated resources where appropriate.

Troubleshooting

Prompt optimization improves the editable prompt. If a failure is caused by a calendar, workflow, handover destination, Knowledge Base source, or field mapping, correct that configuration instead of relying only on prompt rewriting.

## Frequently Asked Questions

### Q. Does Prompt Optimizer modify my live Conversations AI agent automatically?

No. Testing and optimization are performed against a cloned agent. The production prompt remains unchanged until you review a variation and click **Use Prompt**.

### Q. Can I test the same scenario more than once?

Yes. Running multiple chat executions for the same scenario helps you identify whether the agent behaves consistently or whether failures appear only intermittently.

### Q. Can I reuse scenarios from a previous run?

Yes. Reusing earlier scenarios is useful when you want to compare performance after changing the prompt, knowledge, actions, or appointment configuration.

### Q. What should I do when a chat fails?

Review the transcript, action evidence, and AI reasoning first. A failure may come from the prompt, missing or unsupported Knowledge Base content, an action configuration issue, or strict evaluation criteria.

### Q. Why can repeated tests produce different results?

Large language models are probabilistic, so the customer simulation, agent response, and evaluation may vary. Multiple executions provide a more useful view of consistency than a single chat.

### Q. Does Prompt Optimizer support multiple languages?

Yes. Scenarios, customer messages, evaluations, and optimized prompts stay aligned to the language configured for the Conversations AI agent.

### Q. Can Prompt Optimizer test Conversations AI actions?

Yes. It can track actions such as Appointment Booking, Human Handover, Workflow Trigger, Bot Transfer, Stop Bot, Auto Follow-up, Contact Field Update, and Knowledge Base Query when those actions are configured.

### Q. Should I use production calendars and workflows during testing?

Use dedicated test resources whenever possible. Real actions can execute during Prompt Optimizer runs, even though the agent prompt itself is tested through a cloned agent.

### Q. When should I run Prompt Optimizer?

Run it after significant changes to the prompt, Knowledge Base, actions, appointment behavior, or other agent configuration that could change how customers experience the conversation.

## Related Articles

  * [How to Create and Set Up a Conversation AI Bot in HighLevel](<https://help.gohighlevel.com/support/solutions/articles/155000004401-how-to-set-up-a-conversation-ai-bot>)
  * [Bot Goals Overview in Conversation AI](<https://help.gohighlevel.com/support/solutions/articles/155000004417-bot-goals-overview-conversation-ai>)
  * [Customize Conversation AI Agent Responses with Prompts and Instructions](<https://help.gohighlevel.com/support/solutions/articles/155000002255-how-to-customize-conversation-ai-agent-responses-with-prompts-and-instructions>)
  * [How to Use Conversation AI to Book Appointments](<https://help.gohighlevel.com/support/solutions/articles/155000000210-appointment-booking-in-conversation-ai>)
  * [How to Use Knowledge Base Triggers in Conversation AI](<https://help.gohighlevel.com/support/solutions/articles/155000007791-how-to-use-knowledge-base-triggers-in-conversation-ai>)
  * [Review AI Activity Using Agent Logs for Conversation AI](<https://help.gohighlevel.com/support/solutions/articles/155000007996-conversation-ai-agent-logs>)

# Conversation AI - New Knowledge Sources & Quality Upgrades

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000006456-conversation-ai-new-knowledge-sources-quality-upgrades](https://help.gohighlevel.com/support/solutions/articles/155000006456-conversation-ai-new-knowledge-sources-quality-upgrades)  
**Category:** AI Employee  
**Folder:** Conversation AI

---

This guide explains HighLevel’s Knowledge Source and retrieval quality upgrades for Conversation AI. You can use tables, rich-text entries, file uploads, and an improved retrieval pipeline to help AI agents provide more accurate, context-aware answers at scale.

* * *

**TABLE OF CONTENTS**

  * What is the New Knowledge Sources Support?
  * Key Benefits of Knowledge Sources Support & Quality Upgrades
  * Smarter Retrieval with Re-Ranking
  * Expanded Data Type Support
  * Crystal-Clear Source Attribution
  * How To Setup & Use Knowledge Sources Support
  * Frequently Asked Questions
  * Related Articles


* * *

# **What is the New Knowledge Sources Support?**

  


HighLevel Knowledge Bases support multiple source types, including tables, rich text, file uploads, FAQs, web crawler sources, and web search sources. Conversation AI can use these sources to retrieve relevant information before generating a response. Retrieval improvements, including re-ranking, help prioritize the most relevant chunks so responses are more accurate and easier to review.

* * *

## **Key Benefits of Knowledge Sources Support & Quality Upgrades**

  


  * **Higher answer accuracy:** Automatic re-ranking ensures the most relevant information is retrieved before generating a response.  
  

  * **Faster rollout:** Add or replace data sources instantly without the need for retraining from scratch.  
  

  * **Flexible training:** Support for spreadsheets, rich-text documents, PDFs, and more expands what your AI can learn from.  
  

  * **Total transparency:** Every response includes clickable source links in the Response Info side drawer for full visibility.


* * *

## **Smarter Retrieval with Re-Ranking**

  


A lightweight ranking layer now sits between search and answer generation. After the initial vector search returns potential matches, the re-ranker scores each chunk for semantic closeness to the user’s question and sends only the top-ranked passages to the LLM. The result is fewer hallucinations and tighter, on-topic replies.

* * *

## **Expanded Data Type Support**

  


Your Knowledge Base can include several source types:  
  


  * **Tables:** Upload CSV files so AI can reference structured data such as pricing grids, product lists, customer records, or service details.  
  

  * **Rich Text:** Add manually written content directly in the editor, including documentation, policies, instructions, and FAQs.  
  

  * **File Upload:** Upload supported document files such as DOC, DOCX, and PDF. Text is extracted and indexed; embedded images are skipped.  
  

  * **Web Crawler, FAQ, and Web Search:** Use additional Knowledge Base source types when you want AI to reference website content, question-and-answer content, or web-based information.


* * *

## **Crystal-Clear Source Attribution**

  


Every AI response inside Conversations shows a “Response Info” icon. Click it to open the side drawer and view:  
  


  * The exact knowledge chunk(s) used.  
  

  * File or URL name, FAQ label, and timestamp.  
  

  * Quick-edit options to correct or replace the source on the fly.


* * *

## **How To Setup & Use Knowledge Sources Support**

  


###  _**Step 1:** Create or Open a Knowledge Base_

  


  1. Sign in to your sub‑account.  
  

  2. From the left‑hand menu, click on the **AI Agents** tab.  
  
![](https://jumpshare.com/share/xKUFkN6npwAxq0NBGb1O+/Screen+Shot+2025-10-03+at+5.44.29+PM.png)  
  

  3. Click on the **Knowledge Base** tab.  
  
![](https://jumpshare.com/share/gwW1qOgBvn3BuGjyhDnq+/Screen+Shot+2025-10-03+at+5.45.58+PM.png)  
  

  4. Click **\+ Create Knowledge Base** button**** to create a new one**.**  
  
**![](https://jumpshare.com/share/vu9ydypMMgBizdLzPptv+/Screen+Shot+2025-10-03+at+5.47.41+PM.png)**  
  

  5. or **Edit an existing Knowledge Base** by clicking the Knowledge Base **name** , or click the **three** **dots** and choose **Edit**.  
  
![](https://jumpshare.com/share/vF9mMFEswDPVZ1BLJGI7+/Screen+Shot+2025-10-03+at+5.49.25+PM.png)  
  


### _**Step 2:** Add Knowledge Sources_

  


  1. Click **\+ Add Source** button.  
  

  2. Choose the source type you want to add, such as Tables, Rich Text, File Upload, FAQ, Web Crawler, or Web Search, depending on the Knowledge Base content you want the AI to use.   
  

  3. Upload Tables, Files or add Rich Text.  
  
![](https://jumpshare.com/share/9lbg7UkhUECFSbkoFgnp+/GIF+Recording+2025-10-03+at+5.51.27+PM.gif)  
  


### _**Step 3:** Attach the Knowledge Base to a Conversation AI Bot_

  


  1. In AI Agents, click **Conversation****AI**.  
  

  2. Click on the **Agent****List** tab.  
  
![](https://jumpshare.com/share/7Yq8N30lXw3Ra3HgWwnA+/Screen+Shot+2025-10-03+at+5.57.01+PM.png)  
  

  3. To create a new bot, click **\+ Create Bot**. (Check out our detailed guide on [Setting Up Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004401>))  
  
![](https://jumpshare.com/share/i4OFgz9pOUOj6QGDzF3C+/Screen+Shot+2025-10-03+at+6.00.36+PM.png)  
  

  4. To edit an existing bot, click the **bot’s name** , or click the **three dots** and choose **Edit**.  
  
![](https://jumpshare.com/share/gAWYl39WHZ7u5kGdJVUT+/Screen+Shot+2025-10-03+at+6.01.35+PM.png)  
  

  5. Click on the **Bot****Training** tab  
  

  6. In Knowledge Base, select the Knowledge Base you just **created or updated**(including the new Rich Text, Tables, and Files sources).  
  
![](https://jumpshare.com/share/gBFRJrm2iZ5xxiGxKRvQ+/GIF+Recording+2025-10-03+at+6.06.29+PM.gifhttps://jumpshare.com/share/gBFRJrm2iZ5xxiGxKRvQ+/GIF+Recording+2025-10-03+at+6.06.29+PM.gif)  
  


### _**Step 4:** Test Knowledge Base Retrieval_

  


  1. Go to **AI Agents → Knowledge Base** and open the Knowledge Base you want to test.  
  

  2. Wait for newly added or updated content to finish processing or indexing.  
  

  3. Open the **Knowledge Base Retrieval Tester**.  
  

  4. Enter realistic customer-style questions.  
  

  5. Review the answer and retrieved sources.  
  

  6. Update your Knowledge Base if sources are missing, incomplete, outdated, or irrelevant.  
  

  7. Retest the same question to confirm the correct content is retrieved.  
  

  8. After retrieval looks correct, test the full Conversation AI bot experience from the bot testing window.  
  
![](https://jumpshare.com/share/O54smx8AAimKSN23CJUp+/Screen+Shot+2025-10-03+at+6.26.05+PM.png)  
  


### _**Step 5:** Inspect Which Knowledge Chunks Powered the Reply_

  


  1. From your sub‑account dashboard, go to **Conversations**.  
  

  2. **Open a conversation** where the Conversation AI bot posted a reply.  
  

  3. Next to that AI message, click **AI Response Info** button.  
  
![](https://jumpshare.com/share/Yz0eU8MG6IMNk66ionlP+/Screen+Shot+2025-10-03+at+6.31.47+PM.png)  
  

  4. Open **Knowledge Chunks** to see up to three chunks used for that answer.  
  
![](https://jumpshare.com/share/DrYl5yFdACC92Gkv9yVg+/Screen+Shot+2025-10-03+at+6.34.44+PM.png)


* * *

## **Frequently Asked Questions**

  


**Q:**Do I need to retrain the bot after adding a file, table, or other Knowledge Base source?**  
** No. After the source is saved and processing/indexing is complete, the Knowledge Base can retrieve the updated content. For best results, use the Knowledge Base Retrieval Tester to confirm the new source is being retrieved before relying on it in live conversations.

  


**Q: What file types are supported?**

PDF, DOC/DOCX, PPT/PPTX, TXT, and CSV (for tables).

  


**Q: What is the maximum number of columns that can be parsed in a table?  
** Import CSV files with up to **500** **columns** and **select** the **20** **most** **relevant** **columns**

  


**Q: Can I combine tables, rich text, and URLs in one knowledge base?**

Absolutely. The retrieval pipeline treats every chunk equally, then re-ranks for best match.

* * *

## **Related Articles**

  


  * [Conversation AI Bot - Explained](<https://help.gohighlevel.com/en/support/solutions/articles/155000001335>)  
  

  * [Setting Up Conversation AI](<https://help.gohighlevel.com/en/support/solutions/articles/155000004401>)  
  

  * [Training Your Conversation AI Bot](<https://help.gohighlevel.com/en/support/solutions/articles/155000004416>)  
  

  * [Conversation AI Agents Dashboard](<https://help.gohighlevel.com/en/support/solutions/articles/155000005427>)  
  

  * [How to Use Conversation AI to Book Appointments](<https://help.gohighlevel.com/en/support/solutions/articles/155000000210>)  
  

  * [AI Agents Knowledge Base Tables ](<https://help.gohighlevel.com/en/support/solutions/articles/155000006637>)

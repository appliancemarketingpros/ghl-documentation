# Automate Workflows with GHL MCP and N8N

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000007777-automate-workflows-with-ghl-mcp-and-n8n](https://help.gohighlevel.com/support/solutions/articles/155000007777-automate-workflows-with-ghl-mcp-and-n8n)  
**Category:** AI Employee  
**Folder:** MCP Server

---

GHL MCP now works with N8N out of the box, allowing you to connect HighLevel with N8N workflows without requiring custom plugins.

  


This integration simplifies how you build and automate workflows between both platforms, reducing setup time and complexity. This reduces setup complexity and allows faster automation between HighLevel and N8N.

* * *

## **What’s New**

  * Native compatibility between GHL MCP and N8N  
  


  * No custom plugins required  
  


  * Faster and simpler integration setup


* * *

## **How It Works**

  


You can now connect GHL MCP directly with N8N and begin automating workflows immediately.

  


This enables you to:  
  


  * Connect HighLevel data with N8N workflows  
  


  * Automate processes across both platforms  
  


  * Build integrations without additional development or plugins


* * *

## **How to Get Started**  
  


  1. Log in to your GHL MCP account  
  


  2. Configure your MCP connection inside your agent or client  
  


  3. Add your MCP endpoint and authentication headers  
  


  4. Configure your workflows within N8N  
  


  5. Test your workflow to confirm data is flowing correctly


* * *

## **Example: MCP Configuration**

  


Below is an example of how to configure your MCP endpoint and authentication headers inside your agent or client:  
  

    
    
    {  "mcpServers": {    "ghl-mcp": {      "url": "https://services.leadconnectorhq.com/mcp/",      "headers": {        "Authorization": "Bearer <your-token>",        "locationId": "<your-location-id>"      }    }  } }

  
This configuration includes:  
  


  * MCP server endpoint  
  


  * Authorization header (Bearer token)  
  


  * Optional locationId for scoped requests


* * *

## **Frequently Asked Questions**

  


**Do I need a custom plugin to use N8N with GHL MCP?**

No. The integration works out of the box without requiring any custom plugins.

  


**Can I use my existing N8N workflows?**

Yes. Existing N8N workflows can be used with GHL MCP.

  


**Is additional configuration required?**

No advanced setup is required beyond connecting the systems and configuring your workflows.

  


**What is the main benefit of this integration?**

It allows you to automate workflows between HighLevel and N8N quickly without needing custom development or plugins.

* * *

## **Related Articles**  
  


  * [How to Use the HighLevel MCP Server](<https://help.gohighlevel.com/en/support/solutions/articles/155000005741>)


#   


##

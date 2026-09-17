# Design Kits API – Brand Boards API v3

**Source URL:** [https://help.gohighlevel.com/support/solutions/articles/155000008331-design-kits-api-brand-boards-api-v3](https://help.gohighlevel.com/support/solutions/articles/155000008331-design-kits-api-brand-boards-api-v3)  
**Category:** Developer Resources  
**Folder:** Developer Resources

---

API Development

# Design Kits API – Brand Boards API v3

Programmatically manage design kits for HighLevel locations using the Brand Boards REST API v3 suite.

What You'll Learn

The Design Kits API enables marketplace developers to create, read, update, and delete design kits for a location via REST endpoints. Design kits contain brand design data including colors, fonts, and other visual elements that power Brand Boards inside HighLevel. 

  


You can find the Design Kits APIs [here](<https://marketplace.gohighlevel.com/docs/ghl/brand-boards/design-kits/>).

  


This article covers the six available endpoints, authentication requirements, and how the Design Kits API integrates with the broader Brand Boards API v3 suite.

Table of Contents

1

What is the Design Kits API?

2

Key Benefits

3

Available Endpoints

4

Authentication and Authorization

5

Related Articles

6

Frequently Asked Questions

1

## What is the Design Kits API?

The Design Kits API is a public REST API within the Brand Boards API v3 suite that allows marketplace developers to programmatically manage design kits for HighLevel locations. Design kits store brand design data such as colors, fonts, and other visual elements that are used throughout the HighLevel platform, particularly in Brand Boards and page building.

This API provides the same access to design kit data that users have through the Brand Boards interface inside the HighLevel application. Developers can create, retrieve, update, delete, and set default design kits for any location using standard REST operations.

The Design Kits API complements the Brand Voices v3 endpoints, which were released earlier under the same Brand Boards API v3 surface, providing comprehensive programmatic control over a location's brand assets.

2

## Key Benefits

The Design Kits API provides several advantages for marketplace developers and integration partners:

**Programmatic Management** — Create, read, update, and delete design kits without requiring manual interaction with the Brand Boards UI, enabling automation and bulk operations.

**External Integration** — Enable external developer applications and partner apps to manage a location's brand design data directly, supporting workflows that span multiple systems.

**Complete Brand Control** — Combined with the Brand Voices API, developers gain full programmatic access to both content (Brand Voices) and design (Design Kits) aspects of brand management.

**Standard OAuth 2.0 Security** — Uses the same authentication and authorization framework as other HighLevel marketplace APIs, ensuring consistent security practices across integrations.

**Versioned and Documented** — Part of the v3 API catalog with comprehensive documentation available in the HighLevel marketplace developer portal.

3

## Available Endpoints

The Design Kits API provides six REST endpoints under the base path `/brand-boards/locations/:locationId/design-kits`. All endpoints require a valid location ID in the path parameter.

Endpoint 1

GET /design-kits — List Design Kits for a Location

Retrieves all design kits associated with the specified location. Returns an array of design kit objects containing brand design data including colors, fonts, and other visual settings.

Endpoint 2

POST /design-kits — Create a Design Kit for a Location

Creates a new design kit for the specified location. Accepts design kit configuration data in the request body and returns the created design kit object with a unique identifier.

Endpoint 3

GET /design-kits/:designKitId — Get a Design Kit by ID

Retrieves a specific design kit using its unique identifier. Returns the complete design kit object including all brand design properties.

Endpoint 4

PATCH /design-kits/:designKitId — Update a Design Kit by ID

Updates an existing design kit with partial data. Only the properties included in the request body are modified. Returns the updated design kit object.

Endpoint 5

DELETE /design-kits/:designKitId — Delete a Design Kit by ID

Permanently removes a design kit from the location. This operation cannot be undone. Returns a confirmation response upon successful deletion.

Endpoint 6

POST /design-kits/:designKitId/default — Set Default Design Kit

Designates a specific design kit as the default for the location. Automatically unsets any previous default design kit. The default design kit is applied automatically when creating new branded assets.

4

## Authentication and Authorization

The Design Kits API uses standard OAuth 2.0 authentication, consistent with other HighLevel marketplace APIs. Developers must obtain a valid access token through the OAuth 2.0 authorization flow before making API requests.

All API requests must include the access token in the Authorization header using the Bearer token scheme. The token must have the appropriate scopes to access Brand Boards resources for the target location.

For detailed information on implementing OAuth 2.0 authentication with HighLevel's marketplace APIs, refer to the authentication documentation in the HighLevel developer portal.

5

## Related Articles

  * Brand Voices API – Managing Brand Voice Data Programmatically
  * Brand Boards Overview – Creating and Managing Brand Assets
  * OAuth 2.0 Authentication for HighLevel Marketplace APIs
  * HighLevel Marketplace Developer Portal – Getting Started


6

## Frequently Asked Questions

Q: What is a design kit in HighLevel?

A design kit is a collection of brand design data including colors, fonts, and other visual elements that define the look and feel of branded assets within HighLevel. Design kits are used in Brand Boards and throughout the platform to maintain consistent branding across pages, templates, and other content.

Q: Who can use the Design Kits API?

The Design Kits API is available to marketplace developers and integration partners who have registered applications in the HighLevel marketplace. Users must obtain proper OAuth 2.0 authorization to access design kit resources for specific locations.

Q: How does the Design Kits API relate to the Brand Voices API?

Both APIs are part of the Brand Boards API v3 suite. The Brand Voices API manages content-related brand data (tone, messaging, etc.), while the Design Kits API manages visual brand data (colors, fonts, etc.). Together, they provide complete programmatic access to a location's brand assets.

Q: Can I have multiple design kits for a single location?

Yes, a location can have multiple design kits. However, only one design kit can be set as the default at any time. When you set a design kit as default using the POST /design-kits/:designKitId/default endpoint, any previously designated default design kit is automatically unset.

Q: What happens when I delete a design kit?

Deleting a design kit permanently removes it from the location. This operation cannot be undone. If you delete a design kit that is currently set as the default, you will need to designate a new default design kit if one is required for your workflow.

Q: Where can I find the complete API documentation?

Complete API documentation including request/response schemas, parameters, and examples is available in the HighLevel marketplace developer portal at <https://marketplace.gohighlevel.com/docs/ghl/brand-boards/design-kits>.

Q: Is the Design Kits API versioned?

Yes, the Design Kits API is part of the Brand Boards API v3 suite and follows HighLevel's versioned API standards. This ensures stable, predictable behavior and allows developers to integrate with confidence that breaking changes will be communicated through proper versioning practices.

Q: Do I need separate authentication for the Design Kits API?

No, the Design Kits API uses the same OAuth 2.0 authentication system as other HighLevel marketplace APIs. Once you have obtained a valid access token with the appropriate scopes for Brand Boards resources, you can use it to access the Design Kits API endpoints.

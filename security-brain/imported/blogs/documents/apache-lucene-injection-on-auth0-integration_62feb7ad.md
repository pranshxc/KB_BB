---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-18_apache-lucene-injection-on-auth0-integration.md
original_filename: 2023-12-18_apache-lucene-injection-on-auth0-integration.md
title: Apache Lucene Injection on Auth0 Integration
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: 62feb7adb048ffe8778370f2423465bd81eaa2c1ec55de9b124e9137d4ef3aa6
text_sha256: 491c676f916f1cb18be00248bfdedc474a92365efdba081eb81bc5dc8bab333d
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Apache Lucene Injection on Auth0 Integration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-18_apache-lucene-injection-on-auth0-integration.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `62feb7adb048ffe8778370f2423465bd81eaa2c1ec55de9b124e9137d4ef3aa6`
- Text SHA256: `491c676f916f1cb18be00248bfdedc474a92365efdba081eb81bc5dc8bab333d`


## Content

---
title: "Apache Lucene Injection on Auth0 Integration"
url: "https://blog.stratumsecurity.com/2023/12/18/apache-lucene-injection-on-auth0-implementation/"
final_url: "https://blog.stratumsecurity.com/2023/12/18/apache-lucene-injection-on-auth0-implementation/"
authors: ["Colin McQueen"]
bugs: ["Lucene injection"]
publication_date: "2023-12-18"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 615
---

# Apache Lucene Injection on Auth0 Integration

  * [ ](/author/colin/)

#### [Colin McQueen](/author/colin/)

18 Dec 2023 • 2 min read

Share

Apache Lucene Injection was discovered on a past assessment this year and I learned that this vulnerability wasn't mentioned much online. The reason for this is probably because Lucene Injection is limited compared to SQL Injection. Lucene Injection can only be used to query the data (index) that the application is expected to query. This can be exploited if the index (equivalent to an SQL table) is sensitive and you're only supposed to see a subset of the index or certain fields.

## Application Background

The application is a multi-tenant system that stores user information for all tenants in Auth0. Reading online, [Auth0](https://auth0.com/docs/manage-users/user-search/v2?ref=blog.stratumsecurity.com) uses Lucene to query user information. The application web server called Auth0 to query users assigned to the current tenant to share cyber security incident cases with other users. This API is only supposed to query users under the tenant the user is assigned to but the user input wasn't being handled properly and allowed Lucene Injection.

## Exploiting Lucene Injection

The application returned error information that disclosed the Lucene query, which made it easier to exploit. The screenshot below shows the query that expects to return only users for one tenant.

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/12/apache-lucene-auth0-query-injection-1.png)Lucene query disclosed

The following screenshots demonstrate modifying the Lucene query to return other tenant users and a boolean-based condition to discover other fields on the user index in Auth0. For the latter, an empty JSON array would be returned if the field didn't exist.

![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/12/apache-lucene-auth0-query-injection-2.png)Lucene Injection to query all tenant users![](https://storage.ghost.io/c/3b/1b/3b1b83bf-194f-498a-acf4-016bfc6d6580/content/images/2023/12/column-exists.png)Lucene Injection to discover other fields on the user index

The following payloads were used to query all tenant users and other fields in Auth0.
  
  
  // Break out of query and query all users using the name field
  1)+OR+(name:*)+OR+(name:*
  
  // Perform a boolean-based condition checking if the user_metadata.country field exists
  1)+OR+(name:*)+AND+(_exists_:user_metadata.country
  
  // Discover values searching one character at a time
  1)+OR+(name:*)+AND+(user_metadata.country:C*
  1)+OR+(name:*)+AND+(user_metadata.country:Ca*
  ...
  

The last two payloads could be used to query custom fields under app_metadata or user_metadata or to query other [Auth0](https://auth0.com/docs/manage-users/user-accounts/user-profiles/user-profile-structure?ref=blog.stratumsecurity.com) fields (phone numbers, IP addresses, ...).

## Remediation

Reading online, there was mention that Lucene supports prepared statements like SQL. As this was an integration with Auth0, the client likely encoded special characters before passing the user input to Auth0 to prevent the injection.

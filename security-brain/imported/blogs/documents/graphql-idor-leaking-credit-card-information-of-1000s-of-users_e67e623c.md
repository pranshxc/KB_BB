---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-20_graphql-idorleaking-credit-card-information-of-1000s-of-users.md
original_filename: 2022-12-20_graphql-idorleaking-credit-card-information-of-1000s-of-users.md
title: '[GraphQL IDOR]Leaking credit card information of 1000s of users'
category: documents
detected_topics:
- rate-limit
- idor
- command-injection
- graphql
tags:
- imported
- documents
- rate-limit
- idor
- command-injection
- graphql
language: en
raw_sha256: e67e623cac9af213e5c89f6ded35399aaea1f96dc1f26ab03c3f00e294d9f034
text_sha256: 6aa11f602b5a99158abecdc5f3b4a5b13c91b023b4376357c96ff81b7ebf58bd
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# [GraphQL IDOR]Leaking credit card information of 1000s of users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-20_graphql-idorleaking-credit-card-information-of-1000s-of-users.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, command-injection, graphql
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `e67e623cac9af213e5c89f6ded35399aaea1f96dc1f26ab03c3f00e294d9f034`
- Text SHA256: `6aa11f602b5a99158abecdc5f3b4a5b13c91b023b4376357c96ff81b7ebf58bd`


## Content

---
title: "[GraphQL IDOR]Leaking credit card information of 1000s of users"
page_title: "[GraphQL IDOR] Leaking credit card information of 1000s of users [External Audit] | by Vipul Sahu | InfoSec Write-ups"
url: "https://infosecwriteups.com/graphql-idor-leaking-credit-card-information-of-1000s-of-users-d07eec732979"
authors: ["Vipul Sahu"]
bugs: ["IDOR", "GraphQL"]
bounty: "1,500"
publication_date: "2022-12-20"
added_date: "2022-12-23"
source: "pentester.land/writeups.json"
original_index: 1760
scraped_via: "browseros"
---

# [GraphQL IDOR]Leaking credit card information of 1000s of users

[GraphQL IDOR] Leaking credit card information of 1000s of users [External Audit]
Vipul Sahu
Follow
3 min read
·
Dec 20, 2022

103

Hey everyone

I was hunting on a web application. The program was private; for obvious reasons, let’s say the domain is redacted.com. I was able to find mass information by exploiting two different Graphql endpoints.

Press enter or click to view image in full size
Finding Graphql IDOR

While performing initial recon on redacted.com, I found the web application used GraphQL for its API management.

For converting the query to a readable format, I used the graphql raider extension, which converts the graphql query and variables from the unreadable JSON body to a readable format in which the query and variables are displayed in separate tabs. Graphql raider extracted the ‘id’ variable as an insertion point. The response to this request contains users’ personal information, including credit card information.

I created two accounts and checked for IDOR. The application was vulnerable to IDOR, and I was able to get the personal information for my other account.

Spotting a Weird functionality

ID variable is a 12-character long string, so I cannot guess/brute-force the value. I was searching for a way to get my hand on the id parameter, went through the burp suite repeater tabs, and found an exciting endpoint. The endpoint fetched my following list, and the response contains the id value and profile picture of the users I follow.

Get Vipul Sahu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When a user creates an account on redacted.com, the user automatically follows some company executives.

When I clicked on the follower list of these executives, a graphql query was sent that fetches information from the user’s profile, and the response contains the user’s ID and profile picture of many users. I found a user with a million followers, which can also be exploited.

Press enter or click to view image in full size
Exploitation

I collected an ‘id’ from the response of the following list of the company executive to create the POC.

Press enter or click to view image in full size

I observed no protection against brute force attacks for the graphql queries. After this, I grabbed the IDs using bash scripting and brute-forced using the burp Intruder and got thousands of users’ sensitive data.

Disclosure

Reported on 26th December 2020

Linkedin: https://www.linkedin.com/in/vipul-sahu-a7a420174/

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

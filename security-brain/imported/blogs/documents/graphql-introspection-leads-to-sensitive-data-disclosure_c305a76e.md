---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-30_graphql-introspection-leads-to-sensitive-data-disclosure.md
original_filename: 2019-10-30_graphql-introspection-leads-to-sensitive-data-disclosure.md
title: GraphQL introspection leads to sensitive data disclosure.
category: documents
detected_topics:
- graphql
- command-injection
- path-traversal
- information-disclosure
- api-security
tags:
- imported
- documents
- graphql
- command-injection
- path-traversal
- information-disclosure
- api-security
language: en
raw_sha256: c305a76e1ce8a054817d62e2e0e1ac7d05a81913b05b76af218fbf176da5cfd2
text_sha256: ed24250dcc285f34d519c6e760291638f5c71050b2c7669d087ada219449d864
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# GraphQL introspection leads to sensitive data disclosure.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-30_graphql-introspection-leads-to-sensitive-data-disclosure.md
- Source Type: markdown
- Detected Topics: graphql, command-injection, path-traversal, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `c305a76e1ce8a054817d62e2e0e1ac7d05a81913b05b76af218fbf176da5cfd2`
- Text SHA256: `ed24250dcc285f34d519c6e760291638f5c71050b2c7669d087ada219449d864`


## Content

---
title: "GraphQL introspection leads to sensitive data disclosure."
url: "https://medium.com/@R0X4R/graphql-introspection-leads-to-sensitive-data-disclosure-714f1d9d9d4a"
authors: ["Eshan Singh (@R0X4R)"]
bugs: ["Information disclosure"]
publication_date: "2019-10-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4964
scraped_via: "browseros"
---

# GraphQL introspection leads to sensitive data disclosure.

Top highlight

GraphQL introspection leads to sensitive data disclosure.
Eshan Singh
Follow
3 min read
·
Oct 30, 2019

257

4

Press enter or click to view image in full size
source: lynda.com

Introduction

Hello World! I’m Eshan Singh, aka R0X4R. I’m that hacker teenager that your friends told you about. I hack web-server to make the system secure. I’m here to share my recent findings on GraphQL Introspection.

What is GraphQL

All of us know that Facebook uses its own query language to store its data properly. So, according to GraphQL.org GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need, and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

About this vulnerability

For Discovering this bug, I learned the fundamentals of GraphQL for at least 5–6 hours and read all other relevant bug reports, especially Namhamsec’s GraphQL CTF Challenge.

After that, I saw a new program on Bugcrowd, so I participated in it. They gave me a domain [let’s take the domain as example.com because the vulnerability hasn’t fixed yet], i.e. example.com. So I make an account on that domain, then fire burpsuite and added example.com for spidering; after 10–20 secs, I saw that the example.com/graphql, so I got an idea that example.com uses Graphql for their API management.

source: almostdumb.com

Tools that I used in this

Burpsuite
Burpsuite Extensions — JSON Beautifier and GraphQL Raider
A Web Browser [Firefox] :P

How I got the vulnerability

Get Eshan Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First I logged out and logged in again on example.com, then I went to the ‘Update Profile’ section and changed my name from Eshan Singh to Singh Eshan and clicked save. And, then intercepted that request and sent it repeater, then I saw something interesting i.e.

Press enter or click to view image in full size

__typename with PayRollAdmin, so I replaced it with xyz then I again send the request and then checked the response xyz reflects on PayRollAdmin place.

So, for digging more into this, I googled GraphQL Exploits, then I saw a Hackerone disclosed the vulnerability, i.e. https://hackerone.com/reports/291531. So I thought let’s try the same that this guy did on this report.

I googled Introspection GraphQL Payloads, and I got this from PayloadAllTheThings repo:

Press enter or click to view image in full size
Press enter or click to view image in full size

Then I copied the payload and pasted it on graphql tab in burpsuite and sent the request, and walla! I got a juicy response.

source: https://tenor.com/view/omg-oh-my-god-wow-gif-11411674

Impact of this

The application is basically used by payrolls and HR. So when I exploit it I was able to retrieve receipt of transactions and users passwords phone numbers and more

Thanks and regards

Eshan Singh [R0X4R]

Signing out…

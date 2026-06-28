---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-04_getting-email-address-of-any-hackerone-user-worth-7500.md
original_filename: 2023-07-04_getting-email-address-of-any-hackerone-user-worth-7500.md
title: Getting email address of any HackerOne user worth $7,500
category: documents
detected_topics:
- command-injection
- otp
- graphql
- csrf
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- otp
- graphql
- csrf
- information-disclosure
- api-security
language: en
raw_sha256: 748ce53489d921468a439540af15c867d2616ae4872534bc8359075212e4e90a
text_sha256: 0cb18ad13a78273ea8c5e1a73262e41782b75654c956ec706b72372538c8909e
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Getting email address of any HackerOne user worth $7,500

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-04_getting-email-address-of-any-hackerone-user-worth-7500.md
- Source Type: markdown
- Detected Topics: command-injection, otp, graphql, csrf, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `748ce53489d921468a439540af15c867d2616ae4872534bc8359075212e4e90a`
- Text SHA256: `0cb18ad13a78273ea8c5e1a73262e41782b75654c956ec706b72372538c8909e`


## Content

---
title: "Getting email address of any HackerOne user worth $7,500"
url: "https://medium.com/pinoywhitehat/getting-email-address-of-any-hackerone-user-worth-7-500-afb8076ee395"
authors: ["Japz Divino (@japzdivino)"]
programs: ["HackerOne"]
bugs: ["Information disclosure"]
bounty: "7,500"
publication_date: "2023-07-04"
added_date: "2023-07-04"
source: "pentester.land/writeups.json"
original_index: 970
scraped_via: "browseros"
---

# Getting email address of any HackerOne user worth $7,500

Member-only story

Featured

Getting email address of any HackerOne user worth $12,500
Japz Divino
Follow
5 min read
·
Jul 4, 2023

353

1

Severity: High (7.5)
Weakness: Sensitive Information Disclosure
Bounty: Duplicate (First researcher receives $12,500)

Hey hunters, I’m back!

Just wanna share my recent finding in HackerOne’s own bug bounty program. This finding is pretty much straight forward :)

After submitting a report on HackerOne, I’ve added my brother hackerone.com/r3y to the collaborator and observed that the UI for adding collaborators was changed — see below (hhmm interesting).

Press enter or click to view image in full size
New user interface when you add a collaborator

When I am seeing updates, I always try to play with it so I capture the request while adding collaborator and observed this new GraphQL query “operationName”:”ReportCollaboratorQuery”

I took 3 analysts usernames including Co-Founder Jobert’s hackerone username to test for PoC purposes and record the proof-of-concept.

Upon checking the response, I noticed that the email address of all collaborators was disclosed despite I used their hackerone username only to invite them on the report.

POST /graphql HTTP/2
Host: hackerone.com
Cookie: <redacted>
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer:<redacted>
Content-Type: application/json
X-Csrf-Token: <redacted>
X-Product-Area: other
X-Product-Feature: other…

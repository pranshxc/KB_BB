---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-05_csrf-poc-mistake-that-broke-crucial-functions-for-the-end-uservictim.md
original_filename: 2020-08-05_csrf-poc-mistake-that-broke-crucial-functions-for-the-end-uservictim.md
title: CSRF PoC mistake that broke crucial functions for the end user/victim
category: documents
detected_topics:
- business-logic
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- business-logic
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 65327ea291e5b2d3f7898aa5e06e0af2b6d916f6ded7f8078adaa5465cfd077c
text_sha256: c325df03e871ca8bc295979d18bd34860e4be3deb6e9f1cc44eb0fd5af1c1692
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF PoC mistake that broke crucial functions for the end user/victim

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-05_csrf-poc-mistake-that-broke-crucial-functions-for-the-end-uservictim.md
- Source Type: markdown
- Detected Topics: business-logic, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `65327ea291e5b2d3f7898aa5e06e0af2b6d916f6ded7f8078adaa5465cfd077c`
- Text SHA256: `c325df03e871ca8bc295979d18bd34860e4be3deb6e9f1cc44eb0fd5af1c1692`


## Content

---
title: "CSRF PoC mistake that broke crucial functions for the end user/victim"
url: "https://medium.com/bugbountywriteup/csrf-poc-mistake-that-broke-crucial-functions-for-the-end-user-victim-ef4fa4584ca8"
authors: ["Vuk Ivanovic"]
bugs: ["Logic flaw"]
publication_date: "2020-08-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4351
scraped_via: "browseros"
---

# CSRF PoC mistake that broke crucial functions for the end user/victim

Member-only story

CSRF PoC mistake that broke crucial functions for the end user/victim
Vuk Ivanovic
Follow
4 min read
·
Aug 5, 2020

6

You have heard of business logic bugs. The idea of abusing the logic behind the website’s functionality in order to achieve something like a discount or similar that you shouldn’t be able to do, i.e. https://hackerone.com/reports/336131 and similar, none of it is really new. Then, there are other logic errors that I have not seen in the past. Could be I wasn’t looking where I should have been looking.

This is about a very curious logical bug, in my opinion. It is a whole new way to mess with the underlying logic, depending on how the website is coded. In this case, it “only” breaks some of the website’s functionality for the end user/victim, and it can be triggered through csrf. I actually discovered it by pure accident/error in my coding of the csrf PoC.

CSRF Discovery:

The simplest test for csrf is: You follow burp’s request headers, see there’s no x-csrf or other custom headers (if there are, you remove them, and verify that the request still goes through as it should), no Origin limitation, no Referer limitation, etc. Finally, the request body is verified to either has no csrf token or csrf token isn’t being properly validated. Then comes the fun part.

CSRF PoC, and a mistake:

Having verified that there were no limitations/protections from csrf through headers and parameters, I proceeded with getting PoC ready. It was a simple html form, but it had an interesting logic. I’ll try to…

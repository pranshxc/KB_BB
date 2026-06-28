---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-09_read-other-user-support-tickets-in-httpssupportcom-write-up.md
original_filename: 2019-08-09_read-other-user-support-tickets-in-httpssupportcom-write-up.md
title: Read other user support tickets in https://support..com (Write Up)
category: documents
detected_topics:
- idor
- command-injection
- api-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
language: en
raw_sha256: 01ce9104c3d993b271cb10e0d69fc9967b96512d43dc9a2a085b7bdc22e6e8c6
text_sha256: 69d8d4b7e9f15eca1451df8c54335ce354db10e490ae5c56ec13ed4808b8fcdc
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Read other user support tickets in https://support..com (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-09_read-other-user-support-tickets-in-httpssupportcom-write-up.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `01ce9104c3d993b271cb10e0d69fc9967b96512d43dc9a2a085b7bdc22e6e8c6`
- Text SHA256: `69d8d4b7e9f15eca1451df8c54335ce354db10e490ae5c56ec13ed4808b8fcdc`


## Content

---
title: "Read other user support tickets in https://support..com (Write Up)"
page_title: "Evan Ricafort | Blog: Read other user support tickets in https://support..com (Write Up)"
url: "https://blog.evanricafort.com/2019/08/read-other-user-support-tickets-in.html"
final_url: "https://blog.evanricafort.com/2019/08/read-other-user-support-tickets-in.html"
authors: ["Evan Ricafort (@evanricafort)"]
bugs: ["IDOR"]
bounty: "120"
publication_date: "2019-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5090
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVC5iwXY1x0-d-dsruvFy_t_gvyttMvIUFkm1UG1FVhFUUfjSqNPlI2-6wRwo-4Q31rs_gwtY_LnPCfuVtfqVL1xDVOnDaI7qspenSADhdSb5ASfCfT5WuYkIOat2VYSisAAYX2odp/s640/Screenshot_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVC5iwXY1x0-d-dsruvFy_t_gvyttMvIUFkm1UG1FVhFUUfjSqNPlI2-6wRwo-4Q31rs_gwtY_LnPCfuVtfqVL1xDVOnDaI7qspenSADhdSb5ASfCfT5WuYkIOat2VYSisAAYX2odp/s1600/Screenshot_1.png)

  
Howdy!  
  
In this article I will show you how I found a Insecure Direct Object Reference Vulnerability that I found in a private program on Bugcrowd few years ago. The vulnerability allow me to access any support tickets without any restriction by just enumerating/changing the ticket IDs. The vulnerability feature was the ticket printing on the support dashboard.  
  
This issue was reported to a private program on bugcrowd few years ago and closed as Won't fix.  
  
So below is the report timeline and proof of concept of the issue.  
  
_**\--Proof of Concept--**_  
  
1\. Go to https://support.<REDACTED>.com  
2\. Create a ticket  
3\. Print your ticket and you will get the ff. url.  
Vulnerable URL:_https://support. <REDACTED>.com/client/ticket/print/**< ticket id>**_  
  
The ticket ID is composed of five numbers so using BurpSuite intruder, I was able to enumerate to check every single ticket which allowed me to read other users Email Address, Username, Message and etc...  
  
Result: Insecure Direct Object Reference Vulnerability.  
  
_**\--Report Timeline--**_  
  
Report Title: Read any support ticket on with restriction  
Reported: 20, June 2017  
Closed: 21, July 2017  
Reward: $120  
  

> _thank you for the submission. We are awarding the bounty. However, this was scheduled to go offline before your submission, so we are likely not going to fix this one.  
>  Happy hunting!_

  
So I hope you enjoy this write up, have a great day everyone!  
  

_**“It is better to be hated for what you are than to be loved for what you are not.”**  
― Andre Gide, Autumn Leaves _

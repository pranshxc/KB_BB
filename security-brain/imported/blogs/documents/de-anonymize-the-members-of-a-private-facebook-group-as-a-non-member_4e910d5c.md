---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-15_de-anonymize-the-members-of-a-private-facebook-group-as-a-non-member.md
original_filename: 2021-03-15_de-anonymize-the-members-of-a-private-facebook-group-as-a-non-member.md
title: De-anonymize the members of a private Facebook Group as a non-member.
category: documents
detected_topics:
- command-injection
- graphql
- information-disclosure
tags:
- imported
- documents
- command-injection
- graphql
- information-disclosure
language: en
raw_sha256: 4e910d5c74bfe8414ae6b166f4ee5ad3b7e97e4946741dcdf21b9eb7bd680a1d
text_sha256: 39ee4cb7e96cb07b3205d0cdb88399261c6b0912db5a9253952e79bcef77adb4
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# De-anonymize the members of a private Facebook Group as a non-member.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-15_de-anonymize-the-members-of-a-private-facebook-group-as-a-non-member.md
- Source Type: markdown
- Detected Topics: command-injection, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `4e910d5c74bfe8414ae6b166f4ee5ad3b7e97e4946741dcdf21b9eb7bd680a1d`
- Text SHA256: `39ee4cb7e96cb07b3205d0cdb88399261c6b0912db5a9253952e79bcef77adb4`


## Content

---
title: "De-anonymize the members of a private Facebook Group as a non-member."
page_title: "Baibhav Anand Jha"
url: "https://baibhavjha.com.np/blogs/facebookgroupmemberdisclosure/"
final_url: "https://baibhavjha.com.np/blogs/facebookgroupmemberdisclosure/"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["GraphQL", "Information disclosure"]
bounty: "4,500"
publication_date: "2021-03-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3817
---

# [Baibhav Anand Jha ](/)

##  

#### $~# whoami  
![](https://baibhavjha.com.np/images/spongebhav.png) Baibhav Anand Jha  
I do bug-bounties  
I develop  
I learn  
I hack  
He/Him  
  
  

[![](https://baibhavjha.com.np/images/twitter.png)](https://twitter.com/spongebhav) [![](https://baibhavjha.com.np/images/github.png)](https://github.com/baibhavanand) [![](https://baibhavjha.com.np/images/facebook.png)](https://facebook.com/spongebhav) [![](https://baibhavjha.com.np/images/contact.png)](https://baibhavjha.com.np/contact)

# De-anonymize the members of a private Facebook Group as a non-member.

_March 15 | 2 Minutes Read_  
  
  
  

## Description:

A Non-member can determine if someone is the member of a private group or not via **CometHovercardQueryRendererQuery** graphQL mutation. Doc_ID: **4997502340291357**. By changing the actorID with the victim’s actorID and groupID with the group we want to test and in the response if it shows **WeakEntityReference** than he/she is not the member of the group. However, if it shows **StrongEntityReference** than he/she is the member of the group.

  
  

## Steps Of Reproduction:

  1. From a non-member’s account send this request by replacing the actorID variable to that of the victim and groupID variable to that of the group which you want to test against.  
![](https://miro.medium.com/max/1400/1*RnfaWLUIc53IlJ8363NVkQ.png)
  2. If you get **"StrongEntityReference"** in response. He/She is the member of the group. However, If you get **"WeekEntityReference”** in the response he she is not the member of the group. Using this technique you can find out if someone is a member of the private group or not.

  
  

## Timeline

Report Submitted:
  Saturday, January 30, 2021 at 11:42 PM
Triaged:
  Monday, February 1, 2021 at 8:18 PM
Fixed:
  Tuesday, February 2, 2021 at 5:39 PM
Bounty Awarded ($4500):
  Tuesday, February 16, 2021 at 10:28 PM

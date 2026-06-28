---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-15_disclosing-the-members-of-private-facebook-group-as-a-non-member.md
original_filename: 2020-12-15_disclosing-the-members-of-private-facebook-group-as-a-non-member.md
title: Disclosing the members of private Facebook Group as a non-member.
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: a567116e92347cad65a783ba75408064a0b7e12f051617925d8794cdfc2f63d5
text_sha256: 203715b40fc4683197e559f16831bb786cff0121d214f51ee3db67d417ab5a4f
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Disclosing the members of private Facebook Group as a non-member.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-15_disclosing-the-members-of-private-facebook-group-as-a-non-member.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `a567116e92347cad65a783ba75408064a0b7e12f051617925d8794cdfc2f63d5`
- Text SHA256: `203715b40fc4683197e559f16831bb786cff0121d214f51ee3db67d417ab5a4f`


## Content

---
title: "Disclosing the members of private Facebook Group as a non-member."
page_title: "Baibhav Anand Jha"
url: "https://baibhavjha.com.np/blogs/fblitegroupmemberdisclosure/"
final_url: "https://baibhavjha.com.np/blogs/fblitegroupmemberdisclosure/"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "4,500"
publication_date: "2020-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4069
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

# Disclosing the members of private Facebook Group as a non-member.

_December 15 | 2 Minutes Read_  
  
  
  

## Description

It was possible to know if someone was a member of a private group or not via the group profile view endpoint in Facebook lite.  
  

## Steps of Reproduction

  1. From User A account in Fblite (while I am the member of the group) I open the group.  

  2. From User A account in my PC (I leave the group).  

  3. Now when I click on members profile (I cannot see the group posts but I can see the membership dates).  

  4. Now I see the membership date of User B and User C after leaving the group.  

  5. From User B account in my PC I leave the group.  

  6. Now we will notice that membership date for User B disappeared as User B was no longer the member of the group but membership date for User C was still there.  

  7. Now to further confirm the vulnerability from User C account in my PC I left the group.  

  8. Now we will notice that the membership date also disappeared for User C, confirming the vulnerability.  
  

## Timeline

Reported:
  Sunday, November 8, 2020 at 1:15 AM
Triaged:
  Sunday, November 8, 2020 at 4:46 PM
Fixed:
  Tuesday, November 10, 2020 at 10:10 PM
Bounty Awarded ($4500)
  Tuesday, December 15, 2020 at 5:58 AM

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-22_page-owners-cant-remove-or-change-page-roles-of-deactivated-users-or-if-attacker.md
original_filename: 2021-04-22_page-owners-cant-remove-or-change-page-roles-of-deactivated-users-or-if-attacker.md
title: Page Owners Can’t remove or change page roles of deactivated users (or if Attacker
  blocks the page owner) in Facebook Lite, Facebook for Android and touch.facebook.com
category: documents
detected_topics:
- command-injection
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- business-logic
- mobile-security
language: en
raw_sha256: e9b86b2810fca314ca20bddc86705dd69a0bd63d7a98cfd8a573908dc77b820b
text_sha256: c1df1b00221f3ac9050fde3c6025caea3e97cac028dc8f1e23c09b33e40a5f2b
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Page Owners Can’t remove or change page roles of deactivated users (or if Attacker blocks the page owner) in Facebook Lite, Facebook for Android and touch.facebook.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-22_page-owners-cant-remove-or-change-page-roles-of-deactivated-users-or-if-attacker.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `e9b86b2810fca314ca20bddc86705dd69a0bd63d7a98cfd8a573908dc77b820b`
- Text SHA256: `c1df1b00221f3ac9050fde3c6025caea3e97cac028dc8f1e23c09b33e40a5f2b`


## Content

---
title: "Page Owners Can’t remove or change page roles of deactivated users (or if Attacker blocks the page owner) in Facebook Lite, Facebook for Android and touch.facebook.com"
page_title: "Baibhav Anand Jha"
url: "https://baibhavjha.com.np/blogs/deactivateduserspageroles/"
final_url: "https://baibhavjha.com.np/blogs/deactivateduserspageroles/"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "525"
publication_date: "2021-04-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3711
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

# Page Owners Can’t remove or change page roles of deactivated users (or if Attacker blocks the page owner) in Facebook Lite, Facebook for Android and touch.facebook.com

_April 22 | 2 Minutes Read_  
  
  
  

## Description

If the attacker deactivates his account or blocks the Page Owner, Page Owner will not be able to remove or change the attacker’s page role in Facebook Lite, Facebook for Android and touch.facebook.com.  
  

## Impact

Attacker can gain consistent access to the page.  
  

## Setup

Users:  
UserOne  
UserTwo  
  

## Environment:

PageOne with Owner UserOne and admins UserOne and UserTwo.  
  

## Steps of Reproduction

  1. As UserOne, Create a Page, PageOne  

  2. Add UserTwo as the admin of PageOne  

  3. UserTwo deactivates his account or blocks UserOne  

  4. UserOne will now not be able to remove UserTwo’s page role or change his page role in Facebook Lite, Facebook for Android and touch.facebook.com  
  

## FBDL
  
  
  [setup]
  User UserOne
  User UserTwo
  Page PageH with {owner: UserOne, admins: [UserTwo]}
  
  [action]
  UserTwo deactivate_account UserTwo
  

  
  

## Timeline:

Reported
  Sunday, December 20, 2020
Pre-Triaged
  Wednesday, December 23, 2020 at 4:35 AM
Triaged
  Friday, December 25, 2020 at 10:32 AM
Fixed
  Monday, March 1, 2021 at 11:21 PM
Bounty Awarded. ($525) - including bonus
  Thursday, April 22, 2021 at 10:51 PM

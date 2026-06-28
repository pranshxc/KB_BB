---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-23_hiding-ourself-in-close-friends-list-and-avoiding-victim-to-remove-us-from-his-c.md
original_filename: 2020-04-23_hiding-ourself-in-close-friends-list-and-avoiding-victim-to-remove-us-from-his-c.md
title: Hiding ourself in close friend’s list and avoiding victim to remove us from
  his close friend’s list.
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
raw_sha256: 310b61c44b4eebd1aff672ff91aaa85d182e655a3578a48f474aad8d6b9ecb73
text_sha256: 3079819099164346d90b9d7f1f55206cd96f947e54d26865bcdfd13d7de98192
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Hiding ourself in close friend’s list and avoiding victim to remove us from his close friend’s list.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-23_hiding-ourself-in-close-friends-list-and-avoiding-victim-to-remove-us-from-his-c.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `310b61c44b4eebd1aff672ff91aaa85d182e655a3578a48f474aad8d6b9ecb73`
- Text SHA256: `3079819099164346d90b9d7f1f55206cd96f947e54d26865bcdfd13d7de98192`


## Content

---
title: "Hiding ourself in close friend’s list and avoiding victim to remove us from his close friend’s list."
page_title: "Baibhav Anand Jha"
url: "https://baibhavjha.com.np/blogs/hidinginclosefriendlist/"
final_url: "https://baibhavjha.com.np/blogs/hidinginclosefriendlist/"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "500"
publication_date: "2020-04-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4637
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

# Hiding ourself in close friend’s list and avoiding victim to remove us from his close friend’s list.

_April 23 | 2 Minutes Read_  
  
  
  

## Description:

There is a feature in Facebook called close friend’s list which you can find here: https://www.facebook.com/bookmarks/lists this allows you to add someone as a close friend. Exploiting this will allow someone to hide oneself in the close friend’s list and not allow victim to remove them from the close friend’s list.  
  

## Setup

Users: UserOne (Attacker) UserTwo (Victim)  
  

## Environment:

UserOne is in the close friend’s list of UserTwo.  
  

## Steps Of Reproduction:

  1. UserOne (Attacker) is in the close friend list of UserTwo (Victim).  

  2. UserOne deactivates his account.  

  3. UserTwo will no longer be able to see UserOne in his close friend’s list.  

  4. UserOne reactivated his account and he will still be in the close friend’s list of UserTwo.  
  

## Timeline:

Reported
  Friday, March 13, 2020 at 5:23 PM
Triaged
  Monday, April 13, 2020 at 2:45 PM
Fixed
  Tuesday, April 14, 2020 at 9:03 AM
Bounty Awarded ($500)
  Thursday, April 23, 2020 at 4:20 PM

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-24_hiding-from-custom-story-privacy-list-is-possible-in-fblite-making-the-victim-un.md
original_filename: 2020-12-24_hiding-from-custom-story-privacy-list-is-possible-in-fblite-making-the-victim-un.md
title: Hiding from custom story privacy list is possible in FBlite making the victim
  unable to remove you from the list.
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 9c4d795780b8c3475b0a7dc648c9cf6a901953f168520223ec083660419c3a66
text_sha256: 1e8e81806678ec71cd70cf075060d00e6365d6fa3a6eb65262587402d581b786
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Hiding from custom story privacy list is possible in FBlite making the victim unable to remove you from the list.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-24_hiding-from-custom-story-privacy-list-is-possible-in-fblite-making-the-victim-un.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `9c4d795780b8c3475b0a7dc648c9cf6a901953f168520223ec083660419c3a66`
- Text SHA256: `1e8e81806678ec71cd70cf075060d00e6365d6fa3a6eb65262587402d581b786`


## Content

---
title: "Hiding from custom story privacy list is possible in FBlite making the victim unable to remove you from the list."
page_title: "Baibhav Anand Jha"
url: "https://baibhavjha.com.np/blogs/hidingfromcustomlistfblite/"
final_url: "https://baibhavjha.com.np/blogs/hidingfromcustomlistfblite/"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2020-12-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4051
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

# Hiding from custom story privacy list is possible in FBlite making the victim unable to remove you from the list.

_December 24 | 2 Minutes Read_  
  
  
  

## Description:

Attacker can hide himself in the custom story privacy settings in Facebook Lite app making victim unable to remove him from the list, and the attacker will automatically be on the next custom list of the victim custom story settings.  
  

## Impact:

Victim will be unable to remove attacker from the custom story privacy settings allowing attacker to still be on the custom list for new stories that victim uploads. Since victim won’t be able to see that attacker is in that list and will not be able to remove the attacker, after victim uploads a new story and decides to change the custom list, the attacker will still be on the new list without victim’s knowledge.  
  

## Reproduction Steps:

  1. From User A (victim’s) account, upload a story with a custom privacy settings adding User B(attacker) and User C (random user).  

  2. User B (attacker) will now deactivate his account.  

  3. User A (victim) (in FacebookLite app) will upload another story next time and will think of making changes to the custom list but he won’t be able to find the attacker in that list.  

  4. User B (attacker) will be able to continue to be in the custom story privacy list.  
  

## Timeline:

Reported:
  Sunday, September 27, 2020 at 11:48 AM
Pre-Triaged:
  Tuesday, September 29, 2020 at 7:00 AM
Triaged:
  Wednesday, September 30, 2020 at 1:34 AM
Fixed:
  Friday, November 6, 2020 at 12:32 AM
Improper Fix:
  Friday, November 6, 2020 at 12:35 PM
Triaged Again:
  Tuesday, November 10, 2020 at 1:13 AM
Bounty Awarded For First Issue. ($500)
  Thursday, November 12, 2020 at 9:18 PM
Second Issue Patched:
  Monday, December 7, 2020 at 11:59 PM
Bounty Awarded For Second Issue. ($500)
  Thursday, December 24, 2020 at 12:40 AM

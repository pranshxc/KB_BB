---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-11_hiding-from-a-custom-list-is-possible-on-who-sees-our-post-is-possible-making-vi.md
original_filename: 2020-12-11_hiding-from-a-custom-list-is-possible-on-who-sees-our-post-is-possible-making-vi.md
title: Hiding from a custom list is possible on who sees our post is possible making
  victim not remove them from the list.
category: blogs
detected_topics:
- command-injection
- business-logic
tags:
- imported
- blogs
- command-injection
- business-logic
language: en
raw_sha256: f3626fc010f48f230b2423829c8cb47810ee02d8630b911d03173bf9fd0a1b42
text_sha256: 7a4b436725d45f07855ad41dbf3d74b2be78d8a610e1fd71340ed5509b0a3bf0
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Hiding from a custom list is possible on who sees our post is possible making victim not remove them from the list.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-11_hiding-from-a-custom-list-is-possible-on-who-sees-our-post-is-possible-making-vi.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `f3626fc010f48f230b2423829c8cb47810ee02d8630b911d03173bf9fd0a1b42`
- Text SHA256: `7a4b436725d45f07855ad41dbf3d74b2be78d8a610e1fd71340ed5509b0a3bf0`


## Content

---
title: "Hiding from a custom list is possible on who sees our post is possible making victim not remove them from the list."
page_title: "Baibhav Anand Jha"
url: "https://baibhavjha.com.np/blogs/hidingcustomlist/"
final_url: "https://baibhavjha.com.np/blogs/hidingcustomlist/"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2020-12-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4077
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

# Hiding from a custom list is possible on who sees our post is possible making victim not remove them from the list.

_December 11 | 2 Minutes Read_  
  
  
  

## Description:

Attacker can hide in the specific friends list so that victim can’t see him while updating the list in the next post and attacker will be able to see the next post as well since victim couldn’t see him/her resulting in him/her not being removed while updating the specific people list while posting next post.  
  

## Steps of Reproduction:

  1. When posting we see specific friends in the privacy settings.  

  2. User A adds User B along with many other users in this setting for a post.  

  3. User B (attacker deactivates his account).  

  4. User A won’t be able to remove user B (attacker) now while updating the specific friends list for a new post.  
  

## Timeline:

Reported
  Sunday, September 6, 2020 at 12:23 AM
Pre-Triaged
  Tuesday, September 15, 2020 at 4:07 AM
Triaged
  Tuesday, September 15, 2020 at 7:33 AM
Bounty Awarded ($500)
  Thursday, November 12, 2020 at 9:36 PM
Fixed
  Friday, December 11, 2020 at 10:25 AM

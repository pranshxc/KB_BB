---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-21_reply-to-instagram-stories-where-privacy-of-who-can-reply-is-set-to-nobody-part-.md
original_filename: 2019-11-21_reply-to-instagram-stories-where-privacy-of-who-can-reply-is-set-to-nobody-part-.md
title: Reply To Instagram Stories where privacy of who can reply is set to ‘Nobody’.
  (Part 2)
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 754176ec3c3252cced9ba3fa1209b64ba2ab753f84c6c2002ef66c7d989cdcf8
text_sha256: 4b403cbb40131de0f87588e75e0024c33cf45ecb65a6f2a28dbcd4eb3090a57c
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Reply To Instagram Stories where privacy of who can reply is set to ‘Nobody’. (Part 2)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-21_reply-to-instagram-stories-where-privacy-of-who-can-reply-is-set-to-nobody-part-.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `754176ec3c3252cced9ba3fa1209b64ba2ab753f84c6c2002ef66c7d989cdcf8`
- Text SHA256: `4b403cbb40131de0f87588e75e0024c33cf45ecb65a6f2a28dbcd4eb3090a57c`


## Content

---
title: "Reply To Instagram Stories where privacy of who can reply is set to ‘Nobody’. (Part 2)"
page_title: "Baibhav Anand Jha"
url: "https://baibhavjha.com.np/blogs/instagramstory2/"
final_url: "https://baibhavjha.com.np/blogs/instagramstory2/"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "1,000"
publication_date: "2019-11-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4926
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

# Reply To Instagram Stories where privacy of who can reply is set to ‘Nobody’. (Part 2)

_October 21 | 2 Minutes Read_  
  
  
  

## Description

Attacker was able to reply to Instagram stories where who can reply to the story privacy was set to ‘Nobody’. It is the bypass of my previous report.  
  

## Steps of Reproduction

Step 1: Open the story of an Instagram account which appears before the story of the victim account ( as shown in the POC video attached)  
Step 2: While watching the story of the Instagram account before the victim’s account manage to pop up keyboard somehow, it can be done by many ways. (In the POC I have used a 3rd party app to manually pop up the keyboard).  
Step 3: Let the Instagram story of the victim load.  
Step 4: Boom! There is a reply option from which by selecting the image option we can reply to the story.  
  

## Timeline

Reported
  Monday, May 20, 2019 at 5:42 PM
Pre-triaged
  Saturday, May 25, 2019 at 2:27 AM
Triaged
  Friday, June 7, 2019 at 7:25 PM
Fixed
  Thursday, October 3, 2019 at 7:41 PM
Bounty Awarded ($1000)
  Monday, October 21, 2019 at 4:00 PM

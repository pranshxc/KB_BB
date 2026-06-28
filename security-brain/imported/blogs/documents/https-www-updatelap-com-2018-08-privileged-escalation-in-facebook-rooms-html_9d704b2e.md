---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-18_httpswwwupdatelapcom201808privileged-escalation-in-facebook-roomshtml.md
original_filename: 2018-08-18_httpswwwupdatelapcom201808privileged-escalation-in-facebook-roomshtml.md
title: https://www.updatelap.com/2018/08/privileged-escalation-in-facebook-rooms.html
category: documents
detected_topics:
- access-control
- command-injection
- graphql
tags:
- imported
- documents
- access-control
- command-injection
- graphql
language: en
raw_sha256: 9d704b2eaa6f4dc38ff27b72e620e617565b6142bc6a7de73870c9b7955d12f4
text_sha256: 908dcb54d3d4904f33389aaeca1b758e4e86b2c20a5f8e4b0b2bca653e8df462
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# https://www.updatelap.com/2018/08/privileged-escalation-in-facebook-rooms.html

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-18_httpswwwupdatelapcom201808privileged-escalation-in-facebook-roomshtml.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, graphql
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `9d704b2eaa6f4dc38ff27b72e620e617565b6142bc6a7de73870c9b7955d12f4`
- Text SHA256: `908dcb54d3d4904f33389aaeca1b758e4e86b2c20a5f8e4b0b2bca653e8df462`


## Content

---
title: "https://www.updatelap.com/2018/08/privileged-escalation-in-facebook-rooms.html"
page_title: "Privileged Escalation in Facebook Messenger Rooms - Update - أب ديت"
url: "https://www.updatelap.com/2018/08/privileged-escalation-in-facebook-rooms.html"
final_url: "https://www.updatelap.com/2018/08/privileged-escalation-in-facebook-rooms.html"
authors: ["Jafar Abo Nada (@Jafar_Abo_Nada)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Privilege escalation"]
publication_date: "2018-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5744
---

Privileged Escalation in Facebook Rooms Reject user's request to join the Facebook Chat Rooms without having to be the admin.

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhF1L5O-_okA7S2KDROaEUrcnvU6NqF93ijbgHhikLXbnc-oQAKxNBIhpcirUTv9oOKrEJju4O_UV8QWwC7hJ03ENXwPue_BofjWrzFtLyX41M8GPGo9fDaEjj6XmrAzzxtyOYz-704Md90/s640/facebook-messenger-bug.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhF1L5O-_okA7S2KDROaEUrcnvU6NqF93ijbgHhikLXbnc-oQAKxNBIhpcirUTv9oOKrEJju4O_UV8QWwC7hJ03ENXwPue_BofjWrzFtLyX41M8GPGo9fDaEjj6XmrAzzxtyOYz-704Md90/s1600/facebook-messenger-bug.jpg)

  

###  Vulnerability Type:

###  
Privilege Escalation/bypass authorization 

###  
Product Area:

###  
Messenger

  

  

Description/Impact

  
After digging around in Facebook looking for possible bug’s, I came across Messenger Rooms Each room has an administrator who has all the permissions to control almost all of these permissions, for example rejecting or accepting requests to enter the room  
  
After poking around in the HTTP Requests, I found that the endpoint for rejecting a user  
requesting. wasn’t verifying that the user making the POST request was actually an admin of the chat.  
  
So as long as you were in the chat you could send a POST Request to  
("<https://www.messenger.com/api/graphqlbatch/>") and set "thread_id=" On the target room and set the "user_id=" to that of the user you wanted to reject and it would go through. 

  

**Reproduction** Steps:

  
1) attacker intercepts the request to Reject a member to a room  
2) attacker changes the &thread_id to the The target room  
3) attacker changes the &user_id to the The target User  
4) attacker forwards the request and User is out from the room.

  

  

Videos Proof of Concept  
  

  
  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgi-zEdB3ALJxQmkV29i35hyroWg1Pw31LVDavCCRZXqxgaLAp18udKcyAGER5uaurQ_H3L4Z4-E01xj8c8EqqNkNU2F-EOToYGk8wG7leeaPsdzSES9z8yfQRP1rHqr5suD_xBF_44wWrd/s640/Bug+Mas.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgi-zEdB3ALJxQmkV29i35hyroWg1Pw31LVDavCCRZXqxgaLAp18udKcyAGER5uaurQ_H3L4Z4-E01xj8c8EqqNkNU2F-EOToYGk8wG7leeaPsdzSES9z8yfQRP1rHqr5suD_xBF_44wWrd/s1600/Bug+Mas.JPG)

**TimeLine:**

  

18/May/2018 Report Sent

22/May/2018 Initial Response by Facebook/Bug Confirmed by Facebook

12/Jul/2018  Facebook sending it to the appropriate product team for further investigation

01/Aug/2018  Bug fixed and response by Facebook

02/Aug/2018 Confirmation of fix by me

18/Aug/2018 Bounty awarded

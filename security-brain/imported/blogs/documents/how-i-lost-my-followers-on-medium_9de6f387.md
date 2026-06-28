---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-17_how-i-lost-my-followers-on-medium.md
original_filename: 2020-07-17_how-i-lost-my-followers-on-medium.md
title: How I lost my followers on Medium
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
raw_sha256: 9de6f3876a7eb6f1386529bb521790fcb7e49057c954e4231f5c23098c12ae2e
text_sha256: 85ec368991532e420ed28a7a104064343863c3d4ab256eebdb71ebb998ce5904
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I lost my followers on Medium

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-17_how-i-lost-my-followers-on-medium.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, graphql
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `9de6f3876a7eb6f1386529bb521790fcb7e49057c954e4231f5c23098c12ae2e`
- Text SHA256: `85ec368991532e420ed28a7a104064343863c3d4ab256eebdb71ebb998ce5904`


## Content

---
title: "How I lost my followers on Medium"
url: "https://medium.com/bugbountywriteup/how-i-lost-my-followers-on-medium-9fe10e9862aa"
authors: ["Florian (@fh4ntke)"]
programs: ["Medium"]
bugs: ["GraphQL", "Broken authorization"]
publication_date: "2020-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4404
scraped_via: "browseros"
---

# How I lost my followers on Medium

Member-only story

How I lost my followers on Medium
A bug bounty report
FHantke
Follow
3 min read
·
Jul 17, 2020

168

2

I was writing a new article on Medium when I started procrastinating and looking at the traffic this website is producing. Knowing there is a bug bounty program on Medium that I was awarded before, I thought maybe I am lucky once again and decided to play around with the following and unfollowing calls.

The GraphQL API

Medium uses GraphQL, initially developed by Facebook, to communicate with parts of their API and inform the database about follow and unfollow requests. To do so, only the target user-id is required, user authentication is verified via auth cookies. As answer a request, the server would reply with a JSON object as a result, including the key “isFollowing” either set to true or false. Below we see the two requests and responses:

Request:
POST /_/graphql HTTP/1.1
{
 "operationName":"followUser",
 "variables":{"targetUserId":"abc123"},
 "query":"mutation followUser($targetUserId: ID!) {\n followUser(targetUserId: $targetUserId) {\n id\n isFollowing\n __typename\n }\n}\n"
}
Response:
HTTP/1.1 200 OK
{
 "data":{
  "followUser":{
  "id":"abc123",
  "isFollowing":true,
  "__typename":"User"
  }
 }
}
Request:
POST /_/graphql HTTP/1.1
{
 "operationName":"unfollowUser",
 "variables":{"targetUserId":"abc123"}…

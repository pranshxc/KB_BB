---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-06_how-i-got-access-to-1600k-users-pii-data-.md
original_filename: 2022-04-06_how-i-got-access-to-1600k-users-pii-data-.md
title: How i got access to 1600k Users PII Data $$$$
category: documents
detected_topics:
- api-security
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- api-security
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: f9d5a9f83eb9e40e57f9d7dd7617b919e2b77db3d995ee662bd9eba98b05e208
text_sha256: 3574d995b51b57dba4dda4d680f0f0bdce9fe0b3b835d3e74495f6acd0c9f233
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How i got access to 1600k Users PII Data $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-06_how-i-got-access-to-1600k-users-pii-data-.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `f9d5a9f83eb9e40e57f9d7dd7617b919e2b77db3d995ee662bd9eba98b05e208`
- Text SHA256: `3574d995b51b57dba4dda4d680f0f0bdce9fe0b3b835d3e74495f6acd0c9f233`


## Content

---
title: "How i got access to 1600k Users PII Data $$$$"
url: "https://gokulap.medium.com/how-i-got-access-to-1600k-users-pii-data-64a27a540963"
authors: ["Gokul AP (@CodingGokul)"]
bugs: ["Information disclosure"]
bounty: "1,500"
publication_date: "2022-04-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2737
scraped_via: "browseros"
---

# How i got access to 1600k Users PII Data $$$$

How i got access to 1600k Users PII Data $$$$
Gokul AP
Follow
3 min read
·
Apr 6, 2022

620

9

Hello Guys 👋 I am Gokul, Python developer, Cyber security researcher, Part time Bug hunter and Open source tool maker, Studying 3rd year Computer Science Engineering in Madurai, Tamilnadu !

My Social Media links :

Github : https://github.com/gokulapap
LinkedIn : https://linkedin.com/in/gokulap
Twitter : https://twitter.com/CodingGokul
Instagram : https://instagram.com/gokulapap

Hey Let’s dive into the main topic, This is my first Blog post and i have been trying to make this writeup from long time but didn’t get time to make it, now we got it ready !

By the title you might have guessed the content, let’s see how i found that vulnerability and let’s take that target as target.com

On one Evening i was testing that target and i like to find bugs related to Session management and Logical errors, so i was testing a login feature and fired my burp and i was just manipulating the requests to see any sensitive actions/response but didn’t get anything and usually i will use Intercept, Repeater and Intruder alone in Burp, That day i decided to view the Burp HTTP History and saw all history of URLs logged there and i was just scrolling there and was seeing the response which contained JSON, but nothing sensitive !

Then saw a request /app.js in that history tab and i decided to view the source code (Because, most of the js files have unreadable names like fabi65c78.js etc..) but this app.js caught my eye, Usually filename app is kept to main files, so i was scrolling through the source code of that js file, Then i have seen a json inside that js file which had something like zendesk URL, FB App ID etc..

At first sight, I thought FBAppId is some Private data then researched about it and found that its just a public data, Then got “access token” in that same json and i have seen that it was Base64 Encoded so decoded the token and the result i got was “senior@target.com/token:xxxxxxxx” Then used Keyhacks repo and found that it was Zendesk api key !

It was my first API Key finding and i was so excited and I was like

Then i was about to report that to the Security team ! But my Mind :
“You got API key, but what’s it’s for ?”, I didn’t have any idea about what is Zendesk or didn’t know how to even use that API key. So made a little research about it so that i can increase the Impact, So refered many sites and got one documentation, In that it had https://{target}.zendesk.com/api/v1/users.json and i decided to authenticate this API endpoint against the API key, so first i have curled it, curl https://{target}.zendesk.com/api/v1/users.json

Get Gokul AP’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Response was :

{"error":"Couldn't authenticate you"}

Then I used the API key, curl https://{target}.zendesk.com/api/v1/users.json -u (API_KEY)

{
  "id": 123xxxxx,
  "name": "Victim",
  "email": "victim@gmail.com",
  "created_at": "2015-11-25T06:00:20Z",
  "updated_at": "2015-11-25T06:00:20Z",
  "time_zone": "Ekaterinburg",
  "iana_time_zone": "Asia/Yekaterinburg",
  "phone": xxxxxxxxxx,
  "shared_phone_number": null,
  "photo": null,
  "locale_id": 1,
  "locale": "en-US",
  "organization_id": null,
  "role": "end-user",
  "verified": false,
  "external_id": null,
  "tags": [],
  "alias": null,
  "active": true,
  "shared": false,
  "shared_agent": false,
  "last_login_at": null,
  "two_factor_auth_enabled": false,
  "signature": null,
  "details": null,
  "notes": null,
  "role_type": null,
  "custom_role_id": null,
  } 
} "system::embeddable_last_seen": null
..........
..........
  "count" : 1645729
}

I have got access to PII Details of Around 16 Lakh users !

Timeline :

Reported : March 6th 2022
Triaged : March 10th 2022
Confirmation : March 14th 2022
Bounty : 1500$

Tips :

Always check Burp history
Don’t report as soon as you find, increase the impact and then report

Thanks for Reading my writeup, I will make more writeups in the Future !

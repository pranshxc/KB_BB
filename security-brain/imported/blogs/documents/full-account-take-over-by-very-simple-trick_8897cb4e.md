---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-16_full-account-take-over-by-very-simple-trick.md
original_filename: 2023-01-16_full-account-take-over-by-very-simple-trick.md
title: Full Account Take Over by very simple trick.
category: documents
detected_topics:
- access-control
- command-injection
- mfa
tags:
- imported
- documents
- access-control
- command-injection
- mfa
language: en
raw_sha256: 8897cb4e6377dd04d66ad7c4b58cbe41ab0f7d4d3ffaca6eac1dd2facb62965f
text_sha256: 35515041c75c155cd8a7a8b55fbd759560b5fadaed77abf67a01ebd19a441401
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Full Account Take Over by very simple trick.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-16_full-account-take-over-by-very-simple-trick.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mfa
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `8897cb4e6377dd04d66ad7c4b58cbe41ab0f7d4d3ffaca6eac1dd2facb62965f`
- Text SHA256: `35515041c75c155cd8a7a8b55fbd759560b5fadaed77abf67a01ebd19a441401`


## Content

---
title: "Full Account Take Over by very simple trick."
url: "https://medium.com/@xerox0x1/full-account-take-over-by-very-simple-trick-b4025a53047c"
authors: ["XeRox01 (@xerox0x1)"]
bugs: ["Account takeover", "Broken Access Control"]
publication_date: "2023-01-16"
added_date: "2023-01-18"
source: "pentester.land/writeups.json"
original_index: 1668
scraped_via: "browseros"
---

# Full Account Take Over by very simple trick.

Full Account Take Over by very simple trick.
Osama
Follow
3 min read
·
Jan 16, 2023

313

1

H
i, This is @xerox0x1, This is my first write-up, So pardon me if anything slipped. And Have fun!

Press enter or click to view image in full size
# Summary

To be with me; The program is a platform that runs multiple assets for any business. Every assigned company to the program have account and there are dozens of user roles under every account.

Now, you have an overview about what we are dealing with, let’s move to the next part.

As usual, I’ve started to look for Access Control bugs first, because they are the easier. So, quickly I double checked on all user roles — manipulating requests, responses, dorking for any hidden endpoints on search engines, Way back machine, alien vault…..etc”

Get Osama’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Unfortunately, All user roles where handled securely and there was nothing else to be done in such a case, Till I noticed The request of creating a new user in the platform. It was like this,

Press enter or click to view image in full size

Let me break down the marked values for you:-
1-) “platform” : the platform that you want to assign this user with it. “platform ID = account ID”
2-) “uzrole” : The role that will be assigned to that user. As a bad hacker would think I’ve chosen the user role that gives that user the full access to the platform.
3-) “allowedplatforms” : Now this is the most dangerous one. BUT WHY??
• You can add any number of platform IDs you want in this JSON. How many IDs we are talking about?? “countless!! “, look down here.

Press enter or click to view image in full size
I’ve added a couple of platforms in the “allowedplatforms” section and forwarded the request, Because I’ve checked nearly all requests on the same criteria, I was definitely sure that it won’t work, but the surprise it DID WORK!!. It got 200 OK. And the response was something like this.
HTTP/2 200 OK
Date: Sun, 15 Jan 2023 22:33:58 GMT
Content-Type: application/json; charset=utf-8

{
  "reference": {
  "name": "self",
  "value": "lysa@email.com"
  },
  "address": {
  "location": {
  "type": "Point",
  "geometry": []
  },
  "addressLines": [],
  "geocodeScore": 0,
  "cleanScore": 0
  },
  "login": {
  "failedAttempts": 0,
  "history": [],
  "lastActivity": "2023-01-15T22:33:58.285Z",
  "passwordHistory": []
  },
  "rating": {
  "count": 0,
  "total": 0
  },
  "position": {
  "type": "Point",
  "isMock": false
  },
  "start": {
  "type": "none",
  "now": 0
  },
  "timesheet": {
  "days": [],
  "breaks": []
  },
  "status": "VALIDATED",
  "termsAccepted": false,
  "allowedPlatforms": [
  "62fa62057dadb00012f34e9f",
  "62fa62057dadb00012f34e3a",
  "62fa6204f45cbb00112075d5"
  ],
  "gender": "UNKNOWN",
  "passwordHashAlgorithm": "bcrypt",
  "verifiedPassword": true,
  "hubs": [],
  "preferredZones": [],
  "external": false,
  "classic": true,
  "express": false,
  "scheduler": false,
  "roundStartpoint": "default",
  "roundEndpoint": "default",
  "skills": [],
  "unavailable": false,
  "availabilities": [],
  "collectionPoints": [],
  "_id": "63c47f561f30d030e2bf92da",
  "email": "lysa@email.com",
  "firstName": "Lysa",
  "lastName": "Aren",
  "invitationCode": "NNH05LsgkgpePhdJ",
  "uzrole": "572894aeb3d4620cd97a0ede",
  "platform": "62fa62057dadb00012f34e9f",
  "language": "en-001",
  "password": "$2a$10$hIm1199JHi7vZuJBPiHQGOLuEQmRdryffrUilYPQh9nSh8xq0pXVm",
  "pin": "efd926ba52b4e4431a6a173e0e731d2cddec0dfc50f30492ceadfff89af31f67",
  "externalId": "1234",
  "phoneNumber": "12341234",
  "emailCheck": {
  "valid": false
  },
  "phoneNumberCheck": {
  "valid": false
  },
  "when": "2023-01-15T22:33:58.285Z",
  "updated": "2023-01-15T22:33:58.292Z",
  "attachments": [],
  "devices": [],
  "workingTimes": [],
  "holidays": [],
  "__v": 0,
  "id": "63c47f561f30d030e2bf92da"
}
Take a closer look at the “allowedplatfroms” in the response.

• I’ve checked on the platforms that I assigned their IDs earlier in the request, when refreshing the page I’ve found the user I created assigned to these platforms with full-privilege on the account.
• To make sure that everything is right I logged with this user on a couple of platforms and she was logged in with the full privilege. From there we can do anything delete admins, modify stuff, remove the entire account…etc

Unfortunately, The vulnerability was a dup, but I’ve came up with something from it

Conclusion.
• Access control always wins.
• Always try the simplest things, usually the vulnerability is too obvious, You just need to dig well.
• The last advice which is quoted from @stok

“ALWAYS and I mean ALWAYS go for impact!”

That’s it, I thought this vulnerability worth to have a write-up. I hope you enjoyed reading.

Thanks.

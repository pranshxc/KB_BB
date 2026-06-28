---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-16_javascript-analysis-leading-to-admin-portal-access.md
original_filename: 2020-12-16_javascript-analysis-leading-to-admin-portal-access.md
title: JavaScript analysis leading to Admin portal access
category: documents
detected_topics:
- access-control
- jwt
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- jwt
- command-injection
- otp
- api-security
language: en
raw_sha256: f31108617027e4f4b1e3b1acf9612501002047d2048093bcbe0ad449edc46b6f
text_sha256: a6c3904857cad3bd7545b1c5bdf87f9b0ab66df1660849940dfb1477c15101d4
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# JavaScript analysis leading to Admin portal access

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-16_javascript-analysis-leading-to-admin-portal-access.md
- Source Type: markdown
- Detected Topics: access-control, jwt, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `f31108617027e4f4b1e3b1acf9612501002047d2048093bcbe0ad449edc46b6f`
- Text SHA256: `a6c3904857cad3bd7545b1c5bdf87f9b0ab66df1660849940dfb1477c15101d4`


## Content

---
title: "JavaScript analysis leading to Admin portal access"
url: "https://rikeshbaniyaaa.medium.com/javascript-analysis-leading-to-admin-portal-access-ea30f8328c8e"
authors: ["Rikesh Baniya (@rikeshbaniya)"]
bugs: ["Broken authorization", "Broken Access Control"]
publication_date: "2020-12-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4066
scraped_via: "browseros"
---

# JavaScript analysis leading to Admin portal access

JavaScript analysis leading to Admin portal access
Rikesh Baniya
Follow
1 min read
·
Dec 16, 2020

183

1

I love hunting on small scoped websites cause i can be assured that i have seen every corner and analyzed every endpoint of the that website

Program had 2 scopes.

target.com and admin.target.com

Now, since the website had not provided any credentials for admin.target.com i didn't have anything to test on that scope.

After hunting on target.com i found an endpoint named “meUser”.
As soon as i saw that i felt that i have found something.

Now, the only way to know if there is an endpoint named “meAdmin” was to do by analyzing the targets js file

After downloading all the js files I was manually going though them, and guess what.

I was right.

Now, reading the js file I found that this endpoint takes a jwt token value.

Get Rikesh Baniya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With no hope of success I supplied the jwt token i got from “target.com”.

and guess what. I was wrong.

The endpoint was taking the jwt token from a non-priviliged user and in response was giving me information like name,age,phone etc and the mistake it made was it provided me with another jwt token.

Hmmmm,intresting.

What could this token potentially mean.

I further analyzed the js files and found bunch of other endpoints like:
GetUser,GetLocation etc

and all those endpoints were accessible from that token.

It was a realllly intresting and fun bug to exploit.

Thanks for reading :)

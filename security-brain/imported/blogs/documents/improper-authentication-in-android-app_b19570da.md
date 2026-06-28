---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-10_improper-authentication-in-android-app.md
original_filename: 2023-03-10_improper-authentication-in-android-app.md
title: Improper Authentication in Android App
category: documents
detected_topics:
- jwt
- access-control
- xss
- command-injection
- otp
- cors
tags:
- imported
- documents
- jwt
- access-control
- xss
- command-injection
- otp
- cors
language: en
raw_sha256: b19570daa26c50204da8236d7cd191b78abd16b9525f10646be0b4d02d0021bb
text_sha256: c5e8b488106124dad6d0b99f175776bc818a8f60d7ab6219c7c691b9892f141a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# Improper Authentication in Android App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-10_improper-authentication-in-android-app.md
- Source Type: markdown
- Detected Topics: jwt, access-control, xss, command-injection, otp, cors
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `b19570daa26c50204da8236d7cd191b78abd16b9525f10646be0b4d02d0021bb`
- Text SHA256: `c5e8b488106124dad6d0b99f175776bc818a8f60d7ab6219c7c691b9892f141a`


## Content

---
title: "Improper Authentication in Android App"
url: "https://medium.com/@oXnoOneXo/improper-authentication-in-android-app-aa855227e6f1"
authors: ["oXnoOneXo"]
bugs: ["Logic flaw", "Broken authentication", "HTTP response manipulation"]
publication_date: "2023-03-10"
added_date: "2023-03-21"
source: "pentester.land/writeups.json"
original_index: 1395
scraped_via: "browseros"
---

# Improper Authentication in Android App

Improper Authentication in Android App
oXnoOneXo
Follow
2 min read
·
Mar 11, 2023

32

[+] Hello friend, This article will be about a simple Improper Authentication vulnerability that allowed me to bypass the lockout behavior of the application on the users’ accounts. The program was providing several accounts with different roles, One of them was Shipper role. I tried to sign into the app and the login request was a Basic Authentication. When i was trying to login i was facing the following pop-up:

The request was like:

POST /hub/login HTTP/1.1
Host: api.stage.target.com
Authorization: Basic ZGFzaGlw***REDACTED-SUSPECT-TOKEN***Da-Source: app.android
Content-Type: application/json
Content-Length: 0
Accept-Encoding: gzip, deflate
User-Agent: okhttp/4.9.1
Connection: close

The server returned the JWT of the account and the refresh-token including some fields but the most important field was verified, It was assigned with a null value like here:

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: null
Cache-Control: no-cache
Content-Type: application/json; charset=utf-8
Date: Fri, 06 Jan 2023 17:15:20 GMT
Set-Cookie: hub-token=#DATA
Set-Cookie: refresh-token=#DATA
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Vary: accept-encoding,Origin
X-Frame-Options: DENY
X-Xss-Protection: 1; mode=block
Content-Length: 2620
Connection: Close

{--SNIP--,"verified":null,--SNIP--}

When i tried to login with the other accounts using the android application there were no problems but i noticed the verified field in the returned response was true, So i tried to do edit the returned response of shipper(disabled)account request by changing the null=>true and i managed to login successfully and the MainActivity opened:

Thank you for reading, I hope if it was kinda helpful and see you soon❤.

Get oXnoOneXo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Linkedin: https://www.linkedin.com/in/abd-elmonsef-sobhy-58542a1a7/
Facebook: https://www.facebook.com/0xno0nex0

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-14_sql-injection-in-the-http-custom-header.md
original_filename: 2023-06-14_sql-injection-in-the-http-custom-header.md
title: SQL Injection in The HTTP Custom Header
category: documents
detected_topics:
- idor
- access-control
- sqli
- command-injection
- otp
- api-security
tags:
- imported
- documents
- idor
- access-control
- sqli
- command-injection
- otp
- api-security
language: en
raw_sha256: 3a595dcfd2e827453b0618a95a7d806eb666a233d62b28d5153d895b61f04821
text_sha256: 479b49b4bd5cea5538bb88638a5bb449cb0521ec5a7fe922856b8a3e77070b65
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection in The HTTP Custom Header

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-14_sql-injection-in-the-http-custom-header.md
- Source Type: markdown
- Detected Topics: idor, access-control, sqli, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `3a595dcfd2e827453b0618a95a7d806eb666a233d62b28d5153d895b61f04821`
- Text SHA256: `479b49b4bd5cea5538bb88638a5bb449cb0521ec5a7fe922856b8a3e77070b65`


## Content

---
title: "SQL Injection in The HTTP Custom Header"
url: "https://infosecwriteups.com/sql-injection-in-the-http-custom-header-fd117ba1435e"
authors: ["yoshi m lutfi (@yoshiahmadlutfi)"]
bugs: ["SQL injection"]
publication_date: "2023-06-14"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1046
scraped_via: "browseros"
---

# SQL Injection in The HTTP Custom Header

SQL Injection in The HTTP Custom Header
yoshi m lutfi
Follow
2 min read
·
Jun 14, 2023

920

6

It has been a long time since my last write-up. in this short write up I wanna share my last year's findings about SQL Injection that I found in the custom HTTP header request.

Get yoshi m lutfi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, I was doing my API penetration testing for a target. let's say redacted.com and after successful login, the request has one more HTTP header in the request, User header, and the value is a username that login to the application.

POST /abcd/abcd
Authorization: token
Host: redacted.com
User: user.abc
Postman-Token: token
...

{body request}

Now, I try to change the username for IDOR possibility but the server validates it by giving a message with a 500 internal error code and an error message that cannot get this API access.

Press enter or click to view image in full size
Error message when changing the User value

Because this parameter is validated it is potential also for SQL Injection, so I put basic SQL Injection to the request ‘ OR 1=1- - and send the request and with ease, the server accepts the request and gives valid information. No way :D

Press enter or click to view image in full size
The request was accepted by the server

Okay, we got a valid SQL Injection and of course sqlmap will do the rest. But with this vulnerability, it turns out that we can also request to the server without an authorization token.

Press enter or click to view image in full size
Successful request without Authorization token

I hope you can take some points from my write-up, and I am sorry for being inactive for a couple of months. Have a nice day and keep learning!

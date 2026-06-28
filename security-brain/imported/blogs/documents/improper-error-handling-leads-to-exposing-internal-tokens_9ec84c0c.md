---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-28_improper-error-handling-leads-to-exposing-internal-tokens.md
original_filename: 2022-11-28_improper-error-handling-leads-to-exposing-internal-tokens.md
title: Improper error handling leads to exposing internal tokens
category: documents
detected_topics:
- information-disclosure
- access-control
- sqli
- command-injection
- otp
- api-security
tags:
- imported
- documents
- information-disclosure
- access-control
- sqli
- command-injection
- otp
- api-security
language: en
raw_sha256: 9ec84c0cdfbb52c537dbd98ccfa1ac15e3964775a0c93b2c941ca454d7bf4b62
text_sha256: 477829713e94e1607e9890d1c62f3bf5d1aaacecc7a2f28e9a4567a77c9f07ac
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Improper error handling leads to exposing internal tokens

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-28_improper-error-handling-leads-to-exposing-internal-tokens.md
- Source Type: markdown
- Detected Topics: information-disclosure, access-control, sqli, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `9ec84c0cdfbb52c537dbd98ccfa1ac15e3964775a0c93b2c941ca454d7bf4b62`
- Text SHA256: `477829713e94e1607e9890d1c62f3bf5d1aaacecc7a2f28e9a4567a77c9f07ac`


## Content

---
title: "Improper error handling leads to exposing internal tokens"
url: "https://medium.com/@aa.pietruczuk/improper-error-handling-leads-to-exposing-internal-tokens-3355d6b43a32"
authors: ["Agnieszka Pietruczuk"]
bugs: ["Information disclosure"]
publication_date: "2022-11-28"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1846
scraped_via: "browseros"
---

# Improper error handling leads to exposing internal tokens

Improper error handling leads to exposing internal tokens
Agnieszka Pietruczuk
Follow
2 min read
·
Nov 29, 2022

111

1

Recently I started using a new application for secret management. Let the name be [redacted].

I often try to poke around the app just to see if I find any obvious errors. When I tried to access the API without Authorization header one thing caught my attention. The “stack” property was appended to the response body.

{
"status": 401,
"errorCode": "",
"errorClass": "NotAuthenticated",
"stack": "NotAuthenticated\n at /usr/src/app/lib/services/userService.js:56:15\n at Generator.throw (<anonymous>)\n at rejected (/usr/src/app/lib/services/userService.js:6:65)\n at runMicrotasks (<anonymous>)\n at processTicksAndRejections (node:internal/process/task_queues:96:5)"
}

This is usually a bad sign. It’s already showing me a path to the application and the functions names are leaking info about used libraries and sometimes their versions. Also the info in error messages will help attackers use undocumented API.

But it didn’t give me much more to work with. I was trying to cause more crashes and see if there’s anything interesting. The database error would be a good match but the input validation was pretty solid.

Get Agnieszka Pietruczuk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried to test for SQL injection but I was getting a Bad Request response with warnings about illegal characters. And then something unexpected happened. My request passed the backend validation and returned a new type of bug. It was something like this:

{
"error": {
"response": {
"config": {
"url": "https://admin.googleapis.com/admin/directory/v1/users?query=x%40y.com%22%2BOR%2B1%3D1--&maxResults=500&domain=y.com",
"method": "GET",
"userAgentDirectives": [
{
}
],
"headers": {}

The backend was sending requests to Google APIs to fetch more data about the user. Google responded with 400 code that was not handled by the application. The whole error was dumped with response and request headers:

Authorization header!

At first I thought they used my token, but they actually had a backend token for internal communication. This one had additional scopes: admin.directory.user.security.

I validated the token in Google’s token_info endpoint, it allowed me to fetch info about all users and groups in this domain.

I was aware that the application uses another Google service with much more sensitive information. Unfortunately after trying to break the endpoints that were using this functionality I hit the wall.

I reported the bug and the new version was fixed in a few hours. Stack trace was removed along with errors dumped on Bad Request.

Press enter or click to view image in full size

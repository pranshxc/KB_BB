---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-27_access-any-owner-account-without-authentication-auth-bypass-2fa-bypass.md
original_filename: 2022-11-27_access-any-owner-account-without-authentication-auth-bypass-2fa-bypass.md
title: Access Any Owner Account without Authentication (Auth bypass + 2FA bypass)
category: documents
detected_topics:
- mfa
- command-injection
tags:
- imported
- documents
- mfa
- command-injection
language: en
raw_sha256: b211958593135835c2d52f75b44161ba6488658f380c184a4657b37b0ae60aa3
text_sha256: ce86089e458e65a32dbc4e90b3c25963dd180ef42ad11caa4aa7121d5be265e3
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Access Any Owner Account without Authentication (Auth bypass + 2FA bypass)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-27_access-any-owner-account-without-authentication-auth-bypass-2fa-bypass.md
- Source Type: markdown
- Detected Topics: mfa, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `b211958593135835c2d52f75b44161ba6488658f380c184a4657b37b0ae60aa3`
- Text SHA256: `ce86089e458e65a32dbc4e90b3c25963dd180ef42ad11caa4aa7121d5be265e3`


## Content

---
title: "Access Any Owner Account without Authentication (Auth bypass + 2FA bypass)"
url: "https://medium.com/@sharp488/access-any-owner-account-without-authentication-auth-bypass-2fa-bypass-94d0d3ef0d9c"
authors: ["Sharat Kaikolamthuruthil (@sharp488)"]
bugs: ["Authentication bypass", "2FA / MFA bypass", "Account takeover"]
publication_date: "2022-11-27"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1852
scraped_via: "browseros"
---

# Access Any Owner Account without Authentication (Auth bypass + 2FA bypass)

Access Any Owner Account without Authentication (Auth bypass + 2FA bypass)
Sharat Kaikolamthuruthil
Follow
2 min read
·
Nov 27, 2022

76

1

Press enter or click to view image in full size
Access Any Owner Account without Authentication (Auth bypass + 2FA bypass)

Hello Folks,

This write-up is about accessing any owner account of an application without any kind of authentication. It was obtained by chaining multiple bugs to escalate into account takeover.

So after spending 2 months on a private program and finding some bugs I decided to check the js files for any hidden URLs, sensitive information etc. I was able to find a few URLs that were not shown in the application UI (hidden). One of the URLs let’s say https://target.com/reports/thirdparty contained a function to create a third party user which allowed them to access only the reports section of the application without accessing the main dashboard contents.

In order to access the report they had to login via URL hosted on another domain. Lets say https://myreport.com/login.php.

After logging in I noticed that the response did not contain any session id but only orgid & userid parameters in the body.

HTTP/1.1 200 OK

Date: Sun, 20 Nov 2022 08:52:07 GMT

Content-Type: application/json

Content-Length: 175

Get Sharat Kaikolamthuruthil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Connection: close

Server: Apache/2.2.22 (Ubuntu)

Vary: Accept-Encoding

{“success”:true,”message”:”Success!”,”data”:{“logo”:””,”sub”:””,”orgid”:”3848",”userid”:”78895"}}

So I tried to manipulate the response to another orgid & userid. Surprisingly it worked & I was able to gain access to another account’s data. After forwarding the response, the application set a SessionID value whilst redirecting to the reports section.

Now since the main application & this third party report URL contained similar cookie for session let’s say SessionID, using it I decided to access contents of the the main URL. To my surprise it worked & I was able to access all the data & perform actions in the main application as an owner effectively taking over the account without the actual credentials or 2FA code.

Root cause of this issue is that the third party user was assigned an owner’s session to access the reports in third party URL which could be used to access anything in the main application as well.

Also authentication in the third party URL was based on the parameters in the body of the response & not the actual credentials supplied.

Since the attacker could gain complete access to owner account without any authentication, it was triaged as CRITICAL severity bug.

Have a good day!! Keep hacking….😃

Disclaimer: For educational purpose only please do not try for illegal activities.

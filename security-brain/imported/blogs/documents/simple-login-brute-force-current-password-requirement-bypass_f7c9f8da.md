---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-07_simple-login-brute-force-current-password-requirement-bypass.md
original_filename: 2018-09-07_simple-login-brute-force-current-password-requirement-bypass.md
title: Simple Login Brute Force / Current Password Requirement Bypass
category: documents
detected_topics:
- rate-limit
- idor
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- rate-limit
- idor
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: f7c9f8da997f1863887b143641c838b6394e65ab5265f3e7e221f3caef34ae44
text_sha256: 4747fe1a69046ccaa5d3103f81c89459a953e454e1f2ab31b6779eb09ea52e38
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Simple Login Brute Force / Current Password Requirement Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-07_simple-login-brute-force-current-password-requirement-bypass.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `f7c9f8da997f1863887b143641c838b6394e65ab5265f3e7e221f3caef34ae44`
- Text SHA256: `4747fe1a69046ccaa5d3103f81c89459a953e454e1f2ab31b6779eb09ea52e38`


## Content

---
title: "Simple Login Brute Force / Current Password Requirement Bypass"
url: "https://medium.com/@ciph3r7r0ll/simple-login-brute-force-current-password-requirement-bypass-e8f58931e257"
authors: ["Mandeep Jadon (@1337tr0lls)"]
bugs: ["IDOR", "Account takeover", "Bruteforce"]
publication_date: "2018-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5720
scraped_via: "browseros"
---

# Simple Login Brute Force / Current Password Requirement Bypass

Simple Login Brute Force / Current Password Requirement Bypass
Mandeep Jadon
Follow
2 min read
·
Sep 7, 2018

122

1

These Bugzzz

Hello guys ,

I hope you are doing well .

In this blog post , I’ll be giving you a scenario that you can add up your bug bounty checklist.

While hunting down a private website I came across many IDORs, XSS and CSRFs which were pretty straight forward . There was however one instance that was slight different that I found for the first time .

The application had a username/ email update mechanism . To update either of the entities, it was required to enter the current password to prevent unauthorized changes . Following is the POST request :

Request: (Update Username)

POST /my/update/username HTTP/1.1
Host: Redact.com
Connection: close
Content-Length: 110
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://www.redact.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8

csrfmiddlewaretoken=5ODzW8EMxFXNqLjRuxKZOabrvnSEQAhZ&old_username=OldUsername&new_username=NewUser&password=***REDACTED***

A Similar request was for Updating email.

Note that the old username was a hidden parameter that was not in the visible form.

On some tampering I found that giving a valid combination of the parameter “old_username” and “password” (Any valid credentials eg. Attacker’s credentials) It was possible to change the username to any username by the attacker without entering the current password .

Get Mandeep Jadon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thus this bypasses the current password requirement . The back-end system was only checking for valid credentials , irrespective of who is logged in .

In simple words a person having temporary access to your account can update your email and takeover your account without having knowledge of your current password .

And what about the login brute force bypass ?

Easy , Since only the credential pair are being verified at the back-end, irrespective of who is logged into . Pass the victim username or Email in the “old_username” or “old email” field and brute force the “password” field .

On successful bruteforce , you will receive the response that the username/email is updated (That is the attackers email/username is updated). That request has the valid credentials (of the victim) .

ie, You are brute forcing the victim’s account from the attacker’s account .

A low blow , but effective bug .

Thanks for reading :)

Have a good day !!!

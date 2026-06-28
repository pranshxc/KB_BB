---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-16_password-bypass-and-something-else.md
original_filename: 2019-06-16_password-bypass-and-something-else.md
title: Password Bypass and Something Else…
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 55f2aec0ca72ac759290ab9b803ac09843d2f07b8d5c21c9d8376be83fab389f
text_sha256: 2a46131cb9ac90cbc8c6f21aeeb75ee0f3e7225077ecb1257752427dbd574436
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Password Bypass and Something Else…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-16_password-bypass-and-something-else.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `55f2aec0ca72ac759290ab9b803ac09843d2f07b8d5c21c9d8376be83fab389f`
- Text SHA256: `2a46131cb9ac90cbc8c6f21aeeb75ee0f3e7225077ecb1257752427dbd574436`


## Content

---
title: "Password Bypass and Something Else…"
page_title: "Password Bypass - Vibhurushi Chotaliya - Medium"
url: "https://medium.com/@Vibhurushi_Chotaliya/password-bypass-and-something-else-cded0847c9df"
authors: ["Vibhurushi Chotaliya (@_Vibhurushi_)"]
bugs: ["Authentication bypass"]
bounty: "600"
publication_date: "2019-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5208
scraped_via: "browseros"
---

# Password Bypass and Something Else…

Password Bypass
Vibhurushi Chotaliya
Follow
Mar 16, 2019

57

1

Hello guys

This is Vibhurushi Chotaliya. I hope you doing well…

This post is about i was able to bypass password protection when add some bank details and something else.

Get Vibhurushi Chotaliya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

POC:

After login when i add bank details xyz.com it ask me account password.
So i enter the correct password,catch the request in burp.i got response like {“status”:”success”,”data”:{“message”:”Authentication successful.”}}
Now i’m able to change my bank details.
Again i’m re-login in my account, this time i enter wrong password and catch the request in burp.i got response like {“status”:”error”,”data”:”Incorrect password. Please try again."}.
Now you are thinking i was change the response and bypass it…yes you are right.
Again i enter wrong password,catch the request in burp,again i got response like {“status”:”error”,”data”:”Incorrect password. Please try again.”}. then i replaced with this response{“status”:”success”,”data”:{“message”:”Authentication successful.”}} and i bypass the password protection.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-11_pwn-them-all-bugbounty.md
original_filename: 2019-09-11_pwn-them-all-bugbounty.md
title: 'Pwn Them All #BugBounty'
category: documents
detected_topics:
- password-reset
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- command-injection
- otp
language: en
raw_sha256: ccce569c02e950e2335a7fa139ed207b1f4774a015e5c050a288bcde4cf41d0b
text_sha256: 70c02c9334118429d3b0c64d8528266b884bf1a8958884591691ce04ac78dbcb
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Pwn Them All #BugBounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-11_pwn-them-all-bugbounty.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, otp
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `ccce569c02e950e2335a7fa139ed207b1f4774a015e5c050a288bcde4cf41d0b`
- Text SHA256: `70c02c9334118429d3b0c64d8528266b884bf1a8958884591691ce04ac78dbcb`


## Content

---
title: "Pwn Them All #BugBounty"
url: "https://medium.com/@bilalmerokhel/pwn-them-all-bugbounty-4ee60e13c83"
authors: ["Bilal Khan (@bilalmerokhel)"]
bugs: ["Host header injection", "Password reset"]
publication_date: "2019-09-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5037
scraped_via: "browseros"
---

# Pwn Them All #BugBounty

Pwn Them All #BugBounty
Bilal Khan
Follow
2 min read
·
Sep 12, 2019

173

Recently I was Pentesting a private program The web app was built on “Ruby on Rails”, I was testing ‘forgot password’ functionality, of course, why not?

Get Bilal Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was surprised when I saw that the endpoint was vulnerable to Host-Header Injection so, here are the steps of how I was able to exploit it. First I fired up python local server running on port 8080 along with ngrok on port 80

Press enter or click to view image in full size
python server with ngrok

I fired up my burp and firefox typed the URL again to capture the request for further testing. I typed my email in the forgot password form, when I intercept the request first I tried every header like

X-Host: evil.com
X-Server: evil.com
X-Forwarded-For: evil.com
X-Forwarded-Host: evil.com
Press enter or click to view image in full size
password reset form
Press enter or click to view image in full size
captured request

I tried every header and the one which worked for me here was

X-Forwarded-Host: evil.com
Press enter or click to view image in full size
confirmation

Got confirmation about the email has been sent to my email

Press enter or click to view image in full size
the host changed to mine host

Original Host replaced by the evil host (ngrok/mine host). Now victims click the link and I GET a request with the password token of the user

Press enter or click to view image in full size
victims click and code sent to my server

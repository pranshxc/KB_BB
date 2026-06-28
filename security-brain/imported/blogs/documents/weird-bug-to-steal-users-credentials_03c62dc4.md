---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-12_weird-bug-to-steal-users-credentials.md
original_filename: 2024-01-12_weird-bug-to-steal-users-credentials.md
title: Weird bug to steal users credentials
category: documents
detected_topics:
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- command-injection
language: en
raw_sha256: 03c62dc4ede3433afc89c9245abe1d741bc3b8211fca9aa0c7a81ef0096945a8
text_sha256: 7d17a78b632ccb275882cd0668d97f18ee1c88f0b6b2858aad00cdeef561f266
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Weird bug to steal users credentials

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-12_weird-bug-to-steal-users-credentials.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `03c62dc4ede3433afc89c9245abe1d741bc3b8211fca9aa0c7a81ef0096945a8`
- Text SHA256: `7d17a78b632ccb275882cd0668d97f18ee1c88f0b6b2858aad00cdeef561f266`


## Content

---
title: "Weird bug to steal users credentials"
url: "https://medium.com/@fuadahmad062/weird-bug-to-steal-users-credentials-5e80c5d4565f"
authors: ["von001"]
bugs: ["SSRF", "Phishing"]
publication_date: "2024-01-12"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 552
scraped_via: "browseros"
---

# Weird bug to steal users credentials

Weird bug to steal users credentials
von001
Follow
1 min read
·
Jan 12, 2024

73

3

Content Spoofing

Hello this is my first write up i hope you enjoy it

Content spoofing involves manipulating the content of a website to deceive users or trick them into thinking they are interacting with a legitimate site when, in fact, they are not

after recon i found a domain it was game.site.com

the website was providing game puzzle to play

so i notice a parameter calling a game puzzle from deferent wibsite

https://game.site.com/detail?url=http://site.com/

I immediately tried for SSRF. i used 127.0.0.1 and it responded with

“127.0.0.1 refused to connect.”

Get von001’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

after a few minute i thought let’s try for an open redirect

I injected google.com into the “url” parameter, and the page loaded google.com i created a html file with xss payload and run it in my localhost by using this command

python3 -m http.server 8081 

it worked , but the xss was firing on my localhost not game.site.com

I tried for a higher impact. I created a login page to inject it as an iframe into the website

The final payload looked like this:

http://game.site.com/detail?url=http://127.0.0.1:8081/login.html

Press enter or click to view image in full size

the login page you see it my html file by this way you can trick users to your login page

Thanks for reading I hope you enjoyed it.

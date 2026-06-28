---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-29_my-first-apple-bug-and-my-first-writeup.md
original_filename: 2022-06-29_my-first-apple-bug-and-my-first-writeup.md
title: My First Apple Bug And My First Writeup
category: blogs
detected_topics:
- idor
- command-injection
- password-reset
- otp
- mobile-security
tags:
- imported
- blogs
- idor
- command-injection
- password-reset
- otp
- mobile-security
language: en
raw_sha256: ed4b0742723c19bee63046301b0134c008bc11bbb862fadad9fe3587c357a63d
text_sha256: 5e5fa0edf5d8df2ae16af18b5a85ba45f2396278456f08e140804e5829e4337c
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# My First Apple Bug And My First Writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-29_my-first-apple-bug-and-my-first-writeup.md
- Source Type: markdown
- Detected Topics: idor, command-injection, password-reset, otp, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `ed4b0742723c19bee63046301b0134c008bc11bbb862fadad9fe3587c357a63d`
- Text SHA256: `5e5fa0edf5d8df2ae16af18b5a85ba45f2396278456f08e140804e5829e4337c`


## Content

---
title: "My First Apple Bug And My First Writeup"
page_title: "MY FIRST APPLE BUG and MY FIRST WRITEUP | by Aravind(Dinesh) | Medium"
url: "https://medium.com/@aravindb26/my-first-apple-bug-and-my-first-writeup-8a833e8e953c"
authors: ["Banavath Aravind (@nanicyb)"]
programs: ["Apple"]
bugs: ["IDOR", "Email verification bypass"]
publication_date: "2022-06-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2500
scraped_via: "browseros"
---

# My First Apple Bug And My First Writeup

MY FIRST APPLE BUG and MY FIRST WRITEUP
Aravind(Dinesh)
Follow
2 min read
·
Jun 29, 2022

250

4

Hello friends, My name is Aravind. These is my first writeup.

I’m from Mechanical background but my passion went into hacking field because I’m very curious about knowing other’s secret. My curiosity started like I hacked into my friends Facebook like giving them phishing links and said them to login for fun…..

These curiosity made me to dive into bug bounty.

Just shared about my self above. :)

My Bug was very simple that I have bypassed Email verification on Apple subdomain.

Get Aravind(Dinesh)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps To Reproduce:

I have done sign-in to a subdomain we say here it as sub.apple.com
Now their is a feature that we need to verify our Email to enter into that subdomain page
Now I went to my Gmail and copied Email Verification link
Their is a parameter in that link called Email id=***REDACTED-SUSPECT-TOKEN***Now I replaced that string with my actual email id like abc@gmail.com
That's it I have bypassed their string which was not verifying when we do email verification and signup done successful.

From these we need to understand that we need to check every small functional in target domains.

After 7 months I got rewarded and HallofFame in Apple

Apple rewarded me $$$$ :)

Press enter or click to view image in full size
Press enter or click to view image in full size

I will be posting more writeups on bugs I have already found and bounty tips soon….

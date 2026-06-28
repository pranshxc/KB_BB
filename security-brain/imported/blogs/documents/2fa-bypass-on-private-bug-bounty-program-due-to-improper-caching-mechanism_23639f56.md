---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-22_2fa-bypass-on-private-bug-bounty-program-due-to-improper-caching-mechanism.md
original_filename: 2022-05-22_2fa-bypass-on-private-bug-bounty-program-due-to-improper-caching-mechanism.md
title: 2FA Bypass on private bug bounty program due to improper caching mechanism
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
raw_sha256: 23639f5683e2c67f66a159e6d42d026d4894b0bb1973903ed6dbef4d381ed67a
text_sha256: 65e07462c91579d354bf82d26ac66f5808ce9986613e11cb8c1b6d52e067bb14
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA Bypass on private bug bounty program due to improper caching mechanism

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-22_2fa-bypass-on-private-bug-bounty-program-due-to-improper-caching-mechanism.md
- Source Type: markdown
- Detected Topics: mfa, command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `23639f5683e2c67f66a159e6d42d026d4894b0bb1973903ed6dbef4d381ed67a`
- Text SHA256: `65e07462c91579d354bf82d26ac66f5808ce9986613e11cb8c1b6d52e067bb14`


## Content

---
title: "2FA Bypass on private bug bounty program due to improper caching mechanism"
url: "https://medium.com/@sharp488/2fa-bypass-on-private-bug-bounty-program-due-to-improper-caching-mechanism-212c5912bd00"
authors: ["Sharat Kaikolamthuruthil (@sharp488)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2022-05-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2617
scraped_via: "browseros"
---

# 2FA Bypass on private bug bounty program due to improper caching mechanism

Top highlight

2FA Bypass on private bug bounty program due to improper caching mechanism
Sharat Kaikolamthuruthil
Follow
2 min read
·
May 22, 2022

189

3

Press enter or click to view image in full size
2 Factor Authentication Bypass

Hello All,

This is the story of how I was able to bypass 2FA on a private bug bounty program.

Due to privacy policy I cannot disclose the name of the program. This was a website where we could view videos. Lets call it redacted.com.

Get Sharat Kaikolamthuruthil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So the flow of the application was such that after logging into the application and profile is loaded completely, a pop up box will prompt for 2FA code. We cannot access the page contents unless the code is submitted.

Press enter or click to view image in full size
2FA prompt
First I cleared all cache from my browser and opened the website but this time I directly called the video URL e.g. redacted.com/en/video/my-videos/200436.
The application redirected me to the login page.
Since I had cleared all cache from browser the site asked me to accept the cookie policy.
Press enter or click to view image in full size
Cookie Policy
I logged into the account but this time without accepting the cookie policy.
To my surprise the application logged in successfully & the video started playing.
The 2FA prompt was bypassed.

Here the 2FA was dependent on the caching mechanism. As I did not accept the cookie policy, application couldn’t check for 2FA which allowed me to directly access the video.

Since the main priority of the program was to prevent users from viewing videos without 2FA code, this was triaged as a HIGH severity finding.

Hope you guys enjoyed it. 😃

Thank You!!

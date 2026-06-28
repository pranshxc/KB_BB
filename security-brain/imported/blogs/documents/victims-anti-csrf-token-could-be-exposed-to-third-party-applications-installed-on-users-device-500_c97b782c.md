---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-21_victims-anti-csrf-token-could-be-exposed-to-third-party-applications-installed-o.md
original_filename: 2021-05-21_victims-anti-csrf-token-could-be-exposed-to-third-party-applications-installed-o.md
title: Victim’s Anti CSRF Token could be exposed to Third-party Applications installed
  on user’s Device (500$)
category: documents
detected_topics:
- supply-chain
- command-injection
- otp
- csrf
- information-disclosure
tags:
- imported
- documents
- supply-chain
- command-injection
- otp
- csrf
- information-disclosure
language: en
raw_sha256: c97b782cd5dc5f7c3a6f836289143f725e0807cee7ef8d832c0c9c808f68ae88
text_sha256: acbb3a5defad6cbb4a66be18b4ceb8499a9a4069e8ed5c2c00e8f7e800ff342c
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Victim’s Anti CSRF Token could be exposed to Third-party Applications installed on user’s Device (500$)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-21_victims-anti-csrf-token-could-be-exposed-to-third-party-applications-installed-o.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, otp, csrf, information-disclosure
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `c97b782cd5dc5f7c3a6f836289143f725e0807cee7ef8d832c0c9c808f68ae88`
- Text SHA256: `acbb3a5defad6cbb4a66be18b4ceb8499a9a4069e8ed5c2c00e8f7e800ff342c`


## Content

---
title: "Victim’s Anti CSRF Token could be exposed to Third-party Applications installed on user’s Device (500$)"
url: "https://rohitcoder.medium.com/victims-anti-csrf-token-could-be-exposed-to-third-party-applications-installed-on-user-s-device-be8e40d511ba"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2021-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3630
scraped_via: "browseros"
---

# Victim’s Anti CSRF Token could be exposed to Third-party Applications installed on user’s Device (500$)

Victim’s Anti CSRF Token could be exposed to Third-party Applications installed on user’s Device (500$)
Rohit kumar
Follow
2 min read
·
May 20, 2021

29

Press enter or click to view image in full size

Complete Details
===
During my investigation, I found that a user’s DTSG token can be exposed to a third-party application because of a broken feature in Facebook’s Creator Studio (Web Version), That broken feature triggers an HTML file download in user’s device, which contains fb_dtsg, hashes, ajaxpipe_token, LoggedIn user details and some other info.

Note: This file gets downloaded in the User’s Download folder which can be easily accessed by any application, So a malicious application can read this info and use it for exploiting csrf on the user’s device.

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Expected behavior: A zip file or HTML file with only images/thumbnails should be downloaded.
Actual behavior: A “404 Error” HTML page gets downloaded which contains this info

Impact
===
1. Perform any action with obtained fb_dtsg token
2. Get info of LoggedIn user

Have a look at this PoC Video — https://youtu.be/-2MerrwzQPc

Steps
==
1. Visit https://business.facebook.com/creatorstudio/content_posts
2. Click on 3 dots aside any video to open the “Edit Video” Modal box
3. Now, at the footer of the Modal box you will see three dots click on that
4. Now, click on “Download Generated Thumbnails”
5. This will trigger a download of the HTML file on the user’s device, This file contains all sensitive info like dtsg_token and other details.

Also read https://rohitcoder.medium.com/csrf-from-which-we-can-create-a-support-ticket-in-victims-account-500-c1aa61f99c17 (500$)

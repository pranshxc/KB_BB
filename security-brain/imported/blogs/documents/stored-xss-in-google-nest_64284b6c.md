---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-07_stored-xss-in-google-nest.md
original_filename: 2020-04-07_stored-xss-in-google-nest.md
title: Stored XSS in Google Nest
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 64284b6c16c01d2b8ce5c7405399b4df0f3ba6d18f485e57452da1ce1b531059
text_sha256: 7648c332f242a9ee3d57bebc4d438f6de96c76ffe41cf9afeaa7c65c033e24ad
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in Google Nest

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-07_stored-xss-in-google-nest.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `64284b6c16c01d2b8ce5c7405399b4df0f3ba6d18f485e57452da1ce1b531059`
- Text SHA256: `7648c332f242a9ee3d57bebc4d438f6de96c76ffe41cf9afeaa7c65c033e24ad`


## Content

---
title: "Stored XSS in Google Nest"
url: "https://medium.com/bugbountywriteup/stored-xss-in-google-nest-a82373bbda68"
authors: ["Harikrishnan Chandraganesan (@hari_cybex)"]
programs: ["Google"]
bugs: ["Stored XSS"]
publication_date: "2020-04-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4662
scraped_via: "browseros"
---

# Stored XSS in Google Nest

Stored XSS in Google Nest
Harikrishnan Chandraganesan
Follow
2 min read
·
Apr 8, 2020

158

3

Welcome All ! :) This is my first writeup, first blog, first publication, whatever…

Lets get straight to the bug. While testing Google Nest for bugs, I have found a stored XSS in https://store.nest.com/ . Actually this is an accidental XSS. :P

Get Harikrishnan Chandraganesan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I have tested many input fields for XSS and left the tabs opened. After sometime I just left the home.nest.com subdomain and went for the store.nest.com . While changing the home1 to home2 , i just refreshed the page and got a popup. I was like…

Random Vadivelu GIF for expressing happiness :P

Proof of Concept sent to Google :

Timeline :

Mar 17, 2019 - Bug Reported to Google

Mar 19, 2019 - Status changes to Not Reproducible | Explained how to reproduce the bug

Mar 26, 2019 - Nice Catch! from Google ❤

Apr 9, 2019 - Bounty Awarded $$$

So, this was my first bounty from Google. I have reported other minor issues and got hall of fame. But getting a bounty from google is a long time goal for me. Even though the bounty is less but it felt more happiness than the monthly salary of my daily job :) You can see many writeups coming up in the next few days.

Thanks for Reading :) Bella Ciao !

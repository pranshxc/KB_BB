---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-09_how-i-hacked-google-to-read-files-from-their-servers-for-free.md
original_filename: 2022-02-09_how-i-hacked-google-to-read-files-from-their-servers-for-free.md
title: How I hacked Google to read files from their servers for free!
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: f75057a84c494b7529980d115701e0e214e276b5610e5f94813c41b31a853c4e
text_sha256: b0bd47053180dd9df564a33cd7bc0eeb76e48e895f62b8aef2f9036c85c10c17
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked Google to read files from their servers for free!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-09_how-i-hacked-google-to-read-files-from-their-servers-for-free.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `f75057a84c494b7529980d115701e0e214e276b5610e5f94813c41b31a853c4e`
- Text SHA256: `b0bd47053180dd9df564a33cd7bc0eeb76e48e895f62b8aef2f9036c85c10c17`


## Content

---
title: "How I hacked Google to read files from their servers for free!"
url: "https://medium.com/@harishhacker3010/how-i-hacked-google-to-read-files-from-their-servers-for-free-e0486a674912"
authors: ["Harish SG (@CoderHarish)"]
programs: ["Google"]
bugs: ["Arbitrary file read"]
publication_date: "2022-02-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2919
scraped_via: "browseros"
---

# How I hacked Google to read files from their servers for free!

How I hacked Google to read files from their servers for free!
Harish SG
Follow
1 min read
·
Feb 9, 2022

108

2

Hey Guys, This is Harish! I used to hunt to Microsoft and Google VRP, This is my first write up!

When I was having a coffee and browsing through my Twitter, I suddenly got an idea to recon the google acquisitions, After Spending like 2 hrs, I found an outdated Atlassian bamboo on google’s one of the acquisitions While fuzzing different endpoints. I found an interesting response when I sent a GET request to /chart endpoint which leaks some stacktrace with filename parameter not found! Then I tried adding filename as parameter! I was able to read any files from the /tmp folder without authentication!

Get Harish SG’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally got this email from google regarding reward and added me in their Google honourable mentions

Press enter or click to view image in full size

Bug Fixed mail from Google!

Press enter or click to view image in full size

Don’t focus on bounties too much! cuz learning more important in security.

Follow me on twitter to know more! https://twitter.com/CoderHarish

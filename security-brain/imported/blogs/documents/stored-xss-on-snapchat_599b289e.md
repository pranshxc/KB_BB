---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-09_stored-xss-on-snapchat.md
original_filename: 2018-02-09_stored-xss-on-snapchat.md
title: Stored XSS on Snapchat
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
raw_sha256: 599b289e48a974aecad157f506e38193c701dd10313d3adf4a715942b03d33c4
text_sha256: 0a1ece9c54b10b4ec9b103c57322c7a1158817e0b0628d77a93509b68476938d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on Snapchat

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-09_stored-xss-on-snapchat.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `599b289e48a974aecad157f506e38193c701dd10313d3adf4a715942b03d33c4`
- Text SHA256: `0a1ece9c54b10b4ec9b103c57322c7a1158817e0b0628d77a93509b68476938d`


## Content

---
title: "Stored XSS on Snapchat"
url: "https://medium.com/@mrityunjoy/stored-xss-on-snapchat-5d704131d8fd"
authors: ["Mrityunjoy (@mitunjoy11)"]
programs: ["Snapchat"]
bugs: ["Stored XSS"]
publication_date: "2018-02-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5979
scraped_via: "browseros"
---

# Stored XSS on Snapchat

Stored XSS on Snapchat
Mrityunjoy
Follow
2 min read
·
Feb 9, 2018

833

2

Hello Guyz,
This is @Mrityunjoy . A Bug Bounty Hunter from Bangladesh. Today I want to share with you a Stored XSS which I found in Snapchat.

Get Mrityunjoy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While i testing i found a Snapchat Ads Domain. So i decided to test that domain to found some bugs.

When i go to the ADS domain i noticed a Setup Option, That means first we need to create a ADS Account. I PUT a HTML TAG into the BUSINESS NAME field and fill up the other field as random words and started a account.

Press enter or click to view image in full size

I created a Organization and they have a invite member option, where i can invite new members on my Organization.

Press enter or click to view image in full size

I invited my own email to joining as Organization member. After Opening my mail i saw the BUSINESS NAME field was vulnerable to HTML INJECTION

Press enter or click to view image in full size
Press enter or click to view image in full size

I was looking!!!

Simply again i back to the Ads domain and tried to created another account.
I PUT a simple payload test"><img src=x onerror=prompt<domain)>into the BUSINESS NAME field and Started a account.

Now again i created a Organization and invited my own email to joining as Organization member. Quickly i opened my mail and clicked the invitation link.
After clicking the link bingo!!!! Got the XSS POPUP. I Managed to achieve the Stored XSS on all browsers.

Press enter or click to view image in full size

I was Feeling!!!

Timeline
Jul 13th — report submitted
Jul 13th — Triaged
Jul 17th — Rewarded Bounty
Press enter or click to view image in full size
Jul 17th — Resolved

Thanks to Tarek Siddiki & Faisal Ahmed

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-10_sleep-sql-injection-on-name-parameter-while-updating-profile_2.md
original_filename: 2022-11-10_sleep-sql-injection-on-name-parameter-while-updating-profile_2.md
title: Sleep SQL injection on Name Parameter While Updating Profile
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: 160bfefd4e36f47e97ffac7fd5efed0fd7e9c721d1171037930762dacc73fe85
text_sha256: 06cdcd274004fed761da395084b7e22093bc4279cde43ad0251192859114c42d
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Sleep SQL injection on Name Parameter While Updating Profile

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-10_sleep-sql-injection-on-name-parameter-while-updating-profile_2.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `160bfefd4e36f47e97ffac7fd5efed0fd7e9c721d1171037930762dacc73fe85`
- Text SHA256: `06cdcd274004fed761da395084b7e22093bc4279cde43ad0251192859114c42d`


## Content

---
title: "Sleep SQL injection on Name Parameter While Updating Profile"
url: "https://medium.com/@umeryousuf26/sleep-sql-injection-on-name-parameter-while-updating-profile-2bbac9f47336"
authors: ["Umer Yousuf"]
bugs: ["SQL injection"]
bounty: "500"
publication_date: "2022-11-10"
added_date: "2022-11-11"
source: "pentester.land/writeups.json"
original_index: 1932
scraped_via: "browseros"
---

# Sleep SQL injection on Name Parameter While Updating Profile

Sleep SQL injection on Name Parameter While Updating Profile
Umer Yousuf
Follow
Nov 10, 2022

5

1

Hi everyone, I am an Independent Cyber Security Researcher and a Bug Bounty Hunter from Pakistan.

I recently got invited to a private program, which allowed me to be hunted on all the assets that belong to them. So, Just grab a coffee and start hunting without wasting more time.

Start with the usual recon which gives some hanging fruits but after spending an hour at Target, I found an unusual parameter response in updating the profile picture. Therefore used an SQLI sleep payload, and it slept for 5 seconds since the sleep(5). We used it again and it did work.

Payload: 0'XOR(if(now()=sysdate(),sleep(5),0))XOR’Z

Get Umer Yousuf’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The vulnerable updating profile request looked like this after injecting payload through burp intruder:

Press enter or click to view image in full size

Rewarded €500

Press enter or click to view image in full size

Important Tip: Do check each parameter manually.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-11_hunt-for-sql-injection-the-smart-way.md
original_filename: 2020-06-11_hunt-for-sql-injection-the-smart-way.md
title: HUNT for SQL Injection- The Smart Way!
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
raw_sha256: f8d01820413bf3d75cf3a22eb084f5095c204cf067507ad6d807f761f004aca6
text_sha256: 2daad77dcd015abe9492b4fdb3e5cb770b0ffd21515283d2e1d7aa5587ff5c3e
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# HUNT for SQL Injection- The Smart Way!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-11_hunt-for-sql-injection-the-smart-way.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f8d01820413bf3d75cf3a22eb084f5095c204cf067507ad6d807f761f004aca6`
- Text SHA256: `2daad77dcd015abe9492b4fdb3e5cb770b0ffd21515283d2e1d7aa5587ff5c3e`


## Content

---
title: "HUNT for SQL Injection- The Smart Way!"
url: "https://medium.com/@mudassirsharief58/hunt-for-sql-injection-the-smart-way-db85243a4e90"
authors: ["Mudassir Sharief"]
bugs: ["SQL injection"]
publication_date: "2020-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4508
scraped_via: "browseros"
---

# HUNT for SQL Injection- The Smart Way!

HUNT for SQL Injection- The Smart Way!
Mudassir Sharief
Follow
2 min read
·
Jun 12, 2020

286

1

Hello Readers, Welcome to my first post, in this Post i will show how to hunt for the Classic SQL injection. Yes, the classic SQL injection vulnerability still exists and i dumped the whole DB. Lets get started…..

Press enter or click to view image in full size

Many People have this misconception that in this advanced era, why would any application be vulnerable to the classic SQL injection and doesn't give a try. I always used to ignore SQL. One fine day i was browsing through the programs on bug crowd and selected a wide range target lets call it redacted.com.

Now, How to hunt SQL in a smart way?

Lets Break into Steps:

Step 1: I used google dork to fetch all the login pages → site:redacted.com inurl:login

Step 2: Make a list of SQL payloads, hit on all the login pages with Intruder.

Step 3: Check for SQL Query in error/response.

Step 4: If you successfully get SQL error → Run SQL map

Get Mudassir Sharief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step 5: Get the big FAT Bounty !!!!

I followed the same steps and executed Blind SQL Successfully
Press enter or click to view image in full size
SQL Detection

Payload Used Above → admin’ or 1'=’1- -

I used SQL map, captured the request in Burp and made the POST.txt file and ran the SQL map

For your reference on how to use SQL map for post request → https://hackertarget.com/sqlmap-post-request-injection/

Press enter or click to view image in full size
The DB

And…. Finally Get the Reward :)

Press enter or click to view image in full size
Final Tip: The Bugs are out there, Find THEM !!!

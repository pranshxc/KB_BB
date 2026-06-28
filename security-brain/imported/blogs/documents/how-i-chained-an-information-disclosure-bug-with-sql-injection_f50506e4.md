---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-30_how-i-chained-an-information-disclosure-bug-with-sql-injection.md
original_filename: 2023-04-30_how-i-chained-an-information-disclosure-bug-with-sql-injection.md
title: How I Chained an Information Disclosure Bug with SQL Injection
category: documents
detected_topics:
- sqli
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- sqli
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: f50506e4aa31c2ec7bc94e7570199b9290cfacab704bd221c933e4c1c3aebd53
text_sha256: 05a97e9aaa051ec95a9a8a604669a5570d66ef6658f00d39184c62af2af106f6
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# How I Chained an Information Disclosure Bug with SQL Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-30_how-i-chained-an-information-disclosure-bug-with-sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `f50506e4aa31c2ec7bc94e7570199b9290cfacab704bd221c933e4c1c3aebd53`
- Text SHA256: `05a97e9aaa051ec95a9a8a604669a5570d66ef6658f00d39184c62af2af106f6`


## Content

---
title: "How I Chained an Information Disclosure Bug with SQL Injection"
url: "https://goziem.medium.com/how-i-chained-an-information-disclosure-bug-to-sql-injection-bca936d90fb1"
authors: ["Mba-oji Chiagoziem (@g0ziem)"]
bugs: ["SQL injection", ".git folder disclosure"]
publication_date: "2023-04-30"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1211
scraped_via: "browseros"
---

# How I Chained an Information Disclosure Bug with SQL Injection

How I Chained an Information Disclosure Bug with SQL Injection
Mba-oji Chiagoziem
Follow
2 min read
·
Apr 30, 2023

158

2

Good day Hackers,

I’d like to appreciate God for helping me find this bug and I’ll be sharing how I was able to do so.

Press enter or click to view image in full size
What is SQL Injection?

SQL injection is a type of web application security vulnerability that occurs when an attacker can input malicious SQL statements into an application’s input fields. This type of attack takes advantage of the fact that many web applications accept user input without properly validating or sanitizing it.

Summary

I got subdomains of my target and then visited one of the endpoints which was a login page. While I was on the page, I checked the DotGit Chrome Extension and I got a message about an exposed Git repository on the site. I clicked on it, and the .git/index directory was downloaded.

Get Mba-oji Chiagoziem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I viewed the file and behold, a huge number of unauthenticated directories were exposed. I tried my best to visit each endpoint but one of them stood out. It disclosed a MySQL error message:

Press enter or click to view image in full size

After asking for help on Twitter, I finally had an idea of what to do. I began by adding the nom_hachage parameter to the URL and it was like:

https://target.com/endpoint.php?nom_hachage='

The error message immediately changed to the content that was in the nom_hachage parameter.

Press enter or click to view image in full size

I sent the whole request to both Ghauri and Sqlmap:

ghauri -u https://target.com/endpoint.php?nom_hachage=1 --dbs
python3 sqlmap.py -u https://target.com/endpoint.php?nom_hachage=1

Ghauri was able to retrieve the database name and user in less than 15 minutes while Sqlmap is still looking for an exploit😂.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Tip:

Always chain bugs to get maximum impact.

Thanks for reading.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-26_thick-client-attacking-databases-the-funeasy-way.md
original_filename: 2018-09-26_thick-client-attacking-databases-the-funeasy-way.md
title: Thick Client — Attacking databases the fun/easy way
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
raw_sha256: af53e2c777a7dafaa9d0e1f169971d9fb1236762671d49619ae15fb3c618e35e
text_sha256: 355efdbc6e4b6b399f66696f628e548904e04cc070a16ee422577458d3cc9452
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Thick Client — Attacking databases the fun/easy way

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-26_thick-client-attacking-databases-the-funeasy-way.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `af53e2c777a7dafaa9d0e1f169971d9fb1236762671d49619ae15fb3c618e35e`
- Text SHA256: `355efdbc6e4b6b399f66696f628e548904e04cc070a16ee422577458d3cc9452`


## Content

---
title: "Thick Client — Attacking databases the fun/easy way"
page_title: "Thick Client — Attacking databases the fun/easy way | by Richard Clifford | Medium"
url: "https://medium.com/@mantissts/thick-client-attacking-databases-the-fun-easy-way-6e31162b1335"
authors: ["Richard Clifford (@MantisSTS)"]
bugs: ["Thick client", "Credentials sent over unencrypted channel"]
publication_date: "2018-09-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5678
scraped_via: "browseros"
---

# Thick Client — Attacking databases the fun/easy way

Thick Client — Attacking databases the fun/easy way
Richard Clifford
Follow
2 min read
·
Sep 26, 2018

63

I was recently looking at a desktop application of a large security firm which manages the security of various large buildings around the UK. The application was fairly straight-forward for a standard thick-client which retrieved and stored data in SQLServer from a remote host.

The test started off as every other test does — setting up tools, installing dependencies, etc. If you are familiar with a web assessment or a thick-client assessment then the methodology should be familiar to you. Once I had the basic tools setup such as Echo Mirage, Burp, etc, it was a case of looking through the traffic to see if there was anything interesting. After going through the application and logging the traffic I found something interesting!

The application was connecting to the database over a clear-text connection which meant the database credentials were being sent.

Get Richard Clifford’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

[Disclaimer] I am going to redact any sensitive information.

Credentials being sent over clear-text

From this I was able to grab the database credentials, use the metasploit module “windows/mssql/mssql_payload” and get a meterpreter shell. The joy of this is that the shell was running as SYSTEM! \o/

SYSTEM shell on the database server

From metasploit and the meterpreter shell I was able to dump the entire database, create new users on the system, pivot through the network, etc. It goes to show that it’s not a great idea to send credentials over clear-text.

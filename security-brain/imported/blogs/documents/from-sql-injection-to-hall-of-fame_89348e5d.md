---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-18_from-sql-injection-to-hall-of-fame.md
original_filename: 2020-08-18_from-sql-injection-to-hall-of-fame.md
title: From SQL Injection to Hall Of Fame
category: documents
detected_topics:
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- api-security
language: en
raw_sha256: 89348e5d6c1d245d420da608708c5e0101fba4769343854392a3209849352483
text_sha256: d917894ad1711a0143254608895418b5ac83cf1393d5e3f8fd7d0e3679c428c7
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# From SQL Injection to Hall Of Fame

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-18_from-sql-injection-to-hall-of-fame.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `89348e5d6c1d245d420da608708c5e0101fba4769343854392a3209849352483`
- Text SHA256: `d917894ad1711a0143254608895418b5ac83cf1393d5e3f8fd7d0e3679c428c7`


## Content

---
title: "From SQL Injection to Hall Of Fame"
url: "https://medium.com/bugbountywriteup/from-sql-injection-to-hall-of-fame-96a08c869acd"
authors: ["Jadek Mark (@mase289)"]
bugs: ["SQL injection"]
publication_date: "2020-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4310
scraped_via: "browseros"
---

# From SQL Injection to Hall Of Fame

Top highlight

From SQL Injection to Hall Of Fame
Mase289
Follow
2 min read
·
Aug 18, 2020

82

1

Press enter or click to view image in full size
Photo by luis gomes from Pexels

Google Dorking seems an often under-appreciated technique in a bug bounty hunter’s arsenal when assessing a target web application for vulnerabilities. A Google dork query, sometimes just referred to as a dork, is a search string that uses advanced search operators to find information that is not readily available on a website.

Google Dorking, also known as Google hacking, can return information that is difficult to locate through simple search queries. That description includes information that is not intended for public viewing but that has not been adequately protected. Reference here https://whatis.techtarget.com/definition/Google-dork-query

I recently came across an interesting google dork inurl:storefrontb2bwebthat enables us to scan for e-commerce websites that are vulnerable to SQL Injection. This was originally discovered by a bug hunter going by the name ratboy. Typing this query in Google will return 4 pages of results. Unfortunately, most of the website owners have no vulnerability disclosure in place and efforts to contact them via other channels proved futile.

Get Mase289’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

One website had a vulnerability disclosure channel which I found through running a search on google “Company name vulnerability disclosure”. The vulnerable parameter is the username parameter which throws a SQL error when injected with a single or double quote.

Press enter or click to view image in full size
The SQL error message used to verify the vulnerability

Exploiting this SQL Injection bug is trivial with SQLMAP via the following command.

python sqlmap.py -u"http://localhost/storefrontB2BWEB/login.do?setup_principal=true&action=prepare_forgot&login=true&usr_name=foo"
-p usr_name --dbms=mssql --level=5 --risk=3
--tamper=between,space2comment -o --random-agent --parse-errors
--os-shell --technique=ES

Fix

Proper user input escaping.

Reporting this vulnerability to the affected company earned me a place in their hall of fame. It is my hope that all of the companies affected shall take the necessary steps to resolve the issue and more importantly consider having avenues in place where such issues can be reported responsibly for timely resolution.

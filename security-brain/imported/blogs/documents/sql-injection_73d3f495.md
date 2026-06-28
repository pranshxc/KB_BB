---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-17_sql-injection.md
original_filename: 2019-06-17_sql-injection.md
title: SQl Injection
category: documents
detected_topics:
- sqli
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- sqli
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: 73d3f49510b536a6152340f5a3321e31685524074986db05fae67dd2dedf6e69
text_sha256: e1ea72b0343ba469e05652076e414c487633503299b25b9643efde80a015fc8d
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# SQl Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-17_sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `73d3f49510b536a6152340f5a3321e31685524074986db05fae67dd2dedf6e69`
- Text SHA256: `e1ea72b0343ba469e05652076e414c487633503299b25b9643efde80a015fc8d`


## Content

---
title: "SQl Injection"
url: "https://medium.com/@saadahmedx/sql-injection-c87a390afdd3"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["SQL injection"]
bounty: "500"
publication_date: "2019-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5206
scraped_via: "browseros"
---

# SQl Injection

Saad Ahmed
 highlighted

SQl Injection
Saad Ahmed
Follow
2 min read
·
Jun 17, 2019

261

2

Hy Guy’s this write up is all about my SQL Injection that I found in PRIVATE program running on BugCrowd

let assume website name subdomain.private.com/registro/login. when i visit the site I saw the strange behavior this is the admin panel & the website reload it self again & again so I turn on the intercept & capture the request and tried basic bypass eg admin:admin, 1'or’1'=’1 but didn’t work there is two parm _email and _pass

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I put in ’ _email parm & nothing happen but accidentally put ‘ in both _email & _pass and I got <b>Warning</b>: PDOStatement::execute(): SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near…

Press enter or click to view image in full size

SQl Conform :D I tried to exploit further but failed there is WAF that block me to do further injection and them I remember our Awsm OLD facebook group of WEB INJECTORS https://www.facebook.com/groups/webinj3ct0rs/ where we try our best to solve Challenges ;) Still remember those golden days the group having there website with name http://www.securityidiots.com and then I am reading the SQL Injection at login panel http://www.securityidiots.com/Web-Pentest/SQL-Injection/bypass-login-using-sql-injection.html & found a bypass ' OR 1=1 /* it didn’t bypass the login and give me access instead of server disclose the password variable contain the password=***REDACTED***

Press enter or click to view image in full size

Simple reported the issue to the team & this replay

Press enter or click to view image in full size

I hope you guys like it :)

./Logout

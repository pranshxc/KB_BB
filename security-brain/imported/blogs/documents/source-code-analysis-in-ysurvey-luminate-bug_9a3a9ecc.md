---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-10_source-code-analysis-in-ysurvey-luminate-bug.md
original_filename: 2018-04-10_source-code-analysis-in-ysurvey-luminate-bug.md
title: Source Code Analysis in YSurvey — Luminate bug
category: documents
detected_topics:
- access-control
- sqli
- command-injection
tags:
- imported
- documents
- access-control
- sqli
- command-injection
language: en
raw_sha256: 9a3a9ecc69f4f761c4f9a19a40ace236291e1bab0e8120407a3555f956c3a2c9
text_sha256: daffd7ad576fa2c60e1065febd21d45e93bb44b00c6cc40983631a0e2fef1520
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Source Code Analysis in YSurvey — Luminate bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-10_source-code-analysis-in-ysurvey-luminate-bug.md
- Source Type: markdown
- Detected Topics: access-control, sqli, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9a3a9ecc69f4f761c4f9a19a40ace236291e1bab0e8120407a3555f956c3a2c9`
- Text SHA256: `daffd7ad576fa2c60e1065febd21d45e93bb44b00c6cc40983631a0e2fef1520`


## Content

---
title: "Source Code Analysis in YSurvey — Luminate bug"
url: "https://medium.com/@rojanrijal/source-code-analysis-in-ysurvey-luminate-bug-c86dc29b70c4"
authors: ["Rojan Rijal (@uraniumhacker)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Authentication bypass", "Broken authorization", "SQL injection"]
publication_date: "2018-04-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5925
scraped_via: "browseros"
---

# Source Code Analysis in YSurvey — Luminate bug

Source Code Analysis in YSurvey — Luminate bug
Rojan Rijal
Follow
2 min read
·
Apr 11, 2018

111

2

This is going to be a really short bug and also an example of why you should do source code analysis when applicable.

When analyzing a web application add-on that Yahoo has for Luminate, I decided to check YSurvey by checking its source code as well. YSurvey allows website owners to create surveys for their visitors. Based on how it is designed, there is only one admin in YSurvey which will be the website owner. Users filling the survey have no user accounts. This will be an important piece to know to understand this bug.

During the analysis, I found out that when accessing the admin panel, there was a cookie that was identifying if user was an admin. This code simply checked if the cookie was set to cid=1 or not.

So, I opened an incognito session, and modified the cookie on the fly. Once the cid=1 was added, it gave me access to admin panel of that website (Video 1).

Video 1: Conducting request from Burp

After finding access to admin access, I wanted to see if I could escalate the attack and have a chance to make it more severe. This is when a SQL injection vulnerability was discovered in YSbuilder.

Get Rojan Rijal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After finding this vulnerability and reporting this, I started to analyze the source code. During the analysis it was found that when admin loads their survey templates, a GET request is made which queries to the SQL database. This was vulnerable to SQL injection because of the code:

Press enter or click to view image in full size
PHP code that made the sql query

In this code, t_id was directly grabbed from the GET request without any form of sanitization.

This made everything severe because we could now access the root sql database and leverage it to attack the older version of PHPmyadmin they had installed. This would give us multiple access like FTP allowing attacker to deface the whole website of the user.

Timeline:
September 18, 2017: Initial report sent

September 18, 2017: Triaged and Bounty Awarded

September 18, 2017: More analysis given which included a SQL injection

For the fix, Yahoo decided to discontinue YSurvey which was a wise and good choice because there are other resources that do the same thing and can help make Yahoo Small Business more efficient for their users.

It was extremely fun to work with Yahoo’s security team on these vulnerabilities. If you haven’t already, I extremely recommend that you tryout their program.

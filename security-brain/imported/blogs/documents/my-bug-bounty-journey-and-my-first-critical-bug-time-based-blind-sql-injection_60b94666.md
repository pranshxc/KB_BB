---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-17_my-bug-bounty-journey-and-my-first-critical-bug-time-based-blind-sql-injection.md
original_filename: 2020-12-17_my-bug-bounty-journey-and-my-first-critical-bug-time-based-blind-sql-injection.md
title: My Bug Bounty Journey and My First Critical Bug — Time Based Blind SQL Injection
category: documents
detected_topics:
- sqli
- password-reset
- idor
- xss
- command-injection
- otp
tags:
- imported
- documents
- sqli
- password-reset
- idor
- xss
- command-injection
- otp
language: en
raw_sha256: 60b946666f701b5734dc7b4b9c52cc57116f7b19973a360abdf953260a278494
text_sha256: 6749c1737e8f06611b11a4a6d81c038bc9c3f9c427635b0ced309126b3ff8e0c
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# My Bug Bounty Journey and My First Critical Bug — Time Based Blind SQL Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-17_my-bug-bounty-journey-and-my-first-critical-bug-time-based-blind-sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, password-reset, idor, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `60b946666f701b5734dc7b4b9c52cc57116f7b19973a360abdf953260a278494`
- Text SHA256: `6749c1737e8f06611b11a4a6d81c038bc9c3f9c427635b0ced309126b3ff8e0c`


## Content

---
title: "My Bug Bounty Journey and My First Critical Bug — Time Based Blind SQL Injection"
url: "https://marxchryz.medium.com/my-bug-bounty-journey-and-my-first-critical-bug-time-based-blind-sql-injection-aa91d8276e41"
authors: ["Marx Chryz"]
bugs: ["SQL injection"]
bounty: "3,500"
publication_date: "2020-12-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4062
scraped_via: "browseros"
---

# My Bug Bounty Journey and My First Critical Bug — Time Based Blind SQL Injection

Top highlight

My Bug Bounty Journey and My First Critical Bug — Time Based Blind SQL Injection
Marx Chryz Del Mundo
Follow
6 min read
·
Dec 17, 2020

711

9

Hello everyone, I am Marx Chryz and I am new to bug bounty hunting even though I do web penetration testing for more than a year.

My Story

I only thought about bug bounty hunting last May but it is only a month after that, that I tried to study. It is hard to start because I don’t have any motivation to learn and I was shocked because there are so much things that I need to know. There are lot’s of times I doubt myself because I think I’m not better than anyone.

Until something motivated me. It is a talk from RootCon Recovery Mode Last October that pushed me to study more. I was inspired when a speaker said about “Cleartext Transmission of Sensitive Data”. It is a vulnerability that lies when a form that handles sensitive data such as email and password, is submitted via an insecure connection or http. It is a very low hanging bug but I heard only about that in RootCon. After hearing that, I was like “Hey I shouldn’t have doubted myself, It is not I am weak that I can’t find bugs, but it is just I don’t know what types of bug exist”. From there, I started on reading Bugcrowd’s VRT to be able to familiarize myself about bugs, and I read also the Web Application Hacker’s Handbook by Dafydd Stuttard and Web Hacking 101 by Peter Yaworski. I also built a habit of reading writeups everyday to learn more about others experiences.

In a span of few weeks, I learned more than what I learned when I am not motivated. Aside from reading, I watched several videos of Stök, Farah Hawa, and other bug bounty hunters including the talks of Jason Haddix, Peter Yaworski, and James Kettle.

Finding Bugs

I started on looking for low hanging bugs such as bugs related to session and non-expiring password reset tokens, and luckily I managed to gain $100 bounty on that and that was my first bounty! From there, I decided to level up what I hunt so I started looking for XSS and I also managed to find one! The XSS vulnerability occurs because a Content-Type of text/html is returned on a json endpoint. But sadly, It turned out as P5, because only admins can exploit that vulnerability.

Out of frustration that my XSS is P5 instead of P3, I tried to hunt another XSS on the same program. I did some subdomain enumeration and found a subdomain that I didn’t tested before, so why not give it a try? There’s a login page so I created an account to signup.

Press enter or click to view image in full size

Upon browsing the site, I noticed that there’s a search button so I tried doing XSS there but it failed. I didn’t tried for SQL Injection because I thought that would be pretty dumb to do, I guess the developers manage to sanitize that. But something caught my eye, there is a sort button when you click the titles (Referral ID, Type, etc…), that may be possible to be SQL Injection vulnerable!

After clicking it, I was redirected to the URL ?order=type&ordering=ASC&search= Hey! the ASC value seems familiar, is the backend using something like “SELECT * FROM referrals ORDER BY type ASC”? Out of curiosity, I did a typical way to test for SQLi, the single quote (‘). So I changed order=type to order=type’ and to my surprise, the server responsed with an Error 500! I am one step towards SQL Injection! I am just looking for XSS and found a possible SQLi vulnerability.

All I need to do is give a valid proof of concept so I can do a write up. I thought of doing DIOS (dump in one shot for union based SQL Injection). I tried for hours but I can’t do union select 1,2,3,4,5…18--+- All I can do is order by 18. While this proves the existence of SQL Injection, this isn’t enough to be a risk. I need to demonstrate that I got something from their database.

Get Marx Chryz Del Mundo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Upon searching and trying various payloads on my localhost, I realized that UNION SELECT is not possible for queries after the ORDER BY clause since they’re query must be something like “SELECT * FROM referrals ORDER BY type ASC”. So union based SQL Injection is not possible, what if I try something like error based or time based? After trying Error Based, I realized I can’t do that as well because the site only returns a blank page with status of 500, there are no error messages, I can’t do error based. The last resort for me is time based SQL Injection.

I tried some payloads for MySQL, MSSQL, and PostgreSQL but nothing worked, even though the payloads are valid when I tried simulating it on my localhost’s phpmyadmin. None of the most basic payload even worked:
sleep(10)--
benchmark(1000000000,md5(1))--
pg_sleep(10)--
; WAITFOR DELAY ‘00:00:10’;--

I thought, maybe theres a WAF. What if my payloads are blocked. So I tried various WAF bypass techniques but yeah, none worked. I thought, what if the functions such as sleep() and benchmark() are disabled? How could I do time based without this functions for time based?

Since It appears I can’t use those functions, I tried doing boolean based blind with the payload if(1=1,1,(select 1 union select 2)). In simple terms, since the page returns error 500 when there’s an SQL error, if 1=1, then the server must return success 200. But if I used the payload if(1>2,1,(select 1 union select 2)), the server must reply error 500. This happens because my theoretical query is “SELECT * FROM referrals ORDER BY (select 1 union select 2) ASC” and that throws a “subquery returns more than 1 row” based on how I try on my localhost. But guess what? Nothing worked. it appears that the =,< and > is blocked.

I almost gave up at this moment. Then I thought of going back to time based blind because I realized that “Hey, Im trying too many payloads (postgre, mysql, mssql) what if I try to get the database version to lessen my scope of payloads?” But how am I gonna get the db version without time based SQL Injection?

I remembered something, SQL/*!50000 Comments*/. The number 50000 specifies tells the SQL Server to execute the payload inside the comment if the version of SQL is at least 5.00.00. In theory, when I have a payload of /*!50000someInvalidSQLSyntax*/, the page must response with error 500 if the SQL version is at least 5.0.0, if it’s <5.0.0, it must return a normal page.

Let’s bruteforce the version using Burp Intruder. After doing a bruteforce per digit
/*!50731someInvalidSQLSyntax*/ returns an error 500
/*!50732someInvalidSQLSyntax*/ returns a success 200
This means that the version is 5.7.31. Hey, this is a MySQL Server. So going back to the payloads above, I must only try the sleep() and benchmark() since it works on MySQL 5.7.31.

After having the database version enumerated, I felt like I have made some progress after hours of trying and googling. After some time again, I’m still stuck. But glad, google comes to help and I found the payload (select*from(select(sleep(10)))a) and BOOM!

Press enter or click to view image in full size

IT WORKED!!! And now that the server sleep for 10 seconds, I must sleep also (It’s 5am in the morning and I have class lol)

I was shocked when it finally worked. I tried several hours for this and I’ts very pleasing to the eye seeing my payload work. I was nervous because it was my first critical bug and I know they pay high for crits. So I tried again altering the payload and changing the delay time to prove that the delay is not because of my network provider, I tried another one with delay of 30 seconds. And It still worked.

Press enter or click to view image in full size

Finally, I did a report and I passed it to them as fast as I can without sacrificing the quality of report because I won’t get paid if my report is trash and if they can’t replicate my vulnerability.

Report Timeline

Nov 23, 2020 — Bug Submitted
Nov 25, 2020 — Bug Fixed
Dec 12, 2020 — Triaged as mid P1-P2 and eligible for $3500 bounty
Dec 17, 2020 — Bounty Received

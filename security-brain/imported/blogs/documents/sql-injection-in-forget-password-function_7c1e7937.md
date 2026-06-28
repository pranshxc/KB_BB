---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-18_sql-injection-in-forget-password-function.md
original_filename: 2019-07-18_sql-injection-in-forget-password-function.md
title: SQL Injection in Forget Password Function
category: documents
detected_topics:
- sqli
- idor
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- sqli
- idor
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 7c1e79370c09019f83e4ae6f09fc81b290caa1fb008348da391e8b1837916de7
text_sha256: 41d836f9a71c54aac7a4110b9a6e37fa51ed4c7da90f17497cbf7e1034e1cee2
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection in Forget Password Function

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-18_sql-injection-in-forget-password-function.md
- Source Type: markdown
- Detected Topics: sqli, idor, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `7c1e79370c09019f83e4ae6f09fc81b290caa1fb008348da391e8b1837916de7`
- Text SHA256: `41d836f9a71c54aac7a4110b9a6e37fa51ed4c7da90f17497cbf7e1034e1cee2`


## Content

---
title: "SQL Injection in Forget Password Function"
url: "https://medium.com/@kgaber99/sql-injection-in-forget-password-function-3c945512e3cb"
authors: ["Khaled Gaber"]
bugs: ["SQL injection"]
publication_date: "2019-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5137
scraped_via: "browseros"
---

# SQL Injection in Forget Password Function

SQL Injection in Forget Password Function
khaled gaber
Follow
3 min read
·
Jul 18, 2019

529

3

This is my first time on Medium and I wanted to share with you my first SQL injection bug reported to a private bug bounty program let’s name it “example.com” which I discovered in forget password function which I usually look for logical bugs in this function instead of SQLi.

Enumeration Phase

First, try to test the normal behavior of any function before starting to manipulate the input parameters or thinking of how to abuse it, this will make your hunting life much easier and identify the bugs much faster.

Testing the normal behavior by submitting an already existed user email and the response was

Press enter or click to view image in full size

And when submitting an email like “idontexist@test.com” the response was

Press enter or click to view image in full size

Now the time comes for our SQLi testing. first, I tried to end my input with a single quote and the response was “Unable to access data” which was very suspicious.

Knowing that when single quote repeated twice is treated as a literal character, not a special one, I ended my input with two single quotes like [ test@test.com’’ ], Then we had the normal response of the non-existed mail and this was close to prove that this function is vulnerable to SQLi. Also, this clarifies the importance of understanding the application’s behavior and normal response messages.

One of the most important web application enumeration steps is to identify the back-end language and technologies and this sometimes leads to expecting the DBMS engine. From web page extensions like “RetrievePassword.aspx”, the pentester identified that back-end language is “ASP.NET” which always comes with MSSQL server as a DBMS engine. This little piece of information made the exploitation very easy to craft targeted payloads.

Get khaled gaber’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Exploitation Phase:

The basic SQLi exploitation steps are to break the query which we did with single quotes then fix the query with a comment character, then inject anything in between.

After trying a couple of payloads and special characters we were able to inject and fix our query with a payload like the following one [ test@test.com’) — ]

Now I can finally exploit this SQLi vulnerability and started with a simple technique called “Time-Based” which delays the database server responses with a specific amount of time. (WAIT FOR DELAY ‘hh:mm:ss’) is a MSSQL function that suspends the execution for the specified amount of time

as a PoC I was able to delay database server responses up to 30 seconds using the following payload [ anyInput’) WAITFOR DELAY ‘0:0:30’ — ]

Attack Automation:

Since it’s a Time-Based SQLi, it’s very hard to make the exploitation and data exfiltration manually and here “SQLMap” comes to rescue to automate this process.

Submit this vulnerable request and intercept it with “Burp Suite” proxy tool, replace the “E-mail” value with an “*” to be detected by SQLMap as a custom injection point, and save this request.

After a couple tries with SQLMap options, the final command that was used to exploit this SQLi and extract the Database names was:

Press enter or click to view image in full size
Press enter or click to view image in full size

The next steps are to identify the application database then tables and columns then dump data of the juicy columns like usernames, emails, and passwords which were saved as a clear-text format.

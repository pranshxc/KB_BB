---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-14_how-i-found-blind-sql-injection-just-by-browsing-and-getting-a-unique-url.md
original_filename: 2021-07-14_how-i-found-blind-sql-injection-just-by-browsing-and-getting-a-unique-url.md
title: How I found Blind SQL Injection just by browsing and getting a unique URL
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: b1f7387c398b5ce9c588e2ae9549eea610f31050734bdbd8cfb8412bd4186efa
text_sha256: 36d8a0042335bfb0d59427a558cbccdd9542ba552fc67161a665c8b94b709827
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I found Blind SQL Injection just by browsing and getting a unique URL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-14_how-i-found-blind-sql-injection-just-by-browsing-and-getting-a-unique-url.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `b1f7387c398b5ce9c588e2ae9549eea610f31050734bdbd8cfb8412bd4186efa`
- Text SHA256: `36d8a0042335bfb0d59427a558cbccdd9542ba552fc67161a665c8b94b709827`


## Content

---
title: "How I found Blind SQL Injection just by browsing and getting a unique URL"
url: "https://medium.com/@jawadmahdi/how-i-found-blind-sql-injection-just-by-browsing-and-getting-a-unique-url-ed87fa1f35ed"
authors: ["Jawad Mahdi (@hunter0x1)"]
bugs: ["SQL injection"]
publication_date: "2021-07-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3506
scraped_via: "browseros"
---

# How I found Blind SQL Injection just by browsing and getting a unique URL

Jawad Mahdi
 highlighted

How I found Blind SQL Injection just by browsing and getting a unique URL
Jawad Mahdi
Follow
2 min read
·
Jul 16, 2021

258

Hello Guys! I am a part-time bug hunter at Bugcrowd and I will share how I found a Blind SQL INJECTION manually just by browsing and checking http history in BURPSUITE.

So basically, I was Invited to a private program on Bugcrowd. That site was based on Laravel Framework and I thought they might be using MYSQL DATABASE. So I decided to test Blind SQL INJECTION on that site.

I manually browsed all the URLS and they were getting collected in BURPSUITE HTTP HISTORY. I found a unique POST request which weren’t normally available. So I suddenly remembered that sometimes manually browsing can get you unique URLS if you use a PROXY like Burpsuite, I read it in WEB APPLICATION HACKER HANDBOOK.

I found many parameters in that POST request and I started checking those parameters with this payload

‘XOR(if(now()=sysdate(),sleep(5*1),0))OR’

And to my surprise, It worked and slept for 5 seconds. I immediately copied the request and used SQLMAP on that.

I used different SQLMAP command but a firewall was blocking me from fetching the current database.

Get Jawad Mahdi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I then launched this command

sqlmap.py -r request.txt -p “value” -v 3 — level=5 — risk=3 — time-sec=15 — tamper=between — current-db — no-cast

and guess what?

Press enter or click to view image in full size

I was able to retrieve the current database name.

Takeaways

Always check each and every request which you think might be querying with database and check SQL INJECTION there with manual testing and fuzzing and check those responses carefully.

Thank you for reading!

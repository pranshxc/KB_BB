---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-16_sql-in-everywhere.md
original_filename: 2017-11-16_sql-in-everywhere.md
title: SQL in everywhere.
category: documents
detected_topics:
- sqli
- xss
- command-injection
- api-security
tags:
- imported
- documents
- sqli
- xss
- command-injection
- api-security
language: en
raw_sha256: 2b55b1e280942d27ca75a9ceb144b29a4f7e3afdc10fd5805b105abfe66d1548
text_sha256: 717997d826795be304b88cd43ed9b01c01a7d93e5b46043a7adf7f42eb782efd
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# SQL in everywhere.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-16_sql-in-everywhere.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `2b55b1e280942d27ca75a9ceb144b29a4f7e3afdc10fd5805b105abfe66d1548`
- Text SHA256: `717997d826795be304b88cd43ed9b01c01a7d93e5b46043a7adf7f42eb782efd`


## Content

---
title: "SQL in everywhere."
page_title: "SQLi is everywhere.. Hi, | by Utkarsh Agrawal | Medium"
url: "https://medium.com/@agrawalsmart7/sql-is-every-where-5cba6ae9480a"
authors: ["Utkarsh Agrawal (@agrawalsmart7)"]
bugs: ["SQL injection"]
publication_date: "2017-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6050
scraped_via: "browseros"
---

# SQL in everywhere.

Utkarsh Agrawal
 highlighted

Utkarsh Agrawal
Follow
2 min read
·
Nov 16, 2017

101

SQLi is everywhere.

Hi,

This is my first blog post so I am very excited to share this.

This is the story of 3 SQL injection which i found on a program. I am not taken name of that instead let’s say “abc.com” domain.

So as proceed with my first step to collecting the url’s of abc.com domain. So I started digging and collect hundred of urls. And then i started to see if i get some interesting one. And yes, I found a very interesting url which contains a lot of parameters. Something like this.

“ http://abc.com/file.php?ref=-3&uploader=plupload&single=&local=&search=&offset=0&order_by=relevance&sort=DESC&archive=0&collection=&metadatatemplate=&relateto=&redirecturl=”

Get Utkarsh Agrawal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I was very curious to test this URL because more params more opportunities. My first test case is always “XSS” (Developer most of the time forgot to sanitize all the input parameters.). So i started digging for XSS but failed. Now I move on to the SQL by injecting the single quote (‘) to each of the parameter and one parameter i found that is vulnerable to the SQL injection and i.e. sort=DESC. When i inject single quote to that parameter and luckily i got the SQL syntax error with leaking the database name and version no. Then I was like

I quickly submitted that bug to the team. And then i took a deep breath and sit aside. Next day, again i started to check the all the url which are found yesterday to test some other vulnerabilities but wait a minute. There is a POST request for edit the profile, and When we click the submit button the POST request contains post parameter and in these i found interesting parameter “resource_type=2" So i submitted single quote to that, again i found beautiful SQL syntax error. (Off course this was not the case for XSS and any other.)

One last, On that request i saw that there is a same parameter which i found first i.e. sort=DESC in the cookie section, so i was pretty sure that this is also be vulnerable and Yes it is. So i submitted all 3 SQL bugs to that company.

I didn’t sleep full night, Excitement ;), And quickly i got triage and Resolved Reputation. But No rewards, they notified “At this time we are not award any bounties and cash rewards” on the Report policy as i know. But I will never forget that awesome feeling when i found.

But anyways through this experience, We should agree that “Web application always have some vulnerabilities so you are need to find them which are hidden behind the curtains.”

Thank you. Hope you liked it. Tweet me @agrawalsmart7

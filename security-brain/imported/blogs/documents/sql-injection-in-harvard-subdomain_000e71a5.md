---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-02_sql-injection-in-harvard-subdomain_2.md
original_filename: 2021-09-02_sql-injection-in-harvard-subdomain_2.md
title: SQL injection in harvard subdomain
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
raw_sha256: 000e71a50888f19d600f5c5e2a272fe2df8a5da10a3f17e596bc25d02d841517
text_sha256: ff58d42c420c3e1feb71e0b44d33e820dd5275c5f94f00afd144bf0a9099ccf6
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# SQL injection in harvard subdomain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-02_sql-injection-in-harvard-subdomain_2.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `000e71a50888f19d600f5c5e2a272fe2df8a5da10a3f17e596bc25d02d841517`
- Text SHA256: `ff58d42c420c3e1feb71e0b44d33e820dd5275c5f94f00afd144bf0a9099ccf6`


## Content

---
title: "SQL injection in harvard subdomain"
url: "https://noob3xploiter.medium.com/sql-injection-in-harvard-subdomain-be67a5dbf664"
authors: ["Brandon Roldan (@tomorrowisnew_)"]
programs: ["Harvard University"]
bugs: ["XSS", "SQL injection"]
publication_date: "2021-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3356
scraped_via: "browseros"
---

# SQL injection in harvard subdomain

SQL injection in harvard subdomain
Brandon Roldan
3 min read
·
Sep 2, 2021

--

4

Hi. In this writeup, i will show you a sqli that i found in harvard and also, a xss as a bonus

While looking through the subdomains of harvard, i found this one interesting subdomain https://schedule.med.harvard.edu/ . I fuzzed the directory using ffuf and found this one interesting endpoint availability.php

Press enter or click to view image in full size

Visiting that endpoint only gave me this.

So i fuzzed the parameters using arjun and found an interesting parameter called users. I tried it again with the users parameter and saw this

This is the same error message as before. So i guessed i only have to provide a year parameter. I did that and it worked.

Again, its the same as before, i provided a month parameter and it worked.

It worked again, but now, its asking for a day parameter, i gave it and it showed me this

Press enter or click to view image in full size

We can see that our input in users parameter is reflected so i tried to get an xss. And it worked

Press enter or click to view image in full size

So we have an xss. I quickly reported it and tried testing the other parameters. I tried adding ‘ in the day parameter and it gave me an sql error.

Press enter or click to view image in full size

So, i have an sqli injection here. Since i suck at sql injection, i just let sqlmap do the job for me and sqlmap worked.

I dumped the tables. I didnt go any further anymore and reported it to them.

Get Brandon Roldan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The sqli got accepted but the xss does not. Apparently, harvard dont accept xss which sucks since i reported alot of xss to them

This is now fixed so i decided to publish it. Visiting the subdomain will show this

And visiting the endpoint https://schedule.med.harvard.edu/availability.php will throw a 404 error.

Thats the end of the writeup, thanks for reading.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-10_sql-injection-for-50-bounty-but-still-worth-reading.md
original_filename: 2019-03-10_sql-injection-for-50-bounty-but-still-worth-reading.md
title: SQL injection for $50 bounty, but still worth reading!!
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
raw_sha256: f56cf1b41fd17b1df20fca17b47a4643fd9c75848fedabb39b279b00c7a8cd49
text_sha256: 71c0327b7b55d4e9c014fc6d3ee2c2dcbf0c0045d3c06792993934cb7d4ffe1f
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# SQL injection for $50 bounty, but still worth reading!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-10_sql-injection-for-50-bounty-but-still-worth-reading.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f56cf1b41fd17b1df20fca17b47a4643fd9c75848fedabb39b279b00c7a8cd49`
- Text SHA256: `71c0327b7b55d4e9c014fc6d3ee2c2dcbf0c0045d3c06792993934cb7d4ffe1f`


## Content

---
title: "SQL injection for $50 bounty, but still worth reading!!"
url: "https://medium.com/@orthonviper/sql-injection-for-50-bounty-but-still-worth-reading-468442c1cc1a"
authors: ["Ronaldo Messi"]
bugs: ["SQL injection"]
bounty: "50"
publication_date: "2019-03-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5370
scraped_via: "browseros"
---

# SQL injection for $50 bounty, but still worth reading!!

SQL injection for $50 bounty, but still worth reading!!
Sunil Yedla
Follow
2 min read
·
Mar 11, 2019

275

2

Hey guyzz …!!! I hope you all are doing well. Today I’m fully disclosing a PoC demonstration along with some brief documentation of this exploit.

This is a writeup of bug which I found in one of the private programs of Hackerone. Since it is a private program i can’t disclose the name of the program(please note that, i will be referring the program name as : “Redacted” throughout this article). I found SQL injection, in one of their endpoints: “/rest/aom/index?id=”

I’ve been investigating this program since many days and i always end up finding low severity bugs. One day while while loading a url : https://www.redacted.com/aom?utm_source=Frontpage&utm_medium=banner%20popup&utm_campaign=Frontpage%20popup%20June17%20AOM , found an endpoint where I’ve seen id parameter. Old/Basic trick ( ‘ after the ID value ) worked and that is how i found my first sql injection 2 years ago. Below are the complete steps of reproduction.

Steps to reproduce :

loaded the url : https://www.redacted.com/aom?utm_source=Frontpage&utm_medium=banner%20popup&utm_campaign=Frontpage%20popup%20June17%20AOM in mozilla firefox broswer.
Click on the “ FOLLOW “ and capture the requests in Burpsuite.
Now you will get many request followed by host :https://redacted.com, wait for the right endpoint.
I found an endpoint like this:

GET /rest/aom/index?id=3 HTTP/1.1
Host: www.redacted.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0
Accept: /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Requested-With: XMLHttpRequest
Referer: https://www.redacted.com/aom?utm_source=Frontpage%22%3E%3Cscript%20%3Ealert(document.cookie)%3C/script%3E&utm_medium=banner%20popup%22%3E%3Cscript%20%3Ealert(document.cookie)%3C/script%3E&utm_campaign=Frontpage%20popup%20June17%20AOM%22%3E%3Cscript%20%3Ealert(document.cookie)%3C/script%3E
Cookie: __utma=155410345.398014507.1478469081.1478469081.1478724130.2; _ga=GA1.2.398014507.1478469081; aom_popup=1; thumbnail_size=large; __stripe_mid=414d123e-85b7–4737-a479–7693beba627c; _gid=GA1.2.1421519450.1497256887; PHPSESSID=3celt75q8oh51e2jjkdl86iihjo7t3bcrh0lilfauq7odi5behjavnd8i3hsrog6ek1lb437uvu6pv3c8qd2jalt0l1jkjekl93a8f1; language=en; heartbeat=1497297643; _gat=1
Connection: close

5. The very basic check for confirming if a site is vulnerable to SQL Injection is by keeping : ‘ after id value. That is exactly what i did.

6. Now, Server response is like this :

Get Sunil Yedla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

{“message”:”SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ‘’) LIMIT 1' at line 1, query was: SELECT aom_campaign.* FROM aom_campaign WHERE (id=3') LIMIT 1"}

7. I have confirmed that this is not browser or device specific and proceeded with submission.

They awarded me a bounty of $50 and 15 points and HOF. yeah i do think $50 was low for a SQL injection but knowing the fact that the minimum bounty of this program is only 10$, I was okay with it. BTW I found another sql injection on the same day in another endpoint which awarded me the same amount.

Report Time Line :

Submitted report on Hackerone — Jun 13th (2 years ago)

Redacted commented — Jun 13th (2 years ago)

Report Triaged — Jun 13th (2 years ago)

Added more info–Jun 15th (2 years ago)

Status changed to Resolved — Jun 16th (2 years ago)

Awarded 15 points and $50 — Jun 19th (2 years ago)

Thanks for reading!!

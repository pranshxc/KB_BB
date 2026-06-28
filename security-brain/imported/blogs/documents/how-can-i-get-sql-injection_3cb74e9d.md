---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-02_how-can-i-get-sql-injection.md
original_filename: 2022-09-02_how-can-i-get-sql-injection.md
title: How can i get SQL Injection
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
raw_sha256: 3cb74e9dd73682882bf8fdbc95a5773694d1db93b258fc673d52629dc5bdacec
text_sha256: 1171fe2f68cebbc5c2146a336819edf5c5e1dc5a894b2ef661b35fc39a28b8a4
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How can i get SQL Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-02_how-can-i-get-sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `3cb74e9dd73682882bf8fdbc95a5773694d1db93b258fc673d52629dc5bdacec`
- Text SHA256: `1171fe2f68cebbc5c2146a336819edf5c5e1dc5a894b2ef661b35fc39a28b8a4`


## Content

---
title: "How can i get SQL Injection"
url: "https://xthemo.medium.com/how-can-i-get-sql-injection-b8337c2c2bef"
authors: ["Mohamed Abdelhady"]
bugs: ["SQL injection"]
publication_date: "2022-09-02"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2226
scraped_via: "browseros"
---

# How can i get SQL Injection

How can i get SQL Injection
Mohamed Abdelhady
Follow
2 min read
·
Sep 2, 2022

81

2

Hi Guys .

I’m gonna explain How could i get sql injection by easy way.

At First I surf the login page (normal login page)

https://example.com/path/login.aspx

at the beginning I tried default credentials ,but it didn’t work. the second decision was to check the source code . after a while without find anything interesting.

Then I tried login bypasses like admin’- - and all bypasses.

Then I tried NoSQL [$ne] ,but also it didn’t work.

Also I tired the host header in the request X-Forwarded-For|X-Original-URL and most common headers ,but unfortunately it didn’t work .

Get Mohamed Abdelhady’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After trying , So I decided to check JS Files.

Press enter or click to view image in full size

Finally I found a anther Endpoint (internal login page for employees)

https://example.com/path/users/UserLogin2.aspx

I intercept the request and inject single quote (‘) in username field and get SQL error in the response !!!!!!!!!!

Then I inject a SQL query to get the true ordering using ‘ OrDeR/**/By 10000—

Press enter or click to view image in full size

As you see the error represent that false ordering number. And i get the true number.

I tried to get the version of the DBMS. by ‘ UNiOn/**/SelecT null,null,@@version —

Press enter or click to view image in full size

Then i get the database name by ‘ UNiOn SelecT null,null,db_name() —

Press enter or click to view image in full size
Press enter or click to view image in full size

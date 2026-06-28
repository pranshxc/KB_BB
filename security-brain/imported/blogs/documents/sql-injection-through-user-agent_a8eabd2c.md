---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-08_sql-injection-through-user-agent.md
original_filename: 2019-05-08_sql-injection-through-user-agent.md
title: SQL injection through User-Agent
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
raw_sha256: a8eabd2c9cd0b4dae751b57e4fb22a5b2414f7efb4cd5a056e88b259c8cba731
text_sha256: 69ecc82f469ed3f9232f2bc7898f41219592a050e062197c06e0029eedcb8aa9
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# SQL injection through User-Agent

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-08_sql-injection-through-user-agent.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `a8eabd2c9cd0b4dae751b57e4fb22a5b2414f7efb4cd5a056e88b259c8cba731`
- Text SHA256: `69ecc82f469ed3f9232f2bc7898f41219592a050e062197c06e0029eedcb8aa9`


## Content

---
title: "SQL injection through User-Agent"
url: "https://medium.com/@frostnull1337/sql-injection-through-user-agent-44a1150f6888"
authors: ["fr0stNuLL"]
bugs: ["SQL injection"]
publication_date: "2019-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5268
scraped_via: "browseros"
---

# SQL injection through User-Agent

Top highlight

SQL injection through User-Agent
fr0stNuLL
Follow
4 min read
·
May 9, 2019

601

8

Hi everyone, in this simple tutorial I will describe how I was able to exploit a SQL injection, using the user-agent as vector. First of all, I will leave “blur” in the sensitive parts as it was requested from the customer of the private program. After authenticating in the application I came across the following request:

Press enter or click to view image in full size

After, try several things .. and application always return “OK” in the response .. I put a single quote (‘) in the User-Agent Header .. result, instead of the application return 200 OK, returned 401 .. as demonstrated below:

Press enter or click to view image in full size

Next step was trying to exploit some SQL injection payloads, after a few tries it sees that the application was vulnerable to a type of SQL injection Boolean based. Putting the tests into practice, when the payload ‘ AND’ 1 ‘=’ 1 was inserted into the User-Agent the application returned 200 OK, when the payload ‘ AND’ 1 ‘=’ 2 was entered the application returned 401. The images below illustrate the fact:

Press enter or click to view image in full size
Press enter or click to view image in full size

After confirming that the application was vulnerable, the next step was to try to verify which version of the database the application was using. For this, I have tested functions of the Oracle, MySQL, MicrosoftSQL etc. databases. Finally, through the payload ‘ and substring(@@version,1,1)=1=’1'’, it was possible to identify that the database was MySQL or MariaDB. The images bellow show the fact:

OBS: if you don’t know what the function substring here you can found :)

Press enter or click to view image in full size
Press enter or click to view image in full size

After iterates the values of substring function i got the version i it was 10.1.21 Mariadb.

Get fr0stNuLL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

A cool trick when you find a Boolean based, is to test if there is a possibility of using a “subselect”, in my case it was possible.

Press enter or click to view image in full size

To get the name of the table, it is necessary to make a wordlist with some familiar names and it is also cool, to make a wordlist with the name of the company. Through the following payload ‘ AND (select 1 from “WORDLIST” limit 0,1)=1+‘, it was possible to get the name of the table “app_user”, see that in the image the below is returned 200 OK in the response of the server.

Press enter or click to view image in full size

Now, that we have the name of the table, we go behind the name of the columns so we can get the user and the password. In the same way that it was exploited to get the table name, an attempt / error is also used here with common names used in colums such as user, password, user_pass, passwd, etc. The following images illustrate the name of the retrieved columns.

Press enter or click to view image in full size
Press enter or click to view image in full size

Finally, the following payload looks for the “password” column in the “app_user” table where the user id is equal to ‘X’ and brings the user password in the application.

Press enter or click to view image in full size
Return 200 “OK” for user id 971
Press enter or click to view image in full size
Return 401 for user id 972

This is all personal, I can not show the rest with the passwords in the application because it would violate some terms :) any doubt we are together. Sharing is Caring :)

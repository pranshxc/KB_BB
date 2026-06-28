---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-13_sql-injection-remote-code-execution-double-p1.md
original_filename: 2020-09-13_sql-injection-remote-code-execution-double-p1.md
title: SQL Injection & Remote Code Execution - Double P1
category: documents
detected_topics:
- sqli
- command-injection
- ssrf
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- ssrf
- api-security
language: en
raw_sha256: 90f5969cbd0a76810358bd32a89470ceb176f81a20fe02e64eb07609d933c412
text_sha256: c148a054c7032597c72813098cfb926ab460a0406fcaccbd590af7e405e036b3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection & Remote Code Execution - Double P1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-13_sql-injection-remote-code-execution-double-p1.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, ssrf, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `90f5969cbd0a76810358bd32a89470ceb176f81a20fe02e64eb07609d933c412`
- Text SHA256: `c148a054c7032597c72813098cfb926ab460a0406fcaccbd590af7e405e036b3`


## Content

---
title: "SQL Injection & Remote Code Execution - Double P1"
url: "https://medium.com/@shahjerry33/sql-injection-remote-code-execution-double-p1-6038ca88a2ec"
authors: ["Shrey Shah (@ShreySh43332033)"]
bugs: ["SQL injection", "RCE"]
publication_date: "2020-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4266
scraped_via: "browseros"
---

# SQL Injection & Remote Code Execution - Double P1

Top highlight

SQL Injection & Remote Code Execution - Double P1
Jerry Shah (Jerry)
Follow
5 min read
·
Sep 13, 2020

477

Hello everyone I thought of sharing my recent finding of Double P1 which recently got solved and they are sending me Goodie Pack for it. It was a Responsible Disclosure program on which I found this. I found SQLi first and it was a normal database version disclosure so they said we can accept it only when you find something interesting, so I tried to exploit more and got the admin credentials, this SQLi was tough for me. Later after 3 days I enumerated one of its subdomain and found phpmyadmin, I randomly tried the credentials that I obtained using SQLi and I got the access. Then I used a simple PHP script to upload my shell and then I got a RCE.

Company Message 1
Press enter or click to view image in full size
Company Message 2

Summary :

Everyone knows what is SQLi and what is RCE, so I’m not going to give a brief in this blog. I’ll be sharing the technique and cheat sheet that I used for exploitation.

For SQLi I used https://dev.mysql.com/doc/refman/8.0/en/select.html for knowing the query structure, it helped me a lot in exploiting SQLi on the website. I was only able to find the name of database, table names, column names and database version. But I wanted to exploit it more to because I wanted admin credentials so I googled SQLi cheatsheet and found this http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet. It helped me a lot and finally I found the admin credentials. It was a hash obviously, so I used https://crackstation.net/ to crack the hash. I also wanted to check schema table because it contains a lot of information so I used this : https://dev.mysql.com/doc/refman/8.0/en/information-schema.html.

For Remote code execution I used a simple payload inside phpmyadmin page and I got RCE.

Payload : SELECT “<?php system($_GET[‘<anyParameter>’]); ?>” into outfile “/var/www/html/<filename>.php”

I found SQLi vulnerability on 2nd level subdomain and RCE was on 3rd level subdomain.

How I found this vulnerability ?

I found a parameter and 1st I tried for SSRF but it didn’t work so I thought of trying SQLi, I started with SQLi basic testing and took a help from here : http://www.securityidiots.com/Web-Pentest/SQL-Injection/MSSQL/MSSQL-Error-Based-Injection.html
I found it vulnerable to SQLi and the first thing I enumerated was version and database name. So I used database() function and @@version command here.
Press enter or click to view image in full size
Database Version
Press enter or click to view image in full size
Database Name

3. Then I thought of identifying the user so for that I used a simple user() function

Press enter or click to view image in full size
User name

It was simple till here but they told me to exploit more if I want them to accept my report. So I started researching for further exploitation.

4. I exploited further and found a table name from the schema table

Press enter or click to view image in full size
Table Name

5. I wanted to check for some more tables so I used limit statement. I found a table hotel but this is the one I found previously.

Press enter or click to view image in full size
Table Name

NOTE : LIMIT statement is used to retrieve records from one or more tables in a database and limit the number of records returned based on a limit value. “LIMIT statement is not supported in all SQL databases.”

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6. The next step was to find how many tables are there so I changed the query of limit (check the below screenshot for query)

Press enter or click to view image in full size
Table Name
Press enter or click to view image in full size
Table Name

7. Now I had 3 tables so I wanted to find the columns from the table schema.

NOTE : We had total of three tables so I performed the query accordingly

Press enter or click to view image in full size
Column Names along with the table name

8. I changed the table_schema name to mysql to find what is there in it and I found many important tables and columns

Press enter or click to view image in full size
Column Names along with the table name

9. Next step was to find the admin username and password, I found the credentials and reported to them. But later after 3 days I enumerated the subdomain of a subdomain and lucky those credentials worked their on phpmyadmin page which led me to RCE

Press enter or click to view image in full size
Admin Credentials

Phase 2 (RCE) :

Found the phpmyadmin page, in the credentials obtained the password was in a hash form so I used online tool to crack it
Press enter or click to view image in full size
phpmyadmin

2. I used a simple query to put my file on the server and check for RCE

Press enter or click to view image in full size
Putting my file for RCE

3. And I successfully got the RCE

Press enter or click to view image in full size
Remote Code Execution

4. I wanted to exploit it further to get a system shell-back so I used a simple python script from http://pentestmonkey.net/ to get a system shell I was successful

Press enter or click to view image in full size
Python Script
Press enter or click to view image in full size
System Shell
Press enter or click to view image in full size

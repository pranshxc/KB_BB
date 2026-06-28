---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-16_mssql-injection-in-json-request.md
original_filename: 2021-05-16_mssql-injection-in-json-request.md
title: MSSQL Injection In JSON Request
category: documents
detected_topics:
- sqli
- command-injection
- otp
- mobile-security
tags:
- imported
- documents
- sqli
- command-injection
- otp
- mobile-security
language: en
raw_sha256: fb246adb061a1397da167bb13a2759a304005d2fc7f53211e0e546d91842a4d6
text_sha256: 421bb858d67ee9d3180826e719a0a42af5b406056d57a56d8b558d1d36043c25
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# MSSQL Injection In JSON Request

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-16_mssql-injection-in-json-request.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, otp, mobile-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `fb246adb061a1397da167bb13a2759a304005d2fc7f53211e0e546d91842a4d6`
- Text SHA256: `421bb858d67ee9d3180826e719a0a42af5b406056d57a56d8b558d1d36043c25`


## Content

---
title: "MSSQL Injection In JSON Request"
page_title: "MSSQL Injection In JSON Request – Kailash"
url: "https://kailashbohara.com.np/blog/2021/05/16/MSSQL-Injection-in-JSON-request/"
final_url: "https://kailashbohara.com.np/blog/2021/05/16/MSSQL-Injection-in-JSON-request/"
authors: ["Kailash (@Corrupted_brain)"]
bugs: ["SQL injection"]
publication_date: "2021-05-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3651
---

# [MSSQL Injection In JSON Request](https://corrupted-brain.github.io/blog/blog/2021/05/16/MSSQL-Injection-in-JSON-request/ "MSSQL Injection In JSON Request")

[SQL injection](https://portswigger.net/web-security/sql-injection) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to retrieve. The impact of the SQL Injection can be extracting data from the database, dropping data, gaining OS or SQL shell access etc.

As it was private scope, I do not want to disclose the application name. So, I was testing the android application of it. I had to bypass [SSL pinning](https://developer.android.com/training/articles/security-ssl) to intercept the application requests. Finally, I was able to do it. The first page was the registration page while opening an app, I filled in all the necessary details. An OTP code was sent to our provided phone number. I used a random six-digit code and intercepted the OTP validation request as shown below. ![Registration request](/images/posts/app_registration.png) Then I sent the above request to Repeater tab in Burp suite and added a single quote on _DeviceId_ parameter. Modified requests look like `"DeviceId":"lol'"` ![SQL Injection Request](/images/posts/app_registration_sqli_req.png) And the response was like: ![SQL Injection Response](/images/posts/app_registration_sqli_resp.png) This confirms the existence of the vulnerability. To be assured I used the time delay command for few databases as `SLEEP(10)` `WAITFOR DELAY '0:0:10'` `SELECT pg_sleep(10)` and second one worked as shown below. ![SQL Injection Requets](/images/posts/app_registration_sqli_sleep.png)  
Then in the response time, we can see 10ms delays. It confirms MSSQL Injection. ![SQL Injection Response](/images/posts/app_registration_sqli_sleepres.png) To make proof of concept I decided to create a database object using the query `'CREATE TABLE kailash (line varchar(8000));--'`

![SQL Injection Response](/images/posts/app_registration_sqli_tblc.png)

After discussion with the development team, it was confirmed that the above query executed successfully.  
![SQL Injection Response](/images/posts/app_registration_sqli_tbl.jpg)

**_Note_** : _I used different devices during the assessment so you may find difference in parameter values in used screenshots._

* * *

#### Share on

  * [__Twitter](https://twitter.com/intent/tweet?text=MSSQL Injection In JSON Request https://corrupted-brain.github.io/blog/blog/2021/05/16/MSSQL-Injection-in-JSON-request/ "Share on Twitter")
  * [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://corrupted-brain.github.io/blog/blog/2021/05/16/MSSQL-Injection-in-JSON-request/ "Share on Facebook")
  * [__Google+](https://plus.google.com/share?url=https://corrupted-brain.github.io/blog/blog/2021/05/16/MSSQL-Injection-in-JSON-request/ "Share on Google Plus")
  * [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://corrupted-brain.github.io/blog/blog/2021/05/16/MSSQL-Injection-in-JSON-request/&title=MSSQL Injection In JSON Request&summary=MSSQL Injection in android application from JSON Request.&source=https://corrupted-brain.github.io/blog "Share on LinkedIn")

**MSSQL Injection In JSON Request** was published on May 16, 2021.

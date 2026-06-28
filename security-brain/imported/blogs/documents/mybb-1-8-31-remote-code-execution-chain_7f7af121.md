---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-25_mybb-1831-remote-code-execution-chain.md
original_filename: 2023-01-25_mybb-1831-remote-code-execution-chain.md
title: 'MyBB <= 1.8.31: Remote Code Execution Chain'
category: documents
detected_topics:
- xss
- command-injection
- sqli
tags:
- imported
- documents
- xss
- command-injection
- sqli
language: en
raw_sha256: 7f7af12122fd67609115db64324e61e314e0ed183323fb49786d0ee70504fe61
text_sha256: ed5ca500d2ce0b93174d414c7d8ab94fbffcc6be7db19ffc56afcc65c6a419c2
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# MyBB <= 1.8.31: Remote Code Execution Chain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-25_mybb-1831-remote-code-execution-chain.md
- Source Type: markdown
- Detected Topics: xss, command-injection, sqli
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `7f7af12122fd67609115db64324e61e314e0ed183323fb49786d0ee70504fe61`
- Text SHA256: `ed5ca500d2ce0b93174d414c7d8ab94fbffcc6be7db19ffc56afcc65c6a419c2`


## Content

---
title: "MyBB <= 1.8.31: Remote Code Execution Chain"
page_title: "MyBB <= 1.8.31: Remote Code Execution Chain – PT SWARM"
url: "https://swarm.ptsecurity.com/mybb-1-8-31-remote-code-execution-chain/"
final_url: "https://swarm.ptsecurity.com/mybb-1-8-31-remote-code-execution-chain/"
authors: ["Aleksey Solovev"]
programs: ["MyBB"]
bugs: ["RCE", "SQL injection", "Stored XSS"]
publication_date: "2023-01-25"
added_date: "2023-01-26"
source: "pentester.land/writeups.json"
original_index: 1626
---

# MyBB <= 1.8.31: Remote Code Execution Chain

Written by [Aleksey Solovev](https://swarm.ptsecurity.com/author/aleksey-solovev/ "Posts by Aleksey Solovev") on January 25, 2023

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/36b23bfb-image_2023-01-25_14-28-45.png)

## Author

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/07/c90212d7-123-150x150.png)

[Aleksey Solovev](https://swarm.ptsecurity.com/author/aleksey-solovev/ "Posts by Aleksey Solovev")

Web Application Security Expert 

MyBB is one seriously popular type of open-source forum software. However, even a popular tool can contain bugs or even bug chains that can lead to the compromise of an entire system. In this article, we’ll go over one such chain that we found.

## Visual editor persistent XSS

CVE-2022-43707 (HIGH RISK)

Some time ago, my colleague [Igor Sak-Sakovskiy](/author/igor-sak-sakovskiy/) published an article: [Fuzzing for XSS via nested parsers condition](https://swarm.ptsecurity.com/fuzzing-for-xss-via-nested-parsers-condition/). In it, he gives multiple examples of XSS attacks, one of which is in MyBB. The payload given by Igor has been fixed by the MyBB team in version [1.8.25](https://mybb.com/versions/1.8.25/). But I didn’t stop there — I went ahead and started fuzzing the fix!

Firstly, a registered user with low privileges edits his signature in the settings. The following payload is inserted into the editor in the “View Source” mode:
  
  
  [email][email= onpointerover=alert()//]text[/email]

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/3cdb17cf-1.png)Inserting the payload with xss into a user signature

After updating the signature, the link has a new `onpointerover` event handler with the value `alert();//`. When you hover over the rendered text with the mouse cursor, the embedded JavaScript code is executed.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/4a340968-2.png)Execution of the embedded javascript code in the user signature when hover over the mouse cursor

Therefore, if a user belonging to the “Moderator” or “Administrator” group enters the profile of the user who implemented the above payload in the signatures section, then, when that user hovers over the rendered text with the mouse cursor, the embedded JavaScript code will also be executed.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/9b1d8c3f-3.png)Execution of the embedded javascript code when editing the user signature by the administrator when hover over the mouse cursor

## ACP User SQL Injection

CVE-2022-43709 (MEDIUM RISK)

A user who is in the “Administrator” group has the ability to perform an SQL Injection when searching for users via Admin CP: `/admin/index.php?module=user-users&action=search`.

By default, custom fields are vulnerable to an SQL Injection: **_Location_** ,**_Bio_** , **_Gender_**

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/dff481e6-4.png)Custom fields when searching for users

To demonstrate the vulnerability, a search will be performed on the custom **Bio** field. To do this, a user needs to add text to the custom **Bio** field in order for the search to return at least one record.

Here the value **My biography** is added to the custom **Bio** field for the user who is in the “Administrator” group.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/025da56b-5.png)Filling in the custom Bio field

A request is made to search for users by the custom field Bio with the value My biography, which is intercepted using a proxy, for example, BurpSuite.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/4e272ac3-6.png)Search for users by the custom bio field

The user search query is intercepted by the custom Bio field.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/7488aff6-7.png)The user search request intercepted via proxy

A vulnerable place for an SQL Injection is the key of the `profile_fields` array.

`profile_fields[**fid2**]=My biography`

If you add a single quotation mark after `fid2`, the server returns the error “ _HTTP/1.1 503 Service Temporarily Unavailable_ “.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/388a0c50-8.png)Adding the single quotation mark to the key of the custom Bio field in the user search request intercepted through a proxy

The SQL Injection occurred due to the fact that the data transmitted from the user is not fully controlled/escaped. The root of the problem is the file `admin/modules/user/users.php`, namely how the value of the `$column` variable is handled. The value of this `$column`**** variable should either be framed with double quotes or checked for a valid value.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/00404639-9.png)Insufficient escaping of user data leading to a SQL Injection

Due to the lack of checking which values of the `$column` variable are allowed, it is possible to implement the SQL Injection with the condition that special characters will not be used, which will be escaped by the `$db->escape_string` method.

`' AND '.$db->escape_string($column)."`

A payload for the SQL Injection that delays query execution by 5 seconds:

`profile_fields[(**select pg_sleep(5))::text = $quote$$quote$ and fid2**]=My biography`

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/bc2e6459-10.png)The SQL Injection, which causes the execute SQL query to fall asleep for an additional 5 seconds

## Remote code execution via SQL injection

With the help of the SQL Injection found, it is possible to escalate the problem. This will happen if a Database Engine that supports multiple queries is selected when installing MyBB.

During installation, it is necessary to select, for example, PostgreSQL.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/2dbc4915-11.png)When installing the forum engine, the PostgreSQL is selected in the database configuration

When using the PostgreSQL database engine, the SQL Injection found will be executed via the native `pg_send_query` function in the file `inc/db_pgsql.php`.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/f3f7fc43-12.png)Calling the native function pg_send_query when using the Postgresql

According to the official PHP documentation, the [`pg_send_query`](https://www.php.net/manual/en/function.pg-send-query.php) function can execute multiple queries at a time.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/ff47f24b-13.png)The official documentation for the native pg_send_query function

Now let’s talk about how to create and edit templates in MyBB.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/42dc16ed-14.png)The functionality of template editing

The image above shows editing form of the template **member_profile_signature**.

When creating or editing a template, it is also possible to insert variable values, for example, `{$lang→users_signature}`, `{$memprofile['signature']}`.

The template is saved in the database in the `mybb_templates` table. In this case, the edited template **member_profile_signature** has `tid` = 240.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/cb4ca964-15.png)The user signature template stored in the database

In the file `member.php`, the template `member_profile_signature` is taken from the database in line 2158 and passed to the `eval` function.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/aaed1105-16.png)Executing code on the server using a user signature template

One might think that when creating/editing a template, the construction `";${system('id')}` may be injected in the eval function (line 2158 of member.php) and will represent a separate instruction that will also be executed.

However, this is not possible. Before saving the template in the database, the `check_template` function will be called in `admin/modules/style/templates.php` on line 536.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/88294ea7-17.png)When saving a template, the check_template function is called

The purpose of the `check_template` function is to check the template passed by the user for the presence of structures that allow arbitrary code to be executed in the system through the `eval` function.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/19f15229-18.png)The `check_template` function is a sandbox that protects against the introduction of dangerous constructions in the template

If the `check_template` function finds a dangerous construction when checking, it returns true and a saving error occurs.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/38d54274-19.png)The result of the `check_template` function is a security error

If you manage to somehow embed the construction `";${system('id')}` into the template, bypassing the check_template function, you will be able to execute arbitrary code on the server.

Now we go back to the SQL Injection found in MyBB, which uses PostgreSQL with the ability to conduct multi-queries. Using single or double quotes during SQL Injection will lead to their escaping:
  
  
  ' AND '.$db->escape_string($column)."

The SQL query that will rewrite the required construct to the **member_profile_signature** template without using single quotes:
  
  
  update mybb_templates set template = (select concat((select template from mybb_templates mt  where mt.tid = 240),(select CHR(34)||CHR(59)||CHR(36)||CHR(123)||CHR(115)||CHR(121)||CHR(115)||CHR(116)||CHR(101)||CHR(109)||CHR(40)||CHR(39)||CHR(105)||CHR(100)||CHR(39)||CHR(41)||CHR(125)))) where tid = 240;

Then, the final SQL Injection will have the form that will lead to the execution of arbitrary code in the system.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/2b37b736-20.png)Executing the SQL Injection in multi query mode, where the second query overwrites the user signature template and injects malicious code

The result will be the execution of the `system('id')` command.

![](https://swarm.ptsecurity.com/wp-content/uploads/2023/01/cabad446-21.png)The RCE on the server via SQL Injection bypassing the template sandbox function

**Vulnerability fixes can be found on the[official website of MyBB](https://mybb.com/versions/1.8.32/)**.

## To sum up

I’d like to thank the team at MyBB for fixing the vulnerabilities quickly. As for users, I recommend that they update their software as soon as possible.

[RCE](https://swarm.ptsecurity.com/tag/rce/), [Web Application Security](https://swarm.ptsecurity.com/tag/web-application-security/)

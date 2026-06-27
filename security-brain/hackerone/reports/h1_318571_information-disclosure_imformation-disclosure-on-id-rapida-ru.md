---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '318571'
original_report_id: '318571'
title: Imformation Disclosure on id.rapida.ru
weakness: Information Disclosure
team_handle: qiwi
created_at: '2018-02-22T14:33:34.824Z'
disclosed_at: '2018-06-11T09:18:58.446Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- information-disclosure
---

# Imformation Disclosure on id.rapida.ru

## Metadata

- HackerOne Report ID: 318571
- Weakness: Information Disclosure
- Program: qiwi
- Disclosed At: 2018-06-11T09:18:58.446Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет,
Происходит раскрытие путей на id.rapida.ru/dp.php
Шаги для воспроизведения:
1) Перейти на https://id.rapida.ru/login
2) Попробовать авторизоваться через телефон, ожидая смс-код.
3) Попробовать ввести не рабочий смс код(любой)
4) В респонсе можно увидеть пути
```
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 22 Feb 2018 14:29:05 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 1369
Connection: close
Vary: Accept-Encoding
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Methods: POST, OPTIONS
Access-Control-Allow-Credentials: true
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Security-Policy-Report-Only: default-src https:; script-src https: 'unsafe-eval' 'unsafe-inline'; style-src https: 'unsafe-inline'; img-src https: data:; font-src https: data:; report-uri /csp-report
Strict-Transport-Security: max-age=31536000;

{"status":"error","statusMessage":"\u041e\u0434\u043d\u043e\u0440\u0430\u0437\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c \u0432\u0432\u0435\u0434\u0435\u043d \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e. \u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d","data":[],"time":0,"errorCode":-14,"version":""}<br />
<b>Warning</b>:  file_put_contents(): Only 0 of 4780 bytes written, possibly out of free disk space in <b>/var/www/vhosts/id.rapida.ru/www/backend/Libs/Logger/OLogger.php</b> on line <b>68</b><br />
<br />
<b>Fatal error</b>:  Uncaught exception 'Libs\Errors\Exceptions\OBaseException' with message 'Unable to open log file.' in /var/www/vhosts/id.rapida.ru/www/backend/Libs/Logger/OLogger.php:70
Stack trace:
#0 /var/www/vhosts/id.rapida.ru/www/backend/Libs/Logger/ODeferredLogger.php(30): Libs\Logger\OLogger-&gt;WriteMessage('2018-02-22T17:2...')
#1 /var/www/vhosts/id.rapida.ru/www/backend/Libs/Logger/OLog.php(37): Libs\Logger\ODeferredLogger-&gt;flush()
#2 /var/www/vhosts/id.rapida.ru/www/backend/Libs/Errors/OHandler.php(66): Libs\Logger\OLog::Flush()
#3 [internal function]: Libs\Errors\OHandler-&gt;HandleFatalError()
#4 {main}
  thrown in <b>/var/www/vhosts/id.rapida.ru/www/backend/Libs/Logger/OLogger.php</b> on line <b>70</b><br />
```

## Impact

Дальнейшая эксплуатация для заливки шела через всякие sql инъекции и.т.д

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

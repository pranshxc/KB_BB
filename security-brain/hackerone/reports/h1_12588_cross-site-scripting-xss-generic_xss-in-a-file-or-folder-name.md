---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12588'
original_report_id: '12588'
title: XSS in a file or folder name
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-05-20T05:26:35.769Z'
disclosed_at: '2014-07-09T09:24:50.764Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in a file or folder name

## Metadata

- HackerOne Report ID: 12588
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-07-09T09:24:50.764Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Шаги:
- создаем в https://cloud.mail.ru/ папку с именем %22%3e%3cimg src=x onerror=alert(1)%3e
- переходим на страницу https://e.mail.ru/compose
- жмем прикрепить файлы из облака

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

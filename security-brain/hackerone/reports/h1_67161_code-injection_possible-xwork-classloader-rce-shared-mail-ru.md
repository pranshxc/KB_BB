---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '67161'
original_report_id: '67161'
title: 'Possible xWork classLoader RCE: shared.mail.ru'
weakness: Code Injection
team_handle: mailru
created_at: '2015-06-10T09:27:21.118Z'
disclosed_at: '2015-09-13T13:03:37.088Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- code-injection
---

# Possible xWork classLoader RCE: shared.mail.ru

## Metadata

- HackerOne Report ID: 67161
- Weakness: Code Injection
- Program: mailru
- Disclosed At: 2015-09-13T13:03:37.088Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Ее похоже аффектит https://confluence.atlassian.com/display/DOC/Confluence+Security+Advisory+2014-05-21
classLoader пролетает, то есть фикса на уровне регулярок нет
версия в уязвимом скоупе
Я конечно попробую в выходные реально код исполнить, но по внешним признакам оно там есть
Все версии меньше 5.5.2 имеют схожий баг в xwork как было с struts

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

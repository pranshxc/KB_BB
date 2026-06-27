---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '86069'
original_report_id: '86069'
title: xss на нескольких форумах игр от mail.ru (Cross-Site Scripting)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-09-01T07:26:32.872Z'
disclosed_at: '2017-05-25T10:22:29.022Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss на нескольких форумах игр от mail.ru (Cross-Site Scripting)

## Metadata

- HackerOne Report ID: 86069
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2017-05-25T10:22:29.022Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

На форумах таких игр как https://wf.mail.ru/forums, https://pw.mail.ru/forums/  и им подобным использующим такой же форум, есть уязвимость Xss. Что бы java script сработал, следует перейти в сообщения, написать в поле заэнкоденный вариант кода " %3Cscript%3Ealert()%3C/script%3E " и он сработает при нажатии на элемент "переключение редактора в визуальный режим".

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12804'
original_report_id: '12804'
title: Reflected  XSS in User-Agent
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-05-22T12:47:20.894Z'
disclosed_at: '2014-09-16T05:07:44.306Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected  XSS in User-Agent

## Metadata

- HackerOne Report ID: 12804
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2014-09-16T05:07:44.306Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Уязвимость существует на сайтах:
11x11.mail.ru
s2.11x11.mail.ru

Злоумышленник может внедрить произвольный User-Agent, содержащий JS код.
Для примера - ><script>alert(/BigBear/)</script><!--

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

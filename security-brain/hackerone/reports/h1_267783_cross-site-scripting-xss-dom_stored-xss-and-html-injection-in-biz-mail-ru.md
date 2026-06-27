---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '267783'
original_report_id: '267783'
title: Stored XSS and html injection in biz.mail.ru
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mailru
created_at: '2017-09-12T15:45:16.466Z'
disclosed_at: '2017-12-27T14:26:26.949Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: biz.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Stored XSS and html injection in biz.mail.ru

## Metadata

- HackerOne Report ID: 267783
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mailru
- Disclosed At: 2017-12-27T14:26:26.949Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application: biz.mail.ru

Testing environment: Latest chrome

Steps to reproduce

1) go to biz.mail.ru, login
2) go to "My company"
3) create a department named as "></div></form></script><script>alert()</script><iframe src="www.google.com" onload="alert()">
4) add an employee in that department
5) create a new subdepartment
6) add the employee from step 4 in our subdepartment

Actual results: 

Payload says for itself

PoC, exploit code, screenshots, video, references, additional resources:

In attachments .gif

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

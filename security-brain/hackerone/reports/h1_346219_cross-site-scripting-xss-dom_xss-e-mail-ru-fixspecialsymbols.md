---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '346219'
original_report_id: '346219'
title: XSS e.mail.ru fixSpecialSymbols
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mailru
created_at: '2018-05-01T20:04:36.812Z'
disclosed_at: '2018-08-15T16:21:21.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: e.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS e.mail.ru fixSpecialSymbols

## Metadata

- HackerOne Report ID: 346219
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mailru
- Disclosed At: 2018-08-15T16:21:21.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
e.mail.ru

Testing environment
--
Firefox

Steps to reproduce
--
1. send email from `</textarea><img src onerror=alert(1)>`
2. add sender to contacts on https://e.mail.ru/messages/inbox/
3. using Firefox go to https://e.mail.ru/compose/
4. click on `Кому:` to open Contacts

Actual results
--
alert message

Expected results, security impact description and recommendations
--
fixSpecialSymbols uses `textarea` to decode HTML entities, it's unsafe in Firefox
`require('mrg-explorer/utils/utils').fixSpecialSymbols('</textarea><img src onerror=alert(1)>')`

PoC, exploit code, screenshots, video, references, additional resources
--
Screencast: https://yadi.sk/i/Z9wrUqll3V7iPg

{F292555}

## Impact

XSS

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

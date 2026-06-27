---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '62385'
original_report_id: '62385'
title: Pretty Photo Dom XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: jsdelivr
created_at: '2015-05-14T10:10:31.941Z'
disclosed_at: '2015-05-20T13:59:13.460Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Pretty Photo Dom XSS

## Metadata

- HackerOne Report ID: 62385
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: jsdelivr
- Disclosed At: 2015-05-20T13:59:13.460Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Team,

Javascript for http://www.jsdelivr.com/#!prettyphoto hosted on the website points to 3.1.5 which is vulnerable to DOMXSS the upstream released an update 3.1.6 7 days back still the CDN is serving vulnerable edition effectively making all the websites vulnerable to DoMXSS

Details about the issue are outlined : http://blog.anantshri.info/forgotten_disclosure_dom_xss_prettyphoto

github issue for the stuff : https://github.com/scaron/prettyphoto/issues/149

Hope this helps.

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

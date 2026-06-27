---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50481'
original_report_id: '50481'
title: Self Xss on File Replace
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2015-03-07T15:10:05.149Z'
disclosed_at: '2015-07-08T18:38:48.126Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self Xss on File Replace

## Metadata

- HackerOne Report ID: 50481
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2015-07-08T18:38:48.126Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In File manager there is an Replace option to replace files from three resources .
1. from computer
2.incoming
3.Remote files
For remote files if we put 
http://example.com/"><img src=x onerror=confirm('name')>

in the url box
It reflects xss.
Poc: https://www.dropbox.com/s/m7pb9wiwxix1oyu/replacexss.mkv?dl=0

Thanks

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

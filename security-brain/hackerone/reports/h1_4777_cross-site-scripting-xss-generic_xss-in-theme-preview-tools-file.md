---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4777'
original_report_id: '4777'
title: XSS in Theme Preview Tools File
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2014-03-25T19:02:57.824Z'
disclosed_at: '2014-08-28T18:37:39.292Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Theme Preview Tools File

## Metadata

- HackerOne Report ID: 4777
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2014-08-28T18:37:39.292Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/concrete5/concrete5/blob/master/web/concrete/tools/themes/preview.php#L7

Note that one of those values near the end is not escaped.

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

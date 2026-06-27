---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6412'
original_report_id: '6412'
title: Persistent class XSS [the fuck]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: khanacademy
created_at: '2014-04-08T06:28:32.580Z'
disclosed_at: '2014-04-09T17:06:03.140Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Persistent class XSS [the fuck]

## Metadata

- HackerOne Report ID: 6412
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: khanacademy
- Disclosed At: 2014-04-09T17:06:03.140Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I created a class called : `</script>"><img src=x onerror=alert(0)>` and it actually worked 0.0.

It worked here for me : https://www.khanacademy.org/coach/reports/grid?force=1

Best regards,

Olivier Beg

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

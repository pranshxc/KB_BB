---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '32519'
original_report_id: '32519'
title: XSS in fabric.io
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-10-22T20:05:46.941Z'
disclosed_at: '2014-12-23T15:56:03.855Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in fabric.io

## Metadata

- HackerOne Report ID: 32519
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2014-12-23T15:56:03.855Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Proof: http://i.imgur.com/Hk84G3Y.png

Vulnerable Page: https://fabric.io/onboard/invite
Put this code: "><img src=x onerror=alert(document.domain)>
and email
then send invitation

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

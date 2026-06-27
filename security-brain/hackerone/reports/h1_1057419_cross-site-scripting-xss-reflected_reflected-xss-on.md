---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1057419'
original_report_id: '1057419'
title: Reflected XSS on ███
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-12-12T13:25:37.207Z'
disclosed_at: '2021-04-02T18:41:19.562Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on ███

## Metadata

- HackerOne Report ID: 1057419
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-04-02T18:41:19.562Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary 
Reflected XSS on `█████████` for invalid paths.

## Description
Requesting a non-existent path on `█████`, such as `https://██████████/chron0x` the site responds with `No jsonpage404 is /chron0x versus /chron0x./chron0x does not exist`. As it can be seen, the path is reflected. This can be exploited with an XSS. 

Note: I am reporting this here, since the foorter of `███` states `Official ███ Website. The ████████ is an Equal Opportunity Employer.`, and the █████ underlies the DoD. If this should not belong to the DoD scope I would kindly ask to self close this issue.

## Step-by-step Reproduction Instructions

1. Visit `http://█████████/<svg onload=alert("chron0x")>`


## Mitigation/Remediation Actions
Sanitize the path input or switch to a generic error message.

## Impact

Javascript can be executed to steal data, etc.

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

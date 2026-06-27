---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '867436'
original_report_id: '867436'
title: misconfigured CORS let to HPP and SOP bypass
weakness: Misconfiguration
team_handle: btfs
created_at: '2020-05-06T21:37:56.670Z'
disclosed_at: '2020-05-07T21:57:21.720Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- misconfiguration
---

# misconfigured CORS let to HPP and SOP bypass

## Metadata

- HackerOne Report ID: 867436
- Weakness: Misconfiguration
- Program: btfs
- Disclosed At: 2020-05-07T21:57:21.720Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello team,
I found a bug on your website that let me bypass the SOP policy.
Hope you fix it, everything is in the video


https://www.youtube.com/watch?v=PYsU350S-s4

## Impact

The attacker my direct a victim to a phishing page of www.bitterrent.com/login and he/she will be convince to enter their email and password or even hijack csrf-token and sending him a password or email reset link.
I also found a link that expose the csrf-token on the URL and you should check this link in the black.svg host header URL

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

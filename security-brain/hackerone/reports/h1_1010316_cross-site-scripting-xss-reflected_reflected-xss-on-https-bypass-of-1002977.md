---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1010316'
original_report_id: '1010316'
title: 'Reflected XSS on https://████/ (Bypass of #1002977)'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-10-16T19:19:23.539Z'
disclosed_at: '2020-11-23T18:10:40.105Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://████/ (Bypass of #1002977)

## Metadata

- HackerOne Report ID: 1010316
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-11-23T18:10:40.105Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Hello DoD team,

Third time a charm :-)

I really cannot explain what is going on with this ██████████ website,

You just locked the report so i can't comment there, but it seems it works right now and i have proof of a video with time stamp.

I am talking about #1002977, i hope you will see this fast enough when it still works.

███████

##Summary:
Reflected Cross site Scripting (XSS) on https://██████████████████

##Steps To Reproduce:
1. Navigate to https://████████████
2. Alert will pop :-)

█████████

##Recommendations for fix
Content based escaping on the users input, in this case on the url parameter.

##Best Regards,
nagli

## Impact

Attacker can execute JS code on the Victim Behalf.

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

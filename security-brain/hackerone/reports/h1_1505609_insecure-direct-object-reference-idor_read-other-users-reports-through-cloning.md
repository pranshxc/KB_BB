---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1505609'
original_report_id: '1505609'
title: Read Other Users Reports Through Cloning
weakness: Insecure Direct Object Reference (IDOR)
team_handle: gsa_vdp
created_at: '2022-03-09T20:31:34.998Z'
disclosed_at: '2022-05-26T12:41:28.682Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: demo.sftool.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Read Other Users Reports Through Cloning

## Metadata

- HackerOne Report ID: 1505609
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: gsa_vdp
- Disclosed At: 2022-05-26T12:41:28.682Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I team, I have found a vulnerability where I am able to read other users reports through the clone report function.
If an attacker goes to try read another users report, we get a 500 internal error response.
But if an attacker uses the clone report function, we are able to clone a victims report and read it on our attacker account

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Victim account has a scorecard created under https://demo.sftool.gov/tws/
  2. Attacker goes to https://demo.sftool.gov/tws/ and selects clone scorecard
 3. Attacker enters name of score card (any name)
4. Attacker clicks choose score card (have to have an existing scorecard on attacker account prior) and selects scorecard
5 Attacker turns on interceptor and changes name of scorecard to that of victim scorecard under the parameter nTwsUserScorecard.Template=    (use value testnew to see my scorecard)
6 attacker submits request

you have now cloned my scorecard into your own scorecard and can read my details (see poc attached)

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

If an attacker goes to try read another users report, we get a 500 internal error response.
But if an attacker uses the clone report function, we are able to clone a victims report and read it on our attacker account reading sensitive report data of another user

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

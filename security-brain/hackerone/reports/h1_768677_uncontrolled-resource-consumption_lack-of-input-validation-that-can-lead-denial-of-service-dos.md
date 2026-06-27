---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '768677'
original_report_id: '768677'
title: lack of input validation that can lead Denial of Service (DOS)
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2020-01-06T08:16:22.451Z'
disclosed_at: '2020-03-12T20:16:11.542Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# lack of input validation that can lead Denial of Service (DOS)

## Metadata

- HackerOne Report ID: 768677
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2020-03-12T20:16:11.542Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team,

## Summary:
There is no limit to the number of characters in the issue comments, which allows a DoS attack. The DoS attack affects server-side.

## Description

On the input form of Username in `https://twitter.com/settings/screen_name` there's no Input validation using this you can send more payload and may cause of Denial of service or error code 500 Internal Server Error/Internal Error

## Proof of Concept

1. First login your twitter account 
2. Go to the Settings of your account 
3. Click Username
4. Change your username and put the payload then submit

And the response was pop up and say.
==Something went wrong, but don't fret --- it's not your fault.==
and the response code on the server side is `500 Internal Server Error`

Kindly check 2 uploaded photo for my additional Proof of Concept

### Remediation:

    Implementing input validation
    Validating free-form Unicode text
    Define the allowed set of characters to be accepted.
    Minimum and maximum value range


Supporting Material/References:

    payload.txt

Thank you!
Regards

## Impact

Attacker can perform a DOS because of lack of input validation

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

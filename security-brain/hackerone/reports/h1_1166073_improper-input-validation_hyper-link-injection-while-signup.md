---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166073'
original_report_id: '1166073'
title: Hyper Link Injection while signup
weakness: Improper Input Validation
team_handle: upchieve
created_at: '2021-04-15T22:42:45.099Z'
disclosed_at: '2022-06-15T10:04:14.051Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: app.upchieve.org
asset_type: URL
max_severity: none
tags:
- hackerone
- improper-input-validation
---

# Hyper Link Injection while signup

## Metadata

- HackerOne Report ID: 1166073
- Weakness: Improper Input Validation
- Program: upchieve
- Disclosed At: 2022-06-15T10:04:14.051Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Attacker can add their name to a URL in order to send email  containing malicious hyperlinks. while signup  

## Steps To Reproduce:
1-Go to https://app.upchieve.org and create account  with the first name ```http://attacker.com/ ``` and last name .
2-Now check  your email  and you notice there is malicious hyperlinks.
█████████

## Supporting Material/References:

█████

## Recommendations for Fixing/Mitigation
 Validate users input

## Impact

This permits users to send malicious/phishing links to potential clients. It could also have an effect on how spam filters treat ```app.upchieve.org``` emails.

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

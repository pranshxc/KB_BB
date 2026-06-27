---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2270082'
original_report_id: '2270082'
title: Mailgun subdomain takeover
team_handle: deriv
created_at: '2023-12-02T17:39:15.153Z'
disclosed_at: '2024-05-02T06:22:31.569Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: '*.deriv.cloud'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Mailgun subdomain takeover

## Metadata

- HackerOne Report ID: 2270082
- Weakness: 
- Program: deriv
- Disclosed At: 2024-05-02T06:22:31.569Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I have found an unclaimed subdomain of deriv.cloud. Which is successfully claimable.
## Platform(s) Affected:
email.mailgun.deriv.cloud

## Steps To Reproduce:
You just need a mailgun account and the you can successfully claim this domain.

## Supporting Material/References:

https://hackerone.com/reports/819309

## Impact

## Summary:
This subdomain takeover is very similar to other subdomain takeovers with just a few key differences:
1. This will allow any user to use a free mail system. This can be very effective while phishing.
2. Can reveal some very sensitive internal information about the Company which can lead to reputation and financial damage.

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

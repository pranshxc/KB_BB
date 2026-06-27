---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1023773'
original_report_id: '1023773'
title: password field autocomplete enabled
weakness: Insecure Storage of Sensitive Information
team_handle: yelp
created_at: '2020-11-01T08:47:23.880Z'
disclosed_at: '2022-09-27T23:26:28.449Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: '*.yelp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# password field autocomplete enabled

## Metadata

- HackerOne Report ID: 1023773
- Weakness: Insecure Storage of Sensitive Information
- Program: yelp
- Disclosed At: 2022-09-27T23:26:28.449Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
[Most browsers have a facility to remember user credentials that are entered into HTML forms. This function can be configured by the user and also by applications that employ user credentials. If the function is enabled, then credentials entered by the user are stored on their local computer and retrieved by the browser on future visits to the same application.
The stored credentials can be captured by an attacker who gains control over the user's computer. Further, an attacker who finds a separate application vulnerability such as cross-site scripting may be able to exploit this to retrieve a user's browser-stored credentials.]

## Platform(s) Affected:
[both]

## Steps To Reproduce:
[follow the steps]

  1. [signup with the new details]
  1. [go to login page]
  1. [there we will see password details are automatically filled]

## Supporting Material/References:
[none]

## Impact

This autocomplete password can be sniffed without user permission

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

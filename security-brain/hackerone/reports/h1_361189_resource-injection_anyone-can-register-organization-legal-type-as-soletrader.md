---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361189'
original_report_id: '361189'
title: Anyone can register organization legal type as "Soletrader"
weakness: Resource Injection
team_handle: liberapay
created_at: '2018-06-02T21:16:53.384Z'
disclosed_at: '2018-06-03T16:31:39.705Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- resource-injection
---

# Anyone can register organization legal type as "Soletrader"

## Metadata

- HackerOne Report ID: 361189
- Weakness: Resource Injection
- Program: liberapay
- Disclosed At: 2018-06-03T16:31:39.705Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When Organization type is registered, two values are displayed : Business and Organization. 
When another value is provided, an error message is printed saying the Legal Type is wrong. 

This error message is not printed and request success when the value "Soletrader"  is provided.
The value "Soletrader" is part of the MangoPay API Documentation ( <https://docs.mangopay.com/guide/kyc>).

A malicious attacker can register its organization with this Legal Type which seems to be not planned by the librapay.com platform.

**Steps to reproduce**
1. Go to <https://en.liberapay.com/~107759/identity>
2. Check the box "Yes, I represent a business or nonprofit."
3. Inspect element with your browser on the "Organization type" input, and change <option value="BUSINESS">Entreprise</option> with <option value="Soletrader">Entreprise</option>.
4. Select "Enterprise" on the Organization type" input
5. Click on the "Save button".
6. The request is accepted by the platform and the success message "Your identity information has been updated." is printed.

You can try to do the same providing another value than "Soletrader" and you will check that an error is printed.

## Impact

A malicious attacker can register its organization with this Legal Type which seems to be not planned by the librapay.com platform. He could use this to have not planned  or unauthorized features when calling Mangopay API.

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

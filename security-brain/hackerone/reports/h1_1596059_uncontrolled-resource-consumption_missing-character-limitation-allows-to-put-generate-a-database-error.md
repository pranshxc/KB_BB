---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1596059'
original_report_id: '1596059'
title: Missing character limitation allows to put generate a database error
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2022-06-09T16:44:23.306Z'
disclosed_at: '2023-01-09T07:11:26.267Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Missing character limitation allows to put generate a database error

## Metadata

- HackerOne Report ID: 1596059
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2023-01-09T07:11:26.267Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team,
Summary:
=========
There is no limit to the number of characters in the display name, which allows a DoS attack. The DoS attack affects server-side.
Description
=========
On the input form of Username in nextcloud.com/settings/user there's no Input validation using this you can send more payload and may cause of Denial of service or error code 500 Internal Server Error/Internal Error
Proof of Concept
==============
1.Go and login to your account
2. Now go to setting and Deck ---> Add Boards section
3.Insert name and intercept it
4. Send to repeater replace it with payload the response code on the server side is 500 Internal Server Error

## Impact

Impact
=======
Remediation:
===========
+Implementing input validation
+Validating free-form Unicode text
+Define the allowed set of characters to be accepted.
+Minimum and maximum value range
Impact
======
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

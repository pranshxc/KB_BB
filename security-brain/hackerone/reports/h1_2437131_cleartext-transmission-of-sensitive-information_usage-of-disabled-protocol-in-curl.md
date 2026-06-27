---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2437131'
original_report_id: '2437131'
title: Usage of disabled protocol in curl
weakness: Cleartext Transmission of Sensitive Information
team_handle: ibb
created_at: '2024-03-27T18:16:37.043Z'
disclosed_at: '2024-03-29T18:31:08.016Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Usage of disabled protocol in curl

## Metadata

- HackerOne Report ID: 2437131
- Weakness: Cleartext Transmission of Sensitive Information
- Program: ibb
- Disclosed At: 2024-03-29T18:31:08.016Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a protocol selection parameter option disables all protocols without adding any then the default set of protocols would remain in the allowed set due to an error in the logic for removing protocols. The below command would perform a request to curl.se with a plaintext protocol which has been explicitly disabled.

curl --proto -all,-http http://curl.se

The flaw is only present if the set of selected protocols disables the entire set of available protocols, in itself a command with no practical use and therefore unlikely to be encountered in real situations. The curl security team has thus assessed this to be low severity bug.

## Impact

Requests can be sent on an unencrypted link even though the application explicitly disabled that.

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

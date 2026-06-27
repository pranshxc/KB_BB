---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1234531'
original_report_id: '1234531'
title: private keys exposed on the GitHub repository
weakness: Cleartext Storage of Sensitive Information
team_handle: mcuboot
created_at: '2021-06-15T12:14:30.294Z'
disclosed_at: '2021-11-27T07:06:03.422Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 24
asset_identifier: https://github.com/mcu-tools/mcuboot
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# private keys exposed on the GitHub repository

## Metadata

- HackerOne Report ID: 1234531
- Weakness: Cleartext Storage of Sensitive Information
- Program: mcuboot
- Disclosed At: 2021-11-27T07:06:03.422Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
When I searched Github for sensitive information I found some privet key in GitHub repository.
these are private RSA key and private server key, which could be used for unauthorized access.

## Steps To Reproduce:
VISIT THESE LINKS:
Repository : 
EX:
https://github.com/mcu-tools/mcuboot/blob/137d79717764ed32d5da4b4b301f32f81b2bf40f/enc-x25519-priv.pem
https://github.com/mcu-tools/mcuboot/blob/137d79717764ed32d5da4b4b301f32f81b2bf40f/root-ed25519.pem
(This is just an example)
This is the link that contains it all privet key  :-
https://github.com/mcu-tools/mcuboot/search?p=1&q=extension%3Apem+private 

## Supporting Material/References:

https://hackerone.com/reports/50170
https://hackerone.com/reports/638401

## Impact

1).Private key leakage
2). All of the servers using this key will be compromised

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

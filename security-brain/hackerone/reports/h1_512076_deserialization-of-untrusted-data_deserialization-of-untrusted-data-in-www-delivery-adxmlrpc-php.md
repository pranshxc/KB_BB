---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '512076'
original_report_id: '512076'
title: Deserialization of Untrusted Data in www/delivery/adxmlrpc.php
weakness: Deserialization of Untrusted Data
team_handle: revive_adserver
created_at: '2019-03-19T14:41:33.473Z'
disclosed_at: '2019-04-23T13:08:01.674Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- deserialization-of-untrusted-data
---

# Deserialization of Untrusted Data in www/delivery/adxmlrpc.php

## Metadata

- HackerOne Report ID: 512076
- Weakness: Deserialization of Untrusted Data
- Program: revive_adserver
- Disclosed At: 2019-04-23T13:08:01.674Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An attacker could send a specifically crafted payload to the XML-RPC invocation script and trigger the unserialize() call on the "what" parameter in the "openads.spc" RPC method.

## Impact

Such vulnerability could be used to perform various types of attacks, e.g. exploit serialize-related PHP vulnerabilities or PHP object injection.

It is possible, although unconfirmed, that the vulnerability has been used by some attackers in order to gain access to some Revive Adserver instances and deliver malware through them to third party websites.

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

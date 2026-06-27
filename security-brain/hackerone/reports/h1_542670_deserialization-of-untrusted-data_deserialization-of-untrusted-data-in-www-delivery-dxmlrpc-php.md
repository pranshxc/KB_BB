---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '542670'
original_report_id: '542670'
title: Deserialization of Untrusted Data in www/delivery/dxmlrpc.php
weakness: Deserialization of Untrusted Data
team_handle: revive_adserver
created_at: '2019-04-19T14:38:45.548Z'
disclosed_at: '2019-04-23T13:06:06.123Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- deserialization-of-untrusted-data
---

# Deserialization of Untrusted Data in www/delivery/dxmlrpc.php

## Metadata

- HackerOne Report ID: 542670
- Weakness: Deserialization of Untrusted Data
- Program: revive_adserver
- Disclosed At: 2019-04-23T13:06:06.123Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An attacker could send a specifically crafted payload to the XML-RPC invocation script and trigger the unserialize() call on the first parameter in the "pluginExecute" RPC method.

## Impact

Such vulnerability could be used to perform various types of attacks, e.g. exploit serialize-related PHP vulnerabilities or PHP object injection.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1635321'
original_report_id: '1635321'
title: 'Fix : (Security) Mitigate Path Traversal Bug'
weakness: Path Traversal
team_handle: hyperledger
created_at: '2022-07-13T06:20:36.223Z'
disclosed_at: '2022-08-05T21:41:29.606Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https://github.com/hyperledger/fabric-chaincode-java
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# Fix : (Security) Mitigate Path Traversal Bug

## Metadata

- HackerOne Report ID: 1635321
- Weakness: Path Traversal
- Program: hyperledger
- Disclosed At: 2022-08-05T21:41:29.606Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Unsanitized input from arg[0] argument flows into java.io.FileOutputStream, where it is used as a path. This may result in a Path Traversal vulnerability and allow an attacker to write to arbitrary files.

## Impact

Being able to access and manipulate an arbitrary path leads to vulnerabilities when a program is being run with privileges that the user providing the path should not have. A website with a path traversal vulnerability would allow users access to sensitive files on the server hosting it. CLI programs may also be vulnerable to path traversal if they are being ran with elevated privileges (such as with the setuid or setgid flags in Unix systems)

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

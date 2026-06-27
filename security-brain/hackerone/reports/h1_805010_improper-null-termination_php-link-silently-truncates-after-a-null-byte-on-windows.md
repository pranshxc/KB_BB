---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '805010'
original_report_id: '805010'
title: PHP link() silently truncates after a null byte on Windows
weakness: Improper Null Termination
team_handle: ibb
created_at: '2020-02-26T05:04:15.342Z'
disclosed_at: '2020-11-09T01:49:11.631Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- improper-null-termination
---

# PHP link() silently truncates after a null byte on Windows

## Metadata

- HackerOne Report ID: 805010
- Weakness: Improper Null Termination
- Program: ibb
- Disclosed At: 2020-11-09T01:49:11.631Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The bug submitted at: https://bugs.php.net/bug.php?id=78862
The security advisory at: https://nvd.nist.gov/vuln/detail/CVE-2019-11044

The issue allow remote attackers to read or write arbitrary files via crafted input to an application that calls the vulnerable function. As demonstrated by a file\0.ext attack that bypasses an intended configuration in which users may read or write only files.

## Impact

In PHP versions 7.2.x below 7.2.26, 7.3.x below 7.3.13 and 7.4.0 on Windows, PHP link() function accepts filenames with embedded \0 byte and treats them as terminating at that byte. This could lead to security vulnerabilities, e.g. in applications checking paths that the code is allowed to access.

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

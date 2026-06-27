---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '797159'
original_report_id: '797159'
title: PHP builded for Windows with TS support does not resolve relalative paths with
  drive letter correctly
weakness: Path Traversal
team_handle: ibb
created_at: '2020-02-15T11:05:39.461Z'
disclosed_at: '2020-11-09T01:47:33.238Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 0
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- path-traversal
---

# PHP builded for Windows with TS support does not resolve relalative paths with drive letter correctly

## Metadata

- HackerOne Report ID: 797159
- Weakness: Path Traversal
- Program: ibb
- Disclosed At: 2020-11-09T01:47:33.238Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Currently PHP process Windows paths like `C:Users` as if they were absolute. But they are not and PHP builded with TS (thread-safe support) currently points to root drive location instead of the current directory. This gives the attaker unlimited access to the root drive if a) the path is resolved/normalized by the app before used b) permissions are denied (but on Windows the system files are almost always accessible)

Reported to PHP:
https://bugs.php.net/bug.php?id=78939
https://github.com/php/php-src/pull/5001

## Impact

Attaker can get access to all files on the same drive if the path is validated by some middleware correctly but PHP then points to bad location.

Example scenario:
- PHP pwd: `C:/Web/uploads`
- path: `C:secret_data.txt`
- apps checks if the path is within pwd - yes, it is, correct resolved location should be `C:/Web/uploads/secret_data.txt`
- but PHP accesses `C:/secret_data.txt`

If app can write with user supplied path, the path can be handcrafted to point to location like `C:\Users\<USER>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` and inject malicious file to be started when the user logs in.

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

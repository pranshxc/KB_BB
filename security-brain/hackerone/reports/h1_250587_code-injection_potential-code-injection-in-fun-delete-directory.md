---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '250587'
original_report_id: '250587'
title: Potential code injection in fun delete_directory
weakness: Code Injection
team_handle: expressionengine
created_at: '2017-07-17T17:33:10.329Z'
disclosed_at: '2017-09-07T14:56:56.831Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- code-injection
---

# Potential code injection in fun delete_directory

## Metadata

- HackerOne Report ID: 250587
- Weakness: Code Injection
- Program: expressionengine
- Disclosed At: 2017-09-07T14:56:56.831Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Under /system/ee/legacy/libraries/Functions.php, function delete_directory contains calls to `exec` 3 times using different, potentially "unsanitized" paramateres. As the PHP manual suggest, `escapeshellarg` should be used to sanitize individual arguments [1]. 

On an implementation in which the attacker controls the file name, arbitrary code execution is achieved. Better to fix it.

[1] http://php.net/manual/en/function.escapeshellarg.php

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1374318'
original_report_id: '1374318'
title: Arbitrary file injection via symlink attack in rdoc generator
weakness: Resource Injection
team_handle: ruby
created_at: '2021-10-19T11:51:48.050Z'
disclosed_at: '2023-07-18T08:43:02.493Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- resource-injection
---

# Arbitrary file injection via symlink attack in rdoc generator

## Metadata

- HackerOne Report ID: 1374318
- Weakness: Resource Injection
- Program: ruby
- Disclosed At: 2023-07-18T08:43:02.493Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

There is a vulnerability that can allow an attacker to spoof the symbolic link and traverse the file system to unintended locations or access arbitrary files. The symbolic link can permit an attacker to read  a file that they originally did not have permissions to access and to inject its content to the placed-on-the-web documentation.

# PoC

1.
```sh
$ mkdir test
$ cd test
$ ln -s /etc/passwd test
$ rdoc
```
2.
See `doc/test.html` and `doc/js/search_index.js`, they contain the data of `/etc/passwd`.

The spoofed link can refer to files in `~/.ssh`, `~/.gnupg`, `/etc`, `/proc`/, `/sys`, thus, the nature of the disclosed data varies from secrets/credentials to system configurations, hardware info, firewall rules,  and so on.

## Impact

An attacker could gain access to sensitive data or system resources. This could allow access to protected files or directories including configuration files and files containing sensitive information.

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

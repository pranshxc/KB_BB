---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5499'
original_report_id: '5499'
title: Arbitrary command execution in MS-DOS
weakness: Command Injection - Generic
team_handle: msdos
created_at: '2014-04-01T16:35:09.167Z'
disclosed_at: '2014-04-01T17:54:57.371Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- command-injection-generic
---

# Arbitrary command execution in MS-DOS

## Metadata

- HackerOne Report ID: 5499
- Weakness: Command Injection - Generic
- Program: msdos
- Disclosed At: 2014-04-01T17:54:57.371Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Versions 1.1 and 2.0 of MS-DOS allow a malicious actor to execute arbitrary system commands via the main application interface.

Prerequisites:
* MS-DOS 1.1 or MS-DOS 2.0 installation
* Input device (e.g. keyboard)

Steps to reproduce:
* Enter the _command mode_
* Type `VER` to make sure that the system is on of the affected versions
* Pass a known system command like `HELP` to see that the system responds correctly
* Use `EXEC PROGRAM_NAME.BAT` to execute arbitrary programs

See PoC below.

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

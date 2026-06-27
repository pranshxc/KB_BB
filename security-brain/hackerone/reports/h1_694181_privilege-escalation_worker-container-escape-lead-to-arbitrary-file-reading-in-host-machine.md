---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '694181'
original_report_id: '694181'
title: Worker container escape lead to arbitrary file reading in host machine
weakness: Privilege Escalation
team_handle: semmle
created_at: '2019-09-13T02:39:39.780Z'
disclosed_at: '2019-10-16T12:34:13.387Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 110
asset_identifier: lgtm-com.pentesting.semmle.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Worker container escape lead to arbitrary file reading in host machine

## Metadata

- HackerOne Report ID: 694181
- Weakness: Privilege Escalation
- Program: semmle
- Disclosed At: 2019-10-16T12:34:13.387Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Because lack of security, attacker will be able to remove original log file and replace it will a symlink to other file, 
After finishing job, host machine copy file from docker container.
Because the original log file has been removed, the host machine will copy the symlink file.
But the problem is it doesn't copy the linked file in container, it copys the linked file in the HOST MACHINE.

## Steps To Reproduce:
The attack is very simple, just remove the original build.log file and replace with a symlink file,
I used this configuration to read the ``/etc/passwd``:
```extraction:
  cpp:
    after_prepare:
      - rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

## PoC
Content of ``/etc/passwd`` is attached below

## Impact

Give attacker ability to explore the host machine, expose more sensitive informations from it.

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

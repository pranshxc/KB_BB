---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '415272'
original_report_id: '415272'
title: Linux Desktop application slack executable does not use pie / no ASLR
weakness: Violation of Secure Design Principles
team_handle: slack
created_at: '2018-09-27T12:33:08.436Z'
disclosed_at: '2019-11-17T12:44:47.022Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
tags:
- hackerone
- violation-of-secure-design-principles
---

# Linux Desktop application slack executable does not use pie / no ASLR

## Metadata

- HackerOne Report ID: 415272
- Weakness: Violation of Secure Design Principles
- Program: slack
- Disclosed At: 2019-11-17T12:44:47.022Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The slack binary from the Linux desktop application is no position independent executable:

$ file usr/lib/slack/slack 
usr/lib/slack/slack: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, stripped

(pie executables report either "LSB shared object" or "LSB pie executable".)

Position independent executables are required for full ASLR support on Linux. Non-pie-binaries are loaded to a fixed location, thus allowing ROP attacks.

I'm aware that technically this is not a vulnerability, but a lack of a hardening feature. However given that ASLR is generally considered standard practice these days and that lack of it can mean very simple bugs can directly lead to code execution I think it deserves to be fixed.

## Impact

A simple memory corruption bug like a buffer overflow can easily lead to a remote code execution bug. With ASLR these bugs are much harder and sometimes impossible to exploit.

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

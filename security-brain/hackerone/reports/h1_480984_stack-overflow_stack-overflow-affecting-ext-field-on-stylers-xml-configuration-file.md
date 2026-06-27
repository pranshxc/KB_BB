---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '480984'
original_report_id: '480984'
title: Stack overflow affecting "ext" field on stylers.xml configuration file
weakness: Stack Overflow
team_handle: notepad-plus-plus
created_at: '2019-01-16T15:55:52.607Z'
disclosed_at: '2019-08-25T12:51:14.728Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 51
tags:
- hackerone
- stack-overflow
---

# Stack overflow affecting "ext" field on stylers.xml configuration file

## Metadata

- HackerOne Report ID: 480984
- Weakness: Stack Overflow
- Program: notepad-plus-plus
- Disclosed At: 2019-08-25T12:51:14.728Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

A stack buffer overflow vulnerability affects "ext" field into "stylers.xml" configuration file.

"isInList" function doesn't check boundaries on word[64] array.

**Description:**
Vulnerability src file: notepad-plus-plus/PowerEditor/src/MISC/Common/Common.cpp
Vulnerability line: line 329
Variable affected: TCHAR word[64];

## Steps To Reproduce:

Notice: All this steps have been tested on 32-bits version of Notepad++.

  1. Open "stylers.xml" configuration file (C:\Users\%USERPROFILE%\AppData\Roaming\Notepad++)
  2. Modify "ext" field with a long string, such as "123456789012346789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789" (see ExploitationExample.png)
  3. Close Notepad++ application and re-open it.
  4. Application should crash

## Supporting Material/References:

- ExploitationExample.png -> Exploitation example
- CrashEvidence.png -> Evidence of vulnerability exploitation

## Impact

A local attacker could modify this configuration file to trigger a stack buffer overflow. When the victim re-open Notepad++ vulnerability will be exploited.

It's not a remote vulnerability. Local access to stylers.xml is required.

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

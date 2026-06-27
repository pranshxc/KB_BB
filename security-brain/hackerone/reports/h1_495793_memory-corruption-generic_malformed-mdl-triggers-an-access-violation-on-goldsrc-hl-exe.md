---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '495793'
original_report_id: '495793'
title: Malformed .MDL triggers an Access Violation on GoldSRC (hl.exe)
weakness: Memory Corruption - Generic
team_handle: valve
created_at: '2019-02-14T01:34:41.616Z'
disclosed_at: '2019-10-09T00:01:06.274Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 89
asset_identifier: hl.exe
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- memory-corruption-generic
---

# Malformed .MDL triggers an Access Violation on GoldSRC (hl.exe)

## Metadata

- HackerOne Report ID: 495793
- Weakness: Memory Corruption - Generic
- Program: valve
- Disclosed At: 2019-10-09T00:01:06.274Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A malformed player .MDL triggers an exploitable Access Violation on GoldSRC engine games (Half-Life) upon invocation, which could lead to remote code execution on a client.

###Crash Information
FAILURE_ID_HASH_STRING:  um:invalid_pointer_write_exploitable_c0000005_hw.dll!createinterface
Event Type: Exception
Exception Faulting Address: 0x4c01000
First Chance Exception Type: STATUS_ACCESS_VIOLATION (0xC0000005)
Exception Sub-Type: Write Access Violation

FOLLOWUP_IP: 
hw!CreateInterface+282aa
03a554ea d95efc          fstp    dword ptr [esi-4]

PROBLEM_CLASSES: 

    ID:     [0n309]
    Type:   [@ACCESS_VIOLATION]
    Class:  Addendum
    Scope:  BUCKET_ID
    Name:   Omit
    Data:   Omit
    PID:    [Unspecified]
    TID:    [0x6e30]
    Frame:  [0] : hw!CreateInterface

    ID:     [0n282]
    Type:   [INVALID_POINTER_WRITE]
    Class:  Primary
    Scope:  DEFAULT_BUCKET_ID (Failure Bucket ID prefix)
            BUCKET_ID
    Name:   Add
    Data:   Omit
    PID:    [Unspecified]
    TID:    [0x6e30]
    Frame:  [0] : hw!CreateInterface

    ID:     [0n156]
    Type:   [ZEROED_STACK]
    Class:  Addendum
    Scope:  BUCKET_ID
    Name:   Add
    Data:   Omit
    PID:    [0x300]
    TID:    [0x6e30]
    Frame:  [0] : hw!CreateInterface

    ID:     [0n115]
    Type:   [EXPLOITABLE]
    Class:  Addendum
    Scope:  DEFAULT_BUCKET_ID (Failure Bucket ID prefix)
            BUCKET_ID
    Name:   Add
    Data:   Omit
    PID:    [0x300]
    TID:    [0x6e30]
    Frame:  [0] : hw!CreateInterface

BUGCHECK_STR:  APPLICATION_FAULT_INVALID_POINTER_WRITE_ZEROED_STACK_EXPLOITABLE

###Steps for Reproducing the Crash
Place the attached .MDL in the games "Gman" multiplayer model folder (Steam\steamapps\common\Half-Life\valve\models\player\gman) Load the attached .MDL by setting the player character to "Gman" from the games multiplayer menu. Then, start a local game by typing "map crossfire" in console. Finally, execute the command "thirdperson" in console. The game will crash.

## Impact

An attacker hosting a malicious server could compromise a remote client by having them download a custom model, triggering remote code execution on the victim's computer.

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

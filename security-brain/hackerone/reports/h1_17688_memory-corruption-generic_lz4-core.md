---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17688'
original_report_id: '17688'
title: LZ4 Core
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2014-06-26T20:11:22.416Z'
disclosed_at: '2014-07-25T19:18:39.479Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# LZ4 Core

## Metadata

- HackerOne Report ID: 17688
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2014-07-25T19:18:39.479Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#############################################################################
#
# Lab Mouse Security Report 
# LMS-2014-06-16-6
#

Report ID: LMS-2014-06-16-6
CVE ID: CVE-2014-4611

Researcher Name: Don A. Bailey
Researcher Organization: Lab Mouse Security
Researcher Email: donb at securitymouse.com
Researcher Website: www.securitymouse.com

Vulnerability Status: Reported / No response
Vulnerability Embargo: Broken

Vulnerability Class: Integer Overflow
Vulnerability Effect: Memory Corruption
Vulnerability Impact: DoS, OOW, RCE
Vulnerability DoS Practicality: Practical
Vulnerability OOW Practicality: Practical
Vulnerability RCE Practicality: Untested
Vulnerability Criticality: High

Vulnerability Scope:
All versions of the LZ4 software:
https://code.google.com/p/lz4

Functions Affected:
	lz4.c:LZ4_decompress_generic

Criticality Reasoning
---------------------
Due to the design of the algorithm, an attacker can specify any desired
offset to a write pointer. The attacker can instrument the write in such
a way as to only write four bytes at a specified offset. Subsequent code
will allow the attacker to escape from the decompression algorithm without
further memory corruption. This may allow the attacker to overwrite 
critical structures in memory that affect flow of execution. White DoS
and OOW are obvious side effects of this flaw, RCE with respect to this
flaw is untested. 

Vulnerability Description
-------------------------
An integer overflow can occur when processing any variant of a "literal run"
in the affected function. 

Vulnerability Resolution
------------------------
Pending.

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

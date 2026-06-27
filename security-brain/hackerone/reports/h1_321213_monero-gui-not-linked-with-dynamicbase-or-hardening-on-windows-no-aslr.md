---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321213'
original_report_id: '321213'
title: Monero GUI not linked with /DYNAMICBASE or hardening on windows, no ASLR
team_handle: monero
created_at: '2018-03-01T20:21:49.113Z'
disclosed_at: '2018-03-18T00:46:08.663Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# Monero GUI not linked with /DYNAMICBASE or hardening on windows, no ASLR

## Metadata

- HackerOne Report ID: 321213
- Weakness: 
- Program: monero
- Disclosed At: 2018-03-18T00:46:08.663Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The monero daemon is compiled and linked without ASLR, at least on windows. This security hardening feature should be enabled in order to make exploiting of this service harder.

**Description:** 
See above. 

## Releases Affected:

  * At least v0.11.1.0 (probably more) / Tested on Windows 8.1

## Steps To Reproduce:

  1. Start the monero-gui and monero daemon on windows
  2. Start Process Explorer https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer 
  3. Check ASLR under "select columns"
  4. See that ASLR is not activated for this process.

## Supporting Material/References:

  * I've attached a screenshot of the sysinternals tool on my machine.

## Impact

Exploiting code reuse attacks is alot easier without this feature. 
This might impact future bug bounty payouts because people can't exploit reliable bugs to get code execution :)

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

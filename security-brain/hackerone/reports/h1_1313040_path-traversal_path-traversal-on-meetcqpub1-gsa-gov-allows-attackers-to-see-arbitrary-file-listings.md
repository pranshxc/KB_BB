---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1313040'
original_report_id: '1313040'
title: Path Traversal on meetcqpub1.gsa.gov allows attackers to see arbitrary file
  listings.
weakness: Path Traversal
team_handle: gsa_vdp
created_at: '2021-08-20T09:29:43.682Z'
disclosed_at: '2021-10-02T17:52:52.843Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- path-traversal
---

# Path Traversal on meetcqpub1.gsa.gov allows attackers to see arbitrary file listings.

## Metadata

- HackerOne Report ID: 1313040
- Weakness: Path Traversal
- Program: gsa_vdp
- Disclosed At: 2021-10-02T17:52:52.843Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Path Traversal on meetcqpub1.gsa.gov allows attackers to see arbitrary file listings from a directory of their choice.

I wasn't sure if this page was in scope of this program or the TTS program, hopefully this isn't a problem

## Steps To Reproduce:

  1. Navigate to the following URL - https://meetcqpub1.gsa.gov/bin/querybuilder.json.css?path=/home&p.hits=full&p.limit=-1
  2. The path parameter can be manipulated to show other directories on the system as well, for example /etc.

## Impact

An attacker is able to see files and directories present on the system, breaking the confidentiality section of the CIA Triad.

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

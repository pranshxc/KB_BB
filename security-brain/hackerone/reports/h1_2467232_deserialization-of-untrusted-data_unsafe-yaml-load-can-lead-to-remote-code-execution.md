---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2467232'
original_report_id: '2467232'
title: Unsafe yaml load can lead to remote code execution
weakness: Deserialization of Untrusted Data
team_handle: liberapay
created_at: '2024-04-17T13:32:57.498Z'
disclosed_at: '2024-05-04T11:50:22.497Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 51
asset_identifier: https://github.com/liberapay/liberapay.com
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- deserialization-of-untrusted-data
---

# Unsafe yaml load can lead to remote code execution

## Metadata

- HackerOne Report ID: 2467232
- Weakness: Deserialization of Untrusted Data
- Program: liberapay
- Disclosed At: 2024-05-04T11:50:22.497Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

TL;DR
Yaml.load() has the ability to construct an arbitrary Python object. This is dangerous if you receive a YAML document from an untrusted source.


Proof of concept 
https://github.com/liberapay/liberapay.com/blob/master/liberapay/testing/vcr.py#L40

How do I fix it?
Always use yaml.safe_load(). This function limits this ability to simple Python objects like integers or lists. 

If you have any questions 
please comment on the report 

best regards
mrrobot2050

## Impact

Yaml.load() has the ability to construct an arbitrary Python object. This is dangerous if you receive a YAML document from an untrusted source.

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

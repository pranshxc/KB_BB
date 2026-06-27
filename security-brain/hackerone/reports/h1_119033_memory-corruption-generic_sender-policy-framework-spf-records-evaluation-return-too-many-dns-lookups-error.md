---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119033'
original_report_id: '119033'
title: Sender policy framework (SPF) records evaluation return (Too many DNS lookups)
  error
weakness: Memory Corruption - Generic
team_handle: cakebet
created_at: '2016-02-26T23:17:33.656Z'
disclosed_at: '2016-03-28T11:40:18.862Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- memory-corruption-generic
---

# Sender policy framework (SPF) records evaluation return (Too many DNS lookups) error

## Metadata

- HackerOne Report ID: 119033
- Weakness: Memory Corruption - Generic
- Program: cakebet
- Disclosed At: 2016-03-28T11:40:18.862Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team ,

Your SPF record suffers from a “too many lookups” error.

The specifications for the SPF record limit the number of lookups (such as, translating a name to an IP address) to 10.

An SPF record like what is shown below will have the too many lookup errors :

Found v=spf1 record for cakebet.com: 
v=spf1 mx include:zoho.com include:smtp1.uservoice.com include:amazonses.com include:_spf.google.com ~all 

evaluating...
Results - PermError SPF Permanent Error: Too many DNS lookups

- How to Fix it :
Make the SPF record passed validation test with pySPF (Python SPF library)

Good Fix ,

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

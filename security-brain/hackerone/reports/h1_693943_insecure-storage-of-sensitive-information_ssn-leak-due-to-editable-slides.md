---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '693943'
original_report_id: '693943'
title: SSN leak due to editable slides
weakness: Insecure Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2019-09-12T20:05:50.579Z'
disclosed_at: '2020-05-14T18:09:29.111Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# SSN leak due to editable slides

## Metadata

- HackerOne Report ID: 693943
- Weakness: Insecure Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2020-05-14T18:09:29.111Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
A presentation slide contains a screenshot of a records brief which contains an SSN
**Description:**
The slides try to redact the PII of the records with a blue block but we can remove it by editing the slides to remove the offending blue block
## Impact
Critical 
## Step-by-step Reproduction Instructions
We can see an officer record brief, but the area with the SSN is blocked. We can make a copy of the file and edit it to remove the blue block thus allowing us to see the SSN
https://█████████/wp-content/uploads/2018/03/███████
Slide 84
███████
█████████
## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions

Purge Doc

## Impact

Identity theft

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

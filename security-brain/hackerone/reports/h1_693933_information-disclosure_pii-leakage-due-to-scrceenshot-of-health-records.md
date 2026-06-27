---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '693933'
original_report_id: '693933'
title: PII leakage due to scrceenshot of health records
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2019-09-12T19:28:02.016Z'
disclosed_at: '2019-12-02T20:01:41.364Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- information-disclosure
---

# PII leakage due to scrceenshot of health records

## Metadata

- HackerOne Report ID: 693933
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2019-12-02T20:01:41.364Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Document shows a screenshot of a medical record for a soldier 
**Description:**
One of the slides describes the CIV# and PAD DSN# along with some information relating to the soldier such as their name, the information appears to be old but could be still be an issue if they're in service
## Impact
High? maybe critical? Unsure on impact 
## Step-by-step Reproduction Instructions
Check slide 13 specifically but there's other slides that are suspect too
https://███████/wp-content/uploads/2018/12/HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx

## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Purge Doc

## Impact

An attacker could assume soldier identities and learn more about possible health information related to them

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1063371'
original_report_id: '1063371'
title: Sensitive Information Leaking Through DoD Owned Website https://www.█████.mil
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-12-21T12:43:09.410Z'
disclosed_at: '2021-02-01T17:51:24.665Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- information-disclosure
---

# Sensitive Information Leaking Through DoD Owned Website https://www.█████.mil

## Metadata

- HackerOne Report ID: 1063371
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-02-01T17:51:24.665Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
While checking for some vulnerabilities in dod website I came across this sensitive document which contains sensitive details such as personal mail ids, names, phone numbers, client IP, and address.

**Description:**
The above website is leaking information such as - personal mail ids, names, phone numbers, client IP, and address in a clear readable pdf document. This is a high severity issue and requires immediate fixation. It is also a clear privacy violation and insufficient protection mechanism involved in data storage. I look forward to a satisfactory reply from your side.

These details are a complete collection of all the user's comments, which are accumulated into a single pdf.

## Impact
High 

## Step-by-step Reproduction Instructions
visit this link: https://www.█████████.mil/████

## Suggested Mitigation/Remediation Actions
Remove documents from the internet or put applicable authorization mechanism(s) in order to access sensitive documents.

## Impact

Any person can access this document and cause information leakage, target a specific person for a crime.

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

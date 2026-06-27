---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '806213'
original_report_id: '806213'
title: Sensitive Information Leaking Through DoD Owned Website. [██████████]
weakness: Insufficiently Protected Credentials
team_handle: deptofdefense
created_at: '2020-02-27T15:26:02.190Z'
disclosed_at: '2020-05-11T16:38:08.785Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- insufficiently-protected-credentials
---

# Sensitive Information Leaking Through DoD Owned Website. [██████████]

## Metadata

- HackerOne Report ID: 806213
- Weakness: Insufficiently Protected Credentials
- Program: deptofdefense
- Disclosed At: 2020-05-11T16:38:08.785Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary**
While performing recon work on websites owned by DoD i came up with ██████████ website which is leaking sensitive information.

**Description**
The above website is leaking information such as- first name and last name, email address, phone number, house address and organization name of attendees in a clear readable pdf document. This is a high severity issue and requires immediate fixation. It is also a clear privacy violation and insufficient protection mechanism involved in data storage. I look forward for a satisfactory reply from your side.

**Step-by-step Reproduction Instructions**
1. Open a web browser of your choice.
2.  Now open this URL: https://██████/12038/MyDoD/ngb-sfpd-roster.pdf

**Suggested Mitigation/Remediation Actions**
Remove document from the internet or put applicable authorization mechanism(s) in order to access sensitive documents.

## Impact

1. Any person can access this document and cause information leakage, target specific person for crime.
2. Anyone can threaten ██████ employees to reveal secrets which aren't meant to be public by nature.

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

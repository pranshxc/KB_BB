---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '812585'
original_report_id: '812585'
title: Sensitive Information Leaking Through Navy Website. [█████]
weakness: Cleartext Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2020-03-07T03:32:51.234Z'
disclosed_at: '2020-05-14T17:59:19.800Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Sensitive Information Leaking Through Navy Website. [█████]

## Metadata

- HackerOne Report ID: 812585
- Weakness: Cleartext Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2020-05-14T17:59:19.800Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
 While performing recon work on websites owned by DoD i came up with a Navy website which is leaking sensitive information.

**Description:**
The website is leaking information such as- first name and last name, email address, phone number, location, rank, and other information of trainees in a clear readable pdf document. This is a high severity issue and requires immediate fixation. It is also a clear privacy violation and insufficient protection mechanism involved in data storage.
 
## Step-by-step Reproduction Instructions

1. Open a web browser of your choice.
2. Now open this URL: https://███████/sites/██████/Documents/health-promotion-wellness/reproductive-and-sexual-health/██████████

## Suggested Mitigation/Remediation Actions
Remove document from the internet or put applicable authorization mechanism(s) in order to access sensitive documents.

## Impact

Any person can access this document and cause:
1. Information leakage.
2. Impersonation a person.
3. Commit crimes under a fake identity.

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

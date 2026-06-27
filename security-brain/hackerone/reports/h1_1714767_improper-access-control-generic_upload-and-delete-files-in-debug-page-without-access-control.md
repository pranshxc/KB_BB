---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1714767'
original_report_id: '1714767'
title: Upload and delete files in debug page without access control.
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2022-09-28T02:10:27.836Z'
disclosed_at: '2023-02-24T18:40:53.460Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- improper-access-control-generic
---

# Upload and delete files in debug page without access control.

## Metadata

- HackerOne Report ID: 1714767
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2023-02-24T18:40:53.460Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found a debug page with no access control that allows:
- Uploading files.
- Reading files if they are in JSON format.
- Delete files.

## Impact

- Insufficient access control.
- An attacker can delete files exposed by the application.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
## For upload file:
1. Use a browser to navigate to: https://█████/debug. 
2. Click on choose file button.
3. Set the file path in the location field
4. Click on the upload files button.
5.See the file uploaded on the list.

## For Read File
1. Select the file.
2. Click and Read File Content.
3. See the content file.

## For delete file:
1. Select the file.
2. Click on the Delete ENC Files button.

## Suggested Mitigation/Remediation Actions
- Implement access control on the page.

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

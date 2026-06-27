---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1914115'
original_report_id: '1914115'
title: End-to-end encrypted file-drops can be made inaccessible
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2023-03-21T20:28:56.519Z'
disclosed_at: '2023-06-22T06:13:57.173Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
asset_identifier: nextcloud/end_to_end_encryption
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# End-to-end encrypted file-drops can be made inaccessible

## Metadata

- HackerOne Report ID: 1914115
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2023-06-22T06:13:57.173Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Assume a filedrop that is send to 2 people, USER and ATTACKER

1. user uploads their E2EE encrypted fileA into the filedrop
2. All goes well
3. Now ATTACKER comes along and wants mess up the upload from USER
4. They obtain the metadatafile
5. They modify the entry in the filedrop list that USER created
6. They upload their new metadatafile
7. Unlock it
8. FileA is now not able to be decoded at all anymore.

## Impact

The CIA model (Confidentiality, integrity and availability) is here very easy to break. An attacker can almost trivially in this case break the availability.
Note that due to the nature of providing the metadatafile an attacker can trivially know if there are other filedrop files.

To solve
1. Do not provide the metadata file to the user in file drop at all
2. Only send back the new entry (which they can create without the metadatafile)
3. Append the new entry in the backend code.

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

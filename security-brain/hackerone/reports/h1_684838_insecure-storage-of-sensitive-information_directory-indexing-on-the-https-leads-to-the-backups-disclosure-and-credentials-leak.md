---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '684838'
original_report_id: '684838'
title: Directory Indexing on the ████ (https://████/) leads to the backups disclosure
  and credentials leak
weakness: Insecure Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2019-08-30T04:33:53.534Z'
disclosed_at: '2021-01-12T21:54:20.378Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Directory Indexing on the ████ (https://████/) leads to the backups disclosure and credentials leak

## Metadata

- HackerOne Report ID: 684838
- Weakness: Insecure Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2021-01-12T21:54:20.378Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
During poking around `█████████/24` range -  █████ looking for the Cisco devices, I came across `█████` which resolved to the https://██████/
While it's a not `.mil` host, it's likely related to the DoD since it hosted in the DoD-controlled ASN.

I discovered few critical vulnerabilities here, one of them is exposed backup files via directory listing.

##POC
https://███/obj/Debug/
█████
The source code can be found here:
https://█████████/obj/Debug/Package/GLOSS2.zip
It's zipped backup.

The DB credentials exposed here:
https://█████/obj/Debug/Package/GLOSS2.SetParameters.xml
███

##Suggested fix
Disable directory indexing, restrict access to the sensitive files, and change credentials as defense-in-depth measure.

## Impact

Source code & DB credentials leakage. Attacker can use it to compromise the resource.

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

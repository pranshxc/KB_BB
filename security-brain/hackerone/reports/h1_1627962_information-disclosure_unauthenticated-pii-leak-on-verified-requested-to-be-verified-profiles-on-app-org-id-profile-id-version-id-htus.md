---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1627962'
original_report_id: '1627962'
title: Unauthenticated PII leak on verified/requested to be verified profiles on ███████/app/org/{id}/profile/{id}/version/{id}
  [HtUS]
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2022-07-06T14:00:59.651Z'
disclosed_at: '2022-10-14T17:04:05.583Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# Unauthenticated PII leak on verified/requested to be verified profiles on ███████/app/org/{id}/profile/{id}/version/{id} [HtUS]

## Metadata

- HackerOne Report ID: 1627962
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2022-10-14T17:04:05.583Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
On any published profile page,you can switch between their profile's versions(provided they have made at least 1 change after publication) ,which will make a GET request to **███/organization/{id}/profile{id}/version/{id}**.  
While proxying traffic through Burp Suite,another request is being sent to **████████*/app/org/*{id}/profile{id}/version/{id}** ,which exposes some information about the author such as **id,uuid and name**,BUT if  you switch to the version that is **verified/requested to be verified**,the same endpoint(but with different version id) will return the above info **+ their email**,which adds to the PII disclosure.  
Worst of all,this endpoint can be accessed even by unauthenticated users,and all steps above can be done unauthenticated aswell.  

## References
██████████

## Impact

Any **unauthenticated** person can obtain PII information from any **verified** profile or profiles that have **requested verification**.

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

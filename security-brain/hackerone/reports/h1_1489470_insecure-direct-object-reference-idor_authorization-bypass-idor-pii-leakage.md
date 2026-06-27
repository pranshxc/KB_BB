---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1489470'
original_report_id: '1489470'
title: Authorization bypass -> IDOR -> PII Leakage
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2022-02-23T10:43:07.051Z'
disclosed_at: '2022-04-07T20:02:38.596Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Authorization bypass -> IDOR -> PII Leakage

## Metadata

- HackerOne Report ID: 1489470
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2022-04-07T20:02:38.596Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team!
During testing ████ I found  javascript file containing administrative panel functionality.
It is accessible at: 
https://████/█████████
In this file I found an end point responsible for returning data about applications of the website users to the website administrators.
The returned data contains PII data (Full name, phone and email) of military personnel, and or their family members.


## References
Steps to reproduce:

Run following curl command to retrieve data:
curl https://███/███ -X POST -data="url=%2F████████" -k

Modifying ██████████ parameter result in different Application being returned.
I have tested retrieving following ids: █████.

Trying to retrieve record 60000 returns no information, so maybe ~50000 applications are accessible.

## Impact

PII leak of military personnel and family members

## System Host(s)
█████████

## Affected Product(s) and Version(s)
/█████████

## CVE Numbers


## Steps to Reproduce
Run following command to retrieve data:
curl https://███████/███ -X POST -data="url=%2F████████" -k

Modifying ██████ parameter result in different Application being returned.
I have tested retrieving following ids: ███.
Trying to retrieve record 60000 returns no information, so maybe ~50000 applications are accessible.

## Suggested Mitigation/Remediation Actions
1. admin.js should be available only after Administrator successfully logs in
2. all administrative end points must check if authorized administrator is requesting them

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

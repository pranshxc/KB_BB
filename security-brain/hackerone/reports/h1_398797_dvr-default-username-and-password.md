---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '398797'
original_report_id: '398797'
title: DVR default username and password
team_handle: starbucks
created_at: '2018-08-24T02:54:23.873Z'
disclosed_at: '2018-10-15T22:31:22.866Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
---

# DVR default username and password

## Metadata

- HackerOne Report ID: 398797
- Weakness: 
- Program: starbucks
- Disclosed At: 2018-10-15T22:31:22.866Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
default username and password i found in one of your DVR camera system 

**Description:**
hi
after scanning on starbucks register ip from this site http://bge.he.net
i start to scan the ip subnet : ████
then i found this ip : █████ then i try to browse it then i found login page for DVR cam system
as can see in this picture : 
F337222

then i start to test the default username and password
like user -- user 
then i successfully login to your dvr system and browse you cams as i show in this photo :
F337223
  
## Steps To Reproduce:

  1. scanning in  this ip subnet ███████ and found █████████
  2. browse ███████ and i found web client for DVR system
  1. login by default username and password username : user --- password : user

## Impact

an attacker can control your DVR system and changing setting .. etc

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

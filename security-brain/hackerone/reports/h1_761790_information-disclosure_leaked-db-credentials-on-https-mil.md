---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '761790'
original_report_id: '761790'
title: Leaked DB credentials on https://██████████.mil/███
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2019-12-19T16:19:47.238Z'
disclosed_at: '2020-12-03T21:32:20.836Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 42
tags:
- hackerone
- information-disclosure
---

# Leaked DB credentials on https://██████████.mil/███

## Metadata

- HackerOne Report ID: 761790
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2020-12-03T21:32:20.836Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Information disclosure with login credentials for ms-sql database exposed. 

**Description:**
I've found a PHP info file disclosed on https://█████.mil/██████ containing login credentials for a database cloud server (███████) as well as information on the host system such as hostname, username and full paths. The database server is up, but I have not tried connecting to it with the credentials, as I feel that would be going too far. 

## Impact
Possible access to database as well as disclosure of sensitive host information. 

## Step-by-step Reproduction Instructions

1. Go to https://██████████.mil/████████
2. Search for 'password', you should see this: 
    `Data Source=tcp:███,█████████;Initial Catalog=██████████;User  Id=████@██████████;Password=███████ `
3. Run `nc -vvv █████████ █████` to confirm database is running and service ms-sql-s is accepting connections: 
`(UNKNOWN) [███████] ████████ (ms-sql-s) open
^C sent 0, rcvd 0
`

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions
███████ should not be available on the server.

## Impact

Possible access to database as well as disclosure of sensitive host information.

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

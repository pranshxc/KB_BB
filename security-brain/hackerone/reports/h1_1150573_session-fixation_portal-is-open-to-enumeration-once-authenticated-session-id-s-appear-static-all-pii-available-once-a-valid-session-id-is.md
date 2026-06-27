---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1150573'
original_report_id: '1150573'
title: ████████ portal is open to enumeration once authenticated.  Session ID's appear
  static.  All PII available once a valid session ID is found.
weakness: Session Fixation
team_handle: deptofdefense
created_at: '2021-04-05T20:10:54.673Z'
disclosed_at: '2021-04-20T19:33:36.076Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- session-fixation
---

# ████████ portal is open to enumeration once authenticated.  Session ID's appear static.  All PII available once a valid session ID is found.

## Metadata

- HackerOne Report ID: 1150573
- Weakness: Session Fixation
- Program: deptofdefense
- Disclosed At: 2021-04-20T19:33:36.076Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Once Authenticated to █████████ portal with valid credentials you can type in another members session id and you can see any service members data as if you were authenticated as them.

https://█████████

I did not see if there was a way to dump all session id's, but wouldn't be too surprised if it was vulnerable to this.

## References

Replacing that string above with valid session ID's let me see ██████ info

## Impact

All PII held in ██████████ portal exposed.  █████████.  
If website doesn't stop me, I could either dump the list of id's or utilize a tool to brute force a range.

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Step 1: Authenticate to █████████ portal with valid credentials. 
Step 2:  navigate straight to this page with a valid session id
https://████████
If you have a valid session id, you can see any service members data as if you were authenticated as them.

## Suggested Mitigation/Remediation Actions
random session ids.  better authorization to data.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1723896'
original_report_id: '1723896'
title: Sql Injection At █████████
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2022-10-05T22:29:42.816Z'
disclosed_at: '2023-01-06T19:02:47.214Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- sql-injection
---

# Sql Injection At █████████

## Metadata

- HackerOne Report ID: 1723896
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2023-01-06T19:02:47.214Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Hi Security Team I Hope You Are Doing Well 

Sql Injection is a common attack vector that uses malicious SQL code for backend database manipulation to access information that was not intended to be displayed.


1: Visit This Endpoint ``  https://█████/ `` As You Can See This Website Using Asp.net That's Mean To Os Equal Windows.
2: Visit This Endpoint `` https://█████/ProductMaps/PubForm/Details.aspx?PUB_ID=4568 `` As You Experienced  Sometimes To Check The Parameters Put``  '  `` To Know Vulnerable Or Not , If You Put `` ' `` In This Request As `` https://████████/ProductMaps/PubForm/Details.aspx?PUB_ID=4568' `` The Response Said Invalid Request Means To Maybe Vulnerable.
3: So I Decided To Sure That This Endpoint Vulnerable To Sql Injection  Or Not , I Using Sqlmap As You Can See In My PoC Video.

## References

███

## Impact

The impact SQL injection can have on a business is far-reaching. A successful attack may result in the unauthorized viewing of user lists, the deletion of entire tables and, in certain cases, the attacker gaining administrative rights to a database, all of which are highly detrimental to a business.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1: Visit This Endpoint ``  https://███████/ `` As You Can See This Website Using Asp.net That's Mean To Os Equal Windows.
2: Visit This Endpoint `` https://██████/ProductMaps/PubForm/Details.aspx?PUB_ID=4568 `` As You Experienced  Sometimes To Check The Parameters Put``  '  `` To Know Vulnerable Or Not , If You Put `` ' `` In This Request As `` https://██████/ProductMaps/PubForm/Details.aspx?PUB_ID=4568' `` The Response Said Invalid Request Means To Maybe Vulnerable.
3: So I Decided To Sure That This Endpoint Vulnerable To Sql Injection  Or Not , I Using Sqlmap As You Can See In My PoC Video.


Thanks And King Regards

## Suggested Mitigation/Remediation Actions

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

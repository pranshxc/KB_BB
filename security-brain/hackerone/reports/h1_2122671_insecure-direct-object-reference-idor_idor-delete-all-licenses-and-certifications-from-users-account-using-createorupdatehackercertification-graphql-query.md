---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2122671'
original_report_id: '2122671'
title: IDOR - Delete all Licenses and certifications from users account using CreateOrUpdateHackerCertification
  GraphQL query
weakness: Insecure Direct Object Reference (IDOR)
team_handle: security
created_at: '2023-08-24T15:52:11.214Z'
disclosed_at: '2023-08-29T14:30:10.014Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 275
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR - Delete all Licenses and certifications from users account using CreateOrUpdateHackerCertification GraphQL query

## Metadata

- HackerOne Report ID: 2122671
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: security
- Disclosed At: 2023-08-29T14:30:10.014Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hey team,

While editing our **Licenses and certifications** if we change the ID number we can delete other users **Licenses and certifications**. it simply can be done by editing the ID number in our graphql query.
If change the ID from 1 to X possible range then we can delete all the **Licenses and certifications** present between these.


### Steps To Reproduce

1. Log in to your own account in two browsers A and B with User A and User B
2. Create your own **Licenses and certifications* in both the account
3. Now edit your own **Licenses and certifications* and Intercept this using a Burp Proxy 
4. Now In the body change the **ID** number and you will be able to delete all the **Licenses and certifications** present in HackerOne 
5. For now change the ID to the **Licenses and certifications** ID of the Other account and it will be deleted.

PoC Video: ████

## Impact

Able to delete all the **Licenses and certifications** present in HackerOne

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

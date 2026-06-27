---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1061292'
original_report_id: '1061292'
title: TAMS registration details API for admins open at https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/
weakness: Insecure Direct Object Reference (IDOR)
team_handle: gsa_vdp
created_at: '2020-12-18T02:32:53.180Z'
disclosed_at: '2021-05-07T04:45:11.155Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 44
asset_identifier: tams.gsa.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# TAMS registration details API for admins open at https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/

## Metadata

- HackerOne Report ID: 1061292
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: gsa_vdp
- Disclosed At: 2021-05-07T04:45:11.155Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
TAMS administrators are supposed to approve or deny all registration requests. The dashboard that shows these administrators details of a registration request calls the endpoint `https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/(REGISTRATION_ID)`, where `(REGISTRATION_ID)` is numeric.

This endpoint will, without authentication, return the email, address, phone, attachment IDs, address, corporate info, and user roles. It will also return their request status and denial reason if applicable.

Attachments can then be viewed unauthenticated through `https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/(ATTACHMENT_ID)`.

## Steps To Reproduce:

  1. Navigate to the following URL: https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/2634
  2. For attachments, navigate to the following URL: https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/600

## Recommended Mitigation:
Only allow users with valid JWT tokens for the admin role view these two endpoints.

## Impact

An unauthorized attacker can view personal information about contractors and employees gaining access to TAMS.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '77076'
original_report_id: '77076'
title: GA code not verified on the server side allows sending Verification Documents
  on behalf of another user
weakness: Improper Authentication - Generic
team_handle: enter
created_at: '2015-07-20T20:42:07.571Z'
disclosed_at: '2015-11-27T06:28:47.665Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# GA code not verified on the server side allows sending Verification Documents on behalf of another user

## Metadata

- HackerOne Report ID: 77076
- Weakness: Improper Authentication - Generic
- Program: enter
- Disclosed At: 2015-11-27T06:28:47.665Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Host**
api.romit.io

**Endpoint**
/v0/cash/auth/login/verify

**Issue**
The GA Code is not verified on the server side for the users whose "Verification application" has been DENIED by the Romit support Team

**PoC**

1.    Setup an account at app.romit.io, use your apiKey, apiSecret and Location-ID to setup.
2.   Now click on Send Money, add the Phone Number and PIN of an account whose verification application has been denied once.
3.   You are prompted for GA code, enter any code. The server reponds with the following message `
{
  "success" : true,
  "error" : null,
  "response" : {
    "kioskEnrollmentStatusType" : "DENIED"
  }
}`
and prompted with this message on the UI [see image resubmit.png]
4. You are prompted to take an image of your ID and your image.
5. These documents are then saved on the server side.

Thanks
crab

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

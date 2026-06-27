---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1048540'
original_report_id: '1048540'
title: IDOR on https://██████ via POST UID enables database scraping
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2020-12-01T23:05:29.376Z'
disclosed_at: '2021-04-08T18:50:37.284Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR on https://██████ via POST UID enables database scraping

## Metadata

- HackerOne Report ID: 1048540
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2021-04-08T18:50:37.284Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The UID parameter on █████████ in the ██████ (███████) system, with ███████, does not validate that the caller has permission to view information on the UID entered, thereby enabling personnel and student data extraction.

**Description:**
The user operations API endpoint for the ███ (██████████) is ███. It is used for login, forgot password, and administrators viewing user information.

Unfortunately, this endpoint lacks basic security precautions, the most serious of which appears to enable database scraping via ███ (I assume this is for ████████).

By entering sequential and numerical user IDs via the UID parameter, an unauthenticated and unauthorized external attacker can scrape the ████████ database's emails, ████ info, ████████ scores, and first & last names.

## Impact
An unauthenticated, unauthorized external attacker can obtain the full names, emails, military branches, and ████ scores of all users registered in the █████ (███) system.

## Step-by-step Reproduction Instructions

1. Run the following cURL command: `curl 'https://███'  --data-raw 'sendingForm=██████' `

2. Success.

## Other Notes
This ██████████ endpoint appears extremely insecure in general. There is a very verbose ASPX error if you enter sendingForm with any number greater than ██████ and don't specify a UID. There is a null user/UID in the system with UID █████████, which will be matched against whenever not entering a parameter (i.e. excluding "un" and "pn" during login on ███).

I suspect more damage is possible with this endpoint, but as I have already unintentionally and accidentally extracted information on UID █████████(which is not me), I am reporting the vulnerability now and ceasing penetration █████████ing against the endpoint.

## Suggested Mitigation/Remediation Actions
1. Ensure that sendingForm type ████████ can only be utilized by logged in administrative users.
2. Ensure that a null parameter in any form does not evaluate to "true" (so only specifying a username without a password does not lead to a successful login).
████████. Disable ASP verbose error generation.
4. Given how central ████ appears to be, and that it contains information on tens of thousands of students, perform an audit of the source code. It does not appear to use any best practices.

## Impact

An unauthenticated, unauthorized external attacker can obtain the full names, emails, military branches, and █████ scores of all users registered in the ███ (███) system.

An adversarial intelligence agency could obtain information on students participating in DOD ██████ instructional programs.

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

---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '359290'
original_report_id: '359290'
title: LDAP Injection at ██████
weakness: LDAP Injection
team_handle: deptofdefense
created_at: '2018-05-29T13:21:41.942Z'
disclosed_at: '2019-12-02T19:05:49.524Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- ldap-injection
---

# LDAP Injection at ██████

## Metadata

- HackerOne Report ID: 359290
- Weakness: LDAP Injection
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:05:49.524Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An LDAP Injection has been found at the mentioned domain

**Description:**
While performing a user registration, is it possible to edit the request and inject invalid characters, resulting in a LDAP injection

## Step-by-step Reproduction Instructions
1. Visit page https://█████████/Registration/Home/New
2. Start a new registration process with "regular" data
3. The request is correctly processes  
4. Start a new registration process and use a double quote as first name
5. You will get a fatal error

Attached you can find the rogue request and the screenshot of the fatal error.  
Error `0x80005000` is specific of LDAP, this means that the application is trying to handle user data without sanitizing it

## Suggested Mitigation/Remediation Actions
Application should sanitize **all** user input before trying to store it in any way.

## Impact

Attacker could enumerate current domain or exfiltrate data.  
On more practical terms, since user should be manually validated, attacker could bypass such activation.
That's a serious threat, because all requests must be approved and verified by other US Officers.

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
